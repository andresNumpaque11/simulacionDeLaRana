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
    
    jumps = 0
    start = time.time()
    while(x,y) != (250,300):
        direction = random.choice(['N','S','E','O'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1  
        elif direction == 'E':
            x += 1  
        else:
            x -= 1  
            jumps += 1
            if(time.time()-start>1):
                print(x, ",",y)
                return 0
    print("llegué")
    times.append(time.time()-start)
    results.append(jumps)
    return jumps
simulations = 5
total_jumps = 0

while len(times)!=simulations:
    total_jumps+= random_walk()

average_jumps = total_jumps/ simulations
average_time = sum(times)/ len(times)



#vista
ventana = tk.Tk()
ventana.title("Simulacion  bidimensional")

jumps_label = tk.Label(ventana, text=f"el promedio de saltos para llegar a (25, 30) es: {average_jumps}")
jumps_label.pack()

time_label = tk.Label(ventana,  text=f"el tiempo promedio de la simulacion fue de: {average_time}")
time_label.pack()

results_label = tk.Label(ventana, text=f"Resultados de la simulacion: {results}")
results_label.pack()

plt.hist(results)
plt.title("Recorrido para llegar a las coordenadas")
plt.xlabel("Saltos")
plt.ylabel("Frecuencia")
plt.show()

ventana.mainloop()


    
            
 