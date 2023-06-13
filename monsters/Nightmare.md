---
cssclass: [monsters]
title1: Nightmare
desc_short: This eerie horse-like creature's skin is an inky blackness. Fire spurts
  from its hair and nostrils, and its hooves spray sparks.
title2: Nightmare
CR: 5
sources:
- name: Pathfinder RPG Bestiary
  page: 216
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 1600
alignment: NE
size: Large
type: outsider
subtypes:
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 11
  flat_footed: 17
  components:
    dex: 2
    natural: 8
    size: -1
HP:
  HP: 51
  long: 6d10+18
saves:
  fort: 8
  ref: 7
  will: 3
speeds:
  base: 40
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +9 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: bite
      bonus:
      - 9
    - text: 2 hooves +4 (1d6+2 plus 1d4 fire)
      entries:
      - - damage: 1d6+2
        - damage: 1d4
          type: fire
      count: 2
      attack: hooves
      bonus:
      - 4
  special:
  - smoke
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: plane shift
    source: default
    freq: 1/day (self plus 1 rider only)
  sources:
  - name: default
    CL: 6
ability_scores:
  STR: 18
  DEX: 15
  CON: 16
  INT: 13
  WIS: 13
  CHA: 12
BAB: 6
CMB: 11
CMD: 23
CMD_other: 27 vs. trip
feats:
- name: Alertness
- name: Improved Initiative
- name: Run
skills:
  Fly: 13
  Intimidate: 10
  Knowledge (planes): 10
  Perception: 12
  Sense Motive: 12
  Stealth: 7
  Survival: 10
languages:
- Abyssal
- Infernal
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: none
special_abilities:
  Smoke (Su): In battle, a nightmare exhales smoke that chokes and blinds foes, filling
    a 15-foot cone each round as a free action. Anyone in the cone must succeed on
    a DC 16 Fortitude save or become sickened until 1d6 minutes after leaving the
    area. This smoke acts as obscuring mist for the purposes of concealment. The smoke
    persists for 1 round. The save DC is Constitution-based.
desc_long: |-
  Nightmares are flaming harbingers of death. They allow only the most evil of creatures to ride them, and are never mere mounts, but rather willing partners in destruction.

  The cauchemar is a more dangerous variant of the nightmare, particularly valued for its ability to enter the Ethereal Plane with its rider in addition to being able to use plane shift to invade other realities.

---

# Nightmare
This eerie horse-like creature’s skin is an inky blackness. Fire spurts from its hair and nostrils, and its hooves spray sparks.
**Source** Pathfinder RPG Bestiary pg. 216
**XP** 1,600

NE Large outsider (evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 19, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +8 natural, –1 size)
**hp** 51 (6d10+18)
**Fort** +8, **Ref** +7, **Will** +3

##### Offense
**Speed** 40 ft., fly 90 ft. (good)
**Melee** bite +9 (1d4+4), 2 hooves +4 (1d6+2 plus 1d4 fire)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** smoke
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th)
1/day (self plus 1 rider only)—_[[spells/Plane Shift|plane shift]]_

##### Statistics
**Str** 18, **Dex** 15, **Con** 16, **Int** 13, **Wis** 13, **Cha** 12
**Base Atk** +6; **CMB** +11; **CMD** 23 (27 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Improved Initiative|Improved Initiative]]_, Run
**Skills** Fly +13, Intimidate +10, Knowledge (planes) +10, Perception +12, Sense Motive +12, Stealth +7, Survival +10
**Languages** Abyssal, Infernal

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** none

### Special Abilities
**Smoke (Su)** In battle, a _[[spells/Nightmare|nightmare]]_ exhales smoke that chokes and blinds foes, filling a 15-foot cone each round as a free action. Anyone in the cone must succeed on a DC 16 Fortitude save or become _[[conditions/Sickened|sickened]]_ until 1d6 minutes after leaving the area. This smoke acts as _[[spells/Obscuring Mist|obscuring mist]]_ for the purposes of concealment. The smoke persists for 1 round. The save DC is Constitution-based.

##### Description

Nightmares are _[[items/Weapon Magic Abilities/Flaming|flaming]]_ harbingers of death. They allow only the most evil of creatures to ride them, and are never mere mounts, but rather willing partners in _[[spells/Destruction|destruction]]_.

The cauchemar is a more dangerous variant of the _nightmare_, particularly valued for its ability to enter the Ethereal Plane with its rider in addition to being able to use _plane shift_ to invade other realities.