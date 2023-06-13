---
cssclass: [monsters]
title1: Ghole
desc_short: The hulking form has a long, vulturelike neck ending in a headwith a disgusting,
  one-eyed visage.
title2: Ghole
CR: 12
sources:
- name: Bestiary 6
  page: 132
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 19200
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 8
senses:
  darkvision: 60
  scent sickness: true
AC:
  AC: 26
  touch: 14
  flat_footed: 22
  components:
    dex: 4
    natural: 12
HP:
  HP: 168
  long: 16d10+80
saves:
  fort: 12
  ref: 14
  will: 13
immunities:
- disease
speeds:
  base: 40
  burrow: 10
attacks:
  melee:
  - - text: bite +23 (2d6+10/17-20 plus disease)
      entries:
      - - damage: 2d6+10
          crit_range: 17-20
        - effect: disease
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23(1d8+7/19-20 plus disease)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
        - effect: disease
      count: 2
      attack: claws
      bonus:
      - 23
  special:
  - bolster disease
  - powerful bite
  - savage the sick,sneak attack +2d6
space: 5
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: gentle repose
    source: default
    freq: At will
  - name: restore corpse
    source: default
    freq: At will
  - name: ghoul touch
    source: default
    freq: 3/day
    DC: 15
  - name: hide from undead
    source: default
    freq: 3/day
  - name: haste
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 13
ability_scores:
  STR: 25
  DEX: 18
  CON: 21
  INT: 10
  WIS: 17
  CHA: 16
BAB: 16
CMB: 23
CMD: 37
feats:
- name: Cleave
- name: Combat Reflexes
- name: Great Cleave
- name: GreatFortitude
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: ImprovedInitiative
- name: Power Attack
skills:
  Perception: 22
  Sense Motive: 19
  Stealth: 23
  Survival: 22
languages:
- Common
special_qualities:
- change shape (Medium humanoid; alter self)
ecology:
  environment: any land
  organization: solitary, pair, or gang (3-6)
  treasure_type: standard
special_abilities:
  Bolster Disease (Su): A creature bitten by a ghole must succeed at a DC 23 Fortitude
    save or any disease it currently suffers from is bolstered. A disease bolstered
    in this way has its frequency doubled (so a disease that normally has a frequency
    of 1/day has its effects applied once every 12 hours) and can be cured only by
    magic. The bubonic plague carried by a ghole automatically gains these advantages.
    The save DC is Constitution-based.
  Disease (Ex): 'Bubonic Plague: Bite or claw- injury; save Fort DC 23; frequency
    2/day; effect 1d4 Con damage and 1 Cha damage and target is fatigued; cure -.'
  Powerful Bite (Ex): A ghole's bite attack always applies 1-1/2 times its Strength
    modifier to damage rolls and threatens a critical hit on a roll of 19-20. When
    a ghole bites an object, its bite treats the object as having a hardness of 5
    less than the object's actual hardness rating.
  Savage the Sick (Ex): Gholes are vicious when attacking a diseased foe. Against
    diseased targets, a ghole gains a +2 morale bonus on attack rolls and automatically
    adds its sneak attack damage to any damage it deals.
  Scent Sickness (Ex): A ghole has the scent ability against diseased creatures
desc_long: |-
  Gholes are foul denizens of the wilderness that feed upon rotten meat. Their ability to restore flesh to even the most ancient of skeletal remains allows them to harvest flesh from ruins long forgotten by the living. Many gholes keep their favorite skeletons handy to repeat beloved meals, while others hoard ancient skeletons and savor the flavor of restored flesh in a grisly mockery of a gourmand's appreciation of well aged wine or cheese. Many attempt to capture sick victims alive only to imprison them-sepulchers or crypts make for favorite prisons-so they perish of their sickness and thus provide the most delicious meal possible for the foul creature. 

  A typical ghole is 6 feet tall and weighs 250 pounds.

---

# Ghole
The hulking form has a long, vulturelike neck ending in a head

with a disgusting, one-eyed visage.
**Source** Bestiary 6 pg. 132
**XP** 19,200

NE Medium monstrous humanoid
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_ sickness; Perception +22

##### Defense

**AC** 26, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+4 Dex, +12 natural)
**hp** 168 (16d10+80)
**Fort** +12, **Ref** +14, **Will** +13
**Immune** disease

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 10 ft.
**Melee** bite +23 (2d6+10/17–20 plus disease), 2 claws +23

(1d8+7/19–20 plus disease)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** bolster disease, powerful bite, savage the sick,

sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
At will—_[[spells/Gentle Repose|gentle repose]]_, _[[spells/Restore Corpse|restore corpse]]_ 
3/day—_[[spells/Ghoul touch|ghoul touch]]_ (DC 15), _[[spells/Hide from Undead|hide from undead]]_ 
1/day—_[[spells/Haste|haste]]_

##### Statistics
**Str** 25, **Dex** 18, **Con** 21, **Int** 10, **Wis** 17, **Cha** 16
**Base Atk** +16; **CMB** +23; **CMD** 37
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Cleave|Great Cleave]]_, Great

Fortitude, _[[feats/Improved Critical|Improved Critical]]_ (bite, claw), Improved

Initiative, _[[feats/Power Attack|Power Attack]]_
**Skills** Perception +22, Sense Motive +19, Stealth +23,

Survival +22
**Languages** Common
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_Medium_ humanoid; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any land
**Organization** solitary, pair, or gang (3–6)
**Treasure** standard

### Special Abilities

**Bolster Disease (Su)** A creature bitten by a _[[monsters/Ghole|ghole]]_ must succeed at a DC 23 Fortitude save or any disease it currently suffers from is bolstered. A disease bolstered in this way has its frequency doubled (so a disease that normally has a frequency of 1/day has its effects applied once every 12 hours) and can be cured only by magic. The _[[diseases/Bubonic Plague|bubonic plague]]_ carried by a _ghole_ automatically gains these advantages. The save DC is Constitution-based.

**Disease (Ex)** _Bubonic Plague_: Bite or claw— injury; save Fort DC 23; frequency 2/day; effect 1d4 Con damage and 1 Cha damage and target is _[[conditions/Fatigued|fatigued]]_; cure —.

**Powerful Bite (Ex)** A _ghole_’s bite attack always applies 1-1/2 times its Strength modifier to damage rolls and threatens a critical hit on a roll of 19–20. When a _ghole_ bites an object, its bite treats the object as having a hardness of 5 less than the object’s actual hardness rating.
**Savage the Sick (Ex)** Gholes are _[[items/Weapon Magic Abilities/Vicious|vicious]]_ when attacking a diseased foe. Against diseased targets, a _ghole_ gains a +2 morale bonus on attack rolls and automatically adds its sneak attack damage to any damage it deals.
**_Scent_ Sickness (Ex)** A _ghole_ has the _scent_ ability against diseased creatures

##### Description

Gholes are foul denizens of the wilderness that feed upon rotten meat. Their ability to restore flesh to even the most ancient of skeletal remains allows them to harvest flesh from ruins long forgotten by the living. Many gholes keep their favorite skeletons handy to repeat beloved meals, while others hoard ancient skeletons and savor the flavor of restored flesh in a grisly mockery of a gourmand’s appreciation of well aged wine or cheese. Many attempt to capture sick victims alive only to imprison them—sepulchers or crypts make for favorite prisons—so they perish of their sickness and thus provide the most delicious meal possible for the foul creature.

A typical _ghole_ is 6 feet tall and weighs 250 pounds.