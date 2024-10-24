

There are 2 types of encryption **DES** e **AES**, both are symmetric 

## DES
Por ser simetrica, utiliza-se uma mesma chave
Opera em blocos de **64 bits**, onde a msg passa por um processo de permutacoes, utilizzando a rede de Feistel
- **Problema:** vulneralvel a Brute Force, devido ao tamanho da chave(**56 bits fixo**) e reconhecimento de padroes.

## AES
Blocos de 128 bits
Uso de permutacoes, substituticoes e  transformacoes matematicas
Grande tamanho de chave: **128,192,256 bits**
- 128 bits: 10 rodadas
- 192 bits: 12 rodadas
- 256 bits: 14 rodadas
Ex: WPA2, SSL
Muito seguro devido ao tamanho da chave e o uso de varias rodadas

As principais diferenças são:

- **Tamanho da chave:** DES usa 56 bits, AES usa 128, 192 ou 256 bits.
- **Segurança:** DES é considerado inseguro hoje, enquanto AES é altamente seguro.
- **Estrutura:** DES usa uma rede de Feistel, AES usa uma rede de substituição-permutação.
- **Velocidade:** AES é mais rápido e eficiente em plataformas modernas.
- **Uso:** DES está obsoleto, AES é o padrão atual de criptografia.

AES é mais seguro e amplamente utilizado.
