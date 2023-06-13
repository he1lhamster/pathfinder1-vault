---
cssclass: [monsters]
title1: Initiate of Flame
title2: Initiate of Flame
CR: 1/2
sources:
- name: NPC Codex
  page: 62
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 200
race: Dwarf
classes:
- druid 1
alignment: LN
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 0
AC:
  AC: 14
  touch: 10
  flat_footed: 14
  components:
    armor: 4
HP:
  HP: 15
  long: 1d8+7
saves:
  fort: 5
  ref: 0
  will: 4
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: spear +2 (1d8+3/×3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: spear
      bonus:
      - 2
  ranged:
  - - text: sling +0 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: sling
      bonus:
      - 0
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
spell_like_abilities:
  entries:
  - name: fire bolt
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 1
    concentration: 3
spells:
  entries:
  - name: burning handsD
    source: Druid
    level: 1
    DC: 13
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - name: detect poison
    source: Druid
    level: 0
  - name: flare
    source: Druid
    level: 0
    DC: 12
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 1
    concentration: 3
    slots:
      0: at-will
    domains:
    - fire
tactics:
  Before Combat: The druid casts endure elements each day.
  During Combat: The druid casts faerie fire, then drops a smokestick at his feet,
    letting foes come to him, and possibly sets his spear against a charge. He then
    fights with his spear or casts burning hands.
ability_scores:
  STR: 15
  DEX: 10
  CON: 16
  INT: 12
  WIS: 15
  CHA: 6
BAB: 0
CMB: 2
CMD: 12
CMD_other: 16 vs. bull rush or trip
feats:
- name: Toughness
skills:
  Climb: 4
  Handle Animal: 2
  Knowledge (geography): 5
  Knowledge (nature): 3
  Perception: 6
    to notice unusual stonework: 8
  Survival: 8
languages:
- Common
- Druidic
- Dwarven
- Giant
special_qualities:
- nature bond (Fire domain)
- nature sense
- wild empathy -1
gear:
  combat:
  - alchemist's fire (2)
  - smokesticks (2)
  other:
  - masterwork hide armor
  - sling with 20 bullets
  - spear
  - climber's kit
  - healer's kit
  - holly and mistletoe
  - spell component pouch
  - 8 gp
desc_long: These hostile guardians of volcanic mountain regions have tempers to match
  their fiery environs, and tolerate no intruders.

---

# Initiate of Flame

**Source** NPC Codex pg. 62
**XP** 200
Dwarf _[[classes/Druid|druid]]_ 1

LN Medium humanoid (dwarf)
**Init** +0; **Senses** Perception +6

##### Defense

**AC** 14, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor)
**hp** 15 (1d8+7)
**Fort** +5, **Ref** +0, **Will** +4; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Spear|spear]]_ +2 (1d8+3/×3)
**Ranged** _[[items/Weapon/Sling|sling]]_ +0 (1d4+2)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids
**_Spell-Like Abilities_** (CL 1st; concentration +3)
5/day—fire bolt
**_Druid_ Spells Prepared **(CL 1st; concentration +3)
1st—_[[items/Weapon Magic Abilities/Burning|burning]]_ handsD (DC 13), _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_
0 (at will)—_[[spells/Detect Poison|detect poison]]_, _[[spells/Flare|flare]]_ (DC 12), stabilize
**D **Domain spell; **Domain **Fire

### Tactics

**Before Combat **The _druid_ casts _endure elements_ each day.
**During Combat **The _druid_ casts _faerie fire_, then drops a _[[items/Mundane/Smokestick|smokestick]]_ at his feet, letting foes come to him, and possibly sets his _spear_ against a charge. He then fights with his _spear_ or casts _[[spells/Burning Hands|burning hands]]_.

##### Statistics
**Str** 15, **Dex** 10, **Con** 16, **Int** 12, **Wis** 15, **Cha** 6
**Base Atk** +0; **CMB** +2; **CMD** 12 (16 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Toughness|Toughness]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +4, Handle Animal +2, Knowledge (geography) +5, Knowledge (nature) +3, Perception +6 (+8 to notice unusual stonework), Survival +8
**Languages** Common, Druidic, Dwarven, Giant
**SQ** nature bond (Fire domain), nature sense, wild _[[feats/Empathy|empathy]]_ –1
**Combat Gear** _[[classes/Alchemist|alchemist]]_’s fire (2), smokesticks (2); **Other Gear** masterwork _[[items/Armor/Hide armor|hide armor]]_, _sling_ with 20 bullets, _spear_, climber’s kit, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 8 gp

These hostile guardians of _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ mountain regions have tempers to match their fiery environs, and tolerate no intruders.