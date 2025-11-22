from typing import Optional

class Node:
    def __init__(self, word: Optional[str], freq: int, left: 'Node' = None, right: 'Node' = None):
        self.word = word
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return self.word is not None

    def __lt__(self, other: 'Node'):
        return self.freq < other.freq
