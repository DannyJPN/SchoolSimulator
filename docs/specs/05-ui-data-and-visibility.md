# 05 UI, Data and Visibility

## Student UI

Zak ma kdykoli dostupne:

- `rozvrh`
- `ukazatel kazne v %`
- `znamky po predmetech`
- `vahy jednotlivych znamek`
- `prumer po predmetech`
- `aktivni ukoly a jejich terminy`
- `skolni rad`

Zak nevidi:

- skryte kazenske body
- detailni etiketu
- skryte vlastnosti NPC
- celkovy prumer pres vsechny predmety

## Student inventar

Inventar nema limit kapacity.

Obsahuje mimo jine:

- zakovskou knizku
- sesity po predmetech
- ucebnice
- bridlicovou tabulku
- psaci potreby
- osobni veci
- tahaky
- omluvenky

## Student historie

Zak vidi oddelene:

- `skolni historii`
- `domaci historii`
- `historii vlastnich trestu`

Navic ma seznam `znamych trestu`, ale jen pri situaci, kdy si ma trest volit.

## Teacher UI

Ucitel ma kdykoli dostupne:

- rozvrh tridy
- tridni knihu
- seznam zaku
- prubezne znamky
- kazeň
- dochazku po hodinach

Ucitel nevidi:

- domaci dusledky svych trestu
- soukrome vnitrni stavy rodicu

## Tridni kniha

Tridni kniha eviduje:

- dochazku po hodinach
- znamky
- vahy a prumery
- navrh kazne
- napomenuti
- tresty
- pochvaly
- duvody
- intenzity trestu

## Zakovska knizka

Zakovska knizka eviduje:

- znamky
- poznamky
- pochvaly

Nevede:

- napomenuti

## Rodice a znalosti

Rodice pracuji se systemem `znamych informaci`.

Zdroj informaci:

- co jim rekne zak
- co vidi v zakovske knizce
- vysvedceni
- poznamky
- pozdni prichod domu
- nalezeni schovanych predmetu (= nahodne prohledani inventare zaka)
- nahodne informovani od ucitele

Poznamky k detekci lzi a schovavani:

- Rodice detekuji lez jen pres `konkretni dukaz` (knizka, svedek), ne nahodnou pravdepodobnosti.
- Schovani veci = staci ji mit v inventari. Fyzicke skryse neexistuji — rodice prohledavaji primo inventar.
- Prohledani inventare probiha `nahodne`, ne jen pri konkretni udalosti.

Informace od ucitele:

- neni to samostatna hratelna mechanika
- ale prakticky prida rodicum `znalost`
- pravdepodobnost roste:
  - se zavaznosti prohresku
  - s cetnosti prohresku
- rodice reaguji pri `nejblizsi domaci scene`

## Detekce prohresku

### Hrac-ucitel

- rozhoduje to, co realne vidi na obrazovce
- zak v zornem poli = zak, ktereho muze sledovat
- vzdalenost modifikuje sanci odhaleni

### NPC ucitel

- pouziva stejnou logiku simulovane
- zorne pole
- vzdalenost
- aktualni cinnost ucitele

## NPC generace

- Trida se sklada z postav z `velkeho poolu`.
- Jmena a pohlavi se vygeneruji na zacatku kampane.
- Pak zustavaji konstantni.

Pevne vlastnosti NPC zaku mohou zahrnovat:

- sklon zalovat
- sklon priznat se
- sklon kryt druhe
- pamet bez poznamek
- peclivost v poznamkach
- peclivost v noseni pomucek
- tendenci porusovat etiketu

Tyto vlastnosti jsou pro hrace-ucitele zpočatku skryte.
