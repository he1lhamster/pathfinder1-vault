---
cssclass: [monsters]
title1: Kirin
desc_short: With draconic scales covering much of its body, this staglike creature
  moves with awe-inspiring grace.
title2: Kirin
CR: 7
sources:
- name: Bestiary 3
  page: 168
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 3200
alignment: LG
size: Large
type: magical beast
subtypes:
- air
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect evil: true
  low-light vision: true
  scent: true
AC:
  AC: 20
  touch: 15
  flat_footed: 14
  components:
    dex: 6
    natural: 5
    size: -1
HP:
  HP: 85
  long: 9d10+36
saves:
  fort: 10
  ref: 12
  will: 10
resistances:
  cold: 10
  electricity: 30
  fire: 10
SR: 18
speeds:
  base: 60
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: gore +14 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: gore
      bonus:
      - 14
    - text: 2 hooves +8 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: hooves
      bonus:
      - 8
  special:
  - breath weapon (15-ft. cone, 5d6 fire damage, Reflex DC 18 for half, usable every
    1d4 rounds)
  - powerful charge (gore, 2d8+14)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: water walk
    source: default
    freq: Constant
  - name: gaseous form
    source: default
    freq: At will
  - name: gust of wind
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: 1/day
  - name: create food and water
    source: default
    freq: 1/day
  - name: major creation
    source: default
    freq: 1/day
  - name: wind walk
    source: default
    freq: 1/day
    other: self only
  sources:
  - name: default
    CL: 9
    concentration: 15
spells:
  entries:
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 19
  - name: lesser restoration
    source: '?'
    level: 2
  - name: scorching ray
    source: '?'
    level: 2
  - name: color spray
    source: '?'
    level: 1
    DC: 17
  - name: cure light wounds
    source: '?'
    level: 1
  - name: disguise self
    source: '?'
    level: 1
  - name: remove fear
    source: '?'
    level: 1
  - name: sanctuary
    source: '?'
    level: 1
    DC: 17
  - name: arcane mark
    source: '?'
    level: 0
  - name: create water
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: guidance
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 6
    concentration: 12
    slots:
      3: 4
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 20
  DEX: 23
  CON: 18
  INT: 18
  WIS: 21
  CHA: 23
BAB: 9
CMB: 15
CMD: 31
CMD_other: 35 vs. trip
feats:
- name: Combat Casting
- is_bonus: true
  name: Eschew Materials
- name: Flyby Attack
- name: Hover
- name: Iron Will
- name: Weapon Focus (gore)
skills:
  Diplomacy: 15
  Fly: 20
  Knowledge (history): 13
  Perception: 17
  Perform (sing): 15
  Sense Motive: 14
languages:
- Abyssal
- Auran
- Celestial
- Common
- Draconic
- telepathy 100 ft.
ecology:
  environment: any
  organization: solitary or pair
  treasure_type: standard
special_abilities:
  Spells: A kirin casts spells as a 6th-level sorcerer, and can cast spells from the
    cleric list as well as those normally available to a sorcerer. Cleric spells are
    considered arcane spells for a kirin, meaning that the creature does not need
    a divine focus to cast them.
desc_long: |-
  The noble kirin roam the sky, their feet rarely touching soil. They have a stag's graceful body and cloven hooves, a pair of backward-facing horns, and a thick mane and tail ranging from golden to brilliant reds or purples in the hues of the setting sun. Their hide resembles that of a dragon, the scales gleaming ebon or iridescent green.

  Rare in the extreme, kirin seldom meddle openly in worldly affairs, preferring a subtle hand in overturning the schemes of wicked spirits such as hags and oni. The blood of young kirin runs hot, however, and such spirited youths may serve as mounts for cavaliers and paladins of clever wit and untarnished moral quality.

  The wisest and most powerful kirin are known as emperor kirin, having earned this title through the respect of their peers and the strength of their powers. They resemble standard kirin, except their hooves give off sparks as they gallop through the air.

  Emperor kirin have the advanced creature simple template and additional racial Hit Dice. When advancing a kirin's Hit Dice to create an emperor kirin, make the following additional changes. CR: Increase by 1 + the number of additional HD. Breath Weapon: Damage increases by 1d6 for every 2 additional HD. Spellcasting: Increase sorcerer level (for the purpose of spells known and spells per day) by 1 per additional HD. Spell-Like Abilities: Increase caster level by +1 per additional HD. Spell Resistance: Increase by +1 per additional HD.

---

# Kirin
With draconic scales covering much of its body, this staglike creature moves with awe-inspiring _[[spells/Grace|grace]]_.
**Source** Bestiary 3 pg. 168
**XP** 3,200

LG Large magical beast (air)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +17

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+6 Dex, +5 natural, –1 size)
**hp** 85 (9d10+36)
**Fort** +10, **Ref** +12, **Will** +10
**Resist** cold 10, electricity 30, fire 10; **SR** 18

##### Offense
**Speed** 60 ft., fly 120 ft. (good)
**Melee** gore +14 (1d8+5), 2 hooves +8 (1d6+2)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (15-ft. cone, 5d6 fire damage, Reflex DC 18 for half, usable every 1d4 rounds), _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d8+14)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +15)
Constant—_detect evil_, _[[spells/Water Walk|water walk]]_
At will—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Gust Of Wind|gust of wind]]_
1/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Create Food and Water|create food and water]]_, _[[spells/Major Creation|major creation]]_, _[[spells/Wind Walk|wind walk]]_ (self only)
**Spells Known **(CL 6th; concentration +12)
3rd (4/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 19)
2nd (7/day)—lesser _[[spells/Restoration|restoration]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Color Spray|color spray]]_ (DC 17), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 17)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, stabilize

##### Statistics
**Str** 20, **Dex** 23, **Con** 18, **Int** 18, **Wis** 21, **Cha** 23
**Base Atk** +9; **CMB** +15; **CMD** 31 (35 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (gore)
**Skills** Diplomacy +15, Fly +20, Knowledge (history) +13, Perception +17, Perform (sing) +15, Sense Motive +14
**Languages** Abyssal, Auran, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any
**Organization** solitary or pair
**Treasure** standard

### Special Abilities
**Spells **A _[[monsters/Kirin|kirin]]_ casts spells as a 6th-level _[[classes/Sorcerer|sorcerer]]_, and can cast spells from the _[[classes/Cleric|cleric]]_ list as well as those normally available to a _sorcerer_. _Cleric_ spells are considered arcane spells for a _kirin_, meaning that the creature does not need a divine focus to cast them.

##### Description

The noble _kirin_ roam the sky, their feet rarely touching soil. They have a stag’s graceful body and cloven hooves, a pair of backward-facing horns, and a thick mane and tail ranging from golden to brilliant reds or purples in the hues of the setting sun. Their hide resembles that of a dragon, _[[diseases/The Scales|the scales]]_ gleaming ebon or iridescent green.

Rare in the extreme, _kirin_ seldom meddle openly in worldly affairs, preferring a subtle hand in overturning the schemes of wicked spirits such as hags and oni. The blood of young _kirin_ runs hot, however, and such spirited youths may serve as mounts for cavaliers and paladins of clever wit and untarnished moral quality.

The wisest and most powerful _kirin_ are known as emperor _kirin_, having earned this title through the respect of their peers and the strength of their powers. They resemble standard _kirin_, except their hooves give off sparks as they gallop through the air.

Emperor _kirin_ have the advanced creature simple template and additional racial Hit Dice. When _[[items/Weapon Magic Abilities/Advancing|advancing]]_ a _kirin_’s Hit Dice to create an emperor _kirin_, make the following additional changes.

* CR: Increase by 1 + the number of additional HD. 
* _Breath Weapon_: Damage increases by 1d6 for every 2 additional HD. 
* Spellcasting: Increase _sorcerer_ level (for the purpose of spells known and spells per day) by 1 per additional HD. 
* _Spell-Like Abilities_: Increase caster level by +1 per additional HD. 
* _[[universal monster rules/Spell Resistance|Spell Resistance]]_: Increase by +1 per additional HD.