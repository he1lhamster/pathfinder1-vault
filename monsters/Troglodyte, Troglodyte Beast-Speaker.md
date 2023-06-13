---
cssclass: [monsters]
title1: Troglodyte, Troglodyte Beast-Speaker
title2: Troglodyte Beast-Speaker
CR: 3
sources:
- name: Monster Codex
  page: 215
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Troglodyte
classes:
- druid 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 4
senses:
  darkvision: 90
auras:
- name: stench
  radius: 30
  DC: 13
  duration: 10 rounds
AC:
  AC: 16
  touch: 10
  flat_footed: 16
  components:
    natural: 6
HP:
  HP: 35
  long: 5d8+13
saves:
  fort: 8
  ref: 3
  will: 5
speeds:
  base: 30
  climb: 20
attacks:
  melee:
  - - text: mwk club +4 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk club
      bonus:
      - 4
    - text: bite -2 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - -2
    - text: claw -2 (1d4)
      entries:
      - - damage: 1d4
      attack: claw
      bonus:
      - -2
  - - text: bite +3 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - 3
    - text: 2 claws +3 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 3
  ranged:
  - - text: javelin +3 (1d6)
      entries:
      - - damage: 1d6
      attack: javelin
      bonus:
      - 3
spells:
  entries:
  - is_domain_spell: true
    name: hold animal
    source: Druid
    level: 2
    DC: 14
  - name: spider climb
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - is_domain_spell: true
    name: calm animals
    source: Druid
    level: 1
    DC: 13
  - name: charm animal
    source: Druid
    level: 1
    DC: 13
  - name: cure light wounds
    source: Druid
    level: 1
  - name: entangle
    source: Druid
    level: 1
    DC: 13
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 3
    concentration: 5
    slots:
      0: at-will
tactics:
  Before Combat: The beast-speaker casts spider climb on himself and tries to ambush
    his prey from the ceiling, high wall, or ledge.
  Base Statistics: Without spider climb, the beast-speaker's statistics are Speed
    30 ft.; Skills Climb +0.
ability_scores:
  STR: 10
  DEX: 11
  CON: 14
  INT: 10
  WIS: 15
  CHA: 15
BAB: 3
CMB: 3
CMD: 13
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Climb: 8
  Heal: 7
  Knowledge (nature): 2
  Perception: 10
  Spellcraft: 6
  Stealth: 7
    in rocky areas: 11
  Survival: 10
languages:
- Draconic
- Druidic
special_qualities:
- nature bond (Animal domain)
- nature sense
- speak with animals (6 rounds/day)
- trackless step
- wild empathy +5
- woodland stride
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of dominate animal
  - scroll of summon nature's ally II
  other:
  - javelins (6)
  - mwk club
  - headdress (worth 500 gp)
  - 19 gp
ecology:
  environment: any underground
desc_long: Troglodyte divine spellcasters act as spiritual advisors for their tribes.
  Troglodyte clerics usually worship demon lords, particularly those associated with
  caverns and reptiles.

---

# Troglodyte, Troglodyte Beast-Speaker

**Source** Monster Codex pg. 215
**XP** 800
_[[monsters/Troglodyte|Troglodyte]]_ _[[classes/Druid|druid]]_ 3
CE Medium humanoid (reptilian)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft.; Perception +10
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 13, 10 rounds)

##### Defense

**AC** 16, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 natural)
**hp** 35 (5d8+13)
**Fort** +8, **Ref** +3, **Will** +5

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +4 (1d6), bite –2 (1d4), claw –2 (1d4) or bite +3 (1d4), 2 claws +3 (1d4)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +3 (1d6)
**_Druid_ Spells Prepared **(CL 3rd; concentration +5)
2nd—_[[spells/Hold Animal|hold animal]]_ (DC 14), _[[spells/Spider Climb|spider climb]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Calm Animals|calm animals]]_ (DC 13), _[[spells/Charm Animal|charm animal]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Entangle|entangle]]_ (DC 13)
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Know Direction|know direction]]_

### Tactics

**Before Combat** The beast-speaker casts _spider climb_ on himself and tries to ambush his prey from the ceiling, high wall, or ledge.
 **Base Statistics** Without _spider climb_, the beast-speaker’s statistics are **Speed **30 ft.; **Skills **_Climb_ +0.

##### Statistics
**Str** 10, **Dex** 11, **Con** 14, **Int** 10, **Wis** 15, **Cha** 15
**Base Atk** +3; **CMB** +3; **CMD** 13
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** _Climb_ +8, _[[spells/Heal|Heal]]_ +7, Knowledge (nature) +2, Perception +10, Spellcraft +6, Stealth +7 (+11 in rocky areas), Survival +10
**Languages** Draconic, Druidic
**SQ** nature bond (Animal domain), nature sense, _[[spells/Speak with Animals|speak with animals]]_ (6 rounds/day), _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +5, woodland stride
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _[[spells/Dominate Animal|dominate animal]]_, scroll of _[[universal monster rules/Summon|summon]]_ nature’s ally II; **Other Gear** javelins (6), mwk _club_, headdress (worth 500 gp), 19 gp

##### Ecology

**Environment** any underground

##### Description

_Troglodyte_ divine spellcasters act as spiritual advisors for their tribes. _Troglodyte_ clerics usually worship demon lords, particularly those associated with caverns and reptiles.