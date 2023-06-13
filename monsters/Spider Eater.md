---
cssclass: [monsters]
title1: Spider Eater
desc_short: This strange beast resembles a wasp the size of a horse, but with the
  head of a spider and two long appendages ending in pincers.
title2: Spider Eater
CR: 5
sources:
- name: Bestiary 3
  page: 255
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1600
alignment: N
size: Large
type: magical beast
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 18
  touch: 12
  flat_footed: 15
  components:
    dex: 2
    dodge: 1
    natural: 6
    size: -1
HP:
  HP: 52
  long: 5d10+25
saves:
  fort: 9
  ref: 6
  will: 2
defensive_abilities:
- freedom of movement
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +9 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 9
    - text: 2 pincers +4 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: pincers
      bonus:
      - 4
    - text: sting +9 (1d6+5 plus poison)
      entries:
      - - damage: 1d6+5
        - effect: poison
      attack: sting
      bonus:
      - 9
  special:
  - implant
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 10
    concentration: 10
ability_scores:
  STR: 21
  DEX: 14
  CON: 21
  INT: 3
  WIS: 12
  CHA: 10
BAB: 5
CMB: 11
CMD: 24
feats:
- name: Dodge
- name: Hover
- name: Skill Focus (Perception)
skills:
  Fly: 8
  Perception: 15
  _racial_mods:
    Perception:
      _: 4
languages:
- Aklo (cannot speak)
ecology:
  environment: temperate forests
  organization: solitary or brood (2-12)
  treasure_type: none
special_abilities:
  Implant (Ex): A spider eaters grows its eggs inside of a living host. Implanting
    an egg in a host is a full-round action that provokes attacks of opportunity,
    and the target must be helpless but alive. Once an egg is implanted, it exudes
    paralytic enzymes that not only keep the victim in state of perpetual paralysis,
    but also keep it nourished and alive in its comatose but fully aware state. This
    condition lasts until the egg hatches in 1d6 weeks, at which point the young spider
    eater consumes most of its host, killing it. An egg can be surgically removed
    with a DC 25 Heal check (this check deals 2d6 points of damage to the host regardless
    of success), at which point the host recovers from the paralysis in 1d6 rounds.
    Any magical effect that removes paralysis or disease (such as remove paralysis,
    remove disease, or heal) also destroys the egg, but mere immunity to paralysis
    or disease does not offer protection.
  Poison (Ex): Sting-injury; save Fort DC 17; frequency 1/minute for 6 minutes; effect
    paralysis for 1 minute; cure 1 save. The save DC is Constitution-based.
desc_long: |-
  An amalgam of dangerous creatures, this predator, as its name suggests, prefers to hunt and feed upon spiders. Their greatest boon to spider hunting, aside from their stinger, ability to fly, and strong pincers, is their ability to slip through the stickiest of webs in order to get to their prey. Unfortunately for other creatures, when a spider eater is denied its preferred prey, it seeks out any living creature it can find to serve as a host for its ravenous young.

  When hunting, a spider eater drops from the air onto its victim, stinging the prey with its barbed tail. The creature then returns to the air and hovers, waiting for its venom to take hold. Once the opponent succumbs to paralysis, the spider eater lands again, either to feed or implant its egg.

  Although more intelligent than the typical beast, to the point where it can understand a language (usually Aklo), the spider eater is relatively slow-witted. Nevertheless, it is intelligent enough that it resists training-those who seek to ally with spider eaters must befriend them via diplomacy and gifts of spiders to feed upon or implant eggs into, or via intimidation and coercion.

  A spider eater measures roughly 14 feet long and stands 6 feet tall. The creature has a wingspan just over 20 feet and weighs almost 2,000 pounds.

---

# Spider Eater
This strange beast resembles a wasp the size of a _[[monsters/Horse|horse]]_, but with the head of a spider and two long appendages ending in pincers.
**Source** Bestiary 3 pg. 255
**XP** 1,600

N Large magical beast
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +15

##### Defense

**AC** 18, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +1 dodge, +6 natural, –1 size)
**hp** 52 (5d10+25)
**Fort** +9, **Ref** +6, **Will** +2
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** bite +9 (1d8+5), 2 pincers +4 (1d6+2), sting +9 (1d6+5 plus poison)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** implant
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +10)
Constant—_freedom of movement_

##### Statistics
**Str** 21, **Dex** 14, **Con** 21, **Int** 3, **Wis** 12, **Cha** 10
**Base Atk** +5; **CMB** +11; **CMD** 24
**Feats** _Dodge_, _[[feats/Hover|Hover]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Fly +8, Perception +15; **Racial Modifiers** +4 Perception
**Languages** Aklo (cannot speak)

##### Ecology

**Environment** temperate forests
**Organization** solitary or brood (2–12)
**Treasure** none

### Special Abilities

**Implant (Ex)** A spider eaters grows its eggs inside of a living host. Implanting an egg in a host is a full-round action that provokes attacks of opportunity, and the target must be _[[conditions/Helpless|helpless]]_ but alive. Once an egg is implanted, it exudes paralytic enzymes that not only keep the victim in state of perpetual _[[universal monster rules/Paralysis|paralysis]]_, but also keep it nourished and alive in its comatose but fully aware state. This condition lasts until the egg hatches in 1d6 weeks, at which point the young _[[monsters/Spider Eater|spider eater]]_ consumes most of its host, killing it. An egg can be surgically removed with a DC 25 _[[spells/Heal|Heal]]_ check (this check deals 2d6 points of damage to the host regardless of success), at which point the host recovers from the _paralysis_ in 1d6 rounds. Any magical effect that removes _paralysis_ or disease (such as _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Remove Disease|remove disease]]_, or _heal_) also destroys the egg, but mere _[[universal monster rules/Immunity|immunity]]_ to _paralysis_ or disease does not offer protection.

**Poison (Ex) **Sting—injury; save Fort DC 17; frequency 1/minute for 6 minutes; effect _paralysis_ for 1 minute; cure 1 save. The save DC is Constitution-based.

##### Description

An amalgam of dangerous creatures, this predator, as its name suggests, prefers to hunt and feed upon spiders. Their greatest boon to spider hunting, aside from their stinger, ability to fly, and strong pincers, is their ability to slip through the stickiest of webs in order to get to their prey. Unfortunately for other creatures, when a _spider eater_ is denied its preferred prey, it seeks out any living creature it can find to serve as a host for its _[[curses/Ravenous|ravenous]]_ young.

When hunting, a _spider eater_ drops from the air onto its victim, stinging the prey with its barbed tail. The creature then returns to the air and hovers, waiting for its venom to take hold. Once the opponent succumbs to _paralysis_, the _spider eater_ lands again, either to feed or implant its egg.

Although more intelligent than the typical beast, to the point where it can understand a language (usually Aklo), the _spider eater_ is relatively slow-witted. Nevertheless, it is intelligent enough that it resists _[[items/Weapon Magic Abilities/Training|training]]_—those who seek to ally with spider eaters must befriend them via diplomacy and gifts of spiders to feed upon or implant eggs into, or via intimidation and coercion.

A _spider eater_ measures roughly 14 feet long and stands 6 feet tall. The creature has a wingspan just over 20 feet and weighs almost 2,000 pounds.