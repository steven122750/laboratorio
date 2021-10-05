import os
from _ast import In
from itertools import product

from Dominio.Admin import Admin
from Dominio.Inventario import Inventario
from Dominio.Producto import Producto
from Dominio.Usuario import Usuario
from Infraestructura.PersistenciaProducto import PersistenciaProducto

if __name__ == '__main__':
    saver = PersistenciaProducto()
    saver.connect()

    x = True



    print("################ Bienvenido ################")
    while x:
        print("1 --> Ingresar como usuario")
        print("2 --> Ingresar como Administrador")
        opcionP=int(input("Ingresa una opcion: "))

        if opcionP == 1:
            print("Ingresaste como usuario")
            print("1 --> Comprar un producto")
            print("2 --> Buscar producto")
            print("3 --> Sair")

            opcionU = int(input("Ingresa una opcion: "))

            if opcionU == 1:
                print("Productos disponibles")
                print("Lista --> ")
            elif opcionU == 2:
                print("1 --> Buscar por nombre")
                print("2 --> Buscar por id")
                print("3 --> Sair")

                opcionBuscar=int(input("Ingresa una opcion: "))
                if opcionBuscar == 1:
                    pass
                elif opcionBuscar == 2:
                    pass
                elif opcionBuscar == 3:
                    x = False
            elif opcionU == 3:
                x = False

        elif opcionP == 2:
            pin = int(input("Ingresa el pin de administrador"))
            admin = Admin(0000)
            if pin == admin.pin:
                print("Has ingresado")
                print("1 --> Registrar producto")
                print("2 --> Editar precio del producto")
                opcionA = int(input("Ingresa la opcion: "))

                if opcionA == 1:
                    id = input("Id: ")
                    nombre = input("Nombre: ")
                    precio = float(input("Precio"))

                    producto = Producto(precio,nombre,id)
                    PersistenciaProducto.save(producto)
                    PersistenciaProducto.save_json(producto)
                    inventario = Inventario()
                    inventario_json=Inventario()

                    print("Producto guardado en el inventario")





                elif opcionA == 2:
                    inventario = Inventario()
                    inventario_json=Inventario()

                    for file in os.listdir("./files"):
                        if '.gui' in file:
                            inventario.agregar_producto(PersistenciaProducto.load(file))
                        if '.json' in file:
                            inventario_json.agregar_producto(PersistenciaProducto.load_json(file))
                    cambiar = float(input("Nuevo precio --> "))
                    for p in inventario.productos:
                        p.cambiarPrecio(cambiar)
                        PersistenciaProducto.save(p)
                        PersistenciaProducto.save_json(p)

            else:
                print("Datos incorrectos")
                salir = True

        elif opcionP == 3:
            x = False






