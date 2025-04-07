

Para resolver este problema de otimização, precisamos encontrar a quantidade ideal de cada tipo de ração (T1 e T2) que a empresa deve produzir para maximizar seu lucro, considerando as restrições de matéria-prima disponível.

Vou definir as variáveis e estruturar o problema de programação linear:

- Seja x1 = quantidade (em kg) de ração Tipo 1 (T1) a ser produzida
- Seja x2 = quantidade (em kg) de ração Tipo 2 (T2) a ser produzida

**Função objetivo (lucro):**

- Preço de venda T1: R$20,00/kg
- Preço de venda T2: R$30,00/kg
- Custo T1: (5kg cereal × R$1,00) + (1kg carne × R$4,00) = R$9,00/kg
- Custo T2: (2kg cereal × R$1,00) + (4kg carne × R$4,00) = R$18,00/kg
- Lucro T1: R$20,00 - R$9,00 = R$11,00/kg
- Lucro T2: R$30,00 - R$18,00 = R$12,00/kg

Função de lucro a maximizar: L = 11x1 + 12x2

**Restrições:**

- Limitação de cereal: 5x1 + 2x2 ≤ 30.000
- Limitação de carne: 1x1 + 4x2 ≤ 10.000
- Não-negatividade: x1 ≥ 0, x2 ≥ 0

## Solução Ótima

A empresa deve produzir:

- **5.555,56 kg** de ração Tipo 1 (T1)
- **1.111,11 kg** de ração Tipo 2 (T2)

Com esta estratégia de produção, a empresa obterá um **lucro máximo de R$ 74.444,44**
## Utilização dos Recursos
Esta solução utiliza:

- **100% dos cereais** disponíveis (30.000 kg)
- **100% da carne** disponível (10.000 kg)

Isso significa que todos os recursos serão aproveitados de maneira eficiente, sem sobras de matéria-prima.

## Verificação

No ponto ótimo, as restrições de recursos são satisfeitas:

- Cereais: 5 × 5.555,56 + 2 × 1.111,11 = 30.000 kg ✓
- Carne: 1 × 5.555,56 + 4 × 1.111,11 = 10.000 kg ✓

Este é o melhor plano de produção possível considerando as restrições dadas.