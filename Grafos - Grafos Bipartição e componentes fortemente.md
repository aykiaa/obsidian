

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
![[Pasted image 20241106105716.png]]
- **Teoremas Importantes:**
  - **Teorema 1:** Se $C$ e $C'$ são SCCs distintos e existe uma aresta de $u \in C$ para $v \in C'$, então o tempo de término de $C$ é maior que o de $C'$.
  - **Teorema 2:** No grafo transposto, a relação de tempos de término se inverte.
  - **Teorema 3:** O Algoritmo de Kosaraju identifica corretamente os SCCs, garantindo que cada DFS no grafo transposto se restringe a um único componente.

- **Complexidade de Tempo:** $O(|V| + |E|)$, onde $|V|$ é o número de vértices e $|E|$, o número de arestas.

#### **Aplicações de Grafos Direcionados:**
- Utilizados em web (grafo de páginas e hyperlinks), fluxo de controle em programas, redes de transporte, entre outros.

#### **Notas Extras:**
- Grafos bipartidos e SCCs são conceitos cruciais em teoria de grafos, com aplicações práticas que vão de otimização a análise de redes.









### Algoritmo de Kosaraju

- O algoritmo de Kosaraju é usado para encontrar os componentes fortemente conectados de um grafo direcionado.
    
- **Etapas do algoritmo de Kosaraju:**
    
    1. Executar DFS no grafo original e calcular os tempos de término de cada nó.
    2. Calcular o grafo reverso, invertendo a direção de todas as arestas.
    3. Executar DFS no grafo reverso, considerando os nós na ordem decrescente de seus tempos de término.
    4. Cada árvore gerada pelo DFS no grafo reverso representa um componente fortemente conectado.
- **Exemplo de execução do algoritmo de Kosaraju:**
    
- **Por que o algoritmo de Kosaraju funciona?**
    
    - O algoritmo se baseia na ideia de que, se houver uma aresta de um componente C para outro componente C', o maior tempo de término de um nó em C será maior que o maior tempo de término de um nó em C'.
    - Ao executar o DFS no grafo reverso na ordem decrescente dos tempos de término, o algoritmo garante que cada componente fortemente conectado seja visitado antes de quaisquer componentes que tenham arestas direcionadas para ele.
- **Complexidade de tempo do algoritmo de Kosaraju:** O(V + E), onde V é o número de nós e E é o número de arestas no grafo.