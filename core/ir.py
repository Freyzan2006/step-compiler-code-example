from dataclasses import dataclass

from core.ast import VarDeclaration


@dataclass
class IRInstruction:
    op: str
    arg1: str | None = None
    arg2: str | None = None
    result: str | None = None


class IRBuilder:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def build(self, nodes: list[VarDeclaration]):
        for node in nodes:
            self.visit(node)

        return self.instructions

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    # ===== variable declaration =====

    def visit_VarDeclaration(self, node):
        value = self.visit(node.value)

        self.instructions.append(
            IRInstruction(op="STORE", arg1=value, result=node.name)
        )

    # ===== binary operation =====

    def visit_BinaryOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        temp = self.new_temp()

        op_map = {
            "+": "ADD",
            "-": "SUB",
            "*": "MUL",
            "/": "DIV",
        }

        self.instructions.append(
            IRInstruction(op=op_map[node.operator], arg1=left, arg2=right, result=temp)
        )

        return temp

    # ===== number =====

    def visit_Number(self, node):
        temp = self.new_temp()

        self.instructions.append(
            IRInstruction(op="LOAD_CONST", arg1=node.value, result=temp)
        )

        return temp

    # ===== identifier =====

    def visit_Identifier(self, node):
        return node.name
