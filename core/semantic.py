class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, nodes):
        for node in nodes:
            self.visit(node)

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    # ===== Variable Declaration =====

    def visit_VarDeclaration(self, node):
        name = node.name

        if name in self.symbol_table:
            raise Exception(f"Variable '{name}' already declared")

        self.symbol_table[name] = node.var_type

        self.visit(node.value)

    # ===== Binary Operation =====

    def visit_BinaryOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    # ===== Identifier =====

    def visit_Identifier(self, node):
        if node.name not in self.symbol_table:
            raise Exception(f"Variable '{node.name}' not defined")

    # ===== Number =====

    def visit_Number(self, node):
        pass
