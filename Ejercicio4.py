#4. Contraseña Correcta
#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".
#Utilizo estos contadores para contabilizar los intentos del usuario al momento de ingresar la contraseña
contador = 1
contador2 = 1

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while contador <= 5:
    contrasena_usuario = input("Ingrese su contraseña: " )
#Comparo la contraseña ingresada con la cadena correcta, para así validar el ingreso
    if contrasena_usuario == "python123":
        print("Acceso concedido")
#"break" se usa para salir del "loop" en el cual ingresamos
        break
    else:
#Cada vez que se equivoca, los contadores suman para llegar hasta el límito establecido
        print(f"Contraseña incorrecta, tiene {5 - contador2} intentos más")
        contador = contador + 1
        contador2 = contador2 + 1
        if contador == 6:
            print("Su cuenta ha sido bloqueada")