class Calculator:
    def __init__(self):
        self.result = 0
        self.error= 0
        
    def cota_error(self, valor):
        if valor == 0:
            return 0
        if isinstance(valor, int) or valor.is_integer():
            cota_error = 0.5
        else:
            part = str(valor).split('.')
            decimales = len(part[1]) if len(part) == 2 else 0
            cota_error = 0.5 * 10 ** (-decimales)
        return cota_error
    
    def calc_basic(self, a, b, election):
        error_a = self.cota_error(a)
        error_b = self.cota_error(b)
        
        if election == '+':
            self.result = a + b
        elif election == '-':
            self.result = a - b
        self.error = error_a + error_b
        return self.result, self.error

    def calc_not_basic(self, a, b, election):
        error_a = self.cota_error(a)
        error_b = self.cota_error(b)
        if election == '*':
            self.result = a * b
            self.error = ((error_a / abs(a)) + (error_b / abs(b))) * abs(self.result)
        elif election == '/':
            if b == 0:
                self.result = 'Error: Division por cero'
                self.error = 0
            self.result = a / b
            self.error = abs(self.result) * ((error_a / abs(a)) + (error_b / abs(b)))
        
        return self.result, self.error
        
        