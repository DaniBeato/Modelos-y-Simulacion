class OsciladorLineal():
    def __init__(self, dt=1, tiempo_final=250, elongacion_inicial=0.25, velocidad_inicial=0, masa=100, tiempo_inicial=0,
                 constante_resorte=2.5, constante_amortiguacion=0.5):
        self.dt = dt
        self.tiempo_final = tiempo_final
        self.elongacion_inicial = elongacion_inicial
        self.velocidad_inicial = velocidad_inicial
        self.masa = masa
        self.tiempo_inicial = tiempo_inicial
        self.constante_resorte = constante_resorte
        self.constante_amortiguacion = constante_amortiguacion



    def __str__(self):
        return "dt: " + str(self.dt) + ", " + " tiempo final: " + str(self.tiempo_final) + ", " + " elongación inicial: " \
            + str(self.elongacion_inicial) + ", " + " velocidad inicial: " + str(self.velocidad_inicial) + ", " + " masa: " \
            + str(self.masa) + ", " + " tiempo inicial: " + str(self.tiempo_inicial) + ", " + " constante resorte: " \
            + str(self.constante_resorte) + ", " + " constante amortiguación: " + str(self.constante_amortiguacion) + "."


    def simular_oscilador_lineal(self):
        # Estas listas son para guardar los valores de elongación, velocidad y tiempo, y después añadirlos a un diccionario
        # para poder usarlos en las funciones diagrama_fase y diagrama_elongacion, y así graficarlos.
        elongacion_lista = []
        velocidad_lista = []
        segundo_lista = []
        fuerza_aceleracion = 0
        velocidad = self.velocidad_inicial
        elongacion = self.elongacion_inicial
        for segundo in range(self.tiempo_inicial, self.tiempo_final + 1, self.dt):
            # Este if es para que en el segundo inicial (segundo 0) la velocidad inicial, la elongación inicial y la
            # longitud inicial sean iguales a cero 0.
            if segundo == 0:
                aceleracion = 0
                velocidad = self.velocidad_inicial
                elongacion = self.elongacion_inicial
            else:
                aceleracion = fuerza_aceleracion / self.masa
                velocidad = velocidad + aceleracion * self.dt
                elongacion = elongacion + velocidad * self.dt
            fuerza_resorte = -1 * self.constante_resorte * elongacion
            fuerza_amortiguacion = -1 * self.constante_amortiguacion * velocidad
            fuerza_aceleracion = fuerza_resorte + fuerza_amortiguacion

            elongacion_lista.append(elongacion)
            velocidad_lista.append(velocidad)
            segundo_lista.append(segundo)

            print(" Tiempo: ", segundo, " Elongación: ", elongacion, " Velocidad: ", velocidad, " Incremento: ", self.dt,
                  " Fuerza del resorte", fuerza_resorte, " Fuerza de amortiguación",
                  fuerza_amortiguacion, " Fuerza de aceleracion", fuerza_aceleracion, " Aceleración", aceleracion)

        diccionario_listas = {'Elongación': elongacion_lista, 'Velocidad': velocidad_lista, 'Segundo': segundo_lista}
        return diccionario_listas
