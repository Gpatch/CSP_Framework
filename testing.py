import domain
from csps import csp
from relations import VarsDiff
from constraints import constraint
from assignment import Assignment
from bt import BT


# MAP OF AUSTRALIA COLOURING PROBLEM DEMO
def main():
    aus_map_var_names = ["WA", "NSW", "NT", "Q", "V", "SA"]  # Variables for the CSP as regions
    aus_domains = [domain.Domain(i, [1, 2, 3]) for i in aus_map_var_names]  # List of _domains for each region where
    # numbers represent different colours

    # We set the _name, _domains and the initial empty _assignment for the csp. We also specify list of _constraints
    # between variables with a binary relation (for this specific problem) VarsDiff which tells that 2 variables must
    # have different values assigned
    ausCSP = csp.CSP("AUSTRALIA MAP", aus_domains, Assignment([]),
                     [constraint.Constraint('WA /= NT', ["WA", 'NT'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('NT /= Q', ["NT", 'Q'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('SA /= WA', ["SA", 'WA'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('SA /= Q', ["SA", 'Q'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('SA /= NT', ["SA", 'NT'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('Q /= NSW', ["Q", 'NSW'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('SA /= NSW', ["SA", 'NSW'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('SA /= V', ["SA", 'V'], VarsDiff(aus_map_var_names, Assignment([]))),
                      constraint.Constraint('V /= NSW', ["V", 'NSW'], VarsDiff(aus_map_var_names, Assignment([])))
                      ])
    bt_solver = BT(ausCSP)
    print(bt_solver.bt_recursion(ausCSP))
    print(ausCSP)
    print(ausCSP.domains)


main()
