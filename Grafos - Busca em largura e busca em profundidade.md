## BFS (Busca em Largura)

Explora a partir de um vertice *s* todas as direções, adicionando vizinhos de *cada layer* 
- **Objetivo:** Computa os caminhos mais curtos em grafos não ponderados.
- **Funcionamento:** Explora o grafo camada por camada, usando uma fila para processar cada camada antes de passar para a próxima.
- **Aplicações:** Encontrar componentes conectados em grafos.
### Algoritmo
1. **Definir `L0`**: Comece com `L0 = {s}`, onde `s` é o nó inicial.
2. **Definir `L1`**: Todos os vizinhos de `L0` formam `L1`.
3. **Definir `L2`**: Todos os nós que não pertencem a `L0` ou `L1` e que possuem uma aresta conectando-os a um nó em `L1`.
4. **Generalização**: `Li+1` consiste em todos os nós que não pertencem a camadas anteriores e que têm uma aresta para um nó em `Li`.

- **Teorema**: Cada camada `Li` contém todos os nós que estão a uma distância exata `i` de `s`. Há um caminho de `s` até um nó `t` se, e somente se, `t` aparecer em alguma camada.

- **Conclusão**: BFS encontra o caminho mais curto em grafos não ponderados e encontra todos os vértices que são alcançáveis a partir de um vertice s (explorando em ordem de distancia)


## DFS (Depth-First Search)
- **Objetivo:** Explora o grafo indo o mais fundo possível antes de retroceder.
- **Funcionamento:** Usa uma pilha para gerenciar a ordem de exploração, avançando para os vizinhos não explorados até precisar retornar.
- **Propriedades:** Cada chamada recursiva marca nós descendentes como explorados até o final da execução.
Aqui está uma anotação em Markdown baseada nas observações e teoremas sobre **Depth-First Search (DFS)**:

## Observações
- **Observação**: Para uma chamada recursiva DFS(u), todos os nós que são marcados como "Explorado" entre a invocação e o término dessa chamada recursiva são descendentes de `u` na árvore DFS.

## Teorema
- Seja `T` uma árvore de busca em profundidade de um grafo `G`. Se `(x, y)` é uma aresta de `G` que não pertence a `T`, então um dos nós `x` ou `y` é ancestral do outro em `T`.

    - **Demonstração**: Suponha que `(x, y)` seja uma aresta de `G` que não está em `T`, e suponha, sem perda de generalidade, que `x` seja alcançado primeiro pelo algoritmo DFS.
    - Quando a aresta `(x, y)` é examinada durante a execução de DFS(x), ela não é adicionada a `T` porque `y` já foi marcado como "Explorado" (já que a aresta não está em `T`).
    - Como `x` foi o primeiro a ser alcançado pela DFS, `y` ainda estava marcado como "não Explorado" quando DFS(x) foi invocado.
    - Isso indica que `y` é um nó descoberto entre a invocação e o término da chamada recursiva DFS(x).

- **Conclusão**: Com base na observação acima, conclui-se que `y` é um descendente de `x` em `T`.

---

## Comparação BFS x DFS
- **Semelhanças:** Ambos constroem componentes conectados e têm complexidade de tempo similar.
- **Diferenças:** 
  - BFS gera árvores com caminhos curtos e horizontais.
  - DFS gera árvores profundas e estreitas.
![[Pasted image 20241105175820.png]]


## Implementação
# Implementação: Questões Gerais

## Matriz de Adjacência vs Lista de Adjacência
- **Matriz**:
  - **Espaço**: Θ(n²), pode ser ineficiente para grafos esparsos.
  - **Inspeção dos Vizinhos de um Nó**: O(n²) em tempo.
  - **Verificação/Inserção/Remoção de uma Aresta**: O(1).

- **Lista**:
  - **Espaço**: O(m+n)
  - **Inspeção dos Vizinhos de um Nó v**: O(nᵥ) em tempo (nᵥ = número de vizinhos de v).
  - **Verificação de Existência de uma Aresta**: O(n) em tempo.


  - **Fila (Queue)**: Ordem FIFO (First-In, First-Out).
    - Elementos são processados na mesma ordem em que foram adicionados - *BFS*
  - **Pilha (Stack)**: Ordem LIFO (Last-In, First-Out).
    - Elementos são processados na ordem inversa à que foram adicionados, sempre selecionando o mais recente - *DFS*

- **Implementação de Fila e Pilha**:
  - **Estrutura**: Utilizar uma lista encadeada com ponteiros para o primeiro e último elemento.
  - **Remoção**: Sempre seleciona o primeiro elemento (O(1)).
  - **Inserção**:
    - **Fila**: Novo elemento é adicionado no final da lista (O(1)).
    - **Pilha**: Novo elemento é adicionado no início da lista (O(1)).

### Representações de Grafo
- **Matriz de Adjacência:** Espaço `Θ(n²)`; eficiente para verificar a existência de arestas.
- **Lista de Adjacência:** Espaço `O(m + n)`; preferível para grafos esparsos.

### Estruturas de Dados
- **Fila (BFS):** Processa elementos em ordem de chegada.
- **Pilha (DFS):** Processa elementos na ordem inversa de chegada.

## Implementação de BFS e DFS
- **BFS:** Processa camadas em sequência, mantendo uma lista para nós descobertos.
- **DFS:** Explora profundidade com recursão ou pilha; detecta ciclos se encontrar um nó em processamento.

### Análise de Complexidade
- **BFS e DFS:** O(m + n), linear ao tamanho do grafo se representado por lista de adjacência.
- **Detecção de Ciclos (DFS):** Se um nó "cinza" for revisitado, há um ciclo no grafo.