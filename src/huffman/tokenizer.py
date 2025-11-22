import re
from typing import List

def tokenize(text: str) -> List[str]:
    """
    Normalize and split text into words.
    Lowercase, replace newlines with spaces, extract words allowing Portuguese chars and apostrophes.
    """
    text = text.lower().replace("\n", " ")
    words = re.findall(r"[a-záâãàéêíóôõúç0-9']+", text, flags=re.IGNORECASE)
    return words
