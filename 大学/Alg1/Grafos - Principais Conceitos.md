source:[[Graphs-aula1.pdf]]



## Grafos Nao-Direcionados
**Undirected Graphs**
Arestas não possuem direção

**Notation:** 
- *G = (V , E)*
- *V* = vertices
- *E* = edges / arestas
- Parâmetros de tamanho de um Grafo: *n = |V|, m = |E|*

![[image.png]]

---
## Grafos Direcionados 
**Directed Graphs**
Asymetric relationship between two nodes; Vertices têm *DIREÇÃO*

![[0_eg5zFvNZw3jB-THg.png]]

---

## Grafos com peso
Weighted graphs
As arestas possuem *peso*, que indicam a força da relação

![[Pasted image 20241031154557.png]]

**OBS:** as vezes, os vértices também podem possui peso


## Graph Traversal
A *travessia de grafos* é uma das operações mais importantes. Esse processo envolver percorrer uma sequencia de vértices conectados por arestas, explorando as relações e conexões dentro do grafo.
*Ex:*
- um user navegando na web
- propagação de rumor boca a boca
- passageiro de um avião que possui diversas conexões

---
## Conceitos
### Paths and connectivity
Caminhos e conectividade

**Caminhos** em grafos são sequências de nós conectados por arestas. A **conectividade** se refere à existência de caminhos entre os nós de um grafo.

A conectividade em **grafos direcionados difere dos grafos não direcionados.** 
- **grafo direcionado:** a existência de um caminho de um nó `u` para um nó `v` não garante que haja um caminho de `v` para `u`.
- **grafo não-direcionado**: é uma sequencia de vertices, em que cada par de vertices possui uma aresta E entre.

### Tipos de Conectividade em Grafos Direcionados

- **Fortemente Conectado:** Um grafo *direcionado* é fortemente conectado se, para quaisquer dois nós `u` e `v`, existir um caminho de `u` para `v` **e** um caminho de `v` para `u`.
- **Fracamente Conectado:** Um grafo direcionado é fracamente conectado se, ao ignorar a direção das arestas, existir um caminho entre quaisquer dois nós.

![[Pasted image 20241031161555.png]]
### Componentes Conectados

Um **componente conectado** de um *grafo não direcionado* é um subgrafo no qual existe um caminho entre quaisquer dois nós. Em outras palavras, todos os nós dentro de um componente conectado estão interligados.

Em um *grafo não-direcionado* $G = (V, E)$,  um **componente conexo** é um subgrafo $G' = (V', E')$ com as seguintes propriedades:

1. **Subconjuntos de vértices e arestas**: $V' \subset V$ e $E' \subset E$, ou seja, $G'$ é formado por um subconjunto dos vértices e arestas do grafo original.

2. **Caminho entre quaisquer dois vértices**: Para qualquer par de vértices $u$ e $v$ em $V'$, existe um caminho no grafo original $G$ que conecta $u$ e $v$. Isso significa que é possível ir de $u$ a $v$ passando por uma sequência de arestas em $E'$, garantindo que todos os vértices de $G'$ estejam interconectados.

Basicamente, cada **componente conexo é uma "parte" do grafo maior** onde todos os vértices estão conectados entre si por caminhos, mas **não existe uma conexão entre vértices em componentes diferentes.** 
Em outras palavras, se você escolher um vértice em um componente conexo, conseguirá alcançar qualquer outro vértice do mesmo componente, mas não necessariamente vértices de outros componentes.

![[Pasted image 20241031162655.png]]



Um **componente fortemente conectado** de um grafo *direcionado* é um subgrafo no qual existem caminhos de ida e volta entre quaisquer dois nós.

1. **Subconjuntos de vértices e arestas**: $V' \subset V$ e $E' \subset E$, ou seja, $G'$ é formado por um subconjunto dos vértices e arestas do grafo original.

2. **Caminhos em ambas as direções**: Para cada *par de vértices $u$ e $v$ em $V'$,* existe um caminho que vai de *$u$ até $v$ e outro caminho que vai de $v$ até $u$ no grafo original $G$.* Isso significa que qualquer vértice do componente pode ser alcançado a partir de qualquer outro vértice do mesmo componente, respeitando a direção das arestas.

Em outras palavras, cada **componente fortemente conexo** é uma "parte" do grafo onde **todos os vértices estão interconectados de forma bidirecional**. 
Isso é exclusivo de grafos direcionados: se você escolher qualquer vértice $u$ em um componente fortemente conexo, poderá alcançar qualquer outro vértice $v$ e também retornar a $u$ a partir de $v$ através de caminhos que respeitam as direções das arestas.


---

### Ciclos

**Definição:** Um ciclo é um caminho $v_1, v_2, \ldots, v_k$ em que $v_1 = v_k$, $k > 2$, e os primeiros $k-1$ nós, são *todos distintos*, ou seja, não pode repetir vertices

Exemplo de ciclo: $C = 1 - 2 - 4 - 5 - 3 - 1$
![[Pasted image 20241031163348.png]]

---

### Árvores

**Definição**: Um **grafo não direcionado** é uma **árvore** se ele for **conectado** e **não contiver ciclos**.

**Teorema**: Seja $G$ um grafo não direcionado com $n$ nós. Qualquer dois dos seguintes enunciados implicam o terceiro:

- $G$ é conectado -> existe um caminho entre quaisquer nós
- $G$ não contém ciclos.
- $G$ tem $n - 1$ arestas.

*Observação:*
- Remover qualquer aresta de uma árvore desconectará o grafo.
- Qualquer árvore com $n$ nós tem exatamente $n - 1$ arestas.

![[Pasted image 20241031163626.png]]


---
### Árvores Enraizadas

Dada uma árvore $T$, escolha um nó raiz $r$ e oriente cada aresta para longe de $r$.

**Importância**: Modela a estrutura hierárquica.

![[Pasted image 20241031163800.png]]

---

### Grafos Isomórficos

- Dois grafos que contêm o mesmo número de vértices conectados da mesma forma são ditos **isomórficos**.
- Formalmente: dois grafos $G$ e $H$, ambos com vértices $V = \{1, 2, \dots, n\}$, são isomórficos se existir uma permutação $p$ de $V$ tal que $(u, v)$ é uma aresta em $G$ se, e somente se, $(p(u), p(v))$ é uma aresta em $H$.
![[Pasted image 20241031163952.png]]
### Representação de Grafo: Matriz de Adjacência

**Matriz de Adjacência**: matriz $n \times n$ com $A_{uv} = 1$ se $(u, v)$ for uma aresta.
- Duas representações de cada aresta.
- Espaço proporcional a $n^2$.
- Verificar se $(u, v)$ é uma aresta leva tempo $\Theta(1)$.
- Identificar todas as arestas leva tempo $\Theta(n^2)$.

![[Pasted image 20241031164003.png]]

### Representação de Grafo: Listas de Adjacência

**Listas de Adjacência**: array de listas indexado por nós.
- Duas representações de cada aresta.
- Espaço é $\Theta(m + n)$.
- Verificar se $(u, v)$ é uma aresta leva tempo $O(\text{grau}(u))$.
	- *$\text{grau}(u)$ = número de vizinhos de u*
- Identificar todas as arestas leva tempo $\Theta(m + n)$.

![[Pasted image 20241031164010.png]]