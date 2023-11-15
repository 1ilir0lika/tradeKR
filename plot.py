import datetime
import matplotlib.pyplot as plt
import mplcursors
import sys

date = datetime.date.today()
index = []
prices = []
ratio = []
nome_file = 'data/' + str(date) + '.pr'

try:
    with open(nome_file, 'r') as start_file:
        list_of_lines = start_file.readlines()
        all_rows = eval(list_of_lines[0].strip())
        for r in all_rows:
            index.append(r[0])
            prices.append(r[1])
            ratio.append(r[3])

except FileNotFoundError:
    print(f"Error: The file '{nome_file}' does not exist.")
    sys.exit()

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

# Creazione del plot 2D con trasparenza
scatter = plt.scatter(prices, ratio, alpha=0.5)

# Etichette degli assi
plt.xlabel('Best Price')
plt.ylabel('Ratio')

# Regola il layout del grafico per evitare sovrapposizioni di etichette
plt.tight_layout()

# Aggiungi le etichette con i valori di index quando si passa sopra ai punti
cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def display_info(sel):
    ind = sel.index
    sel.annotation.set_text(f'Index: {index[ind]}')

# Mostra il plot
plt.show()
