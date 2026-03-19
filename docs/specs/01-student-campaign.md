# 01 Student Campaign

## Zakladni smycka

- Zak v kampani:
  - vstava doma v `7:00`
  - pripravi se na den
  - jde do skoly
  - absolvuje vyuku a prestavky
  - vraci se domu
  - doma resi ukoly, reakce rodicu, tresty a pochvaly
  - jde spat

## Rano doma

- Ranni domaci faze trva od `7:00`.
- Hraci bezi `60 hernich minut`, ktere muze vyuzit podle sebe.
- Muze:
  - dokoncovat ukol
  - chystat pomucky
  - zpozdit odchod
- Pokud po `8:00` zustava doma:
  - stale musi `manualne odejit`
  - roste riziko, ze ho `rodice pristihnou`
  - roste zpozdeni do skoly
- Ranni dodelavani ukolu je `prohresek`.
- Pokud bude rano pristizen rodici pri dodelavani ukolu, bude `po skole doma potrestan`.

## Cesta do skoly

- Je `hratelna`.
- Hrac nema cestou specialni interakce.
- Cesta sleduje hlavne:
  - `cas`
  - `zpozdeni`
- Zak muze jit i `pozdne`.
- Minuty zpozdeni se pouzivaji pro:
  - vyssi trest ve skole
  - herni prubeh dne
- Pro ucely evidence se pozdni prichod prepocitava na `zameškane hodiny`.
- Evidencne se pocita `cela hodina`.
- Soucasne se interni system opira i o `realne minuty`.

## Prichod do skoly

- Do `8:00` ma byt zak:
  - ve skole
  - na svem miste
  - ve spravne telesne pozici
  - se spravnymi pomuckami
  - s vypracovanymi ukoly
  - se zakovskou knizkou
- Pokud prijde pozde:
  - jde o prohresek
  - snizuje se `kazen`
  - ucitel muze ulozit ruzny trest
  - trest muze mit ruznou intenzitu podle minut zpozdeni

## Chovani v hodine

- Zak:
  - mluvi jen po `vyvolani`
  - dobrovolne vstupuje do vyuky jen `prihlášením`
  - musi `povstat` pri vstupu ucitele
  - musi `povstat`, kdyz je osloven
  - smi si sednout jen na `pokyn ucitele`
  - nesmi bez dovoleni `vstat`
  - nesmi bez dovoleni `opustit misto`
- Prihlaseni:
  - je jediny spravny dobrovolny vstup do vyuky
  - trva maximalne `5 minut`
  - muze byt kdykoli stazeno bez postihu
  - samo o sobe hrace neomezuje v dalsich akcich
- Pohyb zaka bez dovoleni je `fyzicky mozny`, ale zaznamenany jako prohresek (hra ho fyzicky neblokuje).
- Zachod behem hodiny `neni herni mechanika`.

## Pozornost a nepozornost

- Pokud hrac dlouho nic nedela, zak `nedava pozor`.
- Limit pro stav nepozornosti je `60 sekund`.
- Jakakoli akce stav resetuje.
- Zak muze aktivne zvolit:
  - `zasneni`
  - `usnuti`
- Zasneni:
  - je mirnejsi forma nepozornosti
  - omezuje vnimani vyuky
  - ucitel ho vidi, pokud je zak v jeho zornem poli
- Spánek:
  - je aktivni volba
  - prerusi prijem informaci
  - vede k trestu, pokud si ho ucitel vsimne
  - po osloveni ucitelem se zak `automaticky probudi`
  - hrac se muze probudit i sam
  - samovolne probuzeni ma `20 sekund` prodlevu
- U hrace-zaka se ztrata znalosti projevuje hlavne tim, ze hrac sam nevidi a neslysi cast vyuky.
  - pri spanku se zamlzi text a vypnou zvuky

## Poznamky

- Zak ma pro kazdy predmet `vlastni sesit`.
- Sesity jsou `fyzicke predmety v inventari`.
- Lze je `zapomenout doma`.
- Pri vhodnych hodinach je psani poznamek `ocekavany standard`.
- Vyklad ucitele probiha jako `3D animace (ucitel pise na tabuli) + text`. Zak musi obsah manualne opisovat do sesitu.
- Poznamky pise hrac `rucne`. Hra nic automaticky nedoplnuje.
- Zak pozna, zda ma psat poznamky, `sam z kontextu` (bez UI indikace).
- Obsah tabule `zmizi po skonceni vykladu` — zustane jen to, co si zak zapsal do sesitu.
- Poznamky se hodnoti `porovnanim s ocekavanym obsahem` (klicova slova / vety z vykladu).
- Ucitel muze poznamky kontrolovat:
  - hrac-ucitel kdykoli
  - NPC ucitel nahodne
- Chybejici poznamky = `nedostatecna`.
- Poznamky ve spatnem sesite se pri kontrole nepocitaji.
- Zapis do spatneho sesitu se `zjisti az pri kontrole` (zak neni varovaán predem).
- Najednou muze byt otevren `jen jeden sesit`.
- Poznamky lze z chybneho sesitu `prepsat` do spravneho, ale stoji to cas a pozornost.
- Chybejici poznamky lze doplnit `pujcenim sesitu od spoluzaka` (o prestavce nebo doma).

## Domaci ukoly

- Domaci cast je `kazdy skolni den`.
- Ukoly jsou po `predmetech`.
- Aktivni muze byt:
  - maximalne `jeden ukol na predmet`
  - ale vice ukolu napric predmety najednou
- Termin ukolu je vzdy `pristi hodina toho predmetu`.
- Ukol je:
  - `hotovo`
  - `nehotovo`
- V UI neni mezistav.
- Interni rozpracovanost se uklada, ale zobrazuje se jen `0 nebo 100 %`.
- Dokonceni rozpozna hra automaticky, az kdyz jsou vyplneny vsechny pozadovane casti.
- Ukol lze odbýt, neudelat nebo rozpracovat.
- Hrac muze jit spat kdykoli.
- Pokud ukol neudela, druhy den nese nasledky ve skole.

## Opisovani a tahaky

- Zak muze:
  - opisovat ukol o prestavce
  - vytvaret tahaky pred hodinou nebo doma
  - mit vice tahaku naraz
- Opisovat lze `jen od souseda`.
- Soused muze opisovani `odmitnout`.
- Ochota souseda je dana `povahou` a pravdepodobnostnim hodem.
- Opisovani:
  - zabira cas
  - muze byt neuplne
  - lze odevzdat i neuplny opsany ukol
  - pri opisovani ukolu musi zak `rucne prepsat` (copy-paste nefunguje)
- Odhaleni opisovani stoji na:
  - pristizeni
  - nahlaseni
  - priznani
- Nehodnoti se shoda textu.
- Pri pristizeni jsou trestani `oba zaci` (opisujici i ten, od koho se opisovalo).
- Tahak:
  - je predmet v inventari
  - neni trestne ho jen `mit`
  - pouziti je `vzdy prohresek` bez ohledu na typ aktivity (nikdy neni povoleno)
  - vztahuje se vzdy ke konkretnimu predmetu nebo testu
  - po konfiskaci ucitelem je `vracen po vyuce`, pokud zak pride prosit

## Prestavky

- Zak se muze o prestavce volne pohybovat po `tride` a `chodbe`.
- Muze:
  - opisovat ukoly
  - vytvaret tahak
  - chystat pomucky
  - interagovat se spoluzaky textovymi volbami
- Musi se vcas vratit na misto.
- Kdyz ucitel vstoupi:
  - teprve pak se obraci ke tride
  - zak ma kratky cas jeste dobehnout na misto
- Pokud to nestihne a ucitel si toho vsimne, jde o `prohresek`.

## Cesta domu

- Je `hratelna`.
- Znovu sleduje jen:
  - `pohyb`
  - `cas`
- Zak muze zamerne zdrzovat.
- Pozdni prichod domu je samostatny `domaci prohresek`.
- Trest za pozdni prichod zavisi na:
  - delce zpozdeni
  - pricine zpozdeni
- Pozdni prichod po trestu po skole je trestan `prisneji`.

## Domov a rodice

- Rodice jsou dve samostatne entity:
  - `otec`
  - `matka`
- Oba jsou vzdy `doma`.
- Zak muze jednat s kazdym zvlast.
- Rodice maji pevne povahove rysy po celou kampan.
- Povaha rodicu se voli na zacatku kampane formou `celych archetypu` (ne binarnich prepinacu).
- Rodice prohledavaji inventar `nahodne` (ne jen pri konkretni udalosti).
- Schovani veci = staci ji mit v inventari. Fyzicke skryse `neexistuji` — rodice prohledavaji primodlo inventar.
- Rodice detekuji lez jen pres `konkretni dukaz` (knizka, svedek), ne nahodnou pravdepodobnosti.
- Mohou:
  - trestat
  - chvalit
  - ptat se
  - zkoumat zakovskou knizku
  - najit schovane veci
- Dvojity trest od obou rodicu je mozny, ale ma byt `vzacny`.
- Reaguji jen na to, co `vedi`.
- Informace ziskavaji pres:
  - zakovskou knizku
  - vysvedceni
  - poznamky
  - pozdni prichod
  - pozdni prichod domu
  - nalezeni schovanych veci
  - nahodne informovani od ucitele

## Zakovska knizka

- Je `fyzicky predmet v inventari`.
- Zak ji musi nosit `kazdy den`.
- Muze ji schovat.
- Kdyz ji zapomene:
  - je trestan
  - zapis nejde provest primo do ni
  - ucitel si vec muze poznamenat bokem
- Obsahuje:
  - znamky
  - poznamky
  - pochvaly
- Kdyz ji zak ukaze rodicum, vidi `vse`.
- Zakovska knizka `nelze falzifikovat` — veskere zapisy jsou pro zaka nevratne.

## Priznani, lhani a prosby

- Zak se muze:
  - priznat
  - lhat
  - vymlouvat se
  - prosit o zmirneni
  - omluvit se
- Priznani:
  - vede k mirnejsimu trestu
  - pozdni priznani dava mensi ulehu
- Lez:
  - zveda riziko a intenzitu trestu
- Zak muze doma poprosit, aby nemusel ukazovat zakovskou.
- Rodice mohou podle povahy prosbe vyhovet.

## Bedtime

- Zak ma pevny bedtime podle rocniku.
- Navrzeny model:
  - `1. rocnik = 19:30`
  - kazdy dalsi rocnik `+15 minut`
- Bedtime mohou rodice zprisnit:
  - na libovolny pocet dni
  - maximalne `na jeden mesic`
- Po bedtime muze byt vzhuru:
  - tolerovane jen kvuli ukolum
  - a jen pokud s nimi zacal do `5 minut` po prichodu domu nebo po trestu
- Jinak riskuje pristizeni rodici a trest.

## Tresty a reakce zaka

- Zak ma stejny seznam reakci na trest doma i ve skole:
  - prijmout
  - omluvit se
  - prosit o zmirneni
  - vymlouvat se
  - lhat
  - prijmout vinu / poprosit o potrestani
- `Prijmout` je ekvivalent `mlcky prijmout`.
- Vsech 6 reakci je `vzdy dostupnych` bez ohledu na situaci.
- Na jeden trest lze uplatnit `vice reakci za sebou` (omluva → prosba → atd.).
- Zak muze prohresek `priznat proaktivne` jeste pred udelenim trestu.
- Reakce ovlivnuji:
  - intenzitu trestu
  - kazen
- Pokud ma zak velmi vysokou kazen, muze mu byt vyjimecne nabidnuto, aby si `trest zvolil sam`.
- Tuto volbu ma jen u trestu, ktere:
  - uz sam dostal
  - nebo je videl u jineho zaka
- Na volbu ma `1 minutu`.
- Kdyz trest nevybere, vybere ho autorita.

## Ustni zkouseni

- Kratka otazka = zak odpovida `vestoje u sve lavice`.
- Plnohodnotne ustni zkouseni = zak fyzicky `jde NA stupinek` (ne jen k nemu).
- Odpoved je `volny text` (ne vyber z moznosti), casovy limit `30 sekund`.
- Zak dostane znamku za ustni zkouseni `ihned` a vidi ji hned po zkouseni.

## Socialni mechaniky

- Udani spoluzaka — `hrac-zak vidi scenu udani` (ne jen nahly trest).
- Pratelstvi se spoluzaky `nema herni dopad` (kazda interakce je nezavisla).
- Zak muze `sepskat spoluzakovi` bez povoleni — je to prohresek pri pristizeni.
- Pochvala od ucitele = `verejne oznameni` pred celou tridou.

## Absence

- Hrac-zak muze `zamerně zustat doma` (predstírat nemoc). Nahodna nemoc jako udalost neexistuje.
- Prazdniny a svatky jsou `preskoceny` (nejsou hratelne).

## Oslova lavice

- Je separatni lavice `pro jednoho` — nelze delat akce vyzadujici souseda (opisovani, sepskaní).
- Zak musi mit na hlave `Dunce cap` (vizualni ponizeni).
- Poslani na oslovou lavici nastava `ihned po prohresku`, kdykoli behem hodiny.
- Trest trva do konce hodiny, pokud ho ucitel nezrusi drive.

## Ostatni

- Hra lze ulozit `kdykoli`.
- Vychozi rychlost hry = `1:1` (45 hernich minut = 45 realnych minut), nastavitelna.
- Konec skolniho roku je `hratelna scena` (rozd vani vysvedceni, reakce).
- Zak muze zamerně vynechat skolu — system to umoznuje, zak se jednoduze nerozhodne jit.

## Konec kampane

- Zak muze:
  - `propadnout`
  - byt `vyloucen`
- `Kazen 5` znamena `vylouceni`.
- Vylouceni nastava az `po predani vysvedceni`.
- To je `game over`.
