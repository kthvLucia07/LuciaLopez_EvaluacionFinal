import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pandas as pd

def plot_graph(data_dict, ax, canvas):
    ax.clear()  # Limpia el gráfico anterior antes de dibujar el nuevo gráfico de barras

    labels = list(data_dict.keys())
    data = list(data_dict.values())

    x = np.arange(len(labels))
    colors = plt.cm.tab20(np.linspace(0, 1, len(data)))
    ax.bar(x, data, color=colors)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("Gráfico de Barras")
    ax.set_xlabel("Datos")
    ax.set_ylabel("Valores")
    ax.figure.tight_layout()

    canvas.draw()

def add_data(data_dict, name, value, ax, canvas, table):
    data_dict[name] = value
    plot_graph(data_dict, ax, canvas)
    update_table(data_dict, table)

def delete_data(data_dict, name, ax, canvas, table):
    if name in data_dict:
        del data_dict[name]
        plot_graph(data_dict, ax, canvas)
        update_table(data_dict, table)
    else:
        messagebox.showerror("Error", "El dato ingresado no existe.")

def update_table(data_dict, table):
    table.delete(*table.get_children())
    for name, value in data_dict.items():
        table.insert("", "end", values=(name, value))

def main():
    root = tk.Tk()
    root.title("Análisis y Visualización del programa")
    root.geometry("1000x400")

    # Establecer color de fondo celeste bebé (#87CEFA)
    root.configure(bg="#87CEFA")

    data_dict = {}

    figure = plt.figure(figsize=(5, 4))
    ax = figure.add_subplot(111)  # Agregar el widget canvas al objeto figure
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    data_label = tk.Label(root, text="Ingrese los datos (nombre, valor):")
    data_label.pack()

    name_entry = tk.Entry(root)
    name_entry.pack()

    value_entry = tk.Entry(root)
    value_entry.pack()

    add_data_button = tk.Button(root, text="Agregar Datos", command=lambda: add_data(data_dict, name_entry.get(), int(value_entry.get()), ax, canvas, table))
    add_data_button.pack()

    delete_label = tk.Label(root, text="Ingrese el nombre del dato a eliminar:")
    delete_label.pack()

    delete_entry = tk.Entry(root)
    delete_entry.pack()

    delete_data_button = tk.Button(root, text="Eliminar Dato", command=lambda: delete_data(data_dict, delete_entry.get(), ax, canvas, table))
    delete_data_button.pack()

    columns = ("Nombre", "Valor")
    table = ttk.Treeview(root, columns=columns, show="headings")
    table.heading("Nombre", text="Nombre")
    table.heading("Valor", text="Valor")
    table.pack()

    update_table(data_dict, table)  # Mostrar una tabla vacía inicialmente

    root.mainloop()

if __name__ == "__main__":
    main()
