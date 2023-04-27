from back import RK
from equation import resultado

#Nota: el programa funcion(probar con EDO de mas orden)
#Nota: al ejecutar 'front.py' se ejecuta sin grafica
#Nota: al ejecutar 'grafico.py' se ejecuta todo incluida la grafica
#Nota: cambiar eso apra que sea al ejecutar 'front.py' y no 'grafico.py'
def main():
    y_0 = float(input('valor inicial de y: '))
    x_0 = float(input('valor inicial de x: '))
    x_n = float(input('valor final de x: '))
    h = float(input('valor de h: '))
    sol = resultado()
    func = str(sol)
    orden = int(input('orden de la EDO: '))

    result = RK.call_k(orden, x_0, y_0, x_n, h, func)

    for iteration, x, y in result:
        print(f"n° iteracion {iteration}: x={x}, y={y}" )
    
    return result

if __name__ == "__main__":
    main()
