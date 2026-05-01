from core.optimizations.constant_folder import ConstantFolder
from core.optimizations.constant_propagation import ConstantPropagation
from core.optimizations.dead_code_elimination import DeadCodeElimination


class Optimizer:
    def __init__(self):
        self.passes = [ConstantPropagation(), ConstantFolder(), DeadCodeElimination()]

    def optimize(self, instructions):

        for p in self.passes:
            instructions = p.optimize(instructions)

        return instructions
