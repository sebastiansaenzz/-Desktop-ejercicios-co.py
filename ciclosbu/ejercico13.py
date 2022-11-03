numero = list(input("ingrese un numero de 9 cifras"))
numero.reverse()

numero_al_reves = ''

for elemento in numero:
    numero_al_reves += elemento
print(numero_al_reves) 