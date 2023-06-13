---
cssclass: [monsters]
title1: Samsaran
desc_short: This serene-looking slender young man has pale blue skin and solid black
  eyes, and is dressed in simple robes.
title2: Samsaran
CR: 1/2
sources:
- name: Bestiary 4
  page: 230
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 200
race: Male
classes:
- samsaran oracle 1
alignment: N
size: Medium
type: humanoid
subtypes:
- samsaran
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    armor: 3
    dex: 2
HP:
  HP: 11
  long: 1d8+3
saves:
  fort: 0
  ref: 2
  will: 4
  other: +2 vs. death effects, negative energy effects, negative levels
speeds:
  base: 30
attacks:
  melee:
  - - text: spear -1 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: spear
      bonus:
      - -1
  ranged:
  - - text: sling +2 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: sling
      bonus:
      - 2
spell_like_abilities:
  entries:
  - name: comprehend languages
    source: default
    freq: 1/day
  - name: deathwatch
    source: default
    freq: 1/day
  - name: stabilize
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 1
    concentration: 3
spells:
  entries:
  - name: command
    source: Oracle
    level: 1
    DC: 13
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: sanctuary
    source: Oracle
    level: 1
    DC: 13
  - name: ghost sound
    source: Oracle
    level: 0
    DC: 12
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: mage hand
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 1
    concentration: 3
    slots:
      1: 4
      0: at-will
    mystery: lore
ability_scores:
  STR: 8
  DEX: 14
  CON: 11
  INT: 12
  WIS: 14
  CHA: 15
BAB: 0
CMB: -1
CMD: 11
feats:
- name: Toughness
skills:
  Diplomacy: 6
  Disable Device: 7
  Heal: 6
  Knowledge (religion): 5
  Perception: 8
  Spellcraft: 5
  _racial_mods:
    Disable Device:
      _: 2
    Perception:
      _: 2
languages:
- Celestial
- Common
- Draconic
- Samsaran
special_qualities:
- lifebound
- oracle's curse (haunted)
- revelations (think on it)
- shards of the past (Disable Device, Perception)
ecology:
  environment: any land
  organization: solitary or clan (3-12)
  treasure_type: NPC Gear
  treasure:
  - studded leather
  - spear
  - sling with 10 bullets
  - thieves' tools
  - other treasure
desc_long: |-
  Samsarans are a race of humanoids whose spirits naturally reincarnate into another samsaran upon death. They have dark hair, pale bluish skin, and eyes with no visible pupil or iris. A samsaran's blood is clear like water.

  Each samsaran is born with the knowledge that it has lived before, and shall continue onward after death through the cycle of reincarnation. When a samsaran dies, its body fades from sight, and another samsaran child appears somewhere and matures at the normal rate. Samsarans can reproduce with humans and produce true human offspring.

  Typical samsarans pursue simple, ascetic lives apart from mainstream society. They live in small isolated farming communities as individuals or couples, with older samsarans adopting newly manifested children. Some work as consultants, mediators, prophets, or seers.

---

# Samsaran
This serene-looking slender young man has pale blue skin and solid black eyes, and is dressed in simple robes.
**Source** Bestiary 4 pg. 230
**XP** 200
Male _[[monsters/Samsaran|samsaran]]_ _[[classes/Oracle|oracle]]_ 1

N Medium humanoid (_samsaran_)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +2 Dex)
**hp** 11 (1d8+3)
**Fort** +0, **Ref** +2, **Will** +4; +2 vs. death effects, negative energy effects, negative levels

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Spear|spear]]_ –1 (1d6–1)
**Ranged** _[[items/Weapon/Sling|sling]]_ +2 (1d4–1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +3)
1/day—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Deathwatch|deathwatch]]_, stabilize
**_Oracle_ Spells Known **(CL 1st; concentration +3)
1st (4/day)—_[[spells/Command|command]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 13)
0 (at will)—_[[spells/Ghost Sound|ghost sound]]_ (DC 12), _[[spells/Guidance|guidance]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Mystery** lore

##### Statistics
**Str** 8, **Dex** 14, **Con** 11, **Int** 12, **Wis** 14, **Cha** 15
**Base Atk** +0; **CMB** –1; **CMD** 11
**Feats** _[[feats/Toughness|Toughness]]_
**Skills** Diplomacy +6, Disable Device +7, _[[spells/Heal|Heal]]_ +6, Knowledge (religion) +5, Perception +8, Spellcraft +5; **Racial Modifiers** +2 Disable Device, +2 Perception
**Languages** Celestial, Common, Draconic, _Samsaran_
**SQ** _[[feats/Lifebound|lifebound]]_, _oracle_’s curse (haunted), revelations (think on it), shards of the past (Disable Device, Perception)

##### Ecology

**Environment** any land
**Organization** solitary or clan (3–12)
**Treasure** NPC gear (studded leather, _spear_, _sling_ with 10 bullets, thieves’ tools, other treasure)

##### Description

Samsarans are a race of humanoids whose spirits naturally _[[spells/Reincarnate|reincarnate]]_ into another _samsaran_ upon death. They have dark hair, pale bluish skin, and eyes with no visible pupil or iris. A _samsaran_’s blood is clear like water.

Each _samsaran_ is born with the knowledge that it has lived before, and shall continue onward after death through the cycle of reincarnation. When a _samsaran_ dies, its body fades from sight, and another _samsaran_ child appears somewhere and matures at the normal rate. Samsarans can reproduce with humans and produce true human offspring.

Typical samsarans pursue simple, ascetic lives apart from mainstream society. They live in small isolated farming communities as individuals or couples, with older samsarans adopting newly manifested children. Some work as consultants, mediators, prophets, or seers.