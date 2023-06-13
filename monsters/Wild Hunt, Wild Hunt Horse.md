---
cssclass: [monsters]
title1: Wild Hunt, Wild Hunt Horse
desc_short: This powerful steed stands upon wispy puffs of air, its grassymane and
  tail swishing majestically in the wind.
title2: Wild Hunt Horse
CR: 11
sources:
- name: Bestiary 6
  page: 280
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 12800
alignment: CN
size: Large
type: fey
subtypes:
- wild hunt
initiative:
  bonus: 4
senses:
  greensight: 60
  low-light vision: true
  scent: true
  see in darkness: true
AC:
  AC: 25
  touch: 17
  flat_footed: 20
  components:
    deflection: 3
    dex: 4
    dodge,+8 natural: 1
    size: -1
HP:
  HP: 142
  long: 19d6+76
saves:
  fort: 12
  ref: 15
  will: 12
defensive_abilities:
- freedom of movement
- instinctivecooperation
- wild grace
DR:
- amount: 10
  weakness: cold iron
immunities:
- cold
resistances:
  electricity: 10
  fire: 10
speeds:
  base: 100
  other_semicolon: air walk
attacks:
  melee:
  - - text: bite +21 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: bite
      bonus:
      - 21
    - text: 2 hooves +19 (1d10+6 plus bleed)
      entries:
      - - damage: 1d10+6
        - effect: bleed
      count: 2
      attack: hooves
      bonus:
      - 19
  special:
  - bewildering hoofbeats
  - bleed 1d6
  - deafening cry,wild gaze (DC 22)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: know direction
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: speak with plants
    source: default
    freq: Constant
  - name: transport via plants
    source: default
    freq: At will
    other: self and rider only
  - name: stone tell
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 13
    concentration: 16
ability_scores:
  STR: 34
  DEX: 19
  CON: 18
  INT: 9
  WIS: 12
  CHA: 17
BAB: 9
CMB: 22
CMB_other: +26 overrun
CMD: 40
CMD_other: 42 vs.overrun, 44 vs. trip
feats:
- name: Dodge
- name: Endurance
- name: Great Fortitude
- name: GreaterOverrun
- name: Improved Overrun
- name: Multiattack
- name: Power Attack
- name: Run
- name: Weapon Focus (bite)
- name: Weapon Focus (hoof)
skills:
  Acrobatics: 26
  Perception: 23
  Sense Motive: 23
  Stealth: 22
  Survival: 20
languages:
- Common
- Sylvan
- speak with animals,speak with plants
special_qualities:
- planar acclimation
- rider synergy,wild hunt link
ecology:
  environment: any land
  organization: solitary, herd (2-10), orwild hunt
  treasure_type: none
special_abilities:
  Bewildering Hoofbeats (Su): As a standard action, a wild hunt horse can make it
    seem as though hundreds of horses are approaching from all directions. All creatures
    within 60 feet must succeed at a DC 22 Will save or become confused for 1d4 rounds.
    A creature that succeeds at this save is immune to the bewildering hoofbeats ability
    of all wild hunt horses for 24 hours. The save DC is Charisma-based.
  Deafening Cry (Su): As a standard action up to three times per day (but no more
    than once every 1d4 rounds), a wild hunt horse can emit a thundering cry. All
    creatures in a 30-foot cone emanating from the horse take 10d6 points of sonic
    damage and are deafened for 1 minute. Creatures that succeed at a DC 23 Fortitude
    save take half damage and are not deafened. The save DC is Constitution-based.
  Rider Synergy (Su): When a wild hunt horse carries a rider with the wild hunt subtype,
    the two act as one. If either the rider or the mount would take damage, the rider
    and mount decide how to divide the damage (typically splitting it equally). Additionally,
    the rider's movement as a part of the horse's overrun combat maneuver does not
    provoke attacks of opportunity, unless that movement would also cause the horse
    to provoke attacks of opportunity.
  Wild Hunt Link (Su): A wild hunt horse increases the speed of all creatures in its
    wild hunt link by 30 feet. This increase is an enhancement bonus. It also grants
    the members of its link the effects of freedom of movement.
desc_long: When they are not participating in a hunt, wild hunt horses enjoy constructing
  complicated courses through land and sky and racing each other for ever-changing
  stakes.

---

# Wild Hunt, Wild Hunt Horse
This powerful steed stands upon wispy puffs of air, its grassy

mane and tail swishing majestically in the wind.
**Source** Bestiary 6 pg. 280
**XP** 12,800

CN Large fey (wild hunt)
**Init** +4; **Senses** _[[universal monster rules/Greensight|greensight]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_,

_[[universal monster rules/See in Darkness|see in darkness]]_; Perception +23

##### Defense

**AC** 25, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+3 deflection, +4 Dex, +1 _[[feats/Dodge|dodge]]_,

+8 natural, –1 size)
**hp** 142 (19d6+76)
**Fort** +12, **Ref** +15, **Will** +12
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, instinctive

cooperation, wild _[[spells/Grace|grace]]_; **DR** 10/cold iron; **Immune** cold; **Resist** electricity 10, fire 10

##### Offense
**Speed** 100 ft.; _[[spells/Air Walk|air walk]]_
**Melee** bite +21 (2d6+12), 2 hooves +19 (1d10+6 plus _[[universal monster rules/Bleed|bleed]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[items/Weapon Magic Abilities/Bewildering|bewildering]]_ hoofbeats, _bleed_ 1d6, deafening cry,

wild _[[universal monster rules/Gaze|gaze]]_ (DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +16)
Constant—_air walk_, _freedom of movement_, _[[spells/Know Direction|know direction]]_, _[[spells/Speak with Animals|speak with animals]]_, _[[spells/Speak with Plants|speak with plants]]_ 
At will—_[[spells/Transport via Plants|transport via plants]]_ (self and rider only) 
3/day—_[[spells/Stone Tell|stone tell]]_

##### Statistics
**Str** 34, **Dex** 19, **Con** 18, **Int** 9, **Wis** 12, **Cha** 17
**Base Atk** +9; **CMB** +22 (+26 overrun); **CMD** 40 (42 vs.

overrun, 44 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Great Fortitude|Great Fortitude]]_, Greater

Overrun, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, Run, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, hoof)
**Skills** Acrobatics +26, Perception +23, Sense Motive +23,

Stealth +22, Survival +20
**Languages** Common, Sylvan; _speak with animals_,

_speak with plants_
**SQ** _[[items/Weapon Magic Abilities/Planar|planar]]_ acclimation, rider synergy,

wild hunt link

##### Ecology

**Environment** any land
**Organization** solitary, herd (2–10), or

wild hunt
**Treasure** none

### Special Abilities

**_Bewildering_ Hoofbeats (Su)** As a standard action, a wild hunt _[[monsters/Horse|horse]]_ can make it seem as though hundreds of horses are approaching from all directions. All creatures within 60 feet must succeed at a DC 22 Will save or become _[[conditions/Confused|confused]]_ for 1d4 rounds. A creature that succeeds at this save is immune to the _bewildering_ hoofbeats ability of all wild hunt horses for 24 hours. The save DC is Charisma-based.

**Deafening Cry (Su)** As a standard action up to three times per day (but no more than once every 1d4 rounds), a wild hunt _horse_ can emit a _[[items/Weapon Magic Abilities/Thundering|thundering]]_ cry. All creatures in a 30-foot cone emanating from the _horse_ take 10d6 points of sonic damage and are _[[conditions/Deafened|deafened]]_ for 1 minute. Creatures that succeed at a DC 23 Fortitude save take half damage and are not _deafened_. The save DC is Constitution-based.

**Rider Synergy (Su)** When a wild hunt _horse_ carries a rider with the wild hunt subtype, the two act as one. If either the rider or the _[[spells/Mount|mount]]_ would take damage, the rider and _mount_ decide how to divide the damage (typically splitting it equally). Additionally, the rider’s movement as a part of the _horse_’s overrun combat maneuver does not provoke attacks of opportunity, unless that movement would also cause the _horse_ to provoke attacks of opportunity.

**Wild Hunt Link (Su)** A wild hunt _horse_ increases the speed of all creatures in its wild hunt link by 30 feet. This increase is an enhancement bonus. It also grants the members of its link the effects of _freedom of movement_.

##### Description

When they are not participating in a hunt, wild hunt horses enjoy constructing complicated courses through land and sky and racing each other for ever-changing stakes.