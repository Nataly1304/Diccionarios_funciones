
#funciones anonimas lambd
#define una funcion lambda llamada numero_palabras que cuenta las palabras en una cadena.
numero_palabras = lambda t: len(t.strip().split())
numero_palabras = lambda t: len(t.strip().split())
#len se refiere a que se cuenta el numero de elementos en la cadena
#strip se refiere que podemos eliminar espacios en blanco al principio y al final de la cadena
#split se refier se utiliza para dividir una cadena en una lista de palabras o elementos

#llama la funcion lambda con una cadena y muestra el numero de palabras
print(numero_palabras("hola, esto es una prueba con lambda"))