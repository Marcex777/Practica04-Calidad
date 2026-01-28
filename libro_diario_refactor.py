"""
Módulo de Libro Diario (refactorizado).

Objetivo: mejorar calidad de código aplicando PEP8, docstrings,
validaciones y separación entre lógica y presentación.
"""


class LibroDiario:
    """Clase para registrar transacciones y calcular resumen contable."""

    def __init__(self) -> None:
        """Inicializa el libro diario con lista vacía de transacciones."""
        self.transacciones: list[dict] = []

    def agregar(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """
        Agrega una transacción al libro con validaciones básicas.

        Args:
            fecha: Fecha de la transacción.
            descripcion: Descripción de la transacción.
            monto: Monto de la transacción (debe ser > 0).
            tipo: "ingreso" o "egreso".

        Raises:
            ValueError: si tipo es inválido, monto no es positivo o descripción vacía.
        """
        descripcion = (descripcion or "").strip()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        try:
            monto = float(monto)
        except (TypeError, ValueError) as exc:
            raise ValueError("El monto debe ser numérico.") from exc

        if monto <= 0:
            raise ValueError("El monto debe ser mayor que 0.")

        tipo = (tipo or "").strip().lower()
        if tipo not in ("ingreso", "egreso"):
            raise ValueError("El tipo debe ser 'ingreso' o 'egreso'.")

        self.transacciones.append(
            {
                "fecha": fecha,
                "descripcion": descripcion,
                "monto": monto,
                "tipo": tipo,
            }
        )

    def resumen(self) -> dict:
        """
        Calcula y retorna el resumen numérico del libro.

        Returns:
            Diccionario con total_ingresos, total_egresos y balance.
        """
        ingresos = 0.0
        egresos = 0.0

        for t in self.transacciones:
            if t["tipo"] == "ingreso":
                ingresos += t["monto"]
            else:
                egresos += t["monto"]

        return {
            "total_ingresos": ingresos,
            "total_egresos": egresos,
            "balance": ingresos - egresos,
        }

    def resumen_texto(self) -> str:
        """Devuelve el resumen formateado como texto para imprimir."""
        r = self.resumen()
        return (
            f"Total ingresos: {r['total_ingresos']} | "
            f"Total egresos: {r['total_egresos']} | "
            f"Balance: {r['balance']}"
        )
