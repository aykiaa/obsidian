

### Goal
Achar um casamento estável entre **2 conjuntos de elemento com tamanho iguais**, a partir de uma **ordem de preferencia** de cada elemento
- *Ex*: mans x girls, faculdade x estudantes

Se tiver N homens e N mulheres, e que cada um fez a ordem de preferencia, é **GARANTIDO** achar um stable matching.

- **Stable matching**: um stable matching é quando nao ha um emparelhamento onde haja duas pessoas que prefiram estar juntos um com o outro do que com seus parceiros atuais.
		*obs:* precisa ser recíproco 



## Aqui está o exemplo de *Stable Matching* 
---
#### Participantes
- **Homens**: João, Pedro, Lucas, Rafael
- **Mulheres**: Ana, Beatriz, Carla, Daniela

---

### Preferências dos Homens

| Homens | 1ª Escolha | 2ª Escolha | 3ª Escolha | 4ª Escolha |
|--------|------------|------------|------------|------------|
| João   | Beatriz    | Ana        | Carla      | Daniela    |
| Pedro  | Ana        | Carla      | Daniela    | Beatriz    |
| Lucas  | Carla      | Daniela    | Beatriz    | Ana        |
| Rafael | Ana        | Beatriz    | Daniela    | Carla      |

### Preferências das Mulheres

| Mulheres | 1ª Escolha | 2ª Escolha | 3ª Escolha | 4ª Escolha |
|----------|------------|------------|------------|------------|
| Ana      | João       | Pedro      | Lucas      | Rafael     |
| Beatriz  | Lucas      | João       | Rafael     | Pedro      |
| Carla    | Pedro      | Rafael     | João       | Lucas      |
| Daniela  | Rafael     | Lucas      | Pedro      | João       |

---

### Processo de Matching Estável

Abaixo estão as combinações ao final do processo de *stable matching*, usando o algoritmo de Gale-Shapley para garantir a estabilidade.

1. **Rodada 1:** 
   - João propõe para Beatriz (preferida), e ela aceita.
   - Pedro propõe para Ana (preferida), e ela aceita.
   - Lucas propõe para Carla (preferida), e ela aceita.
   - Rafael propõe para Ana (preferida), mas Ana já está com Pedro e prefere Pedro, então Rafael é rejeitado.

2. **Rodada 2:** 
   - Rafael propõe para Beatriz (segunda escolha), mas Beatriz já está com João e prefere João, então Rafael é rejeitado novamente.
   - Rafael propõe para Daniela, que aceita (ninguém havia proposto ainda).

---

### Resultado Final de Matching

| Homens | Parceria Final |
|--------|-----------------|
| João   | Beatriz        |
| Pedro  | Ana            |
| Lucas  | Carla          |
| Rafael | Daniela        |

| Mulheres | Parceria Final |
|----------|-----------------|
| Ana      | Pedro          |
| Beatriz  | João           |
| Carla    | Lucas          |
| Daniela  | Rafael         |

---

Esse matching é estável, pois não há nenhum par que preferiria trocar de parceiro sem que ambos concordassem, o que mantém a estabilidade do conjunto.

**100% garantido** para achar estabilidade, porém *quem faz as propostas, o matching será mais favorável*  para este grupo,
	**PORQUE?** A razão é que o grupo que faz as propostas tem prioridade ao tentar emparelhar-se com sua escolha preferida, enquanto o grupo que recebe as propostas precisa rejeitar ou aceitar com base em suas preferências.

Independente da ordem dentro de um mesmo conjunto, ou seja, **não faz diferença a ordem com que os indivíduos de um mesmo grupo fazem as propostas**. 
Desde que um grupo específico (por exemplo, os homens) esteja fazendo as propostas, todos eles eventualmente terão a chance de propor às suas escolhas preferidas, e o algoritmo garantirá um resultado estável. 
A ordem de proposição entre os membros de um mesmo grupo não altera o matching final; o que realmente importa é **qual grupo está fazendo as propostas** (homens ou mulheres), pois isso determina quem terá prioridade no matching final.


### Em Resumo:
- **Ordem de Proposição**: Determina o grupo beneficiado no resultado.
- **Resultado Estável**: Independentemente de quem faz a proposta, o algoritmo sempre encontra um matching estável, mas a qualidade (satisfação com as escolhas) depende de quem propõe.


## Implementação Eficiente do Algoritmo Gale-Shapley

O objetivo é implementar o algoritmo Gale-Shapley de forma que ele execute em tempo O(n²), onde 'n' representa o número de hospitais e estudantes. Para atingir essa eficiência, a representação dos dados e a organização das operações são cruciais.

**Representação dos Hospitais e Estudantes:**

- Os hospitais e estudantes são indexados de 1 a n.

**Representação do Emparelhamento:**

- Duas matrizes, `estudante[h]` e `hospital[s]`, são utilizadas para representar o emparelhamento.
    - Se o hospital `h` está emparelhado com o estudante `s`, então `estudante[h] = s` e `hospital[s] = h`.
    - O valor 0 é usado para indicar que um hospital ou estudante não está emparelhado.
- Essa representação permite *adicionar ou remover um par do emparelhamento* em tempo *O(1).*

**Conjunto de Hospitais Não Emparelhados:**

- Uma fila (ou pilha) é usada para armazenar o conjunto de hospitais não emparelhados.
- Essa estrutura permite encontrar um hospital não emparelhado em tempo O(1).

---
**Realizando uma Proposta:**

- A operação chave durante uma proposta é encontrar o próximo estudante favorito do hospital.
- Para cada hospital, uma *lista de estudantes, ordenada por preferência*, é mantida.
- Além disso, um *ponteiro para o próximo estudante* a ser proposto é mantido para cada hospital.
- Com essa organização, realizar uma *proposta leva tempo O(1).*
---
**Aceitando ou Rejeitando uma Proposta:**

- Para determinar se o estudante `s` prefere o hospital `h` ao hospital `h'`, o inverso da lista de preferências de hospitais é criado para cada estudante.
- Isso é feito em tempo de pré-processamento Θ(n²) para criar as `n` matrizes de classificação.
- Após o pré-processamento, verificar a preferência do estudante leva tempo O(1).

**Entendendo a Lista Invertida em Profundidade: Otimizando o Algoritmo Gale-Shapley**

A lista invertida, como já discutimos, é uma estrutura de dados fundamental para a implementação eficiente do algoritmo Gale-Shapley. Ela permite que os estudantes comparem rapidamente as propostas dos hospitais, otimizando a etapa de decisão do algoritmo. Vamos explorar mais a fundo seu funcionamento e importância.

**Contexto da Lista Invertida:**
No algoritmo Gale-Shapley, a cada iteração, um hospital não emparelhado propõe ao seu estudante favorito ainda não contatado. O estudante, por sua vez, precisa decidir se aceita a proposta. *Essa decisão depende da comparação entre o hospital proponente e o hospital ao qual ele já está (potencialmente) emparelhado.*

**Problema da Solução Ingênua:**

Se compararmos os hospitais percorrendo a lista de preferências do estudante a cada proposta, a *complexidade seria O(n) para cada comparação*, onde 'n' é o número de hospitais. Em um algoritmo com múltiplas propostas, essa ineficiência se acumula, tornando o processo lento.

**A Lista Invertida como Solução:**

A lista invertida, representada pela matriz `rank[]`, resolve esse problema de forma inteligente. A ideia é armazenar, para cada estudante, a posição (ranking) de cada hospital em sua lista de preferências.

**Exemplo Detalhado:**

Imagine um estudante com a seguinte lista de preferências:

- 1º: Hospital A
- 2º: Hospital D
- 3º: Hospital B
- 4º: Hospital C

A lista invertida `rank[]` para esse estudante seria:

- `rank[A] = 1` (Hospital A está em 1º lugar)
- `rank[B] = 3` (Hospital B está em 3º lugar)
- `rank[C] = 4` (Hospital C está em 4º lugar)
- `rank[D] = 2` (Hospital D está em 2º lugar)

**Comparação Eficiente:**

Agora, se o estudante recebe uma proposta do Hospital C e já está emparelhado com o Hospital D, a comparação é direta:

- `rank[C] = 4`
- `rank[D] = 2`

Como `rank[D] < rank[C]`, o estudante prefere o Hospital D e rejeita a proposta do Hospital C. **Essa comparação, utilizando a lista invertida, é realizada em tempo O(1), tornando a decisão do estudante extremamente eficiente.**

**Construção da Lista Invertida:**

A matriz `rank[]` é construída durante a fase de pré-processamento do algoritmo, que possui complexidade Θ(n²), como descrito nas páginas 64-65 do material. Para cada estudante, percorremos sua lista de preferências `pref[]` e, para cada hospital `i` na lista, definimos `rank[pref[i]] = i`.

**Benefícios da Lista Invertida:**

- **Eficiência:** A principal vantagem da lista invertida é a otimização da etapa de aceitação/rejeição de propostas. A comparação entre hospitais, que antes levava tempo O(n), agora é realizada em tempo O(1).
- **Simplicidade:** A lógica da lista invertida é simples e fácil de implementar, não adicionando complexidade significativa ao algoritmo.
- **Escalabilidade:** A lista invertida torna o algoritmo Gale-Shapley mais escalável, permitindo que ele lide com um grande número de hospitais e estudantes de forma eficiente.

Em resumo, a lista invertida é uma estrutura de dados crucial para a implementação eficiente do algoritmo Gale-Shapley. Ela simplifica e acelera a etapa de decisão do estudante, tornando o algoritmo mais rápido e escalável para cenários do mundo real.

---
**Resumo da Implementação Eficiente:**

- O algoritmo Gale-Shapley pode ser implementado para executar em tempo O(n²).
    - O pré-processamento para criar as matrizes de classificação leva tempo Θ(n²).
    - Existem O(n²) propostas, e processar cada proposta leva tempo O(1).
- No pior caso, qualquer algoritmo para encontrar um emparelhamento estável precisa consultar a lista de preferências do hospital Ω(n²) vezes.

Essa implementação eficiente garante que o algoritmo Gale-Shapley encontre um emparelhamento estável em tempo proporcional ao quadrado do número de participantes, tornando-o escalável para cenários do mundo real com um grande número de hospitais e estudantes.