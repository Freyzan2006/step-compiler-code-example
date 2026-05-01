from core.ast import BinaryOp, Identifier, Number, VarDeclaration
from core.lexer import Token


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self) -> Token | None:
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def eat(self, token_type):
        token = self.current()
        if token and token.type == token_type:
            self.position += 1
            return token
        raise SyntaxError(f"Expected {token_type}, got {token}")

    def parse(self) -> list[VarDeclaration]:
        declarations = []

        while self.current() is not None:
            declarations.append(self.parse_declaration())

        return declarations

    def parse_declaration(self) -> VarDeclaration:
        self.eat("KEYWORD")
        identifier = self.eat("IDENTIFIER")
        self.eat("ASSIGN")
        expr = self.parse_expression()
        self.eat("SEMICOLON")

        return VarDeclaration(var_type="int", name=identifier.value, value=expr)

    def parse_expression(self):
        return self.parse_term()

    def parse_term(self) -> BinaryOp:
        node = self.parse_factor()

        while self.current() and self.current().type in ("PLUS", "MINUS"):
            operator = self.eat(self.current().type)
            right = self.parse_factor()
            node = BinaryOp(node, operator.value, right)

        return node

    def parse_factor(self):
        node = self.parse_primary()

        while self.current() and self.current().type in ("MULTIPLY", "DIVIDE"):
            operator = self.eat(self.current().type)
            right = self.parse_primary()
            node = BinaryOp(node, operator.value, right)

        return node

    def parse_primary(self):
        token = self.current()

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return Number(int(token.value))

        elif token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            return Identifier(token.value)

        elif token.type == "LPAREN":
            self.eat("LPAREN")
            expr = self.parse_expression()
            self.eat("RPAREN")
            return expr

        else:
            raise SyntaxError(f"Unexpected token {token}")
