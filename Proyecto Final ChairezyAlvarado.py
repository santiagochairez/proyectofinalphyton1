import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x500")
    reg.configure(bg="#f4f6f9")
    reg.resizable(False, False)

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="Registro de Productos",
        font=("Arial", 20, "bold"),
        bg="#f4f6f9",
        fg="#1f2937"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(
        reg,
        bg="white",
        bd=2,
        relief="groove"
    )
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # -------------------------
    # ESTILO
    # -------------------------
    label_style = {
        "font": ("Arial", 11, "bold"),
        "bg": "white",
        "fg": "#374151",
        "anchor": "w"
    }

    entry_style = {
        "font": ("Arial", 11),
        "bd": 1,
        "relief": "solid",
        "width": 30
    }

    # -------------------------
    # CAMPOS
    # -------------------------
    tk.Label(frame, text="ID del Producto", **label_style).pack(pady=(20,5), padx=30, fill="x")
    txt_id = tk.Entry(frame, **entry_style)
    txt_id.pack(pady=5)

    tk.Label(frame, text="Descripción", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_desc = tk.Entry(frame, **entry_style)
    txt_desc.pack(pady=5)

    tk.Label(frame, text="Precio", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_precio = tk.Entry(frame, **entry_style)
    txt_precio.pack(pady=5)

    tk.Label(frame, text="Categoría", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_categoria = tk.Entry(frame, **entry_style)
    txt_categoria.pack(pady=5)

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():
        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validaciones
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        frame,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="white",
        activebackground="#374151",
        activeforeground="white",
        width=20,
        height=2,
        cursor="hand2",
        relief="flat"
    )

    btn_guardar.pack(pady=30)


# -------------------------
# FUNCIONES RESTANTES
# -------------------------
from datetime import datetime

def mostrar_ticket(producto, precio, cantidad, total):
  ticket = tk.Toplevel()
  ticket.title("Ticket de Venta")
  ticket.geometry("300x350")
  ticket.resizable(False, False)

  # Fecha y hora
  fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

  # Texto del ticket
  texto = (
  " *** PUNTO DE VENTA ***#\n"
  "--------------------------------------\n"
  f"Fecha: {fecha_hora}\n"
  "--------------------------------------\n"
  f"Producto: {producto}\n"
  f"Precio: ${precio}\n"
  f"Cantidad: {cantidad}\n"
  "--------------------------------------\n"
  f"TOTAL: ${total}\n"
  "--------------------------------------\n"
  " ¡GRACIAS POR SU COMPRA!\n"
  )

  lbl_ticket = tk.Label(ticket, text=texto, justify="left", font=("Consolas", 11))
  lbl_ticket.pack(pady=15)

  btn_cerrar = ttk.Button(ticket, text="Cerrar", command=ticket.destroy)
  btn_cerrar.pack(pady=10)

from datetime import datetime

def mostrar_ticket(producto, precio, cantidad, total):
  ticket = tk.Toplevel()
  ticket.title("Ticket de Venta")
  ticket.geometry("300x350")
  ticket.resizable(False, False)

  # Fecha y hora
  fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

  # Texto del ticket
  texto = (
  " *** PUNTO DE VENTA ***\n"
  "--------------------------------------\n"
  f"Fecha: {fecha_hora}\n"
  "--------------------------------------\n"
  f"Producto: {producto}\n"
  f"Precio: ${precio}\n"
  f"Cantidad: {cantidad}\n"
  "--------------------------------------\n"
  f"TOTAL: ${total}\n"
  "--------------------------------------\n"
  " ¡GRACIAS POR SU COMPRA!\n"
  )

  lbl_ticket = tk.Label(ticket, text=texto, justify="left", font=("Consolas", 11))
  lbl_ticket.pack(pady=15)

  btn_cerrar = ttk.Button(ticket, text="Cerrar", command=ticket.destroy)
  btn_cerrar.pack(pady=10)
def abrir_registro_ventas():
   ven = tk.Toplevel()
   ven.title("Registro de Ventas")
   ven.geometry("420x430")
   ven.resizable(False, False)
   # ------------------------------------
   # Cargar productos desde productos.txt
   # ------------------------------------
   productos = {}

# Lista de nombres de productos
   lista_productos = list(productos.keys())
   # ------------------------------------
   # CONTROLES VISUALES
   # ------------------------------------
   lbl_prod = tk.Label(ven, text="Producto:", font=("Arial", 12))
   lbl_prod.pack(pady=5)
   cb_producto = ttk.Combobox(ven, values=lista_productos, font=("Arial", 12), state="readonly")
   cb_producto.pack(pady=5)
   lbl_precio = tk.Label(ven, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_precio.pack(pady=5)
   lbl_cantidad = tk.Label(ven, text="Cantidad:", font=("Arial", 12))
   lbl_cantidad.pack(pady=5)
   cantidad_var = tk.StringVar(ven)
   ven.cantidad_var = cantidad_var   # importante: mantiene la referencia
   txt_cantidad = tk.Entry(ven, font=("Arial", 12), textvariable=cantidad_var)
   txt_cantidad.pack(pady=5)  
   cantidad_var.trace_add("write", lambda *args: calcular_total())
   lbl_total = tk.Label(ven, text="Total:", font=("Arial", 12))
   lbl_total.pack(pady=5)
   txt_total = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_total.pack(pady=5)
   
   def actualizar_precio(event):
             
      prod = cb_producto.get()
      if prod in productos:
         txt_precio.config(state="normal")
         txt_precio.delete(0, tk.END)
         txt_precio.insert(0, productos[prod])
         txt_precio.config(state="readonly")
         calcular_total()
   def calcular_total(*args):      
      try:
         cant = int(txt_cantidad.get())
         precio = float(txt_precio.get())
         total = cant * precio
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.insert(0, total)
         txt_total.config(state="readonly")
      except:
         # Si no hay número válido, limpiar el total
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.config(state="readonly")
   def registrar_venta():
      prod = cb_producto.get()
      precio = txt_precio.get()
      cant = txt_cantidad.get()
      total = txt_total.get()
      if prod == "" or precio == "" or cant == "" or total == "":
         messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos.")
         return
      # Guardar venta
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivov = os.path.join(BASE_DIR,"ventas.txt")
      with open(archivov, "a", encoding="utf-8") as archivo:
         archivo.write(f"{prod}|{precio}|{cant}|{total}\n")
         messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")
         mostrar_ticket(prod, precio, cant, total)
      # Limpiar campos
      cb_producto.set("")
      txt_precio.config(state="normal"); txt_precio.delete(0, tk.END); txt_precio.config(state="readonly")
      txt_cantidad.delete(0, tk.END)
      txt_total.config(state="normal"); txt_total.delete(0, tk.END); txt_total.config(state="readonly")
   # ------------------------------------
   # EVENTOS Y BOTÓN
   # ------------------------------------
   cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)
   btn_guardar = ttk.Button(ven, text="Registrar Venta", command=registrar_venta)
   btn_guardar.pack(pady=25)
   
   try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivof = os.path.join(BASE_DIR, "productos.txt")

        with open(archivof, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("|")

                if len(partes) == 4:
                    idp, desc, precio, cat = partes
                    productos[desc] = float(precio)

   except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo productos.txt")
        ven.destroy()
        return

   lista_productos = list(productos.keys())

    # ------------------------------------
    # TÍTULO
    # ------------------------------------

def abrir_reportes():
  ventana = tk.Toplevel()
  ventana.title("Reporte de Ventas")
  ventana.geometry("700x400")
  ventana.configure(bg="#f2f2f2")
  titulo = tk.Label(ventana, text="Reporte de Ventas Realizadas",
  font=("Arial", 16, "bold"), bg="#f2f2f2")
  titulo.pack(pady=10)

  # Frame para el GRID
  frame_tabla = tk.Frame(ventana)
  frame_tabla.pack(pady=10)

  # Columnas del archivo ventas.txt
  columnas = ("producto", "precio", "cantidad", "total")
  tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=15)

  # Encabezados
  tabla.heading("producto", text="Producto")
  tabla.heading("precio", text="Precio")
  tabla.heading("cantidad", text="Cantidad")
  tabla.heading("total", text="Total")

  # Tamaño de columnas
  tabla.column("producto", width=250, anchor="center")
  tabla.column("precio", width=100, anchor="center")
  tabla.column("cantidad", width=100, anchor="center")
  tabla.column("total", width=120, anchor="center")
  tabla.pack()

  # --- Leer archivo ventas.txt ---
  try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(BASE_DIR,"ventas.txt")
    with open(archivo, "r", encoding="utf-8") as archivo:
      for linea in archivo:
        if linea.strip():
          datos = linea.strip().split("|")
          if len(datos) == 4:
            tabla.insert("", tk.END, values=datos)
  except FileNotFoundError:
    messagebox.showerror("Error", "El archivo ventas.txt no existe.")
    ventana.destroy()
    return

def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta")
ventana.geometry("500x650")
ventana.configure(bg="#f4f6f9")
ventana.resizable(False, False)

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="#f4f6f9"
    )
    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14),
        bg="#f4f6f9"
    )
    lbl_sin_logo.pack(pady=40)

# -------------------------
# TÍTULO
# -------------------------
titulo_principal = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Arial", 22, "bold"),
    bg="#f4f6f9",
    fg="#111827"
)

titulo_principal.pack(pady=10)

# -------------------------
# ESTILO BOTONES
# -------------------------
btn_config = {
    "bg": "#111827",
    "fg": "white",
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "cursor": "hand2",
    "relief": "flat",
    "activebackground": "#374151",
    "activeforeground": "white"
}

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    **btn_config
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    **btn_config
)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    **btn_config
)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    **btn_config
)
btn_acerca.pack(pady=10)

# -------------------------
# INICIAR APP
# -------------------------
ventana.mainloop()
