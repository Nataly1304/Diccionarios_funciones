# parametros posicionales 
def compra(marca,cantidad,valor): # aca se crea una funcion llamada "compra" de la cual tiene 3 argumrntos marca, cantidad y valor
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    ) 

print(f' lo comprado fue:{compra("AMD",3,2500000)}')
# aca nos imprime la informacion de la compra 