import math
from assignvar import AssignedVar


class Assignment:
    def __init__(self, assignment):
        # assignment = [AssignedVar]
        self.assignment = assignment

    def __str__(self):
        return str([str(item) for item in self.assignment])

    def lookup_var(self, var):
        result = -math.inf
        for i in self.assignment:
            if i.get_var_name() == var:
                result = i.get_var_value()
                break
        return result

    def is_var_assigned(self, var):
        result = False
        for i in self.assignment:
            if i == var:
                result = True
                break
        return result

    def assign(self, var_name, var_val, domain):
        exists = False
        new_var = AssignedVar(var_name, var_val, domain)
        for i in self.assignment:
            if i.get_var_name() == new_var.get_var_name():
                i.set_value(var_val)
                exists = True
                break
        if not exists:
            self.assignment.append(new_var)
