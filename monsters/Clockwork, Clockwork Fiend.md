---
cssclass: [monsters]
title1: Clockwork, Clockwork Fiend
desc_short: Resembling a metallic horned devil, this apparatus whirs with the sound
  of internal mechanisms.
title2: Clockwork Fiend
CR: 17
sources:
- name: Bestiary 6
  page: 60
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 102400
alignment: N
size: Medium
type: construct
subtypes:
- clockwork
initiative:
  bonus: 12
senses:
  darkvision: 60
  low-light vision: true
  see in darkness: true
AC:
  AC: 32
  touch: 20
  flat_footed: 22
  components:
    dex: 8
    dodge: 2
    natural: 12
HP:
  HP: 146
  long: 23d10+20
saves:
  fort: 7
  ref: 17
  will: 7
DR:
- amount: 15
  weakness: adamantine
immunities:
- construct traits
- fire
weaknesses:
- vulnerable to electricity
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +34 (2d8+11/18-20/×3)
      entries:
      - - damage: 2d8+11
          crit_range: 18-20
          crit_multiplier: 3
      attack: bite
      bonus:
      - 34
    - text: 2 claws +34 (2d6+11 plus bleed)
      entries:
      - - damage: 2d6+11
        - effect: bleed
      count: 2
      attack: claws
      bonus:
      - 34
    - text: 2 wings +29 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 29
  special:
  - bleed (2d8)
  - explosive rend
  - overdrive
space: 5
reach: 5
reach_other: 10 ft. with wings
ability_scores:
  STR: 32
  DEX: 26
  CON:
  INT:
  WIS: 11
  CHA: 1
BAB: 23
CMB: 34
CMD: 54
feats:
- name: Improved Initiative
- name: Lightning Reflexes
skills: {}
special_qualities:
- difficult to create
- swift reactions
- winding
ecology:
  environment: any
  organization: solitary, pair, or blasphemy (2 clockwork fiends plus 4-8 clockwork
    angels)
  treasure_type: none
special_abilities:
  Explosive Rend (Su): When a clockwork fiend makes two successful claw attacks against
    the same target in 1 round, its claws ignite into an explosive blast of fire.
    The target of the attack and all creatures within a 5-foot radius of the clockwork
    fiend take 10d6 points of fire damage. A successful DC 21 Reflex save halves this
    damage. The save DC is Constitution-based.
  Overdrive (Su): Once per day when a clockwork fiend is reduced below 100 hit points,
    its internal systems significantly augment the construct. Entering overdrive drastically
    reduces the clockwork fiend's remaining winding time, and as a result, the clockwork
    fiend can operate for only 2d4+10 rounds before it ceases to function and requires
    further winding. Once overdrive is triggered, the clockwork fiend immediately
    gains the following effects for as long as it remains functional. • Gains 100
    temporary hit points. These hit points last until the clockwork fiend ceases functioning
    or is rewound. • Gains an aura of fire. All creatures within 10 feet take 2d6
    points of fire damage at the beginning of the clockwork fiend's turn. • Makes
    all attacks as if using Power Attack (-6 on attack rolls, +12 points of damage
    on all natural attacks).
  Savage Bite (Ex): A clockwork fiend's bite threatens a critical hit on a roll of
    18-20 and deals triple damage on a successful critical hit.
desc_long: Clockwork fiends often guard religious sites, but their tactics focus on
  an overwhelmingly strong offensive.

---

# Clockwork, Clockwork Fiend
Resembling a metallic horned devil, this apparatus whirs with the sound of internal mechanisms.
**Source** Bestiary 6 pg. 60
**XP** 102,400

N Medium construct (clockwork)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +0

##### Defense

**AC** 32, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+8 Dex, +2 _[[feats/Dodge|dodge]]_, +12 natural)
**hp** 146 (23d10+20)
**Fort** +7, **Ref** +17, **Will** +7
**DR** 15/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, fire
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 30 ft.
**Melee** bite +34 (2d8+11/18–20/×3), 2 claws +34 (2d6+11 plus _[[universal monster rules/Bleed|bleed]]_), 2 wings +29 (1d8+5)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with wings)
**Special Attacks** _bleed_ (2d8), explosive _[[universal monster rules/Rend|rend]]_, overdrive

##### Statistics
**Str** 32, **Dex** 26, **Con** —, **Int** —, **Wis** 11, **Cha** 1
**Base Atk** +23; **CMB** +34; **CMD** 54
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**SQ** difficult to create, swift reactions, winding

##### Ecology

**Environment** any
**Organization** solitary, pair, or _[[spells/Blasphemy|blasphemy]]_ (2 clockwork fiends plus 4–8 clockwork angels)
**Treasure** none

### Special Abilities

**Explosive _Rend_ (Su)** When a clockwork fiend makes two successful claw attacks against the same target in 1 round, its claws ignite into an explosive blast of fire. The target of the attack and all creatures within a 5-foot radius of the clockwork fiend take 10d6 points of fire damage. A successful DC 21 Reflex save halves this damage. The save DC is Constitution-based.

**Overdrive (Su)** Once per day when a clockwork fiend is reduced below 100 hit points, its internal systems significantly augment the construct. Entering overdrive drastically reduces the clockwork fiend’s remaining winding time, and as a result, the clockwork fiend can operate for only 2d4+10 rounds before it ceases to function and requires further winding. Once overdrive is triggered, the clockwork fiend immediately gains the following effects for as long as it remains functional.

* • Gains 100 temporary hit points. These hit points last until the clockwork fiend ceases functioning or is rewound. 
* • Gains an aura of fire. All creatures within 10 feet take 2d6 points of fire damage at the beginning of the clockwork fiend’s turn. 
* • Makes all attacks as if using _[[feats/Power Attack|Power Attack]]_ (–6 on attack rolls, +12 points of damage on all _[[universal monster rules/Natural Attacks|natural attacks]]_).
**Savage Bite (Ex)** A clockwork fiend’s bite threatens a critical hit on a roll of 18–20 and deals triple damage on a successful critical hit.

##### Description

Clockwork fiends often _[[npcs/Guard|guard]]_ religious sites, but their tactics focus on an overwhelmingly strong offensive.