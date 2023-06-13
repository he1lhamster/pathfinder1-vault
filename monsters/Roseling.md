---
cssclass: [monsters]
title1: Roseling
desc_short: This small plant is shaped vaguely like a human with a rose blossom for
  a head and soft, petallike wings fluttering from its shoulders.
title2: Roseling
CR: 7
sources:
- name: Planar Adventures
  page: 243
  link: http://paizo.com/products/btpya1am
XP: 3200
alignment: NG
size: Small
type: plant
subtypes:
- extraplanar
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 16
  flat_footed: 15
  components:
    dex: 5
    natural: 4
    size: 1
HP:
  HP: 85
  long: 10d8+40
saves:
  fort: 11
  ref: 8
  will: 7
immunities:
- electricity
- petrification
- plant traits
resistances:
  cold: 10
  sonic: 10
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +9 (1d3+1)
      entries:
      - - damage: 1d3+1
      count: 2
      attack: claws
      bonus:
      - 9
  ranged:
  - - text: 4 thorns +13 (1d4+5 plus euphoria)
      entries:
      - - damage: 1d4+5
        - effect: euphoria
      count: 4
      attack: thorns
      bonus:
      - 13
  special:
  - euphoria
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: speak with plants
    source: default
    freq: Constant
  - name: remove fear
    source: default
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 12
ability_scores:
  STR: 13
  DEX: 20
  CON: 18
  INT: 20
  WIS: 19
  CHA: 21
BAB: 7
CMB: 7
CMD: 22
feats:
- name: Combat Expertise
- name: Deadly Aim
- name: Improved Initiative
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Acrobatics: 15
  Craft (any one): 15
  Craft (typically alchemy): 15
  Fly: 24
  Knowledge (nature): 10
  Knowledge (planes): 10
  Perception: 17
  Stealth: 22
  Survival: 14
languages:
- Celestial
- Common
- Sylvan
- speak with plants
special_qualities:
- change shape (Small rose bush; tree shape)
ecology:
  environment: any (Nirvana)
  organization: solitary, pair, or bed (3-8)
  treasure_type: standard
special_abilities:
  Euphoria (Su): A creature damaged by a roseling's thorns must succeed at a DC 19
    Will save or become filled with joy for 1 hour, during which time the creature
    finds it difficult to take hostile actions. The creature takes a -2 penalty on
    attack and damage rolls, cannot take attacks of opportunity, cannot ready an attack
    or any other action that would deal damage, and takes a -2 penalty on saving throws
    against other emotion effects. This is a mind-affecting emotion and poison effect.
    The save DC is Constitution-based.
  Thorns (Su): A roseling can launch a thorn as a standard action, or up to four thorns
    as a full-round action. A thorn has a range increment of 20 feet (to a maximum
    of 10 range increments) and deals piercing damage. A roseling applies its Dexterity
    modifier (+5 for the typical roseling) on the damage dealt by a thrown thorn instead
    of its Strength modifier. A creature damaged by a thorn is exposed to the roseling's
    euphoria. The save DC is Constitution-based.
desc_long: 'Roselings are often found in Shelyn's divine realm. A roseling's petal
  color reflects its personality: pink roselings are gentle, red roselings are passionate,
  white roselings are shy, yellow roselings are gregarious, and the rare blue roselings
  are transcendent and often more powerful than their kin, having class levels or
  the advanced creature template.'

---

# Roseling
This small plant is shaped vaguely like a human with a rose blossom for a head and soft, petallike wings fluttering from its shoulders.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 243
**XP** 3,200

NG Small plant (extraplanar, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 20, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 Dex, +4 natural, +1 size)
**hp** 85 (10d8+40)
**Fort** +11, **Ref** +8, **Will** +7
**Immune** electricity, petrification, _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 10, sonic 10

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** 2 claws +9 (1d3+1)
**Ranged** 4 thorns +13 (1d4+5 plus euphoria)
**Special Attacks** euphoria
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
Constant—_[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Plants|speak with plants]]_
At will—_[[spells/Remove Fear|remove fear]]_

##### Statistics
**Str** 13, **Dex** 20, **Con** 18, **Int** 20, **Wis** 19, **Cha** 21
**Base Atk** +7; **CMB** +7; **CMD** 22
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Acrobatics +15, Craft (any one, typically alchemy) +15, Fly +24, Knowledge (nature) +10, Knowledge (planes) +10, Perception +17, Stealth +22, Survival +14
**Languages** Celestial, Common, Sylvan; _speak with plants_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small rose bush; _[[spells/Tree Shape|tree shape]]_)

##### Ecology

**Environment** any (Nirvana)
**Organization** solitary, pair, or bed (3–8)
**Treasure** standard

### Special Abilities

**Euphoria (Su)** A creature damaged by a _[[monsters/Roseling|roseling]]_’s thorns must succeed at a DC 19 Will save or become filled with joy for 1 hour, during which time the creature finds it difficult to take hostile actions. The creature takes a –2 penalty on attack and damage rolls, cannot take attacks of opportunity, cannot ready an attack or any other action that would deal damage, and takes a –2 penalty on saving throws against other emotion effects. This is a mind-affecting emotion and poison effect. The save DC is Constitution-based.

**Thorns (Su)** A _roseling_ can launch a thorn as a standard action, or up to four thorns as a full-round action. A thorn has a range increment of 20 feet (to a maximum of 10 range increments) and deals piercing damage. A _roseling_ applies its Dexterity modifier (+5 for the typical _roseling_) on the damage dealt by a thrown thorn instead of its Strength modifier. A creature damaged by a thorn is exposed to the _roseling_’s euphoria. The save DC is Constitution-based.

##### Description

Roselings are often found in Shelyn’s divine realm. A _roseling_’s petal color reflects its personality: pink roselings are gentle, red roselings are passionate, white roselings are shy, yellow roselings are gregarious, and the rare blue roselings are transcendent and often more powerful than their kin, having class levels or the advanced creature template.