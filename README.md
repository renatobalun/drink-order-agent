# 🎯 ZADATAK: AI Agent za naručivanje pića i generiranje PDF naloga

**Cilj:** Izraditi AI agenta koji konvertira nestrukturirane narudžbe (tekst/slika) u strukturirani PDF nalog za skladište.

Za primjer PDFa pogledaj u primjerima naloga.

---

## 1. Ulazni podaci (Input)
Agent mora prihvaćati narudžbe putem dva kanala:
1.  **Tekstualna poruka** (slobodan stil).
2.  **Fotografija** (slika rukopisa ili tiskanog papira) – *zahtijeva OCR analizu prije obrade.*

---

## 2. Pravila interpretacije (Poslovna logika)

Agent mora primijeniti sljedeća stroga pravila mapiranja:

### A) Količine
| Simbol | Značenje | Primjer | Rezultat |
| :---: | :--- | :--- | :--- |
| **#** | Puno pakiranje | `Ožujsko #2` | 2 gajbe |
| **x** | Komad (boca/limenka) | `Vodka x2` | 2 boce |
| *(prazno)* | Nepoznato | `Pivo 5` | jedno puno pakiranje |

### B) Ambalaža i Jedinice (Automatsko mapiranje)
Polje **Jedinica** u PDF-u se određuje automatski na temelju tipa ambalaže.
*Format u PDF-u (Ambalaža): Litraža + Vrsta + Pakiranje.*

| Vrsta ambalaže | Automatska Jedinica | Primjer ispravnog zapisa |
| :--- | :--- | :--- |
| **Bačva** | `bačva` | 30L bačva |
| **Staklo** | `gajba` | 0.5L staklo |
| **Limenka** | `paket` | 0.33L limenka |
| **PET** | `paket` | 1.0L PET |
| **Bez ambalaže** | `paket` | (npr. kava) |

### C) Plaćanje
Kupac bira **točno jedan** način (ako nedostaje, agent mora pitati):
* `Virman`, `Gotovina`, `Kartica`, `Bez računa`, `R1`

### D) Razdvajanje podataka (Stavke vs. Opis)
Bitno je razlikovati što ide u tablicu artikala, a što u napomenu.

| Podatak | Gdje se upisuje u PDF-u? |
| :--- | :--- |
| Artikli (pivo, sokovi...) | **Glavna tablica (Stavke)** |
| Povrat ambalaže (prazne gajbe) | **Polje: OPIS** |
| Datum / Vrijeme dostave | **Polje: OPIS** |
| Naziv objekta | **Polje: OPIS** |

---

## 3. Tijek rada (Workflow)

1.  **Zaprimanje:** Korisnik šalje tekst ili sliku.
2.  **Analiza:**
    *   Prepoznavanje artikala i spajanje s bazom (šifra + naziv).
    *   Primjena pravila za količine i ambalažu.
    *   Izdvajanje napomena (opis) i načina plaćanja.
3.  **Pregled (Validacija):** Agent ispisuje strukturirani sažetak korisniku.
4.  **Izmjene (Loop):**
    *   Korisnik može mijenjati *bilo koju* stavku (količinu, ambalažu, brisati artikle).
    *   Agent ponovno generira sažetak nakon svake promjene.
5.  **Finalizacija:** Korisnik upisuje `/posalji`.
6.  **Izlaz:** Generiranje PDF-a.

---

## 4. Specifikacija PDF dokumenta
Dokument za skladište mora sadržavati točno ove stupce/podatke:

*   **Zaglavlje:** Datum, Način plaćanja, Opis
*   **Tablica stavki:**
    1.  Šifra
    2.  Artikl (puni naziv iz baze)
    3.  Količina
    4.  Jedinica (automatski: gajba/bačva/paket)
    5.  Ambalaža (npr. 0.5L staklo)

---

## 5. Komande agenta

*   `/upute` – Ispisuje kratki vodič za format naručivanja.
*   `/posalji` – Zaključava narudžbu i generira PDF.

---

### ✅ Očekivani rezultat (Checklista za studenta)
1.  [ ] Sustav prepoznaje i tekst i slike.
2.  [ ] Logika `#` vs `x` radi ispravno.
3.  [ ] Jedinice mjere (gajba/paket) se dodjeljuju automatski.
4.  [ ] Povrat ambalaže ne ulazi u stavke, već u opis.
5.  [ ] PDF je generiran sa svim potrebnim stupcima.