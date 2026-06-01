
import tkinter as tk
from tkinter import messagebox
from persistencia.repositorio_revision import RepositorioRevision
from servicios.revision_servicio import RevisionServicio

repo = RepositorioRevision()
servicio = RevisionServicio(repo)

root = tk.Tk()
root.title("Gestión de Revisiones")

tk.Label(root,text="Título").pack()
titulo = tk.Entry(root,width=40)
titulo.pack()

tk.Label(root,text="Descripción").pack()
descripcion = tk.Entry(root,width=40)
descripcion.pack()

lista = tk.Listbox(root,width=60)
lista.pack()

def cargar():
    lista.delete(0, tk.END)
    for r in servicio.obtener_revisiones():
        lista.insert(tk.END, f"{r.titulo} - {r.estado}")

def registrar():
    try:
        servicio.registrar_revision(titulo.get(), descripcion.get())
        titulo.delete(0, tk.END)
        descripcion.delete(0, tk.END)
        cargar()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def aprobar():
    if lista.curselection():
        try:
            servicio.aprobar_revision(lista.curselection()[0])
            cargar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def rechazar():
    if lista.curselection():
        try:
            servicio.rechazar_revision(lista.curselection()[0])
            cargar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

tk.Button(root,text="Registrar",command=registrar).pack()
tk.Button(root,text="Aprobar",command=aprobar).pack()
tk.Button(root,text="Rechazar",command=rechazar).pack()

cargar()
root.mainloop()
