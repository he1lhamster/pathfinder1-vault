---
cssclass: [monsters]
title1: Quickwood
desc_short: Were it not for the image of a sinister face peeking out from its dark
  gray bark, this would look like any other ragged oak tree.
title2: Quickwood
CR: 8
sources:
- name: Bestiary 2
  page: 228
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 4800
alignment: N
size: Huge
type: plant
initiative:
  bonus: 3
senses:
  darkvision: 120
  low-light vision: true
  oaksight: true
auras:
- name: fear aura
  other:
  - variable distance
  DC: 20
AC:
  AC: 19
  touch: 7
  flat_footed: 19
  components:
    dex: -1
    natural: 12
    size: -2
HP:
  HP: 95
  long: 10d8+50
saves:
  fort: 12
  ref: 2
  will: 5
defensive_abilities:
- spell absorption
immunities:
- electricity
- fire
- plant traits
SR: 19 (see spell absorption)
speeds:
  base: 10
attacks:
  melee:
  - - text: bite +14 (2d6+9)
      entries:
      - - damage: 2d6+9
      attack: bite
      bonus:
      - 14
    - text: 3 roots +12 (1d6+4 plus pull)
      entries:
      - - damage: 1d6+4
        - effect: pull
      count: 3
      attack: roots
      bonus:
      - 12
  special:
  - pull (root, 10 ft.)
space: 5
reach: 15
reach_other: 60 ft. with root
ability_scores:
  STR: 29
  DEX: 8
  CON: 21
  INT: 12
  WIS: 15
  CHA: 12
BAB: 7
CMB: 18
CMD: 27
CMD_other: can't be tripped
feats:
- name: Improved Initiative
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Perception)
skills:
  Knowledge (nature): 11
  Perception: 21
  Stealth: 4
    in forests: 8
  _racial_mods:
    Stealth:
      in forests: 4
languages:
- Common
- Sylvan
ecology:
  environment: temperate forests
  organization: solitary
  treasure_type: standard
special_abilities:
  Fear Aura (Su): A quickwood with stored magical energy can activate its fear aura
    as a standard action. The aura has a radius of 10 feet per spell level of the
    effect and lasts for 1 round (Will DC 20 negates). Creatures that fail their saving
    throws become panicked for 1 minute. The DC is Charisma-based and includes a +4
    racial bonus.
  Oaksight (Su): A quickwood may observe the area surrounding any oak tree within
    360 feet as if using clairaudience/clairvoyance. It can use this ability on any
    number of oak trees in the area. Although the quickwood does not need line of
    sight to establish this link, if it does have line of sight to even a single oak
    tree, it cannot be flanked.
  Roots (Ex): A quickwood has dozens of long roots, but can only attack with up to
    three of them in any given round. If the quickwood uses its pull ability to pull
    a target within reach of its bite attack, it can immediately make a free bite
    attack with a +4 bonus on its attack roll against that target.
  Spell Absorption (Su): If a quickwood's spell resistance protects it from a magical
    effect, the creature absorbs that magical energy into its body. It can release
    this energy to activate its fear aura ability. While the plant is storing a spell,
    its SR decreases by 5. It can only store one spell at a time.
desc_long: These carnivorous plants prize human and elven flesh, but eat anything
  they manage to catch. Quickwoods typically explore an area, taking note of any oak
  trees, and then root themselves and wait for prey to wander by. They use their oaksight
  ability to maintain constant surveillance of their hunting grounds and send their
  roots out to drag likely prey back to them.

---

# Quickwood
Were it not for the image of a sinister face peeking out from its dark _[[monsters/Gray|gray]]_ bark, this would look like any other ragged oak tree.
**Source** Bestiary 2 pg. 228
**XP** 4,800

N Huge plant
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, oaksight; Perception +21
**Aura** _[[universal monster rules/Fear|fear]]_ aura (variable distance, DC 20)

##### Defense

**AC** 19, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 19 (–1 Dex, +12 natural, –2 size)
**hp** 95 (10d8+50)
**Fort** +12, **Ref** +2, **Will** +5
**Defensive Abilities** _[[spells/Spell Absorption|spell absorption]]_; **Immune** electricity, fire, _[[universal monster rules/Plant Traits|plant traits]]_; **SR** 19 (see _spell absorption_)

##### Offense
**Speed** 10 ft.
**Melee** bite +14 (2d6+9), 3 roots +12 (1d6+4 plus _[[universal monster rules/Pull|pull]]_)
**Space** 5 ft., **Reach** 15 ft. (60 ft. with _[[spells/Root|root]]_)
**Special Attacks** _pull_ (_root_, 10 ft.)

##### Statistics
**Str** 29, **Dex** 8, **Con** 21, **Int** 12, **Wis** 15, **Cha** 12
**Base Atk** +7; **CMB** +18; **CMD** 27 (can’t be tripped)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Knowledge (nature) +11, Perception +21, Stealth +4 (+8 in forests); **Racial Modifiers** +4 Stealth in forests
**Languages** Common, Sylvan

##### Ecology

**Environment** temperate forests
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Fear_ Aura (Su)** A _[[monsters/Quickwood|quickwood]]_ with stored magical energy can activate its _fear_ aura as a standard action. The aura has a radius of 10 feet per spell level of the effect and lasts for 1 round (Will DC 20 negates). Creatures that fail their saving throws become _[[conditions/Panicked|panicked]]_ for 1 minute. The DC is Charisma-based and includes a +4 racial bonus.

**Oaksight (Su)** A _quickwood_ may observe the area surrounding any oak tree within 360 feet as if using clairaudience/clairvoyance. It can use this ability on any number of oak trees in the area. Although the _quickwood_ does not need line of sight to establish this link, if it does have line of sight to even a single oak tree, it cannot be flanked.

**Roots (Ex)** A _quickwood_ has dozens of long roots, but can only attack with up to three of them in any given round. If the _quickwood_ uses its _pull_ ability to _pull_ a target within reach of its bite attack, it can immediately make a free bite attack with a +4 bonus on its attack roll against that target.
**_Spell Absorption_ (Su)** If a _quickwood_’s _[[universal monster rules/Spell Resistance|spell resistance]]_ protects it from a magical effect, the creature absorbs that magical energy into its body. It can release this energy to activate its _fear_ aura ability. While the plant is storing a spell, its SR decreases by 5. It can only store one spell at a time.

##### Description

These carnivorous plants prize human and elven flesh, but eat anything they manage to catch. Quickwoods typically explore an area, taking note of any oak trees, and then _root_ themselves and wait for prey to wander by. They use their oaksight ability to maintain constant surveillance of their hunting grounds and send their roots out to drag likely prey back to them.