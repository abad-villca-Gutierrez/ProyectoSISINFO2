
import tkinter as tk
from tkinter import ttk

def iniciar_app():
    root=tk.Tk()
    root.title("Sistema de Revisión de Código")
    root.geometry("800x500")
    tk.Label(root,text="SISTEMA DE REVISIÓN DE CÓDIGO",font=("Arial",16,"bold")).pack(pady=10)
    tree=ttk.Treeview(root,columns=("titulo","estado"),show="headings")
    tree.heading("titulo",text="Título")
    tree.heading("estado",text="Estado")
    tree.pack(fill="both",expand=True,padx=10,pady=10)
    root.mainloop()
