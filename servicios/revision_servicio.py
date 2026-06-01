
from modelo.revision import Revision

class RevisionServicio:
    def __init__(self, repositorio):
        self.repo = repositorio

    def registrar_revision(self, titulo, descripcion):
        if not titulo.strip():
            raise ValueError("Título vacío")
        if not descripcion.strip():
            raise ValueError("Descripción vacía")
        revision = Revision(titulo, descripcion)
        self.repo.guardar(revision)

    def obtener_revisiones(self):
        return self.repo.listar()

    def aprobar_revision(self, indice):
        revisiones = self.repo.listar()
        revisiones[indice].aprobar()
        self.repo.actualizar(revisiones)

    def rechazar_revision(self, indice):
        revisiones = self.repo.listar()
        revisiones[indice].rechazar()
        self.repo.actualizar(revisiones)
