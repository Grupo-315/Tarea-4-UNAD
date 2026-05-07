from modelos.cliente import Cliente # De la carpeta llamada modelos busca el archivo cliente.py e importa la clase o elemento llamado Cliente.
from modelos.servicio import ReservaSala, AlquilerEquipo, Asesoria # Se importan tres clases desde el archivo servicio.py
from modelos.reserva import Reserva # Se importa la clase Reserva desde el archivo reserva.py
from excepciones.errores import ClienteError, ReservaError # Se importan excepciones personlizadas
from utils.logger import registrar_log # Se importa la funcion registrar_log desde logger.py

clientes = [] # clientes es una variable y aqui representa una lista vacia, que se usara para guardar clientes
servicios = [] # Se crea una lista vacia para almacenar servicios
reservas = [] # Aqui se crea una lista donde se guardaran las reservas realizadas


def mostrar_menu():                    # Se define una funcion llamada mostrar_menu(), imprime un menu en pantalla. 
    print("\n===== SOFTWARE FJ =====") # El usuario ve las opciones disponibles del programa.
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")


def registrar_cliente(): # Definimos la funcion registrar_cliene.
    try:                 # Se intenta ejecutar un bloque de codigo se maneja errores sin que el programa se cierre.
        nombre = input("Nombre: ") # Pedimos datos al usuario por teclado.
        email = input("Email: ")   # Lo que el usuario escribe se guarda en las variables (nombre, email)

        cliente = Cliente(len(clientes)+1, nombre, email) # Se crea un objeto de tipo Cliente, (len) cuanta cuantos clientes hay en una lista.
        clientes.append(cliente)                          # +1 genera un nuevo ID, (append) agrega el nuevo cliente a la lista clientes.

        print("✅ Cliente registrado")                   # Se muestra un mensaje indicando que todo salio bien.

    except ClienteError as e:         # Si ocurre un error de tipo ClienteError, el programa entra aqui y guarda el error en la variable e.
        print("❌ Error:", e)        # Muestra el error en pantalla
        registrar_log(e)             # Guarda el error en un archivo de registro