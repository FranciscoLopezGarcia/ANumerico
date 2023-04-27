#Se fija los valores actuales de x,y y la función y devuelve el resultado de la función
def f(y, x, func):
    return eval(func)

class RK:
    def call_k(orden, x_0, y_0, x_n, h, func):
        x = x_0
        y = y_0
        iteration = 1
        result = []
        #Dependiendo del orden ingresado es el método que se va a usar
        if orden == 1:
            while x < x_n:
                k_1 = h * f(y, x, func)
                y = y + k_1
                x += h
                result.append((iteration, x, y))
                iteration += 1
        elif orden == 2:
            while x < x_n:
                k_1 = h * f(y, x, func)
                k_2 = h * f(y + 0.5*k_1, x + 0.5*h, func)
                y = y + k_2
                x += h
                result.append((iteration, x, y))
                iteration += 1
        elif orden == 3:
            while x < x_n:
                k_1 = h * f(y, x, func)
                k_2 = h * f(y + 0.5*k_1, x + 0.5*h, func)
                k_3 = h * f(y + k_2, x + h, func)
                y = y + 1/6*(k_1 + 4*k_2 + k_3)
                x += h
                result.append((iteration, x, y))
                iteration += 1
        elif orden == 4:
            while x < x_n:
                k_1 = h * f(y, x, func)
                k_2 = h * f(y + 0.5*k_1, x + 0.5*h, func)
                k_3 = h * f(y + 0.5*k_2, x + 0.5*h, func)
                k_4 = h * f(y + k_3, x + h, func)
                y = y + 1/6*(k_1 + 2*k_2 + 2*k_3 + k_4)
                x += h
                result.append((iteration, x, y))
                iteration += 1
        return result
