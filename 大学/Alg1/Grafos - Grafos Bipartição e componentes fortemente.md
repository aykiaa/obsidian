

### **Grafos Bipartidos**

- **Definição:** Um grafo não direcionado $G = (V, E)$ é bipartido se os vértices puderem ser coloridos em dois grupos (azul e branco) de modo que nenhuma aresta conecte dois vértices da mesma cor.

![[Pasted image 20241106102421.png]]


**Propriedades e Aplicações:**
  - Grafos bipartidos simplificam problemas como *emparelhamento e conjunto independente.*
  - Exemplo de aplicação: correspondência estável (médicos e hospitais).

 **Teste de Bipartição:**
  - Um grafo é bipartido se não contiver *ciclos de tamanho ímpar*. Isso ocorre porque, em um ciclo de comprimento ímpar, não é possível colorir os nós com duas cores de forma que cada aresta conecte nós de cores diferentes.
  
  ![[Pasted image 20241106102635.png]]
  
  - **Algoritmo:** 
	Para testar se um grafo é bipartido, podemos usar o algoritmo BFS (Busca em Largura). Se, durante a execução do BFS, encontrarmos uma aresta que conecta dois nós no mesmo nível, o grafo contém um ciclo de comprimento ímpar e, portanto, **não é bipartido**. Caso contrário, o grafo é bipartido.

![[Pasted image 20241106103216.png]]

---
### **Componentes Fortemente Conexos (SCC)**
 **Definição:**  Em um grafo direcionado, dois nós são **mutuamente alcançáveis** se houver um caminho direcionado de um para o outro e vice-versa. 
Um grafo direcionado é **fortemente conectado** se cada par de nós for mutuamente alcançável. 
**Algoritmo:** $O(m + n)$
- Para determinar se um grafo é fortemente conectado, podemos executar o algoritmo *BFS* a partir de um nó arbitrário e, em seguida, executar o *BFS no grafo reverso* (com a orientação de todas as arestas invertidas). *Se todos os nós forem alcançados em ambas as execuções do BFS, o grafo é fortemente conectado.*

*Ex:*

| **Grafo Direcionado** | **Nó**             | **Aresta Direcionada**      |
| --------------------- | ------------------ | --------------------------- |
| **Transporte**        | Interseção de ruas | Rua de mão única            |
| **Web**               | Página web         | Hiperlink                   |
| **Teia Alimentar**    | Espécie            | Relação de predador e presa |
Um **componente fortemente conectado** é um subconjunto maximal de nós mutuamente alcançáveis.

![[Pasted image 20241106104753.png]]

### Algoritmo de Kosaraju
Dado um grafo, ele identifica *todos os componentes fortemente conectados (SCC)*
  1. **DFS no grafo original:** Calcular os tempos de término de cada vértice e inserir esse tempo em uma lista, que ao final naturalmente já estará em ordem decrescente - $t[v]$.
  2. **Transpor o grafo:** Inverter todas as arestas.
  3. **DFS no grafo transposto:** Seguir a ordem decrescente dos tempos de término - $t[v]$, ou seja, começando do maior tempo. Cada árvore gerada representa um SCC.
  ![[Pasted image 20241106105705.png]]
![[Pasted image 20241106105912.png]]




**Teoremas Importantes:**
  - **Teorema 1:** Se $C$ e $C'$ são SCCs distintos e existe uma aresta de $u \in C$ para $v \in C'$, então o tempo de término de $C$ é maior que o de $C'$.
  ![[Pasted image 20241106110218.png]]
  - **Teorema 2:** No grafo transposto, a relação de tempos de término se inverte.
  - **Teorema 3:** O Algoritmo de Kosaraju identifica corretamente os SCCs, garantindo que cada DFS no grafo transposto se restringe a um único componente.

- **Complexidade de Tempo:** $O(|V| + |E|)$, onde $|V|$ é o número de vértices e $|E|$, o número de arestas.



### Como e Por Que o Algoritmo de Kosaraju Funciona

O **Algoritmo de Kosaraju** é utilizado para encontrar todos os **componentes fortemente conectados (SCCs)** de um grafo direcionado. Ele explora as propriedades de **busca em profundidade (DFS)** e a **reversão de arestas** para identificar essas componentes de forma eficiente.

#### **Passo a Passo do Algoritmo**
1. **Primeira DFS no Grafo Original:**
   - Execute uma DFS no grafo original para calcular os **tempos de término** de cada nó.
   - O tempo de término é atribuído a cada nó quando a DFS finaliza a exploração daquele nó.
   - Resultado: Uma ordem dos nós baseada nos tempos de término (do maior para o menor).

2. **Transposição do Grafo (Grafo Reverso):**
   - Inverta todas as arestas do grafo original, criando o **grafo transposto**.
   - Se havia uma aresta de $u \to v$ no grafo original, agora haverá uma aresta de $v \to u$.

3. **Segunda DFS no Grafo Transposto:**
   - Execute a DFS no grafo transposto, seguindo a **ordem decrescente** dos tempos de término obtidos na primeira DFS.
   - Cada vez que uma nova DFS é iniciada, ela descobre todos os nós pertencentes ao mesmo SCC.

#### **Por Que o Algoritmo Funciona**

O algoritmo se baseia em duas propriedades fundamentais:

1. **A ordem decrescente dos tempos de término garante que os SCCs sejam processados na sequência correta.**
   - O nó com maior tempo de término em um SCC $C$ será o primeiro a ser processado no grafo transposto.
   - Se existe uma aresta de $C$ para outro SCC $C'$, o tempo de término de $C$ será maior que o de $C'$. Assim, $C'$ já terá sido completamente explorado antes de começar a explorar $C$.

2. **O grafo transposto preserva a estrutura interna dos SCCs.**
   - A inversão das arestas não altera a conectividade interna dos SCCs, mas sim a direção das conexões entre SCCs distintos.
   - Quando a DFS no grafo transposto começa em um nó, ela só alcança nós dentro do mesmo SCC, já que todas as conexões de saída do SCC apontam para SCCs já processados (devido à ordem de tempo de término).

#### **Intuição Visual**

- **Grafo Original:** DFS coleta tempos de término. Os SCCs podem ser vistos como "ilhas" fortemente conectadas.
- **Grafo Transposto:** A DFS explora essas ilhas em uma ordem que respeita a hierarquia das conexões entre SCCs.

#### **Complexidade de Tempo**
- A execução de duas DFS (uma no grafo original e outra no transposto) e a construção do grafo transposto têm complexidade $O(|V| + |E|)$, onde:
  - $|V|$ é o número de vértices.
  - $|E|$ é o número de arestas.
  
Assim, o algoritmo é eficiente mesmo para grafos grandes.

#### **Por Que Kosaraju é Correto**
A **primeira DFS** coleta informações sobre a estrutura do grafo através dos tempos de término. A **segunda DFS** garante que todos os nós de um SCC sejam visitados juntos, pois as arestas entre SCCs já foram "direcionadas corretamente" pela inversão do grafo. Essas duas etapas em conjunto asseguram que cada SCC seja identificado de forma independente.



#### **Aplicações de Grafos Direcionados:**
- Utilizados em web (grafo de páginas e hyperlinks), fluxo de controle em programas, redes de transporte, entre outros.