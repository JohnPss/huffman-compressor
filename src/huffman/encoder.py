from typing import Dict, List
from .tree import Node

def generate_codes(root: Node) -> Dict[str, str]:
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
    return "".join(codes[w] for w in words)
