---
cssclass: [monsters]
title1: Angel, Monadic Deva
desc_short: 'This angelic being has smooth skin, a muscular body, and large golden
  wings, and wields a large mace. '
title2: Monadic Deva
CR: 12
sources:
- name: Bestiary 2
  page: 27
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 19200
alignment: NG
size: Medium
type: outsider
subtypes:
- angel
- aquatic
- extraplanar
- good
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect evil: true
  low-light vision: true
auras:
- name: protective aura
AC:
  AC: 27
  touch: 14
  flat_footed: 23
  components:
    dex: 4
    natural: 13
    deflection vs. evil: 4
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 15
  ref: 13
  will: 10
  other: +4 vs. poison
DR:
- amount: 10
  weakness: evil
immunities:
- acid
- cold
- electricity
- fire
- death effects
- energy drain
- petrification
SR: 23
speeds:
  base: 40
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 morningstar +22/+17/+12 (1d8+10 plus solid blow)
      entries:
      - - damage: 1d8+10
        - effect: solid blow
      attack: +3 morningstar
      bonus:
      - 22
      - 17
      - 12
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: charm monster
    source: default
    freq: At will
    DC: 18
    other: elementals only
  - name: discern lies
    source: default
    freq: At will
    DC: 18
  - name: dispel evil
    source: default
    freq: At will
    DC: 19
  - name: dispel magic
    source: default
    freq: At will
  - name: holy smite
    source: default
    freq: At will
    DC: 18
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: plane shift
    source: default
    freq: At will
    DC: 19
  - name: remove curse
    source: default
    freq: At will
  - name: remove disease
    source: default
    freq: At will
  - name: remove fear
    source: default
    freq: At will
  - name: cure serious wounds
    source: default
    freq: 3/day
  - name: holy word
    source: default
    freq: 3/day
    DC: 21
  - name: mirror image
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 1/day
  - name: hold monster
    source: default
    freq: 1/day
    DC: 19
  - name: holy aura
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 21
  DEX: 19
  CON: 18
  INT: 19
  WIS: 18
  CHA: 19
BAB: 14
CMB: 19
CMD: 33
feats:
- name: Alertness
- name: Cleave
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Toughness
skills:
  Diplomacy: 21
  Fly: 25
  Intimidate: 21
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 29
  Sense Motive: 25
  Stealth: 21
  Survival: 27
  Swim: 19
  _racial_mods:
    Perception:
      _: 4
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- amphibious
ecology:
  environment: any good-aligned plane
  organization: solitary, pair, or squad (3-6)
  treasure_type: double
  treasure:
  - +3 morningstar
  - other treasure
special_abilities:
  Solid Blow (Su): If a monadic deva strikes an opponent twice in 1 round with its
    mace, that creature takes an extra 1d8+10 points of damage.
desc_long: |-
  Monadic devas are stoic watchers of the Ethereal Plane and the Elemental Planes. They search those planes for fiendish enclaves, battle evil planar monsters such as xills, and act as celestial liaisons to the genies and elementals. They have been known to broker temporary peace between warring elemental factions, often using their inherent magic to end hostilities long enough for negotiations to take place. In the armies of the good planes, they are leaders and officers, and after centuries of service to a deity, they may be transformed into astral devas. 

  Monadic devas like giving their maces names and proudly announcing them in battle with evil foes. Many of these weapons have seen battle for thousands of years and are quite battered. Younger devas may lend their weapons to good churches on the Material Plane so they can be used by great mortal heroes, though the angels eventually reclaim them after no more than a year and a day. 

  A monadic deva is 7 feet tall and weighs 220 pounds.

---

# Angel, Monadic Deva
This angelic being has smooth skin, a muscular body, and large golden wings, and wields a large mace.

**Source** Bestiary 2 pg. 27
**XP** 19,200

NG Medium outsider (angel, aquatic, extraplanar, good)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +29
**Aura** protective aura

##### Defense

**AC** 27, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+4 Dex, +13 natural; +4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 147 (14d10+70)
**Fort** +15, **Ref** +13, **Will** +10; +4 vs. poison
**DR** 10/evil; **Immune** acid, cold, electricity, fire, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, petrification; **SR** 23

##### Offense
**Speed** 40 ft., fly 90 ft. (good)
**Melee** +3 _[[items/Weapon/Morningstar|morningstar]]_ +22/+17/+12 (1d8+10 plus solid blow)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_detect evil_
At will—aid, _[[spells/Charm Monster|charm monster]]_ (DC 18, elementals only), _[[spells/Discern Lies|discern lies]]_ (DC 18), _[[spells/Dispel Evil|dispel evil]]_ (DC 19), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Holy Smite|holy smite]]_ (DC 18), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Plane Shift|plane shift]]_ (DC 19), _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_
3/day—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Holy Word|holy word]]_ (DC 21), _[[spells/Mirror Image|mirror image]]_
1/day—_[[spells/Heal|heal]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19), _[[spells/Holy Aura|holy aura]]_ (DC 22)

##### Statistics
**Str** 21, **Dex** 19, **Con** 18, **Int** 19, **Wis** 18, **Cha** 19
**Base Atk** +14; **CMB** +19; **CMD** 33
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Diplomacy +21, Fly +25, Intimidate +21, Knowledge (planes) +21, Knowledge (religion) +21, Perception +29, Sense Motive +25, Stealth +21, Survival +27, Swim +19; **Racial Modifiers** +4 Perception
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** any good-aligned plane
**Organization** solitary, pair, or squad (3–6)
**Treasure** double (+3 _morningstar_, other treasure)

### Special Abilities
**Solid Blow (Su)** If a monadic deva strikes an opponent twice in 1 round with its mace, that creature takes an extra 1d8+10 points of damage.

##### Description

Monadic devas are _[[feats/Stoic|stoic]]_ watchers of the Ethereal Plane and the Elemental Planes. They search those planes for fiendish enclaves, battle evil _[[items/Weapon Magic Abilities/Planar|planar]]_ monsters such as xills, and act as celestial liaisons to the genies and elementals. They have been known to broker temporary peace between warring elemental factions, often using their inherent magic to end hostilities long enough for negotiations to take place. In the armies of the good planes, they are leaders and officers, and after centuries of service to a deity, they may be transformed into astral devas.

Monadic devas like giving their maces names and proudly announcing them in battle with evil foes. Many of these weapons have seen battle for thousands of years and are quite battered. Younger devas may lend their weapons to good churches on the Material Plane so they can be used by great mortal heroes, though the angels eventually reclaim them after no more than a year and a day.

A monadic deva is 7 feet tall and weighs 220 pounds.