from os import system;system("cls")
import sys
asientos = ['O'] * 100
precios = [120000, 80000, 50000]
asistentes = []


def comprar_entradas():
    print("Ingrese cantidad de entradas a comprar:")
    cantidad = int(input())

    if cantidad < 1 or cantidad > 3:
        print("cantidad invalida")
        return

    for i in range(cantidad):
        print("Seleccione un asiento :")
        mostrar_asientos_disponibles()

        asiento = int(input())

        if asientos[asiento] == 'X':
            print("no esta disponible. Por favor, elija otro.")
            i -= 1
        else:
            print("Ingrese el rut del asistente:")
            run = input()

            if validar_run(run) and run not in asistentes:
                asistentes.append(run)
            else:
                print("El rut es inválido ")

            
            asientos[asiento] = 'X'

    print("registrado correctamente")


def mostrar_asientos_disponibles():
    print("----- ASIENTOS DISPONIBLES -----")
    for i in range(10):
        for j in range(10):
            if asientos[i * 10 + j] == 'O':
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()


def mostrar_listado_asistentes():
    asistentes_ordenados = sorted(asistentes)
    print("----- LISTADO DE ASISTENTES -----")
    for asistente in asistentes_ordenados:
        print(asistente)

def mostrar_ganancias_totales():
    total = 0
    for i in range(3):
        cantidad = asientos.count('X', i * 30, (i + 1) * 30)
        print("Tipo de entrada:", obtener_tipo_entrada(i))
        print("Cantidad:", cantidad)
        print("Total: $", precios[i] * cantidad)
        print()
        total += precios[i] * cantidad

    print("TOTAL: $", total)


def validar_run(run):
    if run.isdigit():
        return True
    else:
        return False
    
def obtener_tipo_entrada(indice):
    if indice == 0:
        return "Platinum"
    elif indice == 1:
        return "Gold"
    elif indice == 2:
        return "Silver"


def menu():
    while True:
        print("----- MENu--------")
        print("1. Comprar ")
        print("2.  disponibles")
        print("3.  listado ")
        print("4. ganancias")
        print("5. Salir")
        print()

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            comprar_entradas()
        elif opcion == 2:
            mostrar_asientos_disponibles()
        elif opcion == 3:
            mostrar_listado_asistentes()
        elif opcion == 4:
            mostrar_ganancias_totales()
        elif opcion == 5:
            print ("hasta luego ")
            sys.exit()
        else:
            print ("error")
menu()