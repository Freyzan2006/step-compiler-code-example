from typing import Dict


class IRInterpreter:
    def __init__(self):
        self.variables: Dict = {}
        self.temps: Dict = {}

    def get_value(self, name):

        if isinstance(name, (int, float)):
            return name

        if name in self.temps:
            return self.temps[name]

        if name in self.variables:
            return self.variables[name]

        raise Exception(f"Unknown value {name}")

    def execute(self, instructions):

        for instr in instructions:
            op = instr.op

            if op == "LOAD_CONST":
                self.temps[instr.result] = instr.arg1

            elif op == "ADD":
                self.temps[instr.result] = self.get_value(instr.arg1) + self.get_value(
                    instr.arg2
                )

            elif op == "SUB":
                self.temps[instr.result] = self.get_value(instr.arg1) - self.get_value(
                    instr.arg2
                )

            elif op == "MUL":
                self.temps[instr.result] = self.get_value(instr.arg1) * self.get_value(
                    instr.arg2
                )

            elif op == "DIV":
                self.temps[instr.result] = self.get_value(instr.arg1) / self.get_value(
                    instr.arg2
                )

            elif op == "STORE":
                self.variables[instr.result] = self.get_value(instr.arg1)

            else:
                raise Exception(f"Unknown op {op}")

        return self.variables
