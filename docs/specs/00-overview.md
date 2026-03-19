# 00 Overview

## Zakladni vize

- Hra je `3D singleplayer` simulator historickeho skolniho zivota.
- Odehrava se v `ceske vesnicke skole` v `Rakousko-Uhersku`.
- Pevny pocatecni rok je `1900`.
- Hlavni herni osy jsou `prospech` a `kazen`.
- Hra ma byt co nejbliz `historicke realite`, ale nektere systemy budou abstrahovane kvuli hratelnosti.

## Volba role

- Na zacatku si hrac vybira, zda bude hrat `zaka`, nebo `ucitele`.
- Soucasne si voli `vzhled avatara`.
- Zvolena role je pro danou kampan `pevna`.

## Herni prostory

- `trida`
- `chodba`
- `byt ucitele`
- `domov zaka`

Poznamky:

- Svet je zamerne `izolovany na skolu`, pripadne `domov`, pokud hrac hraje zaka.
- Byt ucitele je `nepristupny pro zaka`.
- Cesta do skoly a ze skoly je `hratelna`, ale bez volnych interakci s okolim.

## Kampan

- Kampan zaka pokryva `1. az 9. rocnik`.
- Pokud zak `propadne`, celkova delka kampane se prodluzuje.
- Dokonceni rocniku funguje jako `checkpoint`.
- Fyzicka trida zustava stejna, ale `obsah vyuky` se meni podle rocniku.
- Ve tride je priblizne `20 zaku`.
- Jde o `jednorocnikovou tridu`, ne o smisenou malotridku.
- Ve skole je `jeden ucitel`, ktery uci vsechny predmety.
- Ucitel vede `jen jednu tridu`.
- Ucitel je po celou dochazku `stejny`.
- Spoluzaci zustavaji `stale stejni`, maximalne muze nekdo `propadnout`.

## Cas a denni rytmus

- Hra bezi `plynule`, ne po diskretnich dnech jako v tahove hre.
- Vyucovaci hodina ma `45 hernich minut`.
- Kratka prestavka ma `10 hernich minut`.
- Velka prestavka ma `20 hernich minut`.
- Velka prestavka je vzdy `po druhe hodine`.
- Bezny den ma `4 az 6 hodin` podle rocniku.
- Ucitel dostava od hry signal, ze je cas ukoncit hodinu, ale muze ji `pretahnout`.
- Nadmerne pretahovani hodin snizuje `pozornost a prospech zaku`.

## Rozvrh

- Rozvrh je `pevny`.
- Zak dostane `celotydenni rozvrh` prvni den.
- Rozvrh plati cele `pololeti`.
- Na zacatku dalsiho pololeti se muze zmenit.
- Zobrazitelny je `kdykoli`.

## Perspektiva a forma interakce

- Kamera je `ve treti osobe`.
- Vyuha pouziva hlavne `textove volby`, ale hra zustava plynula v prostoru.
- Pro rozhodovani jsou dulezite i `3D animace` a `pozice postav`.

## Historicke mantinely

- Skola je `ceska`.
- Hra se ma opirat o `historicke prameny`.
- Tresty maji zahrnovat i `dobove telesne a ponizujici tresty`.
- Pohlavi ovlivnuje `vzhled`, `osloveni` a potencialne `nabidku predmetu`, ale v prvni verzi se nebudou implementovat pohlavne rozdelene predmety.
