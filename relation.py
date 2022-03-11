class Relation:
    def __init__(self, variables, assignment, truth):
        self.vars = variables
        self.assignment = assignment
        self.holds = truth

    def holds(self):
        return self.holds

    ######################################
    #########_STANDARD_RELATIONS_#########
    ######################################

    def vars_diff(self):
        self.holds = self.assignment.lookup_var(self.vars[0]) != self.assignment.lookup_var(self.vars[1])
