class Precio:
    def __init__(self, monto, moneda, descuento=0.0):
        self._monto = monto
        self._moneda = moneda
        self._descuento = descuento

    def get_monto(self):
        return self._monto

    def set_monto(self, monto):
        self._monto = monto

    def calcular_precio_final(self):
        return self._monto * (1 - self._descuento)
