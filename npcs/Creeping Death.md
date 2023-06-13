---
cssclass: [monsters]
title1: Creeping Death
title2: Creeping Death
CR: 14
sources:
- name: NPC Codex
  page: 74
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Elf
classes:
- druid 15
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 31
  touch: 16
  flat_footed: 27
  components:
    armor: 7
    deflection: 2
    dex: 3
    dodge: 1
    natural: 5
    shield: 3
HP:
  HP: 96
  long: 15d8+25
saves:
  fort: 12
  ref: 10
  will: 16
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
defensive_abilities:
- 25% chance to negate critical hits and sneak attacks
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
immunities:
- poison
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 cold iron scythe +13/+8/+3 (2d4+2/×4)
      entries:
      - - damage: 2d4+2
          crit_multiplier: 4
      attack: +1 cold iron scythe
      bonus:
      - 13
      - 8
      - 3
  special:
  - wild shape 6/day
spell_like_abilities:
  entries:
  - name: wooden fist
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 15
    concentration: 20
spells:
  entries:
  - is_domain_spell: true
    name: control plants
    source: Druid
    level: 8
    DC: 23
  - name: word of recall
    source: Druid
    level: 8
  - is_domain_spell: true
    name: animate plants
    source: Druid
    level: 7
  - name: creeping doom
    source: Druid
    level: 7
    DC: 22
  - name: true seeing
    source: Druid
    level: 7
  - name: antilife shell
    source: Druid
    level: 6
  - name: mass cure light wounds
    source: Druid
    level: 6
  - is_domain_spell: true
    name: repel wood
    source: Druid
    level: 6
  - name: wall of stone
    source: Druid
    level: 6
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 20
  - name: insect plague
    source: Druid
    level: 5
  - name: stoneskin
    source: Druid
    level: 5
  - name: transmute rock to mud
    source: Druid
    level: 5
  - name: tree stride
    source: Druid
    level: 5
  - is_domain_spell: true
    name: wall of thorns
    source: Druid
    level: 5
  - name: air walk
    source: Druid
    level: 4
  - is_domain_spell: true
    name: command plants
    source: Druid
    level: 4
    DC: 19
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: rusting grasp
    source: Druid
    level: 4
  - name: scrying
    source: Druid
    level: 4
    DC: 19
  - name: daylight
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - is_domain_spell: true
    name: plant growth
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
    count: 2
    DC: 18
  - is_domain_spell: true
    name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: bear's endurance
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - name: longstrider
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: entangle
    source: Druid
    level: 1
    DC: 16
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: detect magic
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 15
    concentration: 20
    slots:
      0: at-will
    domains:
    - plant
tactics:
  Before Combat: The druid casts stoneskin, barkskin, and longstrider and drinks her
    potion of haste.
  During Combat: The druid locks down opponents with entangle, wall of stone, and
    transmute rock to mud, while casting creeping doom and animate plants from a distance.
  Base Statistics: Without stoneskin, barkskin, and longstrider, the druid's statistics
    are AC 27, touch 16, flat-footed 23; DR none; Speed 20 ft.
ability_scores:
  STR: 13
  DEX: 16
  CON: 12
  INT: 12
  WIS: 20
  CHA: 8
BAB: 11
CMB: 12
CMD: 28
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Natural Spell
- name: Power Attack
- name: Spell Penetration
skills:
  Climb: 5
  Fly: 7
  Handle Animal: 9
  Heal: 13
  Knowledge (geography): 10
  Knowledge (nature): 14
  Knowledge (planes): 9
  Perception: 18
  Ride: 6
  Spellcraft: 14
    to identify magic item properties: 16
  Survival: 19
  Swim: 5
languages:
- Abyssal
- Common
- Druidic
- Elven
special_qualities:
- a thousand faces
- bramble armor (1d6+7, 15 rounds/day)
- elven magic
- nature bond (Plant domain)
- nature sense
- timeless body
- trackless step
- weapon familiarity
- wild empathy +14
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - potion of haste
  - scroll of heal
  other:
  - +1 dragonhide breastplate
  - +1 light fortification heavy wooden shield
  - +1 cold iron scythe
  - amulet of natural armor +1
  - cloak of resistance +2
  - headband of inspired wisdom +4
  - pearl of power (1st)
  - ring of protection +2
  - holly and mistletoe
  - spell component pouch
  - 652 gp
desc_long: Creeping death druids see terrain as the ultimate weapon against those
  who would despoil their homes.

---

# Creeping Death

**Source** NPC Codex pg. 74
**XP** 38,400
Elf _[[classes/Druid|druid]]_ 15

NE Medium humanoid (elf)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +18

##### Defense

**AC** 31, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+7 armor, +2 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural, +3 _[[spells/Shield|shield]]_)
**hp** 96 (15d8+25)
**Fort** +12, **Ref** +10, **Will** +16; +2 vs. enchantments, +4 vs. fey and plant-targeted effects
**Defensive Abilities** 25% chance to negate critical hits and sneak attacks; **DR** 10/adamantine (150 points); **Immune** poison, sleep

##### Offense
**Speed** 30 ft.
**Melee** +1 cold iron _[[items/Weapon/Scythe|scythe]]_ +13/+8/+3 (2d4+2/×4)
**Special Attacks** wild shape 6/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
8/day—wooden fist
**_Druid_ Spells Prepared **(CL 15th; concentration +20)
8th—control plantsD (DC 23), _[[spells/Word of Recall|word of recall]]_
7th—_[[spells/Animate Plants|animate plants]]_, _[[spells/Creeping Doom|creeping doom]]_ (DC 22), _[[spells/True Seeing|true seeing]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, mass _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Repel Wood|repel wood]]_, _[[spells/Wall Of Stone|wall of stone]]_
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Insect Plague|insect plague]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_, _[[spells/Tree Stride|tree stride]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Command|command]]_ plantsD (DC 19), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Scrying|scrying]]_ (DC 19)
3rd—_[[spells/Daylight|daylight]]_, greater _[[spells/Magic Fang|magic fang]]_ (2), _[[spells/Plant Growth|plant growth]]_, _[[spells/Protection from Energy|protection from energy]]_ (2, DC 18)
2nd—barkskinD (3), bear’s _[[feats/Endurance|endurance]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Longstrider|longstrider]]_
1st—_cure light wounds_ (2), _[[conditions/Entangled|entangleD]]_ (DC 16), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domain **Plant

### Tactics

**Before Combat **The _druid_ casts _stoneskin_, _[[spells/Barkskin|barkskin]]_, and _longstrider_ and drinks her potion of _[[spells/Haste|haste]]_.
**During Combat **The _druid_ locks down opponents with _[[spells/Entangle|entangle]]_, _wall of stone_, and _transmute rock to mud_, while casting _creeping doom_ and _animate plants_ from a distance.
**Base Statistics **Without _stoneskin_, _barkskin_, and _longstrider_, the _druid_’s statistics are **AC **27, touch 16, _flat-footed_ 23; **DR **none; **Speed **20 ft.

##### Statistics
**Str** 13, **Dex** 16, **Con** 12, **Int** 12, **Wis** 20, **Cha** 8
**Base Atk** +11; **CMB** +12; **CMD** 28
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +5, Fly +7, Handle Animal +9, _[[spells/Heal|Heal]]_ +13, Knowledge (geography) +10, Knowledge (nature) +14, Knowledge (planes) +9, Perception +18, Ride +6, Spellcraft +14 (+16 to _[[spells/Identify|identify]]_ magic item properties), Survival +19, Swim +5
**Languages** Abyssal, Common, Druidic, Elven
**SQ** a thousand faces, bramble armor (1d6+7, 15 rounds/day), elven magic, nature bond (Plant domain), nature sense, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +14, woodland stride
**Combat Gear** potion of _cure serious wounds_, potion of _haste_, scroll of _heal_; **Other Gear** +1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, +1 light _[[universal monster rules/Fortification|fortification]]_ _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 cold iron _scythe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, pearl of power (1st), _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 652 gp

_[[npcs/Creeping Death|Creeping death]]_ druids see terrain as the ultimate weapon against those who would despoil their homes.