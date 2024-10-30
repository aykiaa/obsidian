## Guia de Resolução dos Exercícios do PDF 2

### Exercício 1: Casamentos entre pessoas boas e más

**Enunciado:** Considere uma cidade com _n_ homens e _n_ mulheres que desejam se casar com alguém do sexo oposto. Assuma que existem _k_ homens bons e _n-k_ homens maus. Da mesma forma, existem _k_ mulheres boas e _n-k_ mulheres más. Todas as pessoas prefeririam se casar com qualquer pessoa boa do que com qualquer pessoa má. Em outras palavras, os rankings de preferências de todos incluem todas as pessoas boas (em alguma ordem) em posições mais altas do que qualquer pessoa má. Mostre que em qualquer casamento estável, todo homem bom sempre estará casado com uma mulher boa.

**Demonstração:**

1. **Hipótese da Contradição:** Suponha, por absurdo, que exista um casamento estável M onde um homem bom _m_ está casado com uma mulher má _w_.
    
2. **Existência de um Par Inverso:** Como o número de homens bons é igual ao número de mulheres boas, a existência do par (m, w) implica que deve haver pelo menos uma mulher boa _w'_ casada com um homem mau _m'_. Ou seja, o par (m', w') também pertence a M.
    
3. **Preferências Conflitantes:**
    - A mulher boa _w'_ prefere qualquer homem bom a qualquer homem mau. Portanto, _w'_ prefere _m_ (bom) a _m'_ (mau).
    - O homem bom _m_ prefere qualquer mulher boa a qualquer mulher má. Portanto, _m_ prefere _w'_ (boa) a _w_ (má).
    
1. **Instabilidade:** As preferências descritas no ponto 3 indicam que o par (m, w') forma uma instabilidade em M. Ambos _m_ e _w'_ prefeririam estar casados um com o outro do que com seus parceiros atuais em M.
    
5. **Contradição:** A existência de uma instabilidade contradiz a hipótese inicial de que M é um casamento estável.
    
6. **Conclusão:** Portanto, a suposição inicial de que um homem bom pode estar casado com uma mulher má em um casamento estável é falsa. Em qualquer casamento estável, todo homem bom estará casado com uma mulher boa.
    

### Exercício 2: Casamento Estável com Pares Proibidos

**Enunciado:** Considere uma generalização do Problema do Casamento Estável em que certos pares homem-mulher (ou hospital-estudante) são explicitamente proibidos. Em outras palavras, há um conjunto M de _n_ homens, um conjunto W de _n_ mulheres, e um conjunto F ⊆ M x W de pares que representam casamentos que não são permitidos.

Cada homem _m_ ordena todas as mulheres _w_ tal que (m,w) ∉ F, e cada mulher _w’_ ordena todos os homens _m’_ tal que (m’, w’) ∉ F.

Neste cenário mais geral, um casamento é dito estável se ele não exibe nenhuma das seguintes condições (tipos de instabilidade):

1. Há dois pares (m,w) e (m’, w’) em S com a propriedade de que (m,w’) ∉ F, _m_ prefere _w’_ a _w_ e _w’_ prefere _m_ a _m'_ (condição de instabilidade geral).
2. Há um par (m,w) ∈ S e um homem _m’_ tal que _m’_ não é parte de nenhum par no casamento S, (m’,w) ∉ F e _w_ prefere _m’_ a _m_ (homem solteiro é mais desejado e não é proibido).
3. Há um par (m,w) ∈ S e uma mulher _w’_ tal que _w’_ não é parte de nenhum par no casamento S, (m,w') ∉ F e _m_ prefere _w’_ a _w_ (mulher solteira é mais desejada e não é proibida).
4. Há um homem _m_ e uma mulher _w_, nenhum deles é parte de nenhum par no casamento S e (m,w) ∉ F (há duas pessoas solteiras sem impedimentos para se casarem).

**Tarefa:**

- Apresente um algoritmo que, para qualquer conjunto de preferências e listas de pares proibidos, produz um casamento estável.
- Prove que a solução do algoritmo sempre é um casamento estável.

**Solução:**

**Algoritmo Modificado de Gale-Shapley:**

O algoritmo de Gale-Shapley pode ser modificado para lidar com pares proibidos. A principal alteração é na condição do loop **while**.

1. **Inicialização:** Inicialize um casamento vazio _S_.
    
2. **Loop Principal:** Enquanto houver um homem _m_ que não está casado e ainda não propôs para todas as mulheres permitidas:
    
    - Selecione a mulher _w_ mais preferida por _m_ entre aquelas para quem ele ainda não propôs e *que não são proibidas (ou seja, (m,w) ∉ F).*
    - **Se** _w_ está solteira:
        - Adicione o par (m,w) ao casamento _S_.
    - **Senão Se** _w_ prefere _m_ ao seu parceiro atual _m'_:
        - Remova o par (m', w) de _S_.
        - Adicione o par (m,w) a _S_.
    - **Senão:**
        - _w_ rejeita a proposta de _m_.
3. **Retorno:** Retorne o casamento _S_.
    

**Prova de Estabilidade:**

Para provar que o algoritmo sempre produz um casamento estável, precisamos demonstrar que nenhuma das quatro condições de instabilidade pode ocorrer na solução.

1. **Condição 1 (Instabilidade Geral):** Suponha, por absurdo, que exista uma instabilidade do tipo 1, ou seja, dois pares (m,w) e (m', w') em _S_ com (m,w') ∉ F, _m_ prefere _w'_ a _w_ e _w'_ prefere _m_ a _m'_.
    
    - Se _m_ prefere _w'_ a _w_, então _m_ deve ter proposto a _w'_ antes de propor a _w_ (pois o algoritmo faz propostas em ordem decrescente de preferência).
    - Como _w'_ está casada com _m'_, ela deve ter rejeitado a proposta de _m_ para ficar com _m'_.
    - Portanto, _w'_ prefere _m'_ a _m_.
    - Isso contradiz a suposição de que _w'_ prefere _m_ a _m'_.
    
1. **Condição 2 (Homem Solteiro Preferido):** Suponha, por absurdo, que exista uma instabilidade do tipo 2, ou seja, um par (m,w) ∈ S e um homem _m’_ solteiro tal que (m',w) ∉ F e _w_ prefere _m’_ a _m_.
    
    - Se (m',w) ∉ F, então _m'_ deve ter proposto a _w_ durante o algoritmo (pois homens solteiros propõem para todas as mulheres permitidas).
    - Como _w_ está casada com _m_, ela deve ter rejeitado a proposta de _m'_ para ficar com _m_.
    - Portanto, _w_ prefere _m_ a _m'_.
    - Isso contradiz a suposição de que _w_ prefere _m'_ a _m_.
    
1. **Condição 3 (Mulher Solteira Preferida):** Suponha, por absurdo, que exista uma instabilidade do tipo 3, ou seja, um par (m,w) ∈ S e uma mulher _w’_ solteira tal que (m,w') ∉ F e _m_ prefere _w’_ a _w_.
    
    - Se _w'_ está solteira, então nenhum homem propôs a ela durante o algoritmo.
    - Particularmente, _m_ nunca propôs a _w'_.
    - Portanto, _m_ deve preferir _w_ a _w'_ (pois ele só propõe para mulheres em ordem decrescente de preferência).
    - Isso contradiz a suposição de que _m_ prefere _w'_ a _w_.
    
1. **Condição 4 (Par Solteiro Permitido):** Suponha, por absurdo, que exista uma instabilidade do tipo 4, ou seja, um homem _m_ e uma mulher _w_ solteiros com (m,w) ∉ F.
    
    - Se _m_ está solteiro, ele deve ter proposto para todas as mulheres permitidas, incluindo _w_.
    - Se _w_ recebeu uma proposta de _m_ e está solteira, ela deve ter rejeitado a proposta.
    - Isso contradiz a suposição de que ambos estão solteiros e (m,w) ∉ F.

**Conclusão:**

Como nenhuma das condições de instabilidade pode ocorrer, o algoritmo modificado de Gale-Shapley sempre produz um casamento estável, mesmo na presença de pares proibidos.
O algoritmo modificado *pode resultar em homens ou mulheres solteiros, diferentemente do algoritmo tradicional de Gale-Shapley.* Essa diferença ocorre devido à restrição adicional dos pares proibidos.
- Observação 1d na solução do exercício 2 afirma que se uma *mulher w não está em um par na solução final, nenhum homem a pediu em casamento.* Essa situação pode surgir se **todas as propostas que w poderia receber são de homens com quem ela forma um par proibido.**