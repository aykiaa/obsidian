### Definição
Desempenho para PCS é o quanto tempo gasta para realizar algum trabalho
- Tempo de resposta (**LATENCY**): 
	- é a demora para uma tarefa rodar, executar uma tarefa ou realizar uma consulta no banco de dados

### Tipos de tempo
**Tempo decorrido:** tempo total de uma tarefa, inclui acesso a disco, memória, I/O (Input/Output) - **não se utiliza para comparações**

**Tempo de CPU:** sem I/O e nem tempo gasto por outros programas
	Dividido em System Time e User Time

**Tempo de CPU do Usuário**: tempo para executar a linha de código em um programa - **NOSSO FOCO**

DesempenhoX = 1 / Tempo de Exec de X


### CPU Clock
Operação do hardware digital é governado pela **taxa de clock constante**
![[Pasted image 20241023094308.png]]**Período de Clock**: duração de um ciclo de clock
	ex., 250ps = 0.25ns = 250×10^–12s
**Frequência de Clock**: (taxa: ciclos por segundo)
	 ex., 4.0GHz = 4000MHz = 4.0×10^9 Hz

**Tempo de CPU**
![[Pasted image 20241023094451.png]]
**Instruções / Programa:** qtd de instruções executadas por programa
**Ciclos / Instrução:** qtd de ciclos de clock por instrução (CPI)
**Segundos / Ciclos:** inverso da freq de clock da CPU

Essa fórmula é usada para determinar **quanto tempo uma CPU gasta para executar um programa**, levando em consideração a quantidade de instruções, o CPI e a frequência de clock.

A tabela lista alguns fatores que influenciam cada uma das variáveis da fórmula:
- **Programa**: Afeta a contagem de instruções (Instr. Cnt), pois diferentes programas possuem diferentes números de instruções.
    
- **Compilador**: Afeta tanto a contagem de instruções quanto o CPI, já que um compilador pode otimizar o código para reduzir o número de instruções ou o CPI.
    
- **Conjunto de Instruções**: Influencia a contagem de instruções e o CPI, dependendo do tipo de instruções disponíveis para a CPU.
    
- **Organização**: Refere-se à arquitetura interna da CPU, que afeta tanto o CPI quanto a taxa de clock.
    
- **Tecnologia**: Impacta diretamente na frequência de clock (Clock Rate), já que o avanço da tecnologia de fabricação de chips permite frequências mais altas.


- tempo de ciclo (segundos por ciclo)
- taxa de clock (ciclos por segundo)
- CPI (# médio de ciclos por instrução)
	uma aplicação intensiva em ponto flutuante poderia ter um alto CPI
- MIPS (milhões de instruções por segundo)
	poderia ser bom para um programa usando instruções simples


**OBS**: Assumir que X de ciclos = X de instruções, porém isso é falso já que **instruções gastam tempos diferentes em máquinas diferentes**
	- diferentes instruções consomem diferentes quantidades de ciclos
	- 
	 Algumas instruções podem ser executadas em apenas um ciclo de clock, enquanto outras podem requerer vários ciclos. 
		 *Por exemplo*, uma *simples adição pode gastar menos ciclos do que uma multiplicação* ou uma operação de acesso à memória.
	**Máquinas diferentes**: Processadores diferentes podem ter *arquiteturas diferentes*, o que significa que uma *mesma instrução pode ser executada em diferentes quantidades de ciclos dependendo do design do processador.* 
		Por exemplo, um processador mais moderno com uma melhor arquitetura de pipelining pode executar instruções mais rapidamente do que um processador mais antigo.