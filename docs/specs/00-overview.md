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

- Kampaň žáka se skládá ze dvou fází:
  - **Obecná škola**: `5 ročníků`, věk žáka 6–10 let
  - **Gymnázium**: `8 ročníků`, věk žáka 11–18 let
- Celkem `13 ročníků`.
- Přechod na gymnázium závisí na prospěchu — žák s nedostatečnými výsledky na gymnázium nenastoupí.
- Nedokončení obecné školy bez přechodu na gymnázium je platný konec hry s nižším hodnocením — není to game over.
- Žák může na gymnáziu propadnout nebo být vyloučen — tím hra končí předčasně.
- Gymnázium je jiná škola: jiná budova, jiný učitel, jiné předměty, stejná herní jádro (tresty, pochvaly, úkoly, prospěch).
- Maturita na konci gymnázia je zvláštní herní událost — vyvrcholení hry.
- Pokud zak `propadne`, celkova delka kampane se prodluzuje.
- Dokonceni rocniku funguje jako `checkpoint`.
- Fyzicka trida zustava stejna v ramci kazde faze, ale `obsah vyuky` se meni podle rocniku.
- Ve tride je priblizne `20 zaku`.
- Jde o `jednorocnikovou tridu`, ne o smisenou malotridku.
- Ve skole je `jeden ucitel`, ktery uci vsechny predmety.
- Ucitel vede `jen jednu tridu`.
- Ucitel je po celou dochazku v ramci kazde faze `stejny`.
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
