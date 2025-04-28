import tkinter as tk
from tkinter import messagebox
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculer_statistiques():
    try:
        valeurs = entry.get()
        donnees = [float(x.strip()) for x in valeurs.split(',')]

        moyenne = statistics.mean(donnees)
        mediane = statistics.median(donnees)
        try:
            mode = statistics.mode(donnees)
        except statistics.StatisticsError:
            mode = "Aucun mode unique"
        etendue = max(donnees) - min(donnees)
        variance = statistics.variance(donnees)
        ecart_type = statistics.stdev(donnees)

        resultats = f"""
Moyenne : {moyenne}
Médiane : {mediane}
Mode : {mode}
Étendue : {etendue}
Variance : {variance}
Écart-type : {ecart_type}
        """
        output.config(state='normal')
        output.delete('1.0', tk.END)
        output.insert(tk.END, resultats)
        output.config(state='disabled')

        afficher_graphiques(donnees)

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des nombres séparés par des virgules.")
    except statistics.StatisticsError as e:
        messagebox.showerror("Erreur Statistique", str(e))

def afficher_graphiques(donnees):
    for widget in frame_graphiques.winfo_children():
        widget.destroy()

    fig, axs = plt.subplots(1, 2, figsize=(8, 3), dpi=100)
    fig.subplots_adjust(wspace=0.5)

    # Histogramme
    axs[0].hist(donnees, bins='auto', color='skyblue', edgecolor='black')
    axs[0].set_title("Histogramme")
    axs[0].set_xlabel("Valeurs")
    axs[0].set_ylabel("Fréquence")

    # Boxplot
    axs[1].boxplot(donnees, vert=False)
    axs[1].set_title("Boxplot")
    axs[1].set_xlabel("Valeurs")

    canvas = FigureCanvasTkAgg(fig, master=frame_graphiques)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Statistiques descriptives avec graphiques")
fenetre.geometry("600x600")

label = tk.Label(fenetre, text="Entrez les données (séparées par des virgules) :", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(fenetre, width=60)
entry.pack(pady=5)

bouton = tk.Button(fenetre, text="Calculer", command=calculer_statistiques, bg="#4CAF50", fg="white", font=("Arial", 12))
bouton.pack(pady=10)

output = tk.Text(fenetre, height=8, width=65, state='disabled', bg="#f0f0f0")
output.pack(pady=10)

frame_graphiques = tk.Frame(fenetre)
frame_graphiques.pack(pady=10)

fenetre.mainloop()