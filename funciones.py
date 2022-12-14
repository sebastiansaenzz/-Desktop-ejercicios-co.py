hora_extra = {}

while True:
    name = input("Ingresa el nombre del trabajador: ")
    if name == '':
        break
    
    score = int(input("Ingresa las horas extras del trabajador (0-10): "))
    if score not in range(0, 10):
	    break
    
    if name in hora_extra:
        hora_extra[name] += (score,)
    else:
        hora_extra[name] = (score,)
        
for name in sorted(hora_extra.keys()):
    adding = 0
    counter = 0
    for score in hora_extra[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)