---
cssclass: [monsters]
title1: Bounty Hunter
title2: Bounty Hunter
CR: 11
sources:
- name: NPC Codex
  page: 135
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 12800
race: Human
classes:
- ranger 12
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 8
AC:
  AC: 25
  touch: 16
  flat_footed: 20
  components:
    armor: 5
    deflection: 1
    dex: 4
    dodge: 1
    natural: 4
HP:
  HP: 94
  long: 12d10+24
saves:
  fort: 11
  ref: 13
  will: 6
defensive_abilities:
- evasion
immunities:
- poison
resistances:
  fire: 20
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 kukri +16/+11/+6 (1d4+5/18-20)
      entries:
      - - damage: 1d4+5
          crit_range: 18-20
      attack: +1 kukri
      bonus:
      - 16
      - 11
      - 6
    - text: +1 kukri +16/+11 (1d4+5/18-20)
      entries:
      - - damage: 1d4+5
          crit_range: 18-20
      attack: +1 kukri
      bonus:
      - 16
      - 11
  ranged:
  - - text: mwk composite longbow +17/+12/+7 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 17
      - 12
      - 7
  special:
  - favored enemy (animals +2, humans +6, orcs +2)
spells:
  entries:
  - name: barkskin
    source: Ranger
    level: 2
  - name: cat's grace
    source: Ranger
    level: 2
  - name: wind wall
    source: Ranger
    level: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 9
    concentration: 10
tactics:
  Before Combat: The ranger casts barkskin, cat's grace, delay poison, longstrider,
    and resist energy (fire).
  During Combat: The ranger attacks with his bow using Deadly Aim. In melee, he uses
    his kukris or attempts to grapple.
  Base Statistics: Without barkskin, cat's grace, delay poison, longstrider, and resist
    energy, the ranger's statistics are Init +6; Senses normal; AC 20, touch 14, flat-footed
    17; Ref +11; Immune none; Resist none; Speed 30 ft.; Ranged mwk longbow +15/+10/+5
    (1d8+4/×3); Dex 14; CMD 30 (32 vs. grapple); Skills Acrobatics +12, Stealth +17.
ability_scores:
  STR: 19
  DEX: 18
  CON: 14
  INT: 10
  WIS: 12
  CHA: 10
BAB: 12
CMB: 16
CMB_other: +18 grapple
CMD: 32
CMD_other: 34 vs. grapple
feats:
- name: Deadly Aim
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Improved Grapple
- name: Improved Initiative
- name: Improved Two-Weapon Fighting
- name: Improved Unarmed Strike
- name: Point-Blank Shot
- name: Two-Weapon Fighting
- name: Weapon Focus (kukri)
skills:
  Acrobatics: 14
    when jumping: 18
  Bluff: 10
  Climb: 12
  Disguise: 7
  Knowledge (geography): 8
  Knowledge (nature): 8
  Knowledge (local): 5
  Linguistics: 2
  Perception: 16
  Sense Motive: 11
  Stealth: 19
  Survival: 16
  Swim: 10
languages:
- Common
- Elven
- Orc
special_qualities:
- camouflage
- favored terrain (plains +2, urban +4)
- hunter's bond (companions)
- quarry
- swift tracker
- track +6
- wild empathy +12
- woodland stride
gear:
  combat:
  - potions of cure serious wounds (2)
  - smokesticks (2)
  - tanglefoot bags (2)
  other:
  - +2 studded leather
  - +1 kukris (2)
  - masterwork composite longbow (+4 Str) with 20 arrows
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - ring of protection +1
  - 793 gp
desc_long: A bounty hunter brings back his targets dead or alive.

---

# Bounty Hunter

**Source** NPC Codex pg. 135
**XP** 12,800
Human _[[classes/Ranger|ranger]]_ 12

LN Medium humanoid (human)
**Init** +8; **Senses** Perception +16

##### Defense

**AC** 25, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 armor, +1 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 94 (12d10+24)
**Fort** +11, **Ref** +13, **Will** +6
**Defensive Abilities** evasion; **Immune** poison; **Resist** fire 20

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Kukri|kukri]]_ +16/+11/+6 (1d4+5/18–20), +1 _kukri_ +16/+11 (1d4+5/18–20)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +17/+12/+7 (1d8+4/×3)
**Special Attacks** favored enemy (animals +2, humans +6, orcs +2)
**_Ranger_ Spells Prepared **(CL 9th; concentration +10)
2nd—_[[spells/Barkskin|barkskin]]_, cat’s _[[spells/Grace|grace]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, cat’s _grace_, _delay poison_, _longstrider_, and _resist energy_ (fire).
**During Combat **The _ranger_ attacks with his bow using _[[feats/Deadly Aim|Deadly Aim]]_. In melee, he uses his kukris or attempts to grapple.
**Base Statistics **Without _barkskin_, cat’s _grace_, _delay poison_, _longstrider_, and _resist energy_, the _ranger_’s statistics are **Init **+6; **Senses **normal; **AC **20, touch 14, _flat-footed_ 17; **Ref **+11; **Immune **none; **Resist **none; **Speed **30 ft.; **Ranged **mwk _[[items/Weapon/Longbow|longbow]]_ +15/+10/+5 (1d8+4/×3); **Dex **14; **CMD **30 (32 vs. grapple); **Skills **Acrobatics +12, Stealth +17.

##### Statistics
**Str** 19, **Dex** 18, **Con** 14, **Int** 10, **Wis** 12, **Cha** 10
**Base Atk** +12; **CMB** +16 (+18 grapple); **CMD** 32 (34 vs. grapple)
**Feats** _Deadly Aim_, _Dodge_, _[[feats/Double Slice|Double Slice]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_kukri_)
**Skills** Acrobatics +14 (+18 when jumping), Bluff +10, _[[universal monster rules/Climb|Climb]]_ +12, Disguise +7, Knowledge (geography, nature) +8, Knowledge (local) +5, Linguistics +2, Perception +16, Sense Motive +11, Stealth +19, Survival +16, Swim +10
**Languages** Common, Elven, _[[monsters/Orc|Orc]]_
**SQ** camouflage, favored terrain (plains +2, urban +4), _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +6, wild _[[feats/Empathy|empathy]]_ +12, woodland stride
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), smokesticks (2), tanglefoot bags (2); **Other Gear** +2 studded leather, +1 kukris (2), masterwork _composite longbow_ (+4 Str) with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 793 gp

A _[[npcs/Bounty Hunter|bounty hunter]]_ brings back his targets dead or alive.