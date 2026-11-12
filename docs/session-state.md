# Session State

Tento soubor sleduje, ktera skupina otazek je prave rozpracovana.
Po dokonceni skupiny se stav aktualizuje a commitne.

## Aktualne rozpracovano

**Skupina: Předměty — detaily jednotlivých předmětů**
- Soubor: `docs/specs/08-subjects.md`
- Stav: základní přehled zapsán; detaily jednotlivých předmětů budou probírány dále

## Co uz je v teto vlne uzavreno

- Tresty (fáze 1–3) — kompletní
- Pochvaly
- Archetypy rodičů (základní sada)
- Struktura školy: 5 ročníků obecná škola + 8 ročníků gymnázium + maturita
- Předměty obecné školy a gymnázia — přehled a mechaniky
- Tělocvik — kompletní seznam aktivit, her a rituálů hodiny
- Kampaň učitele — volba školy, konec kampaně, závěrečné hodnocení

## Otevřené otázky z revize spec (2026-11-12)

1. ~~Hodnocení volného textu~~ — uzavřeno (AI hodnocení a vstupy)
2. ~~Kázeň~~ — uzavřeno
3. Podmínka přechodu na gymnázium a pravidla propadnutí — **rozpracováno, čeká na odpověď (otázka 21)**
   - Historické podklady (ověřit v dobových předpisech): přijetí do primy v 10 letech,
     obvykle po 4. (někdy 5.) ročníku obecné školy; povinná přijímací zkouška písemná
     i ústní z náboženství, vyučovacího jazyka a počtů; při dobrém prospěchu na vysvědčení
     obecné školy a v písemné části mohla být ústní zkouška prominuta; při neúspěchu
     nový pokus až další školní rok; gymnázium bylo placené (školné).
   - Varianty k rozhodnutí:
     a) přijímací zkouška podle historie, neúspěch = konec hry s nižším hodnocením
     b) jako a), ale s možností opakovat zkoušku po dalším roce na obecné škole
     c) jako a) + přestup už po 4. ročníku (obecná škola 4 ročníky, celkem 12)
   - Pak navazuje: pravidla propadnutí (kolik nedostatečných, opravné zkoušky).
4. Plynutí času 1:1 vs. délka kampaně (přeskakování prázdných úseků)
5. Jak NPC žáci odpovídají a jak vzniká jejich znalost
6. Drobné nesoulady a duplicity ve spec

## Fronta — detaily předmětů

Předměty, které je potřeba ještě podrobněji specifikovat:
1. Náboženství — obsah katechismu po ročnících (obecná škola + gymnázium)
2. Čeština — typy textů pro diktát, sloh, čtení
3. Počty / Matematika — typy příkladů po ročnících
4. Zeměpis — obsah po ročnících
5. Dějepis — obsah po ročnících
6. Přírodopis — obsah po ročnících
7. Fyzika — obsah po ročnících
8. Latina — rozsah slovní zásoby a gramatiky po ročnících
9. Němčina — obsah po ročnících
10. Geometrie — typy úloh po ročnících

## Dalsi fronta skupin

1. Etiketa
2. Balanc
3. Archetypy rodičů — detaily

## Dokonceno

- Kázeň — výpočet, známka, vyloučení (2026-11-12)
- AI hodnocení, vstupy a rukopis (2026-11-12) - commit `da8c5ae`
- Kampaň učitele — rozsah a konec (2026-11-12) - commit `550e4e4`
- Předměty — přehled a mechaniky (2026-03-21) - commit viz níže
- Pochvaly (2026-03-20) - commit `e45d938`
- Tresty – fáze 3 (2026-03-20) - commit `4c113b5`
- Tresty – fáze 2 (2026-03-20) - commit `2ce99e5`
- Funkcni doplneni specifikace (2026-03-19) - commit `88f6ad1`
- Uvodni zalozeni a synchronizace repozitare - commit `8226dcf`
