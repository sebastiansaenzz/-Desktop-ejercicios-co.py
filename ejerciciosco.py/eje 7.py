                         # ejercicio --> 7

ht = int(input('Ingrese las horas de trabajo semanales del albañil -->'))  
                   # declaracion variable
if ht <= 40:
    pago = ht * 2600
    print('Las horas de trabajo semanales del albañil son:->',ht, 'por lo cual el pago es de->',pago)
else:
    he = ht-40
    total = (he*5000)+(40*2600)
    print('Las horas de trabajo semanales del albañil fueron',ht, 'por lo cual el pago fue de->',total)