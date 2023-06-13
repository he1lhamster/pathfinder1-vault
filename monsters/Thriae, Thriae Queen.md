---
cssclass: [monsters]
title1: Thriae, Thriae Queen
desc_short: This towering, shapely, purple-skinned woman has an insectile lower body,
  antennae on her brow, and the wings of a bee.
title2: Thriae Queen
CR: 18
sources:
- name: Bestiary 3
  page: 267
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 153600
alignment: LN
size: Huge
type: monstrous humanoid
initiative:
  bonus: 4
senses:
  darkvision: 60
  detect secret doors: true
  low-light vision: true
  true seeing: true
AC:
  AC: 33
  touch: 8
  flat_footed: 33
  components:
    natural: 25
    size: -2
HP:
  HP: 312
  long: 25d10+175
  fast_healing: 10
saves:
  fort: 15
  ref: 14
  will: 21
defensive_abilities:
- merope coat
immunities:
- poison
- sonic
resistances:
  acid: 20
SR: 29
speeds:
  base: 30
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: +2 axiomatic light mace +35/+30/+25/+20 (2d6+11/19-20)
      entries:
      - - damage: 2d6+11
          crit_range: 19-20
      attack: +2 axiomatic light mace
      bonus:
      - 35
      - 30
      - 25
      - 20
    - text: sting +27 (2d8+4/19-20 plus poison)
      entries:
      - - damage: 2d8+4
          crit_range: 19-20
        - effect: poison
      attack: sting
      bonus:
      - 27
  special:
  - launch merope
  - spawn soldiers
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect secret doors
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: daylight
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 21
  - name: greater scrying
    source: default
    freq: At will
    DC: 26
  - name: neutralize poison
    source: default
    freq: At will
  - name: remove disease
    source: default
    freq: At will
  - name: speak with dead
    source: default
    freq: At will
    DC: 22
  - name: charm monster
    source: default
    freq: 3/day
    DC: 23
  - name: find the path
    source: default
    freq: 3/day
  - name: giant vermin
    source: default
    freq: 3/day
    other: 8 bees or 6 wasps
  - name: mass cure critical wounds
    source: default
    freq: 3/day
  - name: poison
    source: default
    freq: 3/day
    DC: 23
  - name: restoration
    source: default
    freq: 3/day
  - name: quickened slow
    source: default
    freq: 3/day
    DC: 22
  - name: foresight
    source: default
    freq: 1/day
  - name: mass heal
    source: default
    freq: 1/day
  - name: regenerate
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 28
  DEX: 11
  CON: 25
  INT: 20
  WIS: 21
  CHA: 28
BAB: 25
CMB: 36
CMD: 46
feats:
- name: Alertness
- name: Combat Casting
- name: Combat Expertise
- name: Critical Focus
- name: Greater Spell Penetration
- name: Improved Critical (sting)
- name: Improved Critical (light mace)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Quicken Spell-Like Ability (slow)
- name: Spell Penetration
- name: Weapon Focus (light mace)
skills:
  Bluff: 34
  Diplomacy: 34
  Fly: 28
  Knowledge (arcana): 30
  Knowledge (religion): 30
  Perception: 37
  Sense Motive: 34
  Spellcraft: 30
  Use Magic Device: 34
languages:
- Common
- Sylvan
- Thriae
- telepathy 300 ft.
ecology:
  environment: any
  organization: solitary or colony (1 queen, 3 seers, 11-20 soldiers, and 3-30 giant
    bees)
  treasure_type: double
  treasure:
  - +2 axiomatic light mace
  - other treasure
special_abilities:
  Launch Merope (Su): A thriae queen can launch a stream of merope from a gland in
    her lower body in a 60-foot line as a standard action. A thriae queen using this
    ability can control the purity of the merope she launches, which makes it either
    harm those it touches or heal them. If a thriae queen chooses to make her merope
    harmful, all creatures in the area of effect take 20d8 points of acid damage (Reflex
    DC 29 for half). In addition, any creature in the area of effect is also staggered
    for 1d4 rounds (or 1 round if it succeeds at its Reflex save). If she uses it
    to heal, the merope heals all living creatures in the area of effect for 10d8
    points of damage. A thriae queen can use this ability once every 1d4 rounds. The
    save DC is Constitution-based.
  Merope Coat (Su): A thriae queen is covered in a thin layer of merope. This coating
    acts as a magical barrier between spells cast at the thriae queen, as though she
    were constantly under the effects of spell turning. The coat affects a maximum
    of eight spell levels-when a spell effect is turned, this coating is depleted
    by a number of spell levels equal to the level of the spell reflected. The queen
    regenerates this coating at a rate of one spell level per round. A spell in excess
    of what the merope coat can currently reflect is not reflected, and reduces the
    merope coat to a score of 0. Spells that fail to penetrate the queen's spell resistance
    do not reduce the merope coat's efficiency in this manner.
  Spawn Soldiers (Su): Three times per day as a standard action, a thriae queen can
    spawn a large swarm of wasps. This functions as four separate wasp swarms (Bestiary
    275) that occupy all of the squares adjacent to the thriae queen. These swarms
    do not harm any thriae, and while they move with the queen as she moves, the swarms
    cannot leave her side. The swarms last until they are destroyed or 1 hour passes,
    at which point the swarms die on their own.
  Poison (Ex): Sting-injury; save Fort DC 29; frequency 1/round for 6 rounds; effect
    1d6 Con plus staggered for 1 round; cure 2 consecutive saves.
desc_long: |-
  The most powerful individual within any given thriae colony, the queen is a divine soothsayer, a provider of life, and a destroyer of those would seek to disrupt the order of the colony. Viewed by her children as a benevolent matriarch rather than a mother, the thriae queen is the only fertile member of the colony, and thus the sole reproducer should the colony's population meet a devastating blow, whether through plague, famine, or war. A queen is revered by soldiers and seers alike, both for her physical might and her divine power, and she exemplifies the very best of thriae society in terms of strength, insight, and magnetism. While a queen is often too busy to entertain guests of a thriae hive, those intruders who do catch a glimpse of her are captured by her beauty and grace, and many would follow her if only to be by her side. But those who are allowed to enjoy the queen's company are few, and those few are carefully selected from among the hive's greatest warriors and priestesses, soldiers and seers whose powers have shown them to be skillful as well as loyal.

  Most thriae colonies only have one queen, though particularly large or far-reaching hives have been known to have as many as three at any given time. Thriae queens are the ultimate authority within a hive, and make most of the major decisions regarding the colony's growth. Only the wealthiest and most respected outsiders are granted an audience with the ever-busy queen, whose numerous duties around the hive are analogous to those of any other ruler of a small kingdom. They grant only audiences regarding matters of the utmost concern, matters that stimulate the curiosity of a thriae queen and require not merely the cryptic readings of seers but a true divination as only a queen can provide.

  When not divining or performing governmental tasks, a thriae queen can often be found in her private chamber, where she lies with male consorts, lays eggs, cares for her larvae, and creates the vast stores of merope used every day within the hive. Consorts are chosen carefully, as they are constantly within extremely close proximity to the queen, who is far from vulnerable in her own right but nonetheless often prefers to avoid conflicts with would-be assassins or burglars.

  A thriae queen lays fertilized eggs in one of the waxy, golden cells of her chamber walls. Thriae eggs go through several stages of growth before becoming fully formed thriae-the longest stage of development is the larval stage, which is a crucial point in determining the formation of a thriae. Most larvae are fed merope while they grow, but in the height of her power, a thriae queen selects a single larva to be her successor, and she feeds that individual a special substance secreted from her merope gland called royal merope. This thick, jellylike substance strengthens the larva and causes it to grow greatly in size, and when it pupates and hatches, it does so as a fully grown thriae queen.

  The mother queen teaches its successor in the ways of divining as well as ruling a colony. The successor then faces a choice-either remaining in the colony she was born into and furthering the growth of the hive, or setting out on her own to establish an allied colony. If she does the latter, the remaining queen must birth another successor, which is not considered so much a bother as it is an unavoidable circumstance. Queens do not look upon successors who leave as deserting daughters, instead viewing them as future allies for the colony down the road.

---

# Thriae, Thriae Queen
This towering, shapely, purple-skinned woman has an insectile lower body, antennae on her brow, and the wings of a bee.
**Source** Bestiary 3 pg. 267
**XP** 153,600

LN Huge monstrous humanoid
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Secret Doors|detect secret doors]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +37

##### Defense

**AC** 33, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+25 natural, –2 size)
**hp** 312 (25d10+175); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +15, **Ref** +14, **Will** +21
**Defensive Abilities** merope coat; **Immune** poison, sonic; **Resist** acid 20; **SR** 29

##### Offense
**Speed** 30 ft., fly 50 ft. (good)
**Melee** +2 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _[[items/Weapon/Light mace|light mace]]_ +35/+30/+25/+20 (2d6+11/19–20), sting +27 (2d8+4/19–20 plus poison)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** launch merope, spawn soldiers
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
Constant—_detect secret doors_, _true seeing_
At will—_[[spells/Daylight|daylight]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 21), greater _[[spells/Scrying|scrying]]_ (DC 26), _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Speak with Dead|speak with dead]]_ (DC 22)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 23), _[[spells/Find the Path|find the path]]_, _[[spells/Giant Vermin|giant vermin]]_ (8 bees or 6 wasps), mass _[[spells/Cure Critical Wounds|cure critical wounds]]_, poison  (DC 23), _[[spells/Restoration|restoration]]_, quickened _[[spells/Slow|slow]]_ (DC 22)
1/day—_[[spells/Foresight|foresight]]_, mass _[[spells/Heal|heal]]_, _[[spells/Regenerate|regenerate]]_

##### Statistics
**Str** 28, **Dex** 11, **Con** 25, **Int** 20, **Wis** 21, **Cha** 28
**Base Atk** +25; **CMB** +36; **CMD** 46
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Improved Critical|Improved Critical]]_ (sting), _Improved Critical_ (_light mace_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_slow_), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light mace_)
**Skills** Bluff +34, Diplomacy +34, Fly +28, Knowledge (arcana) +30, Knowledge (religion) +30, Perception +37, Sense Motive +34, Spellcraft +30, Use Magic Device +34
**Languages** Common, Sylvan, Thriae; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.

##### Ecology

**Environment** any
**Organization** solitary or colony (1 queen, 3 seers, 11–20 soldiers, and 3–30 giant bees)
**Treasure** double (+2 _axiomatic_ _light mace_, other treasure)

### Special Abilities

**Launch Merope (Su)** A thriae queen can launch a stream of merope from a gland in her lower body in a 60-foot line as a standard action. A thriae queen using this ability can control the purity of the merope she launches, which makes it either _[[spells/Harm|harm]]_ those it touches or _heal_ them. If a thriae queen chooses to make her merope harmful, all creatures in the area of effect take 20d8 points of acid damage (Reflex DC 29 for half). In addition, any creature in the area of effect is also _[[conditions/Staggered|staggered]]_ for 1d4 rounds (or 1 round if it succeeds at its Reflex save). If she uses it to _heal_, the merope heals all living creatures in the area of effect for 10d8 points of damage. A thriae queen can use this ability once every 1d4 rounds. The save DC is Constitution-based.

**Merope Coat (Su)** A thriae queen is covered in a thin layer of merope. This coating acts as a magical barrier between spells cast at the thriae queen, as though she were constantly under the effects of _[[spells/Spell Turning|spell turning]]_. The coat affects a maximum of eight spell levels—when a spell effect is turned, this coating is depleted by a number of spell levels equal to the level of the spell reflected. The queen regenerates this coating at a rate of one spell level per round. A spell in excess of what the merope coat can currently reflect is not reflected, and reduces the merope coat to a score of 0. Spells that fail to penetrate the queen’s _[[universal monster rules/Spell Resistance|spell resistance]]_ do not reduce the merope coat’s efficiency in this manner.
**Spawn Soldiers (Su)** Three times per day as a standard action, a thriae queen can spawn a large swarm of wasps. This functions as four separate wasp swarms (Bestiary 275) that occupy all of the squares adjacent to the thriae queen. These swarms do not _harm_ any thriae, and while they move with the queen as she moves, the swarms cannot leave her side. The swarms last until they are destroyed or 1 hour passes, at which point the swarms die on their own.

**Poison (Ex)** Sting—injury; save Fort DC 29; frequency 1/round for 6 rounds; effect 1d6 Con plus _staggered_ for 1 round; cure 2 consecutive saves.

##### Description

The most powerful individual within any given thriae colony, the queen is a divine soothsayer, a provider of life, and a destroyer of those would seek to disrupt the order of the colony. Viewed by her children as a _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ matriarch rather than a mother, the thriae queen is the only fertile member of the colony, and thus the sole reproducer should the colony’s population meet a devastating blow, whether through plague, _[[curses/Famine|famine]]_, or war. A queen is revered by soldiers and seers alike, both for her physical might and her _[[spells/Divine Power|divine power]]_, and she exemplifies the very best of thriae society in terms of strength, insight, and magnetism. While a queen is often too busy to entertain guests of a thriae hive, those intruders who do catch a glimpse of her are captured by her beauty and _[[spells/Grace|grace]]_, and many would follow her if only to be by her side. But those who are allowed to enjoy the queen’s company are few, and those few are carefully selected from among the hive’s greatest warriors and priestesses, soldiers and seers whose powers have shown them to be skillful as well as loyal.

Most thriae colonies only have one queen, though particularly large or far-reaching hives have been known to have as many as three at any given time. Thriae queens are the ultimate authority within a hive, and make most of the major decisions regarding the colony’s growth. Only the wealthiest and most respected outsiders are granted an audience with the ever-busy queen, whose numerous duties around the hive are analogous to those of any other ruler of a small kingdom. They grant only audiences regarding matters of the utmost concern, matters that stimulate the curiosity of a thriae queen and require not merely the cryptic readings of seers but a true _[[spells/Divination|divination]]_ as only a queen can provide.

When not divining or performing governmental tasks, a thriae queen can often be found in her private chamber, where she lies with male consorts, lays eggs, cares for her larvae, and creates the vast stores of merope used every day within the hive. Consorts are chosen carefully, as they are constantly within extremely close proximity to the queen, who is far from vulnerable in her own right but nonetheless often prefers to avoid conflicts with would-be assassins or burglars.

A thriae queen lays fertilized eggs in one of the waxy, golden cells of her chamber walls. Thriae eggs go through several stages of growth before becoming fully formed thriae—the longest stage of development is the larval stage, which is a crucial point in determining the formation of a thriae. Most larvae are fed merope while they grow, but in the height of her power, a thriae queen selects a single larva to be her successor, and she feeds that individual a special substance secreted from her merope gland _[[items/Weapon Magic Abilities/Called|called]]_ royal merope. This thick, jellylike substance strengthens the larva and causes it to grow greatly in size, and when it pupates and hatches, it does so as a fully grown thriae queen.

The mother queen teaches its successor in the ways of divining as well as ruling a colony. The successor then faces a choice—either remaining in the colony she was born into and furthering the growth of the hive, or setting out on her own to establish an allied colony. If she does the latter, the remaining queen must birth another successor, which is not considered so much a bother as it is an unavoidable circumstance. Queens do not look upon successors who leave as deserting daughters, instead viewing them as future allies for the colony down the road.