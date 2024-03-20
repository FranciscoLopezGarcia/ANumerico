import numpy as np

def pedir_matriz():
    n = int(input("Ingrese el número de ecuaciones: "))
    matriz = []
    print("Ingrese los coeficientes de cada ecuación (ax + by + cz = d):")
    for i in range(n):
        ecuacion = input(f"Ecuación {i+1} (separe los coeficientes y el término independiente con espacios): ")
        coeficientes = list(map(float, ecuacion.split()))
        matriz.append(coeficientes)
    return matriz

def despejar_incognitas(matriz):
    soluciones = []
    for i, fila in enumerate(matriz):
        coeficientes = fila[:-1]
        resultado = fila[-1]
        ecuacion = []
        for j, coef in enumerate(coeficientes):
            if j != i:
                variable = f"x{j+1}"
                if coef != 0:
                    if coef > 0:
                        signo = "+"
                    else:
                        signo = "-"
                    ecuacion.append(f"{signo} {abs(coef)}*{variable}")
        ecuacion.append(f"= ({resultado} - {' - '.join([f'{coef}*x{k+1}' for k, coef in enumerate(coeficientes) if k != i])}) / {fila[i]}")
        soluciones.append(ecuacion)
    return soluciones

def main():
    matriz = pedir_matriz()
    matriz = np.array(matriz)
    num_incognitas = matriz.shape[1] - 1
    print("\nMatriz ingresada:")
    for fila in matriz:
        ecuacion = " + ".join([f"{coef}*x{i+1}" for i, coef in enumerate(fila[:-1])])
        ecuacion += f" = {fila[-1]}"
        print(ecuacion)
    
    soluciones = despejar_incognitas(matriz)
    print("\nSoluciones:")
    for i, solucion in enumerate(soluciones):
        print(f"Fila {i+1}:")
        for eq in solucion:
            print(eq)

if __name__ == "__main__":
    main()

