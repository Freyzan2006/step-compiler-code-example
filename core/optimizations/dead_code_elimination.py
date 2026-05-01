class DeadCodeElimination:
    def optimize(self, instructions):

        used = set()

        for instr in instructions:
            if instr.arg1:
                used.add(instr.arg1)
            if instr.arg2:
                used.add(instr.arg2)

        optimized = []

        for instr in instructions:
            if instr.result and instr.result.startswith("t"):
                if instr.result not in used:
                    continue

            optimized.append(instr)

        return optimized
