import heapq
from typing import Dict
from .tree import Node

def build_huffman_tree(freq: Dict[str, int]) -> Node:
    """
    Constrói a árvore de Huffman a partir de um dicionário
    de frequências. Retorna o nó raiz.

    Cada palavra/token se torna uma folha, e nós internos
    representam a soma das frequências dos filhos.
    """
    heap = []
    for word, f in freq.items():
        heapq.heappush(heap, Node(word, f))

    if not heap:
        return None

    if len(heap) == 1:
        only = heapq.heappop(heap)
        return Node(None, only.freq, left=only)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(None, a.freq + b.freq, left=a, right=b)
        heapq.heappush(heap, parent)

    return heapq.heappop(heap)
