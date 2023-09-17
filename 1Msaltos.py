
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import ttk
import time

ventana = tk.Tk()
fig, ax = plt.subplots()
tv = ttk.Treeview(ventana, columns=("col1","col2","col3"))
iteration = 0
final_position = []

a = 9
c = 3
m = time.time()
xi = 4
min_value = 0
max_value = 1

def calculate_ri():
    global xi  # Declare xi as a global variable
    xi = ((a * xi) + c) % m
    return xi / (m - 1)

def calculate_ni():
    global min_value, max_value  # Declare min_value and max_value as global variables
    return 1 if(min_value + (max_value - min_value) * calculate_ri())>0.5  else 0
def simulate():
    start = time.time()
    
    actual_position = 0
    jumps_made = 0
    frecuent_positions = {0:1}
    for i in range(1000000):
        jump = calculate_ni()
        
        if jump == 0:
            actual_position-=1
        else:
            actual_position+=1
        
        jumps_made += 1
        
        if actual_position in frecuent_positions:
            frecuent_positions[actual_position] += 1
        else: 
            frecuent_positions[actual_position] = 1
        
    fin = time.time()
    
    final_position.append(actual_position)
    
    tv.column("#0",width=40)
    tv.column("col1", width=80, anchor="center")
    tv.column("col2", width=80, anchor="center")
    tv.column("col3", width=80, anchor="center")
    
    tv.heading("#0", text="#",anchor="center")
    tv.heading("col1",text="Saltos",anchor="center")
    tv.heading("col2",text="Posicion Final",anchor="center")
    tv.heading("col3",text="Tiempo (ms)",anchor="center")
    
    global iteration
    iteration += 1
    execution_time = (fin - start)*1000
    
    tv.insert("","end",text=iteration,values=("1.000.000", actual_position,execution_time))
    tv.grid(row=2,column=2)
    
    
    ax.bar(frecuent_positions.keys(),frecuent_positions.values(),align='center')
    ax.set_xlabel('Posicion')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Frecuencia de las posiciones alcanzadas por la rana')
    
    
    
    fig.set_size_inches(6,4)
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)
    
    fig2, ax2 = plt.subplots()
    ax2.hist(final_position)
    ax2.set_xlabel('posicion')
    ax2.set_ylabel('Frecuencia')
    ax2.set_title('frecuencia de psosiciones finales de la rana')
    
    canvas2 = FigureCanvasTkAgg(fig2, master=ventana)
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=1, column=2)
    
    

    
def close():
    plt.close(fig)
    ventana.destroy()
    
ventana.title("Simulacion de 1M de saltos de la rana")
ventana.protocol("WM_DELETE_WINDOW",close)

btn_start = tk.Button(ventana, text="Iniciar Simulacion", command=simulate)
btn_start.grid(row=0,column=0)

ventana.mainloop()

    
    
    
            
        
    
    
    
