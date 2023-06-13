---
cssclass: [monsters]
title1: Psychopomp, Kere
desc_short: This unnaturally pale woman is dressed in the somber garb of a mourner,
  her countenance covered by a lengthy black veil.
title2: Kere
CR: 10
sources:
- name: 'Pathfinder #64: Beyond the Doomsday Door'
  page: 88
  link: http://paizo.com/products/btpy8t35?Pathfinder-Adventure-Path-64-Beyond-the-Doomsday
    Door
XP: 9600
alignment: N
size: Medium
type: outsider
subtypes:
- psychopomp
- extraplanar
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  spiritsense: true
AC:
  AC: 22
  touch: 15
  flat_footed: 17
  components:
    dex: 5
    natural: 7
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 8
  ref: 15
  will: 13
DR:
- amount: 10
  weakness: adamantine
immunities:
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
SR: 21
speeds:
  base: 30
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +17 (1d4+3 plus 1d6 cold)
      entries:
      - - damage: 1d4+3
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 17
    - text: shroud +17 (infectious fear)
      entries:
      - - effect: infectious fear
      attack: shroud
      bonus:
      - 17
  special:
  - infectious fear (DC 20)
  - veil of tears
space: 5
reach: 5
reach_other: 15 ft. with shroud
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: At will
    DC: 14
  - name: grave tell
    source: default
    freq: At will
  - name: greater invisibility
    source: default
    freq: At will
  - name: hide from undead
    source: default
    freq: At will
    DC: 15
  - name: minor image
    source: default
    freq: At will
    DC: 16
  - name: searing light
    source: default
    freq: At will
  - name: whispering wind
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: 3/day
  - name: mage's faithful hound
    source: default
    freq: 3/day
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 19
  - name: speak with dead
    source: default
    freq: 3/day
    DC: 17
  - name: waves of fatigue
    source: default
    freq: 3/day
  - name: gate
    source: default
    freq: 1/day
    paren_text: to the Boneyard or Material Plane only; planar travel only
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 16
  DEX: 21
  CON: 18
  INT: 13
  WIS: 20
  CHA: 19
BAB: 12
CMB: 15
CMD: 30
feats:
- name: Alertness
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Stealthy
- name: Weapon Finesse
skills:
  Escape Artist: 7
  Fly: 28
  Intimidate: 19
  Knowledge (history): 16
  Knowledge (religion): 16
  Perception: 24
  Sense Motive: 24
  Stealth: 24
languages:
- Abyssal
- Celestial
- Common
- Infernal
special_qualities:
- grave dependent
- grave meld
ecology:
  environment: any (graveyards or the Boneyard)
  organization: solitary
  treasure_type: standard
special_abilities:
  Grave Dependent (Su): A kere is mystically bonded to a single gravestone-typically
    the most impressive or oldest in a graveyard-and must never stray more than 300
    yards from it. A kere who moves 300 yards beyond her bonded grave immediately
    becomes visible and unable to use any of her spell-like abilities. A kere who
    is out of range of her bonded grave for 24 hours takes 1d6 points of Constitution
    damage, and another 1d6 points of Constitution damage every day of separation
    that follows-eventually, this separation kills the kere. A kere can break this
    bond or forge a new bond with a new grave by performing a 24-hour ritual and making
    a successful DC 20 Will save. If a kere is not bonded with a grave, she must either
    actively try to forge a new bond or attempt to return to the Boneyard (where she
    takes no penalties from not being bonded).
  Grave Meld (Su): A kere can meld with any gravestone or funerary sculpture, similarly
    to how the spell meld into stone functions. She can remain melded with such a
    structure as long as she wishes.
  Grave Tell (Sp): This ability functions as the spell stone tell, but only affects
    stone funerary structures, like gravestones, cemetery monuments, lych-gates, mausoleums,
    and similar constructions.
  Infectious Fear (Su): Any creature struck by a kere's shroud must succeed at a DC
    20 Will save or become frightened for 2d4 rounds. Any creature that physically
    touches a creature frightened by this effect must succeed at a DC 20 Will save
    as well or also be frightened for 2d4 rounds (though the fear of the creature
    touched is not contagious). The save DC is Charisma-based.
  Shroud (Ex): A kere's shroud is an insubstantial thing that only a kere can touch.
    Creatures that come into contact with this shroud find it to be as insubstantial
    as mist-though they often do feel the terror it inspires. A creature that is unaware
    of a kere and is struck by her shroud is not aware that a weapon has struck it.
    A kere's shroud vaporizes upon its owner's death.
  Spiritsense (Su): A psychopomp notices, locates, and can distinguish between living
    and undead creatures within 60 feet, just as if she possessed the blindsight ability.
  Spirit Touch (Ex): A psychopomp's natural weapons, as well as any weapon it wields,
    are treated as though they had the ghost touch weapon special ability.
  Veil of Tears (Su): Any graveyard that hosts a kere is gloomier and more solemn.
    All exterior areas within such a graveyard are perpetually affected by darkness
    and mind fog (Will DC 20). Additionally, any undead creature that enters the area
    is also affected as per the spell slow (Will DC 20). Those who save against these
    effects are immune to the graveyard's veil of tears for the next 24 hours. Those
    who fail are affected by these penalties for as long as they remain in the graveyard.
    A veil of tears can be raised or lowered by the resident kere as a free action.
    The veil disperses if a kere leaves the graveyard or is destroyed, and rises upon
    her return. The veil can also be dispelled for 1 day by casting dispel magic or
    a similar spell upon the kere's bonded gravestone. The spell effects are cast
    at the kere's caster level (usually 11th). The saving throw DCs are based on the
    resident kere's Charisma.
desc_long: |-
  Certain places are sacred, settings meant to remain free of the raucous sounds and defiling touch of the living. Graveyards number among some of the most obvious of such places, where stone guardians and the buried weight of the dead bear on visitors with undeniable gravity. But certain forces disregard the fundamental sanctity of such ground-mortal and deathless heretics who use such places to hunt, feed, or cloak fouler deeds. Yet not all cemeteries are unguarded, and the vaporous shadows and palpable dread of some burial grounds suggest not corruption, but the custody of an ominous otherworldly guardian.

  Keres, like all psychopomps, are emissaries of the Boneyard, the necropolis that all mortals must traverse at the end of life. While most psychopomps concern themselves with the souls of the recently deceased, keres mind the resting places of the dead. Their stewardship derives not from any otherworldly care for the deteriorating dust left in the wake of mortal life, but rather from an interest in those who come seeking the dead where they lie. Such creatures often engage in perversions keres seek to oppose. To this end, keres take up lonely residences amid the tombs and monuments of graveyards, spreading an ominous air and giving rise to tales of hauntings and strange encounters to deter even the boldest intruders from trespassing upon the fields they tend.

  Keres appear as pale, sickly women standing about 5 feet tall and weighing less than 100 pounds.

---

# Psychopomp, Kere
This unnaturally pale woman is dressed in the somber garb of a mourner, her countenance covered by a lengthy black _[[spells/Veil|veil]]_.
**Source** Pathfinder #64: Beyond the Doomsday Door pg. 88
**XP** 9,600

N Medium outsider (psychopomp, extraplanar)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, spiritsense; Perception +24

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 Dex, +7 natural)
**hp** 114 (12d10+48)
**Fort** +8, **Ref** +15, **Will** +13
**DR** 10/adamantine; **Immune** death effects, disease, poison; **Resist** cold 10, electricity 10; **SR** 21

##### Offense
**Speed** 30 ft., fly 30 ft. (perfect)
**Melee** 2 claws +17 (1d4+3 plus 1d6 cold), shroud +17 (infectious _[[universal monster rules/Fear|fear]]_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with shroud)
**Special Attacks** infectious _fear_ (DC 20), _veil_ of tears
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
At will—_[[spells/Ghost Sound|ghost sound]]_ (DC 14), grave tell, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Hide from Undead|hide from undead]]_ (DC 15), _[[spells/Minor Image|minor image]]_ (DC 16), _[[spells/Searing Light|searing light]]_, _[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Fog Cloud|fog cloud]]_, mage’s faithful hound, _[[spells/Mirage Arcana|mirage arcana]]_ (DC 19), _[[spells/Speak with Dead|speak with dead]]_ (DC 17), _[[spells/Waves of Fatigue|waves of fatigue]]_
1/day—_[[spells/Gate|gate]]_ (to the Boneyard or Material Plane only; _[[items/Weapon Magic Abilities/Planar|planar]]_ travel only)

##### Statistics
**Str** 16, **Dex** 21, **Con** 18, **Int** 13, **Wis** 20, **Cha** 19
**Base Atk** +12; **CMB** +15; **CMD** 30
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Escape Artist +7, Fly +28, Intimidate +19, Knowledge (history) +16, Knowledge (religion) +16, Perception +24, Sense Motive +24, Stealth +24
**Languages** Abyssal, Celestial, Common, Infernal
**SQ** grave dependent, grave meld

##### Ecology

**Environment** any (graveyards or the Boneyard)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Grave Dependent (Su)** A kere is mystically bonded to a single gravestone—typically the most impressive or oldest in a graveyard—and must never stray more than 300 yards from it. A kere who moves 300 yards beyond her bonded grave immediately becomes visible and unable to use any of her _spell-like abilities_. A kere who is out of range of her bonded grave for 24 hours takes 1d6 points of Constitution damage, and another 1d6 points of Constitution damage every day of separation that follows—eventually, this separation kills the kere. A kere can break this bond or forge a new bond with a new grave by performing a 24-hour ritual and making a successful DC 20 Will save. If a kere is not bonded with a grave, she must either actively try to forge a new bond or attempt to return to the Boneyard (where she takes no penalties from not being bonded).

**Grave Meld (Su)** A kere can meld with any gravestone or funerary sculpture, similarly to how the spell _[[spells/Meld into Stone|meld into stone]]_ functions. She can remain melded with such a structure as long as she wishes.

**Grave Tell (Sp)** This ability functions as the spell _[[spells/Stone Tell|stone tell]]_, but only affects stone funerary structures, like gravestones, cemetery monuments, lych-gates, mausoleums, and similar constructions.

**Infectious _Fear_ (Su)** Any creature struck by a kere’s shroud must succeed at a DC 20 Will save or become _[[conditions/Frightened|frightened]]_ for 2d4 rounds. Any creature that physically touches a creature _frightened_ by this effect must succeed at a DC 20 Will save as well or also be _frightened_ for 2d4 rounds (though the _fear_ of the creature touched is not contagious). The save DC is Charisma-based.
**Shroud (Ex)** A kere’s shroud is an insubstantial thing that only a kere can touch. Creatures that come into contact with this shroud find it to be as insubstantial as mist—though they often do feel the terror it inspires. A creature that is unaware of a kere and is struck by her shroud is not aware that a weapon has struck it. A kere’s shroud vaporizes upon its owner’s death.
**Spiritsense (Su)** A psychopomp notices, locates, and can distinguish between living and undead creatures within 60 feet, just as if she possessed the _[[universal monster rules/Blindsight|blindsight]]_ ability.
**Spirit Touch (Ex)** A psychopomp’s natural weapons, as well as any weapon it wields, are treated as though they had the _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ weapon special ability.

**_Veil_ of Tears (Su)** Any graveyard that hosts a kere is gloomier and more solemn. All exterior areas within such a graveyard are perpetually affected by _[[spells/Darkness|darkness]]_ and _[[spells/Mind Fog|mind fog]]_ (Will DC 20). Additionally, any undead creature that enters the area is also affected as per the spell _[[spells/Slow|slow]]_ (Will DC 20). Those who save against these effects are immune to the graveyard’s _veil_ of tears for the next 24 hours. Those who fail are affected by these penalties for as long as they remain in the graveyard. A _veil_ of tears can be raised or lowered by the resident kere as a free action. The _veil_ disperses if a kere leaves the graveyard or is destroyed, and rises upon her return. The _veil_ can also be dispelled for 1 day by casting _[[spells/Dispel Magic|dispel magic]]_ or a similar spell upon the kere’s bonded gravestone. The spell effects are cast at the kere’s caster level (usually 11th). The saving throw DCs are based on the resident kere’s Charisma.

##### Description

Certain places are _[[items/Weapon Magic Abilities/Sacred|sacred]]_, settings meant to remain free of the raucous sounds and defiling touch of the living. Graveyards number among some of the most obvious of such places, where stone guardians and the buried weight of the dead bear on visitors with undeniable gravity. But certain forces disregard the fundamental sanctity of such ground—mortal and _[[spells/Deathless|deathless]]_ heretics who use such places to hunt, feed, or cloak fouler deeds. Yet not all cemeteries are unguarded, and the vaporous shadows and palpable dread of some burial grounds suggest not corruption, but the custody of an _[[items/Weapon Magic Abilities/Ominous|ominous]]_ otherworldly _[[items/Weapon Magic Abilities/Guardian|guardian]]_.

Keres, like all psychopomps, are emissaries of the Boneyard, the necropolis that all mortals must traverse at the end of life. While most psychopomps concern themselves with the souls of the recently deceased, keres mind the resting places of the dead. Their stewardship derives not from any otherworldly care for the deteriorating dust left in the wake of mortal life, but rather from an interest in those who come seeking the dead where they lie. Such creatures often engage in perversions keres seek to oppose. To this end, keres take up lonely residences amid the tombs and monuments of graveyards, spreading an _ominous_ air and giving rise to tales of hauntings and strange encounters to deter even the boldest intruders from trespassing upon the fields they tend.

Keres appear as pale, sickly women standing about 5 feet tall and weighing less than 100 pounds.