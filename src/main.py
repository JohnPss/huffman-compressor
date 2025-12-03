#!/usr/bin/env python3
"""
main.py - CLI entrypoint for the modular Huffman compressor.
"""
import os
from huffman import tokenize, word_frequency, build_huffman_tree, generate_codes, compress_words, serialize_tree

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
INPUT_PATH = os.path.normpath(os.path.join(DATA_DIR, "input.dat"))
OUTPUT_PATH = os.path.normpath(os.path.join(DATA_DIR, "output.dat"))

def load_texts(path: str):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    parts = [p.strip() for p in __import__("re").split(r'\n\s*\n', raw) if p.strip()]
    return parts

def save_output(path, results):
    import json
    with open(path, "w", encoding="utf-8") as f:
        for i, (ser, codes, comp) in enumerate(results, start=1):
            f.write(f"--- Texto {i} ---\n\n")
            f.write("Estrutura da Árvore (Serializada):\n")
            f.write(ser + "\n\n")
            f.write("Códigos (palavra -> código):\n")
            for w, c in sorted(codes.items(), key=lambda x: (-len(x[1]), x[0])):
                f.write(f"{w} -> {c}\n")
            f.write("\nTexto comprimido (bitstring):\n")
            f.write(comp + "\n\n")
            f.write("Informações para decodificação:\n")
            f.write("tokenization: Standard whitespace split; punctuation remains attached to words.\n")            
            f.write("codes_json:\n")
            f.write(json.dumps(codes, ensure_ascii=False) + "\n\n")

def main():
    try:
        texts = load_texts(INPUT_PATH)
    except FileNotFoundError:
        print(f"Arquivo {INPUT_PATH} não encontrado. Crie data/input.dat com os textos separados por linha em branco.")
        return

    results = []
    for text in texts:
        words = tokenize(text)
        freq = word_frequency(words)
        tree = build_huffman_tree(freq)
        codes = generate_codes(tree)
        comp = compress_words(words, codes)
        ser = serialize_tree(tree)
        results.append((ser, codes, comp))

    save_output(OUTPUT_PATH, results)
    print(f"Processados {len(results)} textos. Saída gravada em {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
