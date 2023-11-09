# funcion lambda
for i in range(2): # aca el bucle itera 2 veces con i con los valores 0 y 1
    
    for j in range(2): # aca hace lo mismo que lo anterior pero con j
        print(f"{i} & {j} = {operadorand (i, j)}") # aca ya nos imprime el valor de i y j dandonos el resultado de la operacion  


# en esta linea se define la funcion operadorand utlizando lamdba 
operadorand = lambda x, y: x & y
