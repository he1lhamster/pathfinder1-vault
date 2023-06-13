---
cssclass: [monsters]
title1: Kaiju, Bezravnis
desc_short: The armored plates of this immense, three-tailed scorpion are fiery red,
  and its stingers glow with molten heat.
title2: Bezravnis
CR: 26
sources:
- name: Bestiary 4
  page: 168
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 2457600
alignment: CN
size: Colossal
type: magical beast
subtypes:
- earth
- kaiju
initiative:
  bonus: 9
senses:
  darkvision: 600
  low-light vision: true
  tremorsense: 600
AC:
  AC: 44
  touch: 7
  flat_footed: 39
  components:
    dex: 5
    natural: 37
    size: -8
HP:
  HP: 615
  long: 30d10+450
  fast_healing: 30
saves:
  fort: 32
  ref: 24
  will: 20
defensive_abilities:
- ferocity
- recovery
DR:
- amount: 20
  weakness: epic
immunities:
- ability damage
- ability drain
- death effects
- disease
- energy drain
- fear
- fire
resistances:
  acid: 30
  cold: 30
  electricity: 30
  negative energy: 30
  sonic: 30
speeds:
  base: 100
  burrow: 100
attacks:
  melee:
  - - text: 2 claws +40 (4d6+18/19-20 plus grab)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 40
    - text: 3 stings +40 (3d6+18/19-20 plus 2d6 fire and poison)
      entries:
      - - damage: 3d6+18
          crit_range: 19-20
        - damage: 2d6
          type: fire
        - effect: poison
      count: 3
      attack: stings
      bonus:
      - 40
  special:
  - burrowing charge
  - constrict (4d6+27)
  - heat beam
  - hurl foe
  - poison
  - trample (2d8+27, DC 43)
  - web (+27 ranged, DC 40, 30 hp)
space: 50
reach: 50
ability_scores:
  STR: 47
  DEX: 20
  CON: 40
  INT: 3
  WIS: 26
  CHA: 23
BAB: 30
CMB: 56
CMB_other: +60 bull rush, +60 grapple
CMD: 71
CMD_other: 73 vs. bull rush, 83 vs. trip
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
skills:
  Climb: 31
  Perception: 37
  Stealth: 2
    when burrowing: 32
  _racial_mods:
    Perception:
      _: 16
    Stealth:
      when burrowing: 30
languages:
- Terran (can't speak)
special_qualities:
- massive
- no breath
ecology:
  environment: warm deserts
  organization: solitary (unique)
  treasure_type: incidental
special_abilities:
  Burrowing Charge (Ex): Once per minute, Bezravnis can make a charge attack while
    burrowing through loose earth, sand, mud, or magma, or through any other loosely
    packed earth or stone. When Bezaravnis reaches the target, it erupts from the
    ground as part of its attack. If Bezravnis hits the target of its burrowing charge
    attack, it deals double damage with its attack. Any creatures standing in or flying
    less than 50 feet above the space Bezravnis occupies at the end of this charge
    are immediately subjected to Bezravnis's trample attack. Any buildings entirely
    within this space take double damage from the trample attack (4d8+54 points)-this
    damage bypasses hardness. In addition, Huge or smaller creatures must succeed
    at a DC 40 Reflex save or be buried in earth, as if by a cave-in or collapse.
    This bury zone extends into all squares affected by Bezravnis's reach.
  Heat Beam (Su): Once every 4 rounds, Bezravnis can fire beams of searing heat and
    fire from one of its three stingers. Each stinger's heat beam is a separate attack
    with its own 4-round recharge period. The kaiju may fire one heat beam from a
    stinger as a move action, two heat beams as a standard action, or all three as
    a full-round action. Each heat beam is a 1,200-foot-long line that deals 20d6
    points of fire damage to everything in its path (Reflex DC 40 half). If Bezravnis
    fires more than one heat beam, it can direct them in different directions. The
    save DC is Constitution-based.
  Poison (Su): Sting-injury; save Fort DC 40; frequency 1/round for 6 rounds; effect
    staggered for 1 round plus loss of fire immunity and resistance; cure 3 consecutive
    saves. As long as a creature suffers the effects of Bezravnis's poison, it loses
    all racial resistances and immunities to fire. Any spell or spell-like effects
    active when the target fails its initial saving throw against this poison are
    suppressed as long as it continues to be staggered by the poison. New effects
    of this nature that become active after that initial failed saving throw function
    normally if the caster succeeds at a DC 35 caster level check; otherwise, the
    spell effects are suppressed until the victim is no longer staggered.
  Web (Ex): Bezravnis's webs are immune to fire damage. In addition, these webs are
    semi-living things that continue to crush and squeeze those entangled by them.
    If a creature is entangled in the webs, at the start of each turn during which
    it is entangled, it takes 2d6+6 points of bludgeoning damage as the webs crush
    and constrict it. This ability otherwise functions the same as the universal monster
    ability.
desc_long: |-
  Bezravnis, known also as the Inferno Below, dwells in the sands of a sparsely inhabited high-altitude desert found in the shadow of the world's largest mountain range. There, the 130-foot-long beast slumbers the centuries away until its cycle of wakefulness rouses it from its torpor and causes it to emerge from the sands in an eruption of fire and ash. The Inferno Below then begins its rampage, traveling in a straight line toward a heavily populated region bordering the great desert. Typically, the Inferno Below's rampage is limited to a single city, and never the same one twice in a row. After destroying no less than two-thirds of the city, it retreats back to the vast desert, burrows deep, and settles into a new sleep of ages.

  The reason for the Inferno Below's cyclic rampages is not well understood, but the cycle of these rampages functions like clockwork-they take place every 273 years with little deviation. As there seems to be no pattern to the kaiju's attacks themselves, with a different city being targeted each cycle, the cities of the bordering nations do their best to prepare for the monster's attack. The nations themselves have little love for each other, and attempts to generate lures to direct the kaiju's march toward an enemy city are common-yet these lures have yet to work, and in fact they seem to result in the kaiju attacking a city in the luring nation more often than not. Other cities spare no expense during a so-called “Inferno Season,” and send huge armies of scouts into the desert to watch for signs of the kaiju's emergence or traces of its burrowing passage through the sands, in hopes of determining the direction of the beast's travel and warning likely target cities (or, in the case of a trajectory that leads it to an enemy city, working to silence warnings).

  Kaiju scholars have correlated Bezravnis's appearance with the passage of a singular red comet in the skies above the world-an astronomical event known as the Inferno Star. As the comet nears the world, Bezravnis emerges, and as the comet vanishes from the sky, the kaiju turns its back and returns to the desert. Confirmation of this correlation has given rise to numerous theories. Some believe that Bezravnis first fell to the world from the Inferno Star, and its advent wakens within the beast a bewildered longing for home that drives it into a frenzy. Others hold that the kaiju exists as a guardian against an even more deadly occupant of the Inferno Star, and that by displaying its power by destroying a city, Bezravnis is in fact protecting the world by driving the Inferno Star back into the depths of space.

  But Bezravnis doesn't always have the luxury of waiting for the Inferno Star to draw near before waking. At several points in the past, lunatics, cults, and accidents have woken the kaiju before its appointed time. Some mad, apocalyptic-minded spellcasters use powerful magic to cause great explosions above the sands where the kaiju slumbers. Earthquakes, severe weather phenomena, and similar natural events have been known to waken the monster early as well. When Bezravnis wakens off-cycle like this, the monster is particularly foul-tempered. It's rampage does not follow a straight line-instead, its travels are erratic as it pursues the perceived cause of its wakening with single-minded ferocity and tenacity. In this way, cults have accomplished what the border nations have not-leading the kaiju to attack an enemy. Of course, such tactics are dangerous and often backfire, for Bezravnis is fast and destructive, and it has been known to follow such tormenters.

  Bezravnis doesn't seem to be particularly vexed by the presence of other kaiju, and ignores them unless it is attacked first. Once attacked, however, the Inferno Below becomes singularly focused and deviates from its path to fight the target creature as long as it remains visible or alive. Smaller foes can sometimes distract the kaiju from its path in this manner if they can deal enough damage upon the creature to bait it into directing its furious rage on them.

---

# Kaiju, Bezravnis
The armored plates of this immense, three-tailed scorpion are fiery red, and its stingers glow with molten _[[universal monster rules/Heat|heat]]_.
**Source** Bestiary 4 pg. 168
**XP** 2,457,600

CN Colossal magical beast (earth, kaiju)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 600 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 600 ft.; Perception +37

##### Defense

**AC** 44, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 39 (+5 Dex, +37 natural, –8 size)
**hp** 615 (30d10+450); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +32, **Ref** +24, **Will** +20
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_, recovery; **DR** 20/epic; **Immune** ability damage, ability drain, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_, fire; **Resist** acid 30, cold 30, electricity 30, negative energy 30, sonic 30

##### Offense
**Speed** 100 ft., _[[universal monster rules/Burrow|burrow]]_ 100 ft.
**Melee** 2 claws +40 (4d6+18/19–20 plus _[[universal monster rules/Grab|grab]]_), 3 stings +40 (3d6+18/19–20 plus 2d6 fire and poison)
**Space** 50 ft., **Reach** 50 ft.
**Special Attacks** burrowing charge, _[[universal monster rules/Constrict|constrict]]_ (4d6+27), _heat_ beam, hurl foe, poison, _[[universal monster rules/Trample|trample]]_ (2d8+27, DC 43), web (+27 ranged, DC 40, 30 hp)

##### Statistics
**Str** 47, **Dex** 20, **Con** 40, **Int** 3, **Wis** 26, **Cha** 23
**Base Atk** +30; **CMB** +56 (+60 bull rush, +60 grapple); **CMD** 71 (73 vs. bull rush, 83 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _Improved Critical_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +31, Perception +37, Stealth +2 (+32 when burrowing); **Racial Modifiers** +16 Perception, +30 Stealth when burrowing
**Languages** Terran (can’t speak)
**SQ** massive, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** warm deserts
**Organization** solitary (unique)
**Treasure** incidental

### Special Abilities

**Burrowing Charge (Ex)** Once per minute, Bezravnis can make a charge attack while burrowing through loose earth, sand, mud, or magma, or through any other loosely packed earth or stone. When Bezaravnis reaches the target, it erupts from the ground as part of its attack. If Bezravnis hits the target of its burrowing charge attack, it deals double damage with its attack. Any creatures standing in or flying less than 50 feet above the space Bezravnis occupies at the end of this charge are immediately subjected to Bezravnis’s _trample_ attack. Any buildings entirely within this space take double damage from the _trample_ attack (4d8+54 points)—this damage bypasses hardness. In addition, Huge or smaller creatures must succeed at a DC 40 Reflex save or be buried in earth, as if by a cave-in or collapse. This bury zone extends into all squares affected by Bezravnis’s reach.

**_Heat_ Beam (Su)** Once every 4 rounds, Bezravnis can fire beams of searing _heat_ and fire from one of its three stingers. Each stinger’s _heat_ beam is a separate attack with its own 4-round _[[spells/Recharge|recharge]]_ period. The kaiju may fire one _heat_ beam from a stinger as a move action, two _heat_ beams as a standard action, or all three as a full-round action. Each _heat_ beam is a 1,200-foot-long line that deals 20d6 points of fire damage to everything in its path (Reflex DC 40 half). If Bezravnis fires more than one _heat_ beam, it can direct them in different directions. The save DC is Constitution-based.

**Poison (Su)** Sting—injury; save Fort DC 40; frequency 1/round for 6 rounds; effect _[[conditions/Staggered|staggered]]_ for 1 round plus loss of fire _[[universal monster rules/Immunity|immunity]]_ and _[[universal monster rules/Resistance|resistance]]_; cure 3 consecutive saves. As long as a creature suffers the effects of Bezravnis’s poison, it loses all racial resistances and immunities to fire. Any spell or spell-like effects active when the target fails its initial saving throw against this poison are suppressed as long as it continues to be _staggered_ by the poison. New effects of this nature that become active after that initial failed saving throw function normally if the caster succeeds at a DC 35 caster level check; otherwise, the spell effects are suppressed until the victim is no longer _staggered_.

**Web (Ex)** Bezravnis’s webs are immune to fire damage. In addition, these webs are semi-living things that continue to crush and _[[spells/Squeeze|squeeze]]_ those _[[conditions/Entangled|entangled]]_ by them. If a creature is _entangled_ in the webs, at the start of each turn during which it is _entangled_, it takes 2d6+6 points of bludgeoning damage as the webs crush and _constrict_ it. This ability otherwise functions the same as the universal monster ability.

##### Description

Bezravnis, known also as the Inferno Below, dwells in the sands of a sparsely inhabited high-altitude desert found in the _[[items/Armor Magic Abilities/Shadow|shadow]]_ of the world’s largest mountain range. There, the 130-foot-long beast slumbers the centuries away until its cycle of wakefulness rouses it from its torpor and causes it to emerge from the sands in an eruption of fire and ash. The Inferno Below then begins its rampage, traveling in a straight line toward a heavily populated region bordering the great desert. Typically, the Inferno Below’s rampage is limited to a single city, and never the same one twice in a row. After destroying no less than two-thirds of the city, it retreats back to the vast desert, burrows deep, and settles into a new sleep of ages.

The reason for the Inferno Below’s cyclic rampages is not well understood, but the cycle of these rampages functions like clockwork—they take place every 273 years with little deviation. As there seems to be no pattern to the kaiju’s attacks themselves, with a different city being targeted each cycle, the cities of the bordering nations do their best to prepare for the monster’s attack. The nations themselves have little love for each other, and attempts to generate lures to direct the kaiju’s march toward an enemy city are common—yet these lures have yet to work, and in fact they seem to result in the kaiju attacking a city in the luring nation more often than not. Other cities spare no expense during a so-called “Inferno Season,” and send huge armies of scouts into the desert to watch for signs of the kaiju’s emergence or traces of its burrowing passage through the sands, in hopes of determining the direction of the beast’s travel and warning likely target cities (or, in the case of a trajectory that leads it to an enemy city, working to _[[spells/Silence|silence]]_ warnings).

Kaiju scholars have correlated Bezravnis’s appearance with the passage of a singular red comet in the skies above the world—an astronomical event known as the Inferno Star. As the comet nears the world, Bezravnis emerges, and as the comet vanishes from the sky, the kaiju turns its back and returns to the desert. Confirmation of this correlation has given rise to numerous theories. Some believe that Bezravnis first fell to the world from the Inferno Star, and its advent wakens within the beast a bewildered longing for home that drives it into a frenzy. Others hold that the kaiju exists as a _[[items/Weapon Magic Abilities/Guardian|guardian]]_ against an even more _[[items/Weapon Magic Abilities/Deadly|deadly]]_ occupant of the Inferno Star, and that by displaying its power by destroying a city, Bezravnis is in fact protecting the world by driving the Inferno Star back into the depths of space.

But Bezravnis doesn’t always have the luxury of waiting for the Inferno Star to draw near before waking. At several points in the past, lunatics, cults, and accidents have woken the kaiju before its appointed time. Some mad, apocalyptic-minded spellcasters use powerful magic to cause great explosions above the sands where the kaiju slumbers. Earthquakes, severe weather phenomena, and similar natural events have been known to waken the monster early as well. When Bezravnis wakens off-cycle like this, the monster is particularly foul-tempered. It’s rampage does not follow a straight line—instead, its travels are erratic as it pursues the perceived cause of its wakening with single-minded _ferocity_ and tenacity. In this way, cults have accomplished what the border nations have not—leading the kaiju to attack an enemy. Of course, such tactics are dangerous and often backfire, for Bezravnis is fast and destructive, and it has been known to follow such tormenters.

Bezravnis doesn’t seem to be particularly vexed by the presence of other kaiju, and ignores them unless it is attacked first. Once attacked, however, the Inferno Below becomes singularly focused and deviates from its path to fight the target creature as long as it remains visible or alive. Smaller foes can sometimes distract the kaiju from its path in this manner if they can deal enough damage upon the creature to bait it into directing its _[[items/Weapon Magic Abilities/Furious|furious]]_ _[[spells/Rage|rage]]_ on them.