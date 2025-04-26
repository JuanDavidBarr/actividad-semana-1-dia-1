#Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).


#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        numero_usuario = int(input("Ingrese un número " ))
        if numero_usuario >= 1 and numero_usuario <= 10:
            print("El número ", numero_usuario,  " está dentro del rango de 1 a 10")
#"break" se usa para salir del "loop" en el cual ingresamos
            break
        else:
            print("El número ", numero_usuario, " no se encuentra en el rango de 1 a 10")
            break
    except ValueError:
        print("Por favor ingrese solo números")
    