---
cssclass: [monsters]
title1: Shrike Worm
desc_short: Iridescent spines cover the back of this enormous, long-legged worm. Writhing
  tentacles sprout from its throat, below a circular, toothy maw dripping with luminescent
  spittle.
title2: Shrike Worm
CR: 15
sources:
- name: 'Pathfinder #114: Black Stars Beckon'
  page: 90
  link: http://paizo.com/products/btpy9qcm?Pathfinder-Adventure-Path-114-Black-Stars-Beckon
XP: 51200
alignment: NE
size: Huge
type: aberration
initiative:
  bonus: 7
senses:
  blindsight: 60
  darkvision: 60
auras:
- name: impossible form
  radius: 100
  DC: 27
AC:
  AC: 29
  touch: 11
  flat_footed: 26
  components:
    dex: 3
    natural: 18
    size: -2
HP:
  HP: 231
  long: 22d8+132
saves:
  fort: 14
  ref: 10
  will: 17
  other: +6 vs. illusion
defensive_abilities:
- illusion sense
DR:
- amount: 10
  weakness: magic
SR: 26
speeds:
  base: 30
  other:
  - air walk
attacks:
  melee:
  - - text: 2 claws +24 (1d8+9)
      entries:
      - - damage: 1d8+9
      count: 2
      attack: claws
      bonus:
      - 24
    - text: 6 tentacles +22 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      count: 6
      attack: tentacles
      bonus:
      - 22
  special:
  - impale
  - phantasmal slime (DC 27, once every 1d4 rounds)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: hallucinatory terrain
    source: default
    freq: 3/day
    DC: 20
  - name: persistent image
    source: default
    freq: 3/day
    DC: 21
  - name: scintillating pattern
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 15
    concentration: 21
ability_scores:
  STR: 28
  DEX: 16
  CON: 20
  INT: 7
  WIS: 19
  CHA: 23
BAB: 16
CMB: 27
CMB_other: +31 grapple
CMD: 40
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Following Step
- name: Great Fortitude
- name: Improved Initiative
- name: Lunge
- name: Multiattack
- name: Step Up
- name: Step Up and Strike
- name: Toughness
- name: Weapon Focus (claw)
- name: Weapon Focus (tentacle)
skills:
  Perception: 29
  Survival: 29
languages:
- Aklo (can't speak)
ecology:
  environment: any land or underground
  organization: solitary, pair, or delusion (3-5)
  treasure_type: incidental
special_abilities:
  Illusion Sense (Ex): Shrike worms can sense illusion magic, rendering it less effective
    against them. A shrike worm gains a bonus on saving throws against illusion spells
    and effects equal to its Charisma bonus, and it does not need to examine or interact
    with an illusion in order to attempt a saving throw to disbelieve it.
  Impale (Ex): If a shrike worm begins its turn with a creature grappled with its
    tentacles, it can attempt a grapple combat maneuver check as a free action to
    try to impale the grappled creature on one of the spines on its back. If the shrike
    worm succeeds, the grappled creature takes 6d6+18 points of damage and is pinned.
    Once a creature is impaled, it loses the grappled condition and the shrike worm
    can use all of its tentacles without penalty. A shrike worm can have up to six
    Medium or smaller creatures impaled on its spikes at a time. An impaled creature
    can remove itself from a spine by succeeding at a combat maneuver or Escape Artist
    check as normal. A creature that is removed from a shrike worm spine (either by
    its own efforts, those of its allies, or magic) takes 3d6 points of bleed damage
    and is sickened for 1d4 rounds.
  Impossible Form (Su): Any creature within 100 feet of the shrike worm that can see
    it must succeed at a DC 27 Will saving throw or become fascinated for as long
    as the creature remains within range of this ability. A creature that fails its
    save believes the shrike worm is a hallucination or an illusion; the shrike worm's
    approach does not constitute an obvious threat and does not break this fascination
    effect. The fascination effect ends as normal if the shrike worm attacks or interacts
    with the affected creature or its allies. A creature that saves against a shrike
    worm's impossible form aura is immune to it for 24 hours. This is a mind-affecting
    effect. The save DC is Charisma-based.
  Phantasmal Slime (Sp): As a standard action that doesn't provoke attacks of opportunity,
    a shrike worm can spew from its mouth a 30-foot cone of scintillating color that
    infects the minds of those it touches. This functions as per phantasmal web (DC
    21), except that a creature that fails its save believes it is caught in threads
    of sticky, luminous slime infested with diminutive shrike worm larvae. The shrike
    worm can use this ability once every 1d4 rounds. A creature that realizes the
    slime is illusory gains a +4 bonus on saves to resist subsequent uses of this
    ability.
desc_long: |-
  Shrike worms are insidious creatures from the edges of reality, and are able to blur the boundary between what is real and unreal in order to take their prey by surprise. Also known as hallucination worms, they are most often called shrike worms due to the method by which they kill their prey. When a shrike worm catches a creature in its tentacles, it then impales its victim on its iridescent back spines, pinning the creature in place in order to prolong its prey's suffering as much as possible.

  Shrike worms grow to over 25 feet long and, despite weighing upward of 16,000 pounds, carry themselves about with surprising grace on their long legs. This lends their movements an unearthly quality, which is further enhanced by their magical abilities.

---

# Shrike Worm
Iridescent spines cover the back of this enormous, long-legged worm. Writhing tentacles sprout from its throat, below a circular, toothy maw dripping with luminescent spittle.
**Source** Pathfinder #114: Black Stars Beckon pg. 90
**XP** 51,200

NE Huge aberration
**Init** +7; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +29
**Aura** impossible form (100 ft., DC 27)

##### Defense

**AC** 29, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+3 Dex, +18 natural, –2 size)
**hp** 231 (22d8+132)
**Fort** +14, **Ref** +10, **Will** +17; +6 vs. illusion
**Defensive Abilities** illusion sense; **DR** 10/magic; **SR** 26

##### Offense
**Speed** 30 ft., _[[spells/Air Walk|air walk]]_
**Melee** 2 claws +24 (1d8+9), 6 tentacles +22 (1d6+4 plus _[[universal monster rules/Grab|grab]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** impale, _[[items/Armor Magic Abilities/Phantasmal|phantasmal]]_ slime (DC 27, once every 1d4 rounds)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
Constant—_air walk_
3/day—_[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 20), _[[spells/Persistent Image|persistent image]]_ (DC 21)
1/day—_[[spells/Scintillating Pattern|scintillating pattern]]_ (DC 24)

##### Statistics
**Str** 28, **Dex** 16, **Con** 20, **Int** 7, **Wis** 19, **Cha** 23
**Base Atk** +16; **CMB** +27 (+31 grapple); **CMD** 40 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Following Step|Following Step]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Step Up and Strike|Step Up and Strike]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw), _Weapon Focus_ (tentacle)
**Skills** Perception +29, Survival +29
**Languages** Aklo (can’t speak)

##### Ecology

**Environment** any land or underground
**Organization** solitary, pair, or delusion (3–5)
**Treasure** incidental

### Special Abilities

**Illusion Sense (Ex)** Shrike worms can sense illusion magic, rendering it less effective against them. A _[[monsters/Shrike Worm|shrike worm]]_ gains a bonus on saving throws against illusion spells and effects equal to its Charisma bonus, and it does not need to examine or interact with an illusion in order to attempt a saving throw to disbelieve it.

**Impale (Ex)** If a _shrike worm_ begins its turn with a creature _[[conditions/Grappled|grappled]]_ with its tentacles, it can attempt a grapple combat maneuver check as a free action to try to impale the _grappled_ creature on one of the spines on its back. If the _shrike worm_ succeeds, the _grappled_ creature takes 6d6+18 points of damage and is _[[conditions/Pinned|pinned]]_. Once a creature is impaled, it loses the _grappled_ condition and the _shrike worm_ can use all of its tentacles without penalty. A _shrike worm_ can have up to six Medium or smaller creatures impaled on its spikes at a time. An impaled creature can remove itself from a spine by succeeding at a combat maneuver or Escape Artist check as normal. A creature that is removed from a _shrike worm_ spine (either by its own efforts, those of its allies, or magic) takes 3d6 points of _[[universal monster rules/Bleed|bleed]]_ damage and is _[[conditions/Sickened|sickened]]_ for 1d4 rounds.

**Impossible Form (Su)** Any creature within 100 feet of the _shrike worm_ that can see it must succeed at a DC 27 Will saving throw or become _[[conditions/Fascinated|fascinated]]_ for as long as the creature remains within range of this ability. A creature that fails its save believes the _shrike worm_ is a hallucination or an illusion; the _shrike worm_’s approach does not constitute an obvious threat and does not break this fascination effect. The fascination effect ends as normal if the _shrike worm_ attacks or interacts with the affected creature or its allies. A creature that saves against a _shrike worm_’s impossible form aura is immune to it for 24 hours. This is a mind-affecting effect. The save DC is Charisma-based.

**_Phantasmal_ Slime (Sp)** As a standard action that doesn’t provoke attacks of opportunity, a _shrike worm_ can spew from its mouth a 30-foot cone of scintillating color that infects the minds of those it touches. This functions as per _[[spells/Phantasmal Web|phantasmal web]]_ (DC 21), except that a creature that fails its save believes it is caught in threads of _[[items/Weapon Magic Abilities/Sticky|sticky]]_, luminous slime infested with diminutive _shrike worm_ larvae. The _shrike worm_ can use this ability once every 1d4 rounds. A creature that realizes the slime is illusory gains a +4 bonus on saves to resist subsequent uses of this ability.

##### Description

Shrike worms are insidious creatures from the edges of reality, and are able to _[[spells/Blur|blur]]_ the boundary between what is real and unreal in order to take their prey by surprise. Also known as hallucination worms, they are most often _[[items/Weapon Magic Abilities/Called|called]]_ shrike worms due to the method by which they kill their prey. When a _shrike worm_ catches a creature in its tentacles, it then impales its victim on its iridescent back spines, pinning the creature in place in order to prolong its prey’s suffering as much as possible.

Shrike worms grow to over 25 feet long and, despite weighing upward of 16,000 pounds, carry themselves about with surprising _[[spells/Grace|grace]]_ on their long legs. This lends their movements an unearthly quality, which is further enhanced by their magical abilities.