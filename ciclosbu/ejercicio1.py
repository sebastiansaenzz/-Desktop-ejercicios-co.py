# divisores

print ("introduzca el numero")

num= int(input())
contador =0
print("los divisores de" ,num")
for divisor in range (1,num+1):
    if (numero%divisor):
        print(divisor,"es divisor")
        contador+=1
        print("el numero", num, "tiene", "divisores")
        
