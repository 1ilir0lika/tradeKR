# tradeKR
- fare scrape con soup di tutti i div di classe
class="marketPrice"

- trovare differenza tra le prima 2 offerte

- farlo per ogni index
https://krunker.io/social.html?p=market&i=index

## todo
### bug
- [x] fixare quando si blocca index 867 per sticker animati
### features 
- [x] far scrivere tutto su un file con le date(come fatto su mscraper)
- [ ] fare plot.py che fa il plot dei dati usando ad esempio manim o matplotlib
- [x] riordinare in base a margine/bestprice oppure in base a margine e basta o bestprice e basta
- [ ] comparare con avg price consigliato da krunker.io(posso o fare scrape ogni volta oppure guardare questo [file](https://api.krunker.io/webhooks/general/items/prices) )
- [ ] togliere dalla lista quelli che non hanno un avg price o che il best price é di molto superiore l'ultimo
- [ ] consigliare quali comprare sulla base del prezzo consigliato da krunker e guardando il grafico(fare questo solo se é giá nella lista dei salvati,non per tutti altrimenti ci vanno anni)
### ottimizzazioni
- [ ] implementare multithreading e riscrivere parti del codice vario
- [ ] skippare appena capisce che non c'é un item anziché aspettare che appaia anche se cé scritto item not found o roba simile
