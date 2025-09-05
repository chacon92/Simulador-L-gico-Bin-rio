# 📘 Simulador Lógico Binário

## 1. Introdução
O **Simulador Lógico Binário** é uma aplicação desenvolvida em **Python** utilizando a biblioteca **Tkinter** para interface gráfica.  

O objetivo do programa é permitir que o usuário insira dois valores inteiros (entre 0 e 15), visualize suas representações binárias de 4 bits e calcule as operações lógicas básicas:

- **AND**
- **OR**
- **XOR**
- **NOT** (apenas para A)

Essa ferramenta pode ser utilizada para fins **didáticos**, em disciplinas de lógica digital, sistemas digitais ou ciência da computação, permitindo visualizar na prática o funcionamento das operações lógicas em números binários.

---

## 2. Requisitos

### 2.1 Requisitos de Software
- Python 3.7 ou superior  
- Biblioteca Tkinter (já incluída por padrão no Python)

### 2.2 Requisitos de Hardware
- Sistema operacional compatível (Windows, Linux ou macOS)  
- Memória mínima: 512 MB RAM  
- Processador: 1 GHz ou superior  

---

## 3. Estrutura do Código
O projeto está estruturado em um único arquivo Python, contendo as seguintes partes principais:

1. **Função `to_bin4(n)`**
   - Converte um número inteiro em sua representação binária de 4 bits.  
   - Exemplo: `to_bin4(5) → "0101"`.  

2. **Função `calcular()`**
   - Responsável por:  
     - Capturar os valores inseridos pelo usuário.  
     - Validar se os valores estão entre 0 e 15.  
     - Calcular as operações lógicas binárias.  
     - Atualizar os resultados na interface gráfica.  

3. **Interface gráfica (Tkinter):**
   - Entradas para os valores A e B.  
   - Botão **Calcular**.  
   - Labels para exibir os resultados das conversões e operações.  

---

## 4. Operações Implementadas
- **AND (A & B):** Retorna 1 se ambos os bits forem 1.  
- **OR (A | B):** Retorna 1 se pelo menos um dos bits for 1.  
- **XOR (A ^ B):** Retorna 1 se os bits forem diferentes.  
- **NOT (~A & 0b1111):** Inverte os bits de A e ajusta para 4 bits.  

---

## 5. Interface Gráfica
A interface contém:  
- Campos de entrada para **Valor A** e **Valor B** (aceitam apenas números entre 0 e 15).  
- Botão **Calcular** que aciona a função `calcular()`.  
- Área de resultados mostrando:  
  - Representação binária de A e B.  
  - Resultados das operações lógicas, em binário e decimal.  

---

## 6. Exemplo de Uso

**Entrada:**
- Valor A = 5  
- Valor B = 9  

**Saída:**

- Binário A: 0101
- Binário B: 1001

**Resultados Lógicos:**
- AND: 0001 (1)
- OR: 1101 (13)
- XOR: 1100 (12)
- NOT A: 1010 (10)
  
  <img width="1342" height="763" alt="Captura de tela 2025-09-05 135322" src="https://github.com/user-attachments/assets/28008486-7a48-4e55-ba48-528db4e6a649" />

---

## 7. Instruções de Execução
1. Salve o código em um arquivo chamado, por exemplo:  
   `simulador_binario.py`  
2. Execute o programa pelo terminal/cmd:  
   ```bash
   python simulador_binario.py

---

## 8. Possíveis Melhorias Futuras

Adicionar operação NOT B.

Incluir operações NAND, NOR e XNOR.

Permitir entrada de números maiores (8 bits, 16 bits).

Exportar resultados para arquivo texto.

Melhorar a interface com cores e ícones.

---

📜 Licença

Este projeto é de uso livre.
Sinta-se à vontade para modificar, utilizar e compartilhar.


