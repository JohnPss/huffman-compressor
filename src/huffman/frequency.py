from typing import List, Dict

def word_frequency(words: List[str]) -> Dict[str, int]:
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
