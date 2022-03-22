import assignment
import assignvar
import domain
from csps import csp
from relations import VarsDiff
from constraints import constraint
from assignment import Assignment
from assignvar import AV


def main():
    aus_map_var_names = ["WA", "NSW", "NT", "Q", "V", "SA"]
    aus_domains = [domain.Domain(i, [1, 2, 3]) for i in aus_map_var_names]
    # aus_assignment = Assignment([AV("WA", 2), AV("NSW", 1)])
    vars_diff_rel = VarsDiff(aus_map_var_names, [])
    ausCSP = csp.CSP("AUSTRALIA MAP", aus_domains, assignment.Assignment([]),
                     [constraint.Constraint('WA /= NT', ["WA", 'NT'], vars_diff_rel),
                      constraint.Constraint('NT /= Q', ["NT", 'Q'], vars_diff_rel),
                      constraint.Constraint('SA /= WA', ["SA", 'WA'], vars_diff_rel),
                      constraint.Constraint('SA /= Q', ["SA", 'Q'], vars_diff_rel),
                      constraint.Constraint('SA /= NT', ["SA", 'NT'], vars_diff_rel),
                      constraint.Constraint('Q /= NSW', ["Q", 'NSW'], vars_diff_rel),
                      constraint.Constraint('SA /= NSW', ["SA", 'NSW'], vars_diff_rel),
                      constraint.Constraint('SA /= V', ["SA", 'V'], vars_diff_rel),
                      constraint.Constraint('V /= NSW', ["V", 'NSW'], vars_diff_rel)
                      ])


    ausCSP.assignment.assign('WA', 1)
    ausCSP.assignment.assign('WA', 2)
    print(ausCSP)



main()
