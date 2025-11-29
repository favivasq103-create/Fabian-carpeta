import random
variable="||'¿¿94091834508354032852jfaifjifjafiejfeiej49848948983983"
longitud=int(input("ingresa la longitud de la contraseña:"))
contra_generada=""
for i in range(longitud):
    contra_generada+=random.choice(variable)
print("Contraseña generada", contra_generada)
