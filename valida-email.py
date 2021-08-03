import constants


global esdebug
global entrada
global estado

esdebug = False
entrada = constants.ENTRADA_INVALIDA
estado = constants.ESTADO_INICIAL



def debug(mensaje):
    global esdebug
    if esdebug:
        print (mensaje)


def validState():
    global entrada
    global estado

    debug ("Ingreso validando estado.  Entrada: "+entrada+", Estado: "+str(estado) )

    if estado == 1:
        if entrada== constants.LETRA:
            estado=2
        else :
            estado = constants.ERROR_ANALIZADOR_LEXICO
    elif estado ==2:
        if entrada in [constants.LETRA, constants.DIGITO]:
            estado=2
        elif entrada == constants.ARROBA:
            estado=3
        else:
            estado = constants.ERROR_ANALIZADOR_LEXICO
    elif estado == 3:
        if entrada == constants.LETRA:
            estado=4
        else :
            estado = constants.ERROR_ANALIZADOR_LEXICO
    elif estado ==4:
        if entrada in [constants.LETRA, constants.DIGITO]:
            estado=4
        elif entrada == constants.SIGNO_PUNTO:
            estado=5
        else:
            estado = constants.ERROR_ANALIZADOR_LEXICO        
    elif estado == 5:
        if entrada == constants.LETRA:
            estado=6
        else: 
            estado == constants.ERROR_ANALIZADOR_LEXICO
    elif estado ==6:
        if entrada in [constants.LETRA, constants.DIGITO]:
            estado=6
        elif entrada == constants.FDC:
            estado=constants.ESTADO_DE_ACEPTACION
        else:
            estado = constants.ERROR_ANALIZADOR_LEXICO        
    elif estado == 7:
        if entrada == constants.FDC:
            estado=constants.ESTADO_DE_ACEPTACION
        else: 
            estado == constants.ERROR_ANALIZADOR_LEXICO            

    debug ("Egreso  validando estado.  Entrada: "+entrada+", Estado: "+str(estado))





def validEmail(datoIngresado):
    global entrada
    global estado    
    entrada = constants.ENTRADA_INVALIDA
    estado = constants.ESTADO_INICIAL
    debug ( "Se establece el estado inicial = 1")
    debug ("\n\nIngreso validar email.  Entrada: "+entrada+", Estado: "+str(estado))
    
    tamanio = len(datoIngresado)
    debug("Tamaño: "+str(tamanio))
    i=0

    for letter in datoIngresado:
        debug("\nLetra procesada: "+ letter )
        i=i+1
        debug("# Caracter: "+str(i))
        if tamanio==i:
            entrada=constants.FDC
        elif letter.isalpha() :
            entrada = constants.LETRA
        elif letter.isdigit():
            entrada = constants.DIGITO
        elif letter == "@":
            entrada = constants.ARROBA
        elif letter == ".":
            entrada = constants.SIGNO_PUNTO
        else:
            entrada = constants.ENTRADA_INVALIDA
            break

        validState()
        if estado == constants.ESTADO_DE_ACEPTACION:
            debug("Estado de aceptación !")
            print("El email ingresado "+datoIngresado+", es un email VALIDO !!")
            break

    if estado != constants.ESTADO_DE_ACEPTACION:
        debug("Error al analizar texto !")
        print("El email ingresado "+datoIngresado+", es un email INVALIDO !!")        

    debug ("\n\nEgreso  validar email.  Entrada: "+entrada+", Estado: "+str(estado))





palabras = ['alicia@gmail.com', 
            'cesar@gmail.com', 
            'edinson@gmail.com',
            'jose@gmail.com',
            '@gmail.com',
            'auto@',
            'au.com',
            'au@com',
            '25jose',
            ':=',
            ':=']



for palabra in palabras:
    debug (palabra )
    validEmail( palabra )

