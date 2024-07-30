from datetime import datetime


class Campeonato:
    def _init_(self, fechaInicio, fechaFin, nombreCampeonato, premio):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.nombreCampeonato = nombreCampeonato
        self.premio = premio
        self.equipos = []

    def iniciarEvento(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def terminarEvento(self, fechaFin):
        self.fechaFin = fechaFin

    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)


class Futbol:
    def _init_(self, categoria, reglamento):
        self.categoria = categoria
        self.reglamento = reglamento


class Equipo:
    def _init_(self, carrera, puntos):
        self.carrera = carrera
        self.puntos = puntos
        self.jugadores = []

    def agregarJugador(self, nombre, posicion):
        jugador = Jugador(nombre, posicion)
        self.jugadores.append(jugador)


class Jugador:
    def _init_(self, nombreJugador, posicion):
        self.nombreJugador = nombreJugador
        self.posicion = posicion


class Registro:
    def _init_(self, costo):
        self.costo = costo

    def agregarEquipo(self, carrera, categoria):
        equipo = Equipo(carrera, 0)
        # Aquí puedes manejar la lógica de agregar equipos al registro


class Partido:
    def _init_(self, fecha, equipoA, equipoB, horarioInicio, horaFin):
        self.fecha = fecha
        self.equipoA = equipoA
        self.equipoB = equipoB
        self.horarioInicio = horarioInicio
        self.horaFin = horaFin
        self.golesEquipoA = 0
        self.golesEquipoB = 0
        self.numeroFaltasEquipoA = 0
        self.numeroFaltasEquipoB = 0

    def decidirGanador(self):
        if self.golesEquipoA > self.golesEquipoB:
            return self.equipoA
        elif self.golesEquipoA < self.golesEquipoB:
            return self.equipoB
        else:
            return "Empate"

    def agregarEstadisticas(self, golesA, golesB, faltasA, faltasB):
        self.golesEquipoA += golesA
        self.golesEquipoB += golesB
        self.numeroFaltasEquipoA += faltasA
        self.numeroFaltasEquipoB += faltasB


class EstadisticaCampeonato:
    def _init_(self):
        self.estadisticas = []

    def presentarEstadistica(self, golesEquipoA, golesEquipoB, numeroFaltasEquipoA, numeroFaltasEquipoB):
        estadistica = {
            "golesEquipoA": golesEquipoA,
            "golesEquipoB": golesEquipoB,
            "numeroFaltasEquipoA": numeroFaltasEquipoA,
            "numeroFaltasEquipoB": numeroFaltasEquipoB
        }
        self.estadisticas.append(estadistica)

    def actualizarEstadistica(self, golesEquipoA, golesEquipoB, numeroFaltasEquipoA, numeroFaltasEquipoB):
        # Lógica para actualizar estadísticas, esto depende de cómo se quiera manejar
        pass


class Ranking:
    def _init_(self, posicion):
        self.posicion = posicion

    def presentarGanador(self, golesEquipoA, golesEquipoB, equipo):
        if golesEquipoA > golesEquipoB:
            return f"El ganador es {equipo}"
        elif golesEquipoA < golesEquipoB:
            return f"El ganador es el otro equipo"
        else:
            return "Empate"


# Función para verificar y obtener una fecha válida
def obtener_fecha(prompt):
    while True:
        fecha_str = input(prompt)
        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("Fecha inválida. Por favor, use el formato YYYY-MM-DD.")


# Función para verificar y obtener un entero válido
def obtener_entero(prompt):
    while True:
        valor_str = input(prompt)
        try:
            return int(valor_str)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


# Función para verificar y obtener un float válido
def obtener_float(prompt):
    while True:
        valor_str = input(prompt)
        try:
            return float(valor_str)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal.")


# Ejemplo de interacciones de usuario
def main():
    fechaInicio = obtener_fecha("Ingrese la fecha de inicio del campeonato (YYYY-MM-DD): ")
    fechaFin = obtener_fecha("Ingrese la fecha de fin del campeonato (YYYY-MM-DD): ")
    nombreCampeonato = input("Ingrese el nombre del campeonato: ")
    premio = input("Ingrese el premio del campeonato: ")

    campeonato = Campeonato(fechaInicio, fechaFin, nombreCampeonato, premio)
    campeonato.iniciarEvento(fechaInicio)

    # Crear equipos
    equipoA_nombre = input("Ingrese el nombre del equipo A: ")
    equipoB_nombre = input("Ingrese el nombre del equipo B: ")

    equipoA = Equipo(equipoA_nombre, 0)
    equipoB = Equipo(equipoB_nombre, 0)

    # Agregar jugadores al equipo A
    num_jugadoresA = obtener_entero("Ingrese el número de jugadores del equipo A: ")
    for _ in range(num_jugadoresA):
        nombreJugador = input("Ingrese el nombre del jugador: ")
        posicion = input("Ingrese la posición del jugador: ")
        equipoA.agregarJugador(nombreJugador, posicion)

    # Agregar jugadores al equipo B
    num_jugadoresB = obtener_entero("Ingrese el número de jugadores del equipo B: ")
    for _ in range(num_jugadoresB):
        nombreJugador = input("Ingrese el nombre del jugador: ")
        posicion = input("Ingrese la posición del jugador: ")
        equipoB.agregarJugador(nombreJugador, posicion)

    campeonato.agregarEquipo(equipoA)
    campeonato.agregarEquipo(equipoB)

    # Crear un partido
    fecha_partido = obtener_fecha("Ingrese la fecha del partido (YYYY-MM-DD): ")
    horarioInicio = input("Ingrese la hora de inicio del partido (HH:MM): ")
    horaFin = input("Ingrese la hora de fin del partido (HH:MM): ")

    partido = Partido(fecha_partido, equipoA, equipoB, horarioInicio, horaFin)

    # Agregar estadísticas del partido
    golesEquipoA = obtener_entero("Ingrese los goles del equipo A: ")
    golesEquipoB = obtener_entero("Ingrese los goles del equipo B: ")
    faltasEquipoA = obtener_entero("Ingrese las faltas del equipo A: ")
    faltasEquipoB = obtener_entero("Ingrese las faltas del equipo B: ")

    partido.agregarEstadisticas(golesEquipoA, golesEquipoB, faltasEquipoA, faltasEquipoB)

    ganador = partido.decidirGanador()
    print(f"El ganador es: {ganador.carrera if ganador != 'Empate' else ganador}")


if __name__ == "__main__":
    main()