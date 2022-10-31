'''
Prescedencia- A seguinte ordem é a correta:

Parenteses
Expoentes
Multiplicação e divisão (da esquerda para a direita)
Somas e subtrações (da esquerda para a esquerda)
'''
print(10 - 5 * 2)

print((10 - 5) * 2)

print(10 ** 2 * 2)

print(10 ** (2 * 2))

print(10 / 2 * 4)

# Teste pátricos sobre precscedência

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4
print(x)

x = (10 + 5) * 4
print(x)

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)
print(x)
print(y)