---
cssclass: [monsters]
title1: Commando Construct
desc_short: Moving with the fluid grace of a predatory animal, this large robot's
  sports an array of dangerous weaponry.
title2: Commando Construct
CR: 9
sources:
- name: Construct Handbook
  page: 36
  link: https://paizo.com/products/btq01vam
XP: 6400
alignment: N
size: Large
type: construct
subtypes:
- augmented
- robot
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 28
  touch: 14
  flat_footed: 23
  components:
    dex: 5
    natural: 14
    size: -1
HP:
  HP: 110
  long: 10d12+45
saves:
  fort: 5
  ref: 8
  will: 3
defensive_abilities:
- hardness 10
immunities:
- construct traits
resistances:
  acid: 5
  cold: 5
  fire: 15
weaknesses:
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  base: 30
  burrow: 20
  climb: 30
  fly: 10
  fly_maneuverability: clumsy
  swim: 20
attacks:
  melee:
  - - text: integrated drill +17 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: integrated drill
      bonus:
      - 17
    - text: integrated laser torch +16 touch (1d6 fire)
      entries:
      - - damage: 1d6
          type: fire
      attack: integrated laser torch
      bonus:
      - 16
      touch: true
    - text: slam +16 (1d6+7 plus grab)
      entries:
      - - damage: 1d6+7
        - effect: grab
      attack: slam
      bonus:
      - 16
  special:
  - breath weapon (30-ft. cone, 3d6 acid plus poison, Reflex DC 15 half, usable every
    1d4 rounds)
  - energized alacrity
  - energy attacks (acid)
  - knockout strike
space: 10
reach: 10
ability_scores:
  STR: 24
  DEX: 20
  CON:
  INT: 15
  WIS: 11
  CHA: 5
BAB: 10
CMB: 18
CMB_other: +22 grapple
CMD: 33
feats:
- name: Acrobatic Steps
- is_bonus: true
  name: Dodge
- name: Great Fortitude
- name: Improved Great Fortitude
- is_bonus: true
  name: Mobility
- name: Nimble Moves
- is_bonus: true
  name: Power Attack
- name: Weapon Focus (drill)
skills:
  Acrobatics: 8
  Climb: 15
  Fly: 5
  Knowledge (engineering): 19
  Knowledge (nature): 19
  Perception: 13
  Swim: 15
  _racial_mods:
    Knowledge (engineering):
      _: 4
    Knowledge (nature):
      _: 4
languages:
- Common
special_qualities:
- reprogram terrain
- tactical awareness
- technological wonders
- terraform
ecology:
  environment: any
  organization: solitary,  pair, or team (3-10)
  treasure_type: none
desc_long: |-
  Commando constructs are elite fighting machines that often operate alone or in small squads. Although they are skilled combatants, these constructs can handle a variety of clandestine activities, including assassination, infiltration, kidnapping, and sabotage. They are most often found wandering the plains of Numeria, or under the service of a local warlord.

   The sample commando construct presented here is built using a terraformer robot  as the base creature. See that entry for full descriptions of its base abilities.

---

# Commando Construct
Moving with the fluid _[[spells/Grace|grace]]_ of a predatory animal, this large robot’s sports an array of dangerous weaponry.
**Source** Construct Handbook pg. 36
**XP** 6,400

N Large construct (augmented, robot)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+5 Dex, +14 natural, -1 size)
**hp** 110 (10d12+45)
**Fort** +5, **Ref** +8, **Will** +3
**Defensive Abilities** hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** acid 5, cold 5, fire 15
**Weaknesses** vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 10 ft. (clumsy), swim 20 ft.
**Melee** integrated _[[items/Mundane/Drill|drill]]_ +17 (1d6+7), integrated laser _[[items/Mundane/Torch|torch]]_ +16 touch (1d6 fire), slam +16 (1d6+7 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 3d6 acid plus poison, Reflex DC 15 half, usable every 1d4 rounds), energized alacrity, energy attacks (acid), knockout strike

##### Statistics
**Str** 24, **Dex** 20, **Con** —, **Int** 15, **Wis** 11, **Cha** 5
**Base Atk** +10; **CMB** +18 (+22 grapple); **CMD** 33
**Feats** _[[feats/Acrobatic Steps|Acrobatic Steps]]_, Dodge, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Great Fortitude|Improved Great Fortitude]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_drill_)
**Skills** Acrobatics +8, _Climb_ +15, Fly +5, Knowledge (engineering) +19, Knowledge (nature) +19, Perception +13, Swim +15; Racial Modifiers +4 Knowledge (engineering), +4 Knowledge (nature)
**Languages** Common
**SQ** reprogram terrain, tactical awareness, technological wonders, _[[spells/Terraform|terraform]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or team (3-10)
**Treasure** none

##### Description

Commando constructs are elite fighting machines that often operate alone or in small squads. Although they are skilled combatants, these constructs can handle a variety of clandestine activities, including assassination, infiltration, kidnapping, and sabotage. They are most often found wandering the plains of Numeria, or under the service of a local warlord.

The sample _[[monsters/Commando Construct|commando construct]]_ presented here is built using a terraformer robot as the base creature. See that entry for full descriptions of its base abilities.