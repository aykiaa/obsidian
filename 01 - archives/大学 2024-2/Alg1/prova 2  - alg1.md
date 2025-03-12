
## Divisão e conquista
- mergesort
- counting inversions
- randomized quicksort
- median and selection
- closest pair of points



### median and selection problems
tendo n elementos em uma lista ordenada, achar o K menor elemento.
O(n) : compares for mix and max

**randomized quickselect**
- definir um pivo
- 3-way partition L,M,R
- analisar um subarray
Ex: se eu quiser o 7th menor elemento, e eu sei que no subarray L só possui 4 elementos, eu não vejo e já pulo para o outro subarray.
![[Pasted image 20250115101721.png]]

*Worst-case linear time:* achar um pivo p que divida a lista de n elementos em 2 pedaços, na qual cada um é **garantido ter < = 7/10n elementos**
![[Pasted image 20250115102748.png]]

###  **Divisão e Conquista: Conceitos e Exemplos**

### Conceito Principal
- Dividir o problema em subproblemas menores do mesmo tipo.
- Resolver os subproblemas recursivamente.
- Combinar as soluções para obter uma solução geral.
- Complexidade típica: _O(n log n)_, em contraste com _Θ(n²)_ da força bruta.
### Exemplos de Algoritmos

#### **Mergesort**

- Classifica recursivamente as metades esquerda e direita de uma lista.
- Mescla as metades classificadas para criar uma lista ordenada completa.
- Processo de mesclagem:
    - Compara elementos menores em cada lista.
    - Anexa o menor elemento a uma nova lista classificada.
- Complexidade de tempo: _O(n log₂ n)_.

#### **Contagem de Inversões**

- Problema: Contar pares invertidos em uma lista _(i, j)_ onde _i < j_ e _aᵢ > aᵣ_.
- Algoritmo:
    - Divide a lista ao meio.
    - Conta inversões recursivamente em cada metade.
    - Combina as contagens usando busca binária e mesclagem
#### **Quicksort**
- Partição da matriz em duas porções:
    - Primeira porção: Elementos menores que o pivô.
    - Segunda porção: Elementos maiores ou iguais ao pivô.
- Complexidade de tempo:
    - Pior caso: _O(n²)_ (partição degenerativa).
    - Melhor caso: _O(n log n)_ (partição equilibrada).

##### **Quicksort Randomizado**

- Escolha do pivô é aleatória para mitigar o pior caso
##### **Partição em 3 Vias**

- Divide a matriz em três partes:
    - Elementos menores que o pivô.
    - Elementos iguais ao pivô.
    - Elementos maiores que o pivô.
- Complexidade:
    - Tempo: _O(n)_.
    - Espaço: _O(1)_.
- Usa o algoritmo de partição em 3 vias de Dijkstra.

### Problemas Resolvidos com Divisão e Conquista

#### **Problema do Par Mais Próximo**

- Encontrar um par de pontos com a menor distância euclidiana
- Algoritmo:
    - Divide o conjunto de pontos por uma linha vertical.
    - Encontra recursivamente o par mais próximo em cada lado.
    - Combina as soluções considerando apenas pontos dentro de uma faixa específica.
- Complexidade: _O(n log n)_.

#### **Problema de Seleção**

- Encontrar o _k_ésimo menor elemento em um conjunto de _n_ elementos.
- Algoritmos:
    - Ordenação: Complexidade _O(n log n)_.
    - Seleção Mediana das Medianas:
        - Mediana de grupos de 5 elementos.
        - Usa a mediana como pivô para particionar a matriz.
        - Garante tamanho balanceado (_3n/10_ elementos em cada parte).
        - Complexidade: _O(n)_.