import heapq
from typing import Dict
from .tree import Node

def build_huffman_tree(freq: Dict[str, int]) -> Node:
    """
    Build Huffman tree from frequency dict (word -> freq).
    """
    heap = []
    for word, f in freq.items():
        heapq.heappush(heap, Node(word, f))
    if not heap:
        return None
    if len(heap) == 1:
        only = heapq.heappop(heap)
        parent = Node(None, only.freq, left=only, right=None)
        return parent
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(None, a.freq + b.freq, left=a, right=b)
        heapq.heappush(heap, parent)
    return heapq.heappop(heap)
