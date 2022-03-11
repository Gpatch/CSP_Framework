class Constraint:
    def __init__(self, name, variables, relation):
        self.name = name
        self.vars = variables
        self.relation = relation

    def __str__(self):
        return self.name

    def check_constraint(self):
        return self.relation.holds

    def get_scope(self):
        return self.vars

    def is_constrained(self, var):
        found = False
        for i in self.vars:
            if i == var:
                found = True
                break
        return found

    def get_neighbours_of(self, var):
        if self.is_constrained(var):
            neighbours = list(self.vars)
            neighbours.remove(var)
            return neighbours
        else:
            return []
