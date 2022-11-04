# Maiúsculs, minúsculas e título

print("maiúsculas, minúsculas e título\n")

curso = "pYtHon"

print(curso.upper())
# >>> "PYTHON"

print(curso.lower())
# >>> "python"

print(curso.title())
# >>> "Python"
print("")
print("Removendo espaços em branco\n")

curso_2 = "    Python"

print(curso_2.strip())
# >>> "Python"

print(curso_2.lstrip())
# >>> "Python "

print(curso_2.rstrip())
# >>> " Python"

# Junções e centralização

curso_3 = "Python"

print(curso_3.center(10, "#"))
# >>> "##Python##"

print(".".join(curso_3))
# >>> "P.y.t.h.o.n"

