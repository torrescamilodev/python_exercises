text = "Ella sabe Python"
print(text[0])
print(text[1])
size = len(text)
print('size => ',size)
print("ultimo caracter:", text[15])
print(text[size - 1])
print(text[-1])
print( "+" * 30)
# slicing

print(text[0:4]) #iria del 0 al 3, el segundo parametro dice hasta donde va sin coger ese elemento en este caso el parametro es 4 iria hasta el index 3.
print(text[10:16]) 
print(text[:10]) # si el primer parametro es 0 se puede obviar
print(text[5:-1]) #No coge el ultimo valor
print(text[5:]) # si ignoramos el segundo parametro ira recorrera hasta el final del string
print(text[:]) # Se coge el mismo String desde el inicio hasta el final
print(text[10:16:1])
print(text[10:16:2]) #El tercer parametro nos dice de a cuantos paso recorre, si el parametro es 1 recorreria normal. 
print(text[::2])