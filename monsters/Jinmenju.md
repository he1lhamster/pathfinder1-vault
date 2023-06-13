---
cssclass: [monsters]
title1: Jinmenju
desc_short: A low hum surrounds this huge, gnarled tree. The rotten fruits that hang
  from its sickly branches look vaguely like human heads.
title2: Jinmenju
CR: 11
sources:
- name: Bestiary 4
  page: 161
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #54: The Empty Throne'
  page: 86
  link: http://paizo.com/pathfinder/v5748btpy8mh1
XP: 12800
alignment: N
size: Huge
type: plant
initiative:
  bonus: 3
senses:
  all-around vision: true
  blindsense: 60
  low-light vision: true
auras:
- name: unsettling drone
  radius: 30
  DC: 18
AC:
  AC: 25
  touch: 7
  flat_footed: 25
  components:
    dex: -1
    natural: 18
    size: -2
HP:
  HP: 149
  long: 13d8+91
saves:
  fort: 14
  ref: 5
  will: 5
immunities:
- plant traits
- poison
speeds:
  base: 10
attacks:
  melee:
  - - text: bite +15 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      attack: bite
      bonus:
      - 15
    - text: 2 slams +16 (1d8+8)
      entries:
      - - damage: 1d8+8
      count: 2
      attack: slams
      bonus:
      - 16
  special:
  - enticing head-fruits
  - intoxicating stench
space: 15
reach: 15
spell_like_abilities:
  entries:
  - superscripts:
    - UM
    name: share memory
    source: default
    freq: At will
    paren_text: with a range of 55 feet, targeting the jinmenju and 1 creature in
      range, DC 14
  - name: sculpt sound
    source: default
    freq: 3/day
    DC: 15
  - name: shout
    source: default
    freq: 3/day
    DC: 16
  sources:
  - name: default
    CL: 13
    concentration: 15
ability_scores:
  STR: 27
  DEX: 8
  CON: 22
  INT: 7
  WIS: 12
  CHA: 15
BAB: 9
CMB: 19
CMD: 28
feats:
- name: Combat Reflexes
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Lunge
- name: Toughness
- name: Weapon Focus (slam)
skills:
  Perception: 17
languages:
- Common
ecology:
  environment: temperate hills or mountains
  organization: solitary
  treasure_type: incidental
special_abilities:
  Enticing Head-Fruits (Su): |-
    Any creature that begins its turn within 5 feet of a jinmenju must succeed at a DC 22 Will save or be magically compelled to immediately grab a headfruit and eat it. This is a mind-affecting compulsion effect. A creature that successfully saves is immune to that jinmenju's enticing head-fruits for 24 hours. The save DC is Constitutionbased. Anyone who takes a bite out of one suffers from the following effect.

    Head-Fruit Poison: Head-fruit-ingested; save Fort DC 22; frequency 1/round for 6 rounds; effect 1d3 Wisdom damage and confused for 1 round; cure 2 consecutive saves. The save DC is Constitution-based.
  Intoxicating Stench (Su): Once per day as a swift action, a jinmenju can cause its
    fruits to emit an unnaturally sweet aroma in a 60-foot spread for 6 rounds. All
    creatures within the area must succeed at a DC 22 Will save each round or be captivated.
    A captivated creature takes no actions except to approach the jinmenju via the
    most direct route possible. If this path leads it into a dangerous area or the
    jinmenju attacks it, the captivated creature receives a new saving throw. This
    is a mind-affecting effect. The save DC is Constitution-based.
  Unsettling Drone (Su): A jinmenju emits a low, persistent hum that unnerves living
    creatures that hear it. Those within 30 feet of it must succeed at a DC 18 Will
    save or become shaken until they leave the affected area and for 1d4 rounds thereafter.
    A creature that successfully saves is immune to that jinmenju's unsettling drone
    for 24 hours. The save DC is Charisma-based.
desc_long: Jinmenjus are trees that grow in hilly regions far from civilized lands,
  and prey on those who come too close. They are remarkably intelligent and crafty,
  and use both scent and magical compulsion to lure prey.

---

# Jinmenju
A low hum surrounds this huge, gnarled tree. The rotten fruits that hang from its sickly branches look vaguely like human heads.
**Source** Bestiary 4 pg. 161, Pathfinder #54: The Empty Throne pg. 86
**XP** 12,800

N Huge plant
**Init** +3; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17
**Aura** unsettling drone (30 ft., DC 18)

##### Defense

**AC** 25, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 25 (–1 Dex, +18 natural, –2 size)
**hp** 149 (13d8+91)
**Fort** +14, **Ref** +5, **Will** +5
**Immune** _[[universal monster rules/Plant Traits|plant traits]]_, poison

##### Offense
**Speed** 10 ft.
**Melee** bite +15 (2d6+8/19–20), 2 slams +16 (1d8+8)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** enticing head-fruits, intoxicating _[[universal monster rules/Stench|stench]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +15)
At will—_[[spells/Share Memory|share memory]]_ (with a range of 55 feet, targeting the _[[monsters/Jinmenju|jinmenju]]_ and 1 creature in range, DC 14)
3/day—_[[spells/Sculpt Sound|sculpt sound]]_ (DC 15), _[[spells/Shout|shout]]_ (DC 16)

##### Statistics
**Str** 27, **Dex** 8, **Con** 22, **Int** 7, **Wis** 12, **Cha** 15
**Base Atk** +9; **CMB** +19; **CMD** 28
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Perception +17
**Languages** Common

##### Ecology

**Environment** temperate hills or mountains
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Enticing Head-Fruits (Su)** Any creature that begins its turn within 5 feet of a _jinmenju_ must succeed at a DC 22 Will save or be magically compelled to immediately _[[universal monster rules/Grab|grab]]_ a headfruit and eat it. This is a mind-affecting compulsion effect. A creature that successfully saves is immune to that _jinmenju_’s enticing head-fruits for 24 hours. The save DC is Constitutionbased. Anyone who takes a bite out of one suffers from the following effect.

Head-Fruit Poison: Head-fruit—ingested; save Fort DC 22; frequency 1/round for 6 rounds; effect 1d3 Wisdom damage and _[[conditions/Confused|confused]]_ for 1 round; cure 2 consecutive saves. The save DC is Constitution-based.

**Intoxicating _Stench_ (Su)** Once per day as a swift action, a _jinmenju_ can cause its fruits to emit an unnaturally sweet aroma in a 60-foot spread for 6 rounds. All creatures within the area must succeed at a DC 22 Will save each round or be captivated. A captivated creature takes no actions except to approach the _jinmenju_ via the most direct route possible. If this path leads it into a dangerous area or the _jinmenju_ attacks it, the captivated creature receives a new saving throw. This is a mind-affecting effect. The save DC is Constitution-based.

**Unsettling Drone (Su)** A _jinmenju_ emits a low, persistent hum that unnerves living creatures that hear it. Those within 30 feet of it must succeed at a DC 18 Will save or become _[[conditions/Shaken|shaken]]_ until they leave the affected area and for 1d4 rounds thereafter. A creature that successfully saves is immune to that _jinmenju_’s unsettling drone for 24 hours. The save DC is Charisma-based.

##### Description

Jinmenjus are trees that grow in hilly regions far from civilized lands, and prey on those who come too close. They are remarkably intelligent and crafty, and use both _[[universal monster rules/Scent|scent]]_ and magical compulsion to lure prey.