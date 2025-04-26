# Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        cuenta_usuario = int(input("Ingrese el total de su cuenta " ))
        while True:
            try:
                porcentaje_propina = int(input("Ingrese el porcentaje de propina que quiere " ))
#Comparo el valor ingresado con los valores disponibles según las políticas del restaurante
                if porcentaje_propina == 10 or porcentaje_propina == 15 or porcentaje_propina == 20:
                    print("Su propina es: ", (porcentaje_propina / 100) * cuenta_usuario)
#"break" se usa para salir del "loop" en el cual ingresamos
                    break
                else:
                    print("Por favor ingrese alguno de los valores mencionados: 10, 15 o 20")
            except ValueError:
                print("Por favor ingrese solo valores numéricos")  
#"break" se usa para salir del "loop" en el cual ingresamos
        break                  
    except ValueError:
        print("Por favor ingrese solo valores númericos")