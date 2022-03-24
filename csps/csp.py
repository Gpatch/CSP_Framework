from assignvar import AV


class CSP:
    def __init__(self, name, domains, assignment, constraints):
        self.name = name
        self.domains = domains
        self.assignment = assignment
        self.constraints = constraints

    def __str__(self):
        return f'{self.name} \n__________________\n \n {self.print_domains()} \n \n {self.print_assignment()}' \
               f'\n \n {self.print_constraints()}'

    def print_domains(self):
        newline = '\n'
        string = f'Domains: {newline}____________ {newline}{newline.join(f"{domain}" for domain in self.domains)}'
        return string

    def print_assignment(self):
        newline = '\n'
        string = f'Assignment: {newline}____________ {newline}{self.assignment.print_assignment()}'
        return string

    def print_constraints(self):
        newline = '\n'
        string = f'Constraints: {newline}____________ {newline}{newline.join(f"{c}" for c in self.constraints)}'
        return string

    def check_constraints(self):
        all_satisfy = True
        for c in self.constraints:
            if not c.check_constr():
                all_satisfy = False
                break
        return all_satisfy

    def csp_vars(self):
        variables = []
        for d in self.domains:
            variables.append(d.var)
        return variables

    def csp_domains(self):
        return self.domains

    def csp_constraints(self):
        return self.constraints

    def set_domains(self, domains):
        self.domains = domains

    def get_domain(self, var):
        correct_domain = []
        for d in self.domains:
            if d.var == var:
                correct_domain = d.domain
                break
        return correct_domain

    def first_unassigned_var(self):
        unassigned = [x for x in self.csp_vars() if not self.assignment.is_assigned(x)]
        return unassigned[0]

    def constraints_of(self, var):
        constr = [c for c in self.constraints if c.is_constrained(var)]
        return constr

    def all_neighbours_of(self, var):
        nbs = [v for c in self.constraints for v in c.neighbours_of(var)]
        return nbs

    def common_constraints(self, x, y):
        constr = [c for c in self.constraints_of(x) if c.is_constrained(y)]
        return constr

    def is_complete(self):
        complete = all([self.assignment.is_assigned(v) for v in self.csp_vars()])
        return complete

    def is_consistent(self):
        consistent = all([c.check_constr() for c in self.csp_constraints()])
        return consistent

    def is_consistent_value(self, var, val):
        self.assign(var, val)
        consistent = self.is_consistent()
        self.assignment.remove_av(var)
        return consistent

    def assign(self, var, val):
        val_set = False
        for i in self.assignment.assignment:
            if i.name == var:
                i.value = val
                val_set = True
                break
        if not val_set:
            self.assignment.assignment.append(AV(var, val))
            self.update_assigment_rels()

    def unassign(self, var):
        self.assignment.remove_av(var)

    def update_assigment_rels(self):
        for c in self.constraints:
            c.relation.assignment = self.assignment
            c.relation.req_assignment_elem = len(self.assignment.assignment)
