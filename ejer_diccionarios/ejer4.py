#estrcutura para hacer iteracion en diccionarios 
calificaciones = {
 'nombre': 'Nataly', 
 'notafinal': 5.0   # se crea una variable calificaciones donde le aisgnamos unos valores 
 }
calificaciones1 = {
 'Nataly': 5.0, 
 'Adriana':5.0,
 'Stefani':4.5,
 'Luis':2.5
 }

# clave es Nataly y valor es 5.0
for clave, valor in calificaciones.items(): # .items se utiliza en diccionarios para obtener una vista de calificaciones almacenadas en el diccionario

    print(clave,valor) #aca imprime la clave que es "nombre" y valor "notafinales".