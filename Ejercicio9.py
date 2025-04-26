#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).


#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        año_ingresado = int(input("Ingrese un año " ))
        if año_ingresado % 100 == 0 and año_ingresado % 400 == 0:
            if año_ingresado % 4 == 0:
                print("El año ", año_ingresado, " es biciesto")
#"break" se usa para salir del "loop" en el cual ingresamos
                break
        else:
            if año_ingresado % 4 == 0 and año_ingresado % 100 != 0:
                print("El año", año_ingresado, " es biciesto")
                break
            else:
                print("El año", año_ingresado, " no es biciesto")
                break
    except ValueError:
        print("Por favor ingrese solo números")
    
