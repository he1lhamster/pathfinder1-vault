---
cssclass: [monsters]
title1: Troglodyte, Troglodyte Priest
title2: Troglodyte Priest
CR: 3
sources:
- name: Monster Codex
  page: 215
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Troglodyte
classes:
- cleric 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: -1
senses:
  darkvision: 90
auras:
- name: stench
  radius: 30
  DC: 14
  duration: 10 rounds
AC:
  AC: 19
  touch: 9
  flat_footed: 19
  components:
    armor: 4
    dex: -1
    natural: 6
HP:
  HP: 30
  long: 5d8+8
saves:
  fort: 7
  ref: 0
  will: 5
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 obsidian spiked gauntlet +10 (1d4+6)
      entries:
      - - damage: 1d4+6
      attack: +1 obsidian spiked gauntlet
      bonus:
      - 10
    - text: bite +3 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: bite
      bonus:
      - 3
    - text: claw +3 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: claw
      bonus:
      - 3
  - - text: bite +8 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: bite
      bonus:
      - 8
    - text: 2 claws +8 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 8
  ranged:
  - - text: javelin +2 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: javelin
      bonus:
      - 2
  special:
  - channel negative energy 4/day (DC 14, 2d6)
  - fury of the Abyss (+1, 5/day)
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 5/day
    other: '+1'
  sources:
  - name: default
    CL: 3
    concentration: 5
spells:
  entries:
  - name: amplify stench
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: bull's strength
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 14
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 13
  - is_domain_spell: true
    name: doom
    source: Cleric
    level: 1
    DC: 13
  - name: magic weapon
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 12
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 3
    concentration: 5
    slots:
      0: at-will
    domains:
    - evil (demon subdomain)
    - strength
tactics:
  Before Combat: The priest casts amplify stench and bull's strength on herself, and
    magic weapon on her spiked gauntlet.
  Base Statistics: Without amplify stench, bull's strength, and magic weapon, the
    priest's statistics are Aura stench (30 ft., DC 12, 10 rounds); Melee mwk obsidian
    spiked gauntlet +8 (1d4+3), bite +1 (1d4+3), claw +1 (1d4+3), or bite +6 (1d4+3),
    2 claws +6 (1d4+3); Ranged javelin +2 (1d6+3); Str 16; CMB +6; CMD 15.
ability_scores:
  STR: 20
  DEX: 9
  CON: 12
  INT: 10
  WIS: 15
  CHA: 13
BAB: 3
CMB: 8
CMD: 17
feats:
- name: Combat Casting
- name: Improved Channel
- name: Weapon Focus (spiked gauntlet)
skills:
  Heal: 7
  Knowledge (planes): 4
  Knowledge (religion): 6
  Sense Motive: 7
  Spellcraft: 5
  Stealth: 1
    in rocky areas: 5
  Perception: 2
languages:
- Draconic
gear:
  combat:
  - potions of cure moderate wounds (2)
  - scroll of spiritual weapon
  - wand of cure light wounds (20 charges)
  - thunderstone
  other:
  - mwk hide armor
  - javelins (6)
  - mwk obsidian spiked gauntlet
  - wooden holy symbol
  - 96 gp
ecology:
  environment: any underground
desc_long: Troglodyte divine spellcasters act as spiritual advisors for their tribes.
  Troglodyte clerics usually worship demon lords, particularly those associated with
  caverns and reptiles.

---

# Troglodyte, Troglodyte Priest

**Source** Monster Codex pg. 215
**XP** 800
_[[monsters/Troglodyte|Troglodyte]]_ _[[classes/Cleric|cleric]]_ 3
CE Medium humanoid (reptilian)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft.; Perception +2
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 14, 10 rounds)

##### Defense

**AC** 19, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 armor, –1 Dex, +6 natural)
**hp** 30 (5d8+8)
**Fort** +7, **Ref** +0, **Will** +5

##### Offense
**Speed** 20 ft.
**Melee** +1 obsidian _[[items/Weapon/Spiked gauntlet|spiked gauntlet]]_ +10 (1d4+6), bite +3 (1d4+5), claw +3 (1d4+5) or bite +8 (1d4+5), 2 claws +8 (1d4+5)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +2 (1d6+5)
**Special Attacks** channel negative energy 4/day (DC 14, 2d6), fury of the Abyss (+1, 5/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +5)
5/day—strength surge (+1)
**_Cleric_ Spells Prepared **(CL 3rd; concentration +5)
2nd—_[[spells/Amplify Stench|amplify stench]]_, bull’s strength, _[[spells/Hold Person|hold person]]_ (DC 14)
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 13), _[[spells/Doom|doom]]_ (DC 13), _[[spells/Magic Weapon|magic weapon]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 12), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Spark|spark]]_
**D** domain spell; **Domains** Evil (Demon subdomain), Strength

### Tactics

**Before Combat** The priest casts _amplify stench_ and bull’s strength on herself, and _magic weapon_ on her _spiked gauntlet_.
 **Base Statistics** Without _amplify stench_, bull’s strength, and _magic weapon_, the priest’s statistics are **Aura** _stench_ (30 ft., DC 12, 10 rounds); **Melee **mwk obsidian _spiked gauntlet_ +8 (1d4+3), bite +1 (1d4+3), claw +1 (1d4+3), or bite +6 (1d4+3), 2 claws +6 (1d4+3); **Ranged **_javelin_ +2 (1d6+3); **Str **16; **CMB **+6; **CMD **15.

##### Statistics
**Str** 20, **Dex** 9, **Con** 12, **Int** 10, **Wis** 15, **Cha** 13
**Base Atk** +3; **CMB** +8; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spiked gauntlet_)
**Skills** _[[spells/Heal|Heal]]_ +7, Knowledge (planes) +4, Knowledge (religion) +6, Sense Motive +7, Spellcraft +5, Stealth +1 (+5 in rocky areas)
**Languages** Draconic
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), scroll of _[[spells/Spiritual Weapon|spiritual weapon]]_, wand of _[[spells/Cure Light Wounds|cure light wounds]]_ (20 charges), _[[items/Mundane/Thunderstone|thunderstone]]_; **Other Gear** mwk _[[items/Armor/Hide armor|hide armor]]_, javelins (6), mwk obsidian _spiked gauntlet_, wooden holy symbol, 96 gp

##### Ecology

**Environment** any underground

##### Description

_Troglodyte_ divine spellcasters act as spiritual advisors for their tribes. _Troglodyte_ clerics usually worship demon lords, particularly those associated with caverns and reptiles.