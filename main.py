from core.interpreter import IRInterpreter
from core.ir import IRBuilder
from core.lexer import Lexer
from core.optimizations.pipline import Optimizer
from core.parser import Parser
from core.semantic import SemanticAnalyzer


def main():
    code = """
    int b = 3;
    int a = 10 + b;
    int c = a * 2;
    """
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)

    parser = Parser(tokens)
    ast = parser.parse()

    print(ast)

    semantic = SemanticAnalyzer()
    semantic.analyze(ast)

    print("Semantic analysis passed")
    print("Symbol table:", semantic.symbol_table)

    ir_builder = IRBuilder()
    ir = ir_builder.build(ast)

    print("IR:")
    for instr in ir:
        print(instr)

    optimizer = Optimizer()
    ir = optimizer.optimize(ir)

    print("Optimized IR:")
    for instr in ir:
        print(instr)

    print("Generate code")
    interpreter = IRInterpreter()
    result = interpreter.execute(ir)

    print("Program result:")
    print(result)


if __name__ == "__main__":
    main()
