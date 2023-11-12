# tradeKR
trade helper per krunker.io

## usage
1. metti il tuo nome utente in username
2. metti i valori che preferisci come ad esempio `min_margine`
3. crea la directory data : ```$ bash setup.sh ```
4. ```$ python main.py```

## roadmap
### bug
- [x] fixare quando si blocca index 867 per sticker animati
- [x] creare in automatico directory data se non esiste
### features 
- [x] far scrivere tutto su un file con le date(come fatto su mscraper)
  - [x] nel caso si fermasse far riprendere da dove lasciato mettendo all_rows=file.read(1) e start=file.read(2) nel seconda linea index attuale 
  - [ ] fare plot.py che fa il plot dei dati usando ad esempio manim o matplotlib
  - [ ] fare servizio systemctl che avvia al boot lo script e segnala mandando notify-send se ho venduto qualcosa guardando differenza di kr
    - [ ] mandarlo anche con un bot telegram  
- [x] riordinare in base a margine/bestprice oppure in base a margine e basta o bestprice e basta
  - [ ] comparare con avg price consigliato da krunker.io(posso o fare scrape ogni volta oppure guardare questo [file](https://api.krunker.io/webhooks/general/items/prices) )
  - [ ] togliere dalla lista quelli che non hanno un avg price o che il best price é di molto superiore l'ultimo
  - [ ] direttamente salvare tutti e poi in un secondo momento poterli filtrare sulla base dei parametri indicati
  - [ ] consigliare quali comprare sulla base del prezzo consigliato da krunker e guardando il grafico(fare questo solo se é giá nella lista dei salvati,non per tutti altrimenti ci vanno anni)
### ottimizzazioni
- [ ] implementare multithreading e riscrivere parti del codice vario
- [ ] skippare appena capisce che non c'é un item anziché aspettare che appaia anche se cé scritto item not found o roba simile
