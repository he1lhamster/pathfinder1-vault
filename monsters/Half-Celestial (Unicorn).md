---
cssclass: [monsters]
title1: Half-Celestial (Unicorn)
desc_short: A winged unicorn rises into the air on ivory pinions, a paragon of grace
  and beauty.
title2: Half-Celestial (Unicorn)
CR: 4
sources:
- name: Pathfinder RPG Bestiary
  page: 169
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 1200
alignment: CG
size: Large
type: outsider
subtypes:
- native
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: magic circle against evil
AC:
  AC: 17
  touch: 13
  flat_footed: 13
  components:
    dex: 4
    natural: 4
    size: -1
    deflection vs. evil: 2
HP:
  HP: 42
  long: 4d10+20
saves:
  fort: 9
  ref: 8
  will: 8
  other: +4 vs. poison
DR:
- amount: 5
  weakness: magic
immunities:
- charm
- compulsion
- disease
- poison
resistances:
  acid: 10
  cold: 10
  electricity: 10
SR: 15
speeds:
  base: 60
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: gore +10 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: gore
      bonus:
      - 10
    - text: 2 hooves +7 (1d3+3)
      entries:
      - - damage: 1d3+3
      count: 2
      attack: hooves
      bonus:
      - 7
  special:
  - smite evil 1/day (+7 attack, +4 damage)
  - powerful charge (gore, 2d8+12)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: protection from evil
    source: default
    freq: 3/day
  - name: aid
    source: default
    freq: 1/day
  - name: bless
    source: default
    freq: 1/day
  - name: cure moderate wounds
    source: default
    freq: 1/day
  - name: greater teleport
    source: default
    freq: 1/day
    other: within its territory*
  - name: neutralize poison
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
ability_scores:
  STR: 22
  DEX: 19
  CON: 20
  INT: 13
  WIS: 25
  CHA: 26
BAB: 4
CMB: 11
CMD: 25
CMD_other: 29 vs. trip
feats:
- name: Multiattack
- name: Weapon Focus (horn)
skills:
  Acrobatics: 11
  Fly: 13
  Knowledge (planes): 5
  Perception: 14
  Sense Motive: 14
  Stealth: 11
  Survival: 14
    forests: 17
  _racial_mods:
    Survival:
      in forests: 3
    Stealth:
      _: 4
languages:
- Common
- Sylvan
special_qualities:
- magical strike
- wild empathy +18
ecology:
  environment: temperate forests
  organization: solitary, mated pair, or blessing (3-6)
  treasure_type: none
desc_long: '*Unicorn abilityDescriptionMost half-celestials are born of a mortal who
  loved a good outsider, but powerful holy magic can also create one.'

---

# Half-Celestial (Unicorn)
A winged _[[monsters/Unicorn|unicorn]]_ rises into the air on ivory pinions, a paragon of _[[spells/Grace|grace]]_ and beauty.
**Source** Pathfinder RPG Bestiary pg. 169
**XP** 1,200

CG Large outsider (native)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +14
**Aura** _[[spells/Magic Circle against Evil|magic circle against evil]]_*

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+4 Dex, +4 natural, –1 size; +2 deflection vs. evil)
**hp** 42 (4d10+20)
**Fort** +9, **Ref** +8, **Will** +8; +4 vs. poison
**DR** 5/magic; **Immune** charm, compulsion, disease, poison; **Resist** acid 10, cold 10, electricity 10; **SR** 15

##### Offense
**Speed** 60 ft., fly 120 ft. (good)
**Melee** gore +10 (1d8+6), 2 hooves +7 (1d3+3)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** smite evil 1/day (+7 attack, +4 damage), _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d8+12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
At will—_[[spells/Detect Evil|detect evil]]_, light
3/day—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Protection From Evil|protection from evil]]_
1/day—aid, _[[spells/Bless|bless]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, greater teleport (within its territory*), _[[spells/Neutralize Poison|neutralize poison]]_

##### Statistics
**Str** 22, **Dex** 19, **Con** 20, **Int** 13, **Wis** 25, **Cha** 26
**Base Atk** +4; **CMB** +11; **CMD** 25 (29 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (horn)
**Skills** Acrobatics +11, Fly +13, Knowledge (planes) +5, Perception +14, Sense Motive +14, Stealth +11, Survival +14 (+17 forests); **Racial Modifiers** +3 Survival in forests, +4 Stealth
**Languages** Common, Sylvan
**SQ** magical strike*, wild _[[feats/Empathy|empathy]]_ +18*

##### Ecology

**Environment** temperate forests
**Organization** solitary, mated pair, or blessing (3–6)
**Treasure** none
*_Unicorn_ ability

##### Description

Most half-celestials are born of a mortal who loved a good outsider, but powerful holy magic can also create one.