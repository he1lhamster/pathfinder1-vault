---
cssclass: [monsters]
title1: Vydrarch
desc_short: Seeping spines cover the inky scales of this long, sinuous beast, its
  twin serpent heads writhing at the ends of its swaying necks.
title2: Vydrarch
CR: 14
sources:
- name: Magnimar, City of Monuments
  page: 62
  link: http://paizo.com/products/btpy8slp?Pathfinder-Campaign-Setting-Magnimar-City-of-Monuments
XP: 38400
alignment: CE
size: Gargantuan
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 29
  touch: 9
  flat_footed: 26
  components:
    dex: 3
    natural: 20
    size: -4
HP:
  HP: 199
  long: 19d10+95
saves:
  fort: 16
  ref: 14
  will: 12
DR:
- amount: 10
  weakness: magic
immunities:
- poison
- sleep
speeds:
  base: 20
  swim: 60
attacks:
  melee:
  - - text: 2 bites +26 (2d8+10/19-20 plus grab)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: bites
      bonus:
      - 26
    - text: tail slap +23 (2d8+5 plus poison spines)
      entries:
      - - damage: 2d8+5
        - effect: poison spines
      attack: tail slap
      bonus:
      - 23
  special:
  - capsize
  - swallow whole (4d6+15 bludgeoning damage, AC 20, 19 hp)
  - veil of fog
space: 20
reach: 20
reach_other: 30 ft. with bite
ability_scores:
  STR: 30
  DEX: 17
  CON: 20
  INT: 7
  WIS: 22
  CHA: 15
BAB: 19
CMB: 33
CMB_other: +37 grapple
CMD: 46
CMD_other: can't be tripped
feats:
- name: Awesome Blow
- name: Cleave
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Multiattack
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Perception: 23
  Swim: 26
languages:
- Aquan
special_qualities:
- amphibious
ecology:
  environment: temperate oceans
  organization: solitary
  treasure_type: standard
special_abilities:
  Poison Spines (Ex): |-
    A vydrarch is covered in jagged spines that secrete a fatal poison. A creature struck by a vydrarch's tail slap attack or that strikes a vydrarch with a melee weapon without reach, an unarmed strike, or a natural weapon takes 1d6 points of piercing damage and risks being poisoned. Any creature that grapples a vydrarch takes 2d6 points of piercing damage and risks being poisoned each round.

    Vydrarch poison: Spine-injury; save Fort DC 24; frequency 1/round for 4 rounds; effect 1d2 Con, 1d2 Wis; cure 2 consecutive saves. The save DC is Constitution-based.
  Veil of Fog (Su): As a standard action, a vydrarch can produce a bank of fog in
    a 100-foot spread centered on itself. This effect is otherwise identical that
    created by a fog cloud spell.
desc_long: |-
  The terrifying creature known as the vydrarch is most well known among Magnimarians from the famous tales of the legendary paladin Alcaydian Indros battling the beast on the shores of what would become Magnimar. The vydrarch was originally thought to be an entirely unique creature, but in recent years, reports from sailors journeying across the Steaming Sea and the remains of wrecked ships washing ashore have hinted at the existence of other such beasts. Vydrarchs live solely for the thrill of destruction and chaos, but what elder force could have created such a monster is unknown. Their dual heads act in tandem to destroy vessels and devour cargo, but survivors of such attacks claim that the heads can act independently of one another if need be, occasionally talking or even arguing among themselves.

  A vydrarch is 40 feet long from tail to head and weighs 10 tons.

---

# Vydrarch
Seeping spines cover the inky scales of this long, sinuous beast, its twin serpent heads writhing at the ends of its swaying necks.
**Source** Magnimar, City of Monuments pg. 62
**XP** 38,400
CE Gargantuan magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +23

##### Defense

**AC** 29, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+3 Dex, +20 natural, –4 size)
**hp** 199 (19d10+95)
**Fort** +16, **Ref** +14, **Will** +12
**DR** 10/magic; **Immune** poison, sleep

##### Offense
**Speed** 20 ft., swim 60 ft.
**Melee** 2 bites +26 (2d8+10/19–20 plus _[[universal monster rules/Grab|grab]]_), tail slap +23 (2d8+5 plus poison spines)
**Space** 20 ft., **Reach** 20 ft. (30 ft. with bite)
**Special Attacks** _[[universal monster rules/Capsize|capsize]]_, _[[universal monster rules/Swallow Whole|swallow whole]]_ (4d6+15 bludgeoning damage, AC 20, 19 hp), _[[spells/Veil|veil]]_ of fog

##### Statistics
**Str** 30, **Dex** 17, **Con** 20, **Int** 7, **Wis** 22, **Cha** 15
**Base Atk** +19; **CMB** +33 (+37 grapple); **CMD** 46 (can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Perception +23, Swim +26
**Languages** Aquan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** temperate oceans
**Organization** solitary
**Treasure** standard

### Special Abilities

**Poison Spines (Ex)** A _[[monsters/Vydrarch|vydrarch]]_ is covered in jagged spines that secrete a fatal poison. A creature struck by a _vydrarch_’s tail slap attack or that strikes a _vydrarch_ with a melee weapon without reach, an unarmed strike, or a natural weapon takes 1d6 points of piercing damage and risks being poisoned. Any creature that grapples a _vydrarch_ takes 2d6 points of piercing damage and risks being poisoned each round.

_Vydrarch_ poison: Spine—injury; save Fort DC 24; frequency 1/round for 4 rounds; effect 1d2 Con, 1d2 Wis; cure 2 consecutive saves. The save DC is Constitution-based.

**_Veil_ of Fog (Su)** As a standard action, a _vydrarch_ can produce a bank of fog in a 100-foot spread centered on itself. This effect is otherwise identical that created by a _[[spells/Fog Cloud|fog cloud]]_ spell.

##### Description

The terrifying creature known as the _vydrarch_ is most well known among Magnimarians from the famous tales of the legendary _[[classes/Paladin|paladin]]_ Alcaydian Indros battling the beast on the shores of what would become Magnimar. The _vydrarch_ was originally thought to be an entirely unique creature, but in recent years, reports from sailors journeying across the _[[items/Armor Magic Abilities/Steaming|Steaming]]_ Sea and the remains of wrecked ships washing ashore have hinted at the existence of other such beasts. Vydrarchs live solely for the thrill of _[[spells/Destruction|destruction]]_ and chaos, but what elder force could have created such a monster is _[[monsters/Unknown|unknown]]_. Their dual heads act in tandem to destroy vessels and devour cargo, but survivors of such attacks claim that the heads can act independently of one another if need be, occasionally talking or even arguing among themselves.

A _vydrarch_ is 40 feet long from tail to head and weighs 10 tons.