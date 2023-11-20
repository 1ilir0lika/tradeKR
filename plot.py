import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tabulate import tabulate
import mplcursors,datetime,webbrowser,sys

date = datetime.date.today()
index = []
prices = []
ratio_buy = []
ratio_gain = []

nome_file = 'data/' + str(date) + '.pr'

try:
    with open(nome_file, 'r') as start_file:
        list_of_lines = start_file.readlines()
        all_rows = eval(list_of_lines[0].strip())
        for r in all_rows:
            index.append(r[0])
            prices.append(r[1])
            ratio_gain.append(r[3])
            ratio_buy.append(r[2])

except FileNotFoundError:
    print(f"Error: The file '{nome_file}' does not exist.")
    sys.exit()

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

# URL base
base_url = 'https://krunker.io/social.html?p=market&i='

# Creazione del plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot dei punti 3D
scatter = ax.scatter(prices, ratio_gain, ratio_buy, alpha=0.5)

# Etichette degli assi
ax.set_xlabel('Best Price')
ax.set_ylabel('Ratio Buy')
ax.set_zlabel('Ratio Gain')

def on_click(event):
    if event.inaxes is not None:
        ind = event.ind[0] if hasattr(event, 'ind') and len(event.ind) else None
        if ind is not None:
            url = base_url + str(index[ind])
            webbrowser.open(url)
            # Cambia il colore del punto selezionato in rosso
            scatter._facecolors3d = 'none'  # Resetta tutti i punti
            scatter._facecolors3d[ind, :] = (1, 0, 0, 1)  # Imposta il punto selezionato in rosso

            # Aggiorna il plot
            plt.draw()

# Collega la funzione on_click all'evento di pressione del pulsante
fig.canvas.mpl_connect('pick_event', on_click)

# Aggiungi le etichette con i valori di index quando si passa sopra ai punti
cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def display_info(sel):
    ind = sel.index
    sel.annotation.set_text(f'Index: {index[ind]}')

# Mostra il plot
plt.show()
