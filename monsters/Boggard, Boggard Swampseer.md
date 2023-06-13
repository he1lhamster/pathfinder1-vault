---
cssclass: [monsters]
title1: Boggard, Boggard Swampseer
title2: Boggard Swampseer
CR: 4
sources:
- name: Monster Codex
  page: 13
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1200
race: Boggard
classes:
- druid 3
alignment: NE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    armor: 3
    dex: 1
    natural: 3
HP:
  HP: 41
  long: 6d8+15
saves:
  fort: 8
  ref: 4
  will: 7
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: mwk club +8 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: mwk club
      bonus:
      - 8
    - text: tongue +1 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 1
      touch: true
  special:
  - icicle (1d6+1 cold damage, 5/day)
  - terrifying croak (DC 14)
spells:
  entries:
  - name: bull's strength
    source: Druid
    level: 2
  - is_domain_spell: true
    name: burst of nettles
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - name: entangle
    source: Druid
    level: 1
    DC: 13
  - superscripts:
    - APG
    name: hydraulic push
    source: Druid
    level: 1
  - name: longstrider
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 12
  - name: guidance
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: resistance
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 3
    concentration: 5
    slots:
      0: at-will
    domains:
    - swamp
ability_scores:
  STR: 15
  DEX: 13
  CON: 12
  INT: 10
  WIS: 15
  CHA: 12
BAB: 4
CMB: 6
CMD: 17
feats:
- name: Improved Initiative
- name: Toughness
- name: Weapon Focus (club)
skills:
  Acrobatics: 4
    when jumping: 20
  Handle Animal: 7
  Heal: 8
  Knowledge (nature): 8
  Perception: 12
  Stealth: 0
    in swamps: 8
  Survival: 10
  Swim: 10
languages:
- Boggard
- Druidic
special_qualities:
- hold breath
- nature bond (Swamp domain)
- nature sense
- swamp stride
- trackless step
- wild empathy +4
- woodland stride
gear:
  combat:
  - scroll of barkskin
  - scroll of fog cloud
  - wand of cure light wounds (30 charges)
  other:
  - +1 leather armor
  - mwk club
  - cloak of resistance +1
  - 240 gp
ecology:
  environment: temperate marshes
desc_long: These casters are often the children of the priest-king.

---

# Boggard, Boggard Swampseer

**Source** Monster Codex pg. 13
**XP** 1,200
_[[monsters/Boggard|Boggard]]_ _[[classes/Druid|druid]]_ 3

NE Medium humanoid (_boggard_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 armor, +1 Dex, +3 natural)
**hp** 41 (6d8+15)
**Fort** +8, **Ref** +4, **Will** +7

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +8 (1d6+3), tongue +1 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Special Attacks** icicle (1d6+1 cold damage, 5/day), terrifying croak (DC 14)
**_Druid_ Spells Prepared **(CL 3rd; concentration +5)
2nd—bull’s strength, _[[spells/Burst of Nettles|burst of nettles]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Entangle|entangle]]_ (DC 13), _[[spells/Hydraulic Push|hydraulic push]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Shillelagh|shillelagh]]_
0 (at will)—_[[spells/Flare|flare]]_ (DC 12), _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domain** Swamp

##### Statistics
**Str** 15, **Dex** 13, **Con** 12, **Int** 10, **Wis** 15, **Cha** 12
**Base Atk** +4; **CMB** +6; **CMD** 17
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_club_)
**Skills** Acrobatics +4 (+20 when jumping), Handle Animal +7, _[[spells/Heal|Heal]]_ +8, Knowledge (nature) +8, Perception +12, Stealth +0 (+8 in swamps), Survival +10, Swim +10
**Languages** _Boggard_, Druidic
**SQ** _[[universal monster rules/Hold Breath|hold breath]]_, nature bond (Swamp domain), nature sense, swamp stride, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +4, woodland stride
**Combat Gear** scroll of _[[spells/Barkskin|barkskin]]_, scroll of _[[spells/Fog Cloud|fog cloud]]_, wand of _[[spells/Cure Light Wounds|cure light wounds]]_ (30 charges); **Other Gear** +1 _[[items/Armor/Leather armor|leather armor]]_, mwk _club_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, 240 gp

##### Ecology

**Environment** temperate marshes

##### Description

These casters are often the children of the priest-king.