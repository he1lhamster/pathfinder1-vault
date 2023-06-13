---
cssclass: [monsters]
title1: Giant-Killer
title2: Giant-Killer
CR: 10
sources:
- name: NPC Codex
  page: 134
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Gnome
classes:
- ranger 11
alignment: NE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 15
  flat_footed: 21
  components:
    armor: 6
    deflection: 1
    dex: 2
    dodge: 1
    natural: 3
    size: 1
HP:
  HP: 116
  long: 11d10+51
saves:
  fort: 12
  ref: 10
  will: 6
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- evasion
immunities:
- poison
resistances:
  fire: 20
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 gnome hooked hammer +13/+8/+3 (1d6+3/19-20/×3)
      entries:
      - - damage: 1d6+3
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 gnome hooked hammer
      bonus:
      - 13
      - 8
      - 3
    - text: mwk gnome hooked hammer +13 (1d4+2/19-20/×4)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
          crit_multiplier: 4
      attack: mwk gnome hooked hammer
      bonus:
      - 13
  - - text: mwk longspear +15/+10/+5 (1d6+3/×3)
      entries:
      - - damage: 1d6+3
          crit_multiplier: 3
      attack: mwk longspear
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: mwk composite longbow +15/+10/+5 (1d6+2/×3)
      entries:
      - - damage: 1d6+2
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 15
      - 10
      - 5
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - favored enemy (earth outsiders +2, giants +6, oozes +2)
spells:
  entries:
  - name: cure moderate wounds
    source: Ranger
    level: 3
  - name: barkskin
    source: Ranger
    level: 2
  - name: bear's endurance
    source: Ranger
    level: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: entangle
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 8
    concentration: 10
tactics:
  Before Combat: The ranger casts barkskin, bear's endurance, delay poison, and resist
    energy (fire).
  During Combat: If facing multiple opponents with reach, the ranger uses Lunge.
  Base Statistics: Without barkskin, bear's endurance, delay poison, and resist energy,
    the ranger's statistics are hp 94; Fort +10; AC 21, touch 15, flat-footed 18;
    Immune none; Resist none; Con 14.
ability_scores:
  STR: 14
  DEX: 14
  CON: 18
  INT: 10
  WIS: 14
  CHA: 10
BAB: 11
CMB: 12
CMD: 26
feats:
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Improved Critical (gnome hooked hammer)
- name: Lunge
- name: Mobility
- name: Power Attack
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
- name: Vital Strike
skills:
  Acrobatics: 17
    when jumping: 13
  Climb: 8
  Knowledge (dungeoneering): 5
  Knowledge (local): 5
  Knowledge (geography): 8
  Knowledge (nature): 8
  Linguistics: 1
  Perception: 18
  Stealth: 19
  Survival: 16
  Swim: 8
languages:
- Common
- Giant
- Gnome
special_qualities:
- favored terrain (mountain +2, underground +4)
- hunter's bond (companions)
- quarry
- swift tracker
- track +5
- wild empathy +11
- woodland stride
gear:
  combat:
  - potion of invisibility
  - scroll of cure serious wounds
  other:
  - +2 chain shirt
  - +1/masterwork gnome hooked hammer
  - masterwork composite longbow (+3 Str) with 20 arrows
  - boots of elvenkind
  - cloak of resistance +1
  - ring of protection +1
  - 630 gp
desc_long: The giant-killer is trained to kill monsters many times her size, using
  speed, specialized weapons, and time honored techniques to bring down even the most
  daunting foes.

---

# Giant-Killer

**Source** NPC Codex pg. 134
**XP** 9,600
Gnome _[[classes/Ranger|ranger]]_ 11

NE Small humanoid (gnome)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +18

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+6 armor, +1 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural, +1 size)
**hp** 116 (11d10+51)
**Fort** +12, **Ref** +10, **Will** +6; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), evasion; **Immune** poison; **Resist** fire 20

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Gnome hooked hammer|gnome hooked hammer]]_ +13/+8/+3 (1d6+3/19–20/×3), mwk _gnome hooked hammer_ +13 (1d4+2/19–20/×4) or mwk _[[items/Weapon/Longspear|longspear]]_ +15/+10/+5 (1d6+3/×3)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +15/+10/+5 (1d6+2/×3)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, favored enemy (earth outsiders +2, giants +6, oozes +2)
**_Ranger_ Spells Prepared **(CL 8th; concentration +10)
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Entangle|entangle]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, bear’s _endurance_, _delay poison_, and _resist energy_ (fire).
**During Combat **If facing multiple opponents with reach, the _ranger_ uses _[[feats/Lunge|Lunge]]_.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _delay poison_, and _resist energy_, the _ranger_’s statistics are **hp **94; **Fort **+10; **AC **21, touch 15, _flat-footed_ 18; **Immune **none; **Resist **none; **Con **14.

##### Statistics
**Str** 14, **Dex** 14, **Con** 18, **Int** 10, **Wis** 14, **Cha** 10
**Base Atk** +11; **CMB** +12; **CMD** 26
**Feats** _Dodge_, _[[feats/Double Slice|Double Slice]]_, _Endurance_, _[[feats/Improved Critical|Improved Critical]]_ (_gnome hooked hammer_), _Lunge_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +17 (+13 when jumping), _[[universal monster rules/Climb|Climb]]_ +8, Knowledge (dungeoneering, local) +5, Knowledge (geography, nature) +8, Linguistics +1, Perception +18, Stealth +19, Survival +16, Swim +8
**Languages** Common, Giant, Gnome
**SQ** favored terrain (mountain +2, underground +4), _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +5, wild _[[feats/Empathy|empathy]]_ +11, woodland stride
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Cure Serious Wounds|cure serious wounds]]_; **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +1/masterwork _gnome hooked hammer_, masterwork _composite longbow_ (+3 Str) with 20 arrows, _[[items/Wondrous Item/Boots of Elvenkind|boots of elvenkind]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 630 gp

The _[[npcs/Giant-Killer|giant-killer]]_ is trained to kill monsters many times her size, using speed, specialized weapons, and time honored techniques to bring down even the most daunting foes.