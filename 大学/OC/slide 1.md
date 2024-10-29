**Pseudo-instrucoes**: sao instruções que ajudam o computar a compilar o programa, como aonde armazenar variáveis.
tags: #ufmg/oc

Para representar números negativos existem 3 propostas: 
	1. Sinal Magnitude
	2. Complemento de 1
	3. Complemento de 2 **(COBRADO NA PROVA)** -> aprender a fazer perto da prova

**Passo a passo -  Complemento de 2**
1. Passar o numero para binário 
2. Fazer o complemento de 1: que é inverter os numeros, ou seja, o que é 0 -> 1 e 1-> 0
3. Somar mais um


### Tipos de Instruções
- **Tipo R:**
	- **Aritmeticas** e **logicas** entre 2 registradores
	- 2 regs de origem (RS1 E RS2) e um reg de destino (RD)
	- operaçoes que envvolvem somente registradores
	- Ex: **ADICAO, SUBTRACAO E MULTIPLICACAO**
			**```add x1, x2, x3```**

- **Tipo I:**
	- **Aritméticas com constantes**, carregamento de dados da memória (instruções **load**), **operações lógicas** com imediato.
	- Reg de origem (RS1), um imediato (valor constante) e destino (RD)
	- EX: **la, addi, andi, beq, bne**
		**``addi x1, x2, 10**
- **Tipo S:**
	- Eh o store stype
	- Armazena dados na memoria (store)
	- armazenar valores de registradores na memória
	- EX: **store, load, sw, sd, **
		```sd x5, 24(x10)```

### Operações Lógicas
1. AND: and, andi
2. OR: or, ori 
3. XOR: xor, xori

### Operações Condicionais
- Desvia para a instrução marcada no final da operação (L1)
1. **beq** rs1, rs2, L1: se rs1 == rs2 desvia para a instrução L1
2. **bne** rs1, rs2, L1: se rs1 != rs2
3. **blt** rs1, rs2, L1: se rs1 < rs2
4. **bge** rs1, rs2, L1: se rs1 >= rs2
![[Pasted image 20241011114727.png]]![[Pasted image 20241011115015.png


### Comandos RISC-V com Funções e Exemplos em C

  

#### 1. `addi` (Add Immediate)

- **Função**: Adiciona um valor imediato ao registrador de origem e armazena o resultado em um registrador de destino.

- **Exemplo em RISC-V**:

```assembly

addi t0,zero,0 // i = 0

```

- **Exemplo em C**:

```c

int i = 0;

```


#### 2. `sw` (Store Word)

- **Função**: Armazena o conteúdo de um registrador em uma posição de memória.

- **Exemplo em RISC-V**:

```assembly

sw ra, 0(sp) // salva o endereço de retorno

```

- **Exemplo em C**:

Usado internamente pelo compilador para salvar o endereço de retorno na pilha.

  

#### 3. `slli` (Shift Left Logical Immediate)

- **Função**: Faz o deslocamento lógico à esquerda de um valor no registrador por uma quantidade de bits especificada por um imediato.

- **Exemplo em RISC-V**:

```assembly

slli t1,t0,3 // t1 = i * 8

```

- **Exemplo em C**:

```c

t1 = i * 8;

```

  

#### 4. `add` (Add)

- **Função**: Adiciona dois registradores e armazena o resultado em um registrador de destino.

- **Exemplo em RISC-V**:

```assembly

add t2,a0,t1 // t2 = endereço de array[i]

```

- **Exemplo em C**:

```c

t2 = &array[i];

```

  

#### 5. `sd` (Store Double Word)

- **Função**: Armazena um valor de 64 bits (double word) da memória a partir de um registrador.

- **Exemplo em RISC-V**:

```assembly

sd zero,0(t2) // array[i] = 0

```

- **Exemplo em C**:

```c

array[i] = 0;

```

  

#### 6. `blt` (Branch if Less Than)

- **Função**: Faz uma comparação entre dois registradores e desvia para um rótulo se a condição for verdadeira.

- **Exemplo em RISC-V**:

```assembly

blt t0,a1,loop1 // se (t0 < a1) vai para loop1

```

- **Exemplo em C**:

```c

if (i < size) goto loop1;

```

  

#### 7. `lw` (Load Word)

- **Função**: Carrega um valor de 32 bits da memória para um registrador.

- **Exemplo em RISC-V**:

```assembly

lw ra, 0(sp) // carrega ra da pilha

```

- **Exemplo em C**:

Usado para restaurar o endereço de retorno salvo.

  

#### 8. `bltu` (Branch if Less Than Unsigned)

- **Função**: Compara dois registradores como valores não assinados e desvia se o primeiro for menor que o segundo.

- **Exemplo em RISC-V**:

```assembly

bltu t0,t2,loop2 // se (t0 < t2) vai para loop2

```

- **Exemplo em C**:

```c

if (p < &array[size]) goto loop2;

```

  

---

  

## Exemplo de Funções em C

  

### `clear1` em C:

```c

void clear1(int array[], int size) {

for (int i = 0; i < size; i++) {

array[i] = 0;

}

}

```

  

### `clear2` em C (usando ponteiros):

```c

void clear2(int *array, int size) {

int *p;

for (p = array; p < array + size; p++) {

*p = 0;

}

}

```

  

Essas funções C correspondem às operações em RISC-V, que iteram sobre o array e definem todos os elementos como 0, usando aritmética de ponteiros e manipulação de endereços diretamente.

