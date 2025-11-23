def ingresar_notas(n):
    notas = []
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def contar_menores_al_promedio(lista):
    promedio = calcular_promedio(lista)
    menores = [x for x in lista if x < promedio]
    return len(menores)

# Ejemplo de uso:
N = int(input("Ingrese la cantidad de notas: "))
lista_notas = ingresar_notas(N)

print("Promedio de notas:", calcular_promedio(lista_notas))
print("Cantidad de notas bajo el promedio:", contar_menores_al_promedio(lista_notas))

