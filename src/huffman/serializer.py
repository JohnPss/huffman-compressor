import json
from .tree import Node

def serialize_tree(root: Node) -> str:
    parts = []
    def dfs(node: Node):
        if node is None:
            return
        if node.is_leaf():
            parts.append("1")
            parts.append(json.dumps({"word": node.word, "freq": node.freq}, ensure_ascii=False))
        else:
            parts.append("0")
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return "\n".join(parts)
