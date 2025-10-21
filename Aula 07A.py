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


# Programa que mostra um número inteiro, seu sucessor e antecessor
n = int(input('Escolha um número: '))
sn = n + 1
tn = n - 1
print('O número escolhido foi {}, e seu sucessor é {}, e seu antecessor é {}'.format(n, sn, tn))


# Programa que lê um número e mostra o dobro, o triplo e a raiz quadrada
n = int(input('Escolha um número: '))
dn = n * 2
tn = n * 3
rn = n**0.5
print('O número escolhido foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n, dn, tn, rn))


# Programa que lê duas notas de um aluno, calcula e mostra a média
nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('Com base em suas notas, sua média é: {:.1f}'.format(media))


# Programa que lê um valor em metros e mostra convertido em centímetros e milímetros
m = float(input('Coloque um valor em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros equivalem a {:.0f} centímetros e {:.0f} milímetros.'.format(m, cm, mm))


# Programa que lê um número inteiro qualquer e mostra a sua tabuada
n = int(input('Coloque um número: '))
print('A tabuada de {} é:'.format(n))
print('{} x 1 = {}'.format(n, n * 1))
print('{} x 2 = {}'.format(n, n * 2))
print('{} x 3 = {}'.format(n, n * 3))
print('{} x 4 = {}'.format(n, n * 4))
print('{} x 5 = {}'.format(n, n * 5))
print('{} x 6 = {}'.format(n, n * 6))
print('{} x 7 = {}'.format(n, n * 7))
print('{} x 8 = {}'.format(n, n * 8))
print('{} x 9 = {}'.format(n, n * 9))
print('{} x 10 = {}'.format(n, n * 10))
