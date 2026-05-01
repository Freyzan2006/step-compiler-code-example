class ConstantPropagation:
    def optimize(self, instructions):
        constants = {}
        optimized = []

        for instr in instructions:
            if instr.op == "LOAD_CONST":
                constants[instr.result] = instr.arg1

            if instr.arg1 in constants:
                instr.arg1 = constants[instr.arg1]

            if instr.arg2 in constants:
                instr.arg2 = constants[instr.arg2]

            optimized.append(instr)

        return optimized
