# PROGETTO SDC 2020 

## Gestione autorizzazioni Informazioni Covid-19

Si vuole aggiungere sicurezza e controllo ad un sistema di aggiornamento e  ricezione informazioni, relative al propagarsi del covid-19 nel territorio nazionale.

Per ogni regione il sistema gestisce le  informazioni alla giornata attraverso 
Inserimento dei dati relativi al numero di: 
- decessi
- infetti 
- guariti
- Visualizzazione dei dati inseriti


### Le regioni sono aggregate per area geografica: 

- Nord 
- Centro
- Sud.



## Sicurezza Controlli e Report

Si vuole aggiungere controlli autorizzativi per ogni regione e per area geografica ipotizzando i seguenti profili:

- Governatore Regionale: accesso e inserimento ai dati della singola regione
- Admin-Area-Geografica: accesso e inserimento a tutti i dati dell’area geografica
- Admin-Governativo: accesso e inserimento a tutti i dati

La funzione di  login è completata con la creazione ed associazione di un cookie per ogni utenza.
L’accesso alle pagine di competenza è controllato dalle  Access Rules & Validation Rules.
La visualizzazione dei dati pubblici aggiornati  è disponibile solamente da un orario in poi per un tempo ( es: dalle 18:00)
Gli accessi protetti, sono loggati su report.

I dati di inserimento sono gestiti con funzione di Update attraverso il metodo POST-7
La funzione di inserimento è soggetta a regole /permessi per i soli profili di admin in particolare:

Il governatore regionale può gestire i soli dati della regione che amministra.
L’amministratore di area geografica può gestire tutti i dati delle regioni appartenenti a quell'area geografica.
L’amministratore governativo nazionale può gestire tutti i dati.

I dati pubblici sono relativi ai singoli dati regionali.
..
Se durante aggiornamento un dato supera una soglia , viene aggiunta una riga visibile al solo amministratore governativo ( in una pagina di riepilogo di allarmi  e tale info sarà loggata anche su report).

Se il valore infetti supera una soglia definita ( sul file.ars o direttamente sul codice lisp) verrà utilizzata la funzione CAT con ADD per aggiungere all’insieme una notifica rispetto alla specifica regione; tale notifica sarà disponibile alla lettura per il solo profilo di amministratore governativo (valutare se includere un limite temporale con timestamp).

Si prevedono 2 modalità di esecuzione attraverso uno  switch:
-Passante ( libera da regole)
-Controllata ( con le regole di accesso)

















 
## Implementazione: 
1 cartella per ogni regione, 
Nel file ars 
Un insieme con tutti
Un insieme con le aree ( nord sud centro)

I dati aggiornati incideranno su un unico file per regione ti tipo csv ( con separatore “,”)
I dati saranno disponibili sulle pagine web che interpretano il csv, pertanto per ogni regione due pagine ( una che inserisce i dati e una che legge). 
3 pagine di Login: una per le regioni, una per le sezioni e una governativa.

Template Html 
Form in python vs node.js
Ars



### endpoint
#### pagine raggiungibili senza autenticazione
http://127.0.0.1:8888/login/loginRegione/login.html
http://127.0.0.1:8888/login/loginArea/login.html
http://127.0.0.1:8888/login/loginAdmin/login.html
http://127.0.0.1:8888/richiesta/richiestaSpostamento.html
http://127.0.0.1:8888//spostamenti/spostamentiCodiceFiscale.html


#### pagine raggiungibili dopo autenticazione (admin nazionale)
http://127.0.0.1:8888/regione/Campania/inserimento/insert.html
http://127.0.0.1:8888/regione/Abruzzo/inserimento/insert.html
http://127.0.0.1:8888/regione/Sicilia/inserimento/insert.html
http://127.0.0.1:8888/regione/Lazio/inserimento/insert.html
http://127.0.0.1:8888/regione/Lombardia/inserimento/insert.html
http://127.0.0.1:8888/regione/Veneto/inserimento/insert.html

http://127.0.0.1:8888/regione/Campania/dati/view.html
http://127.0.0.1:8888/regione/Abruzzo/dati/view.html
http://127.0.0.1:8888/regione/Sicilia/dati/view.html
http://127.0.0.1:8888/regione/Lazio/dati/view.html
http://127.0.0.1:8888/regione/Lombardia/dati/view.html
http://127.0.0.1:8888/regione/Veneto/dati/view.html

visione tutti gli spostamenti
http://127.0.0.1:8888/spostamenti/spostamenti.html

publicazione dei dati per un'ora
http://127.0.0.1:8888/PubblicaDati 


http://127.0.0.1:8888/richiesta/switch.html

visione di tutti gli allert (solo admin nazionale)
http://127.0.0.1:8888//regione/alert.html









