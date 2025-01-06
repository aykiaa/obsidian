  

# **Prova 1**

### **Questão 1 (Hazards em Processadores com Pipeline)**

1. **Tipos de Hazards**:

• Hazard de dados: quando uma instrução depende do resultado de outra.

• Hazard de controle: relacionado a desvios e instruções condicionais.

• Hazard estrutural: compartilhamento de recursos entre instruções.

2. **Geração de código com hazards**:

• Saiba escrever trechos de código que causem hazards e identificar os pontos onde ocorrerão stalls ou bolhas.

3. **Impacto de mudanças no pipeline**:

• Como o aumento de estágios afeta cada tipo de hazard.

• O comportamento de stalls no pipeline.

4. **Técnicas para reduzir hazards**:

• Adiantamento (forwarding).

• Predição de desvios.

• Reordenação de instruções.

  

### **Questão 2 (Sinais em Processadores Multiciclo)**

  

1. **Caminho de Dados Multiciclo**:

• Função de cada estágio (IF, ID, EX, MEM, WB) e quais sinais estão ativos em cada etapa.

• Especificidade dos sinais em instruções como load e branch.
  

### **Questão 3 (Superescalares)**

1. **Superescalares**:

• Conceito de disparar múltiplas instruções por ciclo.

• Cálculo de speedup teórico e prático.

• Diferença entre vazão (throughput) e latência.

• O papel do compilador no desempenho de processadores superescalares.

2. **Diferenças entre issue estático e dinâmico**:

• VLIW (Very Long Instruction Word) versus superescalar com reordenação dinâmica.

3. **Caminhos de Dados em Processadores Superescalares**:

• Justificar a especialização de caminhos de dados em processadores modernos.

  
---
# **Prova 2**

  

### **Questão 1 (Teoria sobre IPC e Hazards)**

1. **IPC em Processadores Multiciclo com Pipeline**:

• Relação entre stalls e IPC.

• Redução de IPC por aumento de hazards.

2. **Impacto de Técnicas de Predição de Desvios**:

• Por que diminui stalls e aumenta IPC.

3. **Ciclo de Processadores Multiciclo versus Uniciclo**:

• Diferença no tempo de ciclo e impacto na execução.

4. **CPI Médio em Função de Hazards**:

• Como hazards aumentam o CPI.

  

### **Questão 2 (Hazards e Adiantamento):**

  

1. **Hazard de Dados com Diagramas**:

• Escrever código com hazards.

• Diagramas de ciclos com e sem adiantamento.

2. **Speedup em Pipeline**:

• Calcular speedup considerando stalls e tempo para encher o pipeline.

3. **Adiantamento EX/MEM e MEM/WB**:

• Como e por que ocorre adiantamento nesses estágios.

  

### **Questão 3 (Sinais no Caminho de Dados):**

  

1. **Configuração de Sinais**:

• Relacionar sinais ativados ao estágio da instrução.

• Conhecer o comportamento dos sinais para instruções como load, store e branch.

  

### **Questão 4 (Superescalares Avançados):**

  

1. **Issue Estático (VLIW) x Dinâmico**:

• Diferenças em como as instruções são agrupadas e disparadas.

2. **Necessidade de Múltiplos PCs e ALUs**:

• Entender que múltiplas ALUs são essenciais, mas múltiplos PCs não.

3. **Caminhos de Dados Especializados**:

• Por que separar caminhos de dados (e.g., Lógico-aritmético, Load/Store, ponto flutuante).

  ---
  

**O que Estudar**

1. **Livro do RISC-V**:

• Caminho de dados para processadores multiciclo e pipeline.

• Exemplos de hazards e técnicas de redução.

2. **Exercícios Práticos**:

• Escrever e analisar código assembly RISC-V.

• Desenhar e interpretar diagramas de ciclos.

3. **Superescalares e Arquitetura Moderna**:

• Conceitos de pipelines e superescalares.

• Predição de desvios e técnicas de otimização de compiladores.

4. **Conceitos de IPC e CPI**:

• Relação entre throughput, latência, e eficiência de execução.

