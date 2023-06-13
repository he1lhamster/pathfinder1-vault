---
cssclass: [monsters]
title1: Robot, Terraformer Robot
desc_short: This large robot's arms end in an assortment of drills, torches,hammers,
  and vices.
title2: Terraformer Robot
CR: 7
sources:
- name: Bestiary 5
  page: 209
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 3200
alignment: N
size: Large
type: construct
subtypes:
- robot
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 22
  touch: 12
  flat_footed: 19
  components:
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 85
  long: 10d10+30
saves:
  fort: 5
  ref: 6
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
  fly 10 ft. (clumsy),swim: 20
attacks:
  melee:
  - - text: integrated drill +15 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: integrated drill
      bonus:
      - 15
    - text: slam +14 (1d6+5 plus grab)
      entries:
      - - damage: 1d6+5
        - effect: grab
      attack: slam
      bonus:
      - 14
    - text: integrated laser torch +14 touch (1d6 fire)
      entries:
      - - damage: 1d6
          type: fire
      attack: integrated laser torch
      bonus:
      - 14
      touch: true
  special:
  - breath weapon (30-ft. cone, 3d6 acid pluspoison, Reflex DC 15 half, usable every
    1d4 rounds)
space: 10
reach: 10
ability_scores:
  STR: 20
  DEX: 16
  CON:
  INT: 15
  WIS: 11
  CHA: 5
BAB: 10
CMB: 16
CMD: 29
feats:
- name: Acrobatic Steps
- name: Great Fortitude
- name: ImprovedGreat Fortitude
- name: Nimble Moves
- name: WeaponFocus (drill)
skills:
  Acrobatics: 6
  Climb: 13
  Fly: 3
  Knowledge (engineering): 19
  Knowledge (nature): 19
  Perception: 13
  Swim: 13
  _racial_mods:
    _other: +4 Knowledge(engineering)
    Knowledge (nature):
      _: 4
languages:
- Common
special_qualities:
- reprogram terrain
- technologicalwonders
- terraform
ecology:
  environment: any
  organization: solitary, pair, or team (3-10)
  treasure_type: none
special_abilities:
  Poison (Ex): Breath weapon-inhaled; save Fort DC 15;frequency 1/round for 6 rounds;
    effect 1d3 Con; cure 2consecutive saves.
  Reprogram Terrain (Ex): Three times per day as an actionthat takes 1 full round,
    a terraformer can release a cloudof nanites that mimics the effects of one of
    the followingspells, using the terraformer's Hit Dice as the caster level:expeditious
    excavation, soften earth and stone, orstone shape.
  Terraform (Ex): 'Ten terraformers working in tandem can createremarkable effects
    over long periods of time, causingpermanent changes to the local environment.
    The robotsmust maintain line of effect to each other, and each mustbe within 1
    mile of one other terraformer. If they do this fora period of at least 2 weeks,
    one of the following effects(robots' choice) occurs in a 1-mile radius: the terrain
    isshaped as per move earth; water in the area is altered asper control water;
    plants in the area are affected as per eitherplant growth or diminish plants;
    or the average temperaturein the area is raised or lowered by 10° Fahrenheit.'
  Technological Wonders (Ex): Effects from a terraformer'sabilities are nonmagical
    in nature, and can't be identified,dispelled, or affected by effects that can
    affect only spells.The duration of these effects never expires.
desc_long: Terraformer robots are sent to planets to pave the way formilitary bases,
  trading outposts, or settlements. A planetdesignated as a waystation might require
  only a few robots,but those marked for permanent habitation might havetheir skies
  darkened by hordes of terraformers, forming ahovering lattice around the globe.

---

# Robot, Terraformer Robot
This large robot’s arms end in an assortment of drills, torches,

hammers, and vices.
**Source** Bestiary 5 pg. 209
**XP** 3,200

N Large construct (robot)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 Dex, +10 natural, –1 size)
**hp** 85 (10d10+30)
**Fort** +5, **Ref** +6, **Will** +3
**Defensive Abilities** hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** acid 5, cold 5, fire 15
**Weaknesses** vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 10 ft. (clumsy),

swim 20 ft.
**Melee** integrated _[[items/Mundane/Drill|drill]]_ +15 (1d6+5), slam +14 (1d6+5 plus _[[universal monster rules/Grab|grab]]_),

integrated laser _[[items/Mundane/Torch|torch]]_ +14 touch (1d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 3d6 acid plus

poison, Reflex DC 15 half, usable every 1d4 rounds)

##### Statistics
**Str** 20, **Dex** 16, **Con** —, **Int** 15, **Wis** 11, **Cha** 5
**Base Atk** +10; **CMB** +16; **CMD** 29
**Feats** _[[feats/Acrobatic Steps|Acrobatic Steps]]_, _[[feats/Great Fortitude|Great Fortitude]]_, Improved

_Great Fortitude_, _[[feats/Nimble Moves|Nimble Moves]]_, Weapon

Focus (_drill_)
**Skills** Acrobatics +6, _Climb_ +13, Fly +3,

Knowledge (engineering) +19,

Knowledge (nature) +19,

Perception +13, Swim +13;

Racial Modifiers +4 Knowledge

(engineering), +4 Knowledge (nature)
**Languages** Common
**SQ** reprogram terrain, technological

wonders, _[[spells/Terraform|terraform]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or team (3–10)
**Treasure** none

### Special Abilities

**Poison (Ex)** _Breath weapon_—inhaled; save Fort DC 15;

frequency 1/round for 6 rounds; effect 1d3 Con; cure 2

consecutive saves.

**Reprogram Terrain (Ex)** Three times per day as an action

that takes 1 full round, a terraformer can release a cloud

of nanites that mimics the effects of one of the following

spells, using the terraformer’s Hit Dice as the caster level:

_[[spells/Expeditious Excavation|expeditious excavation]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_, or

_[[spells/Stone Shape|stone shape]]_.

**_Terraform_ (Ex)** Ten terraformers working in tandem can create

remarkable effects over long periods of time, causing

permanent changes to the local environment. The robots

must maintain line of effect to each other, and each must

be within 1 mile of one other terraformer. If they do this for

a period of at least 2 weeks, one of the following effects

(robots’ choice) occurs in a 1-mile radius: the terrain is

shaped as per _[[spells/Move Earth|move earth]]_; water in the area is altered as

per _[[spells/Control Water|control water]]_; plants in the area are affected as per either

_[[spells/Plant Growth|plant growth]]_ or _[[spells/Diminish Plants|diminish plants]]_; or the average temperature

in the area is raised or lowered by 10° Fahrenheit.

**Technological Wonders (Ex)** Effects from a terraformer’s

abilities are nonmagical in nature, and can’t be identified,

dispelled, or affected by effects that can affect only spells.

The duration of these effects never expires.

##### Description

Terraformer robots are sent to planets to pave the way for

military bases, trading outposts, or settlements. A planet

designated as a waystation might require only a few robots,

but those marked for permanent habitation might have

their skies darkened by hordes of terraformers, forming a

hovering lattice around the globe.