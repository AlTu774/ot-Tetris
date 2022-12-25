# Tetris
Peli jossa liikutetaan tippuvia palikoita ja kerätään pisteitä muodostamalla niistä vaakasuoria rivejä kentän pohjalle.

## Käyttöohjeet
1. Asenna riippuvuudet komennolla: 
```bash 
poetry install
```
2. Käynnistä peli komennolla: 
```bash
poetry run invoke start
```
### Miten peliä pelataan:
- Pelissä palikoita voidaan liikutella oikealle tai vasemmalle nuolinäppäimillä.
- Kun painaa ylös -nuolinäppäintä, palikka kääntyy.
- Alas -nuolinäppäintä pohjaan painamalla palikka tippuu nopeammin.
- Painamalla x -näppäintä palikan voi vaihtaa talteen "hold" -kenttään.
- Game over -ruudussa halutun vaihtoehdon voi vahvistaa painamalla enter -näppäintä.

### Miten peliä testataan:
Peliä testataan komennolla:
```bash
poetry run invoke test
```
Testikattavuusraportin saa komennolla:
```bash
poetry run invoke coverage-report
```
Pylint tarkistukset voi suorittaa komennolla:
```bash
poetry run invoke lint
```
## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
