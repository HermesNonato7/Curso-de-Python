nome = "HerMeS"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))
print("-".join(menu))

# O códigpo a seguir simula o join, porém têm a escrita mais longa
'''
for letra in menu:
    print(letra, end="-")
print()
'''