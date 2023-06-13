---
cssclass: [monsters]
title1: Duergar, Duergar Sharpshooter
title2: Duergar Sharpshooter
CR: 1/2
sources:
- name: Monster Codex
  page: 46
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 200
race: Duergar
classes:
- ranger 1
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 2
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
  HP: 13
  long: 1d10+3
saves:
  fort: 4
  ref: 4
  will: 2
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
  - - text: warhammer +3 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: warhammer
      bonus:
      - 3
  ranged:
  - - text: mwk light crossbow +4 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 4
  special:
  - favored enemy (dwarves +2)
spell_like_abilities:
  entries:
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  - name: ironskin
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 1
    concentration: -2
ability_scores:
  STR: 14
  DEX: 15
  CON: 14
  INT: 10
  WIS: 15
  CHA: 4
BAB: 1
CMB: 3
CMD: 15
CMD_other: 19 vs. bull rush or trip
feats:
- name: Rapid Reload (light crossbow)
skills:
  Climb: 5
  Handle Animal: 1
  Knowledge (dungeoneering): 4
  Perception: 6
  Stealth: 5
  Survival: 6
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- ironskinned
- slow and steady
- stability
- track +1
- wild empathy -2
gear:
  gear:
  - studded leather
  - mwk light crossbow with 20 bolts
  - warhammer
  - 16 gp
ecology:
  environment: any underground
desc_long: Spending much time scouting and exploring alone, rangers prove their toughness
  to their kin.

---

# Duergar, Duergar Sharpshooter

**Source** Monster Codex pg. 46
**XP** 200
_[[monsters/Duergar|Duergar]]_ _[[classes/Ranger|ranger]]_ 1

LE Medium humanoid (dwarf)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +6

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +2 Dex)
**hp** 13 (1d10+3)
**Fort** +4, **Ref** +4, **Will** +2; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Warhammer|warhammer]]_ +3 (1d8+2/×3)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d8/19–20)
**Special Attacks** favored enemy (dwarves +2)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration –2)
1/day—_[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Ironskin|ironskin]]_

##### Statistics
**Str** 14, **Dex** 15, **Con** 14, **Int** 10, **Wis** 15, **Cha** 4
**Base Atk** +1; **CMB** +3; **CMD** 15 (19 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Rapid Reload|Rapid Reload]]_ (_light crossbow_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +5, Handle Animal +1, Knowledge (dungeoneering) +4, Perception +6, Stealth +5, Survival +6
**Languages** Common, Dwarven, Undercommon
**SQ** ironskinned, _[[spells/Slow|slow]]_ and steady, stability, track +1, wild _[[feats/Empathy|empathy]]_ –2
**Gear** studded leather, mwk _light crossbow_ with 20 bolts, _warhammer_, 16 gp

##### Ecology

**Environment** any underground

##### Description

Spending much time scouting and exploring alone, rangers prove their _[[feats/Toughness|toughness]]_ to their kin.