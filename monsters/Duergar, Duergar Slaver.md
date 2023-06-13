---
cssclass: [monsters]
title1: Duergar, Duergar Slaver
title2: Duergar Slaver
CR: 1/2
sources:
- name: Monster Codex
  page: 47
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 200
race: Duergar
classes:
- rogue 1
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 6
senses:
  darkvision: 120
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    armor: 3
    dex: 2
HP:
  HP: 10
  long: 1d8+2
saves:
  fort: 1
  ref: 4
  will: 3
  other: +2 vs. spells
immunities:
- paralysis
- phantasms
- poison
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: short sword +1 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: short sword
      bonus:
      - 1
  - - text: sap +1 (1d6+1 nonlethal)
      entries:
      - - damage: 1d6+1
          type: nonlethal
      attack: sap
      bonus:
      - 1
  ranged:
  - - text: mwk light crossbow +3 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 3
  special:
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: enlarge person
    source: default
    freq: 1/day
    other: self only
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  sources:
  - name: default
    CL: 1
    concentration: -2
ability_scores:
  STR: 13
  DEX: 15
  CON: 12
  INT: 12
  WIS: 16
  CHA: 4
BAB: 0
CMB: 1
CMD: 13
CMD_other: 17 vs. bull rush or trip
feats:
- name: Improved Initiative
skills:
  Acrobatics: 5
  Climb: 4
  Disable Device: 5
  Escape Artist: 5
  Knowledge (dungeoneering): 5
  Perception: 7
  Sense Motive: 7
  Stealth: 5
  Survival: 4
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- slow and steady
- stability
- trapfinding +1
gear:
  gear:
  - studded leather
  - mwk light crossbow with 20 bolts
  - sap
  - short sword
  - 18 gp
ecology:
  environment: any underground
desc_long: Duergar rogues primarily capture and discipline slaves.

---

# Duergar, Duergar Slaver

**Source** Monster Codex pg. 47
**XP** 200
_[[monsters/Duergar|Duergar]]_ _[[classes/Rogue|rogue]]_ 1

LE Medium humanoid (dwarf)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +7

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +2 Dex)
**hp** 10 (1d8+2)
**Fort** +1, **Ref** +4, **Will** +3; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Short sword|short sword]]_ +1 (1d6+1/19–20) or _[[items/Weapon/Sap|sap]]_ +1 (1d6+1 nonlethal)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +3 (1d8/19–20)
**Special Attacks** sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration –2)
1/day—_[[spells/Enlarge Person|enlarge person]]_ (self only), _[[spells/Invisibility|invisibility]]_ (self only)

##### Statistics
**Str** 13, **Dex** 15, **Con** 12, **Int** 12, **Wis** 16, **Cha** 4
**Base Atk** +0; **CMB** +1; **CMD** 13 (17 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Acrobatics +5, _[[universal monster rules/Climb|Climb]]_ +4, Disable Device +5, Escape Artist +5, Knowledge (dungeoneering) +5, Perception +7, Sense Motive +7, Stealth +5, Survival +4
**Languages** Common, Dwarven, Undercommon
**SQ** _[[spells/Slow|slow]]_ and steady, stability, trapfinding +1
**Gear** studded leather, mwk _light crossbow_ with 20 bolts, _sap_, _short sword_, 18 gp

##### Ecology

**Environment** any underground

##### Description

_Duergar_ rogues primarily capture and discipline slaves.