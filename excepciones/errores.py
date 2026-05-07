# Clase de excepción personalizada para errores relacionados con clientes
# Hereda de la clase Exception de Python
class ClienteError(Exception):

    # pass indica que la clase no tiene contenido adicional
    # pero permite crear errores específicos para clientes
    pass


# Clase de excepción personalizada para errores relacionados con servicios
class ServicioError(Exception):

    # Se utiliza para manejar errores específicos de servicios
    pass


# Clase de excepción personalizada para errores relacionados con reservas
class ReservaError(Exception):

    # Permite identificar errores específicos en reservas
    pass