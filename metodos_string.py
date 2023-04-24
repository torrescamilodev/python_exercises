text = 'Aprendiendo a programar Python'

print("programar" in text) # nos dice si en la variable text esta el texto que le colocamos (nos retorna un booleano)

size = len(text) # Nos muestra cuantos caracteres tiene el texto
print(size)

print(text)
print(text.upper()) # Cambia el texto a todos mayusculas
print(text.lower()) # Cambia el texto a todos minusculas
print(text.count('pr')) #Cuenta cuantos caracteres de ese hay en el texto

print(text.swapcase()) # invierte las mayusculas y minusculas
print(text.startswith('Aprend')) # pregunta si el texto comienza con el parametro que se le dio (nos retorna un booleano)
print(text.endswith('Rust')) # pregunta si el texto termina con el parametro que se le dio (nos retorna un booleano)
print(text.replace('Python', 'Go')) # reemplaza el primer parametro por el segundo.

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) # primera letra del texto en mayuscula
print(text_2.title()) # primera letra de cada palabra en mayuscula
print(text_2.isdigit())
print("398".isdigit()) # Si el texto es digitos o no (nos retorna un booleano)