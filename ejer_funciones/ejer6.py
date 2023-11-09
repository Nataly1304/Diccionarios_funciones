# parametro por defecto 

def compra(marca,cantidad,valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    ) # aca nos define de nuevo la funcion compra con sus argumentos donde nos indica que "valor" tiene un valor determiando

print(f' lo comprado fue:{compra("AMD",3)}')
# aca nos imprime la funcion compra con los arguemntos y resultado