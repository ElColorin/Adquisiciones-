# sistema/carro.py

# cart.py
class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro

    def agregar(self, producto):
        product_id = str(producto['id_producto'])  # Cambiar 'id' a 'id_producto'
        precio = float(producto['precio_producto'])  # Asegurarse de que el precio sea un número
        if product_id not in self.carro:
            self.carro[product_id] = {
                'producto_id': producto['id_producto'],  # Cambiar 'id' a 'id_producto'
                'nombre': producto['nombre_producto'],
                'precio': precio,  # Asegurarse de que el precio sea un número
                'cantidad': 1,
                'imagen': producto['imagen_producto']
            }
        else:
            self.carro[product_id]['cantidad'] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id_producto)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carro()

    def restar(self, producto):
        product_id = str(producto.id)
        if product_id in self.carro:
            self.carro[product_id]["cantidad"] -= 1
            if self.carro[product_id]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

    def importe_total_carro(self):
        total = 0.0
        for item in self.carro.values():
            total += float(item['precio']) * item['cantidad']
        print(total)
        return total

    def cantidad_total_productos(self):
        return sum(item["cantidad"] for item in self.carro.values())
  
