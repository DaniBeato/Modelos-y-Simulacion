from oscilador_lineal import OsciladorLineal
from diagrama import Diagrama

import time

oscilador_lineal_preestablecido = OsciladorLineal()
diagrama = Diagrama()



class Menu():

    def mostrar_menu_principal(self):
        while True:
            print("\n")
            print("-------------------------------------------------------")
            print("BIENVENIDO AL SIMULADOR DE OSCILADOR LINEAL")
            print("-------------------------------------------------------")
            print("Elija una opción")
            print("1. Simular con parámetros preestablecidos")
            print("2. Simular con parametros modificados manualmente")
            print("3. Salir")
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)
                self.mostrar_menu_principal()
            if opcion == int(1):
                self.mostrar_menu_parametros_preestablecidos()
            elif opcion == int(2):
                self.mostrar_menu_parametros_modificados()
            elif opcion == int(3):
                print("Saliendo...")
                time.sleep(3)
                exit()
            else:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)


    def mostrar_menu_parametros_preestablecidos(self):
        while True:
            print("\n")
            print("-------------------------------------------------------")
            print("SIMULACIÓN CON PARÁMETROS PREESTABLECIDOS")
            print("-------------------------------------------------------")
            print("Elija una opción")
            print("1. Mostrar parámetros preestablecidos")
            print("2. Realizar simulación")
            print("3. Volver al menú principal")
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)
                self.mostrar_menu_parametros_preestablecidos()
            if opcion == int(1):
                print(oscilador_lineal_preestablecido)
                time.sleep(3)
            elif opcion == int(2):
                resultados = oscilador_lineal_preestablecido.simular_oscilador_lineal()
                time.sleep(3)
                self.mostrar_menu_graficacion(resultados)
            elif opcion == int(3):
                self.mostrar_menu_principal()
            else:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)



    def mostrar_menu_graficacion(self, resultados):
        while True:
            print("\n")
            print("-------------------------------------------------------")
            print("OPCIONES DE GRAFICACIÓN")
            print("-------------------------------------------------------")
            print("Elija una opción")
            print("1. Mostrar diagrama de fase (velocidad respecto a la elongación)")
            print("2. Mostrar diagrama de elongación (elongación respecto al tiempo)")
            print("3. Volver al menú principal")
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)
                self.mostrar_menu_graficacion(resultados)
            if opcion == int(1):
                diagrama.mostrar_diagrama_fase(resultados['Elongación'], resultados['Velocidad'])
            elif opcion == int(2):
                diagrama.mostrar_diagrama_elongacion(resultados['Segundo'], resultados['Elongación'])
            elif opcion == int(3):
                self.mostrar_menu_principal()
            else:
                print("\nOpción inválida. Ej: 1")
                time.sleep(3)



    def mostrar_menu_parametros_modificados(self):
        while True:
            print("\n")
            print("-------------------------------------------------------")
            print("SIMULAR CON PARÁMETROS MODIFICADOS MANUALMENTE")
            print("-------------------------------------------------------")
            dt = int(1)
            try:
                tiempo_final = int(input("Ingrese el tiempo final (segundos): "))
            except ValueError:
                print("\nOpción inválida. Ej: 50")
                time.sleep(3)
                self.mostrar_menu_parametros_modificados()
            try:
                elongacion_inicial = float(input("Ingrese la elongación inicial (metros): "))
            except ValueError:
                print("\nOpción inválida. Ej: 0.78")
                time.sleep(3)
                self.mostrar_menu_parametros_modificados()
            velocidad_inicial = int(0)
            try:
                masa = float(input("Ingrese la masa (kilogramos): "))
            except ValueError:
                print("\nOpción inválida. Ej: 90.5")
                time.sleep(3)
                self.mostrar_menu_parametros_modificados()
            tiempo_inicial = int(0)
            try:
                constante_resorte = float(input("Ingrese la constante del resorte: "))
            except ValueError:
                print("\nOpción inválida. Ej:2.5")
                time.sleep(3)
                self.mostrar_menu_parametros_modificados()
            try:
                constante_amortiguacion = float(input("Ingrese la constante de amortiguación: "))
            except ValueError:
                print("\nOpción inválida. Ej: 0.5")
                time.sleep(3)
                self.mostrar_menu_parametros_modificados()
            oscilador_lineal_modificado = OsciladorLineal(dt, tiempo_final, elongacion_inicial, velocidad_inicial, masa,
                                                          tiempo_inicial, constante_resorte, constante_amortiguacion)
            resultados = oscilador_lineal_modificado.simular_oscilador_lineal()
            time.sleep(3)
            self.mostrar_menu_graficacion(resultados)



