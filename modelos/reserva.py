from excepciones.errores import ReservaError
from utils.logger import registrar_log
# Modulo que gestiona la logica de las reservas del sistema 

# Definicion de la clase reserva para el manejo de atributos como clientes y duracion 

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaError("Duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        
# Metodo encargado de calcular el costo total del servicio basandose en la duracion establecida 

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo(self.duracion)
        except Exception as e:
            registrar_log(f"Error cálculo: {e}")
            raise ReservaError("Error al calcular") from e

# Metodo para validar y confirmar una reserva pendiente  

    def confirmar(self):
        try:
            # Verifica que la reserva no haya sido procesada previamente 
            if self.estado != "pendiente":
                raise ReservaError("La reserva ya fue procesada")
                
            # Actualiza el estado a confirmada y registra el evento en el log
            self.estado = "confirmada"
            registrar_log("Reserva confirmada")

        except Exception as e:
            # Captura errores inesperados durante la confirmacion y los registra 
            registrar_log(f"Error confirmar: {e}")
            print("❌ Error:", e)

# Cancela la reserva existente en el sistema

    def cancelar(self):
        try:
            # Cambia el estado actual a cancelada 
            self.estado = "cancelada"
            # Notifica la cancelacion en el archivo de registro 
            registrar_log("Reserva cancelada")
        except Exception as e:
            registrar_log(f"Error cancelar: {e}")
