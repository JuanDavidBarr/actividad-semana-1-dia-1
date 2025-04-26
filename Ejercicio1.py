# 1. Mayor de Edad
# Pide al usuario su edad. Si tiene 18 años o más, imprime "Eres mayor de edad". Si no, imprime "Eres menor de edad".

#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        edad_usuario = int(input("Ingrese su edad: " ))
#Comparo la edad del usuario con 18, ya que esta es la mayoría de edad en colombia
        if edad_usuario >= 18:
            print("Usted es mayor de edad")
        else: 
            print("Usted es menor de edad")
#"break" se usa para salir del "loop" en el cual ingresamos
        break
    except ValueError:
        print("Por favor ingrese solo números")