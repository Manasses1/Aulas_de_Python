# Programa que lê dois valores e mostra a soma, o produto, a divisão, a divisão inteira e a potência
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma é {}, o produto é {}, e a divisão é {:.5f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
