---
cssclass: [monsters]
title1: Wisagatcak
desc_short: This spiderlike monstrosity watches quietly, skittering about on six needle-sharp
  legs.
title2: Wisagatcak
CR: 14
sources:
- name: Planar Adventures
  page: 249
  link: http://paizo.com/products/btpya1am
XP: 38400
alignment: LE
size: Small
type: outsider
subtypes:
- evil
- extraplanar
- lawful
initiative:
  bonus: 7
senses:
  see in darkness: true
  tremorsense: 30
auras:
- name: insidious whispers
  radius: 60
  DC: 23
AC:
  AC: 30
  touch: 19
  flat_footed: 22
  components:
    dex: 7
    dodge: 1
    natural: 11
    size: 1
HP:
  HP: 200
  long: 16d10+112
saves:
  fort: 12
  ref: 17
  will: 15
DR:
- amount: 10
  weakness: good
immunities:
- cold
SR: 25
speeds:
  base: 50
  burrow: 20
  climb: 40
attacks:
  melee:
  - - text: bite +22 (1d8+5 plus weakness)
      entries:
      - - damage: 1d8+5
        - effect: weakness
      attack: bite
      bonus:
      - 22
    - text: gore +22 (2d4+5)
      entries:
      - - damage: 2d4+5
      attack: gore
      bonus:
      - 22
    - text: 4 talons +22 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 4
      attack: talons
      bonus:
      - 22
  special:
  - rake (2 talons, 1d6+5)
  - ravage flesh
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: At will
  - name: whispering wind
    source: default
    freq: At will
  - name: air walk
    source: default
    freq: 3/day
  - name: freezing sphere
    source: default
    freq: 3/day
    DC: 21
  - name: polar ray
    source: default
    freq: 1/day
    DC: 23
  - name: wall of ice
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 21
  DEX: 24
  CON: 25
  INT: 18
  WIS: 20
  CHA: 21
BAB: 16
CMB: 20
CMB_other: +24 trip
CMD: 38
CMD_other: 48 vs. trip
feats:
- name: Acrobatic Steps
- name: Combat Expertise
- name: Dodge
- name: Greater Trip
- name: Improved Trip
- name: Lunge
- name: Mobility
- name: Nimble Moves
skills:
  Acrobatics: 26
  Bluff: 24
  Climb: 32
  Intimidate: 24
  Knowledge (arcana): 20
  Knowledge (planes): 23
  Perception: 24
  Sense Motive: 24
  Stealth: 30
  Survival: 24
languages:
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: cold mountains (Hell)
  organization: solitary or wave (2-8)
  treasure_type: standard
special_abilities:
  Insidious Whispers (Su): The wisagatcak relentlessly assaults intelligent creatures
    within 60 feet with an onslaught of telepathic whispering consisting of dark temptations
    and horrifying promises that can drive victims mad. If a creature begins its turn
    within the area of a wisagatcak's insidious whispers, it must succeed at a DC
    23 Will save or take 1 point of Wisdom damage. Once a creature takes 4 points
    of Wisdom damage from insidious whispers (from one or multiple overlapping auras),
    it becomes afflicted with paranoia (Pathfinder RPG Horror Adventures 185). A character
    suffering from paranoia is immune to further Wisdom damage from insidious whispers.
    This is a mind-affecting insanity effect. The save DC is Charisma-based.
  Ravage Flesh (Su): If a wisagatcak hits a target with at least three of its attacks,
    it can attempt to rake the foe. Once a wisagatcak has raked a foe, it can automatically
    attempt to rake that foe in the following round and gains a +4 bonus on attack
    and damage rolls with its rake attacks. If a wisagatcak successfully damages the
    same foe with its rake attack in 2 successive rounds, it gains the effects of
    haste in the following round.
  Weakness (Su): A creature bitten by a wisagatcak must succeed at a DC 25 Fortitude
    save or take 1 point of Strength drain. The save DC is Constitution-based.
desc_long: |-
  Though wisagatcaks do not have a true hive mind, waves of these creatures are intimidatingly coordinated when hunting prey. Although they are outsiders and do not need to feed to survive, wisagatcaks enjoy the taste of warm flesh. A single wisagatcak can reduce a human body to its skeleton with unsettling speed.

   A wisagatcak has a leg span of 5 feet and weighs 60 pounds.

---

# Wisagatcak
This spiderlike monstrosity watches quietly, skittering about on six needle-sharp legs.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 249
**XP** 38,400

LE Small outsider (evil, extraplanar, lawful)
**Init** +7; **Senses** _[[universal monster rules/See in Darkness|see in darkness]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +24
**Aura** insidious whispers (60 ft., DC 23)

##### Defense

**AC** 30, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 Dex, +1 dodge, +11 natural, +1 size)
**hp** 200 (16d10+112)
**Fort** +12, **Ref** +17, **Will** +15
**DR** 10/good; **Immune** cold; **SR** 25

##### Offense
**Speed** 50 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** bite +22 (1d8+5 plus weakness), gore +22 (2d4+5), 4 talons +22 (1d6+5)
**Special Attacks** _[[universal monster rules/Rake|rake]]_ (2 talons, 1d6+5), ravage flesh
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Air Walk|air walk]]_, _[[spells/Freezing Sphere|freezing sphere]]_ (DC 21)
1/day—_[[spells/Polar Ray|polar ray]]_ (DC 23), _[[spells/Wall Of Ice|wall of ice]]_

##### Statistics
**Str** 21, **Dex** 24, **Con** 25, **Int** 18, **Wis** 20, **Cha** 21
**Base Atk** +16; **CMB** +20 (+24 _[[universal monster rules/Trip|trip]]_); **CMD** 38 (48 vs. _trip_)
**Feats** _[[feats/Acrobatic Steps|Acrobatic Steps]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Nimble Moves|Nimble Moves]]_
**Skills** Acrobatics +26, Bluff +24, _Climb_ +32, Intimidate +24, Knowledge (arcana) +20, Knowledge (planes) +23, Perception +24, Sense Motive +24, Stealth +30, Survival +24
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** cold mountains (Hell)
**Organization** solitary or wave (2–8)
**Treasure** standard

### Special Abilities

**Insidious Whispers (Su)** The _[[monsters/Wisagatcak|wisagatcak]]_ relentlessly assaults intelligent creatures within 60 feet with an _[[feats/Onslaught|onslaught]]_ of telepathic whispering consisting of dark temptations and horrifying promises that can drive victims mad. If a creature begins its turn within the area of a _wisagatcak_’s insidious whispers, it must succeed at a DC 23 Will save or take 1 point of Wisdom damage. Once a creature takes 4 points of Wisdom damage from insidious whispers (from one or multiple overlapping auras), it becomes afflicted with _[[spells/Paranoia|paranoia]]_ (Pathfinder RPG Horror Adventures 185). A character suffering from _paranoia_ is immune to further Wisdom damage from insidious whispers. This is a mind-affecting _[[spells/Insanity|insanity]]_ effect. The save DC is Charisma-based.

**Ravage Flesh (Su)** If a _wisagatcak_ hits a target with at least three of its attacks, it can attempt to _rake_ the foe. Once a _wisagatcak_ has raked a foe, it can automatically attempt to _rake_ that foe in the following round and gains a +4 bonus on attack and damage rolls with its _rake_ attacks. If a _wisagatcak_ successfully damages the same foe with its _rake_ attack in 2 successive rounds, it gains the effects of _[[spells/Haste|haste]]_ in the following round.

**Weakness (Su)** A creature bitten by a _wisagatcak_ must succeed at a DC 25 Fortitude save or take 1 point of Strength drain. The save DC is Constitution-based.

##### Description

Though wisagatcaks do not have a true hive mind, waves of these creatures are intimidatingly coordinated when hunting prey. Although they are outsiders and do not need to feed to survive, wisagatcaks enjoy the taste of warm flesh. A single _wisagatcak_ can reduce a human body to its skeleton with unsettling speed.

A _wisagatcak_ has a leg span of 5 feet and weighs 60 pounds.