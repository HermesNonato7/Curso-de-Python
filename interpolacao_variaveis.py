# Método format

# Método de interpolação- f-string- Este é o melhor método  

nome= "Hermes"
idade = 36
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade , trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

'''
# Formatação de strings com f-string

 PI = 3.14159
 
 print(f"Valor de PI: {PI:.2f}")
 # >>> "Valor de PI: 3.14"

 print(f"Valor de PI: {PI:10.2f}")
 # >>> "Valor de PI:           3.14"
 '''

nome = "Hermes"
idade = 36
profissao = "Programador"
linguagem = "Python"


print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))


# Método format- Utilizando dicioário

pessoas = {"nome": "Hermes", "idade": 36, "profissao": "Programador", "linguagem": "Python"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoas))


# Método format- outra forma de escrever o format

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Old style %

nome= "Hermes"
idade = 36
profissao = "Programador"
linguagem = "Python"

print("Olá, me chame %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

'''
Das 3 formas de interpolar variáveis em string, a primeira é usando o sinal %, a segunda é utilizando
o método format e a última f strings.

A primeira forma não  é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo focarei
nas 2 últimas.
'''