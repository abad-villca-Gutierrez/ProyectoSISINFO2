
import json, os
from modelo.revision import Revision

class RepositorioRevision:
    def __init__(self, archivo="data/revisiones.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def guardar(self, revision):
        datos = self.listar_raw()
        datos.append({
            "titulo": revision.titulo,
            "descripcion": revision.descripcion,
            "estado": revision.estado
        })
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def actualizar(self, revisiones):
        datos = [{"titulo":r.titulo,"descripcion":r.descripcion,"estado":r.estado} for r in revisiones]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def listar_raw(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def listar(self):
        resultado = []
        for d in self.listar_raw():
            r = Revision(d["titulo"], d["descripcion"])
            r.estado = d["estado"]
            resultado.append(r)
        return resultado
