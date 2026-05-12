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


def crear_servicio():                # Se define la funcion crear_servcio().
    try:                             # Todo lo que esté aqui dentro se ejecuta normalmente, si ocurre un error pasa al bloque except
        print("1. Sala")             # Le muestra al usuario un menu con tres tipos de servicios disponibles.
        print("2. Equipo")
        print("3. Asesoría")
                                     # Se le piden datos al usuario.
        tipo = input("Seleccione: ") # Opcion a elegir.
        nombre = input("Nombre: ")   # Nombre del servicio.
        tarifa = float(input("Tarifa: ")) # Precio del servicio y float() convierte el valor ingresado a numero decimal.

        if tipo == "1":                               # Crea el objeto segun el tipo. 1 objeto de la clase ReservaSala.
            servicio = ReservaSala(nombre, tarifa)
        elif tipo == "2":                             # Objeto de tipo AlquilerEquipo.
            servicio = AlquilerEquipo(nombre, tarifa)
        elif tipo == "3":                             # Objeto de tipo Asesoria.
            servicio = Asesoria(nombre, tarifa)
        else:                                         # Manejo de opcion invalida, cuando el usuario escribe otra cosa, genera error manualmente.
            raise ValueError("Tipo inválido")

        servicios.append(servicio)                    # Agrega el objeto creado a una lista llamada servicios.
        print("✅ Servicio creado")                   # Se muestra la confirmacion.
                                                      # Captura cualquier error ocurrido en el try
    except Exception as e:                            # La variable e guarda el error.
        print("❌ Error:", e)                         # Muestra el error.
        registrar_log(e)                              # Registra el error en un archivo logs.


def crear_reserva():                                  # Se define la funcion crear_reserva()
    try:                                              # Captura errores y evita que el programa se cierre de manera abrupta.
        if not clientes or not servicios:             # Comprueba si las listas clientes o servicios estan vacias.
            print("❌ Debes registrar clientes y servicios primero")  # Muestra un mensaje de error y sale de la funcion usando return.
            return

        print("\nClientes:")                          # Imprime el titulo Clientes.
        for i, c in enumerate(clientes):              # Recorre la lista clientes.
            print(i, "-", c.mostrar_info())           # Muestra cada cliente.

        c_index = int(input("Seleccione cliente: "))  # Pide al usurio escribir el numero del cliente
        cliente = clientes[c_index]                   # Obtiene el cliente seleccionado usando el indice.

        print("\nServicios:")                         # Imprime el titulo servicios
        for i, s in enumerate(servicios):             # Recorre la lista de servicios.
            print(i, "-", s.descripcion())            # Muestra la descripcion del servcio.

        s_index = int(input("Seleccione servicio: ")) # Pide elegir un servicio.
        servicio = servicios[s_index]                 # Guarda el servicio seleccionado.

        duracion = float(input("Duración: "))         # Solicita la duracion del servicio.

        reserva = Reserva(cliente, servicio, duracion)# Crea un objeto Reserva, usando cliente, servicio, duracion.
        reservas.append(reserva)                      # Guarda la reserva en la lista reservas.

        print("💰 Total:", reserva.calcular_total())  # Llama al metodo calcular_total(), para calcular el precio.
        reserva.confirmar()                           # Ejecuta el metodo confirmar() de la reserva.

    except (ValueError, IndexError):                  # Captura ValueError, si el ususario escribe texto en vez de numeros.
        print("❌ Selección inválida")               # Muestra mensaje de error.
    except ReservaError as e:                         # Captura un error personalizado llamado ReservaError. guarda el error en la variable e.
        print("❌ Error:", e)                        # Muestra el mensaje de error
        registrar_log(e)                              # Guarda el error en un archivo de registro.


def ver_reservas():              # Define la funcion ver_reservas, para mostrar todas las reservas registradas.
    if not reservas:             # Comprueba si la lista reservas esta vacia.
        print("No hay reservas") # Si no hay reservas muestra el mensaje "no hay reservas"
        return                   # Termina la funcion usando return.

    for r in reservas:           # Recorre cada elemento de la lista reservas.
        print(f"{r.cliente.mostrar_info()} | {r.servicio.descripcion()} | {r.estado}") # Imprime informacion de la reserva usando un f-string


def main():                       # Define la funcion principal del programa; se controla el menu y las acciones del usuario.
    while True:                   # Crea un ciclo infinito para que el menu aparezca continuamente hasta que el usuario decida salir.
        mostrar_menu()            # Llama a un funcion para imprimir un menu.
        opcion = input("Opción: ") # Solicita al usuario elegir una opcion.

        if opcion == "1":          # Se ejecuta la funcion registrar_cliente(), si el usuario escribe "1".
            registrar_cliente()
        elif opcion == "2":        # Ejecuta la funcion para crear servicios.
            crear_servicio()
        elif opcion == "3":        # Llama a la funcion que crea reservas.
            crear_reserva()
        elif opcion == "4":        # Muestra todas las reservas registradas.
            ver_reservas()
        elif opcion == "5":        # Imprime saliendo..., 
            print("Saliendo...")
            break                  # break termina el ciclco while, el programa finaliza.
        else:
            print("❌ Opción inválida") # Si el usuario escribe una opcion diferente, muestra un mensaje de error.


if __name__ == "__main__":   # Verifica si el archivo se esta ejecutando directamente.
    main()                   # Llama a la funcion principal e inicia el sistema.