Python beadandó

Vers Martin

NK: OLLQVS

Diákjegy-kezelő Program

A program egy egyszerű diákjegy-kezelő alkalmazás amivel lehet:

-diák nevének és jegyének felvétele

-diák törlése a listából

-jegyek átlagának kiszámítása 

-adatok mentése fájlba és betöltése fájlból 

Funkciók:

- Diák nevének megadása
- Diák jegyének rögzítése (1–5 közötti szám)
- Adatfelvétel a táblázatba 
- Kijelölt diák törlése
- Jegyek átlagának kiszámítása
- Minden adat menthető egy "students_VM.txt" fájlba
- Bármikor visszatölthető az adatfájl tartalma
- Hibás adatbevitel esetén figyelmeztető üzenet

Saját modul – vm_utils_VM.py

Tartalmazott elemek:

1. Osztály: VMHelper
   - format_student(name, grade)
2. Függvény:
   - validate_VM_student(name, grade_text)
   
Osztály (StudentStorageVM – storage.py):

Az osztály felelős az adatok programon belüli tárolásáért és
a jegyek kezeléséért.

Metódusok:
- add_student(name, grade)
- delete_student(index)
- calculate_average()
- save_to_file()
- load_from_file()

Grafikus felület (GUI – gui.py):