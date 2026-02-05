SCHEMA BAZE
tablica drinks sa stupcima šifra i naziv
spremati svaku narudžbu u bazu? 
tablica orders, stupac šifra narudžbe automatski generirana, stupac drinks sa poljem svih pica narucenih,
stupac created_at, stupac updated_at

FLOW
preko rute se zaprima narudzba preko slike ili teksta
ide analiza
prvo ide interpretacija ulaznih podataka koji se ispisuju
ide se u bazu sa tim podacima, dohvacaju se sifre i ispravni nazivi pica u narudzbi
ispisivanje sazetka
cijelo vrijeme korisnik moze dodavati jos pica pa onda ide sve ispocetka
