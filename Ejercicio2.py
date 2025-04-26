#2. Número Positivo o Negativo
#Pide un número al usuario. Di si es positivo, negativo o si es cero.

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        numero_usuario = float(input("Ingrese un número: " ))
#Comparo el número ingresado con 0 para verificar que sea positivo, negativo o igual a cero
        if numero_usuario > 0:
            print("El número ingresado es positivo")
        elif numero_usuario == 0:
            print("El número ingresado es cero")
        else:
            print("El número ingresado es negativo")
#"break" se usa para salir del "loop" en el cual ingresamos
        break
    except ValueError:
        print("Ingrese solo números")