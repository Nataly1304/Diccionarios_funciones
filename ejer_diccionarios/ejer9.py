# borrar un elemnto del diccionario 

calificaciones1 = {
 'Nataly': 5.0, 
 'Adriana':5.0,
 'Stefani':4.5,
 'rosa':2.5
 }

del(calificaciones1['Rosa']) # el del nos sirve para eliminar un elemento por individual
for clave, valor in calificaciones1.items(): # aca itera los elementos del diccionario "calificaciones1"
    
    print(clave,valor) # imrpime ya cada clave y valor del diccioanrio 
