from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self, name, variables, relation):
        self._name = name
        self._variables = variables
        self._relation = relation

    def __str__(self):
        return self._name

    def check_constr(self):
        return self._relation.holds

    def scope(self):
        return self._variables

    def is_constrained(self, var):
        result = False
        for i in self._variables:
            if i == var:
                result = True
                break
        return result

    def neighbours_of(self, var):
        nbs = []
        for i in self._variables:
            if i != var:
                nbs.append(i)
        return nbs


