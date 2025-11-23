n = int(input("ingrese la cantidad de temperaturas a registrar --> "))
temperaturas = []
print("===")
for i in range(0,n):
    temp = float(input("ingrese temperatura --> "))
    temperaturas.append(temp)
print("===")
suma = sum(temperaturas)
promedio = suma/n
print("el promedio de temperatura es -->",promedio)
print("===")
cantidad = 0
for i in range (0,n):
    if(temperaturas[i]<promedio):
        cantidad = cantidad + 1
print("hay",cantidad,"temperaturas bajo el promedio")
print("===")
