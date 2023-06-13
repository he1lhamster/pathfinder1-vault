---
cssclass: [monsters]
title1: Earthfather
title2: Earthfather
CR: 19
sources:
- name: NPC Codex
  page: 79
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Dwarf
classes:
- druid 20
alignment: NE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 1
AC:
  AC: 33
  touch: 16
  flat_footed: 31
  components:
    armor: 12
    deflection: 3
    dex: 1
    dodge: 1
    insight: 1
    shield: 5
HP:
  HP: 150
  long: 20d8+57
saves:
  fort: 17
  ref: 10
  will: 22
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- evasion
immunities:
- acid
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 ghost touch quarterstaff +19/+14/+9 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: +1 ghost touch quarterstaff
      bonus:
      - 19
      - 14
      - 9
  ranged:
  - - text: +1 light hammer +17/+12/+7 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: +1 light hammer
      bonus:
      - 17
      - 12
      - 7
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - wild shape at will
spell_like_abilities:
  entries:
  - name: acid dart
    source: default
    freq: 10/day
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - name: quickened cure critical wounds
    source: Druid
    level: 9
    count: 2
  - name: elemental swarmD
    source: Druid
    level: 9
    other: earth spell only
  - name: empowered fire storm
    source: Druid
    level: 9
    DC: 24
  - name: storm of vengeance
    source: Druid
    level: 9
    DC: 27
  - is_domain_spell: true
    name: earthquake
    source: Druid
    level: 8
  - name: finger of death
    source: Druid
    level: 8
    DC: 25
  - name: repel metal or stone
    source: Druid
    level: 8
  - name: reverse gravity
    source: Druid
    level: 8
  - name: word of recall
    source: Druid
    level: 8
  - name: changestaff
    source: Druid
    level: 7
  - name: creeping doom
    source: Druid
    level: 7
    DC: 25
  - is_domain_spell: true
    name: elemental body IV
    source: Druid
    level: 7
    other: earth only
  - name: heal
    source: Druid
    level: 7
  - name: mass cure moderate wounds
    source: Druid
    level: 7
  - name: true seeing
    source: Druid
    level: 7
  - name: antilife shell
    source: Druid
    level: 6
  - name: empowered flame strike
    source: Druid
    level: 6
    DC: 21
  - name: greater dispel magic
    source: Druid
    level: 6
    count: 2
  - is_domain_spell: true
    name: stoneskin
    source: Druid
    level: 6
  - name: animal growth
    source: Druid
    level: 5
    count: 2
    DC: 22
  - name: death ward
    source: Druid
    level: 5
  - name: quickened obscuring mist
    source: Druid
    level: 5
  - is_domain_spell: true
    name: wall of stone
    source: Druid
    level: 5
  - name: wall of thorns
    source: Druid
    level: 5
  - name: air walk
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 21
  - name: freedom of movement
    source: Druid
    level: 4
    count: 2
  - is_domain_spell: true
    name: spike stones
    source: Druid
    level: 4
    DC: 21
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: dominate animal
    source: Druid
    level: 3
    DC: 20
  - name: greater magic fang
    source: Druid
    level: 3
    count: 3
  - is_domain_spell: true
    name: stone shape
    source: Druid
    level: 3
  - name: wind wall
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: bear's endurance
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: soften earth and stone
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: magic stone
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 20
    concentration: 27
    slots:
      0: at-will
    domains:
    - earth
tactics:
  Before Combat: The druid casts shambler to create 1d4+2 advanced shambling mounds.
  During Combat: The druid deploys shambling mounds, wild shapes into a Huge earth
    elemental, and casts spells on himself. If interrupted, he earth glides and casts
    storm of vengeance.
ability_scores:
  STR: 16
  DEX: 13
  CON: 14
  INT: 10
  WIS: 24
  CHA: 6
BAB: 15
CMB: 18
CMD: 34
CMD_other: 38 vs. bull rush or trip
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Heavy Armor Proficiency
- name: Natural Spell
- name: Power Attack
- name: Quicken Spell
- name: Spell Focus (conjuration)
- name: Vital Strike
skills:
  Fly: 3
  Handle Animal: 3
  Knowledge (engineering): 4
  Knowledge (nature): 15
  Knowledge (planes): 8
  Linguistics: 4
  Perception: 22
    to notice unusual stonework: 24
  Perform (percussion): 4
  Ride: 3
  Spellcraft: 21
  Survival: 19
  Swim: 5
languages:
- Aquan
- Auran
- Common
- Druidic
- Dwarven
- Ignan
- Terran
special_qualities:
- a thousand faces
- nature bond (Earth domain)
- nature sense
- timeless body
- trackless step
- wild empathy +18
- woodland stride
gear:
  gear:
  - +3 wild ironwood full plate
  - +3 animated darkwood heavy wooden shield
  - +1 ghost touch quarterstaff
  - +1 light hammer
  - boots of speed
  - cloak of resistance +3
  - dusty rose prism ioun stone
  - headband of inspired wisdom +4
  - ring of evasion
  - ring of protection +3
  - holly and mistletoe
  - spell component pouch
  - 487 gp
desc_long: Providers of ancient wisdom, these rare and powerful dwarven druids are
  venerated by their people.

---

# Earthfather

**Source** NPC Codex pg. 79
**XP** 204,800
Dwarf _[[classes/Druid|druid]]_ 20

NE Medium humanoid (dwarf)
**Init** +1; **Senses** Perception +22

##### Defense

**AC** 33, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+12 armor, +3 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +1 insight, +5 _[[spells/Shield|shield]]_)
**hp** 150 (20d8+57)
**Fort** +17, **Ref** +10, **Will** +22; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), evasion; **Immune** acid, poison

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ _[[items/Weapon/Quarterstaff|quarterstaff]]_ +19/+14/+9 (1d6+5)
**Ranged** +1 _[[items/Weapon/Light hammer|light hammer]]_ +17/+12/+7 (1d4+4)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, wild shape at will
**_Spell-Like Abilities_** (CL 20th; concentration +27)
10/day—acid _[[items/Weapon/Dart|dart]]_
**_Druid_ Spells Prepared **(CL 20th; concentration +27)
9th—quickened _[[spells/Cure Critical Wounds|cure critical wounds]]_ (2), elemental swarmD (earth spell only), empowered _[[spells/Fire Storm|fire storm]]_ (DC 24), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 27)
8th—_[[spells/Earthquake|earthquake]]_, _[[spells/Finger Of Death|finger of death]]_ (DC 25), _[[spells/Repel Metal or Stone|repel metal or stone]]_, _[[spells/Reverse Gravity|reverse gravity]]_, _[[spells/Word of Recall|word of recall]]_
7th—_[[spells/Changestaff|changestaff]]_, _[[spells/Creeping Doom|creeping doom]]_ (DC 25), elemental body IVD (earth only), _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/True Seeing|true seeing]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, empowered _[[spells/Flame Strike|flame strike]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_ (2), _[[spells/Stoneskin|stoneskin]]_
5th—_[[spells/Animal Growth|animal growth]]_ (2, DC 22), _[[spells/Death Ward|death ward]]_, quickened _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Wall Of Stone|wall of stone]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Air Walk|air walk]]_, _dispel magic_, _flame strike_ (DC 21), _[[spells/Freedom of Movement|freedom of movement]]_ (2), spike stonesD (DC 21)
3rd—_cure moderate wounds_, _[[spells/Dominate Animal|dominate animal]]_ (DC 20), greater _[[spells/Magic Fang|magic fang]]_ (3), _[[spells/Stone Shape|stone shape]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Barkskin|barkskin]]_ (3), bear’s _[[feats/Endurance|endurance]]_, bull’s strength, cat’s _[[spells/Grace|grace]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Magic Stone|magic stone]]_, _obscuring mist_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, stabilize
**D **Domain spell; **Domain **Earth

### Tactics

**Before Combat **The _druid_ casts _[[spells/Shambler|shambler]]_ to create 1d4+2 advanced shambling mounds.
**During Combat **The _druid_ deploys shambling mounds, wild shapes into a Huge earth elemental, and casts spells on himself. If interrupted, he earth glides and casts _storm of vengeance_.

##### Statistics
**Str** 16, **Dex** 13, **Con** 14, **Int** 10, **Wis** 24, **Cha** 6
**Base Atk** +15; **CMB** +18; **CMD** 34 (38 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +3, Handle Animal +3, Knowledge (engineering) +4, Knowledge (nature) +15, Knowledge (planes) +8, Linguistics +4, Perception +22 (+24 to notice unusual stonework), Perform (percussion) +4, Ride +3, Spellcraft +21, Survival +19, Swim +5
**Languages** Aquan, Auran, Common, Druidic, Dwarven, Ignan, Terran
**SQ** a thousand faces, nature bond (Earth domain), nature sense, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +18, woodland stride
**Gear** +3 wild _[[spells/Ironwood|ironwood]]_ _[[items/Armor/Full plate|full plate]]_, +3 _[[items/Armor Magic Abilities/Animated|animated]]_ darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _ghost touch_ _quarterstaff_, +1 _light hammer_, _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Evasion|ring of evasion]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 487 gp

Providers of ancient wisdom, these rare and powerful dwarven druids are venerated by their people.