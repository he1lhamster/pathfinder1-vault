---
cssclass: [monsters]
title1: Golem-Breaker
title2: Golem-Breaker
CR: 17
sources:
- name: NPC Codex
  page: 141
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Dwarf
classes:
- ranger 18
alignment: LN
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 31
  touch: 16
  flat_footed: 28
  components:
    armor: 10
    deflection: 3
    dex: 2
    dodge: 1
    natural: 5
HP:
  HP: 203
  long: 18d10+100
saves:
  fort: 18
  ref: 15
  will: 10
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- improved evasion
immunities:
- fire (120 points)
- poison
resistances:
  electricity: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 dwarven urgrosh +25/+20/+15/+10 (1d8+8/19-20/×3)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 dwarven urgrosh
      bonus:
      - 25
      - 20
      - 15
      - 10
    - text: +2 dwarven urgrosh +25/+20/+15 (1d6+8/19-20/×3)
      entries:
      - - damage: 1d6+8
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 dwarven urgrosh
      bonus:
      - 25
      - 20
      - 15
  ranged:
  - - text: +1 heavy crossbow +21 (1d10+1/19-20)
      entries:
      - - damage: 1d10+1
          crit_range: 19-20
      attack: +1 heavy crossbow
      bonus:
      - 21
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - favored enemy (constructs +8, elves +2, goblinoids +2, oozes +2)
spells:
  entries:
  - name: cure serious wounds
    source: Ranger
    level: 4
  - name: freedom of movement
    source: Ranger
    level: 4
  - name: cure moderate wounds
    source: Ranger
    level: 3
  - name: water walk
    source: Ranger
    level: 3
  - name: barkskin
    source: Ranger
    level: 2
  - name: bear's endurance
    source: Ranger
    level: 2
  - name: protection from energy
    source: Ranger
    level: 2
  - name: wind wall
    source: Ranger
    level: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: detect snares and pits
    source: Ranger
    level: 1
    count: 2
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 15
    concentration: 17
tactics:
  Before Combat: The ranger casts barkskin, bear's endurance, delay poison, longstrider,
    protection from energy (fire), and resist energy (electricity).
  During Combat: The ranger uses Mobility and Spring Attack to overcome enemy reach,
    and Greater Vital Strike to make devastating single blows.
  Base Statistics: Without barkskin, bear's endurance, delay poison, freedom of movement,
    longstrider, protection from energy, and resist energy, the ranger's statistics
    are AC 26, touch 16, flat-footed 23; hp 167; Fort +16; Immune none; Resist none;
    Speed 20 ft.; Con 16.
ability_scores:
  STR: 22
  DEX: 14
  CON: 20
  INT: 10
  WIS: 14
  CHA: 6
BAB: 18
CMB: 24
CMD: 40
CMD_other: 44 vs. bull rush or trip
feats:
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Greater Two-Weapon Fighting
- name: Greater Vital Strike
- name: Improved Critical (dwarven urgrosh)
- name: Improved Initiative
- name: Improved Two-Weapon Fighting
- name: Improved Vital Strike
- name: Mobility
- name: Spring Attack
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
- name: Vital Strike
- name: Weapon Focus (dwarven urgrosh)
skills:
  Acrobatics: 19
  Climb: 14
  Heal: 10
  Knowledge (arcana): 15
  Knowledge (dungeoneering): 18
  Knowledge (engineering): 10
  Knowledge (geography): 8
  Knowledge (nature): 8
  Perception: 20
    to notice unusual stonework: 22
  Stealth: 12
  Survival: 15
  Swim: 9
languages:
- Common
- Dwarven
special_qualities:
- camouflage
- favored terrain (forest +2, mountain +4, underground +4, urban +4)
- hide in plain sight
- hunter's bond (companions)
- quarry
- swift tracker
- track +9
- wild empathy +16
- woodland stride
gear:
  combat:
  - boots of speed
  other:
  - +4 mithral breastplate
  - +2/+2 dwarven urgrosh
  - +1 heavy crossbow with 10 bolts
  - bag of holding (type I)
  - belt of giant strength +4
  - cloak of resistance +2
  - golembane scarab
  - ring of protection +3
  - 1,600 gp
desc_long: A golem-breaker makes a ruin of constructs, clockworks, and complex devices.

---

# Golem-Breaker

**Source** NPC Codex pg. 141
**XP** 102,400
Dwarf _[[classes/Ranger|ranger]]_ 18

LN Medium humanoid (dwarf)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 31, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+10 armor, +3 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 203 (18d10+100)
**Fort** +18, **Ref** +15, **Will** +10; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), improved evasion; **Immune** fire (120 points), poison; **Resist** electricity 30

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Dwarven urgrosh|dwarven urgrosh]]_ +25/+20/+15/+10 (1d8+8/19–20/×3), +2 _dwarven urgrosh_ +25/+20/+15 (1d6+8/19–20/×3)
**Ranged** +1 _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +21 (1d10+1/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, favored enemy (constructs +8, elves +2, goblinoids +2, oozes +2)
**_Ranger_ Spells Prepared **(CL 15th; concentration +17)
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Freedom of Movement|freedom of movement]]_
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Water Walk|water walk]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Detect Snares and Pits|detect snares and pits]]_ (2), _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, bear’s _endurance_, _delay poison_, _longstrider_, _protection from energy_ (fire), and _resist energy_ (electricity).
**During Combat **The _ranger_ uses _[[feats/Mobility|Mobility]]_ and _[[feats/Spring Attack|Spring Attack]]_ to overcome enemy reach, and _[[feats/Greater Vital Strike|Greater Vital Strike]]_ to make devastating single blows.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _delay poison_, _freedom of movement_, _longstrider_, _protection from energy_, and _resist energy_, the _ranger_’s statistics are **AC **26, touch 16, _flat-footed_ 23; **hp **167; **Fort **+16; **Immune **none; **Resist **none; **Speed **20 ft.; **Con **16.

##### Statistics
**Str** 22, **Dex** 14, **Con** 20, **Int** 10, **Wis** 14, **Cha** 6
**Base Atk** +18; **CMB** +24; **CMD** 40 (44 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Double Slice|Double Slice]]_, _Endurance_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _Greater Vital Strike_, _[[feats/Improved Critical|Improved Critical]]_ (_dwarven urgrosh_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _Mobility_, _Spring Attack_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dwarven urgrosh_)
**Skills** Acrobatics +19, _[[universal monster rules/Climb|Climb]]_ +14, _[[spells/Heal|Heal]]_ +10, Knowledge (arcana) +15, Knowledge (dungeoneering) +18, Knowledge (engineering) +10, Knowledge (geography, nature) +8, Perception +20 (+22 to notice unusual stonework), Stealth +12, Survival +15, Swim +9
**Languages** Common, Dwarven
**SQ** camouflage, favored terrain (forest +2, mountain +4, underground +4, urban +4), hide in plain sight, _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +9, wild _[[feats/Empathy|empathy]]_ +16, woodland stride
**Combat Gear** _[[items/Wondrous Item/Boots of Speed|boots of speed]]_; **Other Gear** +4 mithral _[[items/Armor/Breastplate|breastplate]]_, +2/+2 _dwarven urgrosh_, +1 _heavy crossbow_ with 10 bolts, bag of holding (type I), _[[items/Wondrous Item/Belt of Giant Strength +4|belt of giant strength +4]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Golembane Scarab|golembane scarab]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 1,600 gp

A _[[npcs/Golem-Breaker|golem-breaker]]_ makes a ruin of constructs, clockworks, and complex devices.