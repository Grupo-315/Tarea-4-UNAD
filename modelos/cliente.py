# Importa la clase Entidad desde el archivo entidad.py
# Esta será la clase padre de Cliente
from modelos.entidad import Entidad

# Importa la excepción personalizada ClienteError
# Se usa para mostrar errores relacionados con clientes
from excepciones.errores import ClienteError


# Se crea la clase Cliente heredando de Entidad
class Cliente(Entidad):

    # Método constructor de la clase
    # Se ejecuta automáticamente al crear un objeto Cliente
    def __init__(self, id, nombre, email):

        # Llama al constructor de la clase padre Entidad
        # para inicializar el atributo id
        super().__init__(id)

        # Llama al método set_nombre para validar y guardar el nombre
        self.set_nombre(nombre)

        # Llama al método set_email para validar y guardar el email
        self.set_email(email)

    # Método para asignar el nombre del cliente
    def set_nombre(self, nombre):

        # Verifica que el nombre no esté vacío
        # strip() elimina espacios en blanco al inicio y final
        if not nombre.strip():

            # Si el nombre es inválido, lanza un error personalizado
            raise ClienteError("Nombre inválido")

        # Guarda el nombre en el atributo protegido _nombre
        self._nombre = nombre

    # Método para asignar el email del cliente
    def set_email(self, email):

        # Verifica que el correo contenga el símbolo @
        if "@" not in email:

            # Si el email es inválido, lanza un error personalizado
            raise ClienteError("Email inválido")

        # Guarda el email en el atributo protegido _email
        self._email = email

    # Método que retorna la información del cliente en texto
    def mostrar_info(self):

        # Devuelve el nombre y correo en formato de cadena
        return f"{self._nombre} - {self._email}"