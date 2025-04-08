#ai 

## Complexidades de Espaço e Tempo em Algoritmos de Busca

*Branching Factor médio (b)*
- É o número médio de sucessores que cada nó gera
- Representa quantas opções ou ramificações são possíveis a partir de cada estado
- Quanto maior o branching factor, mais estados o algoritmo precisa explorar

*Profundidade da solução mais rasa (d)*
- É a distância mínima (número de passos) da raiz até o nó objetivo
- Representa o caminho mais curto até a solução
- Importante para avaliar o desempenho de algoritmos como BFS (Busca em Largura)

*Tamanho máximo de um caminho (m)*
- É o limite máximo de profundidade que um caminho pode ter
- Utilizado para prevenir buscas infinitas em espaços de estados muito grandes
- Pode ser usado como parâmetro em algoritmos como IDDFS (Busca em Profundidade Iterativa)

### Efetividade: Custo da Busca x Custo Total
- **Custo da busca**: recursos computacionais (tempo e memória) necessários para encontrar a solução
- **Custo da solução**: qualidade da solução encontrada (geralmente medida pelo comprimento do caminho)
- **Custo total = custo da busca + custo da solução**

### Complexidade de diferentes algoritmos:
1. **BFS (Busca em Largura)**:
    - Complexidade de tempo: O($b^d$)
    - Complexidade de espaço: O($b^d$)
    - Encontra sempre a solução ótima (menor caminho)
2. **DFS (Busca em Profundidade)**:
    - Complexidade de tempo: O($b^m$)
    - Complexidade de espaço: O($b *m$)
    - Pode não encontrar a solução ótima
3. *_A_ (A-Estrela)**:
    - Complexidade de tempo: O(b^d)
    - Complexidade de espaço: O(b^d)
    - Encontra a solução ótima quando usa uma heurística admissível

