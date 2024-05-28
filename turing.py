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
            if len(elements) != 5:
                raise ValueError("Incorrect instruction format detected")
            curr = (elements[0], elements[1])
            next = (elements[2], elements[3], elements[4])
            instr_dict[curr] = next
        return instr_dict

    def _display_curr_state(self, idx: int, state: str) -> str:
        tape_str = self.tape.strip()
        if idx >= 0 and idx < len(tape_str):
            print(f"{tape_str} {state}\n{' '*idx}^")
        elif idx < 0:
            print(f"{'_'*(-idx)}{tape_str} {state}\n^")
        else:
            print(f"{tape_str}{'_'*(idx+1-len(tape_str))} {state}\n{' '*idx}^")

    def run(self) -> str:
        state = "init"
        idx = 0
        while "halt" != state[:4]:
            self._display_curr_state(idx, state)
            curr = (state, "_")
            if idx >= 0 and idx < len(self.tape) and len(self.tape) != 0:
                curr = (state, self.tape[idx])
            if curr[1] == " ":
                next = self.instructions.get((state, "_"))
            else:
                next = self.instructions.get(curr)
            if not next:
                break
            new_symbol, direction, new_state = next

            if idx == (len(self.tape) - 2) and self.tape[-1] == " ":
                # remove redundant spaces from tape when traversing back
                self.tape = self.tape[: len(self.tape) - 1]
            if new_symbol == "_":
                if curr[1] == " ":
                    self.tape = self.tape
                elif idx < 0:
                    self.tape = " " + self.tape
                elif idx >= len(self.tape):
                    self.tape += " "
                else:
                    self.insert_sign(idx, "")
                    if direction == "R":
                        state = new_state
                        continue
            elif new_symbol != "_":
                if idx < 0:
                    self.tape = new_symbol + self.tape
                    idx += 1
                else:
                    self.insert_sign(idx, new_symbol)
            elif idx >= 0:
                self.tape = self.tape[:idx] + "" + self.tape[idx + 1 :]
            if direction == "L":
                idx -= 1
            elif direction == "R":
                idx += 1
            state = new_state
        self._display_curr_state(idx, state)
        return self.tape.strip()

    def insert_sign(self, idx, symbol):
        t_list = [*self.tape]
        if idx < len(t_list):
            t_list[idx] = symbol
        else:
            t_list.append(symbol)
        self.tape = "".join(t_list)
