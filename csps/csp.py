from assignvar import AV


class CSP:
    def __init__(self, name, domains, assignment, constraints):
        self._name = name
        self._domains = domains
        self._assignment = assignment
        self._constraints = constraints

    def __str__(self):
        return f'{self._name} \n__________________\n \n {self.print_domains()} \n \n {self.print_assignment()}' \
               f'\n \n {self.print_constraints()}'

    def print_domains(self):
        newline = '\n'
        string = f'Domains: {newline}____________ {newline}{newline.join(f"{domain}" for domain in self._domains)}'
        return string

    def print_assignment(self):
        newline = '\n'
        string = f'Assignment: {newline}____________ {newline}{self._assignment.print_assignment()}'
        return string

    def print_constraints(self):
        newline = '\n'
        string = f'Constraints: {newline}____________ {newline}{newline.join(f"{c}" for c in self._constraints)}'
        return string

    def check_constraints(self):
        all_satisfy = True
        for c in self._constraints:
            if not c.check_constr():
                all_satisfy = False
                break
        return all_satisfy

    def csp_vars(self):
        variables = []
        for d in self._domains:
            variables.append(d.var)
        return variables

    @property
    def domains(self):
        return self._domains

    @property
    def constraints(self):
        return self._constraints

    @domains.setter
    def domains(self, dms):
        self._domains = dms

    def get_domain(self, var):
        correct_domain = []
        for d in self._domains:
            if d.var == var:
                correct_domain = d.domain
                break
        return correct_domain

    def first_unassigned_var(self):
        unassigned = [x for x in self.csp_vars() if not self._assignment.is_assigned(x)]
        return unassigned[0]

    def constraints_of(self, var):
        constr = [c for c in self._constraints if c.is_constrained(var)]
        return constr

    def all_neighbours_of(self, var):
        nbs = [v for c in self._constraints for v in c.neighbours_of(var)]
        return nbs

    def common_constraints(self, x, y):
        constr = [c for c in self.constraints_of(x) if c.is_constrained(y)]
        return constr

    def is_complete(self):
        complete = all([self._assignment.is_assigned(v) for v in self.csp_vars()])
        return complete

    def is_consistent(self):
        consistent = all([c.check_constr() for c in self.constraints])
        return consistent

    def is_consistent_value(self, var, val):
        self.assign(var, val)
        consistent = self.is_consistent()
        self._assignment.remove_av(var)
        return consistent

    def assign(self, var, val):
        val_set = False
        for i in self._assignment._assignment:
            if i._name == var:
                i.value = val
                val_set = True
                break
        if not val_set:
            self._assignment._assignment.append(AV(var, val))
            self._update_assigment_rels()

    def unassign(self, var):
        self._assignment.remove_av(var)

    def _update_assigment_rels(self):
        for c in self._constraints:
            c.relation._assignment = self._assignment
            c.relation.req_assignment_elem = len(self._assignment._assignment)
