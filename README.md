# CSP_Framework (In development)
A framework for formulating and solving Constraint Satisfaction Problems (CSPs).
Each problem must be formulated with the following components:
<ul>
  <li>Assigned Variables</li>  
  <li>Domains</li>  
  <li>Assignment</li>  
  <li>Relations</li>
  <li>Constraints</li>  
</ul>
<br>
The following algorithms are heristics are used to solve the CSP (More to be added):
<ul>
  <li>Backtracking</li>
  ...
</ul>
To see an example of CSP please take a look at <a href="https://github.com/Gpatch/CSP_Framework/blob/master/testing.py">testing.py</a>.
<br>
<h2>Documentation</h2>
<h3>AssignedVar</h3>
The <b>AssignedVar</b> class is used to represent a variable name with a particular value. Currently there are
no restrictions on the <b>value</b> attribute type. AV constructor is used.
<br>
<h4>Attributes</h4>
<ul>
  <li>name: String</li>  
  <li>value: Type</li>  
</ul>
<br>
<h3>Assignment</h3>
The <b>Assignment</b> class represents the current state of the CSP.
<br>
<h4>Attributes</h4>
<ul>
  <li>assignment: [AV]</li>   
</ul>
<h4>Methods</h4>
<ul>
  <li>remove_av(var: String)
  Removes the specified variable from the assignment.</li>   
  <li>lookup_var(var: String): Type Searches for the specified variable in the assignment and returns its value if found.</li>
  <li>is_assigned(var: String): Boolean  Searches for the specified variable in the assignment. 
    Returns True if found, False otherwise.</li> 
</ul>
<br>
<h3>Relation</h3>
The <b>Relation</b> abstract class represents the relation which some constraint satisfies.
<br>
<h4>Attributes</h4>
<ul>
  <li>variables: [String]</li>   
  <li>assignment: Assignment</li> 
  <li>holds: Boolean</li>   
  <li>req_assignment_elem: Int</li>
</ul>
<h4>Methods</h4>
<ul>
  <li>set_relation(abstract) A concrete class implements this method to set the relation value. It is up to the implementing concrete class 
    to decide if the relation is unary, binary or n-ary.
  Removes the specified variable from the assignment.</li>
  Example of a standard, already implemented relation is <a href="https://github.com/Gpatch/CSP_Framework/blob/master/relations/vars_diff.py">vars_diff.py</a>
.
</ul>
<br>
<h3>Constraint</h3>
The <b>Constraint</b> class represents the definition of a constraint with a certain relation ofthe CSP.
<br>
<h4>Attributes</h4>
<ul>
  <li>name: String</li>   
  <li>variables: [String]</li>  
  <li>relation: Relation</li>  
</ul>
<h4>Methods</h4>
<ul>
  <li>check_constr(): Boolean Checks if relation of the constraint holds.</li>
  <li>scope(): [String] Returns a list of variables in the constraint.</li>
  <li>is_constrained(var: String): Boolean Checks if the variable is constrained.</li>
  <li>neighbours_of(var: String): [String] Returns all neighbour variables of the specified variable from the current constraint.</li>
</ul>
<br>
<h3>Domain</h3>
The <b>Domain</b> class represents the domain of some variable on the CSP.
<br>
<h4>Attributes</h4>
<ul>
  <li>var: String</li>   
  <li>domain: [Type]</li>  
</ul>
<h4>Methods</h4>
<ul>
  <li>domain_add(val: Type): Add new value to the domain of the variable.</li>
  <li>domain_del(val: Type): Remove value from the domain of the variable.</li>
</ul>
<br>
<h3>CSP</h3>
The <b>CSP</b> class represents the whole CSP problem with relevant variables, domains, assignmnet and constraints with its relations.
<br>
<h4>Attributes</h4>
<ul>
  <li>name: String</li>   
  <li>domains: [Domain]</li>  
  <li>assignment: Assignment</li>
  <li>constraints: [Constraint]</li>  
</ul>
<h4>Methods</h4>
<ul>
  <li>check_constraints():Boolean Checks if all constraints in the CSP are satisfied.</li>
  <li>csp_vars(): [String] Returns all the variables of the CSP.</li>
  <li>get_domain(var: String): [Type] Gets the domain for some variable.</li>
  <li>first_unassigned_var(): String Gets the first variable for the variables list which has not been yet assigned.</li>
  <li>constraints_of(var: String): [Constraint] Gets all the constraints of some variable to which it is contrained.</li>
  <li>all_neighbours_of(var: String): [String] Gets every neightbour of some variable from all the constraints related to this variable.</li>
  <li>common_constraints(x: String, y: String): [Constraint] Gets a list of common constraints between 2 variables.</li>
  <li>is_complete(): Boolean Checks if the assigmnent is complete with all the variables.</li>
  <li>is_consistent(): Boolean Checks if the current assignment of the CSP is consistent by satisfying all the constraints.</li>
  <li>is_consistent_value(var: String, val: Type): Boolean Checks if the the assignemnt fo the CSP would be consistent given this new variable assignment.</li>
  <li>assign(var: String, val:String) Assigns a variable to a value and added to the assignment.</li>
  <li>unassign(var:String) Removes the variable with its value from the CSP assignment</li>
</ul>
<br>
<h3>BT</h3>
The <b>BT</b> class represents the <a href="https://github.com/Gpatch/CSP_Framework/blob/master/bt.py">Backtracking algorithm</a> which solves a given CSP.
<h4>Methods</h4>
<ul>
  <li>bt_recursion(csp: CSP): Boolean Solves the CSP problem by modifying the CSP directly. Returns True if the CSP has been solved, False otherwise</li>
</ul>
<br>
<h2>Next Updates</h2>
Add more algorithms and heuristics to solve problems more efficiently and compare performance against algorithms.
Possible things to implement:
<ul>
  <li>Forwardchecking</li>  
  <li>Least Constraining Variable (LCV) heuristic</li>
  <li>Minimum Remaining Values (MRV) heuristic</li>
  <li>AC-3</li>
  ...
</ul>
