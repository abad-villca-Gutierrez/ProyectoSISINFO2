
class Revision:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "Pendiente"

    def aprobar(self):
        if self.estado != "Pendiente":
            raise ValueError("La revisión ya fue procesada")
        self.estado = "Aprobada"

    def rechazar(self):
        if self.estado != "Pendiente":
            raise ValueError("La revisión ya fue procesada")
        self.estado = "Rechazada"
