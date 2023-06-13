---
cssclass: [monsters]
title1: Blight, Swamp Blight
desc_short: A cloud of mosquitoes churns around this quivering blob, its body studded
  with red eyes and its five tentacles tipped with stingers.
title2: Swamp Blight
CR: 17
sources:
- name: Bestiary 6
  page: 44
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 102400
alignment: LE
size: Medium
type: ooze
subtypes:
- aquatic
- blight
initiative:
  bonus: 14
senses:
  blindsight: 120
auras:
- name: mosquitoes
  radius: 10
  DC: 26
AC:
  AC: 32
  touch: 20
  flat_footed: 22
  components:
    dex: 10
    natural: 12
HP:
  HP: 275
  long: 19d8+190
  fast_healing: 15
saves:
  fort: 18
  ref: 18
  will: 14
defensive_abilities:
- rejuvenation
immunities:
- acid
- ooze traits
speeds:
  base: 30
  swim: 40
attacks:
  melee:
  - - text: 5 stings +26 (1d8+12/19-20 plus toxic acid)
      entries:
      - - damage: 1d8+12
          crit_range: 19-20
        - effect: toxic acid
      count: 5
      attack: stings
      bonus:
      - 26
  special:
  - unquiet bog
space: 5
reach: 15
spell_like_abilities:
  entries:
  - name: blight
    source: default
    freq: 1/day
    DC: 22
  - name: command plants
    source: default
    freq: 1/day
    DC: 21
  - name: dominate monster
    source: default
    freq: 1/day
    other: animals and magical beasts only
    DC: 26
  - name: greater curse terrain
    source: default
    freq: 1/day
  - name: hallucinatory terrain
    source: default
    freq: 1/day
    DC: 21
  - name: insect plague
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 24
ability_scores:
  STR: 34
  DEX: 30
  CON: 31
  INT: 17
  WIS: 23
  CHA: 24
BAB: 14
CMB: 26
CMB_other: +30 trip
CMD: 46
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Great Fortitude
- name: Greater Trip
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Improved Trip
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
skills:
  Intimidate: 26
  Knowledge (geography): 22
  Perception: 25
  Stealth: 29
    in swamps: 37
  Swim: 42
  _racial_mods:
    Stealth:
      in swamps: 8
languages:
- Aklo
- Aquan
- domain telepathy
special_qualities:
- amphibious
- cursed domain
- favored terrain (swamp)
ecology:
  environment: any swamps
  organization: solitary
  treasure_type: standard
special_abilities:
  Mosquitoes Aura (Su): An infestation of mosquitoes with a radius of 10 feet constantly
    surrounds a swamp blight. Any creature within this area takes 2d6 points of damage
    at the end of each round it remains in the area. A creature that takes this damage
    also takes 1d6 points of bleed damage and must succeed at a DC 27 Fortitude save
    or be nauseated for 1 round. Any area effect attack that deals 20 or more points
    of damage to a swamp blight destroys the mosquitoes, removing the mosquito aura
    for 1 minute, after which a new batch of mosquitoes swarms out of the ooze's body
    to replenish the infestation. The save DC is Constitution-based.
  Toxic Acid (Ex): Sting-injury; save Fort DC 29; frequency 1/round for 6 rounds;
    effect 2d6 acid plus 1 Str drain plus staggered for 1 round; cure 2 saves.
  Unquiet Bog (Su): All humanoid creatures that die within a swamp blight's cursed
    domain rise from death as mummies. Creatures with 7 or fewer Hit Dice rise as
    swamp mummies (Pathfinder RPG Bestiary 5 178), while creatures with 8 or more
    Hit Dice rise as mummy lords (Bestiary 5 176). A swamp blight can control a number
    of Hit Dice of mummies equal to double its own Hit Dice (up to 38 Hit Dice of
    mummies for most swamp blights); additional mummies created beyond this limit
    are free-willed but still regard the swamp blight as an ally.
desc_long: |-
  Swamp blights rule over large swaths of boggy land, populating their realms with the mummified forms of those they have slaughtered or who have fallen prey to their domains' denizens. These mummies are the swamp blights' preferred weapon against nearby settlements, and the mummies typically seek to drag the unconscious bodies of their victims back to be killed within their masters' cursed swamplands so the bodies rise as new mummies to bolster the sodden, undead army. Yet even these undead eventually fall prey to the blights' unwillingness to share their realms. 

  A swamp blight is 7 feet across and weighs 540 pounds.

---

# Blight, Swamp Blight
A cloud of mosquitoes churns around this quivering blob, its body studded with red eyes and its five tentacles tipped with stingers.
**Source** Bestiary 6 pg. 44
**XP** 102,400

LE Medium ooze (aquatic, _[[spells/Blight|blight]]_)
**Init** +14; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft.; Perception +25
**Aura** mosquitoes (10 ft., DC 26)

##### Defense

**AC** 32, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+10 Dex, +12 natural)
**hp** 275 (19d8+190); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +18, **Ref** +18, **Will** +14
**Defensive Abilities** rejuvenation; **Immune** acid, ooze traits

##### Offense
**Speed** 30 ft., swim 40 ft.
**Melee** 5 stings +26 (1d8+12/19–20 plus _[[items/Weapon Magic Abilities/Toxic|toxic]]_ acid)
**Space** 5 ft., **Reach** 15 ft.
**Special Attacks** unquiet bog
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +24)
1/day—_blight_ (DC 22), _[[spells/Command Plants|command plants]]_ (DC 21), _[[spells/Dominate Monster|dominate monster]]_ (animals and magical beasts only, DC 26), greater _[[spells/Curse Terrain|curse terrain]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 21), _[[spells/Insect Plague|insect plague]]_

##### Statistics
**Str** 34, **Dex** 30, **Con** 31, **Int** 17, **Wis** 23, **Cha** 24
**Base Atk** +14; **CMB** +26 (+30 _[[universal monster rules/Trip|trip]]_); **CMD** 46 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Intimidate +26, Knowledge (geography) +22, Perception +25, Stealth +29 (+37 in swamps), Swim +42; **Racial Modifiers** +8 Stealth in swamps
**Languages** Aklo, Aquan; domain _[[universal monster rules/Telepathy|telepathy]]_
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, cursed domain, favored terrain (swamp)

##### Ecology

**Environment** any swamps
**Organization** solitary
**Treasure** standard

### Special Abilities

**Mosquitoes Aura (Su)** An infestation of mosquitoes with a radius of 10 feet constantly surrounds a swamp _blight_. Any creature within this area takes 2d6 points of damage at the end of each round it remains in the area. A creature that takes this damage also takes 1d6 points of _[[universal monster rules/Bleed|bleed]]_ damage and must succeed at a DC 27 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1 round. Any area effect attack that deals 20 or more points of damage to a swamp _blight_ destroys the mosquitoes, removing the mosquito aura for 1 minute, after which a new batch of mosquitoes swarms out of the ooze’s body to replenish the infestation. The save DC is Constitution-based.

**_Toxic_ Acid (Ex)** Sting—injury; save Fort DC 29; frequency 1/round for 6 rounds; effect 2d6 acid plus 1 Str drain plus _[[conditions/Staggered|staggered]]_ for 1 round; cure 2 saves.

**Unquiet Bog (Su)** All humanoid creatures that die within a swamp _blight_’s cursed domain rise from death as mummies. Creatures with 7 or fewer Hit Dice rise as swamp mummies (Pathfinder RPG Bestiary 5 178), while creatures with 8 or more Hit Dice rise as _[[monsters/Mummy|mummy]]_ lords (Bestiary 5 176). A swamp _blight_ can control a number of Hit Dice of mummies equal to double its own Hit Dice (up to 38 Hit Dice of mummies for most swamp blights); additional mummies created beyond this limit are free-willed but still regard the swamp _blight_ as an ally.

##### Description

Swamp blights rule over large swaths of boggy land, populating their realms with the mummified forms of those they have slaughtered or who have _[[monsters/Fallen|fallen]]_ prey to their domains’ denizens. These mummies are the swamp blights’ preferred weapon against nearby settlements, and the mummies typically seek to drag the _[[conditions/Unconscious|unconscious]]_ bodies of their victims back to be killed within their masters’ cursed swamplands so the bodies rise as new mummies to bolster the sodden, undead army. Yet even these undead eventually fall prey to the blights’ unwillingness to share their realms.

A swamp _blight_ is 7 feet across and weighs 540 pounds.