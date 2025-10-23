# Programa que lê um valor em metros e mostra convertido em centímetros e milímetros
m = float(input('Coloque um valor em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros equivalem a {:.0f} centímetros e {:.0f} milímetros.'.format(m, cm, mm))


