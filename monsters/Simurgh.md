---
cssclass: [monsters]
title1: Simurgh
desc_short: This massive creature has the body of a resplendent bird but the head
  of a regal canine.
title2: Simurgh
CR: 18
sources:
- name: Bestiary 3
  page: 245
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #24: The Final Wish'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy89a2
XP: 153600
alignment: NG
size: Gargantuan
type: magical beast
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect evil: true
  detect magic: true
  low-light vision: true
auras:
- name: peace
  radius: 50
AC:
  AC: 34
  touch: 10
  flat_footed: 30
  components:
    dex: 3
    dodge: 1
    natural: 24
    size: -4
HP:
  HP: 324
  long: 24d10+192
saves:
  fort: 22
  ref: 17
  will: 14
immunities:
- ability damage
- ability drain
- disease
- fire
- negative energy
- petrification
- poison
- sleep
resistances:
  acid: 10
  cold: 10
  electricity: 10
SR: 29
speeds:
  base: 40
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +32 (2d8+12 plus 2d6 fire)
      entries:
      - - damage: 2d8+12
        - damage: 2d6
          type: fire
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d8+12 plus 2d6 fire)
      entries:
      - - damage: 2d8+12
        - damage: 2d6
          type: fire
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +30 (1d4+6 plus banishing swipe)
      entries:
      - - damage: 1d4+6
        - effect: banishing swipe
      attack: tail slap
      bonus:
      - 30
  ranged:
  - - text: glaring ray +23 touch (20d6 fire)
      entries:
      - - damage: 20d6
          type: fire
      attack: glaring ray
      bonus:
      - 23
      touch: true
  special:
  - banishing swipe
  - glaring ray
  - radiant feathers
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: daylight
    source: default
    freq: At will
  - name: zone of truth
    source: default
    freq: At will
    DC: 18
  - name: flame strike
    source: default
    freq: 3/day
    DC: 21
  - name: mass cure critical wounds
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 16
    concentration: 22
ability_scores:
  STR: 34
  DEX: 16
  CON: 27
  INT: 16
  WIS: 19
  CHA: 23
BAB: 24
CMB: 40
CMD: 54
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Hover
- name: Improved Disarm
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Multiattack
- name: Snatch
- name: Wingover
skills:
  Diplomacy: 26
  Fly: 7
  Heal: 14
  Knowledge (arcana): 33
  Knowledge (dungeoneering): 21
  Knowledge (all others): 15
  Perception: 27
  Perform (sing): 19
  Survival: 14
  _racial_mods:
    Knowledge (all):
      _: 10
languages:
- Celestial
- Common
- Draconic
- tongues
ecology:
  environment: warm deserts or mountains
  organization: solitary
  treasure_type: standard
special_abilities:
  Aura of Peace (Su): Creatures within a 50-foot spread from a simurgh feel a sensation
    of peace wash over them, as if affected by calm emotions, except the simurgh can
    choose which creatures are affected. A DC 28 Will save negates the effects of
    this aura for 1 round, but a new save must be made each round to continue to resist
    the effects. The saving throw is Charisma-based.
  Banishing Swipe (Su): A simurgh can use its radiant tail to return creatures to
    their native planes. In addition to taking damage, any extraplanar creature touched
    by a simurgh's tail must succeed at a DC 28 Will save or be affected as if by
    banishment. A creature that makes this save cannot be affected by the same simurgh's
    banishing swipe for the next 24 hours. The save DC is Charisma-based.
  Glaring Ray (Su): A simurgh can blast a fiery ray of brilliant light from its eyes
    as a standard action to a range of 100 feet.
  Radiant Feathers (Su): Once per day as a standard action, a simurgh can fan out
    its glimmering tail feathers and blast its foes with a 100-foot cone of radiant
    light from its tail. Aside from its size, this attack is identical to a prismatic
    spray (DC 28). The save is Charisma-based.
desc_long: Regarded as living legends, simurghs are held in high regard by desert
  dwellers. Those who live in the desert lands where these benevolent creatures sometimes
  reside consider it a lifetime's worth of luck even to spot one soaring through the
  sky. Simurghs prefer to keep to themselves, well out of the way of lesser creatures
  and their often dubious morals, though they can be relied upon for aid when called
  by those in true need and with a pure heart. A simurgh can live for thousands of
  years, and frequent mentions of these giant avian beings throughout a region's historical
  record are more often than not sightings of the same creature.

---

# Simurgh
This massive creature has the body of a resplendent bird but the head of a regal canine.
**Source** Bestiary 3 pg. 245, Pathfinder #24: The Final _[[spells/Wish|Wish]]_ pg. 86
**XP** 153,600

NG Gargantuan magical beast
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +27
**Aura** peace (50 ft.)

##### Defense

**AC** 34, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+3 Dex, +1 dodge, +24 natural, –4 size)
**hp** 324 (24d10+192)
**Fort** +22, **Ref** +17, **Will** +14
**Immune** ability damage, ability drain, disease, fire, negative energy, petrification, poison, sleep; **Resist** acid 10, cold 10, electricity 10; **SR** 29

##### Offense
**Speed** 40 ft., fly 120 ft. (good)
**Melee** bite +32 (2d8+12 plus 2d6 fire), 2 claws +32 (2d8+12 plus 2d6 fire), tail slap +30 (1d4+6 plus banishing _[[spells/Swipe|swipe]]_)
**Ranged** glaring ray +23 touch (20d6 fire)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** banishing _swipe_, glaring ray, _[[items/Armor Magic Abilities/Radiant|radiant]]_ feathers
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +22)
Constant—_detect evil_, _detect magic_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Daylight|daylight]]_, _[[spells/Zone of Truth|zone of truth]]_ (DC 18)
3/day—_[[spells/Flame Strike|flame strike]]_ (DC 21), mass _[[spells/Cure Critical Wounds|cure critical wounds]]_

##### Statistics
**Str** 34, **Dex** 16, **Con** 27, **Int** 16, **Wis** 19, **Cha** 23
**Base Atk** +24; **CMB** +40; **CMD** 54
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Wingover|Wingover]]_
**Skills** Diplomacy +26, Fly +7, _[[spells/Heal|Heal]]_ +14, Knowledge (arcana) +33, Knowledge (dungeoneering) +21, Knowledge (all others) +15, Perception +27, Perform (sing) +19, Survival +14; **Racial Modifiers** +10 Knowledge (all)
**Languages** Celestial, Common, Draconic; _tongues_

##### Ecology

**Environment** warm deserts or mountains
**Organization** solitary
**Treasure** standard

### Special Abilities

**Aura of Peace (Su)** Creatures within a 50-foot spread from a _[[monsters/Simurgh|simurgh]]_ feel a sensation of peace wash over them, as if affected by _[[spells/Calm Emotions|calm emotions]]_, except the _simurgh_ can choose which creatures are affected. A DC 28 Will save negates the effects of this aura for 1 round, but a new save must be made each round to continue to resist the effects. The saving throw is Charisma-based.

**Banishing _Swipe_ (Su)** A _simurgh_ can use its _radiant_ tail to return creatures to their native planes. In addition to taking damage, any extraplanar creature touched by a _simurgh_’s tail must succeed at a DC 28 Will save or be affected as if by _[[spells/Banishment|banishment]]_. A creature that makes this save cannot be affected by the same _simurgh_’s banishing _swipe_ for the next 24 hours. The save DC is Charisma-based.

**Glaring Ray (Su)** A _simurgh_ can blast a fiery ray of brilliant light from its eyes as a standard action to a range of 100 feet.

**_Radiant_ Feathers (Su)** Once per day as a standard action, a _simurgh_ can fan out its glimmering tail feathers and blast its foes with a 100-foot cone of _radiant_ light from its tail. Aside from its size, this attack is identical to a _[[spells/Prismatic Spray|prismatic spray]]_ (DC 28). The save is Charisma-based.

##### Description

Regarded as living legends, simurghs are held in high regard by desert dwellers. Those who live in the desert lands where these _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ creatures sometimes reside consider it a lifetime’s worth of luck even to spot one soaring through the sky. Simurghs prefer to keep to themselves, well out of the way of lesser creatures and their often dubious morals, though they can be relied upon for aid when _[[items/Weapon Magic Abilities/Called|called]]_ by those in true need and with a pure heart. A _simurgh_ can live for thousands of years, and frequent mentions of these giant avian beings throughout a region’s historical record are more often than not sightings of the same creature.