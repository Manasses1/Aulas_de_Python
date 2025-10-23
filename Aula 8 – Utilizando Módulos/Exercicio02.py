#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math
ca = int(input("Comprimento do cateto adjacente: "))
co = int(input("Comprimento do cateto oposto: "))

hipotenusa = math.hypot(ca, co)

print("A hipotenusa é {}".format(hipotenusa))

#Usado method hypot
