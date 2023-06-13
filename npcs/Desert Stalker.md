---
cssclass: [monsters]
title1: Desert Stalker
title2: Desert Stalker
CR: 13
sources:
- name: NPC Codex
  page: 137
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Half-orc
classes:
- ranger 14
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 27
  touch: 14
  flat_footed: 25
  components:
    armor: 6
    deflection: 2
    dex: 1
    dodge: 1
    natural: 4
    shield: 3
HP:
  HP: 130
  long: 14d10+49
saves:
  fort: 14
  ref: 12
  will: 8
defensive_abilities:
- evasion
- orc ferocity
immunities:
- fire (120 points)
resistances:
  electricity: 30
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 scimitar +18/+13/+8 (1d6+6/15-20)
      entries:
      - - damage: 1d6+6
          crit_range: 15-20
      attack: +1 scimitar
      bonus:
      - 18
      - 13
      - 8
    - text: +2 light shield +21/+16 (1d3+7 plus bull rush)
      entries:
      - - damage: 1d3+7
        - effect: bull rush
      attack: +2 light shield
      bonus:
      - 21
      - 16
  ranged:
  - - text: mwk composite longbow +16/+11/+6 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 16
      - 11
      - 6
  special:
  - favored enemy (animals +2, humans +4, magical beasts +4)
spells:
  entries:
  - name: freedom of movement
    source: Ranger
    level: 4
  - name: neutralize poison
    source: Ranger
    level: 3
  - name: barkskin
    source: Ranger
    level: 2
  - name: protection from energy
    source: Ranger
    level: 2
  - name: wind wall
    source: Ranger
    level: 2
  - name: endure elements
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
    CL: 11
    concentration: 13
tactics:
  Before Combat: The ranger casts barkskin, endure elements, freedom of movement,
    longstrider, pass without trace, protection from energy (fire), and resist energy
    (electricity).
  During Combat: The ranger casts wind wall to separate foes, then uses Improved Shield
    Bash to manipulate positioning.
  Base Statistics: Without barkskin, longstrider, protection from energy, and resist
    energy, the ranger's statistics are AC 23, touch 14, flat-footed 21; Immune none;
    Resist none; Speed 30 ft.; Skills Acrobatics +11.
ability_scores:
  STR: 20
  DEX: 13
  CON: 16
  INT: 10
  WIS: 14
  CHA: 8
BAB: 14
CMB: 19
CMD: 33
feats:
- name: Blind-Fight
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Improved Critical (scimitar)
- name: Improved Initiative
- name: Improved Shield Bash
- name: Improved Two-Weapon Fighting
- name: Power Attack
- name: Shield Master
- name: Shield Slam
- name: Two-Weapon Fighting
skills:
  Acrobatics: 11
    when jumping: 15
  Climb: 13
  Diplomacy: 4
  Handle Animal: 7
  Heal: 10
  Intimidate: 1
  Knowledge (geography): 8
  Knowledge (nature): 13
  Perception: 19
  Ride: 9
  Sense Motive: 5
  Stealth: 18
  Survival: 15
languages:
- Common
- Orc
special_qualities:
- camouflage
- favored terrain (desert +6, mountain +2, urban +2)
- hunter's bond (companions)
- orc blood
- quarry
- swift tracker
- track +7
- weapon familiarity
- wild empathy +13
- woodland stride
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of fly
  - potion of haste
  - scrolls of neutralize poison (2)
  - wand of cure moderate wounds (20 charges)
  other:
  - +2 chain shirt
  - +2 light wooden shield
  - +1 scimitar
  - masterwork composite longbow (+5 Str) with 20 arrows
  - belt of giant strength +2
  - cloak of resistance +2
  - ring of protection +2
  - 981 gp
desc_long: The desert stalker snares his prey and bleeds it dry.

---

# Desert Stalker

**Source** NPC Codex pg. 137
**XP** 25,600
Half-orc _[[classes/Ranger|ranger]]_ 14

LE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19

##### Defense

**AC** 27, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+6 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural, +3 _[[spells/Shield|shield]]_)
**hp** 130 (14d10+49)
**Fort** +14, **Ref** +12, **Will** +8
**Defensive Abilities** evasion, _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Immune** fire (120 points); **Resist** electricity 30

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Scimitar|scimitar]]_ +18/+13/+8 (1d6+6/15–20), +2 light _shield_ +21/+16 (1d3+7 plus bull rush)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +16/+11/+6 (1d8+5/×3)
**Special Attacks** favored enemy (animals +2, humans +4, magical beasts +4)
**_Ranger_ Spells Prepared **(CL 11th; concentration +13)
4th—_[[spells/Freedom of Movement|freedom of movement]]_
3rd—_[[spells/Neutralize Poison|neutralize poison]]_
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Endure Elements|endure elements]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, _endure elements_, _freedom of movement_, _longstrider_, _pass without trace_, _protection from energy_ (fire), and _resist energy_ (electricity).
**During Combat **The _ranger_ casts _wind wall_ to separate foes, then uses _[[feats/Improved _Shield_ Bash|Improved _Shield_ Bash]]_ to manipulate positioning.
**Base Statistics **Without _barkskin_, _longstrider_, _protection from energy_, and _resist energy_, the _ranger_’s statistics are **AC **23, touch 14, _flat-footed_ 21; **Immune **none; **Resist **none; **Speed **30 ft.; **Skills **Acrobatics +11.

##### Statistics
**Str** 20, **Dex** 13, **Con** 16, **Int** 10, **Wis** 14, **Cha** 8
**Base Atk** +14; **CMB** +19; **CMD** 33
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _Dodge_, _[[feats/Double Slice|Double Slice]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scimitar_), _[[feats/Improved Initiative|Improved Initiative]]_, _Improved _Shield_ Bash_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Shield Master|Shield Master]]_, _[[feats/Shield Slam|Shield Slam]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_
**Skills** Acrobatics +11 (+15 when jumping), _[[universal monster rules/Climb|Climb]]_ +13, Diplomacy +4, Handle Animal +7, _[[spells/Heal|Heal]]_ +10, Intimidate +1, Knowledge (geography) +8, Knowledge (nature) +13, Perception +19, Ride +9, Sense Motive +5, Stealth +18, Survival +15
**Languages** Common, _Orc_
**SQ** camouflage, favored terrain (desert +6, mountain +2, urban +2), _[[classes/Hunter|hunter]]_’s bond (companions), _orc_ blood, quarry, swift tracker, track +7, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +13, woodland stride
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of fly, potion of _[[spells/Haste|haste]]_, scrolls of _neutralize poison_ (2), wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (20 charges); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 _[[items/Shield/Light wooden shield|light wooden shield]]_, +1 _scimitar_, masterwork _composite longbow_ (+5 Str) with 20 arrows, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 981 gp

The _[[npcs/Desert Stalker|desert stalker]]_ snares his prey and bleeds it dry.