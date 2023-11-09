# tecnica de iterar los diccionarios 
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']
for n, e in zip(nombres, edades): 
    print('Tú nombre es {0}  y tu edad {1}.'.format(n, e)) # en esta linea se imprime el nombre y la edad. utlizando el format de cadenas 
