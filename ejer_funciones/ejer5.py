# parametros nominales 

def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    ) # aca definimos de nuevo la funcion compra con los mismos parametros.
    

print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')
# aca nos imprime la funcion compra donde nos muestra los parametros por nombre