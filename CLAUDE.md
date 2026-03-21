# CLAUDE.md — SchoolSimulator

## Co je tento projekt

3D singleplayer historický simulátor školního života v české vesnické škole v Rakousko-Uhersku kolem roku 1900. Hráč si volí roli žáka nebo učitele. Hlavní osy jsou prospěch a kázeň.

## Struktura spec souborů

| Soubor | Obsah |
|--------|-------|
| `docs/specs/00-overview.md` | Základní vize, světový kontext, herní čas |
| `docs/specs/01-student-campaign.md` | Kampaň za žáka |
| `docs/specs/02-teacher-campaign.md` | Kampaň za učitele |
| `docs/specs/03-assessment-and-discipline.md` | Hodnocení, tresty, pochvaly, systém kázně |
| `docs/specs/04-school-rules-and-etiquette.md` | Školní řád a etiketa |
| `docs/specs/05-ui-data-and-visibility.md` | UI, viditelnost dat |
| `docs/specs/06-open-questions.md` | Otevřené otázky čekající na rozhodnutí |
| `docs/specs/07-npc-characters.md` | Archetypy a vlastnosti NPC postav (rodiče, učitel, spolužáci) |
| `docs/specs/08-subjects.md` | Předměty, jejich mechaniky a obsah tělocviku |

## Jak probíhá Q&A specifikace

- Spec se buduje iterativně přes Q&A konverzace.
- **Vždy jedna otázka najednou** — neklást více otázek v jedné zprávě.
- Po uzavření skupiny témat se zapíše do spec, zaktualizuje `docs/session-state.md` a udělá commit.
- `docs/session-state.md` sleduje, co je hotové a co je ve frontě.

## Konvence

- Spec soubory jsou psány česky.
- Klíčové pojmy jsou uzavřeny do backtick kódu pro snadné vyhledávání.
- Commit messages jsou česky.
- Každý commit pokrývá jednu logickou skupinu změn.
