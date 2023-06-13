---
cssclass: [monsters]
title1: Troll, Troll Fury
title2: Troll Fury
CR: 8
sources:
- name: Monster Codex
  page: 229
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Troll
classes:
- druid (troll fury) 6 (see page 224)
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 21
  touch: 11
  flat_footed: 19
  components:
    armor: 5
    dex: 2
    natural: 5
    size: -1
HP:
  HP: 156
  long: 12d8+102
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 19
  ref: 7
  will: 13
resistances:
  fire: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +13 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - chosen prey (humans +2)
  - fire bolt (1d6+3 fire, 6/day)
  - rend (2 claws, 1d6+7)
  - wild shape 2/day
space: 10
reach: 10
spells:
  entries:
  - name: call lightning
    source: Druid
    level: 3
    DC: 18
  - name: fireball
    source: Druid
    level: 3
    DC: 18
  - name: poison
    source: Druid
    level: 3
    count: 2
    DC: 16
  - name: barkskin
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - name: flaming sphere
    source: Druid
    level: 2
    DC: 17
  - name: hold animal
    source: Druid
    level: 2
    DC: 15
  - is_domain_spell: true
    name: produce flame
    source: Druid
    level: 2
  - is_domain_spell: true
    name: burning hands
    source: Druid
    level: 1
    DC: 16
  - name: entangle
    source: Druid
    level: 1
    DC: 14
  - name: magic fang
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: pass without trace
    source: Druid
    level: 1
  - name: detect magic
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  - name: resistance
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
tactics:
  During Combat: The fury attacks her foes with fire and electricity spells, typically
    starting with fireball. She avoids melee combat until her offensive spells are
    exhausted. She then casts bull's strength on herself and starts attacking.
ability_scores:
  STR: 23
  DEX: 14
  CON: 27
  INT: 8
  WIS: 16
  CHA: 4
BAB: 8
CMB: 15
CMD: 27
feats:
- name: Combat Casting
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Iron Will
- name: Skill Focus (Perception)
- name: Spell Focus (evocation)
skills:
  Intimidate: 5
  Knowledge (nature): 6
  Perception: 24
  Survival: 10
languages:
- Druidic
- Giant
special_qualities:
- inspire fervor +2
- nature bond (Fire domain)
- nature sense
- trackless step
- woodland stride
gear:
  combat:
  - pearl of power (1st)
  - scroll of fog cloud
  - scroll of protection from energy (fire)
  other:
  - +1 hide armor
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - 110 gp
ecology:
  environment: cold mountains
desc_long: |-
  A troll fury's first duty is to see to the welfare of her tribe, and to ensure its prosperity in the long term. Watching the lands around her carefully, monitoring the migration of game, and minding the lessons of her predecessors all let a troll fury anticipate times of plenty and times of need, and to stockpile or conserve as necessary. Though a troll fury never rushes into a decision that could endanger the tribe, she commands her own tribe or newcomers to their territory to move on if there's a risk that the hunting grounds will be overhunted. Wise tribes leave the area when she tells them to, but sometimes she must drive them away with fire and poison so the animals have time to repopulate.

  To a troll fury's mind, it's wiser to risk traveling to another land in the short term so exhausted lands can recover. This attitude, combined with her knowledge of natural environments, means she's the member of the tribe most likely to lead a migration. In larger tribes, a triumvirate or larger group of furies works together. Each concentrates on a particular area of expertise, but they all back one another up once one of them makes a decision that affects the tribe. This solidarity lets them cow even the most autocratic tribal leaders.

---

# Troll, Troll Fury

**Source** Monster Codex pg. 229
**XP** 4,800
_[[monsters/Troll|Troll]]_ _[[classes/Druid|druid]]_ (_troll_ fury) 6 (see page 224)
CE Large humanoid (giant)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +24

##### Defense

**AC** 21, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 armor, +2 Dex, +5 natural, –1 size)
**hp** 156 (12d8+102); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +19, **Ref** +7, **Will** +13
**Resist** fire 10

##### Offense
**Speed** 20 ft.
**Melee** bite +13 (1d8+6), 2 claws +13 (1d6+6)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** chosen prey (humans +2), fire bolt (1d6+3 fire, 6/day), _[[universal monster rules/Rend|rend]]_ (2 claws, 1d6+7), wild shape 2/day
**_Druid_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 18), _[[spells/Fireball|fireball]]_ (DC 18), poison (2, DC 16)
2nd—_[[spells/Barkskin|barkskin]]_, bull’s strength, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 17), _[[spells/Hold Animal|hold animal]]_ (DC 15), _[[spells/Produce Flame|produce flame]]_
1st—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Entangle|entangle]]_ (DC 14), _[[spells/Magic Fang|magic fang]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Pass without Trace|pass without trace]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

### Tactics

**During Combat** The fury attacks her foes with fire and electricity spells, typically starting with _fireball_. She avoids melee combat until her offensive spells are _[[conditions/Exhausted|exhausted]]_. She then casts bull’s strength on herself and starts attacking.

##### Statistics
**Str** 23, **Dex** 14, **Con** 27, **Int** 8, **Wis** 16, **Cha** 4
**Base Atk** +8; **CMB** +15; **CMD** 27
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Intimidate +5, Knowledge (nature) +6, Perception +24, Survival +10
**Languages** Druidic, Giant
**SQ** inspire fervor +2, nature bond (Fire domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, woodland stride
**Combat Gear** pearl of power (1st), scroll of _[[spells/Fog Cloud|fog cloud]]_, scroll of _[[spells/Protection from Energy|protection from energy]]_ (fire); **Other Gear** +1 _[[items/Armor/Hide armor|hide armor]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, 110 gp

##### Ecology

**Environment** cold mountains

##### Description

A _troll_ fury’s first duty is to see to the welfare of her tribe, and to ensure its prosperity in the long term. Watching the lands around her carefully, monitoring the migration of game, and minding the lessons of her predecessors all let a _troll_ fury anticipate times of plenty and times of need, and to stockpile or conserve as necessary. Though a _troll_ fury never rushes into a decision that could endanger the tribe, she commands her own tribe or newcomers to their territory to move on if there’s a risk that the hunting grounds will be overhunted. Wise tribes leave the area when she tells them to, but sometimes she must drive them away with fire and poison so the animals have time to repopulate.

To a _troll_ fury’s mind, it’s wiser to risk traveling to another land in the short term so _exhausted_ lands can recover. This attitude, combined with her knowledge of natural environments, means she’s the member of the tribe most likely to lead a migration. In larger tribes, a triumvirate or larger group of furies works together. Each concentrates on a particular area of expertise, but they all back one another up once one of them makes a decision that affects the tribe. This solidarity lets them cow even the most autocratic tribal leaders.