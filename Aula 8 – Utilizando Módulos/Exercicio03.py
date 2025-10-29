#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
angulo = float(input('Dgte o angulo que vc deseja: '))
seno = (math.sin(math.radians(angulo)))
print('O angulo de {} tem Seno de {:.2f}'.format(angulo, seno))

cosseno = (math.cos(math.radians(angulo)))
print('O angulo de {} tem Secosseno de {:.2f}'.format(angulo, cosseno))

tangente = (math.tan(math.radians(angulo)))
print('O angulo de {} tem Tangente de {:.2f}'.format(angulo, tangente))