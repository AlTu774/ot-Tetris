# Sovelluslogiikka

```mermaid
  classDiagram
      GameLoop "1" --> "1" Stage
      Blocks -- Stage
class GameLoop{
      events()
	}
class Stage{
      add_new_block()
      drop_block()
      move_block(dir)
      freeze_block()
      rotate_block()
      ...
	}
class Blocks{
      generate_random_block()
      move_rotation_b()
	}
```

Luokka GameLoop lukee pelaajan syötettä jota luokka Stage käyttää palikan liikuttamiseen pelikenttänssä.

# Sekvenssikaavio
```mermaid
 sequenceDiagram
 
 	index->>game_loop: events()
	activate game_loop
	game_loop->>stage: move_block(dir)
	deactivate game_loop
	index->>clock: get_ticks()
	activate clock
	clock-->>index: pygame.time.get_ticks()
	deactivate clock
	index->>stage: drop_block()
	index->>renderer: render_stage()
	
```
Sekvenssiokaavio kun palikkaa liikutetaan oikealle tai vasemmalle. Sen lisäksi palikkaa tiputetaan yhden tilan verran kun tarpeeksi aikaa on kulunut.
