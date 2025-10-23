# Programa que lê um número e mostra o dobro, o triplo e a raiz quadrada
n = int(input('Escolha um número: '))
dn = n * 2
tn = n * 3
rn = n**0.5
print('O número escolhido foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n, dn, tn, rn))
