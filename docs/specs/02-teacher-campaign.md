# 02 Teacher Campaign

## Zaklad

- Ucitel hraje `jednu tridu`.
- Jde o `vesnickou skolu`.
- Uci `vsechny predmety` teto tride.
- Ma `byt ucitele`.
- Jeho kampan zacina `den pred prvnim skolnim dnem`.

## Domaci faze ucitele

- Ucitel ma domaci fazi `kazdy den`.
- Neni povinen ji aktivne vyuzit.
- Pokud ji zanedba:
  - muze to zhorsit vyuku
  - ale hra mu neda automaticky tvrdy statovy postih
- Domaci priprava je hlavne:
  - `interni poznamkovy a navrhovy nastroj`
  - nikoli samostatny system bonusu
- Hrac muze mit stejnou pripravu i mimo hru na papire.

## Co dela ucitel doma

- pripravuje konkretni budoucí hodiny
- pripravuje vyklad a okruhy ke zkouseni
- pripravuje konkretni:
  - testy
  - diktaty
  - samostatne prace
  - ukoly
- opravuje pisemne prace
- pracuje s archivem starsich materialu

## Plan hodiny

- Plan hodiny je vazan na `konkretni budouci hodinu v rozvrhu`.
- U jedne hodiny existuje `jeden plan`.
- Hrac se k nemu muze `vracet a upravovat ho`.
- Plan obsahuje hlavne:
  - co chce ucitel predat
  - co chce po zácích vyzkouset
  - konkretni pripraveny obsah pro test/diktat/ukol
- Nejde o povinny pevny scenar cele hodiny.

## Archiv

- Ucitel ma `trvaly archiv` pripravenych materialu.
- Muze:
  - material znovu pouzit
  - upravit ho
  - smazat ho
- Smazani ma mit `potvrzovaci dialog`.

## Opravovani praci

- Testy muze opravovat:
  - doma
  - o prestavkach
  - v hodine, kdyz trida dela samostatnou praci
- Opravovani muze byt `rozlozene na vice dni`.
- Ucitel nemusi vse opravit ihned na dalsi hodinu.

## Vyuka

- Ucitel pri hodine aktivne rozhoduje, co dela.
- Muze volit mezi:
  - vykladem
  - zkousenim
  - testem
  - diktatem
  - samostatnou praci
  - trestanim
  - chodenim po tride a dohledem
- Zkousi jen `jednoho zaka najednou`.
- Během zkouseni muze dynamicky menit obtiznost dalsich otazek.

## Dohled

- Pro hrace-ucitele plati:
  - to, co vidi na obrazovce, je jeho realne `zorne pole`
  - dohled zavisi na `zornem poli a vzdalenosti`
- Muze:
  - chodit po tride
  - stat na miste
- Oboji muze fungovat jako dohled.
- Odhalovani podvadeni se ridí:
  - viditelnosti zaka
  - vzdalenosti od ucitele
- Player-teacher nema dostavat skryte bonusy mimo to, co vidi.

## Pozdní prichody

- Kdyz zak prijde pozde:
  - ucitel voli typ trestu
  - minuty zpozdeni urcuji rozsah intenzity
- Muze:
  - zaka pustit do zbytku hodiny
  - nebo ho fakticky z hodiny vyradit trestem

## Zasedaci poradek

- Ucitel urcuje `konkretni mista` na zacatku roku.
- Tato akce je `hratelna`.
- Pri urcovani vidi o zácích `zakladni profil`.
- Chovani a studijni sklony odhaluje postupne.
- Zasedaci poradek je pak pevny.
- Vyjimkou je `oslovska lavice`.

## Tresty z pohledu ucitele

- Ucitel voli:
  - `typ trestu`
  - `intenzitu`
  - `duvod`
- Duvod a typ trestu jsou oddelene volby.
- Existuje `pevny seznam trestu`.
- Intenzita je ciselna nebo typove specificka.
- Nektere tresty mohou byt bez pevneho limitu, ale:
  - prilis tvrdy trest snizuje `autoritu ucitele`
- Oslovska lavice trva do `konce hodiny`, pokud ji ucitel neukonci drive.
- Zustani po skole je samostatny trest:
  - max `3 hodiny`
  - ucitel muze ulozit i konkretni cinnost

## Poznamka

- `Poznamka` je samostatny `typ trestu`.
- Muze byt:
  - jedinym trestem
  - nebo soucasti kombinace s dalsim trestem

## Pochvala

- Pochvala je samostatna jedina udalost.
- Nema intenzitu.
- Ma pevny duvod z pevneho seznamu.

## Zapisy a evidence

- Ucitel pracuje hlavne s:
  - `tridni knihou`
  - `zakovskou knizkou`
- Zakovska knizka je primarni misto zapisu pro:
  - znamky
  - poznamky
  - pochvaly
- Hra to nasledne propise do evidence.
- Kdyz zak knizku nema:
  - hrac-ucitel si musi pamatovat a zapsat bokem sam
  - NPC ucitel zapisuje bokem automaticky
- NPC ucitel vse zapisuje `okamzite`.
- Po potvrzeni je kazdy zapis `nevratny`.
- Pred potvrzenim existuje `nahled`.

## Tridni kniha

- Je to `UI obrazovka`, ne fyzicky predmet.
- Obsahuje:
  - seznam zaku
  - dochazku po hodinach
  - znamky
  - historii prohresku
  - ulozene tresty
  - pochvaly
  - navrh znamky z kazne
- Dochazka se vyhodnocuje `automaticky`.
- Ucitel ji `nemuze rucne opravovat`.
- Zaznamenava se do ni vsechny tresty udelene ucitelem, i `po skole`.

## Znamkovani

- Ucitel rucne zapisuje znamky.
- Pocty se skladaji z vice druhu aktivit.
- Ucitel muze menit vahy konkretni aktivity pri tvorbe konkretniho testu nebo zkouseni.
- Na konci pololeti:
  - hra ukaze podklady
  - ucitel vidi prumer
  - ucitel zada vyslednou znamku rucne
- Ucitel muze volit mezi:
  - `rounddown(prumer)`
  - `roundup(prumer)`

## Kazen

- Hrac-ucitel vidi u zaka `navrh znamky z kazne`, ne skryte body.
- Znamku z kazne zadava `rucne`.
- Stejne tak muze i `nespravedlive pritvrdit`.
- Nespravedlive tvrde hodnoceni zhorsuje chovani a duveru tridy.

## NPC zaci

- Hrac-ucitel nevidi jejich skryte vlastnosti.
- Musi je odhalovat:
  - pozorovanim
  - oficialni evidenci
  - vlastni pameti
- Hra nebude obsahovat soukromy zapisnik ucitele o jednotlivych zácích.

## Podminka selhani

- Game over pro ucitele nastava, pokud `propadnou vsichni zaci`.
