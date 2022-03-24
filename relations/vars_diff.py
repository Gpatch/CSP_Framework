from relations.relation import Relation


class VarsDiff(Relation):
    def __init__(self, variables, assignment):
        super().__init__(variables, assignment, len(assignment._assignment))

    def set_relation(self):
        if self.req_assignment_elem < 2:
            return True

        x = self.variables[0]
        y = self.variables[1]

        x_v = self.assignment.lookup_var(x)
        y_v = self.assignment.lookup_var(y)

        if x_v is None and y_v is None:
            result = True
        else:
            if x_v != y_v:
                result = True
            else:
                result = False
        return result
