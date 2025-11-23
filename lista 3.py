milista = [3,12,5,1,7,8,2,9,0,4,2,13,23,6]
num = int(input("ingrese un numero --> "))
if(num in milista):
    i = 0
    while(num!=milista[i]):
        i = i + 1
        print("el numero",num,"esta en el indice",i)
else:
    print("el numero no existe en la lista")
    