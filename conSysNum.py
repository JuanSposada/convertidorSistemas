#!/usr/bin/env python
#
# Convertidor de Sistemas
#
# Juan Sebasatian Moreno Posada
# Sept/18/2023
# al22760047.AT.ite.dot.edu.dot.mx

import argparse
import sys


def validacion(**kwargs):
    numero = 0
    for key, value in kwargs.items():
        if key == 'numero':
            if value < 0:
                print('No se puede ingresar un valor negativo')
                sys.exit(2)
            numero = value
    return numero

def convBin(numero):

    binario = ''
    while numero > 0:
        modulo = numero % 2
        numero = numero // 2
        binario = str(modulo) + binario

    return binario

def convOct(numero):
    octal = ''
    while numero > 0:
        modulo = numero % 8
        numero = numero // 8
        octal = str(modulo) + octal
    return octal

def convHex(numero):
    hexa = ''
    while numero > 0:
        modulo = numero % 16
        numero = numero // 16
        if modulo > 9:
            if modulo == 10:
                modulo = 'A'
            elif modulo == 11:
                modulo = 'B'
            elif modulo == 12:
                modulo = 'C'
            elif modulo == 13:
                modulo = 'D'
            elif modulo == 14:
                modulo = 'E'
            elif modulo == 15:
                modulo = 'F'
        hexa = str(modulo) + hexa
    return hexa

def main(**kwargs):
    numero = validacion(**kwargs)

    print('decimal: ' + str(numero))
    print("binario: " + str(convBin(numero)))
    print('octal: ' + str(convOct(numero)))
    print('Hexa : ' + str(convHex(numero)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='convSysNum',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
                    Convertidor de Sistemas numericos, ingresando un numero decimal por el usuario,
                    por medio de consola con la isntruccion, de esta manera que si se quiere
                     ejecutar el codigo debe declararse como:
                                        <archivo.py> --numero 345
                    el programa calcula su valor en binario, octal y en hexadecimal
        ''',
        epilog='''
                    La informacion se desplegara en pantalla, imprimiendo los resultados
        '''
    )
    parser.add_argument('-n', '--numero', dest='numero',
                        help='Numero decimal que se desea convertir',
                        type=int, required=True)
    datos_ingresar = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**datos_ingresar)

