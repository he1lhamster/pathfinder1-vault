---
cssclass: [monsters]
title1: Gremlin, Vexgit
desc_short: With a head like an angry crustacean, this fierce little insectoid creature
  clacks and rattles with a tiny but solid-looking hammer.
title2: Vexgit
CR: 1
sources:
- name: Bestiary 2
  page: 145
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #19: Howl of the Carrion King'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy8735
XP: 400
alignment: LE
size: Tiny
type: fey
initiative:
  bonus: 1
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 15
  touch: 13
  flat_footed: 14
  components:
    dex: 1
    natural: 2
    size: 2
HP:
  HP: 8
  long: 1d6+5
saves:
  fort: 2
  ref: 3
  will: 3
DR:
- amount: 5
  weakness: cold iron
SR: 12
speeds:
  base: 20
  climb: 20
attacks:
  melee:
  - - text: warhammer +0 (1d4-2/×3)
      entries:
      - - damage: 1d4-2
          crit_multiplier: 3
      attack: warhammer
      bonus:
      - 0
    - text: bite -2 (1d3-2)
      entries:
      - - damage: 1d3-2
      attack: bite
      bonus:
      - -2
  special:
  - speedy sabotage
  - wrecking crew
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: prestidigitation
    source: default
    freq: At will
  - name: rusting grasp
    source: default
    freq: 1/hour
  - name: snare
    source: default
    freq: 1/hour
  sources:
  - name: default
    CL: 1
    concentration: 1
ability_scores:
  STR: 6
  DEX: 13
  CON: 14
  INT: 12
  WIS: 13
  CHA: 11
BAB: 0
CMB: -1
CMD: 7
feats:
- name: Skill Focus (Disable Device)
- is_bonus: true
  name: Toughness
- is_bonus: true
  name: Weapon Finesse
skills:
  Appraise: 2
  Climb: 13
  Craft (traps): 5
  Disable Device: 9
  Knowledge (engineering): 2
  Perception: 5
  Stealth: 13
    in metal or stony areas: 17
    when moving: 9
  _racial_mods:
    Disable Device:
      _: 4
    Stealth:
      in metal or stony areas: 4
      when moving: -4
languages:
- Undercommon
ecology:
  environment: any underground or urban
  organization: solitary, pair, mob (3-12), or infestation (13-20 with 1-3 sorcerers
    of 1st-3rd level, 1 rogue leader of 2nd-4th level, 2-14 trained dire rats, 2-5
    trained venomous snakes, and 1-3 rat swarms)
  treasure_type: standard
  treasure:
  - warhammer
  - other treasure
special_abilities:
  Speedy Sabotage (Su): Vexgits are adept at disassembling machinery, reducing even
    complex devices to trash with shocking speed. When using the Disable Device skill,
    these gremlins treat all devices as being one category simpler for the purposes
    of determining how long it takes to use the skill. Thus, difficult devices count
    as tricky, tricky devices count as simple, and simple devices can be dismantled
    as a free action.
  Wrecking Crew (Su): A group of up to six vexgits can work together to dismantle
    a device. This ability functions like the aid another action, but a single vexgit
    can receive help from up to five other vexgits, granting it up to a +10 bonus
    on its Disable Device check.
desc_long: |-
  Maniacally destructive little brutes, vexgits delight in scrapping and sabotaging the works of larger races. The larger and more complicated the target, the better. While one of these spiteful gremlins might delight in trapping someone behind a door with a jammed lock, loosening the wheels on a carriage, or sneakily removing all the nails from a small boat, it's when groups of vexgits get together that they're truly dangerous. In such instances, the portcullis of a vexgit-infested gatehouse turns into a deadly weapon, while a clock tower becomes an avalanche of gears waiting to topple. Engineers warn apprentices of masterful constructions destroyed by these unruly gremlins, with many blaming their greatest failures on such tiny saboteurs.

  Like most gremlins, vexgits prefer to live underground, but cities and the devices they find there fascinate them, often drawing mobs of the dangerous fey to sewer tunnels and abandoned warehouses.

  Vexgits stand 1-1/2 feet tall and weigh approximately 16 pounds.

---

# Gremlin, Vexgit
With a head like an angry crustacean, this fierce little insectoid creature clacks and rattles with a tiny but solid-looking _[[items/Mundane/Hammer|hammer]]_.
**Source** Bestiary 2 pg. 145, Pathfinder #19: Howl of the Carrion _[[npcs/King|King]]_ pg. 84
**XP** 400

LE Tiny fey
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 15, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 Dex, +2 natural, +2 size)
**hp** 8 (1d6+5)
**Fort** +2, **Ref** +3, **Will** +3
**DR** 5/cold iron; **SR** 12

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** _[[items/Weapon/Warhammer|warhammer]]_ +0 (1d4–2/×3), bite –2 (1d3–2)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** speedy sabotage, wrecking crew
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +1)
At will—_[[spells/Prestidigitation|prestidigitation]]_
1/hour—_[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Snare|snare]]_

##### Statistics
**Str** 6, **Dex** 13, **Con** 14, **Int** 12, **Wis** 13, **Cha** 11
**Base Atk** +0; **CMB** –1; **CMD** 7
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Disable Device), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Appraise +2, _Climb_ +13, Craft (traps) +5, Disable Device +9, Knowledge (engineering) +2, Perception +5, Stealth +13 (+17 in metal or stony areas, +9 when moving); **Racial Modifiers** +4 Disable Device, +4 Stealth in metal or stony areas, –4 Stealth when moving
**Languages** Undercommon

##### Ecology

**Environment** any underground or urban
**Organization** solitary, pair, mob (3–12), or infestation (13–20 with 1–3 sorcerers of 1st–3rd level, 1 _[[classes/Rogue|rogue]]_ leader of 2nd–4th level, 2–14 trained dire rats, 2–5 trained venomous snakes, and 1–3 rat swarms)
**Treasure** standard (_warhammer_, other treasure)

### Special Abilities
**Speedy Sabotage (Su) **Vexgits are adept at disassembling machinery, reducing even complex devices to trash with shocking speed. When using the Disable Device skill, these gremlins treat all devices as being one category simpler for the purposes of determining how long it takes to use the skill. Thus, difficult devices count as tricky, tricky devices count as simple, and simple devices can be dismantled as a free action.

**Wrecking Crew (Su)** A group of up to six vexgits can work together to dismantle a device. This ability functions like the aid another action, but a single vexgit can receive help from up to five other vexgits, granting it up to a +10 bonus on its Disable Device check.

##### Description

Maniacally destructive little brutes, vexgits delight in scrapping and sabotaging the works of larger races. The larger and more complicated the target, the better. While one of these _[[items/Armor Magic Abilities/Spiteful|spiteful]]_ gremlins might delight in trapping someone behind a door with a jammed lock, loosening the wheels on a carriage, or sneakily removing all the nails from a small boat, it’s when groups of vexgits get together that they’re truly dangerous. In such instances, the portcullis of a vexgit-infested gatehouse turns into a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ weapon, while a clock tower becomes an avalanche of gears waiting to topple. Engineers warn apprentices of masterful constructions destroyed by these unruly gremlins, with many blaming their greatest failures on such tiny saboteurs.

Like most gremlins, vexgits prefer to live underground, but cities and the devices they find there fascinate them, often drawing mobs of the dangerous fey to sewer tunnels and abandoned warehouses.

Vexgits stand 1-1/2 feet tall and weigh approximately 16 pounds.