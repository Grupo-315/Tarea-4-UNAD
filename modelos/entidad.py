# Importa ABC y abstractmethod del módulo abc
# ABC permite crear clases abstractas
# abstractmethod obliga a que ciertos métodos sean implementados en las clases hijas
from abc import ABC, abstractmethod


# Se crea la clase abstracta Entidad
# Hereda de ABC para indicar que es una clase abstracta
class Entidad(ABC):

    # Método constructor
    # Se ejecuta automáticamente al crear un objeto
    def __init__(self, id):

        # Guarda el id en un atributo protegido
        self._id = id

    # Decorador que convierte el método en abstracto
    # Obliga a las clases hijas a implementar este método
    @abstractmethod
    def mostrar_info(self):

        # pass significa que el método queda vacío por ahora
        # porque será definido en las clases que hereden de Entidad
        pass