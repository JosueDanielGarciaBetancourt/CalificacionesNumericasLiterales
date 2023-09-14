class Calificaciones():
    def __init__ (self, calificacion_numero):
        self.calificacion_numero = calificacion_numero
        self.calificacion_letra = ""

    def evaluar (self):
        if (self.calificacion_numero > 9.0):
            self.calificacion_letra = "A"
        elif (self.calificacion_numero > 8.0):
            self.calificacion_letra = "B"
        elif (self.calificacion_numero >= 7.5):
            self.calificacion_letra = "C"
        else:
            self.calificacion_letra = "R"
    def imprimirCalificacionLetra (self):
        print(f"La calificación literal es: {self.calificacion_letra}")