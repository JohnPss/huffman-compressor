import re
from typing import List

def tokenize(text: str) -> List[str]:
    """
    Divide o texto em palavras e sinais de pontuação, preservando a ordem.
    Palavras são sequências alfanuméricas; pontuações são tokens individuais.

    Exemplo:
        "Olá, mundo!" → ["Olá", ",", "mundo", "!"]
    """
    return re.findall(r"\w+|[^\w\s]", text)
