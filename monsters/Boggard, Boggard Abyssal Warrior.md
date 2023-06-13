---
cssclass: [monsters]
title1: Boggard, Boggard Abyssal Warrior
title2: Boggard Abyssal Warrior
CR: 8
sources:
- name: Monster Codex
  page: 11
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Boggard
classes:
- antipaladin 7 (Pathfinder RPG Advanced Player's Guide 118)
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: cowardice
  radius: 10
AC:
  AC: 20
  touch: 10
  flat_footed: 20
  components:
    armor: 7
    natural: 3
HP:
  HP: 98
  long: 3d8+7d10+47
  HD: 10
saves:
  fort: 14
  ref: 6
  will: 8
immunities:
- disease
speeds:
  base: 15
  swim: 30
attacks:
  melee:
  - - text: +1 greataxe +16/+11 (1d12+8/19-20/×3)
      entries:
      - - damage: 1d12+8
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 greataxe
      bonus:
      - 16
      - 11
    - text: tongue +9 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 9
      touch: true
  ranged:
  - - text: throwing axe +9 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: throwing axe
      bonus:
      - 9
  special:
  - channel negative energy (DC 15, 4d6)
  - smite good 3/day (+2 attack and AC, +7 damage)
  - terrifying croak (DC 15)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 9
spells:
  entries:
  - name: invisibility
    source: Antipaladin
    level: 2
  - name: death knell
    source: Antipaladin
    level: 1
    DC: 13
  - name: doom
    source: Antipaladin
    level: 1
    DC: 13
  sources:
  - name: Antipaladin
    type: prepared
    CL: 4
    concentration: 6
ability_scores:
  STR: 20
  DEX: 11
  CON: 16
  INT: 8
  WIS: 9
  CHA: 14
BAB: 9
CMB: 14
CMD: 24
feats:
- name: Improved Critical (greataxe)
- name: Improved Initiative
- name: Power Attack
- name: Toughness
- name: Weapon Focus (greataxe)
skills:
  Acrobatics: 0
    when jumping: 16
  Bluff: 6
  Intimidate: 8
  Knowledge (religion): 3
  Perception: 3
  Sense Motive: 4
  Stealth: 0
    in swamps: 8
  Swim: 10
languages:
- Boggard
special_qualities:
- cruelties (sickened, staggered)
- fiendish boon (weapon +1, 1/day)
- hold breath
- swamp stride
- touch of corruption 5/day (3d6)
gear:
  combat:
  - potions of cure moderate wounds (3)
  other:
  - +1 breastplate
  - +1 greataxe
  - throwing axe
  - cloak of resistance +1
  - 922 gp
ecology:
  environment: temperate marshes
desc_long: A few boggards serve their tribes in specialized roles.

---

# Boggard, Boggard Abyssal Warrior

**Source** Monster Codex pg. 11
**XP** 4,800
_[[monsters/Boggard|Boggard]]_ _[[classes/Antipaladin|antipaladin]]_ 7 (Pathfinder RPG Advanced Player’s Guide 118)
CE Medium humanoid (_boggard_)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +3
**Aura** cowardice (10 ft.)

##### Defense

**AC** 20, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 armor, +3 natural)
**hp** 98 (10 HD; 3d8+7d10+47)
**Fort** +14, **Ref** +6, **Will** +8
**Immune** disease

##### Offense
**Speed** 15 ft., swim 30 ft.
**Melee** +1 _[[items/Weapon/Greataxe|greataxe]]_ +16/+11 (1d12+8/19–20/×3), tongue +9 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** _[[items/Weapon/Throwing axe|throwing axe]]_ +9 (1d6+5)
**Special Attacks** channel negative energy (DC 15, 4d6), smite good 3/day (+2 attack and AC, +7 damage), terrifying croak (DC 15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
At will—_[[spells/Detect Good|detect good]]_
**_Antipaladin_ Spells Prepared** (CL 4th; concentration +6)
2nd—_[[spells/Invisibility|invisibility]]_
 1st—_[[spells/Death Knell|death knell]]_ (DC 13), _[[spells/Doom|doom]]_ (DC 13)

##### Statistics
**Str** 20, **Dex** 11, **Con** 16, **Int** 8, **Wis** 9, **Cha** 14
**Base Atk** +9; **CMB** +14; **CMD** 24
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (_greataxe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greataxe_)
**Skills** Acrobatics +0 (+16 when jumping), Bluff +6, Intimidate +8, Knowledge (religion) +3, Perception +3, Sense Motive +4, Stealth +0 (+8 in swamps), Swim +10
**Languages** _Boggard_
**SQ** cruelties (_[[conditions/Sickened|sickened]]_, _[[conditions/Staggered|staggered]]_), fiendish boon (weapon +1, 1/day), _[[universal monster rules/Hold Breath|hold breath]]_, swamp stride, touch of corruption 5/day (3d6)
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (3); **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _greataxe_, _throwing axe_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 922 gp

##### Ecology

**Environment** temperate marshes

##### Description

A few boggards serve their tribes in specialized roles.