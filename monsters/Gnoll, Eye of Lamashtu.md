---
cssclass: [monsters]
title1: Gnoll, Eye of Lamashtu
title2: Eye of Lamashtu
CR: 5
sources:
- name: Monster Codex
  page: 97
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Gnoll
classes:
- cleric of Lamashtu 4
alignment: CE
size: Medium
type: humanoid
subtypes:
- gnoll
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 11
  flat_footed: 17
  components:
    armor: 5
    dex: 1
    natural: 2
HP:
  HP: 31
  long: 6d8+4
saves:
  fort: 7
  ref: 2
  will: 7
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk falchion +8 (2d4+4/18-20)
      entries:
      - - damage: 2d4+4
          crit_range: 18-20
      attack: mwk falchion
      bonus:
      - 8
  ranged:
  - - text: javelin +5 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: javelin
      bonus:
      - 5
  special:
  - channel negative energy 6/day (DC 15, 2d6)
spell_like_abilities:
  entries:
  - name: copycat
    source: default
    freq: 6/day
    other: 4 rounds
  - name: strength surge
    source: default
    freq: 6/day
    other: '+2'
  sources:
  - name: default
    CL: 4
    concentration: 7
spells:
  entries:
  - name: death knell
    source: Cleric
    level: 2
    DC: 15
  - superscripts:
    - UM
    name: dread bolt
    source: Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 14
  - name: doom
    source: Cleric
    level: 1
    DC: 14
  - is_domain_spell: true
    name: enlarge person
    source: Cleric
    level: 1
    DC: 14
  - name: entropic shield
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: ray of sickening
    source: Cleric
    level: 1
    DC: 14
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: guidance
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 4
    concentration: 7
    slots:
      0: at-will
    domains:
    - strength
    - trickery
ability_scores:
  STR: 17
  DEX: 12
  CON: 10
  INT: 8
  WIS: 16
  CHA: 12
BAB: 4
CMB: 7
CMD: 18
feats:
- name: Combat Casting
- name: Extra Channel
- name: Improved Channel
skills:
  Spellcraft: 8
  Perception: 3
languages:
- Gnoll
gear:
  combat:
  - potion of cure light wounds
  - wand of cure light wounds (50 charges)
  - alchemist's fire (2)
  other:
  - mwk scale mail
  - javelins (2)
  - mwk falchion
  - amulet of natural armor +1
  - 33 gp
ecology:
  environment: warm plains or desert
desc_long: Gnolls revere Lamashtu above all other gods.

---

# Gnoll, Eye of Lamashtu

**Source** Monster Codex pg. 97
**XP** 1,600
_[[monsters/Gnoll|Gnoll]]_ _[[classes/Cleric|cleric]]_ of Lamashtu 4
CE Medium humanoid (_gnoll_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +3

##### Defense

**AC** 18, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +1 Dex, +2 natural)
**hp** 31 (6d8+4)
**Fort** +7, **Ref** +2, **Will** +7

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Falchion|falchion]]_ +8 (2d4+4/18–20)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +5 (1d6+3)
**Special Attacks** channel negative energy 6/day (DC 15, 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +7)
6/day—copycat (4 rounds), strength surge (+2)
**_Cleric_ Spells Prepared **(CL 4th; concentration +7)
2nd—_[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Dread Bolt|dread bolt]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Invisibility|invisibility]]_
1st—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Doom|doom]]_ (DC 14), _[[spells/Enlarge Person|enlarge person]]_ (DC 14), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Ray of Sickening|ray of sickening]]_ (DC 14)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize
**D** domain spell; **Domains** Strength, Trickery

##### Statistics
**Str** 17, **Dex** 12, **Con** 10, **Int** 8, **Wis** 16, **Cha** 12
**Base Atk** +4; **CMB** +7; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Channel|Improved Channel]]_
**Skills** Spellcraft +8
**Languages** _Gnoll_
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, wand of _cure light wounds_ (50 charges), _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** mwk _[[items/Armor/Scale mail|scale mail]]_, javelins (2), mwk _falchion_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, 33 gp

##### Ecology

**Environment** warm plains or desert

##### Description

Gnolls revere Lamashtu above all other gods.