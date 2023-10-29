# tradeKR
- fare scrape con soup di tutti i div di classe
class="marketPrice"

- trovare differenza tra le prima 2 offerte

- farlo per ogni index
https://krunker.io/social.html?p=market&i=index

- ritornare delta maggiore

`se delta > price/10+(guadagno effettivo che voglio avere){
	vendi
}`

## todo
- [ ] far scrivere tutto su un file con le date
- [ ] riordinare in base a margine/bestprice oppure in base a margine e basta o bestprice e basta
- [ ] comparare con avg price consigliato da krunker.io(posso o fare scrape ogni volta oppure scaricare un file che li contiene tutti)
- [ ] implementare multithreading
- [x] fixare quando si blocca index 867 per sticker animati
