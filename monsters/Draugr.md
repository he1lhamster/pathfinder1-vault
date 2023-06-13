---
cssclass: [monsters]
title1: Draugr
desc_short: 'This barnacle-encrusted walking corpse looks like a zombie, but is dripping
  with water and gives off a nauseating stench. '
title2: Draugr
CR: 2
sources:
- name: Bestiary 2
  page: 110
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 600
alignment: CE
size: Medium
type: undead
subtypes:
- water
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 14
  touch: 10
  flat_footed: 14
  components:
    armor: 2
    natural: 2
HP:
  HP: 19
  long: 3d8+6
saves:
  fort: 2
  ref: 1
  will: 3
DR:
- amount: 5
  weakness: bludgeoning or slashing
immunities:
- undead traits
resistances:
  fire: 10
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: greataxe +5 (1d12+4/×3 plus nausea)
      entries:
      - - damage: 1d12+4
          crit_multiplier: 3
        - effect: nausea
      attack: greataxe
      bonus:
      - 5
  - - text: slam +5 (1d10+4 plus nausea)
      entries:
      - - damage: 1d10+4
        - effect: nausea
      attack: slam
      bonus:
      - 5
ability_scores:
  STR: 17
  DEX: 10
  CON:
  INT: 8
  WIS: 10
  CHA: 13
BAB: 2
CMB: 5
CMD: 15
feats:
- name: Power Attack
- name: Toughness
skills:
  Climb: 9
  Perception: 6
  Stealth: 6
  Swim: 11
languages:
- Common (cannot speak)
ecology:
  environment: any coastal
  organization: solitary or crew (2-8)
  treasure_type: standard
  treasure:
  - greataxe
  - leather armor
  - other treasure
special_abilities:
  Nausea (Su): A creature that is damaged by a draugr must make a DC 12 Fortitude
    save or be nauseated for 1 round. The save DC is Charisma-based.
desc_long: |-
  Draugr smell of decay and the sea, and drip water wherever they go. These foul beings are usually created when humanoid creatures are lost at sea in regions haunted by evil spirits or necromantic effects. The corpses of these drowned sailors cling fiercely to unlife, attacking any living creatures that intrude upon them. Their attacks smear rancid flesh, rotting seaweed, and swaths of vermin on whatever they hit. 

  In the case of draugr who manifest when an entire ship sinks, these undead usually stay with the wreck of their ship. Some draugr may be found under the control of aquatic necromancers, while others may wander the seas as undead pirates aboard ghost ships.

---

# Draugr
This barnacle-encrusted walking corpse looks like a zombie, but is dripping with water and gives off a nauseating _[[universal monster rules/Stench|stench]]_.

**Source** Bestiary 2 pg. 110
**XP** 600
CE Medium undead (water)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., Perception +6

##### Defense

**AC** 14, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 armor, +2 natural)
**hp** 19 (3d8+6)
**Fort** +2, **Ref** +1, **Will** +3
**DR** 5/bludgeoning or slashing; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 10

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** _[[items/Weapon/Greataxe|greataxe]]_ +5 (1d12+4/×3 plus nausea) or slam +5 (1d10+4 plus nausea)

##### Statistics
**Str** 17, **Dex** 10, **Con** —, **Int** 8, **Wis** 10, **Cha** 13
**Base Atk** +2; **CMB** +5; **CMD** 15
**Feats** _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +9, Perception +6, Stealth +6, Swim +11
**Languages** Common (cannot speak)

##### Ecology

**Environment** any coastal
**Organization** solitary or crew (2–8)
**Treasure** standard (_greataxe_, _[[items/Armor/Leather armor|leather armor]]_, other treasure)

### Special Abilities

**Nausea (Su)** A creature that is damaged by a _[[monsters/Draugr|draugr]]_ must make a DC 12 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Charisma-based.

##### Description

_Draugr_ smell of decay and the sea, and drip water wherever they go. These foul beings are usually created when humanoid creatures are lost at sea in regions haunted by evil spirits or necromantic effects. The corpses of these drowned sailors cling fiercely to unlife, attacking any living creatures that intrude upon them. Their attacks smear rancid flesh, rotting seaweed, and swaths of vermin on whatever they hit.

In the case of _draugr_ who manifest when an entire ship sinks, these undead usually stay with the wreck of their ship. Some _draugr_ may be found under the control of aquatic necromancers, while others may wander the seas as undead pirates aboard _[[monsters/Ghost|ghost]]_ ships.