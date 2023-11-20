# tradeKR
trade helper per krunker.io

## usage
1. metti il tuo nome utente in username `username='*default*'`
2. metti i valori che preferisci come ad esempio `min_margine`
3. crea la directory data : ```$ bash setup.sh ```
4. ```$ python main.py```
5. la prima volta,siccome krunker non ti mostra gli item se non sei loggato,dovrai **accettare i cookie e fare il login**,cosí lo sarai sempre anche in tutte le future schede
6. dopo che ha raccolto diversi dati per visualizzarli meglio eseguire ```$ python plot.py```

## roadmap
### bug
- [x] fixare quando si blocca index 867 per sticker animati
- [x] creare in automatico directory data se non esiste
- [x] fixare path per tutti quanti ovvero con ~ anziché lo username
### features 
- [x] far scrivere tutto su un file con le date(come fatto su mscraper)
  - [x] nel caso si fermasse far riprendere da dove lasciato mettendo all_rows=file.read(1) e start=file.read(2) nel seconda linea index attuale 
  - [x] fare plot.py che fa il plot dei dati usando ad esempio manim o matplotlib
    - [ ] fare tipo menú a tendina dove posso scegliere il minimo di margine che voglio vedere nel grafico/il massimo di elementi/il massimo di prezzo etc 
  - [ ] fare servizio systemctl che avvia al boot lo script e segnala mandando notify-send se ho venduto qualcosa guardando differenza di kr
    - [ ] mandarlo anche con un bot telegram  
- [x] riordinare in base a margine/bestprice oppure in base a margine e basta o bestprice e basta
  - [x] comparare con last price consigliato da krunker.io(posso o fare scrape ogni volta oppure guardare questo [file](https://api.krunker.io/webhooks/general/items/prices) )
  - [ ] togliere dalla lista quelli che non hanno un last price o che il best price é di molto superiore l'ultimo
    - [ ] comprarlo in automatico sulla base dell'andamento del prezzo 
  - [ ] consigliare quali comprare sulla base del prezzo consigliato da krunker e guardando il grafico(fare questo solo se é giá nella lista dei salvati,non per tutti altrimenti ci vanno anni)
### ottimizzazioni
- [ ] implementare multithreading e riscrivere parti del codice vario
- [ ] skippare appena capisce che non c'é un item anziché aspettare che appaia anche se cé scritto item not found o roba simile
- [ ] creare blacklist di item che non interessano e da non vedere mai esempio: tutti gli item che costano meno di quanto vuoi guadagnare
### grafica
  - [ ] rendere carino readme
    - [ ] aggiungere video su come usare
  - [ ] tradurre in inglese
  - [ ] fare progetto con roadmap e non usare piú README
  
