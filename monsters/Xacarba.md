---
cssclass: [monsters]
title1: Xacarba
desc_short: This towering, three-tailed, six-eyed beast seems like three rune-backed
  serpents partially melded together into one body.
title2: Xacarba
CR: 15
sources:
- name: Bestiary 2
  page: 288
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #18: Descent into Midnight'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy86v1
XP: 51200
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 9
senses:
  arcane sight: true
  darkvision: 120
  detect good: true
  low-light vision: true
  scent: true
  true seeing: true
AC:
  AC: 31
  touch: 12
  flat_footed: 25
  components:
    dex: 5
    dodge: 1
    natural: 19
    size: -4
HP:
  HP: 210
  long: 20d10+100
saves:
  fort: 17
  ref: 13
  will: 20
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 26
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: bite +25 (3d8+9 plus poison)
      entries:
      - - damage: 3d8+9
        - effect: poison
      attack: bite
      bonus:
      - 25
    - text: 3 tail slaps +20 (2d8+4 plus grab)
      entries:
      - - damage: 2d8+4
        - effect: grab
      count: 3
      attack: tail slaps
      bonus:
      - 20
  special:
  - constrict (2d6+9)
  - redirect spell
space: 20
reach: 15
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 20
  - name: charm monster
    source: default
    freq: 3/day
    DC: 21
  - name: mass suggestion
    source: default
    freq: 3/day
    DC: 23
  - name: scrying
    source: default
    freq: 3/day
    DC: 21
  - name: symbol of pain
    source: default
    freq: 3/day
    DC: 22
  - name: touch of idiocy
    source: default
    freq: 3/day
  - name: vision
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: hezrou
      amount: 1
      chance: 50%
    - name: succubi
      amount: 1d4
      chance: 50%
  sources:
  - name: default
    CL: 18
    concentration: 25
ability_scores:
  STR: 29
  DEX: 21
  CON: 21
  INT: 26
  WIS: 22
  CHA: 24
BAB: 20
CMB: 33
CMB_other: +37 grapple
CMD: 49
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Spring Attack
- name: Vital Strike
skills:
  Acrobatics: 25
    jump: 29
  Bluff: 30
  Climb: 17
  Diplomacy: 27
  Disguise: 27
  Intimidate: 27
  Knowledge (arcana): 31
  Knowledge (any two): 31
  Linguistics: 28
  Perception: 29
  Sense Motive: 29
  Spellcraft: 31
  Stealth: 16
  Use Magic Device: 27
languages:
- Abyssal
- Common
- Draconic
- telepathy 100 ft.
special_qualities:
- change shape (any humanoid as a swift action, but always retains one serpentine
  trait that negates the bonus to Disguise checks; alter self)
ecology:
  environment: any land (Abyss)
  organization: solitary
  treasure_type: standard
special_abilities:
  Poison (Su): |-
    Bite-injury; save Fort DC 25; frequency 1/round for 6 rounds; effect one chosen by the xacarba from three options; cure 2 consecutive saves. The save DC is Constitution-based.

    Fiendish Bile: effect 1d4 Str damage (good-aligned creatures also take 2d8 points of damage).

    Mysterious Blood: effect 1d4 Dex and 1d4 Wis damage plus confusion for 1 round.

    Vile Disjunction: effect targeted greater dispel magic (CL 18th) on the creature.
  Redirect Spell (Su): Any creature that attempts to cast a spell within 30 feet of
    a xacarba must cast the spell defensively. If the caster fails the concentration
    check to do so (or if the caster opts to not cast defensively), the xacarba can
    choose the target of the spell as a immediate action. The new target must be a
    legal target-if there's no legal alternative target to choose from, this ability
    cannot be used.
desc_long: Fiends hailing from the darkest reaches of the Abyss, xacarbas are manipulation
  and destruction intertwined. With their infamous ability to redirect spells, these
  serpentine goliaths wreak havoc on the mind as well as the body, turning allies
  against one another and reveling in the destruction doing so produces.

---

# Xacarba
This towering, three-tailed, six-eyed beast seems like three rune-backed serpents partially melded together into one body.
**Source** Bestiary 2 pg. 288, Pathfinder #18: Descent into Midnight pg. 88
**XP** 51,200
CE Gargantuan outsider (chaotic, evil, extraplanar)
**Init** +9; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Good|detect good]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +29

##### Defense

**AC** 31, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+5 Dex, +1 dodge, +19 natural, –4 size)
**hp** 210 (20d10+100)
**Fort** +17, **Ref** +13, **Will** +20
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 26

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +25 (3d8+9 plus poison), 3 tail slaps +20 (2d8+4 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+9), redirect spell
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +25)
Constant—_arcane sight_, _detect good_, _true seeing_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_, _[[spells/Suggestion|suggestion]]_ (DC 20)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 21), mass _suggestion_ (DC 23), _[[spells/Scrying|scrying]]_ (DC 21), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 22), _[[spells/Touch of Idiocy|touch of idiocy]]_, _[[spells/Vision|vision]]_
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 hezrou or 1d4 succubi, 50%)

##### Statistics
**Str** 29, **Dex** 21, **Con** 21, **Int** 26, **Wis** 22, **Cha** 24
**Base Atk** +20; **CMB** +33 (+37 grapple); **CMD** 49 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +25 (+29 _[[spells/Jump|jump]]_), Bluff +30, _Climb_ +17, Diplomacy +27, Disguise +27, Intimidate +27, Knowledge (arcana) +31, Knowledge (any two) +31, Linguistics +28, Perception +29, Sense Motive +29, Spellcraft +31, Stealth +16, Use Magic Device +27
**Languages** Abyssal, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid as a swift action, but always retains one serpentine trait that negates the bonus to Disguise checks; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any land (Abyss)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Poison (Su)** Bite—injury; save Fort DC 25; frequency 1/round for 6 rounds; effect one chosen by the _[[monsters/Xacarba|xacarba]]_ from three options; cure 2 consecutive saves. The save DC is Constitution-based.

Fiendish Bile: effect 1d4 Str damage (good-aligned creatures also take 2d8 points of damage).

Mysterious Blood: effect 1d4 Dex and 1d4 Wis damage plus _[[spells/Confusion|confusion]]_ for 1 round.

Vile Disjunction: effect targeted greater _[[spells/Dispel Magic|dispel magic]]_ (CL 18th) on the creature.

**Redirect Spell (Su) **Any creature that attempts to cast a spell within 30 feet of a _xacarba_ must cast the spell defensively. If the caster fails the concentration check to do so (or if the caster opts to not cast defensively), the _xacarba_ can choose the target of the spell as a immediate action. The new target must be a legal target—if there’s no legal alternative target to choose from, this ability cannot be used.

##### Description

Fiends hailing from the darkest reaches of the Abyss, xacarbas are manipulation and _[[spells/Destruction|destruction]]_ intertwined. With their infamous ability to redirect spells, these serpentine goliaths wreak havoc on the mind as well as the body, turning allies against one another and reveling in the _destruction_ doing so produces.