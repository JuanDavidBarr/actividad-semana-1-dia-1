#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:
#"Bajo peso" si es menor a 18.5
#"Normal" si está entre 18.5 y 24.9
#"Sobrepeso" si está entre 25 y 29.9
#"Obesidad" si es mayor o igual a 30


#Utilizo "while" para repetir la instrucción de ingresar edad en caso tal que el usuario ingrese un valor no válido.
while True:
#Utilizo "try", para que no me aparezca un error en caso de que la variable ingresada no sea de tipo entero 
    try:
        peso_usuario = float(input("Ingrese su peso en kilogramos " ))
        while True:
            try:
                altura_usuario = float(input("Ingrese su altura " ))
                imc_usuario = peso_usuario / (altura_usuario**2)
                if imc_usuario < 18.5:
                    print("Usted tiene bajo peso")
#"break" se usa para salir del "loop" en el cual ingresamos
                    break
                elif imc_usuario >= 18.5 and imc_usuario <= 24.9:
                    print("Usted tiene un peso normal")
                    break
                elif imc_usuario >= 25 and imc_usuario <= 29.9:
                    print("Usted tiene sobrepeso")
                    break
                else:
                    imc_usuario >= 30
                    print("Usted sufre de obesidad")
            except ValueError:
                print("Por favor ingrese solo números")
    except ValueError:
        print("Por favor ingrese solo números")