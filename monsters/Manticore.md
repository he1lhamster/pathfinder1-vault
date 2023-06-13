---
cssclass: [monsters]
title1: Manticore
desc_short: This fearsome creature has the body of a lion, the wings of a dragon,
  the face of a snarling man, and a tail of dripping spikes.
title2: Mythic Manticore
CR: 6
MR: 2
sources:
- name: Mythic Adventures
  page: 208
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 2400
alignment: LE
size: Large
type: magical beast
subtypes:
- mythic
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 19
  touch: 11
  flat_footed: 17
  components:
    dex: 2
    natural: 8
    size: -1
HP:
  HP: 77
  long: 6d10+44
saves:
  fort: 9
  ref: 7
  will: 3
DR:
- amount: 5
  weakness: epic
speeds:
  base: 30
  fly: 50
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +11 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 11
    - text: 2 claws +11 (2d4+6)
      entries:
      - - damage: 2d4+6
      count: 2
      attack: claws
      bonus:
      - 11
  ranged:
  - - text: 4 spikes +9 (1d6+6 plus poison)
      entries:
      - - damage: 1d6+6
        - effect: poison
      count: 4
      attack: spikes
      bonus:
      - 9
  special:
  - mythic power (2/day, surge +1d6)
  - poison
  - pounce
  - skewer
space: 10
reach: 5
ability_scores:
  STR: 22
  DEX: 15
  CON: 18
  INT: 7
  WIS: 12
  CHA: 9
BAB: 6
CMB: 13
CMD: 25
CMD_other: 29 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- is_mythic: true
  name: Weapon Focus (spikes)
skills:
  Fly: -3
  Perception: 9
  Survival: 4
    when tracking: 8
  _racial_mods:
    Perception:
      _: 4
    Survival:
      when tracking: 4
languages:
- Common
ecology:
  environment: warm hills and marshes
  organization: solitary, pair, or pride (3-6)
  treasure_type: standard
special_abilities:
  Poison (Ex): Spike-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d4 Str; cure 2 consecutive saves.
  Skewer (Ex): If a mythic manticore confirms a critical hit with a spike, the spike
    pins the target to the ground or a nearby surface. If the target is using winged
    flight, the spike snares its wings. The target is considered grappled by the manticore
    (though the manticore is not considered to be grappling) and must escape the grapple
    to move from its square. A flying creature must escape on its turn or plummet
    to the ground. As a swift action, a mythic manticore can expend one use of mythic
    power to skewer all targets hit by its spikes that turn, even if the attacks weren't
    critical hits.
  Spikes (Ex): With a snap of its tail, a mythic manticore can loose a volley of four
    spikes as a standard action (make an attack roll for each spike). This attack
    has a range of 180 feet with no range increment. All targets must be within 30
    feet of each other. The creature can launch only 24 spikes in any 24-hour period.
desc_long: |-
  A mythic manticore is a nightmarish creature, perhaps the result of crossbreeding with poisonous drakes, decadent sphinxes, or aberrant chimeras. A voracious eater, a mythic manticore may devour an entire corpse, as well as its weapons and armor, leaving nothing but a bloody stain on the ground and a few organs it finds unpalatable. Any metal bits it eats are digested and used to grow its deadly spikes. Some are known to dine on giant venomous snakes and spiders with the intent of making their poison even more powerful.

  A mythic manticore uses its thrown spikes to hold prey in place from a distance so it can leap upon it and tear it apart. It is especially fond of skewering the wings of a flying creature, forcing it to plummet to the ground where it becomes easy pickings. Its weakness-inducing poison makes it especially dangerous to winged mounts, as the poisoned creature may find itself unable to carry a rider.

---

# Manticore
This creature has a vaguely humanoid head, the body of a _[[monsters/Lion|lion]]_, and the wings of a dragon. Its tail ends in long, sharp spikes.
**Source** Pathfinder RPG Bestiary pg. 199
**XP** 1,600

LE Large magical beast
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +9

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +6 natural, –1 size)
**hp** 57 (6d10+24)
**Fort** +9, **Ref** +7, **Will** +3

##### Offense
**Speed** 30 ft., fly 50 ft. (clumsy)
**Melee** bite +10 (1d8+5), 2 claws +10 (2d4+5)
**Ranged** 4 spikes +8 (1d6+5)
**Space** 10 ft., **Reach** 5 ft.

##### Statistics
**Str** 20, **Dex** 15, **Con** 18, **Int** 7, **Wis** 12, **Cha** 9
**Base Atk** +6; **CMB** +12; **CMD** 24 (28 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (spikes)
**Skills** Fly –3, Perception +9, Survival +4 (+8 tracking); **Racial Modifiers** +4 Perception, +4 Survival when tracking
**Languages** Common

##### Ecology

**Environment** warm hills and marshes
**Organization** solitary, pair, or pride (3–6)
**Treasure** standard

### Special Abilities
**Spikes (Ex)** With a snap of its tail, a _[[monsters/Manticore|manticore]]_ can loose a volley of four spikes as a standard action (make an attack roll for each spike). This attack has a range of 180 feet with no range increment. All targets must be within 30 feet of each other. The creature can launch only 24 spikes in any 24-hour period.

##### Description

Manticores are fierce predators that patrol a wide area in search of fresh meat. A typical _manticore_ is about 10 feet long and weighs about 1,000 pounds. Some have more human-like heads, usually with beards. Males and females look much alike.

Manticores eat any meat, even carrion, though they prefer human flesh and rarely pass up an opportunity for such a delicacy. They are smart and social enough to bargain with or bully evil humanoids into alliances or offering tribute, and more powerful creatures may hire or bribe them to _[[npcs/Guard|guard]]_ or patrol a place or area. They like lairs in high places, such as hilltops and caves in cliffs.

Although manticores were likely a magical creation, they have long since established themselves as a naturally occurring species. Curiously, manticores seem strangely fecund, and can interbreed with a number of other similarly shaped creatures, including lions, dire lions, lamias, sphinxes, and even chimeras. The progeny of a _manticore_ and an unusual mate is summarized on the table below.

**_Manticore_’s Mate** **Offspring** LionStandard _manticore_ Dire lionAdvanced _manticore_ LamiaLamia with spiked tail and spikes special attack SphinxSphinx with spiked tail and spikes special attack ChimeraChimera with spiked tail and spikes special attack