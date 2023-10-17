a1 = int(input('Digite o tamanho o lado A: '))
a2 = int(input('Digite o tamanho o lado B: '))
a3 = int(input('Digite o tamanho o lado C: '))

if (a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2):
    print('É possivél formar um triangulo')
else:
    print('Não é possível formar um triagulo')

elif (a1 == a2) and (a1 == a3):
print('Equilatero')
elif (a1 == a2) or (a1 == a3) or (a2 == a3):
print('Isósceles')
else:
print('Escaleno')