```mermaid
  classDiagram
     Pelilauta "1" -- "2..8" Pelaaja
     Pelilauta "1" -- "40" Ruutu
     class Pelilauta{
            aloitusruutu
            vankila
     }
     class Ruutu{
             tyyppi
             nimi
     }
     Kortti <-- Ruutu
