from abc import ABC, abstractmethod
# Clase que define la estructura base para todos los servicios del sistema 
class Servicio(ABC):
    def __init__(self, nombre, tarifa):
        # Inicializacion de atributos: nombre del servicio y el costo base 
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        # Metodo para retornar el detalle especifico de cada tipo de servicio 
        pass

# Clase que implementa el servicio especifico de reserva de salones 
 
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        # El costo se calcula multiplicando la tarifa horaria por el tiempo usado 
        return self.tarifa * horas

    def descripcion(self):
        return f"Sala: {self.nombre}"

# Clase para la gestion de alquiler de equipos tecnologicos o materiales  

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        # Calculo basado en la tarifa diaria por la cantidad de dias de alquiler 
        return self.tarifa * dias

    def descripcion(self):
        # Retorna el nombre del equipo alquilado 
        return f"Equipo: {self.nombre}"

# Clase para asesorias del servicio 

class Asesoria(Servicio):
    
    # Calcula el costo segun el tiempo del servicio 
    
    def calcular_costo(self, horas):
        return self.tarifa * horas

# Devuelve la descripcion del servicio 

    def descripcion(self):
        return f"Asesoría: {self.nombre}"
