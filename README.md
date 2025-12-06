# 📦 Huffman Text Compressor

> Implementação modular do Algoritmo de Huffman para compressão de textos sem perdas (lossless) baseada em frequência de palavras.

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=flat&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/JohnPss/huffman-compressor)

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como trabalho prático da disciplina de **Algoritmos e Estruturas de Dados** do CEFET-MG. O objetivo é implementar um compressor de texto utilizando o **Algoritmo de Huffman**, uma técnica de codificação estatística que atribui códigos binários de tamanho variável aos símbolos com base em suas frequências de ocorrência.

### 🎯 Diferencial: Compressão Baseada em Palavras

Diferente das implementações tradicionais que operam em nível de **caracteres**, este compressor trabalha com **palavras completas** como unidade básica de codificação. Essa abordagem é particularmente eficiente para textos com alta recorrência de termos específicos, como documentos técnicos, artigos científicos ou textos repetitivos.

**Exemplo:**
- **Tradicional (caracteres)**: `"dado"` = 4 símbolos distintos
- **Este projeto (palavras)**: `"dado dado dado"` = 1 símbolo com frequência 3

---

## ✨ Funcionalidades Principais

- ✅ **Tokenização Inteligente**: Separa palavras e pontuação de forma independente
- ✅ **Construção de Árvore de Huffman**: Implementação eficiente usando heap (fila de prioridade)
- ✅ **Geração de Códigos Otimizados**: Códigos binários mais curtos para palavras mais frequentes
- ✅ **Visualização da Árvore**: Representação ASCII art da estrutura hierárquica
- ✅ **Compressão de Múltiplos Textos**: Processa vários blocos de texto em um único arquivo
- ✅ **Saída Estruturada**: Arquivo `output.dat` com árvore, códigos e texto comprimido
- ✅ **Sem Dependências Externas**: Utiliza apenas a biblioteca padrão do Python

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.6** ou superior
- Sistema operacional: Linux (testado no Ubuntu 24.04), macOS ou Windows

### Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JohnPss/huffman-compressor.git
   cd huffman-compressor
   ```

2. **Execute o compressor:**
   ```bash
   python3 src/main.py
   ```

   **Saída esperada:**
   ```
   Iniciando compressão de texto com Huffman...

   Processando texto 1...
   Processando texto 2...
   Processando texto 3...

   Processo concluído!
   Arquivo gerado: data/output.dat
   ```

3. **Verifique o resultado:**
   ```bash
   cat data/output.dat
   ```

---

## 📂 Estrutura do Projeto

```
huffman-compressor/
│
├── data/                          # Diretório de dados
│   ├── input.dat                  # Arquivo de entrada (textos separados por linha em branco)
│   └── output.dat                 # Arquivo de saída (gerado pelo programa)
│
├── src/                           # Código-fonte
│   ├── main.py                    # Ponto de entrada do programa
│   └── huffman/                   # Pacote modular do compressor
│       ├── __init__.py            # Exporta as funções públicas
│       ├── tree.py                # Classe Node (nó da árvore)
│       ├── tokenizer.py           # Tokenização de texto
│       ├── frequency.py           # Cálculo de frequências
│       ├── builder.py             # Construção da árvore de Huffman
│       ├── encoder.py             # Geração de códigos e compressão
│       └── serializer.py          # Serialização visual da árvore
│
├── requirements.txt               # Dependências (vazio - só stdlib)
└── README.md                      # Este arquivo
```

---

## 🧠 Como Funciona o Algoritmo

### 1️⃣ Tokenização
O texto é dividido em **tokens** (palavras e pontuação):

```python
Entrada:  "O computador executa instruções."
Saída:    ['O', 'computador', 'executa', 'instruções', '.']
```

**Decisão de Design:** A pontuação é separada das palavras para aumentar a taxa de compressão. Por exemplo, `"teste."` e `"teste"` são consideradas a mesma palavra base.

### 2️⃣ Cálculo de Frequências
Conta quantas vezes cada token aparece:

```python
{'O': 1, 'computador': 1, 'executa': 1, 'instruções': 1, '.': 1}
```

### 3️⃣ Construção da Árvore de Huffman
Algoritmo guloso que constrói a árvore binária:

1. Cria um nó folha para cada token
2. Insere todos em uma **fila de prioridade** (heap)
3. Enquanto houver mais de um nó:
   - Remove os dois nós de **menor frequência**
   - Cria um nó pai com **frequência = soma dos filhos**
   - Insere o pai de volta na fila
4. O último nó restante é a **raiz**

**Complexidade:** O(n log n), onde n = número de tokens únicos

### 4️⃣ Geração de Códigos
Percorre a árvore atribuindo códigos binários:

- **Filho esquerdo**: adiciona `0`
- **Filho direito**: adiciona `1`

```
Palavra        | Frequência | Código
---------------|------------|-------
O              | 1          | 0110
computador     | 1          | 1110
executa        | 1          | 0111
.              | 1          | 1001
```

Palavras mais frequentes ficam mais próximas da raiz (códigos menores).

### 5️⃣ Compressão
Substitui cada palavra pelo seu código binário:

```
Texto original:    "O computador executa."
Texto comprimido:  01101110011110101001
```

---

## 📊 Exemplo de Saída

### Estrutura da Árvore (ASCII Art)
```
[RAIZ] (Total: 13)
├── 0: [5]
│   ├── 0: [2]
│   │   ├── 0: 'precisão' (1)
│   │   └── 1: 'alta' (1)
│   └── 1: [3]
│       ├── 0: 'e' (1)
│       └── 1: [2]
│           ├── 0: 'O' (1)
│           └── 1: 'executa' (1)
└── 1: [8]
    ├── 0: [4]
    │   ├── 0: [2]
    │   │   ├── 0: 'velocidade' (1)
    │   │   └── 1: '.' (1)
    │   └── 1: [2]
    │       ├── 0: 'processa' (1)
    │       └── 1: 'instruções' (1)
    └── 1: [4]
        ├── 0: [2]
        │   ├── 0: 'com' (1)
        │   └── 1: 'dados' (1)
        └── 1: [2]
            ├── 0: 'computador' (1)
            └── 1: 'em' (1)
```

### Tabela de Códigos
```
precisão: 000
alta: 001
e: 010
O: 0110
executa: 0111
velocidade: 1000
.: 1001
processa: 1010
instruções: 1011
com: 1100
dados: 1101
computador: 1110
em: 1111
```

### Texto Comprimido
```
0110111001111011111100110000101010110111000001001
```

---

## 🛠️ Decisões de Implementação

### 1. Por que separar pontuação das palavras?

**Problema:** Se mantivermos pontuação anexada, `"teste"` e `"teste."` seriam tokens diferentes.

**Solução:** Separar pontuação aumenta a recorrência de palavras, melhorando a compressão.

**Regex utilizado:**
```python
re.findall(r'\w+|[^\w\s]', text)
```
- `\w+`: captura palavras (letras, números, _)
- `[^\w\s]`: captura pontuação (qualquer coisa que não seja palavra nem espaço)
- **Resultado:** espaços são ignorados automaticamente

### 2. Por que usar heap (heapq)?

O algoritmo de Huffman precisa sempre pegar os **dois nós de menor frequência**. Um heap (min-heap) permite isso em **O(log n)** por operação, tornando o algoritmo eficiente.

### 3. Por que arquitetura modular?

Separar o código em módulos (`tokenizer`, `frequency`, `builder`, etc.) facilita:
- ✅ Manutenção
- ✅ Testes unitários
- ✅ Reutilização de código
- ✅ Compreensão do fluxo

### 4. Por que gerar visualização ASCII da árvore?

A prática exige que o `output.dat` contenha a estrutura da árvore em formato textual. A visualização ASCII:
- É legível por humanos
- Facilita debugging
- Permite reconstruir a árvore manualmente se necessário

---

## 📝 Formato do Arquivo de Entrada

O arquivo `data/input.dat` deve conter textos separados por **linhas em branco**:

```
O computador executa instruções em alta velocidade e processa dados com precisão.

A memória armazena informações que são acessadas rapidamente pela CPU.

Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador.
```

**Regras:**
- Cada bloco de texto será processado independentemente
- Linhas em branco delimitam os blocos
- Codificação: UTF-8

---

## 📈 Análise de Complexidade

| Operação                  | Complexidade | Justificativa                          |
|---------------------------|--------------|----------------------------------------|
| Tokenização               | O(n)         | Percorre o texto uma vez               |
| Cálculo de frequências    | O(n)         | Percorre a lista de tokens             |
| Construção da árvore      | O(k log k)   | k inserções/remoções no heap           |
| Geração de códigos        | O(k)         | Travessia DFS da árvore                |
| Compressão                | O(n)         | Substitui cada token pelo código       |
| **Total**                 | **O(n + k log k)** | n = tokens, k = tokens únicos |

Para textos com alta repetição, k << n, então a complexidade se aproxima de **O(n)**.

---

## 🎓 Conceitos Aplicados

Este projeto demonstra os seguintes conceitos de Estruturas de Dados:

1. **Árvores Binárias**: Estrutura hierárquica com nós e folhas
2. **Heap (Fila de Prioridade)**: Estrutura eficiente para mínimos/máximos
3. **Algoritmos Gulosos**: Huffman sempre escolhe os dois menores
4. **Travessia de Árvores (DFS)**: Geração dos códigos binários
5. **Dicionários (Hash Tables)**: Armazenamento de frequências e códigos
6. **Modularização**: Separação de responsabilidades (SOLID)

---

## 🧪 Testando o Projeto

### Teste 1: Texto Simples
```bash
echo "dado dado dado" > data/input.dat
python3 src/main.py
cat data/output.dat
```

**Resultado esperado:** `'dado'` deve ter frequência 3 e código curto (ex: `0`)

### Teste 2: Texto com Pontuação
```bash
echo "Olá, mundo! Olá, Python!" > data/input.dat
python3 src/main.py
cat data/output.dat
```

**Resultado esperado:** `'Olá'` e `','` devem ser tokens separados

### Teste 3: Múltiplos Textos
```bash
cat > data/input.dat << EOF
Texto um.

Texto dois.

Texto três.
EOF
python3 src/main.py
cat data/output.dat
```

**Resultado esperado:** 3 blocos separados no output

---

## 🐛 Resolução de Problemas

### Problema: `ModuleNotFoundError: No module named 'huffman'`
**Solução:** Execute sempre a partir do diretório raiz:
```bash
cd huffman-compressor
python3 src/main.py
```

### Problema: `FileNotFoundError: 'data/input.dat' não encontrado`
**Solução:** Crie o arquivo ou verifique se está no diretório correto:
```bash
ls data/input.dat
```

### Problema: Output vazio ou texto não separado
**Solução:** Certifique-se de que os textos estão separados por **linha em branco**

---

## 📚 Referências

- **Huffman, D. A.** (1952). "A Method for the Construction of Minimum-Redundancy Codes". *Proceedings of the IRE*.
- **Cormen, T. H., et al.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. Capítulo 16.3: Huffman codes.
- **Documentação Python**: [heapq](https://docs.python.org/3/library/heapq.html) e [re](https://docs.python.org/3/library/re.html)

---

## 👨‍💻 Autor

**João Pedro Siqueira**  
Engenharia de Computação - CEFET-MG  
📧 Email: joaopedrosilvasiqueira1@gmail.com
🔗 GitHub: [@JohnPss](https://github.com/JohnPss)

**Disciplina:** Algoritmos e Estruturas de Dados  
**Professor:** Michel Pires

