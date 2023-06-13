---
cssclass: [monsters]
title1: Troll, Troll Acolyte
title2: Troll Acolyte
CR: 6
sources:
- name: Monster Codex
  page: 226
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Troll
classes:
- cleric 2
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    deflection: 1
    dex: 1
    natural: 6
    size: -1
HP:
  HP: 92
  long: 8d8+56
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 15
  ref: 3
  will: 8
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +9 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 9
    - text: 2 claws +10 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 10
  special:
  - channel negative energy 3/day (DC 11, 1d6)
  - destructive smite (+1, 4/day)
  - rend (2 claws, 1d6+7)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: storm burst
    source: default
    freq: 4/day
    other: 1d6+1 nonlethal
  sources:
  - name: default
    CL: 2
    concentration: 3
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Cleric
    level: 1
  - superscripts:
    - UC
    name: sun metal
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 11
  - name: detect magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 2
    concentration: 3
    slots:
      0: at-will
    domains:
    - destruction
    - weather
tactics:
  Before Combat: The troll acolyte casts bless on herself and her allies.
  During Combat: The troll acolyte casts divine favor or sun metal, then attacks.
ability_scores:
  STR: 21
  DEX: 12
  CON: 25
  INT: 8
  WIS: 13
  CHA: 10
BAB: 5
CMB: 11
CMD: 23
feats:
- name: Channel Smite
- name: Improved Iron Will
- name: Iron Will
- name: Weapon Focus (claw)
skills:
  Intimidate: 4
  Perception: 7
languages:
- Giant
gear:
  combat:
  - potion of bull's strength
  - potion of invisibility
  other:
  - amulet of natural armor +1
  - ring of protection +1
  - 50 gp
ecology:
  environment: cold mountains
desc_long: A troll acolyte has tested her devotion to a demon lord by searing her
  flesh with acid and fire so it must heal naturally, without regeneration.

---

# Troll, Troll Acolyte

**Source** Monster Codex pg. 226
**XP** 2,400
_[[monsters/Troll|Troll]]_ _[[classes/Cleric|cleric]]_ 2
CE Large humanoid (giant)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +7

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+1 deflection, +1 Dex, +6 natural, –1 size)
**hp** 92 (8d8+56); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +15, **Ref** +3, **Will** +8

##### Offense
**Speed** 30 ft.
**Melee** bite +9 (1d8+5), 2 claws +10 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 3/day (DC 11, 1d6), destructive smite (+1, 4/day), _[[universal monster rules/Rend|rend]]_ (2 claws, 1d6+7)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +3)
4/day—storm burst (1d6+1 nonlethal)
**_Cleric_ Spells Prepared **(CL 2nd; concentration +3)
1st—_[[spells/Bless|bless]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sun Metal|sun metal]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 11), _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_
**D** domain spell; **Domains** _[[spells/Destruction|Destruction]]_, Weather

### Tactics

**Before Combat** The _troll_ _[[npcs/Acolyte|acolyte]]_ casts _bless_ on herself and her allies.
 **During Combat** The _troll_ _acolyte_ casts _divine favor_ or _sun metal_, then attacks.

##### Statistics
**Str** 21, **Dex** 12, **Con** 25, **Int** 8, **Wis** 13, **Cha** 10
**Base Atk** +5; **CMB** +11; **CMD** 23
**Feats** _[[feats/Channel Smite|Channel Smite]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Intimidate +4, Perception +7
**Languages** Giant
**Combat Gear** potion of bull’s strength, potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 50 gp

##### Ecology

**Environment** cold mountains

##### Description

A _troll_ _acolyte_ has tested her devotion to a demon lord by searing her flesh with acid and fire so it must _[[spells/Heal|heal]]_ naturally, without _regeneration_.