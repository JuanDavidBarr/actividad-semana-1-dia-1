#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero  
    try:
        numero_usuario_1 = int(input("Ingrese el primer número " ))
        while True:
            try:
                numero_usuario_2 = int(input("Ingrese el segundo número " ))
                if numero_usuario_1 > numero_usuario_2:
                    print(numero_usuario_1, " es mayor que ", numero_usuario_2)
#"break" se usa para salir del "loop" en el cual ingresamos
                    break
                elif numero_usuario_1 < numero_usuario_2:
                    print(numero_usuario_2, " es mayor que ", numero_usuario_1)
                    break
                else:
                    print("Los números ingresados son iguales")
                    break
            except ValueError:
                print("Por favor ingrese números enteros")   
        break   
    except ValueError:
        print("Por favor ingrese números enteros")