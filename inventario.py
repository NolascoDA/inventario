nombre = input("¿Cómo te llamas? ")
print(f"Bienvenid@ a nuestro stock, {nombre}!")
print("Por favor, elige una opción:")
print("1 - Agregar un producto")
print("2 - Modificar un producto")
print("3 - Actualizar un producto")
print("4 - Eliminar un producto")
print("5 - Mostrar el stock completo")


# Pedir al usuario que elija una opción
opcion = input("Ingresa el número de la opción (1-5): ")

# Validar que la opción esté dentro del rango de opciones disponibles
while opcion not in ['1', '2', '3', '4', '5']:
    print("Por favor, elige un número entre 1 y 5.")
    opcion = input("Por favor, elige una opción (1-5): ")

if opcion == '1':
    print("Vamos a agregar un producto")
elif opcion == '2':
    print("Vamos a modificar un producto de nuestro stock")
elif opcion == '3':
    print("Vamos a actualizar un producto de nuestro stock")
elif opcion == '4':
    print("Vamos a eliminar un producto de nuestro stock")
elif opcion == '5':
    print("Aquí tienes todo nuestro stock: " + "{mostrar_productos()}")


class Producto:
    def __init__(self, n_serie, nombre, categoria, precio, cantidad):
        self.n_serie = n_serie
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"ID: {self.n_serie}, Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar productos por ID
    
    def agregar_producto(self, producto):
        if producto.n_serie in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[producto.n_serie] = producto
            print(f"Producto '{producto.nombre}' agregado con éxito.")
    
    def actualizar_producto(self, n_serie, nuevo_nombre=None, nuevo_precio=None, nueva_cantidad=None):
        if n_serie in self.productos:
            producto = self.productos[n_serie]
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nuevo_precio:
                producto.precio = nuevo_precio
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            print(f"Producto '{producto.nombre}' actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")
    
    def eliminar_producto(self, n_serie):
        if n_serie in self.productos:
            del self.productos[n_serie]
            print(f"Producto con ID {n_serie} eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")
    
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

