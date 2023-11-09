# funcion con parametros 
def raiz(value): # "raiz" es una funcion que se crea   
    
    return value ** (1/2) # en esta linea lo que hace es que devuelve la raiz cuadrada de "value"

print(f'La raiz cuadrada es: {raiz(4)}') # aca ya nos imprime el resultado con el argumento 4

def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True") # imprime un mensaje si el "obj" es verdadero
    else:
        
         print(f"{obj} is False") # aca de lo contrario si es falso nos imprime otro mensaje 

validarsiexiste(1) # funcion llamada "validarsiexiste" con un argumento de 1 


