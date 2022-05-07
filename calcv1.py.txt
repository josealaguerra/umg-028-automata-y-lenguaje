# Tipos de tokens
tokenENTERO, tokenSuma, tokenResta, tokenMultiplica, tokenDivide, tokenFinDeCadena = 'ENTERO', 'SUMA', 'RESTA', 'MULTIPLICA', 'DIVIDE', 'FINDECADENA'

# Signos validos
cSignoSuma, cSignoResta, cSignoMultiplica, cSignoDivide  = '+', '-', '*', '/'




class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value


    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # Cadena de caracteres ingresada por el usuario por ejemplo "2+3"
        self.text = text
        # Posicion actual
        self.pos = 0
        # Token actual
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error al interpretar cadena')
    
    
    def advance(self):
        """Avanza una posición en la cadena de caracteres"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]
            
        
    def skip_whitespace(self):
        """Se salta los espacios en blanco de la cadena de caracteres"""        
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    
    def integer(self):
        """Obtiene un token de un numero entero."""
        result =''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)



    def get_next_token(self):
        """Analizador lexico (tokenizador)

        Separar la cadena de caracteres en tokens, un token a la vez.
        """
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(tokenENTERO, self.integer())
            
            if self.current_char == cSignoSuma:
                self.advance()
                return Token(tokenSuma, cSignoSuma)

            if self.current_char == cSignoResta:
                self.advance()
                return Token(tokenResta, cSignoResta)

            if self.current_char == cSignoMultiplica:
                self.advance()
                return Token(tokenMultiplica, cSignoMultiplica)

            if self.current_char == cSignoDivide:
                self.advance()
                return Token(tokenDivide, cSignoDivide)

            self.error()
            
        return Token(tokenFinDeCadena, None)
    

    def eat(self, token_type):
        # compara el token leido con el que se paso por parametro
        # si difieren da una excepcion
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()



    def expr(self):
        """expr -> NUMERO OPERADOR NUMERO"""
        # Obtiene el primer token
        self.current_token = self.get_next_token()

        # Esperamos que el token actual sea un numero entero
        left = self.current_token
        self.eat(tokenENTERO)

        # Esperamos un signo valido para este token
        op = self.current_token
        if op.type == tokenSuma:
            self.eat(tokenSuma)
        else:
            if op.type == tokenResta:
                self.eat(tokenResta)
            else:
                if op.type == tokenMultiplica:
                    self.eat(tokenMultiplica)
                else:
                    if op.type == tokenDivide:
                        self.eat(tokenDivide)
                    else:
                        self.error()

        # El tercer token debe ser otro numero entero
        right = self.current_token
        self.eat(tokenENTERO)
        # Se debio encontrar el fin de cadena
        
        # Se interpreta la cadena de caracteres ingresada
        if op.type == tokenSuma:
            result = left.value + right.value
        else:
            if op.type == tokenResta:
                result = left.value - right.value
            else:
                if op.type == tokenMultiplica:
                    result = left.value * right.value                
                else:
                    if op.type == tokenDivide:
                        result = left.value / right.value

        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            #text = raw_input('calc> ')
            text = input('calcula> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()