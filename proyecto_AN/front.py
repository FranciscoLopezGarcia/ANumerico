from calculator import Calculator

def main():
    calc = Calculator()
    
    a = float(input('Ingrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    election = input('Ingrese la operacion a realizar: ')
    
    if election in ['+', '-']:
        result, error = calc.calc_basic(a, b, election)
    elif election in ['*', '/']:
        result, error = calc.calc_not_basic(a, b, election)
    else:
        result = 'Error: Operacion no valida'
        error = 0
        
    print(f'El resultado es: {result} con un error de {error}')
    
if __name__ == '__main__':
    main()