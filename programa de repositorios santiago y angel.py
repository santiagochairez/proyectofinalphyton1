import tkinter as tk
from tkinter import font

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # Tamaño más grande

# Configurar el fondo de la ventana
ventana.configure(bg="#1E1E2F")  # Fondo oscuro elegante

# Crear un estilo de fuente personalizado
fuente_personalizada = font.Font(family="Helvetica", size=16, weight="bold")

# Crear la etiqueta con texto más grande y colores llamativos
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Santiago Chairez y Ángel Alvarado",
    font=fuente_personalizada,
    fg="#FFD700",  # Texto dorado
    bg="#1E1E2F",  # Fondo coincide con la ventana
    wraplength=400,  # Ajuste de texto para que no se salga de la ventana
    justify="center"
)
etiqueta.pack(pady=50)

# Ejecutar la ventana
ventana.mainloop()