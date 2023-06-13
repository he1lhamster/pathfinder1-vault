---
cssclass: [monsters]
title1: Duergar, Duergar Sergeant
title2: Duergar Sergeant
CR: 1
sources:
- name: Monster Codex
  page: 50
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 400
race: Duergar
classes:
- fighter 2
alignment: LE
size: Large
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 0
senses:
  darkvision: 120
AC:
  AC: 16
  touch: 9
  flat_footed: 15
  components:
    armor: 7
    size: -1
HP:
  HP: 23
  long: 2d10+8
saves:
  fort: 6
  ref: 0
  will: 2
  will_other: +1 vs. fear
  other: +2 vs. spells
defensive_abilities:
- bravery +1
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
  - - text: mwk dwarven waraxe +5 (2d8+4/×3)
      entries:
      - - damage: 2d8+4
          crit_multiplier: 3
      attack: mwk dwarven waraxe
      bonus:
      - 5
  ranged:
  - - text: heavy crossbow +3 (2d8/19-20)
      entries:
      - - damage: 2d8
          crit_range: 19-20
      attack: heavy crossbow
      bonus:
      - 3
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
    CL: 2
    concentration: -1
ability_scores:
  STR: 17
  DEX: 10
  CON: 16
  INT: 10
  WIS: 15
  CHA: 4
BAB: 2
CMB: 5
CMD: 16
CMD_other: 20 vs. bull rush or trip on solid ground
feats:
- name: Cleave
- name: Power Attack
- name: Weapon Focus (dwarven waraxe)
skills:
  Handle Animal: 1
  Perception: 2
  Ride: -2
  Survival: 6
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- slow and steady
- stability
gear:
  combat:
  - potions of cure light wounds (2)
  - alchemist's fire (2)
  other:
  - banded mail
  - heavy crossbow with 10 bolts
  - mwk dwarven waraxe
  - 9 gp
ecology:
  environment: any underground
desc_long: Veteran soldiers among the duergar lead groups of warriors or form their
  own elite strike forces. These soldiers always use enlarge person before combat.

---

# Duergar, Duergar Sergeant

**Source** Monster Codex pg. 50
**XP** 400
_[[monsters/Duergar|Duergar]]_ _[[classes/Fighter|fighter]]_ 2

LE Large humanoid (dwarf)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +2

##### Defense

**AC** 16, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+7 armor, –1 size)
**hp** 23 (2d10+8)
**Fort** +6, **Ref** +0, **Will** +2 (+1 vs. _[[universal monster rules/Fear|fear]]_); +2 vs. spells
**Defensive Abilities** bravery +1; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Dwarven waraxe|dwarven waraxe]]_ +5 (2d8+4/×3)
**Ranged** _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +3 (2d8/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration –1)
1/day—_[[spells/Enlarge Person|enlarge person]]_ (self only), _[[spells/Invisibility|invisibility]]_ (self only)

##### Statistics
**Str** 17, **Dex** 10, **Con** 16, **Int** 10, **Wis** 15, **Cha** 4
**Base Atk** +2; **CMB** +5; **CMD** 16 (20 vs. bull rush or _[[universal monster rules/Trip|trip]]_ on solid ground)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dwarven waraxe_)
**Skills** Handle Animal +1, Perception +2, Ride –2, Survival +6
**Languages** Common, Dwarven, Undercommon
**SQ** _[[spells/Slow|slow]]_ and steady, stability
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** _[[items/Armor/Banded mail|banded mail]]_, _heavy crossbow_ with 10 bolts, mwk _dwarven waraxe_, 9 gp

##### Ecology

**Environment** any underground

##### Description

Veteran soldiers among the _duergar_ lead groups of warriors or form their own elite strike forces. These soldiers always use _enlarge person_ before combat.