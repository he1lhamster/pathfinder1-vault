---
cssclass: [monsters]
title1: Ogre, Ogre Priest
title2: Ogre Priest
CR: 4
sources:
- name: Monster Codex
  page: 154
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1200
race: Ogre
classes:
- cleric 2
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: -2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 19
  touch: 7
  flat_footed: 19
  components:
    armor: 6
    dex: -2
    natural: 6
    size: -1
HP:
  HP: 51
  long: 6d8+24
saves:
  fort: 11
  ref: -1
  will: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk greatsword +11 (3d6+10/19-20)
      entries:
      - - damage: 3d6+10
          crit_range: 19-20
      attack: mwk greatsword
      bonus:
      - 11
  ranged:
  - - text: javelin +1 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: javelin
      bonus:
      - 1
  special:
  - channel negative energy 1/day (DC 9, 1d6)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 4/day
    other: '+1'
  - name: vision of madness
    source: default
    freq: 4/day
    other: +/-1
  sources:
  - name: default
    CL: 2
    concentration: 3
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: enlarge person
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 2
    concentration: 3
    slots:
      0: at-will
    domains:
    - madness
    - strength
ability_scores:
  STR: 25
  DEX: 6
  CON: 19
  INT: 8
  WIS: 12
  CHA: 7
BAB: 4
CMB: 12
CMD: 20
feats:
- name: Combat Casting
- name: Iron Will
- name: Power Attack
skills:
  Perception: 7
  Spellcraft: 4
languages:
- Giant
gear:
  combat:
  - potion of cure light wounds
  - potion of invisibility
  - scroll of cure moderate wounds
  - alchemist's fire (2)
  other:
  - mwk breastplate
  - javelins (3)
  - mwk greatsword
  - amulet of natural armor +1
  - unholy symbol
  - 157 gp
ecology:
  environment: temperate or cold hills
desc_long: Ogres belittle those who value smarts over strength, but clever ogres find
  their own paths to power.

---

# Ogre, Ogre Priest

**Source** Monster Codex pg. 154
**XP** 1,200
_[[monsters/Ogre|Ogre]]_ _[[classes/Cleric|cleric]]_ 2
CE Large humanoid (giant)
**Init** –2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 19, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+6 armor, –2 Dex, +6 natural, –1 size)
**hp** 51 (6d8+24)
**Fort** +11, **Ref** –1, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Greatsword|greatsword]]_ +11 (3d6+10/19–20)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +1 (1d8+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 1/day (DC 9, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +3)
4/day—strength surge (+1), _[[spells/Vision|vision]]_ of madness (+/–1)
**_Cleric_ Spells Prepared **(CL 2nd; concentration +3)
1st—_[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Enlarge Person|enlarge person]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mending|mending]]_, stabilize
**D** domain spell; **Domains** Madness, Strength

##### Statistics
**Str** 25, **Dex** 6, **Con** 19, **Int** 8, **Wis** 12, **Cha** 7
**Base Atk** +4; **CMB** +12; **CMD** 20
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Perception +7, Spellcraft +4
**Languages** Giant
**Combat Gear** potion of _cure light wounds_, potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** mwk _[[items/Armor/Breastplate|breastplate]]_, javelins (3), mwk _greatsword_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 157 gp

##### Ecology

**Environment** temperate or cold hills

##### Description

Ogres belittle those who value smarts over strength, but clever ogres find their own paths to power.