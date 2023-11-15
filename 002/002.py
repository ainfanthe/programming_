#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# 002: Temperature Converter

def converter():
    print("\n--Temperature Converter--\n")
    print("[1] °F to °C")
    print("[2] °C to °F\n")
    option = int(input(''))
    if option == 1:
         # (°F - 32) × 5/9
        fahrenheit = int(input('Fahrenheit: '))
        celsius = (fahrenheit - 32) * 5/9
        print('{} °F -> {} °C').format(fahrenheit, celsius)
    elif option == 2:
        # (9/5) °C+32
        celsius = int(input('Celsius: '))
        fahrenheit = (9/5) * celsius + 32
        print('{} °C -> {} °F'.format(celsius, fahrenheit))
converter()