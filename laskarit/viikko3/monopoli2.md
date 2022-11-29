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
     }
     class Pelaaja{
             rahaa
             kadut
     }
     
     Kortti <.. Sattumat_yhteismaat
     Ruutu -- Sattumat_yhteismaat
     Ruutu -- Asemat_laitokset
     Ruutu -- Vankila
     Pelilauta .. Vankila
     Ruutu -- Kadut
     Pelaaja .. Kadut
     
```
