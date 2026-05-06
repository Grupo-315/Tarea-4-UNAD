# Importamos ABC (Abstract Base Class) y abstractmethod
# Esto nos permite crear clases abstractas en Python
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    No se puede instanciar directamente, solo sirve como base.
    """

    def __init__(self, id):
        """
        Constructor de la clase Entidad

        Parámetros:
        id (int): Identificador único de la entidad
        """
        # Atributo protegido (encapsulación)
        self._id = id

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto obligatorio.

        Todas las clases que hereden de Entidad deben implementar
        este método para mostrar su información.
        """
        pass