" This file is for blah blah blah "

ejemplo = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 'b', 'c']

# Agregar elemento
ejemplo.append('lol')

# Agregar un elmento en un lugar especifico
ejemplo.insert(2, 'babayaga')

# Quitar elemento especifico
ejemplo.remove('c')

# remove elemento segun posicion
ejemplo.pop(3)

# Elminar elemento por su indice
del ejemplo[1]

# contar nro de veces que aparece un elmento en una lista

conteo = ejemplo.count(7)

print(ejemplo)

# recorrer con for

for i in ejemplo:
    print(i)
