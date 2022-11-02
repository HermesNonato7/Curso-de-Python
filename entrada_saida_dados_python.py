nome = "Hermes"
sobrenome = "Nonato"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="-")

'''
A função builtin print recebe um argumento obrigatório do tipo varargs
de objeto e 4 argumentos opcionais (sep, end, file e flush).
Todos os objetos são convertidos em string, separados por sep e
terminados por end.
'''