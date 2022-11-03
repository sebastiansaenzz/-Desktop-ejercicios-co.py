                                   #ejercicio --->6

d = int(input("Ingrese un número este será convertido a el mes que corresponde en el año --->"))
if d <= 31:
    print("Es el",d, "mes de enero")
elif d <= 59:
    f = d - 31
    print("Es el",f, "mes de febrero")
elif d <= 90:
    m = d - 59
    print('Es el',m, 'mes de marzo')
elif d <= 121:
    a = d - 90
    print('Es el',a, 'mes de abril')
elif d <= 152:
    ma = d - 121
    print('Es el',ma, 'mes de mayo')   
elif d <= 182:
    j = d - 152
    print('Es el',j, 'mes de junio')
elif d <= 213:
    ju = d - 182
    print('Es el',ju, 'mes de julio')
elif d <= 244:
    ag = d - 213
    print('Es el',ag, 'mes de agosto')
elif d <= 274:
    s = d - 244
    print('Es el',s, 'mes de septiembre')
elif d <= 305:
    o = d - 274
    print('Es el',o, 'mes de octubre')
elif d <= 335:
    n = d - 305
    print('Es el',n, 'mes de noviembre')
elif d <= 366:
    di = d - 335
    print('Es el',di, 'mes de diciembre')
else:
    print('El número está fuera de lo permitido')    
print ("fin del programa")                               

