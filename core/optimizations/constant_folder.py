from core.ir import IRInstruction


class ConstantFolder:
    def optimize(self, instructions):
        constants = {}
        optimized = []

        for instr in instructions:
            if instr.op == "LOAD_CONST":
                constants[instr.result] = instr.arg1
                optimized.append(instr)

            elif instr.op in ("ADD", "SUB", "MUL", "DIV"):
                left = constants.get(instr.arg1)
                right = constants.get(instr.arg2)

                if left is not None and right is not None:
                    if instr.op == "ADD":
                        value = left + right
                    elif instr.op == "SUB":
                        value = left - right
                    elif instr.op == "MUL":
                        value = left * right
                    elif instr.op == "DIV":
                        value = left / right

                    constants[instr.result] = value

                    optimized.append(
                        IRInstruction(op="LOAD_CONST", arg1=value, result=instr.result)
                    )

                else:
                    optimized.append(instr)

            else:
                optimized.append(instr)

        return optimized
