---
cssclass: [monsters]
title1: Baregara
desc_short: This lumbering apelike monster has blood-red fur, twisted horns, and a
  hideous fanged orifice set in the center of its chest.
title2: Baregara
CR: 12
sources:
- name: Bestiary 3
  page: 34
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #42: Sanctum of the Serpent God'
  page: 80
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/serpentsSkull/v5748btpy8ihw
XP: 19200
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 13
  flat_footed: 21
  components:
    dex: 4
    natural: 12
    size: -1
HP:
  HP: 168
  long: 16d10+80
saves:
  fort: 15
  ref: 14
  will: 10
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
SR: 23
speeds:
  base: 30
  climb: 40
attacks:
  melee:
  - - text: bite +23 (1d8+8)
      entries:
      - - damage: 1d8+8
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (1d10+8 plus grab)
      entries:
      - - damage: 1d10+8
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 23
    - text: gore +23 (1d8+8)
      entries:
      - - damage: 1d8+8
      attack: gore
      bonus:
      - 23
  special:
  - devouring grapple
  - monstrous challenge
  - one-armed hold
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: dispel magic
    source: default
    freq: At will
  - name: teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: quickened hold person
    source: default
    freq: 3/day
    DC: 16
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: dire apes
      amount: 1d4
      chance: 50%
    - name: girallons
      amount: 1d2
      chance: 35%
  - name: unholy blight
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 16
    concentration: 19
ability_scores:
  STR: 26
  DEX: 19
  CON: 20
  INT: 15
  WIS: 16
  CHA: 17
BAB: 16
CMB: 25
CMB_other: +29 grapple
CMD: 39
feats:
- name: Critical Focus
- name: Improved Initiative
- name: Intimidating Prowess
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (hold person)
- name: Step Up
- name: Throw Anything
skills:
  Acrobatics: 15
  Bluff: 14
  Climb: 27
  Diplomacy: 11
  Intimidate: 30
  Knowledge (nature): 10
  Knowledge (planes): 13
  Perception: 22
  Sense Motive: 14
  Stealth: 19
  Survival: 19
  Swim: 16
languages:
- Abyssal
- Celestial
- Common
- Draconic
- telepathy 100 ft.
ecology:
  environment: warm forests (Abyss)
  organization: solitary, pair, or troop (3-5)
  treasure_type: standard
special_abilities:
  Devouring Grapple (Ex): The mouth at the center of a baregara's chest automatically
    deals 2d8+4 points of damage per round to any creature the baregara successfully
    grapples.
  Monstrous Challenge (Su): As a standard action, a baregara can make an Intimidate
    check to demoralize an opponent. If this check is successful, the baregara surges
    with power and gains a +4 enhancement bonus to Strength and Constitution for 10
    minutes. This ability is usable three times per day.
  One-Armed Hold (Ex): A baregara's huge arms allow it to initiate and maintain a
    grapple without the standard -4 penalty for not having both hands free.
desc_long: |-
  Although natives of the Abyss that often serve as minions for powerful demons or demon lords, baregaras are not in fact demons themselves. Some scholars classify them as “proto-demons”-monsters like bebiliths or xacabras that could perhaps someday complete their supernatural evolution into full demonic glory, but that have not quite yet reached that end. Of course, to the baregara's victims, these debates are incidental.

  In the Abyss, baregaras form small troops just like the apes of the Material Plane. These troops are led by the strongest fighter or an individual anointed by a powerful demon the baregara troop serves. Rivalries between troops are part of a complex hierarchy that is all but incomprehensible to non-baregaras, but planar scholars have observed that all baregaras take trophies from notable kills, and that these grisly mementos play some role in establishing the convoluted social standing of the troop leaders and their followers.

  Even when knuckle-walking on their enormous hands, baregaras stand over 12 feet high when measured to the top of their horns, and their dense bodies can weigh up to 1,500 pounds.

---

# Baregara
This lumbering apelike monster has blood-red fur, twisted horns, and a hideous fanged orifice set in the center of its chest.
**Source** Bestiary 3 pg. 34, Pathfinder #42: Sanctum of the Serpent God pg. 80
**XP** 19,200
CE Large outsider (chaotic, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +22

##### Defense

**AC** 25, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 Dex, +12 natural, –1 size)
**hp** 168 (16d10+80)
**Fort** +15, **Ref** +14, **Will** +10
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 23

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** bite +23 (1d8+8), 2 claws +23 (1d10+8 plus _[[universal monster rules/Grab|grab]]_), gore +23 (1d8+8)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** devouring grapple, monstrous challenge, one-armed hold
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +19)
Constant—_[[spells/See Invisibility|see invisibility]]_
At will—_[[spells/Dispel Magic|dispel magic]]_, teleport (self plus 50 lbs. of objects only)
3/day—quickened _[[spells/Hold Person|hold person]]_ (DC 16)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 1d4 dire apes 50% or 1d2 girallons 35%), _[[spells/Unholy Blight|unholy blight]]_ (DC 17)

##### Statistics
**Str** 26, **Dex** 19, **Con** 20, **Int** 15, **Wis** 16, **Cha** 17
**Base Atk** +16; **CMB** +25 (+29 grapple); **CMD** 39
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_hold person_), _[[feats/Step Up|Step Up]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Acrobatics +15, Bluff +14, _Climb_ +27, Diplomacy +11, Intimidate +30, Knowledge (nature) +10, Knowledge (planes) +13, Perception +22, Sense Motive +14, Stealth +19, Survival +19, Swim +16
**Languages** Abyssal, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** warm forests (Abyss)
**Organization** solitary, pair, or troop (3–5)
**Treasure** standard

### Special Abilities

**Devouring Grapple (Ex)** The mouth at the center of a _[[monsters/Baregara|baregara]]_’s chest automatically deals 2d8+4 points of damage per round to any creature the _baregara_ successfully grapples.

**Monstrous Challenge (Su)** As a standard action, a _baregara_ can make an Intimidate check to demoralize an opponent. If this check is successful, the _baregara_ surges with power and gains a +4 enhancement bonus to Strength and Constitution for 10 minutes. This ability is usable three times per day.

**One-Armed Hold (Ex)** A _baregara_’s huge arms allow it to _[[npcs/Initiate|initiate]]_ and maintain a grapple without the standard –4 penalty for not having both hands free.

##### Description

Although natives of the Abyss that often serve as minions for powerful demons or demon lords, baregaras are not in fact demons themselves. Some scholars classify them as “proto-demons”—monsters like bebiliths or xacabras that could perhaps someday complete their supernatural evolution into full demonic glory, but that have not quite yet reached that end. Of course, to the _baregara_’s victims, these debates are incidental.

In the Abyss, baregaras form small troops just like the apes of the Material Plane. These troops are led by the strongest _[[classes/Fighter|fighter]]_ or an individual anointed by a powerful demon the _baregara_ troop serves. Rivalries between troops are part of a complex hierarchy that is all but incomprehensible to non-baregaras, but _[[items/Weapon Magic Abilities/Planar|planar]]_ scholars have observed that all baregaras take trophies from notable kills, and that these grisly mementos play some role in establishing the convoluted social standing of the troop leaders and their followers.

Even when knuckle-walking on their enormous hands, baregaras stand over 12 feet high when measured to the top of their horns, and their dense bodies can weigh up to 1,500 pounds.