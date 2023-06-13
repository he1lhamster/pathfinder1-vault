---
cssclass: [monsters]
title1: Linnorm, Sea Linnorm
desc_short: This unfathomably large serpent sports a distinctly draconic face. Its
  body is deep, blackened gray with swatches of crimson. An entrancing set of lures
  dangles off its face, each glowing with a pulsating orange light accented by regular
  electrical discharges.
title2: Sea Linnorm
CR: 22
sources:
- name: 'Pathfinder #126: Beyond the Veiled Past'
  page: 90
  link: http://paizo.com/products/btpy9xf0?Pathfinder-Adventure-Path-126-Beyond-the-Veiled-Past
XP: 614400
alignment: NE
size: Colossal
type: dragon
subtypes:
- aquatic
initiative:
  bonus: 13
senses:
  darkvision: 60
  low-light vision: true
  scent: true
  true seeing: true
AC:
  AC: 39
  touch: 11
  flat_footed: 30
  components:
    dex: 9
    natural: 28
    size: -8
HP:
  HP: 455
  long: 26d12+286
  regeneration: 15
  regeneration_weakness: cold iron
saves:
  fort: 26
  ref: 24
  will: 23
defensive_abilities:
- freedom of movement
DR:
- amount: 20
  weakness: cold iron
immunities:
- curse effects
- electricity
- mind-affecting effects
- paralysis
- poison
- sleep
SR: 33
speeds:
  base: 40
  fly: 100
  fly_maneuverability: average
  swim: 100
attacks:
  melee:
  - - text: bite +35 (3d8+17/19-20 plus poison)
      entries:
      - - damage: 3d8+17
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 35
    - text: 2 claws +35 (2d8+17)
      entries:
      - - damage: 2d8+17
      count: 2
      attack: claws
      bonus:
      - 35
    - text: tail slap +30 (3d6+8 plus grab)
      entries:
      - - damage: 3d6+8
        - effect: grab
      attack: tail slap
      bonus:
      - 30
  special:
  - breath weapon (DC 34)
  - constrict (tail, 3d6+24)
  - death curse
  - lure
space: 30
reach: 30
ability_scores:
  STR: 44
  DEX: 28
  CON: 32
  INT: 7
  WIS: 27
  CHA: 29
BAB: 26
CMB: 51
CMD: 70
CMD_other: can't be tripped
feats:
- name: Cleave
- name: Combat Reflexes
- name: Following Step
- name: Great Cleave
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Snatch
- name: Step Up
- name: Step Up and Strike
- name: Vital Strike
skills:
  Acrobatics: 9
    when jumping: 13
  Fly: 30
  Perception: 37
  Stealth: 22
  Swim: 54
languages:
- Aklo
- Draconic
- Sylvan
special_qualities:
- amphibious
ecology:
  environment: cold oceans
  organization: solitary
  treasure_type: triple
special_abilities:
  Breath Weapon (Su): Once every 1d4 rounds as a standard action, a sea linnorm can
    expel a 120-foot line of intense stored bioelectricity, dealing 26d8 points of
    electricity damage to all creatures struck (Reflex DC 34 half). A secondary discharge
    arcs off each target that fails its save, striking the nearest creature within
    30 feet as long as that creature has not already been targeted by the breath weapon
    or another discharge. Secondary discharges do not cause tertiary discharges. The
    bioelectricity overwhelms the nervous systems of living creatures, causing any
    living creature that takes damage from the linnorm's breath weapon to be stunned
    for 1d4 rounds. A successful DC 34 Fortitude saving throw negates the stunning
    effect. Creatures struck by a secondary discharge receive a +4 bonus on this saving
    throw. The save DC is Constitution-based.
  Death Curse (Su): |-
    When a creature slays a sea linnorm, the slayer is affected by the curse of crushing depths.

     Curse of Crushing Depths: save Will DC 32; effect creature takes 3d6 points of damage every round while fully submerged in water, as though suffering water pressure damage, regardless of the creature's actual depth and bypassing any magical protection against water pressure (such as freedom of movement or life bubble). The save DC is Charisma-based.
  Lure (Su): As a free action, a sea linnorm can light the dangling lures on its head;
    any other creature within a 120-foot radius that can see the lure must succeed
    at a DC 32 Will save or become fascinated for 1 round. In addition to the regular
    effects of being fascinated, a creature affected by this ability also takes a
    -4 penalty on saving throws against the sea linnorm's breath weapon. Regardless
    of the preceding interactions between the sea linnorm and its target, a creature
    affected by this ability does not view the sea linnorm who has fascinated it as
    a potential threat until that sea linnorm actually attacks-allowing it to approach
    without breaking the fascination effect. Once a creature succeeds at its saving
    throw against this effect, it is immune to the same sea linnorm's lure ability
    for 24 hours. The save DC is Charisma-based.
  Poison (Ex): Bite-injury; save Fort DC 34; frequency 1/round for 10 rounds; effect
    8d8 points of electricity damage, 1d6 Dex drain, and 1d6 Con drain; cure 3 consecutive
    saves.
desc_long: |-
  Few, if any, linnorm breeds are more reclusive than the sea linnorm. These immense specimens of primeval draconic lineage dwell in the deepest underwater trenches of the world, blending into their surroundings thanks to their darkened scales. A sea linnorm's distinctive facial lures attract all manner of sea life, which the linnorm promptly feasts upon before returning to its lair. Luckily for all nonaquatic civilizations, sea linnorms rarely leave the ocean depths they call home.

   A typical sea linnorm grows up to 55 feet long and weighs around 14,000 pounds. It is believed that sea linnorms are effectively immortal, with the oldest recorded sea linnorms surviving well over 5,000 years.

---

# Linnorm, Sea Linnorm
This unfathomably large serpent sports a distinctly draconic face. Its body is deep, blackened _[[monsters/Gray|gray]]_ with swatches of crimson. An entrancing set of lures dangles off its face, each glowing with a pulsating orange light accented by regular electrical discharges.
**Source** Pathfinder #126: Beyond the Veiled Past pg. 90
**XP** 614,400

NE Colossal dragon (aquatic)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +37

##### Defense

**AC** 39, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+9 Dex, +28 natural, –8 size)
**hp** 455 (26d12+286); _[[universal monster rules/Regeneration|regeneration]]_ 15 (cold iron)
**Fort** +26, **Ref** +24, **Will** +23
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron; **Immune** curse effects, electricity, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 33

##### Offense
**Speed** 40 ft., fly 100 ft. (average), swim 100 ft.
**Melee** bite +35 (3d8+17/19–20 plus poison), 2 claws +35 (2d8+17), tail slap +30 (3d6+8 plus _[[universal monster rules/Grab|grab]]_)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (DC 34), _[[universal monster rules/Constrict|constrict]]_ (tail, 3d6+24), death curse, lure

##### Statistics
**Str** 44, **Dex** 28, **Con** 32, **Int** 7, **Wis** 27, **Cha** 29
**Base Atk** +26; **CMB** +51; **CMD** 70 (can't be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Following Step|Following Step]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Step Up and Strike|Step Up and Strike]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +9 (+13 when jumping), Fly +30, Perception +37, Stealth +22, Swim +54
**Languages** Aklo, Draconic, Sylvan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** cold oceans
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds as a standard action, a sea linnorm can expel a 120-foot line of intense stored bioelectricity, dealing 26d8 points of electricity damage to all creatures struck (Reflex DC 34 half). A secondary _[[spells/Discharge|discharge]]_ arcs off each target that fails its save, striking the nearest creature within 30 feet as long as that creature has not already been targeted by the _breath weapon_ or another _discharge_. Secondary discharges do not cause tertiary discharges. The bioelectricity overwhelms the nervous systems of living creatures, causing any living creature that takes damage from the linnorm’s _breath weapon_ to be _[[conditions/Stunned|stunned]]_ for 1d4 rounds. A successful DC 34 Fortitude saving throw negates the stunning effect. Creatures struck by a secondary _discharge_ receive a +4 bonus on this saving throw. The save DC is Constitution-based.

**Death Curse (Su)** When a creature slays a sea linnorm, the _[[classes/Slayer|slayer]]_ is affected by the curse of crushing depths.

Curse of Crushing Depths: save Will DC 32; effect creature takes 3d6 points of damage every round while fully submerged in water, as though suffering water pressure damage, regardless of the creature’s actual depth and bypassing any magical protection against water pressure (such as _freedom of movement_ or _[[spells/Life Bubble|life bubble]]_). The save DC is Charisma-based.

**Lure (Su)** As a free action, a sea linnorm can light the dangling lures on its head; any other creature within a 120-foot radius that can see the lure must succeed at a DC 32 Will save or become _[[conditions/Fascinated|fascinated]]_ for 1 round. In addition to the regular effects of being _fascinated_, a creature affected by this ability also takes a –4 penalty on saving throws against the sea linnorm’s _breath weapon_. Regardless of the preceding interactions between the sea linnorm and its target, a creature affected by this ability does not view the sea linnorm who has _fascinated_ it as a potential threat until that sea linnorm actually attacks—allowing it to approach without _[[items/Weapon Magic Abilities/Breaking|breaking]]_ the fascination effect. Once a creature succeeds at its saving throw against this effect, it is immune to the same sea linnorm’s lure ability for 24 hours. The save DC is Charisma-based.

**Poison (Ex)** Bite—injury; save Fort DC 34; frequency 1/round for 10 rounds; effect 8d8 points of electricity damage, 1d6 Dex drain, and 1d6 Con drain; cure 3 consecutive saves.

##### Description

Few, if any, linnorm breeds are more reclusive than the sea linnorm. These immense specimens of primeval draconic lineage dwell in the deepest _[[items/Weapon Magic Abilities/Underwater|underwater]]_ trenches of the world, blending into their surroundings thanks to their darkened scales. A sea linnorm’s distinctive facial lures attract all manner of sea life, which the linnorm promptly feasts upon before returning to its lair. Luckily for all nonaquatic civilizations, sea linnorms rarely leave the ocean depths they call home.

A typical sea linnorm grows up to 55 feet long and weighs around 14,000 pounds. It is believed that sea linnorms are effectively immortal, with the oldest recorded sea linnorms surviving well over 5,000 years.