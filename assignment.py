from assignvar import AV

class Assignment:
    def __init__(self, assignment: list):  # list of AV's
        self._assignment = assignment

    def print_assignment(self):
        newline = '\n'
        return f'{newline.join(f"{x}" for x in self._assignment)}'

    def lookup_var(self, var):
        result = None
        for i in self._assignment:
            if i.name == var:
                result = i.value
                break
        return result

    def is_assigned(self, var):
        result = False
        for i in self._assignment:
            if i.name == var:
                result = True
                break
        return result

    def assign(self, var, val):
        val_set = False
        for i in self._assignment:
            if i.name == var:
                i.value = val
                val_set = True
                break
        if not val_set:
            self._assignment.append(AV(var, val))
