from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    ID = 1
    NUM = 2
    STR = 3
    LPAREN = 4
    RPAREN = 5
@dataclass
class Token:
    """Represent a token produced by the lexer."""
    line: int
    col: int
    typ: TokenType
    value: str