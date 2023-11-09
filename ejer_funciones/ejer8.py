# parametros mutables 
def listalimpia(arg, result=None): # aca se define la funcion "listalimpia" donde tiene 2 argumentos arg y result
    if result is None:
        result = []
        result.append(arg) # aca se agrega el argumento arg a la lista result
        print(result)
        
# donde arg se refiere el elemento que se va agregar a la lista
# y reult se refiere a una lista opcional es decir "None"

# se llama la funcion "a" y "b" como argumento, que es lo que se imprimira. 
listalimpia("a") 
listalimpia("b") 



