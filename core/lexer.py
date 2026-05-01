import re
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    position: int


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.tokens = []

        self.token_specification = [
            ("NUMBER", r"\d+"),
            ("IDENTIFIER", r"[a-zA-Z_]\w*"),
            ("PLUS", r"\+"),
            ("MINUS", r"-"),
            ("MULTIPLY", r"\*"),
            ("DIVIDE", r"/"),
            ("ASSIGN", r"="),
            ("LPAREN", r"\("),
            ("RPAREN", r"\)"),
            ("SEMICOLON", r";"),
            ("SKIP", r"[ \t\n]+"),
            ("MISMATCH", r"."),
        ]

        self.regex = re.compile(
            "|".join(
                f"(?P<{name}>{pattern})" for name, pattern in self.token_specification
            )
        )

    def tokenize(self) -> list[Token]:
        for match in self.regex.finditer(self.source):
            kind = match.lastgroup
            value = match.group()
            position = match.start()

            if kind == "SKIP":
                continue
            elif kind == "MISMATCH":
                raise SyntaxError(f"Unexpected character {value} at {position}")
            else:
                # Проверка на ключевое слово
                if kind == "IDENTIFIER" and value == "int":
                    kind = "KEYWORD"

                self.tokens.append(Token(kind, value, position))

        return self.tokens
