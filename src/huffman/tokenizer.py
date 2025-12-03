from typing import List

def tokenize(text: str) -> List[str]:
    """
    Tokenização simples por espaços em branco (whitespace).
    Qualquer coisa entre espaços é considerada um 'token' inteiro.
    Exemplo: 'Olá, mundo!' -> ['Olá,', 'mundo!']
    """
    # .split() sem argumentos divide por qualquer espaço em branco (espaço, tab, enter)
    # e remove espaços vazios do resultado.
    return text.split()