---
cssclass: [monsters]
title1: Demon, Babau
desc_short: This emaciated figure looks like a horned human skeleton smothered within
  a bone-tight hide of slimy leather.
title2: Babau
CR: 6
sources:
- name: Pathfinder RPG Bestiary
  page: 57
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 2400
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
AC:
  AC: 19
  touch: 11
  flat_footed: 18
  components:
    dex: 1
    natural: 8
HP:
  HP: 73
  long: 7d10+35
saves:
  fort: 10
  ref: 6
  will: 5
defensive_abilities:
- protective slime
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 17
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +12 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 12
    - text: bite +12 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: bite
      bonus:
      - 12
  - - text: longspear +12/+7 (1d8+7/x3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: longspear
      bonus:
      - 12
      - 7
    - text: bite +7 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: bite
      bonus:
      - 7
  special:
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
    - name: babau at
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 7
ability_scores:
  STR: 21
  DEX: 13
  CON: 20
  INT: 14
  WIS: 13
  CHA: 16
BAB: 7
CMB: 12
CMD: 23
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Iron Will
- name: Skill Focus (Stealth)
skills:
  Acrobatics: 11
  Climb: 12
  Disable Device: 11
  Escape Artist: 11
  Perception: 19
  Sense Motive: 11
  Sleight of Hand: 11
  Stealth: 22
  _racial_mods:
    Perception:
      _: 8
    Stealth:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or gang (3-8)
  treasure_type: standard
  treasure:
  - longspear
  - other treasure
special_abilities:
  Protective Slime (Su): A layer of acidic slime coats a babau's skin. Any creature
    that strikes a babau with a natural attack or unarmed strike takes 1d8 points
    of acid damage from this slime if it fails a DC 18 Reflex save. A creature that
    strikes a babau with a melee weapon must make a DC 18 Reflex save or the weapon
    takes 1d8 points of acid damage; if this damage penetrates the weapon's hardness,
    the weapon gains the broken condition. Ammunition that strikes a babau is automatically
    destroyed after it inflicts its damage.
desc_long: |-
  The babau is an assassin, a murderer, and a sadist-certainly not traits unusual in the demons, yet the babau's penchant for stealth and surprise sets it apart from its generally less-subtle kin. With no need to eat (although most babaus relish the flavor of mortal meat on their thin, raspy tongues), a babau can wait in ambush for years or decades-their inhuman patience in anticipating a well-conceived murder also setting them apart from the other denizens of the Abyss. Babaus obsess over the act of killing and take great pride in their grisly art, often leaving behind some form of grim marker or obscure signature, whether it be a distinctive modus operandi, an unnerving token, or other profane evidence.

  A babau typically carries a longspear or other weapon with which it can strike at foes beyond its normal reach, but given the opportunity, a babau prefers to fight with its teeth or claws. The foul, caustic sludge that constantly seeps from their flesh prevents them from wearing armor unless it is specially treated or resistant to acid.

  A babau is 6 feet tall but weighs only 140 pounds. They form from mortal souls of lone killers-those who, in life, took pleasure in more personal and intimate murders. Loosed upon the Material Plane, a babau often finds itself in the same role, haunting the shadowy corners of the world as remorseless assassins.

---

# Demon, Babau
This emaciated figure looks like a horned human skeleton smothered within a bone-tight hide of slimy leather.
**Source** Pathfinder RPG Bestiary pg. 57
**XP** 2,400
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +19

##### Defense

**AC** 19, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+1 Dex, +8 natural)
**hp** 73 (7d10+35)
**Fort** +10, **Ref** +6, **Will** +5
**Defensive Abilities** protective slime; **DR** 10/cold iron or good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 17

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +12 (1d6+5), bite +12 (1d6+5) or _[[items/Weapon/Longspear|longspear]]_ +12/+7 (1d8+7/x3), bite +7 (1d6+2)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _longspear_)
**Special Attacks** sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th)
Constant—_see invisibility_
At will—_[[spells/Darkness|darkness]]_, _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only)
1/day—_[[universal monster rules/Summon|summon]]_ (level 3, 1 babau at 40%)

##### Statistics
**Str** 21, **Dex** 13, **Con** 20, **Int** 14, **Wis** 13, **Cha** 16
**Base Atk** +7; **CMB** +12; **CMD** 23
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Acrobatics +11, _[[universal monster rules/Climb|Climb]]_ +12, Disable Device +11, Escape Artist +11, Perception +19, Sense Motive +11, Sleight of Hand +11, Stealth +22; **Racial Modifiers** +8 Perception, +8 Stealth
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or gang (3–8)
**Treasure** standard (_longspear_, other treasure)

### Special Abilities

**Protective Slime (Su) **A layer of acidic slime coats a babau’s skin. Any creature that strikes a babau with a natural attack or unarmed strike takes 1d8 points of acid damage from this slime if it fails a DC 18 Reflex save. A creature that strikes a babau with a melee weapon must make a DC 18 Reflex save or the weapon takes 1d8 points of acid damage; if this damage penetrates the weapon’s hardness, the weapon gains the _[[conditions/Broken|broken]]_ condition. Ammunition that strikes a babau is automatically destroyed after it inflicts its damage.

##### Description

The babau is an assassin, a murderer, and a sadist—certainly not traits unusual in the demons, yet the babau’s penchant for stealth and surprise sets it apart from its generally less-subtle kin. With no need to eat (although most babaus relish the flavor of mortal meat on their thin, raspy _[[spells/Tongues|tongues]]_), a babau can wait in ambush for years or decades—their inhuman patience in anticipating a well-conceived murder also setting them apart from the other denizens of the Abyss. Babaus obsess over the act of killing and take great pride in their grisly art, often leaving behind some form of grim marker or obscure signature, whether it be a distinctive modus operandi, an unnerving token, or other profane evidence.

A babau typically carries a _longspear_ or other weapon with which it can strike at foes beyond its normal reach, but given the opportunity, a babau prefers to fight with its teeth or claws. The foul, caustic sludge that constantly seeps from their flesh prevents them from wearing armor unless it is specially treated or resistant to acid.

A babau is 6 feet tall but weighs only 140 pounds. They form from mortal souls of lone killers—those who, in life, took pleasure in more personal and intimate murders. Loosed upon the Material Plane, a babau often finds itself in the same role, haunting the shadowy corners of the world as remorseless assassins.