import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

duomenys = pd.read_csv('health-index-1.csv')

def atnaujinti_grafika():
    # Pasirinkti metu ntervala
    metu_intervalas = metu_intervalo_combobox.get()
    pradzios_metai, pabaigos_metai = map(int, metu_intervalas.split('-'))

    # Filtruoti duomenis pagal pasirinktą metų intervalą
    filtruoti_duomenys = duomenys[(duomenys['year'] >= pradzios_metai) & (duomenys['year'] <= pabaigos_metai)]

    if pasirinkimas.get() == "Visos šalys":
         # Apskaičiuoti vidutinį HDI kiekvienam laikotarpiui
        vidutinis_hdi = filtruoti_duomenys.groupby('year')['value'].mean()


        # Plot duomenis
        ax.clear()
        ax.plot(vidutinis_hdi.index, vidutinis_hdi.values, marker='o')
        ax.set_xlabel('Metai')
        ax.set_ylabel('Vidutinis HDI')
        ax.set_title(f'Vidutinis HDI ({metu_intervalas})')

        canvas.draw()
                
    else:
        # Apskaičiuoti HDI pagal šalį su vidurkiu
        median_by_country = filtruoti_duomenys.groupby('country')['value'].mean()
        
        top_five = median_by_country.nlargest(5)
        worst_five = median_by_country.nsmallest(5)

        # Bar chartas penkiem geriausiam ir blogiausiam HDI
        ax.clear()
        ax.bar(top_five.index, top_five.values, color='green', label='Aukščiausi HDI')
        ax.bar(worst_five.index, worst_five.values, color='red', label='Žemiausi')
        ax.set_ylabel('Vidutinis HDI')
        ax.set_title(f'Aukščiausi ir žemiausi HDI ({metu_intervalas})')
        ax.legend()
       
        ax.set_xticklabels(top_five.index.append(worst_five.index), rotation=30)
            

    canvas.draw()

#TKINTER 
root = tk.Tk()
root.title("HDI Analizė")
root.geometry("800x800")

ttk.Label(root, text="Pasirinkite Metų Intervalą:").grid(row=0, column=0)
metu_intervalo_combobox = ttk.Combobox(root, values=['1980-1985', '1990-1995', '2000-2005', '2010-2013'])
metu_intervalo_combobox.grid(row=0, column=1)
metu_intervalo_combobox.current(0)

pasirinkimas = tk.StringVar()
pasirinkimas.set("Visos šalys")

ttk.Radiobutton(root, text="Visos šalys", variable=pasirinkimas, value="Visos šalys").grid(row=1, column=0)
ttk.Radiobutton(root, text="Vidutinis HDI pagal šalį", variable=pasirinkimas, value="Vidutinis HDI pagal šalį").grid(row=1, column=1)

atnaujinti_mygtukas = ttk.Button(root, text="Atnaujinti Grafiką", command=atnaujinti_grafika)
atnaujinti_mygtukas.grid(row=3, columnspan=2, padx=5, pady=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=4, columnspan=2)
canvas.get_tk_widget().configure(width=800, height=700)

atnaujinti_grafika()
root.mainloop()
