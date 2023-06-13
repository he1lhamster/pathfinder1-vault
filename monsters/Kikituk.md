---
cssclass: [monsters]
title1: Kikituk
desc_short: This lumbering whale skeleton has a set of bony legs affixed toits frame.
  Its bones bear complex scrimshaw patterns.
title2: Kikituk
CR: 13
sources:
- name: Bestiary 6
  page: 177
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 25600
alignment: NE
size: Huge
type: construct
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: frightful presence
  radius: 60
  DC: 24
  duration: 2d4 rounds
AC:
  AC: 28
  touch: 14
  flat_footed: 26
  components:
    dex: 2
    natural: 14
    profane,-2 size: 4
HP:
  HP: 170
  long: 20d10+60
saves:
  fort: 12
  ref: 14
  will: 14
immunities:
- acid
- construct traits
speeds:
  base: 40
  swim: 60
attacks:
  melee:
  - - text: bite +27 (4d6+18)
      entries:
      - - damage: 4d6+18
      attack: bite
      bonus:
      - 27
    - text: 2 claws +27 (1d6+9)
      entries:
      - - damage: 1d6+9
      count: 2
      attack: claws
      bonus:
      - 27
  special:
  - shearing jaws
  - trample (2d6+13, DC 29)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: At will
  - name: enervation
    source: default
    freq: At will
    DC: 18
  - name: invisibility
    source: default
    freq: At will
  - name: quickened invisibility
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 29
  DEX: 14
  CON:
  INT: 12
  WIS: 19
  CHA: 19
BAB: 20
CMB: 31
CMB_other: +35 sunder
CMD: 47
CMD_other: 49 vs. sunder
feats:
- name: Great Fortitude
- name: Greater Sunder
- name: ImprovedInitiative
- name: Improved Lightning Reflexes
- name: Improved Sunder
- name: LightningReflexes
- name: PowerAttack
- name: QuickenSpell-Like Ability(invisibility)
- name: Toughness
- name: Vital Strike
skills:
  Intimidate: 14
  Perception: 24
  Stealth: 14
  Swim: 27
languages:
- Common
special_qualities:
- scrimshaw magic
ecology:
  environment: any
  organization: solitary
  treasure_type: none
special_abilities:
  Scrimshaw Magic (Sp, Su): When a kikituk is created, its creator inscribes three
    spells-ones that require no costly material components-as scrimshaw designs. One
    of these spells must be 2nd level or lower, and the other two must be 4th level
    or lower. The kikituk can use these spells as spell-like abilities (CL 12th) at
    will (its Quicken Spell-like Ability feat applies to the spell that's 2nd-level
    or lower). Erase removes one spell from a kikituk's scrimshaw unless it succeeds
    at a Fortitude save against the spell. If a kikituk's scrimshaw is removed in
    this manner, it loses access to that spell as a spell-like ability. If all three
    spells are removed, it runs amok, slaughtering the nearest living creatures with
    reckless abandon-even its creator. As long as it has at least one scrimshaw spell
    in place, a kikituk gains a profane bonus to AC and on all saving throws equal
    to its Charisma modifier (+4 for the typical kikituk).
  Shearing Jaws (Ex): A kikituk applies double its Strength modifier to its damage
    with a successful bite attack.
desc_long: Kikituks are constructs created by wicked spellcasters.

---

# Kikituk
This lumbering _[[monsters/Whale|whale]]_ skeleton has a set of bony legs affixed to

its frame. Its bones bear complex scrimshaw patterns.
**Source** Bestiary 6 pg. 177
**XP** 25,600

NE Huge construct
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 24, 2d4 rounds)

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+2 Dex, +14 natural, +4 profane,

–2 size)
**hp** 170 (20d10+60)
**Fort** +12, **Ref** +14, **Will** +14
**Immune** acid, _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** 40 ft., swim 60 ft.
**Melee** bite +27 (4d6+18), 2 claws +27 (1d6+9)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** shearing jaws, _[[universal monster rules/Trample|trample]]_ (2d6+13, DC 29)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_ (DC 18), _[[spells/Invisibility|invisibility]]_ 
3/day—quickened _invisibility_

##### Statistics
**Str** 29, **Dex** 14, **Con** —, **Int** 12, **Wis** 19, **Cha** 19
**Base Atk** +20; **CMB** +31 (+35 sunder); **CMD** 47 (49 vs. sunder)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Sunder|Greater Sunder]]_, Improved

Initiative, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Sunder|Improved Sunder]]_, Lightning

Reflexes, Power

Attack, Quicken

Spell-Like Ability

(_invisibility_), _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Intimidate +14, Perception +24, Stealth +14, Swim +27
**Languages** Common
**SQ** scrimshaw magic

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

### Special Abilities
**Scrimshaw Magic (Sp, Su)** When a _[[monsters/Kikituk|kikituk]]_ is created, its creator inscribes three spells—ones that require no costly material components—as scrimshaw designs. One of these spells must be 2nd level or lower, and the other two must be 4th level or lower. The _kikituk_ can use these spells as _spell-like abilities_ (CL 12th) at will (its _[[feats/Quicken Spell-Like Ability|Quicken Spell-like Ability]]_ feat applies to the spell that’s 2nd-level or lower). _[[spells/Erase|Erase]]_ removes one spell from a _kikituk_’s scrimshaw unless it succeeds at a Fortitude save against the spell. If a _kikituk_’s scrimshaw is removed in this manner, it loses access to that spell as a spell-like ability. If all three spells are removed, it runs amok, slaughtering the nearest living creatures with reckless abandon—even its creator. As long as it has at least one scrimshaw spell in place, a _kikituk_ gains a profane bonus to AC and on all saving throws equal to its Charisma modifier (+4 for the typical _kikituk_).
**Shearing Jaws (Ex)** A _kikituk_ applies double its Strength modifier to its damage with a successful bite attack.

##### Description

Kikituks are constructs created by wicked spellcasters.