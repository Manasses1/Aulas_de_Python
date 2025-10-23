#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

n1 = str(input("Escolha o primeiro aluno: "))
n2 = str(input("Escolha o segundo aluno: "))
n3 = str(input("Escolha o Terceiro aluno: "))
n4 = str(input("Escolha o quarto aluno: "))
n5 = str(input("Escolha o quinto aluno: "))

#Cria uma lista com os nomes
alunos = [n1, n2, n3, n4, n5]

#Escolhe aleatoriamente
escolhido = random.choice(alunos)

print("O aluno escolhido para apagar o quadro foi {}".format(escolhido))