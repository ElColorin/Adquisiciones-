# sistema/carro.py

# cart.py
class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, producto):
        product_id = str(producto.id)
        if product_id not in self.carro:
            self.carro[product_id] = {
                "producto_id": producto.id,
                "nombre_producto": producto.nombre_producto,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            self.carro[product_id]["cantidad"] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        product_id = str(producto.id)
        if product_id in self.carro:
            del self.carro[product_id]
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
        return sum(item["precio"] * item["cantidad"] for item in self.carro.values())
