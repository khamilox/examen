ruleta = [0] * 37

N = int(input("Ingrese un número sorteado (0 al 36): "))
if N >= 0 and N <= 36:
    ruleta[N] = ruleta[N] + 1
else:
    print(-1)

print("Números que no han salido:")
for i in range(37):
    if ruleta[i] == 0:
        print(i, end=" ")
print()

N = int(input("Ingrese un número (0 al 36) para calcular su porcentaje: "))
total = 0
for i in range(37):
    total = total + ruleta[i]

if total == 0:
    porcentaje = 0
else:
    porcentaje = ruleta[N] * 100 / total

print("El número", N, "ha salido el", porcentaje, "% de las veces.")
