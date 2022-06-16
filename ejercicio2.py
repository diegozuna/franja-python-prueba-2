#EJERCICIO 2
print("INGRESE PALABRA 1")
palabra1 = input()
while (len(palabra1) < 3):
    print("DEBE TENER 3 LETRAS MINIMO")
    palabra1 = input()
print("INGRESE PALABRA 2")
palabra2 = input()
while (len(palabra2) < 3):
    print("DEBE TENER 3 LETRAS MINIMO")
    palabra2 = input()
cont = 0
if palabra1[-1] == palabra2[-1]:
    cont = cont + 1
if palabra1[-2] == palabra2[-2]:
    cont = cont + 1
if palabra1[-3] == palabra2[-3]:
    cont = cont + 1
if cont < 2:
    print("No riman")
if cont == 2:
    print("Riman un poco")
if cont == 3:
    print("Riman")