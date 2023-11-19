#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# 004: Caesar cipher

def cifrar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha(): 
            offset = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - offset + clave) % 26 + offset)
        else:
            resultado += caracter
    return resultado

def descifrar(texto_cifrado, clave):
    return cifrar(texto_cifrado, -clave)

texto_original = input("Texto: ")
clave_secreta = int(input("Clave: "))

texto_cifrado = cifrar(texto_original, clave_secreta)
print(f'Texto cifrado: {texto_cifrado}')

texto_descifrado = descifrar(texto_cifrado, clave_secreta)
print(f'Texto descifrado: {texto_descifrado}')


