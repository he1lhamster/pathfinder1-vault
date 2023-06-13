---
cssclass: [monsters]
title1: Crypt Thing
desc_short: 'Shreds of leathery flesh cling to this skeletal figure's body, while
  twin motes of fiery light glow deep in its eye sockets. '
title2: Crypt Thing
CR: 5
sources:
- name: Bestiary 2
  page: 60
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 1600
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: fear
  radius: 10
  other:
  - frightened for 1d4 rounds
  DC: 16
  DC_type: Will
AC:
  AC: 19
  touch: 13
  flat_footed: 16
  components:
    dex: 2
    dodge: 1
    natural: 6
HP:
  HP: 52
  long: 8d8+16
saves:
  fort: 4
  ref: 6
  will: 8
defensive_abilities:
- channel resistance +2
DR:
- amount: 10
  weakness: bludgeoning or magic
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +10 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: claws
      bonus:
      - 10
  special:
  - teleporting burst
spell_like_abilities:
  entries:
  - name: quickened dimension door
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 8
    concentration: 10
ability_scores:
  STR: 19
  DEX: 14
  CON:
  INT: 13
  WIS: 14
  CHA: 15
BAB: 6
CMB: 10
CMD: 23
feats:
- name: Alertness
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Bluff: 6
  Intimidate: 13
  Knowledge (arcana): 6
  Knowledge (dungeoneering): 5
  Knowledge (history): 3
  Perception: 15
  Sense Motive: 15
  Stealth: 9
languages:
- Common
ecology:
  environment: any underground
  organization: solitary
  treasure_type: standard
special_abilities:
  Teleporting Burst (Su): Once per day, a crypt thing can teleport all creatures within
    50 feet of it to randomly determined locations. The crypt thing can only affect
    creatures of which it is aware and to which it has line of sight. A successful
    DC 16 Will save negates this effect. An affected creature is teleported in a random
    direction (roll 1d8, with 1 indicating north and the other numbers indicating
    compass going clockwise) and a random distance (1d10 × 100 feet) away from the
    crypt thing; determine each creature's direction randomly. A teleported creature
    arrives in the closest open space to the determined destination, but must appear
    on a solid surface capable of supporting its weight. If there is no appropriate
    destination in that direction, the creature does not teleport at all. The save
    DC is Charisma-based.
desc_long: |-
  Crypt things are undead creatures found guarding tombs, graves, and crypts. Necromancers and other spellcasters create them to guard such areas, and the crypt things never leave their appointed lairs, even to pursue enemies. Their warded area may be a single room or passage, an entire grave complex, or even a city-sized necropolis. Though naturally solitary, multiple crypt things may guard a common area, often in conjunction with constructs or other undead. 

  A crypt thing only initiates combat if it is attacked or if the object or crypt it is guarding is touched or entered. Until this condition is met, a crypt thing is content to remain motionless-it may even answer questions or otherwise interact with visitors if its master has directed it to do so. Rumors exist of variant crypt things that do not teleport their foes, but instead paralyze opponents and turn them invisible, leaving victims to helplessly watch their allies being torn apart by the angry guardian.

---

# Crypt Thing
Shreds of leathery flesh cling to this skeletal figure’s body, while twin motes of fiery light glow deep in its eye sockets.

**Source** Bestiary 2 pg. 60
**XP** 1,600

NE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15
**Aura** _[[universal monster rules/Fear|fear]]_ (10 ft., _[[conditions/Frightened|frightened]]_ for 1d4 rounds, Will DC 16 negates)

##### Defense

**AC** 19, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 52 (8d8+16)
**Fort** +4, **Ref** +6, **Will** +8
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **DR** 10/bludgeoning or magic; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +10 (1d8+4)
**Special Attacks** teleporting burst
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +10)
3/day—quickened _[[spells/Dimension Door|dimension door]]_

##### Statistics
**Str** 19, **Dex** 14, **Con** —, **Int** 13, **Wis** 14, **Cha** 15
**Base Atk** +6; **CMB** +10; **CMD** 23
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Bluff +6, Intimidate +13, Knowledge (arcana) +6, Knowledge (dungeoneering) +5, Knowledge (history) +3, Perception +15, Sense Motive +15, Stealth +9
**Languages** Common

##### Ecology

**Environment** any underground
**Organization** solitary
**Treasure** standard

### Special Abilities

**Teleporting Burst (Su) **Once per day, a _[[monsters/Crypt Thing|crypt thing]]_ can teleport all creatures within 50 feet of it to randomly determined locations. The _crypt thing_ can only affect creatures of which it is aware and to which it has line of sight. A successful DC 16 Will save negates this effect. An affected creature is teleported in a random direction (roll 1d8, with 1 indicating north and the other numbers indicating _[[items/Mundane/Compass|compass]]_ going clockwise) and a random distance (1d10 × 100 feet) away from the _crypt thing_; determine each creature’s direction randomly. A teleported creature arrives in the closest open space to the determined destination, but must appear on a solid surface capable of supporting its weight. If there is no appropriate destination in that direction, the creature does not teleport at all. The save DC is Charisma-based.

##### Description

Crypt things are undead creatures found _[[items/Armor Magic Abilities/Guarding|guarding]]_ tombs, graves, and crypts. Necromancers and other spellcasters create them to _[[npcs/Guard|guard]]_ such areas, and the crypt things never leave their appointed lairs, even to pursue enemies. Their warded area may be a single room or passage, an entire grave complex, or even a city-sized necropolis. Though naturally solitary, multiple crypt things may _guard_ a common area, often in conjunction with constructs or other undead.

A _crypt thing_ only initiates combat if it is attacked or if the object or crypt it is _guarding_ is touched or entered. Until this condition is met, a _crypt thing_ is content to remain motionless—it may even answer questions or otherwise interact with visitors if its master has directed it to do so. Rumors exist of variant crypt things that do not teleport their foes, but instead paralyze opponents and turn them _[[conditions/Invisible|invisible]]_, leaving victims to helplessly watch their allies being torn apart by the angry _[[items/Weapon Magic Abilities/Guardian|guardian]]_.