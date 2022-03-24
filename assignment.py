class Assignment:
    def __init__(self, assignment: list):  # list of AV's
        self._assignment = assignment

    @property
    def assignment(self):
        return self._assignment

    def remove_av(self, var):
        for a in self._assignment:
            if a._name == var:
                self._assignment.remove(a)

    def print_assignment(self):
        newline = '\n'
        return f'{newline.join(f"{x}" for x in self._assignment)}'

    def lookup_var(self, var):
        result = None
        for i in self._assignment:
            if i._name == var:
                result = i.value
                break
        return result

    def is_assigned(self, var):
        result = False
        for i in self._assignment:
            if i._name == var:
                result = True
                break
        return result
