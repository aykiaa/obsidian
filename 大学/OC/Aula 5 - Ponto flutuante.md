### Resolução da Questão 4 (Formato de Ponto Flutuante)

---

### **Introdução:**
Nesta anotação, revisaremos os conceitos e passos necessários para resolver problemas relacionados à **representação de números em ponto flutuante**. A estrutura apresentada segue o formato especificado:

- **Sinal:** 1 bit  
- **Expoente:** 5 bits (peso 15)  
- **Fração:** 8 bits  

---

## **Passo a Passo para Resolver a Questão 4**

### **1. Letra (a): Representação no formato científico normalizado**

#### **Objetivo:**  
Normalizar os números $X$ e $Y$ em formato de sinal-fração-potência.

#### **Passos:**
1. **Número $X = -7,25$:**  
   - Converter para binário:  
     $-7,25_{10} = -111,01_2$  
   - Normalizar (deixar na forma $1,XX... \times 2^n$):  
     $-111,01_2 = -1,1101_2 \times 2^2$

2. **Número $Y = 3,5$:**  
   - Converter para binário:  
     $3,5_{10} = 11,1_2$  
   - Normalizar:  
     $11,1_2 = 1,11_2 \times 2^1$

---

### **2. Letra (b): Representação no formato de ponto flutuante**

#### **Objetivo:**  
Escrever os números $X$ e $Y$ no formato de ponto flutuante, conforme o esquema:

$$
\text{Sinal (1 bit)} \ | \ \text{Expoente (5 bits)} \ | \ \text{Fração (8 bits)}
$$

#### **Passos:**
1. **Para $X = -7,25$:**  
   - Sinal $S = 1$ (número negativo)  
   - Expoente ajustado:  
     $$
     E = 2 + 15 = 17 \quad \Rightarrow \quad 17_{10} = 10001_2
     $$
   - Fração:  
     $$
     1,1101 \quad \text{(preencher até 8 bits)} \quad \Rightarrow \quad 11010000
     $$  
   **Representação:**  
   $$
   X = 1 \ | \ 10001 \ | \ 11010000
   $$

2. **Para $Y = 3,5$:**  
   - Sinal $S = 0$ (número positivo)  
   - Expoente ajustado:  
     $$
     E = 1 + 15 = 16 \quad \Rightarrow \quad 16_{10} = 10000_2
     $$
   - Fração:  
     $$
     1,11 \quad \text{(preencher até 8 bits)} \quad \Rightarrow \quad 11000000
     $$  
   **Representação:**  
   $$
   Y = 0 \ | \ 10000 \ | \ 11000000
   $$

---

### **3. Letra (c): Multiplicação $X \times Y$**

#### **Objetivo:**  
Multiplicar os números no formato normalizado e ajustar o resultado ao formato de ponto flutuante.

#### **Passos:**
1. **Valores normalizados:**  
   $$
   X = -1,1101_2 \times 2^2
   $$  
   $$
   Y = 1,11_2 \times 2^1
   $$

2. **Multiplicação das frações:**  
   $$
   (-1,1101_2) \times (1,11_2) = -1,11011010_2
   $$  
   - Resultado tem 9 bits: $1,11011010_2$.  
   - **Truncar** para 8 bits (remover o último bit):  
     $$
     1,1101101_2
     $$

3. **Soma dos expoentes:**  
   $$
   (2 + 1) = 3
   $$

4. **Resultado final:**  
   $$
   -1,1101101_2 \times 2^3
   $$

---

### **4. Letra (d): Exemplos de Overflow e Underflow**

#### **Objetivo:**  
Demonstrar situações onde ocorrem **overflow** e **underflow**.

#### **Definições:**
- **Overflow:** Ocorre quando o expoente ultrapassa o valor máximo permitido ($E_{\text{max}} = 31$).  
- **Underflow:** Ocorre quando o expoente é menor que o valor mínimo permitido ($E_{\text{min}} = 0$).

#### **Exemplo de Overflow:**  
1. Valor máximo de expoente ajustado: $E = 31$, obtido pois em 5 bits temos 16 + 8 + 4 + 2 + 1 = 31
2. Representação máxima:  
   $$
   1,1111111_2 \times 2^{16}
   $$  
3. **Overflow ocorre** para qualquer número com expoente maior:  
   $$
   1,0000000_2 \times 2^{17}
   $$

#### **Exemplo de Underflow:**  
1. Valor mínimo de expoente ajustado: $E = 0$.  
2. Representação mínima:  
   $$
   1,0000000_2 \times 2^{-15}
   $$  
3. **Underflow ocorre** para qualquer número com expoente menor:  
   $$
   1,0000000_2 \times 2^{-16}
   $$

---

### **Conclusão:**  

