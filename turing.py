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
        pass

    def run(self) -> str:
        pass
