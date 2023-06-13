---
cssclass: [monsters]
title1: Smoke Sentinel
desc_short: This cloud of thick black smoke crackles as flashes of electricity illuminate
  it from within, but it whirs as if mechanical.
title2: Smoke Sentinel
CR: 9
sources:
- name: 'Pathfinder #122: Into the Shattered Continent'
  page: 88
  link: http://paizo.com/products/btpy9uk0?Pathfinder-Adventure-Path-122-Into-the-Shattered-Continent
XP: 6400
alignment: N
size: Huge
type: construct
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  see alignment: true
AC:
  AC: 20
  touch: 20
  flat_footed: 14
  components:
    deflection: 6
    dex: 5
    dodge: 1
    size: -2
HP:
  HP: 98
  long: 9d10+49
saves:
  fort: 3
  ref: 8
  will: 8
defensive_abilities:
- gaseous
immunities:
- construct traits
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 tendrils +12 touch (3d6 electricity)
      entries:
      - - damage: 3d6
          type: electricity
      count: 2
      attack: tendrils
      bonus:
      - 12
      touch: true
  special:
  - engulf (DC 21, 1d6 Wis)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: see alignment
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  - name: fear
    source: default
    freq: At will
    DC: 20
  - name: major image
    source: default
    freq: 3/day
    DC: 19
  sources:
  - name: default
    CL: 9
    concentration: 15
ability_scores:
  STR:
  DEX: 21
  CON:
  INT: 10
  WIS: 20
  CHA: 23
BAB: 9
CMB: 11
CMD: 33
CMD_other: can't be tripped
feats:
- name: Ability Focus (engulf)
- name: Dodge
- name: Improved Initiative
- name: Toughness
- name: Weapon Finesse
skills:
  Fly: 9
  Perception: 14
  Stealth: 6
languages:
- tongues (can't speak in natural form)
special_qualities:
- change shape (Small or Medium humanoid, alter self)
- tethered
ecology:
  environment: temperate or warm forests
  organization: solitary
  treasure_type: incidental
special_abilities:
  Engulf (Ex): A smoke sentinel can engulf creatures in its path as a standard action.
    The smoke sentinel merely has to move over its opponents, and it affects as many
    creatures as it can cover. It cannot make other attacks during a round in which
    it engulfs a creature. A targeted creature can make an attack of opportunity against
    the smoke sentinel, but if it does so, it is not entitled to a saving throw against
    the engulf attack. A creature that does not make an attack of opportunity can
    attempt a DC 21 Reflex saving throw to avoid being engulfed; on a success, it
    is pushed back or aside (target's choice) as the smoke sentinel moves forward.
    An engulfed creature takes 1d6 points of Wisdom damage at the start of its turn
    each round it remains within the smoke sentinel's space. The save DC is Dexterity-based
    and includes a +2 racial bonus.
  Gaseous (Ex): A smoke sentinel can pass through small holes and even cracks without
    reducing its speed. It cannot enter water or other liquids. It has no Strength
    score and cannot manipulate objects. Its gaseous form renders the smoke sentinel
    immune to all nonmagical attack forms. Even when hit by spells or magic weapons,
    it takes only half damage. Spells and effects that do not deal damage have only
    a 50% chance of affecting a smoke sentinel. A smoke sentinel has no natural armor
    bonus, but it has a deflection bonus equal to its Charisma bonus.
  Tethered (Su): A smoke sentinel is tethered to a hollow physical object (usually
    a small box or totem) from which it can travel no farther than 1 mile. An intelligent
    creature who holds the construct's tether for at least 1 hour gains the ability
    to control the smoke sentinel as though it were the target of a dominate monster
    spell. This control lasts until another intelligent creature holds the tether
    for an hour or more, whereupon that creature gains control of the construct. If
    its controller dies or otherwise ceases to command the smoke sentinel, the construct
    continues carrying out its most recent command. Should its last command be a finite
    task, the smoke sentinel reverts to the role of guardian when finished, keeping
    potential threats away from the site of its tether. A smoke sentinel can compress
    to fit within its tether as a fullround action. While in the tether, it recovers
    from damage at a rate of 1 hit point per hour.
desc_long: |-
  Smoke sentinels are clouds of sentient black smoke that protect isolated ruins throughout the shattered continent of Azlant. As amorphous clouds, smoke sentinels have no distinguishing features, but they often extend their bodies into long tendrils that slither along the ground like hungry vines. No matter how thin a smoke sentinel may make its form, its smoke remains thick and opaque, hiding everything within it from view. Though the strange electrical energy that courses through its body crackles and arcs, the resulting illumination provides no insight into what may lie at the cloud's heart.

   A smoke sentinel usually attempts to determine an intruder's intentions through use of its see alignment and detect thoughts spell-like abilities. It may take the form of a trusted associate or loved one in order to further interact with the trespasser and bring deeper thoughts and motivations to the creature's surface thoughts. Unless directly threatened or certain that the target of its investigation poses a threat to its master or other sworn charge, the smoke sentinel employs illusions and fear to confuse and frighten the interloper away. Only in extreme cases or when instructed to do so does the construct use its deadly physical attacks.

   While it can compress and condense its form to fit into incredibly small spaces, a smoke sentinel most often appears as a weightless cloud occupying approximately 3,500 cubic feet of space.

---

# Smoke Sentinel
This cloud of thick black smoke crackles as flashes of electricity illuminate it from within, but it whirs as if mechanical.
**Source** Pathfinder #122: Into the Shattered Continent pg. 88
**XP** 6,400

N Huge construct
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Alignment|see alignment]]_; Perception +14

##### Defense

**AC** 20, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+6 deflection, +5 Dex, +1 _[[feats/Dodge|dodge]]_, –2 size)
**hp** 98 (9d10+49)
**Fort** +3, **Ref** +8, **Will** +8
**Defensive Abilities** gaseous; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 2 tendrils +12 touch (3d6 electricity)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Engulf|engulf]]_ (DC 21, 1d6 Wis)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +15)
Constant—_see alignment_, _[[spells/Tongues|tongues]]_ 
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[universal monster rules/Fear|fear]]_ (DC 20) 
3/day—_[[spells/Major Image|major image]]_ (DC 19)

##### Statistics
**Str** —, **Dex** 21, **Con** —, **Int** 10, **Wis** 20, **Cha** 23
**Base Atk** +9; **CMB** +11; **CMD** 33 (can't be tripped)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_engulf_), _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Fly +9, Perception +14, Stealth +6
**Languages** _tongues_ (can’t speak in natural form)
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or _[[classes/Medium|Medium]]_ humanoid, _[[spells/Alter Self|alter self]]_), tethered

##### Ecology

**Environment** temperate or warm forests
**Organization** solitary
**Treasure** incidental

### Special Abilities

**_Engulf_ (Ex)** A _[[monsters/Smoke Sentinel|smoke sentinel]]_ can _engulf_ creatures in its path as a standard action. The _smoke sentinel_ merely has to move over its opponents, and it affects as many creatures as it can cover. It cannot make other attacks during a round in which it engulfs a creature. A targeted creature can make an attack of opportunity against the _smoke sentinel_, but if it does so, it is not entitled to a saving throw against the _engulf_ attack. A creature that does not make an attack of opportunity can attempt a DC 21 Reflex saving throw to avoid being engulfed; on a success, it is pushed back or aside (target’s choice) as the _smoke sentinel_ moves forward. An engulfed creature takes 1d6 points of Wisdom damage at the start of its turn each round it remains within the _smoke sentinel_’s space. The save DC is Dexterity-based and includes a +2 racial bonus.

**Gaseous (Ex)** A _smoke sentinel_ can pass through small holes and even cracks without reducing its speed. It cannot enter water or other liquids. It has no Strength score and cannot manipulate objects. Its _[[spells/Gaseous Form|gaseous form]]_ renders the _smoke sentinel_ immune to all nonmagical attack forms. Even when hit by spells or magic weapons, it takes only half damage. Spells and effects that do not deal damage have only a 50% chance of affecting a _smoke sentinel_. A _smoke sentinel_ has no natural armor bonus, but it has a _deflection_ bonus equal to its Charisma bonus.

**Tethered (Su)** A _smoke sentinel_ is tethered to a hollow physical object (usually a small box or totem) from which it can travel no farther than 1 mile. An intelligent creature who holds the construct’s tether for at least 1 hour gains the ability to control the _smoke sentinel_ as though it were the target of a _[[spells/Dominate Monster|dominate monster]]_ spell. This control lasts until another intelligent creature holds the tether for an hour or more, whereupon that creature gains control of the construct. If its controller dies or otherwise ceases to _[[spells/Command|command]]_ the _smoke sentinel_, the construct continues carrying out its most recent _command_. Should its last _command_ be a finite task, the _smoke sentinel_ reverts to the role of _[[items/Weapon Magic Abilities/Guardian|guardian]]_ when finished, keeping potential threats away from the site of its tether. A _smoke sentinel_ can compress to fit within its tether as a fullround action. While in the tether, it recovers from damage at a rate of 1 hit point per hour.

##### Description

Smoke sentinels are clouds of sentient black smoke that protect isolated ruins throughout the shattered continent of Azlant. As _[[universal monster rules/Amorphous|amorphous]]_ clouds, smoke sentinels have no distinguishing features, but they often extend their bodies into long tendrils that slither along the ground like hungry vines. No matter how thin a _smoke sentinel_ may make its form, its smoke remains thick and opaque, hiding everything within it from view. Though the strange electrical energy that courses through its body crackles and arcs, the resulting illumination provides no insight into what may lie at the cloud’s heart.

A _smoke sentinel_ usually attempts to determine an intruder’s intentions through use of its _see alignment_ and _detect thoughts_ _spell-like abilities_. It may take the form of a trusted _[[feats/Associate|associate]]_ or loved one in order to further interact with the trespasser and bring deeper thoughts and motivations to the creature’s surface thoughts. Unless directly threatened or certain that the target of its investigation poses a threat to its master or other sworn charge, the _smoke sentinel_ employs illusions and _fear_ to confuse and frighten the interloper away. Only in extreme cases or when instructed to do so does the construct use its _[[items/Weapon Magic Abilities/Deadly|deadly]]_ physical attacks.

While it can compress and condense its form to fit into incredibly small spaces, a _smoke sentinel_ most often appears as a weightless cloud occupying approximately 3,500 cubic feet of space.