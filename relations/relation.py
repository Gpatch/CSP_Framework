from abc import ABC, abstractmethod


class Relation(ABC):
    def __init__(self, variables, assignment, elems=None):
        self._variables = variables
        self._assignment = assignment
        #self._name = self.name_gen()
        self._req_assignment_elem = elems
        self._holds = self.set_relation()

   # @property
 #   def name(self):
 #       return self._name

    @property
    def variables(self):
        return self._variables

    @property
    def assignment(self):
        return self._assignment

    @property
    def holds(self):
        return self.set_relation()

    @property
    def req_assignment_elem(self):
        return self._req_assignment_elem

    @holds.setter
    def holds(self, val):
        self._holds = val

    @abstractmethod
    def set_relation(self):
        pass

  #  @abstractmethod
  #  def name_gen(self):
  #      pass










