from typing import Dict, List
from .tree import Node

def generate_codes(root: Node) -> Dict[str, str]:
    """
    Gera os códigos binários de Huffman percorrendo a árvore.
    Folhas recebem o código acumulado ao longo do caminho.
    """
    codes = {}

    def dfs(node: Node, prefix: str):
        if node is None:
            return
        if node.is_leaf():
            codes[node.word] = prefix or "0"
            return
        dfs(node.left, prefix + "0")
        dfs(node.right, prefix + "1")

    dfs(root, "")
    return codes


def compress_words(words: List[str], codes: Dict[str, str]) -> str:
    """
    Comprime uma lista de palavras/tokens concatenando seus códigos.
    """
    return "".join(codes[w] for w in words)
