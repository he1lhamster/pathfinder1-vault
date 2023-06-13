---
cssclass: [monsters]
title1: Ghoul
desc_short: This humanoid creature has long, sharp teeth, and its pallid flesh is
  stretched tightly over its starved frame.
title2: Ghoul
CR: 1
sources:
- name: Pathfinder RPG Bestiary
  page: 146
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 400
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 14
  touch: 12
  flat_footed: 12
  components:
    dex: 2
    natural: 2
HP:
  HP: 13
  long: 2d8+4
saves:
  fort: 2
  ref: 2
  will: 5
defensive_abilities:
- channel resistance +2
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +3 (1d6+1 plus disease and paralysis)
      entries:
      - - damage: 1d6+1
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 3
    - text: 2 claws +3 (1d6+1 plus paralysis)
      entries:
      - - damage: 1d6+1
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 3
  special:
  - paralysis (1d4+1 rounds, DC 13, elves are immune to this effect)
ability_scores:
  STR: 13
  DEX: 15
  CON:
  INT: 13
  WIS: 14
  CHA: 14
BAB: 1
CMB: 2
CMD: 14
feats:
- name: Weapon Finesse
skills:
  Acrobatics: 4
  Climb: 6
  Perception: 7
  Stealth: 7
  Swim: 3
languages:
- Common
ecology:
  environment: any land
  organization: solitary, gang (2-4), or pack (7-12)
  treasure_type: standard
special_abilities:
  Disease (Su): 'Ghoul Fever: Bite-injury; save Fort DC 13; onset 1 day; frequency
    1/day; effect 1d3 Con and 1d3 Dex damage; cure 2 consecutive saves. The save DC
    is Charisma-based. A humanoid who dies of ghoul fever rises as a ghoul at the
    next midnight. A humanoid who becomes a ghoul in this way retains none of the
    abilities it possessed in life. It is not under the control of any other ghouls,
    but it hungers for the flesh of the living and behaves like a normal ghoul in
    all respects. A humanoid of 4 Hit Dice or more rises as a ghast.'
desc_long: |-
  Ghouls are undead that haunt graveyards and eat corpses. Legends hold that the first ghouls were either cannibalistic humans whose unnatural hunger dragged them back from death or humans who in life fed on the rotting remains of their kin and died (and were reborn) from the foul disease-the true source of these undead scavengers is unclear.

  Ghouls lurk on the edges of civilization (in or near cemeteries or in city sewers) where they can find ample supplies of their favorite food. Though they prefer rotting bodies and often bury their victims for a while to improve their taste, they eat fresh kills if they are hungry enough. Though most surface ghouls live primitively, rumors speak of ghoul cities deep underground led by priests who worship ancient cruel gods or strange demon lords of hunger. These “civilized” ghouls are no less horrific in their eating habits, and in fact the concept of a well-laid ghoul banquet table is perhaps even more horrifying than the concept of taking a meal fresh from the coffin.

---

# Ghoul
This humanoid creature has long, sharp teeth, and its pallid flesh is stretched tightly over its starved frame.
**Source** Pathfinder RPG Bestiary pg. 146
**XP** 400
CE Medium undead
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +7

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 natural)
**hp** 13 (2d8+4)
**Fort** +2, **Ref** +2, **Will** +5
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2

##### Offense
**Speed** 30 ft.
**Melee** bite +3 (1d6+1 plus disease and _[[universal monster rules/Paralysis|paralysis]]_) and 2 claws +3 (1d6+1 plus _paralysis_)
**Special Attacks** _paralysis_ (1d4+1 rounds, DC 13, elves are immune to this effect)

##### Statistics
**Str** 13, **Dex** 15, **Con** —, **Int** 13, **Wis** 14, **Cha** 14
**Base Atk** +1; **CMB** +2; **CMD** 14
**Feats** _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +4, _[[universal monster rules/Climb|Climb]]_ +6, Perception +7, Stealth +7, Swim +3
**Languages** Common

##### Ecology

**Environment** any land
**Organization** solitary, gang (2–4), or pack (7–12)
**Treasure** standard

### Special Abilities

**Disease (Su)** _[[diseases/Ghoul Fever|Ghoul Fever]]_: Bite—injury; save Fort DC 13; onset 1 day; frequency 1/day; effect 1d3 Con and 1d3 Dex damage; cure 2 consecutive saves. The save DC is Charisma-based. A humanoid who dies of _ghoul fever_ rises as a _[[monsters/Ghoul|ghoul]]_ at the next midnight. A humanoid who becomes a _ghoul_ in this way retains none of the abilities it possessed in life. It is not under the control of any other ghouls, but it hungers for the flesh of the living and behaves like a normal _ghoul_ in all respects. A humanoid of 4 Hit Dice or more rises as a ghast.

##### Description

Ghouls are undead that haunt graveyards and eat corpses. Legends hold that the first ghouls were either cannibalistic humans whose unnatural hunger dragged them back from death or humans who in life fed on the rotting remains of their kin and died (and were reborn) from the foul disease—the true source of these undead scavengers is unclear.

Ghouls lurk on the edges of civilization (in or near cemeteries or in city sewers) where they can find ample supplies of their favorite food. Though they prefer rotting bodies and often bury their victims for a while to improve their taste, they eat fresh kills if they are hungry enough. Though most surface ghouls live primitively, rumors speak of _ghoul_ cities deep underground led by priests who worship ancient _[[items/Weapon Magic Abilities/Cruel|cruel]]_ gods or strange demon lords of hunger. These “civilized” ghouls are no less horrific in their eating habits, and in fact the concept of a well-laid _ghoul_ banquet table is perhaps even more horrifying than the concept of taking a meal fresh from the coffin.