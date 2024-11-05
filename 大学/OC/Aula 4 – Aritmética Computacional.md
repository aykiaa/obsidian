## Operações em complemento de 2
O complemento de dois é um método para representar *números negativos em sistemas binários.* Ele aborda as limitações de outros métodos, como sinal-magnitude e complemento de um, oferecendo vantagens em termos de equilíbrio, número de zeros e, principalmente, **facilidade de realizar operações aritméticas**.

No complemento de dois, *o bit mais significativo representa o sinal do número: 0 para positivo e 1 para negativo.* Para números positivos, a representação é a mesma da forma binária padrão.

**Para obter a representação em complemento de dois de um número negativo, você pode seguir estes passos:**

1. **Inverter todos os bits** do número positivo correspondente.
2. **Somar 1** ao resultado da inversão.

Por exemplo, para representar -6 em complemento de dois (usando 4 bits):

1. Começamos com a representação binária de +6: `0110`
2. Invertemos todos os bits: `1001`
3. Somamos 1: `1010`

Portanto, -6 em complemento de dois é representado por `1010`.

**Vantagens do complemento de dois:**

- **Simplifica as operações aritméticas**, permitindo que a adição e a subtração sejam realizadas com a mesma lógica de circuito.
- **Elimina a ambiguidade de ter duas representações para zero**, presente no método sinal-magnitude.
- **Oferece um intervalo de representação simétrico** para números positivos e negativos.

Com o complemento de dois, *a adição e a subtração são realizadas como se os números fossem positivos*, ignorando o bit de sinal. O resultado estará na forma de complemento de dois.

### Overflow
Um overflow ocorre quando o *resultado de uma operação aritmética excede o limite de representação do sistema.* 
O termo "overflow" refere-se especificamente ao número que ultrapassa o limite de representação, não ao carry que pode ocorrer durante o cálculo.

Em complemento de dois, um overflow pode ser detectado quando;
- POSITIVO + POSITIVO = NEGATIVO
- NEGATIVO + NEGATIVO = POSITIVO
- POSITIVO - NEGATIVO = NEGATIVO
- NEGATIVO - POSITIVO = POSITIVO

**Exemplo de Overflow:**

Suponha que estejamos trabalhando com números de 4 bits em complemento de dois. O maior número positivo representável é *0111 (+7)* e o menor número negativo é *1000 (-8)*. Se somarmos +7 e +1, o resultado aritmético é +8. No entanto, +8 não pode ser representado em complemento de dois com 4 bits. O resultado da soma binária seria 1000, que em complemento de dois representa -8. Isso é um overflow!

**Para detectar um overflow:**

- **Arquiteturas de Computadores:** Utilizam **exceções** (interrupções). Quando um overflow ocorre, o controle do programa salta para um endereço predefinido, interrompendo o fluxo normal de execução. O endereço interrompido é salvo para um possível retorno após o tratamento da exceção.
- **Software e Linguagens de Programação:** Os detalhes de como o overflow é tratado e sinalizado dependem do software e da linguagem de programação utilizada.


**Observações Importantes:**

- O conceito de overflow está diretamente ligado à forma como os números são representados no computador, principalmente em complemento de dois, que é o método mais utilizado.
- A detecção e tratamento de overflow são cruciais para garantir a confiabilidade dos programas, evitando resultados inesperados e erros de cálculo.




## Multiplicacao de Binarios

 Assim como na multiplicação decimal, o processo é realizado através de uma série de passos que combinam multiplicações parciais e deslocamentos para gerar o produto final.

**1. Processo Básico:**

- O processo se assemelha à multiplicação decimal, onde cada bit do multiplicador é multiplicado pelo multiplicando.
- Os resultados parciais (0 ou o multiplicando) são deslocados para a esquerda de acordo com a posição do bit no multiplicador.
- Os resultados deslocados são somados para obter o produto final.

**2. Exemplo Ilustrativo:**

Para ilustrar, vamos multiplicar os números binários 1000 (multiplicando) por 1001 (multiplicador):

```
    1000   (multiplicando) 8
x   1001   (multiplicador) 9
---------
    1000   (1000 x 1)
   0000    (1000 x 0, deslocado 1 posição à esquerda)
  0000     (1000 x 0, deslocado 2 posições à esquerda)
 1000      (1000 x 1, deslocado 3 posições à esquerda)
---------
 1001000  (produto final) 72
```

**3. Implementação em Hardware:**

- A multiplicação binária é implementada em hardware utilizando circuitos lógicos, como somadores e deslocadores.
- O processo pode ser otimizado para reduzir o número de operações e o tempo de execução.

**4. Versão Otimizada:**

Uma versão otimizada do processo de multiplicação, descrita nas fontes, utiliza um registrador de produto que acumula os resultados parciais. O algoritmo segue estes passos:

1. **Inicialização:** O registrador de produto é inicializado com zero.
2. **Teste:** Verifica-se o bit menos significativo do multiplicador.
    - Se for 1, o multiplicando é somado à metade esquerda do registrador de produto.
3. **Deslocamento:** O registrador de produto é deslocado um bit para a direita.
4. **Repetição:** Os passos 2 e 3 são repetidos para cada bit do multiplicador.
5. **Conclusão:** Após a última iteração, o registrador de produto conterá o produto final.

**5. Multiplicação no RISC-V:**

A arquitetura RISC-V oferece quatro instruções para multiplicação:

- **`mul`:** Retorna os 64 bits menos significativos do produto.
- **`mulh`:** Retorna os 64 bits mais significativos do produto, assumindo operandos com sinal.
- **`mulhu`:** Retorna os 64 bits mais significativos do produto, assumindo operandos sem sinal.
- **`mulhsu`:** Retorna os 64 bits mais significativos do produto, assumindo um operando com sinal e outro sem sinal.

**6. Números Negativos:**

A *multiplicação de números negativos em binário pode ser realizada convertendo os números para complemento de dois* e, em seguida, multiplicando como se fossem positivos. O resultado final será ajustado para refletir o sinal correto.

**7. Considerações Adicionais:**

- As fontes destacam que a velocidade do hardware é influenciada pelo número de portas lógicas e pela organização do circuito. A multiplicação, sendo mais complexa, exige mais portas e, consequentemente, pode ser mais lenta que operações como adição.
- A otimização da multiplicação binária em hardware visa minimizar o número de portas e a propagação do sinal para aumentar a velocidade de processamento.
