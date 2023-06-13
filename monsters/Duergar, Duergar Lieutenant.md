---
cssclass: [monsters]
title1: Duergar, Duergar Lieutenant
title2: Duergar Lieutenant
CR: 5
sources:
- name: Monster Codex
  page: 46
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Duergar
classes:
- ranger 6
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 1
senses:
  darkvision: 120
AC:
  AC: 20
  touch: 11
  flat_footed: 19
  components:
    armor: 5
    dex: 1
    natural: 4
HP:
  HP: 61
  long: 6d10+24
saves:
  fort: 8
  ref: 6
  will: 4
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
  - - text: +1 warhammer +11/+6 (2d6+4/×3)
      entries:
      - - damage: 2d6+4
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 11
      - 6
  ranged:
  - - text: mwk light crossbow +8 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 8
  special:
  - favored enemy (dwarves +4, elves +2)
spell_like_abilities:
  entries:
  - superscripts:
    - APG
    name: dust of twilight
    source: default
    freq: 1/day
  - name: ironskin
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 6
    concentration: 3
spells:
  entries:
  - superscripts:
    - APG
    name: lead blades
    source: Ranger
    level: 1
  - name: longstrider
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 3
    concentration: 5
tactics:
  Before Combat: The lieutenant casts ironskin and lead blades on himself.
  Base Statistic: When not under the effects of ironskin and lead blades, the lieutenant's
    statistics are AC 16, touch 11, flat-footed 15; Melee +1 warhammer +11/+6 (1d8+4/×3).
ability_scores:
  STR: 16
  DEX: 12
  CON: 16
  INT: 10
  WIS: 15
  CHA: 4
BAB: 6
CMB: 9
CMD: 20
CMD_other: 24 vs. bull rush or trip
feats:
- name: Cleave
- name: Endurance
- name: Mounted Combat
- name: Power Attack
- name: Weapon Focus (warhammer)
skills:
  Climb: 11
  Handle Animal: 6
  Knowledge (dungeoneering): 9
  Perception: 11
  Ride: 9
  Survival: 11
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- favored terrain (underground +2)
- hunter's bond (companions)
- ironskinned
- slow and steady
- stability
- track +3
- twilight touched
- wild empathy +3
gear:
  combat:
  - potion of cure moderate wounds
  - potion of invisibility
  - alchemist's fire (2)
  - thunderstones (2)
  other:
  - +1 chain shirt
  - +1 warhammer
  - mwk light crossbow with 20 bolts
  - 51 gp
ecology:
  environment: any underground
desc_long: Spending much time scouting and exploring alone, rangers prove their toughness
  to their kin.

---

# Duergar, Duergar Lieutenant

**Source** Monster Codex pg. 46
**XP** 1,600
_[[monsters/Duergar|Duergar]]_ _[[classes/Ranger|ranger]]_ 6

LE Medium humanoid (dwarf)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +11

##### Defense

**AC** 20, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 armor, +1 Dex, +4 natural)
**hp** 61 (6d10+24)
**Fort** +8, **Ref** +6, **Will** +4; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Warhammer|warhammer]]_ +11/+6 (2d6+4/×3)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d8/19–20)
**Special Attacks** favored enemy (dwarves +4, elves +2)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +3)
1/day—_[[spells/Dust Of Twilight|dust of twilight]]_, _[[spells/Ironskin|ironskin]]_
**_Ranger_ Spells Prepared **(CL 3rd; concentration +5)
1st—_[[spells/Lead Blades|lead blades]]_, _[[spells/Longstrider|longstrider]]_

### Tactics

**Before Combat** The lieutenant casts _ironskin_ and _lead blades_ on himself.
 **Base Statistic** When not under the effects of _ironskin_ and _lead blades_, the lieutenant's statistics are **AC** 16, touch 11, _flat-footed_ 15; **Melee** +1 _warhammer_ +11/+6 (1d8+4/×3).

##### Statistics
**Str** 16, **Dex** 12, **Con** 16, **Int** 10, **Wis** 15, **Cha** 4
**Base Atk** +6; **CMB** +9; **CMD** 20 (24 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_warhammer_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +11, Handle Animal +6, Knowledge (dungeoneering) +9, Perception +11, Ride +9, Survival +11
**Languages** Common, Dwarven, Undercommon
**SQ** favored terrain (underground +2), _[[classes/Hunter|hunter]]_’s bond (companions), ironskinned, _[[spells/Slow|slow]]_ and steady, stability, track +3, twilight touched, wild _[[feats/Empathy|empathy]]_ +3
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Invisibility|invisibility]]_, _[[classes/Alchemist|alchemist]]_’s fire (2), thunderstones (2); **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _warhammer_, mwk _light crossbow_ with 20 bolts, 51 gp

##### Ecology

**Environment** any underground

##### Description

Spending much time scouting and exploring alone, rangers prove their _[[feats/Toughness|toughness]]_ to their kin.