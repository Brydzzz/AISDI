class Turing:
    def __init__(self, tape: str, instr_list: list[str]):
        self.tape = tape
        self.instructions = self._parse_ins(instr_list)

    def _parse_ins(
        self, instructions
    ) -> dict[tuple[str, str], tuple[str, str, str]]:
        instr_dict = {}
        for instr in instructions:
            elements = instr.strip().split()
            curr = (elements[0], elements[1])
            next = (elements[2], elements[3], elements[4])
            instr_dict[curr] = next
        return instr_dict

    def _display_curr_state(self, idx: int, state: str) -> str:
        if idx >= 0 and idx < len(self.tape):
            print(f"{self.tape} {state}\n{' '*idx}^")
        elif idx < 0:
            print(f"{'_'*(-idx)}{self.tape} {state}\n^")
        else:
            print(
                f"{self.tape}{'_'*(idx+1-len(self.tape))} {state}\n{' '*idx}^"
            )

    def run(self) -> str:
        state = "init"
        idx = 0
        while "halt" not in state:
            self._display_curr_state(idx, state)
            curr = (state, "_")
            if idx >= 0 and idx < len(self.tape):
                curr = (state, self.tape[idx])
            if curr[1] == " ":
                next = self.instructions.get((state, "_"))
            else:
                next = self.instructions.get(curr)
            if not next:
                next = self.instructions.get((state, "*"))
                if not next:
                    break
            new_symbol, direction, new_state = next
            if new_symbol != "_" and new_symbol != "*":
                self.tape = self.tape[:idx] + new_symbol + self.tape[idx + 1 :]
            elif new_symbol != "*" and idx >= 0:
                self.tape = self.tape[:idx] + "" + self.tape[idx + 1 :]
            if direction == "L":
                idx -= 1
            elif direction == "R":
                idx += 1
            state = new_state
        self._display_curr_state(idx, state)
