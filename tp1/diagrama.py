import matplotlib.pyplot as plt

class Diagrama():

    def mostrar_diagrama_fase(self, elongacion_lista, velocidad_lista):
        plt.plot(elongacion_lista, velocidad_lista)
        plt.xlabel('Elongación')
        plt.ylabel('Velocidad')
        plt.title('Diagrama de Fase')
        plt.show()

    def mostrar_diagrama_elongacion(self, segundo_lista, elongacion_lista):
        plt.plot(segundo_lista, elongacion_lista, color='red')
        plt.xlabel('Tiempo (Segundos)')
        plt.ylabel('Elongación (Metros)')
        plt.title('Diagrama de Elongación')
        plt.show()

