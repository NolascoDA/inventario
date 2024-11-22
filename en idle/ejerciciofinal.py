Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Producto:
...     def __init__(self, n_serie, nombre, categoria, precio, cantidad):
...         self.n_serie = n_serie
...         self.nombre = nombre
...         self.categoria = categoria
...         self.precio = precio
...         self.cantidad = cantidad
...     
...     def __str__(self):
...         return f"ID: {self.n_serie}, Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"
... 
... class Inventario:
...     def __init__(self):
...         self.productos = {}  # Usamos un diccionario para almacenar productos por ID
...     
...     def agregar_producto(self, producto):
...         if producto.n_serie in self.productos:
...             print("Error: El producto ya existe en el inventario.")
...         else:
...             self.productos[producto.n_serie] = producto
...             print(f"Producto '{producto.nombre}' agregado con éxito.")
...     
...     def actualizar_producto(self, n_serie, nuevo_nombre=None, nuevo_precio=None, nueva_cantidad=None):
...         if n_serie in self.productos:
...             producto = self.productos[n_serie]
...             if nuevo_nombre:
...                 producto.nombre = nuevo_nombre
...             if nuevo_precio:
...                 producto.precio = nuevo_precio
...             if nueva_cantidad is not None:
...                 producto.cantidad = nueva_cantidad
...             print(f"Producto '{producto.nombre}' actualizado con éxito.")
...         else:
...             print("Error: Producto no encontrado.")
...     
...     def eliminar_producto(self, n_serie):
...         if n_serie in self.productos:
...             del self.productos[n_serie]
...             print(f"Producto con ID {n_serie} eliminado con éxito.")
...         else:
            print("Error: Producto no encontrado.")
    
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Ejemplo de uso:
if __name__ == "__main__":
    inventario = Inventario()
    
    # Agregar productos
    producto1 = Producto(1, "Laptop", 1200.50, 10)
    producto2 = Producto(2, "Smartphone", 800.75, 15)
    
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    
    # Mostrar productos
    print("\nInventario actual:")
    inventario.mostrar_productos()
    
    # Actualizar producto
    inventario.actualizar_producto(1, nuevo_precio=1100.00, nueva_cantidad=12)
    
    # Eliminar un producto
    inventario.eliminar_producto(2)
    
    # Mostrar productos después de las modificaciones
    print("\nInventario después de modificaciones:")
    inventario.mostrar_productos()
[DEBUG ON]
[DEBUG OFF]
