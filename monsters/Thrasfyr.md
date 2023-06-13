---
cssclass: [monsters]
title1: Thrasfyr
desc_short: Neither quite bear nor bull nor serpent, this immense, six-legged creature
  is bound in chains and covered with scintillating red scales.
title2: Thrasfyr
CR: 17
sources:
- name: Bestiary 2
  page: 263
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 102400
alignment: CE
size: Huge
type: magical beast
subtypes:
- fire
initiative:
  bonus: 5
senses:
  darkvision: 120
  low-light vision: true
  see invisibility: true
AC:
  AC: 32
  touch: 9
  flat_footed: 31
  components:
    dex: 1
    natural: 23
    size: -2
HP:
  HP: 279
  long: 18d10+180
  regeneration: 15
  regeneration_weakness: acid or cold
saves:
  fort: 21
  ref: 14
  will: 15
DR:
- amount: 15
  weakness: cold iron and slashing
immunities:
- fire
- sonic
resistances:
  electricity: 30
SR: 28
weaknesses:
- vulnerable to cold
speeds:
  base: 50
  climb: 50
attacks:
  melee:
  - - text: 2 bites +26 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: bites
      bonus:
      - 26
    - text: 4 claws +26 (1d8+10)
      entries:
      - - damage: 1d8+10
      count: 4
      attack: claws
      bonus:
      - 26
    - text: gore +26 (2d6+10)
      entries:
      - - damage: 2d6+10
      attack: gore
      bonus:
      - 26
  special:
  - breath weapon (80-foot cone, 20d8 fire damage, Reflex DC 29 half, usable once
    every 1d4 rounds)
  - entangling chains
  - powerful charge (gore, 4d8+24)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: 1/day
    paren_text: self plus 50 lbs. of objects only, and only to a master's side
  sources:
  - name: default
    CL: 18
    concentration: 23
ability_scores:
  STR: 30
  DEX: 13
  CON: 31
  INT: 5
  WIS: 24
  CHA: 20
BAB: 18
CMB: 30
CMD: 41
CMD_other: 49 vs. trip
feats:
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
skills:
  Climb: 18
  Perception: 28
languages:
- Aklo
- Sylvan
special_qualities:
- master's bond
- planar acclimation
ecology:
  environment: any
  organization: solitary
  treasure_type: double
special_abilities:
  Entangling Chains (Su): A thrasfyr can control the six chains that hang from its
    body as if they were its own limbs. As a standard action, it can cause these chains
    to snake outward to a radius of 30 feet. All creatures in this area take 10d6
    points of slashing damage and become entangled-a DC 20 Reflex save halves the
    damage and negates the entangled condition. An entangled creature can escape with
    a DC 20 Reflex save or a DC 30 Escape Artist check made as a full-round action.
    The chains can also be sundered (hardness 10, hp 20, Break DC 28). The thrasfyr
    creates these chains from its own body-destroyed chains regrow in 24 hours. The
    save DC is Dexterity-based.
  Master's Bond (Su): A thrasfyr can form a bond with a willing creature by touching
    that creature. This allows the thrasfyr to communicate telepathically with the
    bonded creature with no range restriction (provided the thrasfyr and its master
    are on the same plane). Both thrasfyr and master can sense the other's condition
    as if both were under the effect of a status spell. A thrasfyr can maintain a
    bond with only one master at a time.
  Planar Acclimation (Ex): A thrasfyr is always considered to be on its home plane,
    regardless of what plane it finds itself upon. It never gains the extraplanar
    subtype.
desc_long: The legendary thrasfyr is one of the Tane-a group of powerful monsters
  created by godlike beings from the primal world of the fey. A thrasfyr without a
  master prefers to dwell in rugged hilly regions, where it spends most of its time
  slumbering and dreaming-it is said that all thrasfyrs dream of themselves as graceful
  and beautiful fey, for legends say that the first thrasfyrs were created from such
  creatures as a form of punishment.

---

# Thrasfyr
Neither quite bear nor bull nor serpent, this immense, six-legged creature is bound in chains and covered with scintillating red scales.
**Source** Bestiary 2 pg. 263
**XP** 102,400
CE Huge magical beast (fire)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +28

##### Defense

**AC** 32, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+1 Dex, +23 natural, –2 size)
**hp** 279 (18d10+180); _[[universal monster rules/Regeneration|regeneration]]_ 15 (acid or cold)
**Fort** +21, **Ref** +14, **Will** +15
**DR** 15/cold iron and slashing; **Immune** fire, sonic; **Resist** electricity 30; **SR** 28
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** 2 bites +26 (2d6+10), 4 claws +26 (1d8+10), gore +26 (2d6+10)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (80-foot cone, 20d8 fire damage, Reflex DC 29 half, usable once every 1d4 rounds), entangling chains, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d8+24)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +23)
Constant—_[[spells/Air Walk|air walk]]_, _see invisibility_
1/day—greater teleport (self plus 50 lbs. of objects only, and only to a master’s side)

##### Statistics
**Str** 30, **Dex** 13, **Con** 31, **Int** 5, **Wis** 24, **Cha** 20
**Base Atk** +18; **CMB** +30; **CMD** 41 (49 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _Climb_ +18, Perception +28
**Languages** Aklo, Sylvan
**SQ** master’s bond, _[[items/Weapon Magic Abilities/Planar|planar]]_ acclimation

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double

### Special Abilities

**Entangling Chains (Su)** A _[[monsters/Thrasfyr|thrasfyr]]_ can control the six chains that hang from its body as if they were its own limbs. As a standard action, it can cause these chains to snake outward to a radius of 30 feet. All creatures in this area take 10d6 points of slashing damage and become _[[conditions/Entangled|entangled]]_—a DC 20 Reflex save halves the damage and negates the _entangled_ condition. An _entangled_ creature can escape with a DC 20 Reflex save or a DC 30 Escape Artist check made as a full-round action. The chains can also be sundered (hardness 10, hp 20, Break DC 28). The _thrasfyr_ creates these chains from its own body—destroyed chains regrow in 24 hours. The save DC is Dexterity-based.

**Master’s Bond (Su)** A _thrasfyr_ can form a bond with a willing creature by touching that creature. This allows the _thrasfyr_ to communicate telepathically with the bonded creature with no range restriction (provided the _thrasfyr_ and its master are on the same plane). Both _thrasfyr_ and master can sense the other’s condition as if both were under the effect of a _[[spells/Status|status]]_ spell. A _thrasfyr_ can maintain a bond with only one master at a time.

**_Planar_ Acclimation (Ex)** A _thrasfyr_ is always considered to be on its home plane, regardless of what plane it finds itself upon. It never gains the extraplanar subtype.

##### Description

The legendary _thrasfyr_ is one of the Tane—a group of powerful monsters created by godlike beings from the primal world of the fey. A _thrasfyr_ without a master prefers to dwell in rugged hilly regions, where it spends most of its time slumbering and dreaming—it is said that all thrasfyrs _[[spells/Dream|dream]]_ of themselves as graceful and beautiful fey, for legends say that the first thrasfyrs were created from such creatures as a form of punishment.