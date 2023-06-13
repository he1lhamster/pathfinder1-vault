---
cssclass: [monsters]
title1: Boggard, Boggard Hunter
title2: Boggard Hunter
CR: 5
sources:
- name: Monster Codex
  page: 14
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Boggard
classes:
- ranger 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 18
  touch: 11
  flat_footed: 17
  components:
    armor: 4
    dex: 1
    natural: 3
HP:
  HP: 53
  long: 3d8+3d10+24
  HD: 6
saves:
  fort: 10
  ref: 6
  will: 4
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: morningstar +9 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: morningstar
      bonus:
      - 9
    - text: tongue +4 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 4
      touch: true
  ranged:
  - - text: mwk composite longbow +8 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 8
  special:
  - combat style (archery)
  - favored enemy (reptilian humanoids +2)
  - terrifying croak (DC 12)
ability_scores:
  STR: 19
  DEX: 13
  CON: 16
  INT: 8
  WIS: 13
  CHA: 8
BAB: 5
CMB: 9
CMD: 20
feats:
- name: Endurance
- name: Point-Blank Shot
- name: Precise Shot
- name: Toughness
- name: Weapon Focus (composite longbow)
skills:
  Acrobatics: 5
    when jumping: 21
  Knowledge (nature): 5
  Perception: 14
  Stealth: 8
    in swamps: 16
  Survival: 8
  Swim: 12
languages:
- Boggard
special_qualities:
- favored terrain (swamp +2)
- hold breath
- swamp stride
- track +1
- wild empathy +2
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 studded leather
  - morningstar
  - mwk composite longbow (+4 Str)
  - cloak of resistance +1
  - 267 gp
ecology:
  environment: temperate marshes
desc_long: Boggard rangers stalk silently through the swamps.

---

# Boggard, Boggard Hunter

**Source** Monster Codex pg. 14
**XP** 1,600
_[[monsters/Boggard|Boggard]]_ _[[classes/Ranger|ranger]]_ 3
CE Medium humanoid (_boggard_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 18, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +1 Dex, +3 natural)
**hp** 53 (6 HD; 3d8+3d10+24)
**Fort** +10, **Ref** +6, **Will** +4

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** _[[items/Weapon/Morningstar|morningstar]]_ +9 (1d8+4), tongue +4 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +8 (1d8+4/×3)
**Special Attacks** combat style (archery), favored enemy (reptilian humanoids +2), terrifying croak (DC 12)

##### Statistics
**Str** 19, **Dex** 13, **Con** 16, **Int** 8, **Wis** 13, **Cha** 8
**Base Atk** +5; **CMB** +9; **CMD** 20
**Feats** _[[feats/Endurance|Endurance]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite longbow_)
**Skills** Acrobatics +5 (+21 when jumping), Knowledge (nature) +5, Perception +14, Stealth +8 (+16 in swamps), Survival +8, Swim +12
**Languages** _Boggard_
**SQ** favored terrain (swamp +2), _[[universal monster rules/Hold Breath|hold breath]]_, swamp stride, track +1, wild _[[feats/Empathy|empathy]]_ +2
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 studded leather, _morningstar_, mwk _composite longbow_ (+4 Str), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 267 gp

##### Ecology

**Environment** temperate marshes

##### Description

_Boggard_ rangers stalk silently through the swamps.