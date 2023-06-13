---
cssclass: [monsters]
title1: Daredevil Hunter
title2: Daredevil Hunter
CR: 16
sources:
- name: NPC Codex
  page: 140
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Elf
classes:
- ranger 17
alignment: CN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 33
  touch: 19
  flat_footed: 26
  components:
    armor: 9
    deflection: 2
    dex: 6
    dodge: 1
    natural: 5
HP:
  HP: 142
  long: 17d10+44
saves:
  fort: 15
  ref: 20
  will: 9
  other: +2 vs. enchantments
defensive_abilities:
- improved evasion
immunities:
- poison
- sleep
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 elven curve blade +20/+15/+10/+5 (1d10+4/18-20)
      entries:
      - - damage: 1d10+4
          crit_range: 18-20
      attack: +1 elven curve blade
      bonus:
      - 20
      - 15
      - 10
      - 5
  ranged:
  - - text: +2 composite longbow +26/+21/+16/+11 (1d8+4/19-20/×3)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 composite longbow
      bonus:
      - 26
      - 21
      - 16
      - 11
  special:
  - favored enemy (animals +2, dragons +4, giants +4, magical beasts +4)
spells:
  entries:
  - name: darkvision
    source: Ranger
    level: 3
  - name: neutralize poison
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
  - name: snare
    source: Ranger
    level: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: hide from animals
    source: Ranger
    level: 1
  - name: longstrider
    source: Ranger
    level: 1
  - name: pass without trace
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 14
    concentration: 15
tactics:
  Before Combat: The ranger casts barkskin, bear's endurance, darkvision, delay poison,
    longstrider, and pass without trace.
  During Combat: The ranger prefers ranged combat. He uses Deadly Aim with Rapid Shot,
    hoping to also use Tiring Critical.
  Base Statistics: Without barkskin, bear's endurance, darkvision, delay poison, and
    longstrider, the ranger's statistics are Senses low-light vision; AC 28, touch
    19, flat-footed 21; hp 108; Fort +13; Immune sleep; Speed 30 ft.; Con 11; Skills
    Acrobatics +23.
ability_scores:
  STR: 14
  DEX: 24
  CON: 15
  INT: 10
  WIS: 13
  CHA: 10
BAB: 17
CMB: 19
CMD: 39
feats:
- name: Critical Focus
- name: Deadly Aim
- name: Dodge
- name: Endurance
- name: Improved Critical (composite longbow)
- name: Manyshot
- name: Mobility
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Rapid Shot
- name: Shot on the Run
- name: Spring Attack
- name: Tiring Critical
skills:
  Acrobatics: 23
    when jumping: 27
  Climb: 9
  Handle Animal: 8
  Knowledge (arcana): 10
  Knowledge (local): 10
  Knowledge (nature): 13
  Perception: 21
  Ride: 11
  Stealth: 26
  Survival: 21
  Swim: 5
languages:
- Common
- Elven
special_qualities:
- camouflage
- elven magic
- favored terrain (forest +2, mountain +4, plains +4)
- hide in plain sight
- hunter's bond (companions)
- quarry
- swift tracker
- track +8
- weapon familiarity
- wild empathy +17
- woodland stride
gear:
  combat:
  - +1 dragon-bane arrows (5)
  - +1 giant-bane arrows (5)
  - +1 magical beast-bane arrows (5); potions of displacement (2)
  - potions of fly (2)
  - potions of haste (2)
  - scroll of commune with nature
  - wand of cure moderate wounds (20 charges)
  other:
  - +3 mithral breastplate
  - +1 elven curve blade
  - +2 composite longbow (+2 Str) with 60 arrows
  - belt of incredible dexterity +4
  - boots of elvenkind
  - cloak of resistance +3
  - efficient quiver
  - ring of feather falling
  - ring of protection +2
  - 1,380 gp
desc_long: The daredevil hunter seeks the largest and most dangerouscreatures for
  trophy kills.

---

# Daredevil Hunter

**Source** NPC Codex pg. 140
**XP** 76,800
Elf _[[classes/Ranger|ranger]]_ 17

CN Medium humanoid (elf)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 33, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+9 armor, +2 _[[spells/Deflection|deflection]]_, +6 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 142 (17d10+44)
**Fort** +15, **Ref** +20, **Will** +9; +2 vs. enchantments
**Defensive Abilities** improved evasion; **Immune** poison, sleep

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Elven curve blade|elven curve blade]]_ +20/+15/+10/+5 (1d10+4/18–20)
**Ranged** +2 _[[items/Weapon/Composite longbow|composite longbow]]_ +26/+21/+16/+11 (1d8+4/19–20/×3)
**Special Attacks** favored enemy (animals +2, dragons +4, giants +4, magical beasts +4)
**_Ranger_ Spells Prepared **(CL 14th; concentration +15)
3rd—_darkvision_, _[[spells/Neutralize Poison|neutralize poison]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Snare|snare]]_
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Hide from Animals|hide from animals]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, bear’s _endurance_, _darkvision_, _delay poison_, _longstrider_, and _pass without trace_.
**During Combat **The _ranger_ prefers ranged combat. He uses _[[feats/Deadly Aim|Deadly Aim]]_ with _[[feats/Rapid Shot|Rapid Shot]]_, hoping to also use _[[feats/Tiring Critical|Tiring Critical]]_.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _darkvision_, _delay poison_, and _longstrider_, the _ranger_’s statistics are **Senses **_low-light vision_; **AC **28, touch 19, _flat-footed_ 21; **hp **108; **Fort **+13; **Immune **sleep; **Speed **30 ft.; **Con **11; **Skills **Acrobatics +23.

##### Statistics
**Str** 14, **Dex** 24, **Con** 15, **Int** 10, **Wis** 13, **Cha** 10
**Base Atk** +17; **CMB** +19; **CMD** 39
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _Deadly Aim_, _Dodge_, _Endurance_, _[[feats/Improved Critical|Improved Critical]]_ (_composite longbow_), _[[feats/Manyshot|Manyshot]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _Rapid Shot_, _[[feats/Shot on the Run|Shot on the Run]]_, _[[feats/Spring Attack|Spring Attack]]_, _Tiring Critical_
**Skills** Acrobatics +23 (+27 when jumping), _[[universal monster rules/Climb|Climb]]_ +9, Handle Animal +8, Knowledge (arcana, local) +10, Knowledge (nature) +13, Perception +21, Ride +11, Stealth +26, Survival +21, Swim +5
**Languages** Common, Elven
**SQ** camouflage, elven magic, favored terrain (forest +2, mountain +4, plains +4), hide in plain sight, _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +8, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +17, woodland stride
**Combat Gear** +1 dragon-bane arrows (5), +1 giant-bane arrows (5), +1 magical beast-bane arrows (5); potions of _[[spells/Displacement|displacement]]_ (2), potions of fly (2), potions of _[[spells/Haste|haste]]_ (2), scroll of _[[spells/Commune with Nature|commune with nature]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (20 charges); **Other Gear** +3 mithral _[[items/Armor/Breastplate|breastplate]]_, +1 _elven curve blade_, +2 _composite longbow_ (+2 Str) with 60 arrows, _[[items/Wondrous Item/Belt of Incredible Dexterity +4|belt of incredible dexterity +4]]_, _[[items/Wondrous Item/Boots of Elvenkind|boots of elvenkind]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Efficient Quiver|efficient quiver]]_, _[[items/Ring/Ring of Feather Falling|ring of feather falling]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 1,380 gp

The _[[npcs/Daredevil Hunter|daredevil hunter]]_ seeks the largest and most dangerouscreatures for trophy kills.