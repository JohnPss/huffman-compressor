"""
Programa principal para compressão de textos utilizando o algoritmo de Huffman.

Este módulo:
    • Lê textos presentes no arquivo data/input.dat
    • Tokeniza cada texto
    • Calcula as frequências
    • Constrói a árvore de Huffman
    • Gera os códigos binários
    • Comprime o texto original
    • Gera o arquivo data/output.dat contendo:
        - Árvore de Huffman (formato textual)
        - Códigos gerados para cada token
        - Texto comprimido
        - Metadados necessários para decodificação

O programa deve ser executado via linha de comando e atende aos requisitos
do trabalho acadêmico de compressão sem perdas.
"""

import os
from huffman import tokenize, word_frequency, build_huffman_tree
from huffman import generate_codes, compress_words, serialize_tree


INPUT_PATH = "data/input.dat"
OUTPUT_PATH = "data/output.dat"


def read_input_file() -> str:
    """Lê o arquivo de entrada e valida sua existência e conteúdo."""
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Arquivo '{INPUT_PATH}' não encontrado.")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        raise ValueError("O arquivo input.dat está vazio.")

    return content


def process_text_block(text: str) -> str:
    """Processa um bloco de texto aplicando o algoritmo de Huffman."""

    # Tokenização
    tokens = tokenize(text)
    if not tokens:
        raise ValueError("Nenhum token encontrado no texto.")

    # Frequências
    freq = word_frequency(tokens)

    # Construção da árvore
    root = build_huffman_tree(freq)
    if root is None:
        raise RuntimeError("Falha ao construir a árvore de Huffman.")

    # Geração dos códigos
    codes = generate_codes(root)

    # Compressão
    compressed = compress_words(tokens, codes)

    # Serialização da árvore
    tree_text = serialize_tree(root)

    # Formatação do bloco para o output
    block_output = []
    block_output.append("=== ÁRVORE DE HUFFMAN ===")
    block_output.append(tree_text)
    block_output.append("\n=== CÓDIGOS ===")
    for word, code in codes.items():
        block_output.append(f"{word}: {code}")
    block_output.append("\n=== TEXTO COMPRIMIDO ===")
    block_output.append(compressed)
    block_output.append("\n=== METADADOS ===")
    block_output.append(f"Total de tokens: {len(tokens)}")
    block_output.append(f"Total de códigos: {len(codes)}")
    block_output.append("\n--------------------------------------\n")

    return "\n".join(block_output)


def write_output_file(content: str):
    """Escreve o arquivo de saída com tratamento de erros."""
    try:
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        raise IOError(f"Erro ao escrever '{OUTPUT_PATH}': {e}")


def main():
    print("Iniciando compressão de texto com Huffman...\n")

    # 1. Ler input.dat
    raw = read_input_file()

    # 2. Separar os textos por linha em branco
    blocks = [b.strip() for b in raw.split("\n\n") if b.strip()]
    if not blocks:
        raise ValueError("Nenhum bloco de texto válido foi encontrado no input.dat.")

    # 3. Processar cada bloco individualmente
    output_blocks = []
    for index, block in enumerate(blocks, start=1):
        print(f"Processando texto {index}...")
        result = process_text_block(block)
        output_blocks.append(result)

    # 4. Gerar output.dat
    final_output = "\n".join(output_blocks)
    write_output_file(final_output)

    print("\nProcesso concluído!")
    print(f"Arquivo gerado: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
