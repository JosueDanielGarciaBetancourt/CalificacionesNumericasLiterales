from logica.Calificaciones import Calificaciones

if __name__ == '__main__':
    calificacionNumerica = float(input("Ingrese la calificación numérica: "))
    calificaciones = Calificaciones(calificacionNumerica)
    calificaciones.evaluar()
    calificaciones.imprimirCalificacionLetra()

