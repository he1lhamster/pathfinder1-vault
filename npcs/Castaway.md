---
cssclass: [monsters]
title1: Castaway
title2: Castaway
CR: 11
sources:
- name: NPC Codex
  page: 71
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 12800
race: Half-orc
classes:
- druid 12
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 15
  flat_footed: 17
  components:
    armor: 3
    deflection: 1
    dex: 3
    dodge: 1
    shield: 3
HP:
  HP: 79
  long: 12d8+22
saves:
  fort: 11
  ref: 9
  will: 14
  other: +4 vs. fey and plant-targeted effects
defensive_abilities:
- orc ferocity
immunities:
- poison
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 scimitar +12/+7 (1d6+3/18-20)
      entries:
      - - damage: 1d6+3
          crit_range: 18-20
      attack: +1 scimitar
      bonus:
      - 12
      - 7
  - - text: mwk club +12/+7 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: mwk club
      bonus:
      - 12
      - 7
  ranged:
  - - text: dart +12/+7 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: dart
      bonus:
      - 12
      - 7
  special:
  - wild shape 5/day
spell_like_abilities:
  entries:
  - name: lightning lord
    source: default
    freq: 12/day
  - name: storm burst
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 12
    concentration: 16
spells:
  entries:
  - is_domain_spell: true
    name: control winds
    source: Druid
    level: 6
    DC: 20
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: repel wood
    source: Druid
    level: 6
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 19
  - name: cure critical wounds
    source: Druid
    level: 5
  - is_domain_spell: true
    name: ice storm
    source: Druid
    level: 5
  - name: tree stride
    source: Druid
    level: 5
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 18
  - name: freedom of movement
    source: Druid
    level: 4
  - is_domain_spell: true
    name: sleet storm
    source: Druid
    level: 4
  - is_domain_spell: true
    name: call lightning
    source: Druid
    level: 3
    DC: 17
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
    count: 3
  - name: protection from energy
    source: Druid
    level: 3
    DC: 17
  - name: barkskin
    source: Druid
    level: 2
    count: 2
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
    name: fog cloud
    source: Druid
    level: 2
  - name: endure elements
    source: Druid
    level: 1
  - name: entangle
    source: Druid
    level: 1
    DC: 15
  - name: faerie fire
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: detect magic
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  - name: virtue
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 12
    concentration: 16
    slots:
      0: at-will
    domains:
    - weather
tactics:
  Before Combat: The druid casts liveoak every 12 days and endure elements every morning.
  During Combat: The druid commands his treant to protect him while he wild shapes
    into a Huge air elemental and casts freedom of movement, barkskin, and greater
    magic fang. He then spontaneously uses summon nature's ally VI to summon a dire
    tiger, upon which he casts animal growth, barkskin, greater magic fang, and cat's
    grace.
ability_scores:
  STR: 14
  DEX: 16
  CON: 13
  INT: 10
  WIS: 18
  CHA: 8
BAB: 9
CMB: 11
CMD: 26
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Power Attack
- name: Spell Focus (conjuration)
skills:
  Climb: 8
  Fly: 9
  Handle Animal: 5
  Heal: 11
  Intimidate: 1
  Knowledge (nature): 13
  Linguistics: 3
  Perception: 17
  Sense Motive: 9
  Survival: 15
  Swim: 7
special_qualities:
- nature bond (Weather domain)
- nature sense
- orc blood
- trackless step
- weapon familiarity
- wild empathy +11
- woodland stride
gear:
  combat:
  - potion of haste
  - scroll of plant growth
  other:
  - +1 light fortification leather armor
  - +1 darkwood heavy steel shield
  - +1 scimitar
  - darts (5)
  - masterwork club
  - brooch of shielding
  - cloak of resistance +2
  - headband of inspired wisdom +2
  - ring of protection +1
  - healer's kit
  - holly and mistletoe
  - spell component pouch
  - 273 gp
desc_long: By way of a shipwreck or magical transportation, some druids find themselves
  alone on far-flung islands.

---

# Castaway

**Source** NPC Codex pg. 71
**XP** 12,800
Half-orc _[[classes/Druid|druid]]_ 12

LN Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +17

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +3 _[[spells/Shield|shield]]_)
**hp** 79 (12d8+22)
**Fort** +11, **Ref** +9, **Will** +14; +4 vs. fey and plant-targeted effects
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Immune** poison

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Scimitar|scimitar]]_ +12/+7 (1d6+3/18–20) or mwk _[[items/Weapon/Club|club]]_ +12/+7 (1d6+2)
**Ranged** _[[items/Weapon/Dart|dart]]_ +12/+7 (1d4+2)
**Special Attacks** wild shape 5/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
12/day—lightning lord
7/day—storm burst
**_Druid_ Spells Prepared **(CL 12th; concentration +16)
6th—control windsD (DC 20), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Repel Wood|repel wood]]_
5th—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 19), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Tree Stride|tree stride]]_
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _dispel magic_, _[[spells/Flame Strike|flame strike]]_ (DC 18), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Sleet Storm|sleet storm]]_
3rd—call lightningD (DC 17), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, greater _[[spells/Magic Fang|magic fang]]_ (3), _[[spells/Protection from Energy|protection from energy]]_ (DC 17)
2nd—_[[spells/Barkskin|barkskin]]_ (2), bear’s _[[feats/Endurance|endurance]]_, bull’s strength, cat’s _[[spells/Grace|grace]]_, _[[spells/Fog Cloud|fog cloud]]_
1st—_[[spells/Endure Elements|endure elements]]_, _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, stabilize, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domain **Weather

### Tactics

**Before Combat **The _druid_ casts _[[spells/Liveoak|liveoak]]_ every 12 days and _endure elements_ every morning.
**During Combat **The _druid_ commands his _[[monsters/Treant|treant]]_ to protect him while he wild shapes into a Huge air elemental and casts _freedom of movement_, _barkskin_, and greater _magic fang_. He then spontaneously uses _[[universal monster rules/Summon|summon]]_ nature’s ally VI to _summon_ a dire _[[monsters/Tiger|tiger]]_, upon which he casts _[[spells/Animal Growth|animal growth]]_, _barkskin_, greater _magic fang_, and cat’s _grace_.

##### Statistics
**Str** 14, **Dex** 16, **Con** 13, **Int** 10, **Wis** 18, **Cha** 8
**Base Atk** +9; **CMB** +11; **CMD** 26
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration)
**Skills** _[[universal monster rules/Climb|Climb]]_ +8, Fly +9, Handle Animal +5, _[[spells/Heal|Heal]]_ +11, Intimidate +1, Knowledge (nature) +13, Linguistics +3, Perception +17, Sense Motive +9, Survival +15, Swim +7
**SQ** nature bond (Weather domain), nature sense, _orc_ blood, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +11, woodland stride
**Combat Gear** potion of _[[spells/Haste|haste]]_, scroll of _[[spells/Plant Growth|plant growth]]_; **Other Gear** +1 light _[[universal monster rules/Fortification|fortification]]_ _[[items/Armor/Leather armor|leather armor]]_, +1 darkwood _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _scimitar_, darts (5), masterwork _club_, _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 273 gp

By way of a shipwreck or magical transportation, some druids find themselves alone on far-flung islands.