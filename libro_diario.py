class LibroDiario:

    def __init__(self):
      self.transacciones = []

    def agregar(self,fecha, descripcion,monto,tipo):
     self.transacciones.append({
      "fecha": fecha,
        "descripcion": descripcion,
      "monto": monto,
        "tipo": tipo
      })

    def resumen(self):
     ingresos=0
     egresos=0
     for t in self.transacciones:
      if t["tipo"]=="ingreso":
        ingresos+=t["monto"]
      else:
        egresos+=t["monto"]
     return "Total ingresos: " + str(ingresos) + " Total egresos: " + str(egresos)
