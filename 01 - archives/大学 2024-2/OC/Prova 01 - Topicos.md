## Questao 1
*Organizacao X Arquitetura de processadores*

### Arquitetura
A arquitetura de um processador diz respeito a **tudo o que o programador vê**, ou seja, é a visão abstrata que o programador tem do sistema. 
**Aspectos Incluídos:**
- Funcionamento das instruções
- Número de bits suportados
- Tipos de dados manipulados
- Métodos de manipulação dos dados

**Exemplos de Arquitetura:**
- x86
- ARM
- MIPS

### Organização
A organização de um processador se refere ao **aspecto físico** do processador, isto é, **como os componentes estão dispostos internamente e fisicamente**. 

**Aspectos Incluídos:**
- Unidade Lógica e Aritmética (ALU)
- Memória cache
- Design de barramento

**Observação:** A organização se preocupa com a implementação física dos componentes, ao contrário da arquitetura, que é uma visão mais lógica e voltada para o programador.


*O que influencia o CPI de um programa*
*O que influencia o tempo de execucao* 
### CPI (Ciclos por Instrução)
O **CPI (Cycles Per Instruction)** mede a quantidade média de ciclos necessários para executar cada instrução de um programa. Ele é influenciado por diversos fatores, incluindo:

- **Tipo de Instruções**: Diferentes instruções requerem diferentes números de ciclos. Por exemplo, instruções de multiplicação geralmente exigem mais ciclos do que instruções de soma.
- **Organização do Processador**: Componentes como cache, pipeline e unidade de execução paralela podem afetar o CPI. 
- **Estrutura de Pipeline**: Processadores com pipelines mais eficientes podem reduzir o CPI ao permitir que várias instruções sejam executadas simultaneamente.
- **Dependências entre Instruções**: Dependências de dados (data hazards) e controle (control hazards) podem impactar o CPI, pois podem introduzir ciclos de espera.

### Tempo de Execução
O **tempo de execução** de um programa depende de múltiplos fatores, incluindo o CPI, frequência do processador e quantidade total de instruções. 

**Fatores que Influenciam o Tempo de Execução:**
- **Número Total de Instruções**: Programas com mais instruções tendem a ter tempos de execução mais longos, assumindo que o CPI e a frequência se mantenham constantes.
- **CPI Médio**: Quanto menor o CPI médio, menor o número de ciclos necessários para executar o programa, o que reduz o tempo de execução.
- **Frequência do Processador**: Processadores com frequência mais alta executam ciclos em menor tempo, reduzindo o tempo total de execução.
---



### Questao 2
Ver um programa em assembly e saber o que ele faz

*Indicar quais instrucoes pertencem a qual tipo, sendo Tipo R,I,S*
[[Tipos de Instrucoes]]


*Explicar o que são pseudo-instrucoes e como exemplos*

**Pseudo-instruções** são instruções que não são diretamente executadas pelo processador. Elas são usadas para facilitar a escrita e leitura do código, ajudando o compilador ou montador a traduzir essas instruções para uma sequência equivalente de instruções reais do processador. 

Essas instruções são "pseudo" porque não correspondem a instruções reais na arquitetura do processador. Em vez disso, elas são convertidas em uma ou mais instruções que o processador consegue entender
**Ex: .data, .text**
### Objetivo das Pseudo-Instruções
As pseudo-instruções auxiliam o programador em várias tarefas, incluindo:

- **Definir a localização de variáveis e constantes** no código.
- **Simplificar operações complexas**, transformando-as em sequências mais intuitivas de escrever.
- **Facilitar operações de controle de fluxo** e manipulação de dados.



---
### Questao 3
Numeros binarios em complemente de 2
 - saber quais numeros sao e o raciocino
 - Multiplicar os dois numeros binarios, empregando um algoritmo aprendido em sala

### Questao 4
Saber numero ponto flutuante
Representar no formato cientifico normalizado (sinal-fracao-potencia) e no formato de ponto flutuante
Multiplicacao
Mostrar valores em ponto flutuante que geram overflow e underflow
