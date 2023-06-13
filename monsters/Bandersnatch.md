---
cssclass: [monsters]
title1: Bandersnatch
desc_short: This six-limbed beast stalks forward with a fluid grace. Barbed quills
  run along its back, and its eyes glow with a blue light.
title2: Bandersnatch
CR: 17
sources:
- name: Bestiary 3
  page: 32
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 102400
alignment: N
size: Gargantuan
type: magical beast
initiative:
  bonus: 11
senses:
  blindsense: 120
  darkvision: 120
  low-light vision: true
  scent: true
AC:
  AC: 33
  touch: 13
  flat_footed: 26
  components:
    dex: 7
    natural: 20
    size: -4
HP:
  HP: 310
  long: 23d10+184
  fast_healing: 10
saves:
  fort: 21
  ref: 20
  will: 11
defensive_abilities:
- quick recovery
- quill defense
immunities:
- fear
- paralysis
- poison
- sleep
speeds:
  base: 60
  climb: 20
attacks:
  melee:
  - - text: bite +32 (2d8+13 plus grab)
      entries:
      - - damage: 2d8+13
        - effect: grab
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d6+13/19-20)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +27 (2d8+19/×3 plus pain)
      entries:
      - - damage: 2d8+19
          crit_multiplier: 3
        - effect: pain
      attack: tail slap
      bonus:
      - 27
  ranged:
  - - text: 4 quills +26 (1d10+13/19-20)
      entries:
      - - damage: 1d10+13
          crit_range: 19-20
      count: 4
      attack: quills
      bonus:
      - 26
  special:
  - bounding charge
  - brutal tail
  - gaze
  - lash out
  - pounce
  - rake (4 claws, +32, 2d6+13/19-20)
  - rend (2 claws, 2d6+19)
space: 20
reach: 15
reach_other: 20 ft. with tail slap
ability_scores:
  STR: 36
  DEX: 25
  CON: 27
  INT: 2
  WIS: 15
  CHA: 18
BAB: 23
CMB: 40
CMB_other: +44 grapple
CMD: 57
CMD_other: 65 vs. trip
feats:
- name: Bleeding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Critical Mastery
- name: Exhausting Critical
- name: Improved Critical (claws)
- name: Improved Critical (quills)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Skill Focus (Stealth)
- name: Tiring Critical
skills:
  Acrobatics: 19
    when jumping: 31
  Climb: 21
  Perception: 26
  Stealth: 18
    forests: 26
  Survival: 3
    tracking: 23
  _racial_mods:
    Acrobatics:
      _: 8
    Perception:
      _: 10
    Stealth:
      _: 4
      forests: 12
    Survival:
      when tracking: 20
special_qualities:
- planar acclimation
- relentless tracker
ecology:
  environment: any forests
  organization: solitary
  treasure_type: incidental
special_abilities:
  Bounding Charge (Ex): A bandersnatch can move through difficult terrain when it
    charges.
  Brutal Tail (Ex): The quills and barbs on a bandersnatch's tail cause triple damage
    on a critical hit from its tail slap. A bandersnatch adds 1-1/2 times its strength
    bonus on attack rolls when using its tail slap.
  Gaze (Su): Confused for 1 round, range 30 feet, Fortitude DC 29 negates. A bandersnatch
    can direct its gaze attack against a single foe as a swift action. This is a mind-affecting
    compulsion effect. The save DC is Constitution-based.
  Lash Out (Ex): As a swift action, a bandersnatch can make a single attack with a
    bite, claw, or tail slap. A bandersnatch cannot lash out on the same round it
    charges.
  Pain (Ex): Whenever a creature takes damage from a bandersnatch's tail slap attack,
    quills, or quill defense, that creature must make a DC 28 Reflex save or a quill
    lodges in its flesh, causing the creature to become sickened until the quill is
    removed. Removing one quill requires a DC 20 Heal check made as a full-round action.
    For every 5 by which the check exceeds the DC, one additional quill can be removed.
    On a failed check, a quill is still removed, but the process deals 1d10+6 points
    of damage to the victim. The save DC is Dexterity-based.
  Planar Acclimation (Ex): A bandersnatch is always considered to be on its home plane,
    regardless of what plane it finds itself upon. It never gains the extraplanar
    subtype.
  Quill Defense (Ex): Any creature that strikes a bandersnatch with a non-reach melee
    weapon, unarmed strike, or natural weapon takes 1d10 points of piercing damage
    from the bandersnatch's quills and suffers from the bandersnatch's pain attack.
  Quick Recovery (Su): 'A debilitated bandersnatch recovers with frightening speed.
    If a bandersnatch starts its turn affected by any or all of the following conditions,
    these conditions end at the end of its turn: confused, dazed, dazzled, exhausted,
    fatigued, nauseated, sickened, and stunned. Furthermore, a bandersnatch affected
    by ability damage, ability drain, or a mind-affecting effect that allows a save
    receives a single additional save against the effect of its choice at the original
    DC at the end of its turn in order to shake off the effect.'
  Quills (Ex): With a snap of its tail, a bandersnatch can loose a volley of four
    quills as a standard action (make an attack roll for each spike). This attack
    has a range of 300 feet with no range increment. All targets must be within 30
    feet of each other. Launched quills regrow in a single round, during which the
    bandersnatch's defensive abilities are unaffected.
  Relentless Tracker (Ex): A bandersnatch can move at up to double its speed and still
    track without penalty. It gains a +10 competence bonus on Survival checks made
    to track creatures it has wounded.
desc_long: |-
  Bandersnatches are consummate hunters, and only the deadliest predators or the most cunning intelligent prey offer them sport. Once a bandersnatch has marked a creature for death, it runs it to ground without fear, rest, or remorse.

  Bandersnatches rely on speed, shock, and terror to bring down prey. They pace their quarry from a distance, hidden among the trees, then break from cover, savage their target, and dart away again. They drag smaller creatures away to dispatch at leisure, while engaging larger ones in skirmishes until they gradually wear their prey down. An outmatched bandersnatch withdraws at full speed, stopping only to pick off pursuers that distance themselves from their allies. Once its wounds heal, the bandersnatch returns to the scene of its defeat, picks up the trail of its assailants, and eliminates them one by one.

  In appearance, a bandersnatch resembles a tawny, six-legged great cat, but with wickedly barbed quills running the length of its body and down to the tip of its long, flexible tail. Its quills serve to deter attackers, but also act as a formidable weapon. With a single flick of its muscular tail, a bandersnatch can fling as many as a half-dozen quills at distant foes with surprising accuracy. A bandersnatch captivates any prey that meets the gaze of its saucerlike, luminous eyes. A bandersnatch measures 40 feet in length plus another 10 feet of tail and weighs 12,000 pounds. Despite their bulk, bandersnatches move with speed, grace, and even considerable stealth when required.

  Bandersnatches were once native to the primal world of the fey, where they preyed on the greatest hunters of that ancient realm. As with other legendary creatures from this realm, such as the jabberwock, bandersnatches belong to a group of creatures known collectively as the “Tane.” Whether the fey were careless in guarding their portals or released the first bandersnatches into Material Plane deliberately cannot be said with certainty. Rare in the extreme on the Material Plane, bandersnatches lair within forgotten forests where ancient beasts walk the world.

  Bandersnatches mate only rarely. A female becomes fertile perhaps once or twice per century, leaving the male soon after mating and giving birth to only one or two kittens per litter. The mother brings meat to her ravenous young, which mature into lesser bandersnatches (see below) within a year. Bandersnatches live for a thousand years or longer.

---

# Bandersnatch
This six-limbed beast stalks forward with a fluid _[[spells/Grace|grace]]_. Barbed quills run along its back, and its eyes glow with a blue light.
**Source** Bestiary 3 pg. 32
**XP** 102,400

N Gargantuan magical beast
**Init** +11; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +26

##### Defense

**AC** 33, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+7 Dex, +20 natural, –4 size)
**hp** 310 (23d10+184); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +21, **Ref** +20, **Will** +11
**Defensive Abilities** quick recovery, quill defense; **Immune** _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +32 (2d8+13 plus _[[universal monster rules/Grab|grab]]_), 2 claws +32 (2d6+13/19–20), tail slap +27 (2d8+19/×3 plus pain)
**Ranged** 4 quills +26 (1d10+13/19–20)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with tail slap)
**Special Attacks** bounding charge, brutal tail, _[[universal monster rules/Gaze|gaze]]_, lash out, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (4 claws, +32, 2d6+13/19–20), _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+19)

##### Statistics
**Str** 36, **Dex** 25, **Con** 27, **Int** 2, **Wis** 15, **Cha** 18
**Base Atk** +23; **CMB** +40 (+44 grapple); **CMD** 57 (65 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Critical Mastery|Critical Mastery]]_, _[[feats/Exhausting Critical|Exhausting Critical]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _Improved Critical_ (quills), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Tiring Critical|Tiring Critical]]_
**Skills** Acrobatics +19 (+31 when jumping), _Climb_ +21, Perception +26, Stealth +18 (+26 forests), Survival +3 (+23 tracking); **Racial Modifiers** +8 Acrobatics, +10 Perception, +4 Stealth (+12 forests), +20 Survival when tracking
**SQ** _[[items/Weapon Magic Abilities/Planar|planar]]_ acclimation, relentless tracker

##### Ecology

**Environment** any forests
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Bounding Charge (Ex)** A _[[monsters/Bandersnatch|bandersnatch]]_ can move through difficult terrain when it charges.

**Brutal Tail (Ex)** The quills and barbs on a _bandersnatch_’s tail cause triple damage on a critical hit from its tail slap. A _bandersnatch_ adds 1-1/2 times its strength bonus on attack rolls when using its tail slap.

**_Gaze_ (Su)** _[[conditions/Confused|Confused]]_ for 1 round, range 30 feet, Fortitude DC 29 negates. A _bandersnatch_ can direct its _gaze_ attack against a single foe as a swift action. This is a mind-affecting compulsion effect. The save DC is Constitution-based.

**Lash Out (Ex)** As a swift action, a _bandersnatch_ can make a single attack with a bite, claw, or tail slap. A _bandersnatch_ cannot lash out on the same round it charges.

**Pain (Ex)** Whenever a creature takes damage from a _bandersnatch_’s tail slap attack, quills, or quill defense, that creature must make a DC 28 Reflex save or a quill lodges in its flesh, causing the creature to become _[[conditions/Sickened|sickened]]_ until the quill is removed. Removing one quill requires a DC 20 _[[spells/Heal|Heal]]_ check made as a full-round action. For every 5 by which the check exceeds the DC, one additional quill can be removed. On a failed check, a quill is still removed, but the process deals 1d10+6 points of damage to the victim. The save DC is Dexterity-based.

**_Planar_ Acclimation (Ex)** A _bandersnatch_ is always considered to be on its home plane, regardless of what plane it finds itself upon. It never gains the extraplanar subtype.

**Quill Defense (Ex)** Any creature that strikes a _bandersnatch_ with a non-reach melee weapon, unarmed strike, or natural weapon takes 1d10 points of piercing damage from the _bandersnatch_’s quills and suffers from the _bandersnatch_’s pain attack.

**Quick Recovery (Su)** A debilitated _bandersnatch_ recovers with frightening speed. If a _bandersnatch_ starts its turn affected by any or all of the following conditions, these conditions end at the end of its turn: _confused_, _[[conditions/Dazed|dazed]]_, _[[conditions/Dazzled|dazzled]]_, _[[conditions/Exhausted|exhausted]]_, _[[conditions/Fatigued|fatigued]]_, _[[conditions/Nauseated|nauseated]]_, _sickened_, and _[[conditions/Stunned|stunned]]_. Furthermore, a _bandersnatch_ affected by ability damage, ability drain, or a mind-affecting effect that allows a save receives a single additional save against the effect of its choice at the original DC at the end of its turn in order to shake off the effect.

**Quills (Ex)** With a snap of its tail, a _bandersnatch_ can loose a volley of four quills as a standard action (make an attack roll for each spike). This attack has a range of 300 feet with no range increment. All targets must be within 30 feet of each other. Launched quills regrow in a single round, during which the _bandersnatch_’s defensive abilities are unaffected.

**Relentless Tracker (Ex)** A _bandersnatch_ can move at up to double its speed and still track without penalty. It gains a +10 competence bonus on Survival checks made to track creatures it has wounded.

##### Description

Bandersnatches are consummate hunters, and only the deadliest predators or the most _[[items/Weapon Magic Abilities/Cunning|cunning]]_ intelligent prey offer them sport. Once a _bandersnatch_ has marked a creature for death, it runs it to ground without _fear_, rest, or remorse.

Bandersnatches rely on speed, _[[items/Weapon Magic Abilities/Shock|shock]]_, and terror to bring down prey. They pace their quarry from a distance, hidden among the trees, then break from cover, savage their target, and _[[items/Weapon/Dart|dart]]_ away again. They drag smaller creatures away to dispatch at leisure, while engaging larger ones in skirmishes until they gradually wear their prey down. An outmatched _bandersnatch_ withdraws at full speed, stopping only to pick off pursuers that distance themselves from their allies. Once its wounds _heal_, the _bandersnatch_ returns to the scene of its defeat, picks up the trail of its assailants, and eliminates them one by one.

In appearance, a _bandersnatch_ resembles a tawny, six-legged great cat, but with wickedly barbed quills running the length of its body and down to the tip of its long, flexible tail. Its quills serve to deter attackers, but also act as a formidable weapon. With a single flick of its muscular tail, a _bandersnatch_ can _[[feats/Fling|fling]]_ as many as a half-dozen quills at distant foes with surprising accuracy. A _bandersnatch_ captivates any prey that meets the _gaze_ of its saucerlike, luminous eyes. A _bandersnatch_ measures 40 feet in length plus another 10 feet of tail and weighs 12,000 pounds. Despite their bulk, bandersnatches move with speed, _grace_, and even considerable stealth when required.

Bandersnatches were once native to the primal world of the fey, where they preyed on the greatest hunters of that ancient realm. As with other legendary creatures from this realm, such as the _[[monsters/Jabberwock|jabberwock]]_, bandersnatches belong to a group of creatures known collectively as the “Tane.” Whether the fey were careless in _[[items/Armor Magic Abilities/Guarding|guarding]]_ their portals or released the first bandersnatches into Material Plane deliberately cannot be said with certainty. Rare in the extreme on the Material Plane, bandersnatches lair within forgotten forests where ancient beasts walk the world.

Bandersnatches mate only rarely. A female becomes fertile perhaps once or twice per century, leaving the male soon after mating and giving birth to only one or two kittens per litter. The mother brings meat to her _[[curses/Ravenous|ravenous]]_ young, which mature into lesser bandersnatches (see below) within a year. Bandersnatches live for a thousand years or longer.