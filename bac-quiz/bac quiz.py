bac=int(input("ingrese poblacion inicial"))
bac1=bac*2
p=float(input("ingrese porcentaje de crecimiento"))
while bac<bac1:
    print('bac',bac)
    bac=bac+(bac*p)
    peint("bacterias",bac)