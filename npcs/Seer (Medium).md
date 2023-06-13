---
cssclass: [monsters]
title1: Seer (Medium)
title2: Seer (Medium)
CR: 4
sources:
- name: GameMastery Guide
  page: 299
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 1200
race: Human
classes:
- cleric 5
alignment: N
size: Medium
type: humanoid
initiative:
  bonus: 1
AC:
  AC: 21
  touch: 11
  flat_footed: 20
  components:
    armor: 7
    dex: 1
    shield: 3
HP:
  HP: 22
  long: 5d8
saves:
  fort: 5
  ref: 3
  will: 8
speeds:
  base: 20
attacks:
  melee:
  - - text: light mace +2 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: light mace
      bonus:
      - 2
  ranged:
  - - text: dart +4 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: dart
      bonus:
      - 4
  special:
  - channel positive energy 7/day (DC 14, 3d6)
spell_like_abilities:
  entries:
  - name: calming touch
    source: default
    freq: 6/day
    other: 1d6+5 nonlethal
  - name: gentle rest
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 5
    concentration: 8
spells:
  entries:
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 16
  - name: helping hand
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: speak with dead
    source: Cleric
    level: 3
  - name: augury
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: gentle repose
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 15
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - name: comprehend languages
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: deathwatch
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 14
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 8
    slots:
      0: at-will
    domains:
    - community
    - repose
ability_scores:
  STR: 8
  DEX: 12
  CON: 10
  INT: 14
  WIS: 17
  CHA: 14
BAB: 3
CMB: 2
CMD: 13
feats:
- name: Alertness
- name: Extra Channel
- name: Shield Focus
- name: Turn Undead
skills:
  Diplomacy: 10
  Heal: 11
  Knowledge (planes): 9
  Knowledge (religion): 9
  Perception: 8
  Profession (midwife): 9
  Sense Motive: 13
  Spellcraft: 6
languages:
- Celestial
- Common
- Infernal
gear:
  gear:
  - +1 chainmail
  - heavy wooden shield
  - light mace
  - darts (2)
  - cloak of resistance +1
  - silver holy symbol
  - augury focus
npc_boon: A medium can cast
desc_long: |-
  augury, speak with dead, or gentle repose at no charge, or magical healing at a 10% discount.

  A medium is a speaker who bridges the worlds of the living and the dead. She proclaims rest and blesses gravesites, ushering in birth and consigning the dead to the ground, yet it is also her seance that recalls the shades of the lost and ensures the continuity of a community's past, present, and future.

  A medium could be a village priestess or wise woman, or can simply be used as a generic wandering cleric, or one of many low-to-mid-level priests staff ing a temple.

  A medium might be accompanied by two acolytes or a doomsayer (CR 5), or two cultists (CR 6). A medium and hedge wizard (CR 6), hermit (CR 7), or conjurist (CR 7) could preside over a forest oracle or be traveling mendicant mystics. A medium and two acolytes might accompany a priest (CR 9), while five or six mediums could form the entourage for a saint (CR 12) or high priest (CR 13).

---

# Seer (Medium)

**Source** GameMastery Guide pg. 299
**XP** 1,200
Human _[[classes/Cleric|cleric]]_ 5

N Medium humanoid
**Init** +1; **Senses** Perception +8

##### Defense

**AC** 21, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 armor, +1 Dex, +3 _[[spells/Shield|shield]]_)
**hp** 22 (5d8)
**Fort** +5, **Ref** +3, **Will** +8

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Light mace|light mace]]_ +2 (1d6–1)
**Ranged** _[[items/Weapon/Dart|dart]]_ +4 (1d4–1)
**Special Attacks** channel positive energy 7/day (DC 14, 3d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
6/day—_[[items/Armor Magic Abilities/Calming|calming]]_ touch (1d6+5 nonlethal), gentle rest
**_Cleric_ Spells Prepared **(CL 5th; concentration +8)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Helping Hand|helping hand]]_, _[[spells/Speak with Dead|speak with dead]]_
2nd—_[[spells/Augury|augury]]_, _[[spells/Gentle Repose|gentle repose]]_, _[[spells/Silence|silence]]_ (DC 15), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 14), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Deathwatch|deathwatch]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 14)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Community, Repose

##### Statistics
**Str** 8, **Dex** 12, **Con** 10, **Int** 14, **Wis** 17, **Cha** 14
**Base Atk** +3; **CMB** +2; **CMD** 13
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Shield Focus|Shield Focus]]_, _[[feats/Turn Undead|Turn Undead]]_
**Skills** Diplomacy +10, _[[spells/Heal|Heal]]_ +11, Knowledge (planes) +9, Knowledge (religion) +9, Perception +8, Profession (midwife) +9, Sense Motive +13, Spellcraft +6
**Languages** Celestial, Common, Infernal
**Gear** +1 _[[items/Armor/Chainmail|chainmail]]_, _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, _light mace_, darts (2), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, silver holy symbol, _augury_ focus

**Boon** A _medium_ can cast _augury_, _speak with dead_, or _gentle repose_ at no charge, or magical healing at a 10% discount.

A _medium_ is a speaker who bridges the worlds of the living and the dead. She proclaims rest and blesses gravesites, ushering in birth and consigning the dead to the ground, yet it is also her seance that recalls the _[[spells/Shades|shades]]_ of the lost and ensures the continuity of a community’s past, present, and future.

A _medium_ could be a village priestess or wise woman, or can simply be used as a generic wandering _cleric_, or one of many low-to-mid-level priests staff ing a temple.

A _medium_ might be accompanied by two acolytes or a _[[npcs/Doomsayer|doomsayer]]_ (CR 5), or two cultists (CR 6). A _medium_ and hedge _[[classes/Wizard|wizard]]_ (CR 6), _[[npcs/Hermit|hermit]]_ (CR 7), or conjurist (CR 7) could preside over a forest _[[classes/Oracle|oracle]]_ or be traveling mendicant mystics. A _medium_ and two acolytes might accompany a priest (CR 9), while five or six mediums could form the entourage for a saint (CR 12) or high priest (CR 13).