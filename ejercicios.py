num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
if(num1==num2):
    print("los numeros son iguales")
else:
    print("los numeros son diferentes ")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El número mayor es {num1}.")
elif num2 > num1:
    print(f"El número mayor es {num2}.")
else:
    print("Ambos números son iguales.")
num = int(input("Ingrese un número: "))

if num == 1:
    print("Es uno.")
elif num == 2:
    print("Es dos.")
elif num == 3 or num == 4:
    print("Es tres o cuatro.")
else:
    print("No es 1, 2, 3 ni 4.")

