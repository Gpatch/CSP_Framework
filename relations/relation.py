from abc import ABC, abstractmethod


class Relation(ABC):
    def __init__(self, variables, assignment, elems=None):
        self._variables = variables
        self._assignment = assignment
        self._req_assignment_elem = elems
        self._holds = self.set_relation()

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, vs):
        self._variables = vs

    @property
    def assignment(self):
        return self._assignment

    @assignment.setter
    def assignment(self, li):
        self._assignment = li

    @property
    def req_assignment_elem(self):
        return self._req_assignment_elem

    @req_assignment_elem.setter
    def req_assignment_elem(self, val):
        self._req_assignment_elem = val

    @property
    def holds(self):
        return self.set_relation()

    @holds.setter
    def holds(self, val):
        self._holds = val

    @abstractmethod
    def set_relation(self):
        pass

