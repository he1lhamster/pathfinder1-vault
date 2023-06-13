---
cssclass: [monsters]
title1: Garuda
desc_short: This winged creature has clawed hands and bird's talons. Large, glinting
  eyes and a serrated beak dominate its avian face.
title2: Garuda
CR: 9
sources:
- name: Bestiary 3
  page: 123
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: Cult of the Ebon Destroyers
  page: 29
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderModules/v5748btpy8ihu
XP: 6400
alignment: CG
size: Medium
type: outsider
subtypes:
- native
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 19
  touch: 15
  flat_footed: 14
  components:
    dex: 5
    natural: 4
HP:
  HP: 115
  long: 11d10+55
saves:
  fort: 8
  ref: 12
  will: 9
DR:
- amount: 10
  weakness: evil or magic
SR: 21
speeds:
  base: 30
  fly: 80
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +16 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 16
    - text: 2 claws +16 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 16
    - text: 2 talons +16 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: talons
      bonus:
      - 16
    - text: 2 wings +11 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 2
      attack: wings
      bonus:
      - 11
  ranged:
  - - text: +1 shock longbow +17/+12/+7 (1d8+4/×3 plus 1d6 electricity)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
        - damage: 1d6
          type: electricity
      attack: +1 shock longbow
      bonus:
      - 17
      - 12
      - 7
  special:
  - hatred
  - swooping pounce
  - talon or wing
spells:
  entries:
  - name: displacement
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: alter self
    source: '?'
    level: 2
  - name: protection from arrows
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: grease
    source: '?'
    level: 1
    DC: 14
  - name: mage armor
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: shocking grasp
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    concentration: 10
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 16
  DEX: 21
  CON: 20
  INT: 15
  WIS: 14
  CHA: 17
BAB: 11
CMB: 14
CMD: 29
feats:
- name: Deadly Aim
- name: Manyshot
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Rapid Shot
- is_bonus: true
  name: Weapon Finesse
skills:
  Acrobatics: 19
  Fly: 23
  Intimidate: 21
  Perception: 20
  Sense Motive: 20
  Spellcraft: 13
  Stealth: 19
  Survival: 13
  _racial_mods:
    Intimidate:
      _: 4
    Perception:
      _: 4
    Sense Motive:
      _: 4
languages:
- Common
- Garuda
ecology:
  environment: tropical hills and mountains
  organization: solitary, pair, or aerie (3-6)
  treasure_type: double
  treasure:
  - +1 shock composite longbow [+3 Str]
  - other treasure
special_abilities:
  Hatred (Ex): Garudas receive a +1 racial bonus on attack and damage rolls against
    nagas and other serpentine monsters of the aberration type.
  Spells: Garudas cast spells as 7th-level sorcerers.
  Swooping Pounce (Ex): When a garuda makes a diving aerial charge, it can make a
    full attack with its natural weapons.
  Talon or Wing (Ex): A garuda cannot use its wing attacks while flying, and cannot
    use its talon attacks while not flying.
desc_long: |-
  Garudas are noble, birdlike creatures that inhabit rugged hills. While they remain detached from humanoid societies, they are impetuous and gallant, often serving as protectors of nearby communities.

  Most garudas stand around 6 feet tall with a wingspan of 15 feet and weigh approximately 150 pounds.

---

# Garuda
This winged creature has clawed hands and bird’s talons. Large, glinting eyes and a serrated beak dominate its avian face.
**Source** Bestiary 3 pg. 123, Cult of the Ebon Destroyers pg. 29
**XP** 6,400

CG Medium outsider (native)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +4 natural)
**hp** 115 (11d10+55)
**Fort** +8, **Ref** +12, **Will** +9
**DR** 10/evil or magic; **SR** 21

##### Offense
**Speed** 30 ft., fly 80 ft. (good)
**Melee** bite +16 (1d6+3), 2 claws +16 (1d4+3), 2 talons +16 (1d4+3), 2 wings +11 (1d4+1)
**Ranged** +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Longbow|longbow]]_ +17/+12/+7 (1d8+4/×3 plus 1d6 electricity)
**Special Attacks** hatred, swooping _[[universal monster rules/Pounce|pounce]]_, talon or wing
**Spells Known **(CL 7th; concentration +10)
3rd (5/day)—_[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Grease|grease]]_ (DC 14), _[[spells/Mage Armor|mage armor]]_, _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 16, **Dex** 21, **Con** 20, **Int** 15, **Wis** 14, **Cha** 17
**Base Atk** +11; **CMB** +14; **CMD** 29
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +19, Fly +23, Intimidate +21, Perception +20, Sense Motive +20, Spellcraft +13, Stealth +19, Survival +13; **Racial Modifiers** +4 Intimidate, +4 Perception, +4 Sense Motive
**Languages** Common, _[[monsters/Garuda|Garuda]]_

##### Ecology

**Environment** tropical hills and mountains
**Organization** solitary, pair, or aerie (3–6)
**Treasure** double (+1 _shock_ _[[items/Weapon/Composite longbow|composite longbow]]_ [+3 Str], other treasure)

### Special Abilities

**Hatred (Ex)** Garudas receive a +1 racial bonus on attack and damage rolls against nagas and other serpentine monsters of the aberration type.
**Spells **Garudas cast spells as 7th-level sorcerers.
**Swooping _Pounce_ (Ex)** When a _garuda_ makes a diving aerial charge, it can make a full attack with its natural weapons.

**Talon or Wing (Ex)** A _garuda_ cannot use its wing attacks while flying, and cannot use its talon attacks while not flying.

##### Description

Garudas are noble, birdlike creatures that inhabit rugged hills. While they remain detached from humanoid societies, they are impetuous and gallant, often serving as protectors of nearby communities.

Most garudas stand around 6 feet tall with a wingspan of 15 feet and weigh approximately 150 pounds.