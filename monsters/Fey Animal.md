---
cssclass: [monsters]
title1: Fey Animal
desc_short: This wolverine's eyes possess the unmistakable glint of intelligence,
  and its mouth seems to twitch as if it were about to laugh.
title2: Fey Animal
CR: 3
sources:
- name: Lands of the Linnorm Kings
  page: 58
  link: http://paizo.com/products/btpy8ode?Pathfinder-Campaign-Setting-Lands-of-the-Linnorm-Kings
XP: 800
alignment: CN
size: Medium
type: fey
subtypes:
- augmented animal
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 17
  touch: 14
  flat_footed: 13
  components:
    dex: 4
    natural: 3
HP:
  HP: 22
  long: 3d8+9
saves:
  fort: 5
  ref: 7
  will: 3
DR:
- amount: 5
  weakness: cold iron
SR: 14
speeds:
  base: 40
  burrow: 20
  climb: 20
attacks:
  melee:
  - - text: bite +4 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: bite
      bonus:
      - 4
    - text: 2 claws +4 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: claws
      bonus:
      - 4
  special:
  - death curse (DC 13)
  - rage
spell_like_abilities:
  entries:
  - name: charm person
    source: default
    freq: 1/day
    DC: 13
  - name: faerie fire
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 3
    concentration: 5
ability_scores:
  STR: 15
  DEX: 19
  CON: 15
  INT: 12
  WIS: 14
  CHA: 14
BAB: 2
CMB: 4
CMD: 18
CMD_other: 22 vs. trip
feats:
- name: Skill Focus (Bluff)
- name: Toughness
skills:
  Acrobatics: 10
  Bluff: 12
  Climb: 16
  Knowledge (nature): 7
  Perception: 8
  Sense Motive: 8
  Stealth: 14
languages:
- Skald
- Sylvan
ecology:
  environment: cold forests
  organization: solitary
  treasure_type: none
desc_long: There is no description for this monster.

---

# Fey Animal
This _[[monsters/Wolverine|wolverine]]_’s eyes possess the unmistakable glint of intelligence, and its mouth seems to twitch as if it were about to laugh.
**Source** Lands of the Linnorm Kings pg. 58
**XP** 800

CN Medium fey (augmented animal)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 17, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+4 Dex, +3 natural)
**hp** 22 (3d8+9)
**Fort** +5, **Ref** +7, **Will** +3
**DR** 5/cold iron; **SR** 14

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +4 (1d4+2), 2 claws +4 (1d6+2)
**Special Attacks** death curse (DC 13), _[[spells/Rage|rage]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +5)
1/day—_[[spells/Charm Person|charm person]]_ (DC 13), _[[spells/Faerie Fire|faerie fire]]_

##### Statistics
**Str** 15, **Dex** 19, **Con** 15, **Int** 12, **Wis** 14, **Cha** 14
**Base Atk** +2; **CMB** +4; **CMD** 18 (22 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Bluff), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +10, Bluff +12, _Climb_ +16, Knowledge (nature) +7, Perception +8, Sense Motive +8, Stealth +14
**Languages** _[[classes/Skald|Skald]]_, Sylvan

##### Ecology

**Environment** cold forests
**Organization** solitary
**Treasure** none

There is no description for this monster.