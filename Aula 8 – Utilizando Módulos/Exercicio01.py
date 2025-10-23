#Crie um programa que leia um numero Real qualquer pelo teclado e mostra na tela a sua porção inteira.
#Ex:
#Digite um numero: 6.127. O numero 6.127 tem sua parte inteira 6.

num = float(input('Digite um numero: '))
print('O numero digitado foi {}, e a porção inteira é {}'.format(num, int(num)))