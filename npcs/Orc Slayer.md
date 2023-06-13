---
cssclass: [monsters]
title1: Orc Slayer
title2: Orc Slayer
CR: 7
sources:
- name: NPC Codex
  page: 131
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Elf
classes:
- ranger 8
alignment: CN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 22
  touch: 15
  flat_footed: 18
  components:
    armor: 5
    deflection: 1
    dex: 4
    natural: 2
HP:
  HP: 62
  long: 8d10+14
saves:
  fort: 8
  ref: 13
  will: 4
  other: +2 vs. enchantments
immunities:
- sleep
resistances:
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk elven curve blade +15/+10 (1d10+1/18-20)
      entries:
      - - damage: 1d10+1
          crit_range: 18-20
      attack: mwk elven curve blade
      bonus:
      - 15
      - 10
  ranged:
  - - text: +1 longbow +15/+10 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 longbow
      bonus:
      - 15
      - 10
  special:
  - favored enemy (animals +2, orcs +4)
spells:
  entries:
  - name: barkskin
    source: Ranger
    level: 2
  - name: cat's grace
    source: Ranger
    level: 2
  - name: entangle
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 5
    concentration: 6
tactics:
  Before Combat: The ranger casts barkskin, cat's grace, and resist energy (fire).
  During Combat: If ranger acts in the surprise round, she casts entangle. She prefers
    to attack at range and from cover.
  Base Statistics: Without barkskin, cat's grace, and resist energy, the ranger's
    statistics are Init +4; AC 20, touch 15, flat-footed 16; Ref +11; Melee mwk elven
    curve blade +13/+8 (1d10+1/18-20); Ranged +1 longbow +13/+8 (1d8+1/×3); Dex 19;
    CMD +24; Skills Acrobatics +11, Ride +10, Stealth +14.
ability_scores:
  STR: 13
  DEX: 23
  CON: 12
  INT: 12
  WIS: 12
  CHA: 8
BAB: 8
CMB: 9
CMD: 26
feats:
- name: Combat Reflexes
- name: Deadly Aim
- name: Endurance
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Weapon Finesse
skills:
  Acrobatics: 13
  Climb: 9
  Heal: 8
  Knowledge (dungeoneering): 6
  Knowledge (geography): 6
  Knowledge (nature): 8
  Perception: 14
  Ride: 12
  Stealth: 16
  Survival: 12
  Swim: 7
languages:
- Common
- Elven
- Orc
special_qualities:
- elven magic
- favored terrain (forest +4, plains +2)
- hunter's bond (companions)
- swift tracker
- track +4
- weapon familiarity
- wild empathy +7
- woodland stride
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 chain shirt
  - +1 longbow with 20 arrows
  - masterwork elven curve blade
  - cloak of resistance +1
  - ring of protection +1
  - 194 gp
desc_long: The orc slayer is driven by vengeance to kill all orcs.

---

# Orc Slayer

**Source** NPC Codex pg. 131
**XP** 3,200
Elf _[[classes/Ranger|ranger]]_ 8

CN Medium humanoid (elf)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 armor, +1 _[[spells/Deflection|deflection]]_, +4 Dex, +2 natural)
**hp** 62 (8d10+14)
**Fort** +8, **Ref** +13, **Will** +4; +2 vs. enchantments
**Immune** sleep; **Resist** fire 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Elven curve blade|elven curve blade]]_ +15/+10 (1d10+1/18–20)
**Ranged** +1 _[[items/Weapon/Longbow|longbow]]_ +15/+10 (1d8+1/×3)
**Special Attacks** favored enemy (animals +2, orcs +4)
**_Ranger_ Spells Prepared **(CL 5th; concentration +6)
2nd—_[[spells/Barkskin|barkskin]]_, cat’s _[[spells/Grace|grace]]_
1st—_[[spells/Entangle|entangle]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, cat’s _grace_, and _resist energy_ (fire).
**During Combat **If _ranger_ acts in the surprise round, she casts _entangle_. She prefers to attack at range and from cover.
**Base Statistics **Without _barkskin_, cat’s _grace_, and _resist energy_, the _ranger_’s statistics are **Init **+4; **AC **20, touch 15, _flat-footed_ 16; **Ref **+11; **Melee **mwk _elven curve blade_ +13/+8 (1d10+1/18–20); **Ranged** +1 _longbow_ +13/+8 (1d8+1/×3); **Dex **19; **CMD **+24; **Skills **Acrobatics +11, Ride +10, Stealth +14.

##### Statistics
**Str** 13, **Dex** 23, **Con** 12, **Int** 12, **Wis** 12, **Cha** 8
**Base Atk** +8; **CMB** +9; **CMD** 26
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +13, _[[universal monster rules/Climb|Climb]]_ +9, _[[spells/Heal|Heal]]_ +8, Knowledge (dungeoneering, geography) +6, Knowledge (nature) +8, Perception +14, Ride +12, Stealth +16, Survival +12, Swim +7
**Languages** Common, Elven, _[[monsters/Orc|Orc]]_
**SQ** elven magic, favored terrain (forest +4, plains +2), _[[classes/Hunter|hunter]]_’s bond (companions), swift tracker, track +4, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +7, woodland stride
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _longbow_ with 20 arrows, masterwork _elven curve blade_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 194 gp

The _[[npcs/Orc Slayer|orc slayer]]_ is driven by _[[feats/Vengeance|vengeance]]_ to kill all orcs.