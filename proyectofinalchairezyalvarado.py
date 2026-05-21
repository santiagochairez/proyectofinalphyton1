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
def abrir_registro_ventas():
    ven = tk.Toplevel()
    ven.title("Registro de Ventas")
    ven.geometry("760x700")
    ven.configure(bg="#f4f6f9")
    ven.resizable(False, False)

    # ------------------------------------
    # CARGAR PRODUCTOS
    # ------------------------------------
    productos = {}

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
    titulo = tk.Label(
        ven,
        text="Registro de Ventas",
        font=("Arial", 22, "bold"),
        bg="#f4f6f9",
        fg="#0b1736"
    )
    titulo.pack(pady=30)

    # ------------------------------------
    # FRAME PRINCIPAL
    # ------------------------------------
    frame = tk.Frame(
        ven,
        bg="white",
        bd=1,
        relief="solid"
    )
    frame.pack(padx=35, pady=10, fill="both", expand=True)

    # ------------------------------------
    # ESTILOS
    # ------------------------------------
    fuente_label = ("Arial", 16, "bold")
    fuente_entry = ("Arial", 14)

    estilo = ttk.Style()
    estilo.theme_use("clam")

    estilo.configure(
        "TCombobox",
        fieldbackground="white",
        background="white",
        foreground="black",
        padding=8,
        font=fuente_entry
    )

    # ------------------------------------
    # PRODUCTO
    # ------------------------------------
    lbl_prod = tk.Label(
        frame,
        text="Producto",
        font=fuente_label,
        bg="white",
        fg="#0b1736"
    )
    lbl_prod.pack(anchor="w", padx=50, pady=(40, 10))

    cb_producto = ttk.Combobox(
        frame,
        values=lista_productos,
        font=fuente_entry,
        state="readonly",
        width=30
    )
    cb_producto.pack(pady=5)

    # ------------------------------------
    # PRECIO
    # ------------------------------------
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        font=fuente_label,
        bg="white",
        fg="#0b1736"
    )
    lbl_precio.pack(anchor="w", padx=50, pady=(25, 10))

    txt_precio = tk.Entry(
        frame,
        font=fuente_entry,
        width=32,
        relief="solid",
        bd=1,
        state="readonly",
        justify="center"
    )
    txt_precio.pack(pady=5)

    # ------------------------------------
    # CANTIDAD
    # ------------------------------------
    lbl_cantidad = tk.Label(
        frame,
        text="Cantidad",
        font=fuente_label,
        bg="white",
        fg="#0b1736"
    )
    lbl_cantidad.pack(anchor="w", padx=50, pady=(25, 10))

    cantidad_var = tk.StringVar(ven)
    ven.cantidad_var = cantidad_var

    txt_cantidad = tk.Entry(
        frame,
        font=fuente_entry,
        textvariable=cantidad_var,
        width=32,
        relief="solid",
        bd=1,
        justify="center"
    )
    txt_cantidad.pack(pady=5)

    cantidad_var.trace_add("write", lambda *args: calcular_total())

    # ------------------------------------
    # TOTAL
    # ------------------------------------
    lbl_total = tk.Label(
        frame,
        text="Total",
        font=fuente_label,
        bg="white",
        fg="#0b1736"
    )
    lbl_total.pack(anchor="w", padx=50, pady=(25, 10))

    txt_total = tk.Entry(
        frame,
        font=fuente_entry,
        width=32,
        relief="solid",
        bd=1,
        state="readonly",
        justify="center"
    )
    txt_total.pack(pady=5)

    # ------------------------------------
    # FUNCIONES
    # ------------------------------------
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
            txt_total.insert(0, f"${total:.2f}")
            txt_total.config(state="readonly")

        except:

            txt_total.config(state="normal")
            txt_total.delete(0, tk.END)
            txt_total.config(state="readonly")

    def registrar_venta():

        prod = cb_producto.get()
        precio = txt_precio.get()
        cant = txt_cantidad.get()
        total = txt_total.get()

        if prod == "" or precio == "" or cant == "" or total == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Todos los campos deben estar completos."
            )
            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivov = os.path.join(BASE_DIR, "ventas.txt")

        with open(archivov, "a", encoding="utf-8") as archivo:
            archivo.write(f"{prod}|{precio}|{cant}|{total}\n")

        messagebox.showinfo(
            "Venta Registrada",
            "La venta se registró correctamente."
        )

        # LIMPIAR CAMPOS
        cb_producto.set("")

        txt_precio.config(state="normal")
        txt_precio.delete(0, tk.END)
        txt_precio.config(state="readonly")

        txt_cantidad.delete(0, tk.END)

        txt_total.config(state="normal")
        txt_total.delete(0, tk.END)
        txt_total.config(state="readonly")

    # ------------------------------------
    # EVENTOS
    # ------------------------------------
    cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)

    # ------------------------------------
    # BOTÓN
    # ------------------------------------
    btn_guardar = tk.Button(
        frame,
        text="Registrar Venta",
        font=("Arial", 16, "bold"),
        bg="#07142e",
        fg="white",
        activebackground="#10254d",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=25,
        pady=12,
        command=registrar_venta
    )

    btn_guardar.pack(pady=45)
            
def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

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