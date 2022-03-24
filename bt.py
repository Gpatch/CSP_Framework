from assignment import Assignment
from assignvar import AV
import copy


class BT:
    def __init__(self, csp):
        self._csp = csp

    def bt_recursion(self, csp, nodes=0):
        if csp.is_complete():
            return True

        curr_var = csp.first_unassigned_var()
        curr_domain = csp.get_domain(curr_var)

        for v in curr_domain:
            if csp.is_consistent_value(curr_var, v):
                self._csp.assign(curr_var, v)
                if self.bt_recursion(csp, nodes + 1):
                    return True
                else:
                    csp.unassign(curr_var)
            else:
                nodes += 1



