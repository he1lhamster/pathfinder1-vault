---
cssclass: [monsters]
title1: Flea, Mammoth Flea
desc_short: This mammoth flea is size of a horse. Its legs dangle awkwardly from its
  great, swollen body armored entirely in disfigured plates.
title2: Mammoth Flea
CR: 2
sources:
- name: Bestiary 4
  page: 99
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 600
alignment: N
size: Large
type: vermin
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 13
  touch: 13
  flat_footed: 9
  components:
    dex: 3
    dodge: 1
    size: -1
HP:
  HP: 22
  long: 4d8+4
saves:
  fort: 5
  ref: 4
  will: 1
DR:
- amount: 5
  weakness: slashing
immunities:
- disease
- mind-affecting effects
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +4 (1d8+3 plus blood drain and disease)
      entries:
      - - damage: 1d8+3
        - effect: blood drain
        - effect: disease
      attack: bite
      bonus:
      - 4
  special:
  - blood drain (1d2 Con)
  - disease
space: 10
reach: 10
ability_scores:
  STR: 13
  DEX: 17
  CON: 13
  INT:
  WIS: 11
  CHA: 6
BAB: 3
CMB: 6
CMD: 19
feats:
- is_bonus: true
  name: Dodge
skills:
  Acrobatics: 0
    when jumping: 20
  Perception: 0
  _racial_mods:
    Acrobatics:
      when jumping: 20
special_qualities:
- uncanny leap (see giant flea)
ecology:
  environment: temperate forests, hills, mountains, or plains
  organization: solitary, pair, or cluster (3-8)
  treasure_type: none
special_abilities:
  Disease (Ex): Bite-injury; save Fort DC 13; onset 1d3 days; frequency 1 day; effect
    1 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: Mammoth fleas are fierce predators. They require vast amounts of blood
  to survive, though once full, they can survive for months before needing to feed
  again. For this reason, they seek larger prey like cows and horses, and plague agrarian
  communities that raise herd animals. A mammoth flea's bite is excruciatingly painful,
  and leaves behind a raised, ringshaped scar.

---

# Flea, Mammoth Flea
This mammoth flea is size of a _[[monsters/Horse|horse]]_. Its legs dangle awkwardly from its great, swollen body armored entirely in disfigured plates.
**Source** Bestiary 4 pg. 99
**XP** 600

N Large vermin
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +0

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 9 (+3 Dex, +1 dodge, –1 size)
**hp** 22 (4d8+4)
**Fort** +5, **Ref** +4, **Will** +1
**DR** 5/slashing; **Immune** disease, mind-affecting effects

##### Offense
**Speed** 30 ft.
**Melee** bite +4 (1d8+3 plus _[[universal monster rules/Blood Drain|blood drain]]_ and disease)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _blood drain_ (1d2 Con), disease

##### Statistics
**Str** 13, **Dex** 17, **Con** 13, **Int** —, **Wis** 11, **Cha** 6
**Base Atk** +3; **CMB** +6; **CMD** 19
**Feats** _Dodge_
**Skills** Acrobatics +0 (+20 when jumping); **Racial Modifiers** +20 Acrobatics when jumping
**SQ** uncanny leap (see giant flea)

##### Ecology

**Environment** temperate forests, hills, mountains, or plains
**Organization** solitary, pair, or cluster (3–8)
**Treasure** none

### Special Abilities

**Disease (Ex)** Bite—injury; save Fort DC 13; onset 1d3 days; frequency 1 day; effect 1 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

Mammoth fleas are fierce predators. They require vast amounts of blood to survive, though once full, they can survive for months before needing to feed again. For this reason, they seek larger prey like cows and horses, and plague agrarian communities that raise herd animals. A mammoth flea’s bite is excruciatingly painful, and leaves behind a raised, ringshaped scar.