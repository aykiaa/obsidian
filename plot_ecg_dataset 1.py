#!/usr/bin/env python
# coding: utf-8

# In[10]:


import wfdb
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.patches as mpatches

# Configurações
pasta_dados = "/scratch/guilherme.evangelista/ECG-Segmentation/1.0.1/data"  # Caminho da sua pasta
record_number = '1'  # Número do registro (1 a 200)
lead = 'i'  # Escolha a derivação (ex: 'ii', 'v1', 'avf', etc)
sampfrom = 0  # Início da amostra
sampto = 5000  # 10 segundos * 500 Hz = 5000 amostras

# Caminho completo para o registro
caminho_registro = os.path.join(pasta_dados, record_number)

# 1. Listar os arquivos disponíveis para verificar a estrutura
print(f"Verificando arquivos disponíveis na pasta {pasta_dados}:")
try:
    arquivos = os.listdir(pasta_dados)
    arquivos_relacionados = [arq for arq in arquivos if arq.startswith(record_number + '.')]
    print(f"Arquivos encontrados para o registro {record_number}:")
    for arq in arquivos_relacionados:
        print(f"  - {arq}")
except Exception as e:
    print(f"Erro ao listar arquivos: {e}")

# 2. Carregar o sinal ECG de forma correta para o formato LUDB
try:
    # Carregue todas as derivações e depois selecione a específica
    record = wfdb.rdrecord(caminho_registro)
    print(f"Sinal ECG carregado com sucesso: {len(record.p_signal)} amostras")
    print(f"Derivações disponíveis: {record.sig_name}")
    
    # Encontre o índice da derivação desejada
    if lead in record.sig_name:
        lead_index = record.sig_name.index(lead)
        print(f"Índice da derivação {lead}: {lead_index}")
        
        # Extraia apenas a derivação desejada
        sinal_ecg = record.p_signal[:, lead_index]
    else:
        print(f"Derivação {lead} não encontrada. Usando a primeira derivação disponível.")
        sinal_ecg = record.p_signal[:, 0]
        lead = record.sig_name[0]
    
    # Aplicar janela de amostras se especificado
    if sampto > 0:
        sinal_ecg = sinal_ecg[sampfrom:sampto]
        
    print(f"Sinal ECG extraído: {len(sinal_ecg)} amostras")
    
except Exception as e:
    print(f"Erro ao carregar o sinal ECG: {e}")
    # Tente um método alternativo para carregar os dados
    try:
        print("Tentando método alternativo para carregar o sinal...")
        header = wfdb.rdheader(caminho_registro)
        print(f"Informações do cabeçalho: {header.__dict__}")
        
        # Tente carregar uma derivação específica
        record_especifico = wfdb.rdrecord(
            caminho_registro,
            channels=[0],  # Use o primeiro canal disponível
            physical=True
        )
        sinal_ecg = record_especifico.p_signal.flatten()
        print(f"Sinal ECG carregado com método alternativo: {len(sinal_ecg)} amostras")
    except Exception as e2:
        print(f"Também falhou o método alternativo: {e2}")
        print("Não foi possível carregar o sinal ECG.")
        exit()

# 3. Carregar anotações para a derivação escolhida
try:
    annotations = wfdb.rdann(
        caminho_registro,
        extension=lead,
        sampfrom=sampfrom,
        sampto=sampto if sampto > 0 else None,
        return_label_elements=['symbol']
    )
    anotacoes_encontradas = True
    print(f"Anotações carregadas com sucesso da extensão '{lead}'!")
    print(f"Número de anotações: {len(annotations.sample)}")
    print(f"Símbolos de anotação únicos: {set(annotations.symbol)}")
    
    # Imprimir as anotações originais para verificação
    print("\nAnotações originais carregadas:")
    for i, (samp, symb) in enumerate(zip(annotations.sample, annotations.symbol)):
        print(f"  [{i}] Amostra: {samp}, Símbolo: '{symb}'")
    
except Exception as e:
    print(f"Erro ao carregar anotações com extensão '{lead}': {e}")
    anotacoes_encontradas = False

# 4. Criar vetor de tempo para o eixo x
amostras = np.arange(len(sinal_ecg))

# 5. Preparar para colorir o traçado
plt.figure(figsize=(15, 5))

# Definir cores para cada tipo de anotação
cores = {
    'p': 'green',      # Cor para ondas P
    'N': 'red',        # Cor para complexos QRS
    't': 'blue',       # Cor para ondas T
    'baseline': 'gray' # Cor para linha de base (traçado normal)
}

# Mapeamento de rótulos para texto na legenda
texto_rotulo = {
    'p': 'Onda P',
    'N': 'Complexo QRS', 
    't': 'Onda T',
    'baseline': 'Linha de Base'
}

# Dicionário para armazenar intervalos de anotações
intervalos = {
    'p': [],  # Intervalos de ondas P
    'N': [],  # Intervalos de complexos QRS
    't': []   # Intervalos de ondas T
}

# Contador para verificar anotações processadas
anotacoes_processadas = 0

# Se encontrou anotações, processe-as
if anotacoes_encontradas:
    marcacoes = annotations.sample
    rotulos = annotations.symbol
    
    # Ajustar índices das marcações conforme a janela de amostras
    if sampfrom > 0:
        marcacoes_originais = marcacoes.copy()
        rotulos_originais = rotulos.copy()
        
        marcacoes = [m - sampfrom for m in marcacoes if sampfrom <= m < sampto]
        rotulos = [r for i, r in enumerate(rotulos) if sampfrom <= annotations.sample[i] < sampto]
        
        print(f"\nAjuste realizado: {len(marcacoes_originais)} anotações originais -> {len(marcacoes)} após janelamento")
    
    # Procurar pares de início e fim de cada tipo de anotação
    inicio_atual = None
    tipo_atual = None
    sequencia_esperada = []  # Para verificar se alguma anotação está sendo pulada
    
    print("\nProcessando anotações para encontrar intervalos:")
    for i, (samp, lbl) in enumerate(zip(marcacoes, rotulos)):
        print(f"  Processando anotação {i}: Amostra {samp}, Símbolo '{lbl}'")
        
        if 0 <= samp < len(sinal_ecg):  # Verificar se está dentro dos limites
            if lbl == '(' and tipo_atual is None:  # Início de uma anotação
                inicio_atual = samp
                print(f"    - Encontrado início de anotação na amostra {inicio_atual}")
                sequencia_esperada.append('tipo')
                continue
            
            if lbl in ['p', 'N', 't'] and inicio_atual is not None:
                tipo_atual = lbl
                print(f"    - Definido tipo da anotação: '{tipo_atual}'")
                sequencia_esperada.append('fim')
                continue
                
            if lbl == ')' and inicio_atual is not None and tipo_atual is not None:
                fim_atual = samp
                # Adicionar intervalo ao dicionário correspondente
                if tipo_atual in intervalos:
                    intervalos[tipo_atual].append((inicio_atual, fim_atual))
                    print(f"    - Intervalo completo: Tipo '{tipo_atual}', Início {inicio_atual}, Fim {fim_atual}")
                    print(f"      * Pontos abrangidos: {list(range(inicio_atual, fim_atual+1))}")
                    anotacoes_processadas += 3  # Contabiliza as 3 anotações processadas (início, tipo, fim)
                inicio_atual = None
                tipo_atual = None
                sequencia_esperada = []
                continue
        else:
            print(f"    - Anotação fora dos limites do sinal, ignorando")
    
    # Verificar anotações incompletas
    if inicio_atual is not None or tipo_atual is not None:
        print(f"\nALERTA: Sequência de anotação incompleta detectada!")
        print(f"  Início atual: {inicio_atual}, Tipo atual: {tipo_atual}")
        print(f"  Sequência esperada: {sequencia_esperada}")
    
    # Verificar se todas as anotações foram processadas
    if anotacoes_processadas != len(marcacoes):
        print(f"\nALERTA: Nem todas as anotações foram processadas!")
        print(f"  Total de anotações: {len(marcacoes)}")
        print(f"  Anotações processadas: {anotacoes_processadas}")
        print(f"  Possível perda de {len(marcacoes) - anotacoes_processadas} anotações")
    
    # Imprimir resumo dos intervalos encontrados
    print("\nResumo dos intervalos encontrados:")
    for tipo, lista_intervalos in intervalos.items():
        print(f"  Tipo '{tipo}' ({len(lista_intervalos)} intervalos):")
        for i, (inicio, fim) in enumerate(lista_intervalos):
            print(f"    [{i}] Início: {inicio}, Fim: {fim}, Duração: {fim-inicio+1} amostras")
            print(f"        Pontos: {list(range(inicio, fim+1))}")

# Criar um array para armazenar a cor de cada ponto do sinal
cores_por_ponto = ['baseline'] * len(sinal_ecg)

# Preencher o array de cores com base nas anotações
for tipo, lista_intervalos in intervalos.items():
    for inicio, fim in lista_intervalos:
        for i in range(inicio, fim+1):
            if 0 <= i < len(cores_por_ponto):
                cores_por_ponto[i] = tipo

# Plotar o ECG com cores diferentes por segmento
segmento_atual = cores_por_ponto[0]
inicio_segmento = 0

# Percorrer todos os pontos do sinal
for i in range(1, len(sinal_ecg) + 1):
    # Se mudou o segmento ou é o final do sinal
    if i == len(sinal_ecg) or cores_por_ponto[i] != segmento_atual:
        # Plotar o segmento atual
        x = amostras[inicio_segmento:i]
        y = sinal_ecg[inicio_segmento:i]
        if len(x) > 0:
            plt.plot(x, y, color=cores[segmento_atual], linewidth=1.5)
        
        # Preparar para o próximo segmento
        if i < len(sinal_ecg):
            segmento_atual = cores_por_ponto[i]
            inicio_segmento = i

# Adicionar uma legenda única com descrição das cores
legend_patches = []
for tipo in ['p', 'N', 't', 'baseline']:
    if tipo in cores:
        patch = mpatches.Patch(color=cores[tipo], label=texto_rotulo[tipo])
        legend_patches.append(patch)

plt.legend(handles=legend_patches, loc='upper right')

plt.title(f'Registro {record_number} - Derivação {lead.upper()} com Traçado Colorido')
plt.xlabel('Amostras')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.tight_layout()

# Salve o gráfico
#plt.savefig(f'ecg_record_{record_number}_{lead}_colored.png', dpi=300, bbox_inches='tight')
print(f"Gráfico salvo como ecg_record_{record_number}_{lead}_colored.png")

# Mostre o gráfico
plt.show()


# In[11]:


import wfdb
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.patches as mpatches
from scipy import signal

# Configurações
pasta_dados = "/scratch/guilherme.evangelista/ECG-Segmentation/1.0.1/data"
record_number = '1'
lead = 'ii'
original_fs = 500  # Original sampling frequency
target_fs = 400    # Target sampling frequency
target_length = 4096  # Target length in samples

# Verificar arquivos disponíveis na pasta
print(f"Verificando arquivos disponíveis na pasta {pasta_dados}:")
arquivos = [f for f in os.listdir(pasta_dados) if f.startswith(record_number)]
print(f"Arquivos encontrados para o registro {record_number}:")
for arquivo in sorted(arquivos):
    print(f"  - {arquivo}")

# Calculate required original samples to get 4096 points after resampling
# Using the ratio of sampling rates to determine original samples needed
original_samples_needed = int(target_length * (original_fs / target_fs))
sampfrom = 0
sampto = original_samples_needed

# Caminho completo para o registro
caminho_registro = os.path.join(pasta_dados, record_number)

# Carregar o sinal ECG
try:
    record = wfdb.rdrecord(caminho_registro)
    print(f"Sinal ECG carregado com sucesso: {len(record.p_signal)} amostras")
    
    # Listar derivações disponíveis
    print(f"Derivações disponíveis: {record.sig_name}")
    
    # Encontre o índice da derivação desejada
    if lead in record.sig_name:
        lead_index = record.sig_name.index(lead)
        print(f"Índice da derivação {lead}: {lead_index}")
        sinal_ecg = record.p_signal[:, lead_index]
    else:
        sinal_ecg = record.p_signal[:, 0]
        lead = record.sig_name[0]
    
    print(f"Sinal ECG extraído: {len(sinal_ecg)} amostras")
    
    # Aplicar janela de amostras
    sinal_ecg = sinal_ecg[sampfrom:sampto]
    
    # Resample the signal from 500Hz to 400Hz
    num_samples = int(len(sinal_ecg) * (target_fs / original_fs))
    sinal_ecg_resampled = signal.resample(sinal_ecg, num_samples)
    
    # Ensure exactly 4096 points (no padding, only trimming if necessary)
    if len(sinal_ecg_resampled) > target_length:
        sinal_ecg_resampled = sinal_ecg_resampled[:target_length]
    
    # Update target_length to match the actual length if no padding
    if len(sinal_ecg_resampled) < target_length:
        target_length = len(sinal_ecg_resampled)
        print(f"Ajustando comprimento alvo para {target_length} amostras (sem padding)")
    
except Exception as e:
    print(f"Erro ao carregar o sinal ECG: {e}")
    exit()

# Carregar anotações
try:
    annotations = wfdb.rdann(
        caminho_registro,
        extension=lead,
        sampfrom=sampfrom,
        sampto=sampto
    )
    anotacoes_encontradas = True
    print(f"Anotações carregadas com sucesso da extensão '{lead}'!")
    print(f"Número de anotações: {len(annotations.sample)}")
    
    # Imprimir símbolos de anotação únicos
    simbolos_unicos = set(annotations.symbol)
    print(f"Símbolos de anotação únicos: {simbolos_unicos}")
    print()
    
    # Imprimir anotações carregadas
    print("Anotações originais carregadas:")
    for i, (samp, lbl) in enumerate(zip(annotations.sample, annotations.symbol)):
        print(f"  [{i}] Amostra: {samp}, Símbolo: '{lbl}'")
    print()
    
    # Adjust annotation sample points for new sampling rate
    adjusted_samples = np.array(annotations.sample) * (target_fs / original_fs)
    annotations.sample = np.round(adjusted_samples).astype(int)
    
except Exception as e:
    print(f"Erro ao carregar anotações: {e}")
    anotacoes_encontradas = False

# Criar vetor de tempo para o eixo x (ajustado para o tamanho real)
amostras = np.arange(target_length)

# Plotting setup
plt.figure(figsize=(15, 5))

cores = {
    'p': 'green',
    'N': 'red',
    't': 'blue',
    'baseline': 'gray'
}

texto_rotulo = {
    'p': 'Onda P',
    'N': 'Complexo QRS', 
    't': 'Onda T',
    'baseline': 'Linha de Base'
}

intervalos = {
    'p': [],
    'N': [],
    't': []
}

# Process annotations
if anotacoes_encontradas:
    inicio_atual = None
    tipo_atual = None
    
    print("Processando anotações para encontrar intervalos:")
    
    for i, (samp, lbl) in enumerate(zip(annotations.sample, annotations.symbol)):
        print(f"  Processando anotação {i}: Amostra {samp}, Símbolo '{lbl}'")
        
        if 0 <= samp < target_length:
            if lbl == '(':
                inicio_atual = samp
                print(f"    - Encontrado início de anotação na amostra {samp}")
            elif lbl in ['p', 'N', 't'] and inicio_atual is not None:
                tipo_atual = lbl
                print(f"    - Definido tipo da anotação: '{tipo_atual}'")
            elif lbl == ')' and inicio_atual is not None and tipo_atual is not None:
                fim_atual = samp
                if tipo_atual in intervalos:
                    intervalos[tipo_atual].append((inicio_atual, fim_atual))
                    print(f"    - Intervalo completo: Tipo '{tipo_atual}', Início {inicio_atual}, Fim {fim_atual}")
                    # Exibir detalhes dos pontos
                    pontos = list(range(inicio_atual, fim_atual + 1))
                    print(f"      * Pontos abrangidos: {pontos}")
                inicio_atual = None
                tipo_atual = None

# Imprimir resumo dos intervalos encontrados
print("\nResumo dos intervalos encontrados:")
for tipo, lista_intervalos in intervalos.items():
    print(f"  Tipo '{tipo}' ({len(lista_intervalos)} intervalos):")
    for i, (inicio, fim) in enumerate(lista_intervalos):
        print(f"    [{i}] Início: {inicio}, Fim: {fim}, Duração: {fim - inicio + 1} amostras")
        pontos = list(range(inicio, fim + 1))
        print(f"        Pontos: {pontos}")

# Create color array
cores_por_ponto = ['baseline'] * target_length

# Fill colors based on annotations
for tipo, lista_intervalos in intervalos.items():
    for inicio, fim in lista_intervalos:
        for i in range(inicio, fim+1):
            if 0 <= i < target_length:
                cores_por_ponto[i] = tipo

# Plot the signal
segmento_atual = cores_por_ponto[0]
inicio_segmento = 0

for i in range(1, target_length + 1):
    if i == target_length or cores_por_ponto[i] != segmento_atual:
        x = amostras[inicio_segmento:i]
        y = sinal_ecg_resampled[inicio_segmento:i]
        if len(x) > 0:
            plt.plot(x, y, color=cores[segmento_atual], linewidth=1.5)
        
        if i < target_length:
            segmento_atual = cores_por_ponto[i]
            inicio_segmento = i

# Add legend
legend_patches = [mpatches.Patch(color=cores[tipo], label=texto_rotulo[tipo]) 
                 for tipo in ['p', 'N', 't', 'baseline'] if tipo in cores]
plt.legend(handles=legend_patches, loc='upper right')

plt.title(f'Registro {record_number} - Derivação {lead.upper()} ({target_fs}Hz, {target_length} pontos)')
plt.xlabel('Amostras')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.tight_layout()

# Save and show the plot
output_filename = f'ecg_record_{record_number}_{lead}_{target_fs}hz_{target_length}.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"Gráfico salvo como {output_filename}")
plt.show()


# In[12]:




