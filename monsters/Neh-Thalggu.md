---
cssclass: [monsters]
title1: Neh-Thalggu
desc_short: This crab-like nightmare has a lamprey mouth, twitching eyes on its legs,
  and several blisters along its back that hold human brains.
title2: Neh-Thalggu
CR: 8
sources:
- name: Bestiary 2
  page: 197
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 4800
alignment: CE
size: Large
type: aberration
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 19
  flat_footed: 18
  components:
    dex: 3
    natural: 2
    insight: 7
    size: -1
HP:
  HP: 105
  long: 10d8+60
saves:
  fort: 9
  ref: 6
  will: 11
DR:
- amount: 10
  weakness: magic
immunities:
- confusion effects
SR: 19
speeds:
  base: 10
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +13 (1d8+7 plus poison)
      entries:
      - - damage: 1d8+7
        - effect: poison
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - rend (2 claws, 2d6+7)
space: 10
reach: 5
spells:
  entries:
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 16
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 16
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: alter self
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: grease
    source: Sorcerer
    level: 1
    DC: 14
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 14
  - name: shield
    source: Sorcerer
    level: 1
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 17
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 24
  DEX: 16
  CON: 23
  INT: 19
  WIS: 18
  CHA: 17
BAB: 7
CMB: 15
CMD: 35
CMD_other: cannot be tripped
feats:
- name: Arcane Strike
- name: Extend Spell
- name: Combat Reflexes
- is_bonus: true
  name: Eschew Materials
- name: Improved Initiative
- name: Power Attack
skills:
  Fly: 15
  Knowledge (arcana): 23
  Knowledge (dungeoneering): 23
  Knowledge (planes): 23
  Perception: 17
  Sense Motive: 17
  Spellcraft: 17
  Stealth: 12
  Use Magic Device: 16
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Protean
- Undercommon
- telepathy (100 feet)
special_qualities:
- brain collection
- strange knowledge
ecology:
  environment: any
  organization: solitary
  treasure_type: double
special_abilities:
  Brain Collection (Ex): A neh-thalggu can store up to seven humanoid brains and use
    them to enhance its knowledge and power. Each stored brain grants a neh-thalggu
    a cumulative +1 insight bonus to AC, concentration checks, and Knowledge checks.
    A neh-thalggu can extract a brain from a helpless opponent with a coup de grace
    attack, or as a standard action from a body that has been dead for no more than
    1 minute. A neh-thalggu that has fewer than seven brains gains one negative level
    for each missing brain. These negative levels can never become permanent, but
    they can only be removed by replacing one of its collected brains. The stats presented
    here assume a monster with a full collection.
  Poison (Ex): Bite-injury; save Fort DC 21; frequency 1/round for 6 rounds; effect
    1d2 Strength damage and staggered; cure 2 consecutive saves. The save DC is Constitution-based.
  Spells: A neh-thalggu casts spells as a 7th-level sorcerer. For each negative level
    it takes from missing brains, its caster level is reduced by 1. A neh-thalggu
    with no collected brains cannot cast any of its spells.
  Strange Knowledge (Ex): All Knowledge skills are class skills for neh-thalggus.
desc_long: |-
  Known also as brain collectors, the alien neh-thalggus hail from distant worlds, traveling the gulfs of space on immense living ships that swiftly decay when they land upon a new world, leaving behind a deadly cargo of hungry monsters. Neh-thalggus are carnivores, but they do not digest humanoid brains they eat-rather, these brains lodge in one of several bulbous blisters on the creature's back and help to increase its intellect.

  Some speculate that neh-thalggus encountered in this reality may merely be juveniles of their kind, perhaps exiled from their home worlds by greater kin until they can prove their worth on other worlds. Their brain collections may be a morbid form of currency in their home realm, or the thoughts in these brains may merely be fuel for a dark apotheosis into an even more sinister mature form.

---

# Neh-Thalggu
This crab-like _[[spells/Nightmare|nightmare]]_ has a lamprey mouth, twitching eyes on its legs, and several blisters along its back that hold human brains.
**Source** Bestiary 2 pg. 197
**XP** 4,800
CE Large aberration
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +17

##### Defense

**AC** 21, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +2 natural, +7 insight, –1 size)
**hp** 105 (10d8+60)
**Fort** +9, **Ref** +6, **Will** +11
**DR** 10/magic; **Immune** _[[spells/Confusion|confusion]]_ effects; **SR** 19

##### Offense
**Speed** 10 ft., fly 40 ft. (perfect)
**Melee** bite +13 (1d8+7 plus poison), 2 claws +13 (1d6+7)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+7)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 7th; concentration +17)
3rd (5/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 16), _[[spells/Hold Person|hold person]]_ (DC 16)
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Alter Self|alter self]]_, _[[spells/Invisibility|invisibility]]_
1st (7/day)—_[[spells/Grease|grease]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Shield|shield]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 24, **Dex** 16, **Con** 23, **Int** 19, **Wis** 18, **Cha** 17
**Base Atk** +7; **CMB** +15; **CMD** 35 (cannot be tripped)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +15, Knowledge (arcana, dungeoneering, and planes) +23, Perception +17, Sense Motive +17, Spellcraft +17, Stealth +12, Use Magic Device +16
**Languages** Abyssal, Aklo, Common, Draconic, Protean, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ (100 feet)
**SQ** brain collection, strange knowledge

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double

### Special Abilities

**Brain Collection (Ex)** A _[[monsters/Neh-Thalggu|neh-thalggu]]_ can store up to seven humanoid brains and use them to enhance its knowledge and power. Each stored brain grants a _neh-thalggu_ a cumulative +1 insight bonus to AC, concentration checks, and Knowledge checks. A _neh-thalggu_ can extract a brain from a _[[conditions/Helpless|helpless]]_ opponent with a coup de _[[spells/Grace|grace]]_ attack, or as a standard action from a body that has been dead for no more than 1 minute. A _neh-thalggu_ that has fewer than seven brains gains one negative level for each missing brain. These negative levels can never become permanent, but they can only be removed by replacing one of its collected brains. The stats presented here assume a monster with a full collection.

**Poison (Ex)** Bite—injury; save Fort DC 21; frequency 1/round for 6 rounds; effect 1d2 Strength damage and _[[conditions/Staggered|staggered]]_; cure 2 consecutive saves. The save DC is Constitution-based.
**Spells **A _neh-thalggu_ casts spells as a 7th-level _sorcerer_. For each negative level it takes from missing brains, its caster level is reduced by 1. A _neh-thalggu_ with no collected brains cannot cast any of its spells.
**Strange Knowledge (Ex)** All Knowledge skills are class skills for neh-thalggus.

##### Description

Known also as brain collectors, the alien neh-thalggus hail from distant worlds, traveling the gulfs of space on immense living ships that swiftly decay when they land upon a new world, leaving behind a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ cargo of hungry monsters. Neh-thalggus are carnivores, but they do not digest humanoid brains they eat—rather, these brains lodge in one of several bulbous blisters on the creature’s back and help to increase its intellect.

Some speculate that neh-thalggus encountered in this reality may merely be juveniles of their kind, perhaps exiled from their home worlds by greater kin until they can prove their worth on other worlds. Their brain collections may be a morbid form of currency in their home realm, or the thoughts in these brains may merely be fuel for a dark _[[feats/Apotheosis|apotheosis]]_ into an even more sinister mature form.