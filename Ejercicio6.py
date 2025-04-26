#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.
NUMERO_SECRETO = 7

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        numero_de_usuario = int(input("Por favor ingrese un número entero " ))
#Comparo el número ingresado con las condiciones establecidas
        if numero_de_usuario > NUMERO_SECRETO:
            print("Su número es mayor")
#"break" se usa para salir del "loop" en el cual ingresamos
            break
        elif numero_de_usuario < NUMERO_SECRETO:
            print("Su número es menor")
            break
        else: 
            numero_de_usuario == NUMERO_SECRETO
            print("Acertaste!")
            break
    except ValueError:
        print("Por favor ingrese un número entero")