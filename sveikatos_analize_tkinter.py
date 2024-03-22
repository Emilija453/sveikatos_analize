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
                
    elif pasirinkimas.get() == "Aukščiausi-žemiausi HDI":

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
    
    elif pasirinkimas.get() == "Baltijos šalys":
        
        baltijos_salys = duomenys[(duomenys['country'].isin(['Estonija', 'Latvia', 'Lithuania'])) & (duomenys['year'] >= pradzios_metai) & (duomenys['year'] <= pabaigos_metai)]
        
        vidutinis_hdi_baltija = baltijos_salys.groupby('year')['value'].mean()
        
        ax.clear()
        ax.plot(vidutinis_hdi_baltija.index, vidutinis_hdi_baltija.values, marker='o')
        ax.set_xlabel('Metai')
        ax.set_ylabel('Vidutinis HDI')
        ax.set_title(f'Vidutinis HDI Baltijos šalyse ({metu_intervalas})')

        canvas.draw()


    elif pasirinkimas.get() == "Skandinavijos šalys":
    
        skandinavijos_salys = duomenys[(duomenys['country'].isin(['Denmark', 'Sweden', 'Norway'])) & (duomenys['year'] >= pradzios_metai) & (duomenys['year'] <= pabaigos_metai)]
        
        vidutinis_hdi_skandinavija = skandinavijos_salys.groupby('year')['value'].mean()
        
        # Plot duomenis
        ax.clear()
        ax.plot(vidutinis_hdi_skandinavija.index, vidutinis_hdi_skandinavija.values, marker='o')
        ax.set_xlabel('Metai')
        ax.set_ylabel('Vidutinis HDI')
        ax.set_title(f'Vidutinis HDI Skandinavijos šalyse ({metu_intervalas})')

        canvas.draw()

    else:
        metu_intervalo_combobox.config(state='disabled')
    
        skandinavijos_salys = duomenys[duomenys['country'].isin(['Denmark', 'Sweden', 'Norway'])]
        baltijos_salys = duomenys[duomenys['country'].isin(['Estonija', 'Latvia', 'Lithuania'])]

        baltijos_saliu_pokytis = baltijos_salys.groupby('year')['value'].mean().round(2).pct_change() * 100
        skandinavijos_saliu_pokytis = skandinavijos_salys.groupby('year')['value'].mean().round(2).pct_change() * 100
        bendras_saliu_pokytis = duomenys.groupby('year')['value'].mean().round(2).pct_change() * 100

    
        ax.clear()
        ax.plot(bendras_saliu_pokytis.index, bendras_saliu_pokytis.values, label='Visų šalių')
        ax.plot(baltijos_saliu_pokytis.index, baltijos_saliu_pokytis.values, label='Baltijos šalių')
        ax.plot(skandinavijos_saliu_pokytis.index, skandinavijos_saliu_pokytis.values, label='Skandinavijos šalių')
        ax.set_xlabel('Metai')
        ax.set_ylabel('Pokytis proc.')
        ax.set_title('Sveikatos indekso pokytis 1985-2013')
        ax.legend()

        canvas.draw()

    


#TKINTER 
root = tk.Tk()
root.title("HDI Analizė")
root.geometry("800x800")

ttk.Label(root, text="Pasirinkite Metų Intervalą:").grid(row=0, column=0)
metu_intervalo_combobox = ttk.Combobox(root, values=['1980-1985', '1990-1995', '2000-2005', '2010-2013'])
metu_intervalo_combobox.grid(row=0, column=1, sticky="ew")  
metu_intervalo_combobox.current(0)

pasirinkimas = tk.StringVar()
pasirinkimas.set("Visos šalys")

# Radio button frame'as
radio_frame = ttk.Frame(root)
radio_frame.grid(row=1, column=0, columnspan=4)

ttk.Radiobutton(radio_frame, text="Visos šalys", variable=pasirinkimas, value="Visos šalys").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(radio_frame, text="Aukščiausi-žemiausi HDI", variable=pasirinkimas, value="Aukščiausi-žemiausi HDI").grid(row=0, column=1, sticky="w")
ttk.Radiobutton(radio_frame, text="Baltijos šalys", variable=pasirinkimas, value="Baltijos šalys").grid(row=0, column=2, sticky="w")
ttk.Radiobutton(radio_frame, text="Skandinavijos šalys", variable=pasirinkimas, value="Skandinavijos šalys").grid(row=0, column=3, sticky="w")
ttk.Radiobutton(radio_frame, text="Sveikatos indekso pokyčiai", variable=pasirinkimas, value="Sveikatos indekso pokyčiai").grid(row=0, column=4, sticky="w")

atnaujinti_mygtukas = ttk.Button(root, text="Atnaujinti Grafiką", command=atnaujinti_grafika)
atnaujinti_mygtukas.grid(row=3, columnspan=2, padx=5, pady=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=4, columnspan=2)
canvas.get_tk_widget().configure(width=800, height=700)

atnaujinti_grafika()
root.mainloop()

