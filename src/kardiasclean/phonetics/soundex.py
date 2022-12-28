"""
Phonetic Algorithms

Paper:
    https://iopscience.iop.org/article/10.1088/1757-899X/508/1/012106/pdf
"""
import re

D_SOUNDEX_EN = {
    0: {"A", "E", "H", "I", "O", "U", "W", "Y"},
    1: {"B", "F", "P", "V"},
    2: {"C", "G", "J", "K", "Q", "S", "X", "Z"},
    3: {"D", "T"},
    4: {"L"},
    5: {"M", "N"},
    6: {"R"},
}

D_ES_SUB = {
    r'(^H)': '',
    r'(^V)': 'B',
    r'(^[ZX])': 'S',
    r'(^G)([EI])': lambda x: f'J{x.group(2)}',
    r'(^C)([^HEI])': lambda x: f'K{x.group(2)}',
    r'(Ñ)': 'N',
    r'(CH)': 'V',
    r'(QU)': 'K',
    r'(LL)': 'J',
    r'(C[EI])': 'S',
    r'(Y[AEIOU])': 'J',
    r'(G[EI])': 'J',
    r'(NY)': 'N',
}

def find_soundex_digit(char: str, d_soundex: dict = D_SOUNDEX_EN) -> int:
    """Get soundex digit from character.
    Iterates over soundex dictionary of sets."""
    for key in d_soundex:
        if char in d_soundex[key]:
            return key


def soundex_en(word: str) -> str:
    """
    American Soundex:
        - Convert all letters into upper case.
        - Retain the first letter in the word w.
        - From word w, all pairs of same digits and zeroes are removed.
        - The first four characters of word w are considered to be Soundex code.
    
    Implementation:
        - Find digit from sets, exclude adjacent repeats.
        - Exclude zeroes and join as string.
        - Put string back together, zero-pad and limit.
    """
    word = word.upper()
    result = [find_soundex_digit(word[0])]
    for char in word[1:]:
        digit = find_soundex_digit(char)
        if digit is not None and digit != result[-1]:
            result.append(digit)
    result = "".join(str(r) for r in result[1:] if r != 0)
    return f"{word[0]}{result.ljust(3, '0')[0:3]}"


def soundex_es(word: str) -> str:
    """
    Spanish Soundex:
    https://wiki.postgresql.org/wiki/SoundexESP    
    """
    word = word.upper()
    for pattern, replace in D_ES_SUB.items():
        word = re.sub(pattern, replace, word)
    return soundex_en(word)

# conda create --name hac python=3.9