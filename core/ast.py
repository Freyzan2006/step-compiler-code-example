from dataclasses import dataclass


class ASTNode:
    pass


@dataclass
class Number(ASTNode):
    value: int


@dataclass
class Identifier(ASTNode):
    name: str


@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class VarDeclaration(ASTNode):
    var_type: str
    name: str
    value: ASTNode
