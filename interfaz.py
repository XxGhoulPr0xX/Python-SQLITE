import tkinter as tk
from tkinter import messagebox,ttk
from logica import *

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Practica")
        self.root.geometry("820x240")
        self.root.resizable(False, False)
        self.alpha = logica(self)
        self.primerInterfaz()

    def primerInterfaz(self):
        self.lblOpcion1 = tk.Label(self.root, text="1   Crear BD")
        self.lblOpcion1.grid(row=0, column=0, padx=10, pady=5)

        self.lblOpcion2 = tk.Label(self.root, text="2 Conectar BD")
        self.lblOpcion2.grid(row=1, column=0, padx=10, pady=5)

        self.txtOpcion = tk.Text(self.root, height=1, width=10)
        self.txtOpcion.grid(row=2, column=1, padx=10, pady=5)

        self.btnEnviar = tk.Button(self.root, text="Enviar", command=self.alpha.recuperarOpcion)
        self.btnEnviar.grid(row=2, column=2, pady=10)

    def crearBD(self):
        self.lblNombreBD = tk.Label(self.root, text="Ingrese el nombre de la base")
        self.lblNombreBD.grid(row=0, column=0, padx=10, pady=5)

        self.txtNombreBD = tk.Text(self.root, height=1, width=10)
        self.txtNombreBD.grid(row=1, column=1, padx=10, pady=5)

        self.btnEnviarBD = tk.Button(self.root, text="ok", command=self.alpha.creacionBD)
        self.btnEnviarBD.grid(row=2, column=1, pady=10)

    def conectarBD(self):
        self.lblCrearBD = tk.Label(self.root, text="1 Crear tabla")
        self.lblCrearBD.grid(row=0, column=0, padx=10, pady=5)

        self.lblIngresarDatos = tk.Label(self.root, text="2 Ingresar datos")
        self.lblIngresarDatos.grid(row=1, column=0, padx=10, pady=5)

        self.lblImprimirDatos = tk.Label(self.root, text="3 Imprime")
        self.lblImprimirDatos.grid(row=2, column=0, padx=10, pady=5)

        self.txtOpcionC = tk.Text(self.root, height=1, width=10)
        self.txtOpcionC.grid(row=3, column=0, rowspan=2, padx=10, pady=5)

        self.btnEnviarC = tk.Button(self.root, text="Enviar", command=self.alpha.conectarBD)
        self.btnEnviarC.grid(row=3, column=1, pady=10)

    def crearTabla(self):
        tipos_sqlite = ["TEXT", "INTEGER", "REAL"]

        # Etiqueta Base de Datos
        self.lblIngresaBD = tk.Label(self.root, text="Base de Datos:")
        self.lblIngresaBD.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaBD = tk.Text(self.root, height=1, width=30)
        self.txtIngresaBD.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta Nombre de Tabla
        self.lblIngresaTabla = tk.Label(self.root, text="Nombre de Tabla:")
        self.lblIngresaTabla.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.txtIngresaTabla = tk.Text(self.root, height=1, width=30)
        self.txtIngresaTabla.grid(row=0, column=3, padx=10, pady=5)

        # Campo 1
        self.lblIngresaC1 = tk.Label(self.root, text="Campo 1:")
        self.lblIngresaC1.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaC1 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaC1.grid(row=2, column=1, padx=10, pady=5)

        self.lblIngresaTipo1 = tk.Label(self.root, text="Tipo:")
        self.lblIngresaTipo1.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        self.cmbTipo1 = ttk.Combobox(self.root, values=tipos_sqlite, width=10, state="readonly")
        self.cmbTipo1.grid(row=2, column=3, padx=10, pady=5)

        # Campo 2
        self.lblIngresaC2 = tk.Label(self.root, text="Campo 2:")
        self.lblIngresaC2.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaC2 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaC2.grid(row=3, column=1, padx=10, pady=5)

        self.lblIngresaTipo2 = tk.Label(self.root, text="Tipo:")
        self.lblIngresaTipo2.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.cmbTipo2 = ttk.Combobox(self.root, values=tipos_sqlite, width=10, state="readonly")
        self.cmbTipo2.grid(row=3, column=3, padx=10, pady=5)

        # Campo 3
        self.lblIngresaC3 = tk.Label(self.root, text="Campo 3:")
        self.lblIngresaC3.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaC3 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaC3.grid(row=4, column=1, padx=10, pady=5)

        self.lblIngresaTipo3 = tk.Label(self.root, text="Tipo:")
        self.lblIngresaTipo3.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.cmbTipo3 = ttk.Combobox(self.root, values=tipos_sqlite, width=10, state="readonly")
        self.cmbTipo3.grid(row=4, column=3, padx=10, pady=5)

        # Campo 4
        self.lblIngresaC4 = tk.Label(self.root, text="Campo 4:")
        self.lblIngresaC4.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaC4 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaC4.grid(row=5, column=1, padx=10, pady=5)

        self.lblIngresaTipo4 = tk.Label(self.root, text="Tipo:")
        self.lblIngresaTipo4.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        self.cmbTipo4 = ttk.Combobox(self.root, values=tipos_sqlite, width=10, state="readonly")
        self.cmbTipo4.grid(row=5, column=3, padx=10, pady=5)

        # Botón Enviar
        self.btnEnviarC = tk.Button(self.root, text="Enviar", command=self.alpha.creacionDeTablas)
        self.btnEnviarC.grid(row=3, column=4)

    def ingresarDatos(self):
        # Etiqueta Base de Datos
        self.lblNombreIngresaBD = tk.Label(self.root, text="Ingresando datos:")
        self.lblNombreIngresaBD.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.txtNombreIngresoBD = tk.Text(self.root, height=1, width=30)
        self.txtNombreIngresoBD.grid(row=0, column=1, padx=10, pady=5)

        self.btnEnviarC = tk.Button(self.root, text="Agregar", command=self.alpha.insertarDatos)
        self.btnEnviarC.grid(row=0, column=2)
        # Campo 1
        self.lblIngresaDatosC1 = tk.Label(self.root, text="Campo 1:")
        self.lblIngresaDatosC1.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosC1 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosC1.grid(row=2, column=1, padx=10, pady=5)

        self.lblIngresaDatosTipo1 = tk.Label(self.root, text="Valor:")
        self.lblIngresaDatosTipo1.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosTipo1 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosTipo1.grid(row=2, column=3, padx=10, pady=5)

        # Campo 2
        self.lblIngresaDatosC2 = tk.Label(self.root, text="Campo 2:")
        self.lblIngresaDatosC2.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosC2 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosC2.grid(row=3, column=1, padx=10, pady=5)

        self.lblIngresaDatosTipo2 = tk.Label(self.root, text="Valor:")
        self.lblIngresaDatosTipo2.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosTipo2 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosTipo2.grid(row=3, column=3, padx=10, pady=5)

        # Campo 3
        self.lblIngresaDatosC3 = tk.Label(self.root, text="Campo 3:")
        self.lblIngresaDatosC3.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosC3 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosC3.grid(row=4, column=1, padx=10, pady=5)

        self.lblIngresaDatosTipo3 = tk.Label(self.root, text="Valor:")
        self.lblIngresaDatosTipo3.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosTipo3 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosTipo3.grid(row=4, column=3, padx=10, pady=5)

        # Campo 4
        self.lblIngresaDatosC4 = tk.Label(self.root, text="Campo 4:")
        self.lblIngresaDatosC4.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosC4 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosC4.grid(row=5, column=1, padx=10, pady=5)

        self.lblIngresaDatosTipo4 = tk.Label(self.root, text="Valor:")
        self.lblIngresaDatosTipo4.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        self.txtIngresaDatosTipo4 = tk.Text(self.root, height=1, width=30)
        self.txtIngresaDatosTipo4.grid(row=5, column=3, padx=10, pady=5)

        # Botón Enviar
        self.btnEnviarC1 = tk.Button(self.root, text="Enviar", command=self.alpha.getDatosYenviarlos)
        self.btnEnviarC1.grid(row=3, column=4)

    def imprimirDatos(self):
        self.lblImprime = tk.Label(self.root, text="Imprime")
        self.lblImprime.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.lblEleccion = tk.Label(self.root, text="Elige el nombre de la base y \nsu tabla por separado por una coma:")
        self.lblEleccion.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.txtEleccion = tk.Text(self.root, height=1, width=30)
        self.txtEleccion.grid(row=2, column=0, padx=10, pady=5)

        self.btnEnviarC2 = tk.Button(self.root, text="Enviar", command=self.alpha.consulta)
        self.btnEnviarC2.grid(row=2, column=1)

    def imprimirDatos2(self):
        self.btnEnviarCi1 = tk.Button(self.root, text="ok", command=self.alpha.destruir)
        self.btnEnviarCi1.grid(row=1, column=1)

        self.txtResultadosCi1 = tk.Text(self.root, height=10, width=10)
        self.txtResultadosCi1.grid(row=0, column=0, padx=10, pady=5)