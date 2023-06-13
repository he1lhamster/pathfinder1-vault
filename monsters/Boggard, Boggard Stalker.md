---
cssclass: [monsters]
title1: Boggard, Boggard Stalker
title2: Boggard Stalker
CR: 9
sources:
- name: Monster Codex
  page: 14
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 6400
race: Boggard
classes:
- ranger 7
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    deflection: 1
    dex: 1
    natural: 3
HP:
  HP: 95
  long: 3d8+7d10+44
  HD: 10
saves:
  fort: 12
  ref: 8
  will: 5
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: +1 handaxe +14/+9 (1d6+6/19-20/×3)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 handaxe
      bonus:
      - 14
      - 9
    - text: +1 handaxe +14/+9 (1d6+6/19-20/×3)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 handaxe
      bonus:
      - 14
      - 9
    - text: tongue +9 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 9
      touch: true
  ranged:
  - - text: javelin +10 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: javelin
      bonus:
      - 10
  special:
  - combat style (two-weapon)
  - favored enemy (dragons +2, humans +4)
  - terrifying croak (DC 12)
spells:
  entries:
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 4
    concentration: 5
ability_scores:
  STR: 20
  DEX: 13
  CON: 16
  INT: 8
  WIS: 13
  CHA: 8
BAB: 9
CMB: 14
CMD: 26
feats:
- name: Double Slice
- name: Endurance
- name: Improved Critical (handaxe)
- name: Improved Initiative
- name: Improved Two-Weapon Fighting
- name: Toughness
- name: Two-Weapon Fighting
- name: Weapon Focus (handaxe)
skills:
  Acrobatics: 5
    when jumping: 21
  Climb: 9
  Handle Animal: 4
  Knowledge (nature): 5
  Perception: 18
  Stealth: 14
    in swamps: 22
  Survival: 14
  Swim: 17
languages:
- Boggard
special_qualities:
- favored terrain (swamp +2)
- hold breath
- hunter's bond (companions)
- swamp stride
- track +3
- wild empathy +6
- woodland stride
gear:
  combat:
  - potion of barkskin
  - potion of cure moderate wounds
  - potion of invisibility
  other:
  - +1 studded leather
  - +1 handaxes (2)
  - javelins (3)
  - cloak of resistance +1
  - ring of protection +1
  - 360 gp
ecology:
  environment: temperate marshes
desc_long: Boggard rangers stalk silently through the swamps.

---

# Boggard, Boggard Stalker

**Source** Monster Codex pg. 14
**XP** 6,400
_[[monsters/Boggard|Boggard]]_ _[[classes/Ranger|ranger]]_ 7
CE Medium humanoid (_boggard_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +18

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +3 natural)
**hp** 95 (10 HD; 3d8+7d10+44)
**Fort** +12, **Ref** +8, **Will** +5

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** +1 _[[items/Weapon/Handaxe|handaxe]]_ +14/+9 (1d6+6/19–20/×3), +1 _handaxe_ +14/+9 (1d6+6/19–20/×3), tongue +9 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +10 (1d6+5)
**Special Attacks** combat style (two-weapon), favored enemy (dragons +2, humans +4), terrifying croak (DC 12)
**_Ranger_ Spells Prepared **(CL 4th; concentration +5)
1st—_[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_

##### Statistics
**Str** 20, **Dex** 13, **Con** 16, **Int** 8, **Wis** 13, **Cha** 8
**Base Atk** +9; **CMB** +14; **CMD** 26
**Feats** _[[feats/Double Slice|Double Slice]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Critical|Improved Critical]]_ (_handaxe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_handaxe_)
**Skills** Acrobatics +5 (+21 when jumping), _[[universal monster rules/Climb|Climb]]_ +9, Handle Animal +4, Knowledge (nature) +5, Perception +18, Stealth +14 (+22 in swamps), Survival +14, Swim +17
**Languages** _Boggard_
**SQ** favored terrain (swamp +2), _[[universal monster rules/Hold Breath|hold breath]]_, _[[classes/Hunter|hunter]]_’s bond (companions), swamp stride, track +3, wild _[[feats/Empathy|empathy]]_ +6, woodland stride
**Combat Gear** potion of _[[spells/Barkskin|barkskin]]_, potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** +1 studded leather, +1 handaxes (2), javelins (3), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 360 gp

##### Ecology

**Environment** temperate marshes

##### Description

_Boggard_ rangers stalk silently through the swamps.