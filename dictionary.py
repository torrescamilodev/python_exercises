my_dict = {}
print(type(my_dict))

my_dict = {
  'name': 'Camilo Andrés',
  'last_name': 'Torres Rodríguez',
  'age': 24
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age')) #si no existe retorna un none y no un error, mejor usar get

print('name' in my_dict) #solo sirve con las llaves
print('person' in my_dict)
print('Camilo' in my_dict)

print('')
print('')
print('')


person = {
  'name': 'Camilo',
  'last_name': 'Torres',
  'langs': ['python', 'javascript'],
  'age': 24
}

print(person)

person['name'] = 'Andrés'
person['age'] += 1 
person['langs'].append('java')
print(person)

del person['last_name'] #eliminar elemento
person.pop('age') # eliminar elemento

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())

person['twitter'] = 'torrescamilodev@gmail.com' #Agregar una llave al diccionario

print(person)