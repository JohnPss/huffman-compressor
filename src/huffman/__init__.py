"""
huffman package - modular implementation for the Huffman compressor project.
"""
from .tree import Node
from .tokenizer import tokenize
from .frequency import word_frequency
from .builder import build_huffman_tree
from .encoder import generate_codes, compress_words
from .serializer import serialize_tree
