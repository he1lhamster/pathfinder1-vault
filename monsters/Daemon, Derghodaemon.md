---
cssclass: [monsters]
title1: Daemon, Derghodaemon
desc_short: 'A deadly and vicious bouquet of insectile claws sprouts from this horrid,
  three-legged, multi-eyed beast. '
title2: Derghodaemon
CR: 12
sources:
- name: Bestiary 2
  page: 66
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 19200
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  all-around vision: true
  darkvision: 60
  detect magic: true
  see invisibility: true
auras:
- name: feeblemind
  DC: 20
AC:
  AC: 27
  touch: 14
  flat_footed: 22
  components:
    dex: 5
    natural: 13
    size: -1
HP:
  HP: 161
  long: 14d10+84
saves:
  fort: 15
  ref: 14
  will: 7
DR:
- amount: 10
  weakness: good
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 23
speeds:
  base: 40
attacks:
  melee:
  - - text: 5 claws +21 (1d6+8/19-20)
      entries:
      - - damage: 1d6+8
          crit_range: 19-20
      count: 5
      attack: claws
      bonus:
      - 21
  special:
  - rend (2 claws, 1d8+12 plus 2 Con damage)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: fear
    source: default
    freq: 3/day
    DC: 17
  - name: quickened summon swarm
    source: default
    freq: 3/day
  - name: creeping doom
    source: default
    freq: 1/day
  - name: insect plague
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: derghodaemon
      amount: 1
      chance: 30%
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 27
  DEX: 20
  CON: 22
  INT: 7
  WIS: 17
  CHA: 16
BAB: 14
CMB: 23
CMD: 38
CMD_other: 40 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Improved Critical (claws)
- name: Power Attack
- name: Quicken Spell-Like Ability (summon swarm)
- name: Sickening Critical
- name: Vital Strike
skills:
  Intimidate: 20
  Perception: 28
  Sense Motive: 20
  Stealth: 18
  _racial_mods:
    Perception:
      _: 4
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- swarmwalking
ecology:
  environment: any (Abaddon)
  organization: solitary or infestation (2-6)
  treasure_type: standard
special_abilities:
  Feeblemind Aura (Su): By grinding and clicking its mandibles and chitinous plates
    together (a free action), a derghodaemon can affect all creatures within 30 feet
    as if by a feeblemind spell. Daemons are immune to this effect, but all other
    creatures must make a DC 20 Will save to resist the effects. A creature that makes
    this save is immune to the effect for 24 hours. A creature that fails remains
    affected as long as the derghodaemon continues to maintain the aura and the subject
    remains within 30 feet of the derghodaemon. Once either condition ends, the victim
    of this effect can attempt a new DC 20 Will save once per minute to recover from
    the effect; otherwise, it can be cured by a heal, limited wish, miracle, or wish
    spell. A derghodaemon cannot use its spell-like abilities or rend attack in any
    round in which it uses its feeblemind aura. This is a sonic mind-affecting effect.
    The save DC is Charisma-based.
  Swarmwalking (Su): A derghodaemon is immune to damage or distraction effects caused
    by swarms.
desc_long: |-
  These brutal daemons personify death resulting from violent insanity, such as being murdered by a maniac or torn to shreds by a pack of rabid predators. These insectoid creatures roam the Outer Planes, scavenging battlefields and following the inevitable trail of violence in those hostile worlds. They hunt the weak and dying along the fringe of battles, feeding off their victims' suffering until they make their kill. Attacks from a derghodaemon often come from within a cloud of biting insects. 

  Brutish and low on intellect, derghodaemons find themselves serving as front-line fighters in fiendish armies. A derghodaemon stands 9 feet tall and weighs 800 pounds.

---

# Daemon, Derghodaemon
A _[[items/Weapon Magic Abilities/Deadly|deadly]]_ and _[[items/Weapon Magic Abilities/Vicious|vicious]]_ bouquet of insectile claws sprouts from this horrid, three-legged, multi-eyed beast.

**Source** Bestiary 2 pg. 66
**XP** 19,200

NE Large outsider (daemon, evil, extraplanar)
**Init** +5; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +28
**Aura** _[[spells/Feeblemind|feeblemind]]_ (DC 20)

##### Defense

**AC** 27, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+5 Dex, +13 natural, –1 size)
**hp** 161 (14d10+84)
**Fort** +15, **Ref** +14, **Will** +7
**DR** 10/good; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 23

##### Offense
**Speed** 40 ft.
**Melee** 5 claws +21 (1d6+8/19–20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 claws, 1d8+12 plus 2 Con damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
Constant—_detect magic_, _see invisibility_
At will—greater teleport (self plus 50 lbs. of objects only)
3/day—_[[universal monster rules/Fear|fear]]_ (DC 17), quickened _[[spells/Summon Swarm|summon swarm]]_
1/day—_[[spells/Creeping Doom|creeping doom]]_, _[[spells/Insect Plague|insect plague]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 derghodaemon 30%)

##### Statistics
**Str** 27, **Dex** 20, **Con** 22, **Int** 7, **Wis** 17, **Cha** 16
**Base Atk** +14; **CMB** +23; **CMD** 38 (40 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_summon swarm_), _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Intimidate +20, Perception +28, Sense Motive +20, Stealth +18; **Racial Modifiers** +4 Perception
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** swarmwalking

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary or infestation (2–6)
**Treasure** standard

### Special Abilities

**_Feeblemind_ Aura (Su) **By _[[items/Armor Magic Abilities/Grinding|grinding]]_ and clicking its mandibles and chitinous plates together (a free action), a derghodaemon can affect all creatures within 30 feet as if by a _feeblemind_ spell. Daemons are immune to this effect, but all other creatures must make a DC 20 Will save to resist the effects. A creature that makes this save is immune to the effect for 24 hours. A creature that fails remains affected as long as the derghodaemon continues to maintain the aura and the subject remains within 30 feet of the derghodaemon. Once either condition ends, the victim of this effect can attempt a new DC 20 Will save once per minute to recover from the effect; otherwise, it can be cured by a _[[spells/Heal|heal]]_, _[[spells/Limited Wish|limited wish]]_, _[[spells/Miracle|miracle]]_, or _[[spells/Wish|wish]]_ spell. A derghodaemon cannot use its _spell-like abilities_ or _rend_ attack in any round in which it uses its _feeblemind_ aura. This is a sonic mind-affecting effect. The save DC is Charisma-based.
**Swarmwalking (Su)** A derghodaemon is immune to damage or _[[universal monster rules/Distraction|distraction]]_ effects caused by swarms.

##### Description

These brutal daemons personify death resulting from violent _[[spells/Insanity|insanity]]_, such as being murdered by a maniac or torn to shreds by a pack of rabid predators. These insectoid creatures roam the Outer Planes, scavenging battlefields and following the inevitable trail of violence in those hostile worlds. They hunt the weak and _[[conditions/Dying|dying]]_ along the fringe of battles, feeding off their victims’ suffering until they make their kill. Attacks from a derghodaemon often come from within a cloud of biting insects.

Brutish and low on intellect, derghodaemons find themselves serving as front-line fighters in fiendish armies. A derghodaemon stands 9 feet tall and weighs 800 pounds.