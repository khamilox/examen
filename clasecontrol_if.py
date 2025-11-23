# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
num1 = int(input("ingrese un numero entero--->"))
if(num1 < 10):
    print("se ingreso un numero menor que 10")
    print("esto esta fuera del if")
num1 = int(input("ingrese un numero de entero---->"))
if(num1 > 0 ):
    print("se ingreso un numero positivo")
else:
    print("se ingreso un numero negativo o cero")
num1 = int(input("ingrese un numero entero---->"))
if(num1 > 0):
    print("se ingreso un numero positivo")
elif(num1 == 0):
    print("se ingreso un cero")
else:
    print("se ingreso un numero negativo")
print("esto esta fuera del if-elif-else")
