import os
inicializacion = True

print("Bienvenid@ a la aplicación de estadísticas animales en Madrid")

while inicializacion:
    print("Elija la opción que quiera ejecutar")
    print("[1] Comparación número animales por año y evolución relativa (normalizada) de perros y gatos")
    print("[2] Evolución total del censo - Perros vs Gatos" )
    print("[3] Evolución por distrito - Colores por especie")
    print("[4] Número perros por distrito 2024 MADRID")
    print("[5] Número gatos por distrito 2024 MADRID")
    print("[6] Relación entre personas y perros por distrito (normalizado)")
    print("[7] Parques Caninos vs Perros por distrito (normalizado)")
    print("[8] Salir")

    user_choice = input("Escriba su elección: ")
    if not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 8:
        print("Error. Debe de introducir un número entre 1-9")
        input("Pulse enter para continuar")
        continue

    match user_choice:
        case "1":
            os.system('py CensoAnimales1_Operaciones.py')
        case "2":
            os.system('py CensoAnimales2_Totales.py')
        case "3":
            os.system('py CensoAnimales3_SuperDistritos.py')
        case "4":
            os.system('py CensoAnimales4_PerrosDistrito.py')
        case "5":
            os.system('py CensoAnimales5_GatosDistrito.py')
        case "6":
            os.system('py CensoAnimales6_RatioPersonasPerros.py')
        case "7":
            os.system('py CensoAnimales7_ComparacionParquePerrosDistrito.py')
        case "8":
            inicializacion = False
            print("Muchas gracias por usar nuestra aplicación")
        case _:
            print("Lo sentimos, un error inesperado ha sucedido")
            inicializacion= False
