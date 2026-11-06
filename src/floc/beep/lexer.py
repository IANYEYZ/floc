from .token import Token, TokenType

class lexer:
    def __init__(self, src: str) -> None:
        self.src = src
        self.tokenStack: list[Token] = []
        self.pos = 0
        self.line = 0
        self.col = 0
    def __getNextToken(self) -> Token:
        if self.src[self.pos] == "(":
            return Token(self.line, self.col, TokenType.LPAREN, "(")
        if self.src[self.pos] == ")":
            return Token(self.line, self.col, TokenType.RPAREN, ")")
    def advance(self) -> Token:
        """Get the next token in the source code."""
        if len(self.tokenStack) != 0:
            return self.tokenStack.pop()
        return self.__getNextToken()