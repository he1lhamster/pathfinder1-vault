---
cssclass: [monsters]
title1: Kobold, Kobold Scalecaster
title2: Kobold Scalecaster
CR: 1/2
sources:
- name: Monster Codex
  page: 131
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 200
race: Kobold
classes:
- sorcerer 1
alignment: LN
size: Small
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 14
  flat_footed: 12
  components:
    dex: 3
    natural: 1
    size: 1
HP:
  HP: 7
  long: 1d6+1
saves:
  fort: 0
  ref: 3
  will: 3
weaknesses:
- light sensitivity
speeds:
  base: 60
attacks:
  melee:
  - - text: 2 claws -2 (1d3-3)
      entries:
      - - damage: 1d3-3
      count: 2
      attack: claws
      bonus:
      - -2
  ranged:
  - - text: light crossbow +4 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
  special:
  - claws (1d3-3, 5 rounds/day)
spells:
  entries:
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 13
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 13
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 12
  - name: ray of frost
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 1
    concentration: 3
    slots:
      1: 4
      0: at-will
    bloodline: draconic (gold)
ability_scores:
  STR: 4
  DEX: 16
  CON: 10
  INT: 10
  WIS: 13
  CHA: 15
BAB: 0
CMB: -4
CMD: 9
feats:
- name: Eschew Materials
- name: Improved Initiative
skills:
  Craft (trapmaking): 2
  Perception: 3
  Profession (miner): 3
  Stealth: 11
  Use Magic Device: 6
languages:
- Draconic
special_qualities:
- bloodline arcana (fire spells deal +1 damage per die)
- crafty
gear:
  combat:
  - scroll of mage armor
  - scroll of vanish
  - caltrops
  - silversheen
  other:
  - light crossbow
  - 54 gp
ecology:
  environment: temperate underground or deep forest
desc_long: Kobolds see sorcery as proof of their draconic heritage.

---

# Kobold, Kobold Scalecaster

**Source** Monster Codex pg. 131
**XP** 200
_[[monsters/Kobold|Kobold]]_ _[[classes/Sorcerer|sorcerer]]_ 1

LN Small humanoid (reptilian)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +3

##### Defense

**AC** 15, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +1 natural, +1 size)
**hp** 7 (1d6+1)
**Fort** +0, **Ref** +3, **Will** +3
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 60 ft.
**Melee** 2 claws –2 (1d3–3)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d6/19–20)
**Special Attacks** claws (1d3–3, 5 rounds/day)
**_Sorcerer_ Spells Known **(CL 1st; concentration +3)
1st (4/day)—_[[spells/Burning Hands|burning hands]]_ (DC 13), _[[spells/Charm Person|charm person]]_ (DC 13)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 12), _[[spells/Ray of Frost|ray of frost]]_
**Bloodline** draconic (gold)

##### Statistics
**Str** 4, **Dex** 16, **Con** 10, **Int** 10, **Wis** 13, **Cha** 15
**Base Atk** +0; **CMB** –4; **CMD** 9
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Craft (trapmaking) +2, Perception +3, Profession (_[[npcs/Miner|miner]]_) +3, Stealth +11, Use Magic Device +6
**Languages** Draconic
**SQ** bloodline arcana (fire spells deal +1 damage per die), crafty
**Combat Gear** scroll of _[[spells/Mage Armor|mage armor]]_, scroll of _[[spells/Vanish|vanish]]_, _[[items/Mundane/Caltrops|caltrops]]_, _[[items/Wondrous Item/Silversheen|silversheen]]_; **Other Gear** _light crossbow_, 54 gp

##### Ecology

**Environment** temperate underground or deep forest

##### Description

Kobolds see sorcery as proof of their _[[feats/Draconic Heritage|draconic heritage]]_.