from typing import List, Dict

def word_frequency(words: List[str]) -> Dict[str, int]:
    """
    Retorna um dicionário mapeando cada palavra/token
    para sua quantidade de ocorrências na lista.
    """
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
