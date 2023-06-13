---
cssclass: [monsters]
title1: Undine
desc_short: This blue-haired, blue-skinned man moves with a liquid grace. His ears
  are fin-like, and his hands and feet are webbed.
title2: Undine
CR: 1/2
sources:
- name: Bestiary 2
  page: 275
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 200
race: Undine
classes:
- cleric 1
alignment: N
size: Medium
type: outsider
subtypes:
- native
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    armor: 5
    dex: 2
HP:
  HP: 8
  long: 1d8
saves:
  fort: 1
  ref: 3
  will: 5
resistances:
  cold: 5
speeds:
  base: 30
  other_semicolon: 20 ft. in armor, swim 30 ft.
attacks:
  melee:
  - - text: trident +0 (1d8)
      entries:
      - - damage: 1d8
      attack: trident
      bonus:
      - 0
  ranged:
  - - text: sling +2 (1d4)
      entries:
      - - damage: 1d4
      attack: sling
      bonus:
      - 2
  special:
  - channel positive energy 7/day (DC 12, 1d6)
spell_like_abilities:
  entries:
  - name: hydraulic push
    source: default
    freq: 1/day
  - name: dazing touch
    source: domain
    freq: 6/day
  - name: icicle
    source: domain
    freq: 6/day
    other: 1d6+1 cold damage
  sources:
  - name: default
    CL: 1
    concentration: 3
  - name: domain
    CL: 1
    concentration: 4
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - name: charm person
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    concentration: 4
    slots:
      0: at-will
    domains:
    - charm
    - water
ability_scores:
  STR: 11
  DEX: 14
  CON: 8
  INT: 10
  WIS: 17
  CHA: 14
BAB: 0
CMB: 0
CMD: 12
feats:
- name: Extra Channel
skills:
  Diplomacy: 6
  Knowledge (religion): 4
  Swim: 4
  Perception: 3
languages:
- Aquan
- Common
special_qualities:
- water affinity
ecology:
  environment: any land
  organization: solitary, pair, or gang (3-5)
  treasure_type: NPC Gear
  treasure:
  - scale mail
  - trident
  - other treasure
special_abilities:
  Elemental Affinity (Ex): Undine sorcerers with the elemental (water) bloodline treat
    their Charisma score as 2 points higher for all sorcerer class abilities. Undine
    clerics with the Water domain cast their Water domain powers and spells at +1
    caster level.
desc_long: |-
  Undines are humans whose ancestry includes elemental beings of water, such as marids. This connection with the Plane of Water is most noticeably manifested in their coloration, which tends to mimic that of lakes or oceans-all undines have limpid, blue eyes, and their skin and hair can range from pale blue-white to the 

  deep blue or green of the sea.

---

# Undine
This blue-haired, blue-skinned man moves with a liquid _[[spells/Grace|grace]]_. His ears are fin-like, and his hands and feet are webbed.
**Source** Bestiary 2 pg. 275
**XP** 200
_[[monsters/Undine|Undine]]_ _[[classes/Cleric|cleric]]_ 1

N Medium outsider (native)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +3

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor, +2 Dex)
**hp** 8 (1d8)
**Fort** +1, **Ref** +3, **Will** +5
**Resist** cold 5

##### Offense
**Speed** 30 ft.; 20 ft. in armor, swim 30 ft.
**Melee** _[[items/Weapon/Trident|trident]]_ +0 (1d8)
**Ranged** _[[items/Weapon/Sling|sling]]_ +2 (1d4)
**Special Attacks** channel positive energy 7/day (DC 12, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +3)
1/day—_[[spells/Hydraulic Push|hydraulic push]]_
 **Domain _Spell-Like Abilities_ **(CL 1st; concentration +4)
 6/day—dazing touch
 6/day—icicle (1d6+1 cold damage)
**_Cleric_ Spells Prepared **(CL 1st; concentration +4)
1st—_[[spells/Bless|bless]]_, _[[spells/Charm Person|charm person]]_, _[[spells/Divine Favor|divine favor]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, stabilize
**D **Domain spell; **Domains **Charm, Water

##### Statistics
**Str** 11, **Dex** 14, **Con** 8, **Int** 10, **Wis** 17, **Cha** 14
**Base Atk** +0; **CMB** +0; **CMD** 12
**Feats** _[[feats/Extra Channel|Extra Channel]]_
**Skills** Diplomacy +6, Knowledge (religion) +4, Swim +4
**Languages** Aquan, Common
**SQ** water affinity

##### Ecology

**Environment** any land
**Organization** solitary, pair, or gang (3–5)
**Treasure** NPC gear (_[[items/Armor/Scale mail|scale mail]]_, _trident_, other treasure)

### Special Abilities

**Elemental Affinity (Ex)** _Undine_ sorcerers with the elemental (water) bloodline treat their Charisma score as 2 points higher for all _[[classes/Sorcerer|sorcerer]]_ class abilities. _Undine_ clerics with the Water domain cast their Water domain powers and spells at +1 caster level.

##### Description

Undines are humans whose ancestry includes elemental beings of water, such as marids. This connection with the Plane of Water is most noticeably manifested in their coloration, which tends to _[[monsters/Mimic|mimic]]_ that of lakes or oceans—all undines have limpid, blue eyes, and their skin and hair can range from pale blue-white to the

deep blue or green of the sea.