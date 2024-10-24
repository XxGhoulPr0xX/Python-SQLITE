from conexion import *
import tkinter as tk
from tkinter import simpledialog, messagebox


class logica:
    def __init__(self,interfaz):
        self.beta=interfaz
        self.charlie=BD()
        self.sesionActual=""

    def recuperarOpcion(self):
        opcion=self.beta.txtOpcion.get("1.0", tk.END).strip()
        if opcion == "1":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.crearBD()
        elif opcion=="2":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.conectarBD()
        else:
            messagebox.showwarning("Advertencia", "No es una opción valida")

    def creacionBD(self):
        nombreBaseDatos=self.beta.txtNombreBD.get("1.0", tk.END).strip()
        self.charlie.conectarBD(nombreBaseDatos)
        for widget in self.beta.root.winfo_children():
            widget.destroy()
        self.beta.primerInterfaz()

    def conectarBD(self):
        opcion=self.beta.txtOpcionC.get("1.0", tk.END).strip()
        if opcion == "1":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.crearTabla()
        elif opcion=="2":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
                self.beta.ingresarDatos()
        elif opcion=="3":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.imprimirDatos()
        elif opcion=="0":
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.primerInterfaz()
        else:
            messagebox.showwarning("Advertencia", "No es una opción valida")

    def creacionDeTablas(self):
        nombreBaseDatos = self.beta.txtIngresaBD.get("1.0", tk.END).strip()
        nombreDeTabla= self.beta.txtIngresaTabla.get("1.0", tk.END).strip()
        campo1 = self.beta.txtIngresaC1.get("1.0", tk.END).strip()
        valor1 = self.beta.cmbTipo1.get().strip()
        campo2 = self.beta.txtIngresaC2.get("1.0", tk.END).strip()
        valor2 = self.beta.cmbTipo2.get().strip()
        campo3 = self.beta.txtIngresaC3.get("1.0", tk.END).strip()
        valor3 = self.beta.cmbTipo3.get().strip()
        campo4 = self.beta.txtIngresaC4.get("1.0", tk.END).strip()
        valor4 = self.beta.cmbTipo4.get().strip()
        campos_y_valores = {
            campo1: valor1,
            campo2: valor2,
            campo3: valor3,
            campo4: valor4,
        }
        campos = [campo1, campo2, campo3, campo4]
        campos_filtrados = [campo for campo in campos if campo]
        if len(set(campos_filtrados)) != len(campos_filtrados):
            messagebox.showwarning("Error: Hay campos duplicados", "Por favor, ingresa nombres de campo únicos.")
        else:
            self.sesionActual=nombreBaseDatos
            self.charlie.conectarBD(self.sesionActual)
            self.charlie.creaBD(nombreDeTabla, campos_y_valores)
            self.charlie.cerrarConexion()
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.conectarBD()

    def insertarDatos(self):
        nombreTabla = self.beta.txtNombreIngresoBD.get("1.0", tk.END).strip()
        self.charlie.conectarBD(self.sesionActual)
        columnas = self.charlie.obtenerNombresColumnas(nombreTabla)
        self.charlie.cerrarConexion()
        if columnas:
            if len(columnas) > 0:
                self.beta.txtIngresaDatosC1.delete("1.0", tk.END)
                self.beta.txtIngresaDatosC1.insert(tk.END, columnas[0])
            if len(columnas) > 1:
                self.beta.txtIngresaDatosC2.delete("1.0", tk.END)
                self.beta.txtIngresaDatosC2.insert(tk.END, columnas[1])
            if len(columnas) > 2:
                self.beta.txtIngresaDatosC3.delete("1.0", tk.END)
                self.beta.txtIngresaDatosC3.insert(tk.END, columnas[2])
            if len(columnas) > 3:
                self.beta.txtIngresaDatosC4.delete("1.0", tk.END)
                self.beta.txtIngresaDatosC4.insert(tk.END, columnas[3])
        else:
            messagebox.showwarning("Error", "No se encontraron columnas en la tabla especificada.")


    def getDatosYenviarlos(self):
            nombreTabla = self.beta.txtNombreIngresoBD.get("1.0", tk.END).strip()
            valor1 = self.beta.txtIngresaDatosTipo1.get("1.0", tk.END).strip()
            valor2 = self.beta.txtIngresaDatosTipo2.get("1.0", tk.END).strip()
            valor3 = self.beta.txtIngresaDatosTipo3.get("1.0", tk.END).strip()
            valor4 = self.beta.txtIngresaDatosTipo4.get("1.0", tk.END).strip()
            valor=[valor1,valor2,valor3,valor4]
            self.charlie.conectarBD(self.sesionActual)
            columnas = self.charlie.obtenerNombresColumnas(nombreTabla)
            tipos_columnas = self.charlie.obtenerTipoColumnas(nombreTabla)
            valores = []
            for i in range(len(columnas)):
                tipo_dato = tipos_columnas[columnas[i]]
                valor_actual = valor[i]
                if tipo_dato == 'INTEGER':
                    valores.append(int(valor_actual))
                elif tipo_dato == 'REAL':
                    valores.append(float(valor_actual))
                else:
                    valores.append(valor_actual)
            self.charlie.insertarDatos(nombreTabla, valores)
            self.charlie.cerrarConexion()
            for widget in self.beta.root.winfo_children():
                widget.destroy()
            self.beta.conectarBD()

    def consulta(self):
        entrada = self.beta.txtEleccion.get("1.0", tk.END).strip()
        elementos = [elem.strip() for elem in entrada.split(",")]
        for widget in self.beta.root.winfo_children():
            widget.destroy()
        self.beta.imprimirDatos2()
        if len(elementos) == 2:
            nombreBaseDatos, nombreTabla = elementos
            self.sesionActual=nombreBaseDatos
            self.charlie.conectarBD(self.sesionActual)
            self.beta.txtResultadosCi1.delete("1.0", tk.END)
            self.beta.txtResultadosCi1.insert(tk.END, self.charlie.imprimirContenido(nombreTabla))
            self.charlie.cerrarConexion()
        else:
            messagebox.showwarning("Error","Se deben ingresar exactamente dos elementos separados por una coma.")
        
    def destruir(self):
        for widget in self.beta.root.winfo_children():
            widget.destroy()
        self.beta.conectarBD()
