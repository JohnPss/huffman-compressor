from typing import Optional

class Node:
    """
    Representa um nó da árvore de Huffman.
    Folhas possuem uma palavra/token; nós internos possuem soma de frequências.
    """

    def __init__(self, word: Optional[str], freq: int, left: 'Node' = None, right: 'Node' = None):
        self.word = word
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        """Retorna True se o nó contém uma palavra/token."""
        return self.word is not None

    def __lt__(self, other: 'Node'):
        """Permite comparação por frequência para uso em heap."""
        return self.freq < other.freq
