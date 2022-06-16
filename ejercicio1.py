#EJERCICIO 1
lista = ['adkjdkasjdaskdj', 'aa', 'aaa', 'aaaa']

def palabra_mas_larga(lista):
    largo = 0
    for palabra in lista:
        largo_aux = len(palabra)
        if (largo_aux > largo):
            palabra_aux = palabra
            largo = largo_aux
    return palabra_aux        
            
print(palabra_mas_larga(lista))