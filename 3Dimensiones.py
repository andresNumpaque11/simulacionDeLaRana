import random
import math
import time
import tkinter as tk
import matplotlib.pyplot as plt

times = []
results = []

def random_walk():
    x = 0
    y = 0
    z = 0
    jumps = 0
    start = time.time()
    while(x,y,z) != (45,23,17):
        direction = random.choice(['U','D','E','O','N','S'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y-= 1
        elif direction == 'E':
            x+= 1
        elif direction == 'O':
            x-= 1
        elif direction == 'U':
            z+= 1
        else:
            z-=1
        jumps+=1
        if(time.time()-start>0.001):
            print(x,",",y,",",z)
            return 0
    print("llegué a las coordenadas")
    times.append(time.time()-start)
    results.append(jumps)
    return jumps
simulations = 2
total_jumps = 0

while len(times) != simulations:
    total_jumps += random_walk()
    

average_jumps = total_jumps/simulations
average_times = sum(times)/len(times)


ventana = tk.Tk()
ventana.title("Simulacion trifimensional")


jumps_label = tk.Label(ventana, text=f"el promedio de saltos para llegar a (45,23,17) es: {average_jumps}")
jumps_label.pack()

time_label = tk.Label(ventana,  text=f"el tiempo promedio de la simulacion fue de: {average_times}")
time_label.pack()

results_label = tk.Label(ventana, text=f"Resultados de la simulacion: {results}")
results_label.pack()

plt.hist(results)
plt.title("Grafica de numero de saltos para llegar a las coordenadas")
plt.xlabel("Numero de saltos")
plt.ylabel("Frecuencia")
plt.show()

ventana.mainloop()