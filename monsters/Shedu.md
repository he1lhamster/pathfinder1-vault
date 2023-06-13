---
cssclass: [monsters]
title1: Shedu
desc_short: This noble creature stands strong and tall with the body of a powerful
  bull and the head of a wise-looking human.
title2: Shedu
CR: 9
sources:
- name: Bestiary 3
  page: 2543
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 6400
alignment: LG
size: Large
type: magical beast
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect chaos: true
  detect evil: true
  low-light vision: true
  true seeing: true
AC:
  AC: 24
  touch: 16
  flat_footed: 23
  components:
    dex: 1
    insight: 6
    natural: 8
    size: -1
HP:
  HP: 115
  long: 11d10+55
  fast_healing: 5
saves:
  fort: 12
  ref: 14
  will: 11
defensive_abilities:
- prescience
DR:
- amount: 10
  weakness: evil
resistances:
  electricity: 10
  fire: 10
SR: 20
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: gore +17 (2d8+7/19-20)
      entries:
      - - damage: 2d8+7
          crit_range: 19-20
      attack: gore
      bonus:
      - 17
    - text: 2 hooves +12 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: hooves
      bonus:
      - 12
    - text: 2 wings +12 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: wings
      bonus:
      - 12
  special:
  - trample (2d6+10, DC 22)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: empowered cure moderate wounds
    source: default
    freq: 3/day
  - name: dispel magic
    source: default
    freq: 3/day
  - name: magic circle against evil
    source: default
    freq: 3/day
  - name: remove disease
    source: default
    freq: 3/day
  - name: shield other
    source: default
    freq: 3/day
  - name: dismissal
    source: default
    freq: 1/day
    DC: 19
  - name: flame strike
    source: default
    freq: 1/day
    DC: 19
  - name: restoration
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 24
  DEX: 13
  CON: 20
  INT: 19
  WIS: 22
  CHA: 19
BAB: 11
CMB: 19
CMB_other: +23 bull rush
CMD: 36
CMD_other: 38 vs. bull rush, 40 vs. trip
feats:
- name: Empower Spell-Like Ability (cure moderate wounds)
- name: Greater Bull Rush
- name: Improved Bull Rush
- name: Improved Critical (gore)
- name: Iron Will
- name: Power Attack
skills:
  Diplomacy: 15
  Fly: 17
  Knowledge (planes): 15
  Knowledge (religion): 15
  Perception: 20
  Sense Motive: 17
languages:
- Auran
- Celestial
- Common
- telepathy 100 ft.
ecology:
  environment: warm deserts
  organization: solitary
  treasure_type: standard
special_abilities:
  Prescience (Su): A shedu can see all the possible outcomes of any of its own futures.
    This grants the creature an insight bonus to its AC and on initiative checks and
    Reflex saves equal to its Wisdom bonus (+6 for most shedus).
desc_long: |-
  Shedus live far from the hustle and bustle of humanity in harsh deserts. There they populate caves, ruins, or ancient temples reclaimed from the shifting sands. In these places of refuge, shedus contemplate the struggle between good and evil throughout the universe. Tireless vehicles of good and kindness, shedus fight against outsiders who corrupt and threaten humanity. Skilled in healing, shedus focus on eliminating plagues, even hunting down outsiders and undead working in that destructive medium.

  Shedus rarely make their homes near each other. This is not out of any sort of animosity, but rather from a feeling that having two or more shedus within close proximity wastes the opportunity to provide aid to a larger region. When a shedu roams through the lands of another, it always seeks out the local shedu for an opportunity to talk and share knowledge over the course of 3 days. After this period, the visiting shedu departs with a new perspective and more points to ponder in its eternal struggle against the evils of the world.

---

# Shedu
This noble creature stands strong and tall with the body of a powerful bull and the head of a wise-looking human.
**Source** Bestiary 3 pg. 2543
**XP** 6,400

LG Large magical beast
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +20

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+1 Dex, +6 insight, +8 natural, –1 size)
**hp** 115 (11d10+55); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +12, **Ref** +14, **Will** +11
**Defensive Abilities** prescience; **DR** 10/evil; **Resist** electricity 10, fire 10; **SR** 20

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** gore +17 (2d8+7/19–20), 2 hooves +12 (1d6+3), 2 wings +12 (1d6+3)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Trample|trample]]_ (2d6+10, DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant— _detect chaos_, _detect evil_, _true seeing_
3/day—empowered _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Shield Other|shield other]]_
1/day—_[[spells/Dismissal|dismissal]]_ (DC 19), _[[spells/Flame Strike|flame strike]]_ (DC 19), _[[spells/Restoration|restoration]]_

##### Statistics
**Str** 24, **Dex** 13, **Con** 20, **Int** 19, **Wis** 22, **Cha** 19
**Base Atk** +11; **CMB** +19 (+23 bull rush); **CMD** 36 (38 vs. bull rush, 40 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_cure moderate wounds_), _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (gore), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Diplomacy +15, Fly +17, Knowledge (planes) +15, Knowledge (religion) +15, Perception +20, Sense Motive +17
**Languages** Auran, Celestial, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** warm deserts
**Organization** solitary
**Treasure** standard

### Special Abilities

**Prescience (Su)** A _[[monsters/Shedu|shedu]]_ can see all the possible outcomes of any of its own futures. This grants the creature an insight bonus to its AC and on initiative checks and Reflex saves equal to its Wisdom bonus (+6 for most shedus).

##### Description

Shedus live far from the hustle and bustle of humanity in harsh deserts. There they populate caves, ruins, or ancient temples reclaimed from the shifting sands. In these places of _[[spells/Refuge|refuge]]_, shedus contemplate the struggle between good and evil throughout the universe. Tireless vehicles of good and kindness, shedus fight against outsiders who corrupt and threaten humanity. Skilled in healing, shedus focus on eliminating plagues, even hunting down outsiders and undead working in that destructive medium.

Shedus rarely make their homes near each other. This is not out of any sort of animosity, but rather from a feeling that having two or more shedus within close proximity wastes the opportunity to provide aid to a larger region. When a _shedu_ roams through the lands of another, it always seeks out the local _shedu_ for an opportunity to talk and share knowledge over the course of 3 days. After this period, the visiting _shedu_ departs with a new perspective and more points to ponder in its eternal struggle against the evils of the world.