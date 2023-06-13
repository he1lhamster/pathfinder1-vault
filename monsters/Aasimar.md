---
cssclass: [monsters]
title1: Aasimar
desc_short: This supernaturally beautiful woman looks human, yet emanates a strange
  sense of calm and benevolence.
title2: Aasimar
CR: 1/2
sources:
- name: Pathfinder RPG Bestiary
  page: 7
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 200
race: Aasimar
classes:
- cleric 1
alignment: NG
size: Medium
type: outsider
subtypes:
- native
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    armor: 5
HP:
  HP: 11
  long: 1d8+3
saves:
  fort: 4
  ref: 0
  will: 5
resistances:
  acid: 5
  cold: 5
  electricity: 5
speeds:
  base: 30
  base_other: 20 ft. in armor
attacks:
  melee:
  - - text: heavy mace -1 (1d8-1)
      entries:
      - - damage: 1d8-1
      attack: heavy mace
      bonus:
      - -1
  ranged:
  - - text: light crossbow +0 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 0
  special:
  - channel positive energy (5/day, 1d6, DC 12); rebuke death (1d4+1, 6/day); touch
    of good (6/day)
spell_like_abilities:
  entries:
  - name: daylight
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 1
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - is_domain_spell: true
    name: protection from evil
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    slots:
      0: at-will
    domains:
    - good
    - healing
ability_scores:
  STR: 8
  DEX: 10
  CON: 14
  INT: 13
  WIS: 17
  CHA: 14
BAB: 0
CMB: -1
CMD: 9
feats:
- name: Turn Undead
skills:
  Diplomacy: 8
  Heal: 7
  Knowledge (religion): 5
  Perception: 5
  _racial_mods:
    Diplomacy:
      _: 2
    Perception:
      _: 2
languages:
- Celestial
- Common
- Draconic
ecology:
  environment: any land
  organization: solitary, pair, or team (3-6)
  treasure_type: NPC Gear
  treasure:
  - scale mail
  - heavy mace
  - light crossbow with 10 bolts
  - other treasure
desc_long: Aasimars are humans with a significant amount of celestial or other good
  outsider blood in their ancestry. Aasimars are not always good, but it is a natural
  tendency for them, and they gravitate to good faiths or organizations associated
  with celestials. Aasimar heritage can hide for generations, only to appear suddenly
  in the child of two apparently human parents. Most societies interpret aasimar births
  as good omens. Aasimars look mostly human except for some minor physical trait that
  reveals their unusual heritage. Typical aasimar features are hair that shines like
  metal, unusual eye or skin color, or even glowing golden halos.

---

# Aasimar
This supernaturally beautiful woman looks human, yet emanates a strange sense of calm and benevolence.
**Source** Pathfinder RPG Bestiary pg. 7
**XP** 200
_[[monsters/Aasimar|Aasimar]]_ _[[classes/Cleric|cleric]]_ 1

NG Medium outsider (native)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +5

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor)
**hp** 11 (1d8+3)
**Fort** +4, **Ref** +0, **Will** +5
**Resist** acid 5, cold 5, electricity 5

##### Offense
**Speed** 30 ft. (20 ft. in armor)
**Melee** _[[items/Weapon/Heavy mace|heavy mace]]_ -1 (1d8-1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +0 (1d8/19-20)
**Special Attacks** channel positive energy (5/day, 1d6, DC 12); _[[spells/Rebuke|rebuke]]_ death (1d4+1, 6/day); touch of good (6/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st)
1/day - _[[spells/Daylight|daylight]]_
**Spells Prepared** (CL 1st)
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 14), _[[spells/Protection From Evil|protection from evil]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, stabilize
**D** domain spell; **Domains** Good, Healing

##### Statistics
**Str** 8, **Dex** 10, **Con** 14, **Int** 13, **Wis** 17, **Cha** 14
**Base Atk** +0; **CMB** -1; **CMD** 9
**Feats** _[[feats/Turn Undead|Turn Undead]]_
**Skills** Diplomacy +8, _[[spells/Heal|Heal]]_ +7, Knowledge (religion) +5; **Racial Modifiers** +2 Diplomacy, +2 Perception
**Languages** Celestial, Common, Draconic

##### Ecology

**Environment** any land
**Organization** solitary, pair, or team (3-6)
**Treasure** NPC gear (_[[items/Armor/Scale mail|scale mail]]_, _heavy mace_, _light crossbow_ with 10 bolts, other treasure)

##### Description

Aasimars are humans with a significant amount of celestial or other good outsider blood in their ancestry. Aasimars are not always good, but it is a natural tendency for them, and they gravitate to good faiths or organizations associated with celestials. _Aasimar_ heritage can hide for generations, only to appear suddenly in the child of two apparently human parents. Most societies interpret _aasimar_ births as good omens. Aasimars look mostly human except for some minor physical trait that reveals their unusual heritage. Typical _aasimar_ features are hair that shines like metal, unusual eye or skin color, or even glowing golden halos.