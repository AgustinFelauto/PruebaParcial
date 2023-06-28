from datetime import date

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

class Mercado:
    def __init__(self):
        self.pasillos = [[] for _ in range(5)]  

    def agregar_producto(self, producto, pasillo):
        self.pasillos[pasillo].append(producto)

    def remover_producto(self, producto, pasillo):
        self.pasillos[pasillo].remove(producto)

    def calcular_expirados(self):
        expirados = []
        today = date.today()
        for pasillo in self.pasillos:
            for producto in pasillo:
                if (producto.fecha_exp - today).days <= 1:
                    expirados.append(producto)
        for producto in expirados:
            self.remover_producto(producto, self.pasillos.index(pasillo))

    def imprimir_stock(self):
        for i, pasillo in enumerate(self.pasillos):
            print(f"Pasillo {i+1}:")
            for producto in pasillo:
                print(f"ID: {producto.id} - Descripción: {producto.descripcion} - Fecha de expiración: {producto.fecha_exp}")