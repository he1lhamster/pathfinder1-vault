---
cssclass: [monsters]
title1: Giant, Rune Giant
desc_short: This giant's skin is black and pitted, like roughly cast iron, and etched
  with glowing red runes.
title2: Rune Giant
CR: 17
sources:
- name: Bestiary 2
  page: 130
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #6: Spires of Xin-Shalast'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy817c
XP: 102400
alignment: LE
size: Gargantuan
type: humanoid
subtypes:
- giant
initiative:
  bonus: 0
senses:
  low-light vision: true
AC:
  AC: 30
  touch: 6
  flat_footed: 30
  components:
    armor: 9
    natural: 15
    size: -4
HP:
  HP: 270
  long: 20d8+180
saves:
  fort: 15
  ref: 6
  will: 20
immunities:
- cold
- electricity
- fire
speeds:
  base: 35
  base_other: 50 ft. without armor
  other_semicolon: air walk
attacks:
  melee:
  - - text: mwk longsword +27/+22/+17 (4d6+22/17-20)
      entries:
      - - damage: 4d6+22
          crit_range: 17-20
      attack: mwk longsword
      bonus:
      - 27
      - 22
      - 17
  - - text: 2 slams +26 (2d6+15)
      entries:
      - - damage: 2d6+15
      count: 2
      attack: slams
      bonus:
      - 26
  ranged:
  - - text: mwk spear +12/+7/+2 (4d6+15/×3)
      entries:
      - - damage: 4d6+15
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 12
      - 7
      - 2
  special:
  - command giants
  - runes
  - spark shower
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: charm person
    source: default
    freq: At will
    DC: 15
  - name: suggestion
    source: default
    freq: At will
    DC: 17
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 22
  - name: dominate person
    source: default
    freq: 3/day
    DC: 19
  - name: demand
    source: default
    freq: 1/day
    DC: 22
  - name: true seeing
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 24
ability_scores:
  STR: 41
  DEX: 11
  CON: 28
  INT: 14
  WIS: 23
  CHA: 18
BAB: 15
CMB: 34
CMD: 44
feats:
- name: Awesome Blow
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (longsword)
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Quick Draw
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 15
    jump: 23
  Craft (any one): 25
  Knowledge (history): 12
  Knowledge (nobility): 12
  Perception: 29
languages:
- Common
- Giant
- Terran
ecology:
  environment: cold mountains
  organization: solitary, pair, patrol (3-6), squad (7-12), or company (13-30 plus
    2-4 fighters or rogues of 2nd-4th level, 1 oracle or sorcerer of 5th-8th level,
    1 ranger or monk commander of 5th-6th level, 10-20 yetis, 1-4 cloud giants, 8-12
    frost giants, 10-16 stone giants, 4-8 lamia matriarchs, and 1-2 adult blue dragons)
  treasure_type: standard
  treasure:
  - masterwork full plate armor
  - masterwork longsword
  - 3 masterwork spears
  - other treasure
special_abilities:
  Command Giant (Su): A rune giant gains a +4 racial bonus on the save DC of charm
    or compulsion effects used against giants.
  Runes (Ex): As a free action, whenever a rune giant uses its spark shower or spell-like
    abilities, it can cause the runes on its body to flash with light. All creatures
    within 10 feet of the giant must make a DC 24 Fortitude save or be blinded for
    1 round. The saving throw is Charisma-based.
  Spark Shower (Su): As a standard action, a rune giant can cause a shower of sparks
    to erupt out of one of the runes on its body. These sparks function as a breath
    weapon (30-ft. cone; 10d6 fire and 10d6 electricity damage; Reflex DC 29 half;
    usable once every 1d4 rounds). The save DC is Constitution-based.
desc_long: |-
  Magically crafted and crossbred from taiga and fire giant slaves by ancient wizards, rune giants are anathema to their own kind. Given power to command and magically control other giants, the rune giants themselves served their even more powerful masters, and in so doing granted ancient empires armies of giants to command. In the eons since these ancient empires collapsed, rune giants have persisted as a race of their own, little more than bogeymen, horrors whispered of late at night by superstitious giants.

  Rune giants' charcoal flesh is decorated by dozens of runes-manifestations of their eldritch powers. Rune giants are 40 feet tall and weigh 25,000 pounds.

---

# Giant, Rune Giant
This giant’s skin is black and pitted, like roughly cast iron, and etched with glowing red runes.
**Source** Bestiary 2 pg. 130, Pathfinder #6: Spires of Xin-Shalast pg. 86
**XP** 102,400

LE Gargantuan humanoid (giant)
**Init** +0; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +29

##### Defense

**AC** 30, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+9 armor, +15 natural, –4 size)
**hp** 270 (20d8+180)
**Fort** +15, **Ref** +6, **Will** +20
**Immune** cold, electricity, fire

##### Offense
**Speed** 35 ft. (50 ft. without armor); _[[spells/Air Walk|air walk]]_
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +27/+22/+17 (4d6+22/17–20) or 2 slams +26 (2d6+15)
**Ranged** mwk _[[items/Weapon/Spear|spear]]_ +12/+7/+2 (4d6+15/×3)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[spells/Command|command]]_ giants, runes, _[[spells/Spark|spark]]_ shower
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
Constant—_air walk_
At will—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Suggestion|suggestion]]_ (DC 17)
3/day—mass _[[spells/Charm Monster|charm monster]]_ (DC 22), _[[spells/Dominate Person|dominate person]]_ (DC 19)
1/day—_[[spells/Demand|demand]]_ (DC 22), _[[spells/True Seeing|true seeing]]_

##### Statistics
**Str** 41, **Dex** 11, **Con** 28, **Int** 14, **Wis** 23, **Cha** 18
**Base Atk** +15; **CMB** +34; **CMD** 44
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_longsword_), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +15 (+23 _[[spells/Jump|jump]]_), Craft (any one) +25, Knowledge (history) +12, Knowledge (nobility) +12, Perception +29
**Languages** Common, Giant, Terran

##### Ecology

**Environment** cold mountains
**Organization** solitary, pair, patrol (3–6), squad (7–12), or company (13–30 plus 2–4 fighters or rogues of 2nd–4th level, 1 _[[classes/Oracle|oracle]]_ or _[[classes/Sorcerer|sorcerer]]_ of 5th–8th level, 1 _[[classes/Ranger|ranger]]_ or _[[classes/Monk|monk]]_ commander of 5th–6th level, 10–20 yetis, 1–4 cloud giants, 8–12 frost giants, 10–16 stone giants, 4–8 _[[monsters/Lamia|lamia]]_ matriarchs, and 1–2 adult blue dragons)
**Treasure** standard (masterwork _[[items/Armor/Full plate|full plate]]_ armor, masterwork _longsword_, 3 masterwork spears, other treasure)

### Special Abilities

**_Command_ Giant (Su)** A rune giant gains a +4 racial bonus on the save DC of charm or compulsion effects used against giants.

**Runes (Ex)** As a free action, whenever a rune giant uses its _spark_ shower or _spell-like abilities_, it can cause the runes on its body to flash with light. All creatures within 10 feet of the giant must make a DC 24 Fortitude save or be _[[conditions/Blinded|blinded]]_ for 1 round. The saving throw is Charisma-based.
**_Spark_ Shower (Su)** As a standard action, a rune giant can cause a shower of sparks to erupt out of one of the runes on its body. These sparks function as a _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone; 10d6 fire and 10d6 electricity damage; Reflex DC 29 half; usable once every 1d4 rounds). The save DC is Constitution-based.

##### Description

Magically crafted and crossbred from taiga and fire giant slaves by ancient wizards, rune giants are anathema to their own kind. Given power to _command_ and magically control other giants, the rune giants themselves served their even more powerful masters, and in so doing granted ancient empires armies of giants to _command_. In the eons since these ancient empires collapsed, rune giants have persisted as a race of their own, little more than bogeymen, horrors whispered of late at night by superstitious giants.

Rune giants’ _[[items/Mundane/Charcoal|charcoal]]_ flesh is decorated by dozens of runes—manifestations of their eldritch powers. Rune giants are 40 feet tall and weigh 25,000 pounds.