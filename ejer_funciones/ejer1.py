# forma de definir una funcion 
def saludar(): # se define una funcion llamada "saludar"
    print("saludo")

def retornarNumero(): # se define una funcion llamada "retornarnumero"
    return 1

saludar() 
retornarNumero() 

if retornarNumero()==1: # en esta linea lo que se hace es que se verifica si el valor retorneado por la funcion es igual a 1 
    print("devolvió un uno") # aca ya se imprime
else:
    print("No devolvió un uno")# se coloca un else por si la funcion no se cumple
