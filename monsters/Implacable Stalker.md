---
cssclass: [monsters]
title1: Implacable Stalker
desc_short: Scars cover the twisted and grotesque body of this demon, its skin stained
  the color of blood.
title2: Implacable Stalker
CR: 8
sources:
- name: Horror Adventures
  page: 238
  link: http://paizo.com/products/btpy9n5a?Pathfinder-Roleplaying-Game-Horror-Adventures
XP: 4800
race: Babau
classes:
- implacable stalker
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  see invisibility: true
  sense fear: 120
auras:
- name: fear aura
  radius: 60
  DC: 16
AC:
  AC: 25
  touch: 11
  flat_footed: 24
  components:
    dex: 1
    natural: 14
HP:
  HP: 101
  long: 7d10+63
saves:
  fort: 13
  ref: 6
  will: 5
defensive_abilities:
- protective slime
- terrifying inevitability
DR:
- amount: 10
  weakness: cold iron or good
- amount: 5
  weakness: '-'
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
  sonic: 10
SR: 19
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +14 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: bite
      bonus:
      - 14
    - text: 2 claws +14 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 14
  - - text: longspear +14/+9 (1d8+10/×3)
      entries:
      - - damage: 1d8+10
          crit_multiplier: 3
      attack: longspear
      bonus:
      - 14
      - 9
    - text: bite +9 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 9
  special:
  - gory display
  - right behind you
  - sneak attack +2d6
space: 5
reach: 5
reach_other: 10 ft. with longspear
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: babau
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 7
    concentration: 10
ability_scores:
  STR: 25
  DEX: 13
  CON: 26
  INT: 14
  WIS: 13
  CHA: 16
BAB: 7
CMB: 14
CMD: 25
feats:
- name: Combat Reflexes
- is_bonus: true
  name: Diehard
- is_bonus: true
  name: Endurance
- name: Improved Initiative
- is_bonus: true
  name: Intimidating Prowess
- name: Iron Will
- name: Skill Focus (Stealth)
- is_bonus: true
  name: Toughness
skills:
  Acrobatics: 11
    when jumping: 7
  Climb: 14
  Disable Device: 11
  Escape Artist: 11
  Intimidate: 18
  Perception: 19
  Sense Motive: 11
  Sleight of Hand: 11
  Stealth: 28
  Survival: 1
    to follow tracks: 7
  _racial_mods:
    Acrobatics:
      when jumping: -4
    Intimidate:
      _: 8
    Perception:
      _: 8
    Stealth:
      _: 14
    Survival:
      to follow tracks: 6
languages:
- Abyssal
- Celestail
- Draconic
- telepathy 100 ft.
special_qualities:
- nightmare resurrection
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
  treasure:
  - longspear
  - other treasure
special_abilities:
  Protective Slime (Su): A layer of acidic slime coats a babau's skin. Any creature
    that strikes a babau with a natural attack or unarmed strike takes 1d8 points
    of acid damage from this slime if it fails a DC 21 Reflex save. A creature that
    strikes a babau with a melee weapon must succeed at a DC 21 Reflex save or the
    weapon takes 1d8 points of acid damage; if this damage penetrates the weapon's
    hardness, the weapon gains the broken condition. Ammunition that strikes a babau
    is automatically destroyed after it inflict its damage. The save DC is Constitution-based.
desc_long: Implacable stalkers embody murderous predation. They not only revel in
  hunting down and killing their victims in gory, brutal fashion, but they draw supernatural
  strength and power from their victims' fear and terror. They look similar to other
  creatures of their kind, but are often covered in gruesome scars and exude an aura
  of menace.

---

# Implacable Stalker
Scars cover the twisted and grotesque body of this demon, its skin stained the color of blood.
**Source** Horror Adventures pg. 238
**XP** 4,800
Babau _[[monsters/Implacable Stalker|implacable stalker]]_
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_, _[[spells/Sense Fear|sense fear]]_ 120 ft.; Perception +19
**Aura** _[[universal monster rules/Fear|fear]]_ aura (60 ft., DC 16)

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+1 Dex, +14 natural)
**hp** 101 (7d10+63)
**Fort** +13, **Ref** +6, **Will** +5
**Defensive Abilities** protective slime, terrifying inevitability; **DR** 10/cold iron or good, 5/—; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10, sonic 10; **SR** 19

##### Offense
**Speed** 20 ft.
**Melee** bite +14 (1d6+7), 2 claws +14 (1d6+7) or _[[items/Weapon/Longspear|longspear]]_ +14/+9 (1d8+10/×3), bite +9 (1d6+3)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _longspear_)
**Special Attacks** _[[items/Weapon Magic Abilities/Gory|gory]]_ display, right behind you, sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
Constant—_see invisibility_
 At will—_[[spells/Darkness|darkness]]_, _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only)
 1/day—_[[universal monster rules/Summon|summon]]_ (level 3, 1 babau 40%)

##### Statistics
**Str** 25, **Dex** 13, **Con** 26, **Int** 14, **Wis** 13, **Cha** 16
**Base Atk** +7; **CMB** +14; **CMD** 25
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +11 (+7 when jumping), _[[universal monster rules/Climb|Climb]]_ +14, Disable Device +11, Escape Artist +11, Intimidate +18, Perception +19, Sense Motive +11, Sleight of Hand +11, Stealth +28, Survival +1 (+7 to follow tracks); **Racial Modifiers** –4 Acrobatics when jumping, +8 Intimidate, +8 Perception, +14 Stealth, +6 Survival to follow tracks
**Languages** Abyssal, Celestail, Draconic, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[spells/Nightmare|nightmare]]_ _[[spells/Resurrection|resurrection]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard (_longspear_, other treasure)

### Special Abilities

**Protective Slime (Su)** A layer of acidic slime coats a babau’s skin. Any creature that strikes a babau with a natural attack or unarmed strike takes 1d8 points of acid damage from this slime if it fails a DC 21 Reflex save. A creature that strikes a babau with a melee weapon must succeed at a DC 21 Reflex save or the weapon takes 1d8 points of acid damage; if this damage penetrates the weapon’s hardness, the weapon gains the _[[conditions/Broken|broken]]_ condition. Ammunition that strikes a babau is automatically destroyed after it inflict its damage. The save DC is Constitution-based.

##### Description

Implacable stalkers embody murderous predation. They not only revel in hunting down and killing their victims in _gory_, brutal fashion, but they draw supernatural strength and power from their victims’ _fear_ and terror. They look similar to other creatures of their kind, but are often covered in gruesome scars and exude an aura of menace.