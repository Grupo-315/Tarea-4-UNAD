# Importamos la clase base Entidad
from modelos.entidad import Entidad

# Importamos la excepción personalizada
from excepciones.errores import ClienteError


class Cliente(Entidad):
    """
    Clase que representa un cliente del sistema.
    Hereda de Entidad (aplicando herencia).
    """

    def __init__(self, id, nombre, email):
        """
        Constructor de la clase Cliente

        Parámetros:
        id (int): Identificador del cliente
        nombre (str): Nombre del cliente
        email (str): Correo electrónico del cliente
        """

        # Llamamos al constructor de la clase padre (Entidad)
        super().__init__(id)

        # =========================
        # VALIDACIONES (ROBUSTEZ)
        # =========================

        # Validamos que el nombre no esté vacío
        if not nombre or nombre.strip() == "":
            # Lanzamos una excepción personalizada
            raise ClienteError("El nombre no puede estar vacío")

        # Validamos que el email tenga formato básico
        if "@" not in email or "." not in email:
            raise ClienteError("El correo electrónico no es válido")

        # =========================
        # ENCAPSULACIÓN
        # =========================

        # Atributos privados (convención con _)
        self._nombre = nombre
        self._email = email

    # =========================
    # MÉTODO PARA MOSTRAR INFO
    # =========================
    def mostrar_info(self):
        """
        Retorna la información del cliente en formato texto.

        Este método sobrescribe el método abstracto de la clase Entidad.
        """
        return f"Cliente: {self._nombre} | Email: {self._email}"

    # =========================
    # GETTERS (ENCAPSULACIÓN)
    # =========================
    def get_nombre(self):
        """
        Retorna el nombre del cliente
        """
        return self._nombre

    def get_email(self):
        """
        Retorna el email del cliente
        """
        return self._email

    # =========================
    # SETTERS (VALIDACIONES)
    # =========================
    def set_nombre(self, nuevo_nombre):
        """
        Permite modificar el nombre del cliente con validación
        """
        if not nuevo_nombre:
            raise ClienteError("El nombre no puede estar vacío")
        self._nombre = nuevo_nombre

    def set_email(self, nuevo_email):
        """
        Permite modificar el email con validación
        """
        if "@" not in nuevo_email:
            raise ClienteError("Correo inválido")
        self._email = nuevo_email