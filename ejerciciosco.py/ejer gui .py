#ejercicio 5 guia

print ("cuestionario")

print ("este cusestionario tiene como unica respuesta 'v' (verdadero) 'f' (falso) ")
print ("el programa solo reconocera las respuestas en mayusculas")

pregunta1 = "¿Colon descubrió América?"
pregunta2 = "¿La independencia de Colombia fue en el año 1810?"
pregunta3 = "¿The Doors fue un grupo de rock Americano?"

respuesta1 = "v"
respuesta2 = "v"
respuesta3 = "v"

formulacion1= input(f"pregunta 1 :{pregunta1}")
formulacion2= input(f"pregunta 2 :{pregunta2}")
formulacion3= input(f"pregunta 3 :{pregunta3}")

aciertos1 = False 
aciertos2 = False
aciertos3 = False

#pregunta1
if (formulacion1 == respuesta1):
    aciertos1 = True
    else:
 aciertos1 = False

 #pregunta 2       
if (formulacion2 == respuesta1):
    aciertos2 = True
    else:
aciertos2 = False
#pregunta 3
if (formulacion3 == respuesta1):
    aciertos3 = True
    else 
aciertos3 = False
#respuesta1
if (aciertos1 == True):
    print ("pregunta 1 es correcta")

    else:

    print ("pregunta 1 es incorrecta")
#respuesta2
if (aciertos2 == True):
    print ("pregunta 2 es correcta")

    else:

    print ("pregunta 2 es incorrecta")    
#respuesta3
if (aciertos3 == True):
    print ("pregunta 3 es correcta")

    else:

    print ("pregunta 3 es incorrecta")      
