import tkinter as tk
import random as rd

ventana = tk.Tk()
ancho = 800
alto = 600
size=f"{ancho}x{alto}"

ventana.geometry(size)
ventana.resizable(False,False)

colores = [
  "#3E92CC", "#E94F37", "#2E933C", "#F6D55C", "#5D2E8C",
  "#1FAB89", "#F45B69", "#FF6F61", "#9D44B5", "#4DD599",
  "#F7B32B", "#8C2F39", "#FF934F", "#4F5D75", "#B8F2E6",
  "#F25F5C", "#247BA0", "#FF1654", "#7FDBDA", "#1E555C",
  "#C0CAAD", "#FFE156", "#6A0572", "#0077B6", "#D81159",
  "#F4D06F", "#A1C181", "#6F1D1B", "#00B4D8", "#720026",
  "#C3B299", "#5C5470", "#FAA916", "#424B54", "#B80C09",
  "#6A994E", "#F6AE2D", "#D62828", "#003049", "#80B918",
  "#E36414", "#3D348B", "#9AE19D", "#7B2CBF", "#EF476F",
  "#06D6A0", "#118AB2", "#073B4C", "#FFD166", "#D7C0D0"
]

for i in range(12):
    ventana.rowconfigure(i, weight=1)
    ventana.columnconfigure(i,weight=1)

for column in range(12):
    for row in range(12):
        btn = tk.Button(ventana,text=f"Boton {column + 1}",bg= rd.choice(colores)) 
        btn.grid(sticky="news", row=row,column=column)

print("Hola")

ventana.mainloop()