import sympy as sp    #You import SymPy and assign it the alias (sp) to write shorter commands.

x, y, r = sp.symbols ('x y r', real=True)
#You create three symbolic variables: x, y, r.
#real=True tells SymPy to treat them as real numbers (useful for assumptions/simplifications).
#Important: r is a parameter, so it stays symbolic (no numeric substitution).

eq1 = sp.Eq(2*x**2 + 3*y**2, r)  #sp.Eq(LHS, RHS) builds a symbolic equation.
#Here you define the first equation
eq2 = sp.Eq(y,2*x +1)
#You define the second system equation

sol= sp.solve ([eq1, eq2], [x, y], dict = True)
#sp.solve(...) solves the system symbolically
#First argument: [eq1, eq2] → list of equations.
#Second argument: [x, y] → unknowns you want to solve for.
#dict=True → output as a list of dictionaries:
#[{x: ..., y: ...}, {x: ..., y: ...}]

#SymPy essentially substitutes eq 2 into eq1 =r, gets a quadratic in x, solves for x, then computes y.

print(sol)

