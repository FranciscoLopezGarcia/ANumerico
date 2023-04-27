from sympy import *

def resultado():
    eq_str = input("Ingrese la ecuación: ")

    #Se fija si la ecuación es igual a algo o igual a 0
    if '=' in eq_str:
        lhs_str, rhs_str = eq_str.split('=')
        lhs = sympify(lhs_str)
        rhs = sympify(rhs_str)
        eq = Eq(lhs, rhs)
    else:
        expr = sympify(eq_str)
        eq = Eq(expr, 0)

    vars = sorted(eq.free_symbols, key=str)
    var_a_despejar = input(f"Ingrese la variable a despejar (de {vars}): ")

    sol = solve(eq, var_a_despejar)
    sol_simplificado = simplify(sol[0])

    print(f"{var_a_despejar} = {sol_simplificado}")
    
    return sol_simplificado