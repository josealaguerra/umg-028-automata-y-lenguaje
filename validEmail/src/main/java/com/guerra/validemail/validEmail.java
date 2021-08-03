/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.guerra.validemail;

import sun.security.util.Length;

/**
 *
 * @author jose.guerra
 */
public class validEmail {

    private  String LETRA = "letra";
    private  String DIGITO = "digito";
    private  String ARROBA = "arroba";
    private  String SIGNO_PUNTO= "punto";
    private  String FDC = "FDC";
    private  String ENTRADA_INVALIDA = "invalida";    

    private  int ERROR_ANALIZADOR_LEXICO = -1;
    private  int ESTADO_DE_ACEPTACION=999;
    private  int ESTADO_INICIAL=1;

            
    private  boolean esDebug=false;
    
    private  String entrada;
    private  int estado;
            
    
    public validEmail(){
        
    }
    

    /***
     * 
     * @param mensaje 
     */
    private  void debug(String mensaje){
        if(esDebug)
            System.out.println(mensaje);
    }

    /***
     * 
     * @param entrada
     * @param estado 
     */
    private  void validState(){

        debug("\n\nIngreso validando estado.  Entrada){ "+entrada+", Estado){ "+estado);

        if (estado == 1){
            if (entrada.equals(LETRA))
                estado=2;
            else 
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado ==2){
            if (entrada.equals(LETRA) || entrada.equals(DIGITO))
                estado=2;
            else if( entrada.equals(ARROBA))
                estado=3;
            else
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado == 3){
            if (entrada.equals(LETRA))
                estado=4;
            else 
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado ==4){
            if (entrada.equals(LETRA) || entrada.equals(DIGITO))
                estado=4;
            else if( entrada.equals(SIGNO_PUNTO))
                estado=5;
            else
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado == 5){
            if (entrada.equals(LETRA))
                estado=6;
            else if( entrada.equals(FDC))
                estado=ESTADO_DE_ACEPTACION;
            else
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado ==6){
            if (entrada.equals(LETRA) || entrada.equals(DIGITO))
                estado=6;
            else if( entrada.equals(FDC))
                estado=ESTADO_DE_ACEPTACION;
            else
                estado = ERROR_ANALIZADOR_LEXICO;
        }else if( estado == 7){
            if (entrada.equals(FDC))
                estado=ESTADO_DE_ACEPTACION;
            else
                estado = ERROR_ANALIZADOR_LEXICO;
        }

        debug ("\n\nEgreso  validando estado.  Entrada){ "+entrada+", Estado){ "+estado);
    }


    public  boolean isAlpha(char char1) {
        return (char1 >= 'a' && char1 <= 'z') || (char1 >= 'A' && char1 <= 'Z');
    }

            /**
             * 
             */
    private void isValidThisEmail(String datoIngresado){
        estado = ESTADO_INICIAL;
        debug ( "Se establece el estado inicial = 1");
        debug ("\n\nIngreso validar email.  Entrada){ "+entrada+", Estado){ "+estado)    ;

        int tamanio = datoIngresado.length();
        int caracterProcesado=0;
        char letra;
        for (int indexString=0; indexString<tamanio; indexString++){
            
            letra = datoIngresado.charAt(indexString);
            debug("\n\nLetra procesada: "+ letra );
            caracterProcesado=caracterProcesado+1;
            if (tamanio==caracterProcesado)
                entrada=FDC;
            else if( isAlpha(letra) )
                entrada=LETRA;
            else if( java.lang.Character.isDigit(letra) )
                entrada=DIGITO;
            else if( letra == '@')
                entrada=ARROBA;
            else if( letra == '.')
                entrada=SIGNO_PUNTO;
            else
                entrada=ENTRADA_INVALIDA;

            validState();
            if (estado == ESTADO_DE_ACEPTACION){
                debug("Estado de aceptación !");
                System.out.println("La cadena "+datoIngresado+" es un email valido !");
                break;
            }
        }
        if (estado != ESTADO_DE_ACEPTACION){
            debug("Error al analizar texto !");
            System.out.println("La cadena "+datoIngresado+" NO es un email valido !");
        }

    }







    public static void main(String[] args) {
        
        validEmail ve = new validEmail();
        ve.isValidThisEmail( "alicia@gmail.com" );
        ve.isValidThisEmail( "cesar@gmail.com" );
        ve.isValidThisEmail( "edinson@gmail.com" );
        ve.isValidThisEmail( "jose@gmail.com" );
        ve.isValidThisEmail( "@gmail.com" );
        ve.isValidThisEmail( "auto@" );
        ve.isValidThisEmail( "au.com" );
        ve.isValidThisEmail( "au@com" );
        ve.isValidThisEmail( "25jose" );
        ve.isValidThisEmail( "){=" );
        ve.isValidThisEmail( "){=" );
    }

}
