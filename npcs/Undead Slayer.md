---
cssclass: [monsters]
title1: Undead Slayer
title2: Undead Slayer
CR: 15
sources:
- name: NPC Codex
  page: 139
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Human
classes:
- ranger 16
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 25
  touch: 14
  flat_footed: 23
  components:
    armor: 6
    deflection: 2
    dex: 2
    natural: 5
HP:
  HP: 132
  long: 16d10+40
saves:
  fort: 17
  ref: 15
  will: 10
defensive_abilities:
- improved evasion
immunities:
- cold (120 points)
- fire (120 points)
- poison
resistances:
  electricity: 30
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 holy scimitar +21/+16/+11/+6 (1d6+6/18-20)
      entries:
      - - damage: 1d6+6
          crit_range: 18-20
      attack: +1 holy scimitar
      bonus:
      - 21
      - 16
      - 11
      - 6
    - text: +1 undead-bane light hammer +21/+16/+11 (1d4+6)
      entries:
      - - damage: 1d4+6
      attack: +1 undead-bane light hammer
      bonus:
      - 21
      - 16
      - 11
  ranged:
  - - text: mwk composite longbow +19/+14/+9/+4 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 19
      - 14
      - 9
      - 4
  special:
  - favored enemy (aberrations +2, evil outsiders +2, humans +2, undead +8)
spells:
  entries:
  - name: freedom of movement
    source: Ranger
    level: 4
  - name: remove disease
    source: Ranger
    level: 3
    count: 2
  - name: barkskin
    source: Ranger
    level: 2
  - name: owl's wisdom
    source: Ranger
    level: 2
  - name: protection from energy
    source: Ranger
    level: 2
    count: 2
  - name: calm animals
    source: Ranger
    level: 1
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
    CL: 13
    concentration: 15
tactics:
  Before Combat: The ranger casts barkskin, delay poison, freedom of movement, longstrider,
    protection from energy (cold, fire), and resist energy (electricity).
  During Combat: The ranger allows herself to be surrounded by weak undead so she
    can use Great Cleave and Power Attack.
  Base Statistics: Without barkskin, delay poison, longstrider, protection from energy,
    and resist energy, the ranger's statistics are AC 20, touch 14, flat-footed 18;
    Immune none; Resist none; Speed 30 ft.; Skills Acrobatics +17.
ability_scores:
  STR: 20
  DEX: 14
  CON: 14
  INT: 10
  WIS: 14
  CHA: 8
BAB: 16
CMB: 21
CMD: 35
feats:
- name: Cleave
- name: Double Slice
- name: Endurance
- name: Great Fortitude
- name: Greater Two-Weapon Fighting
- name: Improved Two-Weapon Fighting
- name: Improved Vital Strike
- name: Point-Blank Shot
- name: Power Attack
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
- name: Vital Strike
- name: Weapon Focus (light hammer)
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 17
    when jumping: 21
  Climb: 13
  Heal: 15
  Knowledge (dungeoneering): 8
  Knowledge (local): 5
  Knowledge (planes): 5
  Knowledge (nature): 6
  Knowledge (religion): 15
  Perception: 21
  Perform (string): 1
  Ride: 10
  Spellcraft: 13
  Stealth: 21
  Survival: 15
  Swim: 13
languages:
- Common
special_qualities:
- camouflage
- favored terrain (forest +2, underground +4, urban +4)
- hunter's bond (companions)
- quarry
- swift tracker
- track +8
- wild empathy +15
- woodland stride
gear:
  combat:
  - necklace of fireballs (type I)
  - potion of blur
  - potion of bull's strength
  - potions of cure serious wounds (2)
  - potions of hide from undead (5)
  - potions of lesser restoration (2)
  - silversheen
  - alchemical silver arrows (20)
  - holy water (4)
  other:
  - +2 chain shirt
  - +1 holy scimitar
  - +1 undead-bane light hammer
  - masterwork composite longbow (+5 Str) with 20 arrows
  - belt of mighty constitution +2
  - cloak of resistance +3
  - ring of protection +2
  - 743 gp
desc_long: An undead slayer's sole purpose is to destroy undead.

---

# Undead Slayer

**Source** NPC Codex pg. 139
**XP** 51,200
Human _[[classes/Ranger|ranger]]_ 16

LG Medium humanoid (human)
**Init** +2; **Senses** Perception +21

##### Defense

**AC** 25, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+6 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +5 natural)
**hp** 132 (16d10+40)
**Fort** +17, **Ref** +15, **Will** +10
**Defensive Abilities** improved evasion; **Immune** cold (120 points), fire (120 points), poison; **Resist** electricity 30

##### Offense
**Speed** 40 ft.
**Melee** +1 holy _[[items/Weapon/Scimitar|scimitar]]_ +21/+16/+11/+6 (1d6+6/18–20), +1 undead-bane _[[items/Weapon/Light hammer|light hammer]]_ +21/+16/+11 (1d4+6)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +19/+14/+9/+4 (1d8+5/×3)
**Special Attacks** favored enemy (aberrations +2, evil outsiders +2, humans +2, undead +8)
**_Ranger_ Spells Prepared **(CL 13th; concentration +15)
4th—_[[spells/Freedom of Movement|freedom of movement]]_
3rd—_[[spells/Remove Disease|remove disease]]_ (2)
2nd—_[[spells/Barkskin|barkskin]]_, owl’s wisdom, _[[spells/Protection from Energy|protection from energy]]_ (2)
1st—_[[spells/Calm Animals|calm animals]]_, _[[spells/Delay Poison|delay poison]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, _delay poison_, _freedom of movement_, _longstrider_, _protection from energy_ (cold, fire), and _resist energy_ (electricity).
**During Combat **The _ranger_ allows herself to be surrounded by weak undead so she can use _[[feats/Great Cleave|Great Cleave]]_ and _[[feats/Power Attack|Power Attack]]_.
**Base Statistics **Without _barkskin_, _delay poison_, _longstrider_, _protection from energy_, and _resist energy_, the _ranger_’s statistics are **AC **20, touch 14, _flat-footed_ 18; **Immune **none; **Resist **none; **Speed **30 ft.; **Skills **Acrobatics +17.

##### Statistics
**Str** 20, **Dex** 14, **Con** 14, **Int** 10, **Wis** 14, **Cha** 8
**Base Atk** +16; **CMB** +21; **CMD** 35
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Double Slice|Double Slice]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _Power Attack_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light hammer_, _scimitar_)
**Skills** Acrobatics +17 (+21 when jumping), _[[universal monster rules/Climb|Climb]]_ +13, _[[spells/Heal|Heal]]_ +15, Knowledge (dungeoneering) +8, Knowledge (local, planes) +5, Knowledge (nature) +6, Knowledge (religion) +15, Perception +21, Perform (string) +1, Ride +10, Spellcraft +13, Stealth +21, Survival +15, Swim +13
**Languages** Common
**SQ** camouflage, favored terrain (forest +2, underground +4, urban +4), _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +8, wild _[[feats/Empathy|empathy]]_ +15, woodland stride
**Combat Gear** necklace of fireballs (type I), potion of _[[spells/Blur|blur]]_, potion of bull’s strength, potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potions of _[[spells/Hide from Undead|hide from undead]]_ (5), potions of lesser _[[spells/Restoration|restoration]]_ (2), _[[items/Wondrous Item/Silversheen|silversheen]]_, alchemical silver arrows (20), _[[items/Mundane/Holy water|holy water]]_ (4); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +1 holy _scimitar_, +1 undead-bane _light hammer_, masterwork _composite longbow_ (+5 Str) with 20 arrows, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 743 gp

An _[[npcs/Undead Slayer|undead slayer]]_’s sole purpose is to destroy undead.