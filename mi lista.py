milista = [3,12,5,1,7,8,2,9,0,4,2,13,23,6]
print(milista)
milista.append(55) #agrega el 55
print(milista)
suma = sum(milista) #suma toda la lista (debe ser 150)
print(suma)
largo = len(milista) #guarda la cantidad de elementos en la lista (15 son)
print(largo)
milista.pop() #elimina el ultimo elemento (en este caso el 55)
print(milista)
milista.pop(1) #elimina el contenido del indice 1 en este caso el 12
print(milista)
milista.remove(2) #elimina el primer numero 2 de la lista en la lista (este entre el 8 y el 9)
print(milista)
minimo = min(milista) #obtiene el minimo elemento en la lista (es el 0 )
print(minimo)
maximo = max(milista) #obtiene el maximo elemento en la lista (es el 23)
print(maximo)
