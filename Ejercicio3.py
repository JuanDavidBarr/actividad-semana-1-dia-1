#3. Par o Impar
#Pide un número entero. Indica si es par o impar.

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero
    try:
        numero_usuario = int(input("Ingrese un número entero: " ))
#Utilizo la operación "módulo" para verificar que el número ingresado sea par
        if numero_usuario % 2 == 0:
            print(numero_usuario, " es par")
        else: 
            print(numero_usuario, " es impar")
#"break" se usa para salir del "loop" en el cual ingresamos
        break
    except ValueError:
        print("Ingrese por favor solo números enteros")