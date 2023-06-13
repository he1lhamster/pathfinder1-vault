---
cssclass: [monsters]
title1: Daemon, Temerdaemon
desc_short: This humanoid creature's limbs-four arms and four legs-bend in awkward
  configurations. It wields a scythe in its largest arms.
title2: Temerdaemon
CR: 14
sources:
- name: Bestiary 6
  page: 77
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 3: Horsemen of the Apocalypse'
  page: 58
  link: http://paizo.com/products/btpy8odg?Pathfinder-Campaign-Setting-Book-of-the-Damned-Volume-3-Horsemen-of-the-Apocalypse
XP: 38400
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
auras:
- name: reaper's curse
  radius: 30
  DC: 23
  duration: 10 rounds
AC:
  AC: 29
  touch: 15
  flat_footed: 23
  components:
    dex: 6
    natural: 14
    size: -1
HP:
  HP: 195
  long: 17d10+102
saves:
  fort: 16
  ref: 13
  will: 17
DR:
- amount: 10
  weakness: good and silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 25
speeds:
  base: 30
  other_semicolon: air walk
attacks:
  melee:
  - - text: +1 scythe +23/+18/+13/+8 (2d4+8/19-20/×4 plus confusion)
      entries:
      - - damage: 2d4+8
          crit_range: 19-20
          crit_multiplier: 4
        - effect: confusion
      attack: +1 scythe
      bonus:
      - 23
      - 18
      - 13
      - 8
    - text: 2 claws +16 (1d4+2 plus confusion)
      entries:
      - - damage: 1d4+2
        - effect: confusion
      count: 2
      attack: claws
      bonus:
      - 16
  special:
  - confusion
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: bestow curse
    source: default
    freq: At will
    DC: 19
  - name: death knell
    source: default
    freq: At will
    DC: 17
  - name: gaseous form
    source: default
    freq: At will
  - name: passwall
    source: default
    freq: At will
  - name: stone shape
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: disintegrate
    source: default
    freq: 3/day
    DC: 21
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: illusory wall
    source: default
    freq: 3/day
    DC: 19
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: temerdaemon
      amount: 1
      chance: 30%
  sources:
  - name: default
    CL: 15
    concentration: 20
ability_scores:
  STR: 21
  DEX: 22
  CON: 23
  INT: 13
  WIS: 24
  CHA: 20
BAB: 17
CMB: 23
CMB_other: +25 trip
CMD: 39
CMD_other: 45 vs. trip
feats:
- name: Blinding Critical
- name: Combat Expertise
- name: Critical Focus
- name: Improved Critical (scythe)
- name: Improved Initiative
- name: Improved Trip
- name: Lightning Reflexes
- name: Power Attack
- name: Weapon Focus (scythe)
skills:
  Bluff: 25
  Intimidate: 25
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 27
  Sense Motive: 27
  Stealth: 22
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- undersized weapons
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or trapper gang (3 temerdaemons and 10-16 cacodaemons)
  treasure_type: standard
  treasure:
  - +1 scythe
  - other treasure
special_abilities:
  Confusion (Su): A creature struck in combat by a temerdaemon's melee attacks must
    succeed at a DC 23 Will save or be confused for 1 round. The durations from multiple
    strikes and failed saving throws stack. This is a mind-affecting effect. The save
    DC is Charisma-based.
  Reaper's Curse (Su): Creatures within 30 feet of a temerdaemon are afflicted by
    a profound increase in self-inflicted and allyinflicted wounds, failures in magic,
    and similar accidental damage. Arcane spell failure chances from armor are doubled.
    A creature that rolls a natural 1 on its attack roll automatically rerolls the
    attack against itself or an ally (50% chance of either). A creature that rolls
    a natural 1 on its roll to cast defensively suffers a mishap (see Scroll Mishaps
    on page 491 of the Pathfinder RPG Core Rulebook). Skill checks that have consequences
    if failed by 5 or more (such as Climb, Disable Device, and Swim) have these consequences
    on all failed checks
desc_long: |-
  Temerdaemons exist to personify accidental death. A knight falls onto her sword; a peasant trips and breaks his neck; a structure fails in ways its builders never foresaw and buries dozens of innocents- and a temerdaemon cackles knowingly in the distance. While true accidents please the fiend, it also delights in engineering incomprehensibly complex plots that lead to the slaughter of as many mortals as possible. A temerdaemon often wades into the aftermath of such catastrophes, carving apart survivors and sowing mass confusion and hysteria. 

  Temerdaemons only rarely cooperate among themselves, but a trio of them sometimes forms a “trapper gang” to pursue common goals. 

  A gangly mass consisting of a rotund torso, four arms, and four legs, a temerdaemon is 10 feet long and weighs 1,200 pounds, not counting its often bizarre collection of odd mechanical fetishes and other tinkering equipment.

---

# Daemon, Temerdaemon
This humanoid creature’s limbs—four arms and four legs—bend in awkward configurations. It wields a _[[items/Weapon/Scythe|scythe]]_ in its largest arms.
**Source** Bestiary 6 pg. 77, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 3: Horsemen of the Apocalypse pg. 58
**XP** 38,400

NE Large outsider (daemon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +27
**Aura** reaper’s curse (30 ft., DC 23, 10 rounds)

##### Defense

**AC** 29, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+6 Dex, +14 natural, –1 size)
**hp** 195 (17d10+102)
**Fort** +16, **Ref** +13, **Will** +17
**DR** 10/good and silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 25

##### Offense
**Speed** 30 ft.; _[[spells/Air Walk|air walk]]_
**Melee** +1 _scythe_ +23/+18/+13/+8 (2d4+8/19–20/×4 plus _[[spells/Confusion|confusion]]_), 2 claws +16 (1d4+2 plus _confusion_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _confusion_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Passwall|passwall]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 20) 
3/day—_[[spells/Disintegrate|disintegrate]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Illusory Wall|illusory wall]]_ (DC 19), _[[spells/Suggestion|suggestion]]_ (DC 18) 
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 temerdaemon 30%)

##### Statistics
**Str** 21, **Dex** 22, **Con** 23, **Int** 13, **Wis** 24, **Cha** 20
**Base Atk** +17; **CMB** +23 (+25 _[[universal monster rules/Trip|trip]]_); **CMD** 39 (45 vs. _trip_)
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Bluff +25, Intimidate +25, Knowledge (planes, religion) +21, Perception +27, Sense Motive +27, Stealth +22
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or trapper gang (3 temerdaemons and 10–16 cacodaemons)
**Treasure** standard (+1 _scythe_, other treasure)

### Special Abilities

**_Confusion_ (Su)** A creature struck in combat by a temerdaemon’s melee attacks must succeed at a DC 23 Will save or be _[[conditions/Confused|confused]]_ for 1 round. The durations from multiple strikes and failed saving throws stack. This is a mind-affecting effect. The save DC is Charisma-based.

**Reaper’s Curse (Su)** Creatures within 30 feet of a temerdaemon are afflicted by a profound increase in self-inflicted and allyinflicted wounds, failures in magic, and similar accidental damage. Arcane spell failure chances from armor are doubled. A creature that rolls a natural 1 on its attack roll automatically rerolls the attack against itself or an ally (50% chance of either). A creature that rolls a natural 1 on its roll to cast defensively suffers a mishap (see Scroll Mishaps on page 491 of the Pathfinder RPG Core Rulebook). Skill checks that have consequences if failed by 5 or more (such as _[[universal monster rules/Climb|Climb]]_, Disable Device, and Swim) have these consequences on all failed checks

##### Description

Temerdaemons exist to personify accidental death. A _[[npcs/Knight|knight]]_ falls onto her sword; a peasant trips and breaks his neck; a structure fails in ways its builders never foresaw and buries dozens of innocents— and a temerdaemon cackles knowingly in the distance. While true accidents please the fiend, it also delights in engineering incomprehensibly complex plots that lead to the slaughter of as many mortals as possible. A temerdaemon often wades into the aftermath of such catastrophes, carving apart survivors and sowing mass _confusion_ and hysteria.

Temerdaemons only rarely cooperate among themselves, but a trio of them sometimes forms a “trapper gang” to pursue common goals.

A gangly mass consisting of a rotund torso, four arms, and four legs, a temerdaemon is 10 feet long and weighs 1,200 pounds, not counting its often bizarre collection of odd mechanical fetishes and other tinkering equipment.