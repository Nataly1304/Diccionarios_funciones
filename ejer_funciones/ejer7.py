#parametros mutables 

#Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes
#define una funcion llamada lista donde toma dos argumentos que es arg y result.
# arg es el argumento que se va agregar a la lista y result se toma como una lista vacia 
def lista(arg, result=[]):
 result.append(arg)
 print(result)

#llama la funcion lista con la cadena "domingo" y una lista vacia
lista('domingo', [])