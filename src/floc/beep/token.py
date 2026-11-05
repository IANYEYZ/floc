from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    ID = 1
    NUM = 2
    STR = 3
@dataclass
class Token:
    line: int
    col: int
    typ: TokenType
    value: str