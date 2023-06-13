---
cssclass: [monsters]
title1: Daemon, Leukodaemon
desc_short: 'This human-shaped beast has a horse's skull for a head. It walks on cracked
  hooves and bears the rotting wings of a carrion bird. '
title2: Leukodaemon
CR: 9
sources:
- name: Bestiary 2
  page: 68
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #8: Seven Days to the Grave'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy82qy
XP: 6400
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  deathwatch: true
  detect good: true
auras:
- name: infectious aura
  radius: 50
AC:
  AC: 23
  touch: 16
  flat_footed: 16
  components:
    dex: 7
    natural: 7
    size: -1
HP:
  HP: 115
  long: 10d10+60
saves:
  fort: 9
  ref: 14
  will: 12
DR:
- amount: 10
  weakness: good or silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 20
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +16 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: bite
      bonus:
      - 16
    - text: 2 claws +16 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 16
  ranged:
  - - text: +1 composite longbow +18/+13 (2d6+8/×3 plus contagion)
      entries:
      - - damage: 2d6+8
          crit_multiplier: 3
        - effect: contagion
      attack: +1 composite longbow
      bonus:
      - 18
      - 13
  special:
  - breath of flies
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: contagion
    source: default
    freq: At will
    DC: 17
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: harm
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: leukodaemon only
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 10
    concentration: 13
ability_scores:
  STR: 25
  DEX: 24
  CON: 23
  INT: 16
  WIS: 21
  CHA: 16
BAB: 10
CMB: 18
CMD: 35
feats:
- name: Alertness
- name: Hover
- name: Improved Initiative
- name: Point-Blank Shot
- name: Weapon Focus (longbow)
skills:
  Fly: 18
  Heal: 18
  Intimidate: 16
  Knowledge (planes): 16
  Perception: 22
  Sense Motive: 22
  Stealth: 16
  Survival: 15
  Use Magic Device: 16
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary or wake (2-10)
  treasure_type: standard
  treasure:
  - +1 composite longbow
  - other treasure
special_abilities:
  Breath of Flies (Su): Once per minute as a standard action, a leukodaemon can unleash
    a cloud of corpse-bloated, biting black flies in a 20-foot cone. Those caught
    in the cone take 8d6 points of slashing damage. A DC 21 Reflex save halves this
    damage. Those who take any damage are also sickened for 1 minute. In addition,
    the flies linger for 1d4+1 rounds, congealing into a buzzing 20-foot-square cloud
    centered on the cone's original point of origin. Any creature that ends its turn
    in this cloud must make a DC 21 Reflex save to avoid taking 4d6 points of damage
    and becoming sickened for 1 minute. This cloud of flies may be dispersed by any
    area effect that does damage or creates wind of at least strong wind force. All
    daemons are immune to this effect. The save DCs are Constitution-based.
  Contagion (Su): Any arrow a leukodaemon fires from a bow is tainted with disease.
    If a creature is damaged by a leukodaemon's arrow, it must make a DC 19 Fortitude
    save or be affected as if by the spell contagion. A leukodaemon can manifest arrows
    at will and never runs out of ammunition.
  Infectious Aura (Su): All creatures within 50 feet of a leukodaemon take a -4 penalty
    on Fortitude saves against disease effects.
desc_long: |-
  Deacons of the Horseman of Pestilence, leukodaemons serve their lord in Abaddon as well as across the planes by spreading plagues and pandemics. 

  Leukodaemons stand upward of 14 feet tall but weigh just over 200 pounds. The skulls that serve as their heads can be replaced with any skulls, yet these creatures choose horse skulls to show their loyalty to the Horsemen. The creature's true head is merely a blistered knob between its shoulders.

---

# Daemon, Leukodaemon
This human-shaped beast has a _[[monsters/Horse|horse]]_’s skull for a head. It walks on cracked hooves and bears the rotting wings of a carrion bird.

**Source** Bestiary 2 pg. 68, Pathfinder #8: Seven Days to the Grave pg. 80
**XP** 6,400

NE Large outsider (daemon, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/Detect Good|detect good]]_; Perception +22
**Aura** infectious aura (50 ft.)

##### Defense

**AC** 23, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+7 Dex, +7 natural, –1 size)
**hp** 115 (10d10+60)
**Fort** +9, **Ref** +14, **Will** +12
**DR** 10/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 20

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** bite +16 (1d8+7), 2 claws +16 (1d6+7)
**Ranged** +1 _[[items/Weapon/Composite longbow|composite longbow]]_ +18/+13 (2d6+8/×3 plus _[[spells/Contagion|contagion]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** breath of flies
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
Constant—_deathwatch_, _detect good_
At will—_contagion_ (DC 17), _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only)
1/day—_[[spells/Harm|harm]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 3, 1 leukodaemon only, 35%)

##### Statistics
**Str** 25, **Dex** 24, **Con** 23, **Int** 16, **Wis** 21, **Cha** 16
**Base Atk** +10; **CMB** +18; **CMD** 35
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_[[items/Weapon/Longbow|longbow]]_)
**Skills** Fly +18, _[[spells/Heal|Heal]]_ +18, Intimidate +16, Knowledge (planes) +16, Perception +22, Sense Motive +22, Stealth +16, Survival +15, Use Magic Device +16
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary or wake (2–10)
**Treasure** standard (+1 _composite longbow_, other treasure)

### Special Abilities

**Breath of Flies (Su)** Once per minute as a standard action, a leukodaemon can unleash a cloud of corpse-bloated, biting black flies in a 20-foot cone. Those caught in the cone take 8d6 points of slashing damage. A DC 21 Reflex save halves this damage. Those who take any damage are also _[[conditions/Sickened|sickened]]_ for 1 minute. In addition, the flies linger for 1d4+1 rounds, congealing into a buzzing 20-foot-square cloud centered on the cone’s original point of origin. Any creature that ends its turn in this cloud must make a DC 21 Reflex save to avoid taking 4d6 points of damage and becoming _sickened_ for 1 minute. This cloud of flies may be dispersed by any area effect that does damage or creates wind of at least strong wind force. All daemons are immune to this effect. The save DCs are Constitution-based.

**_Contagion_ (Su)** Any arrow a leukodaemon fires from a bow is tainted with disease. If a creature is damaged by a leukodaemon’s arrow, it must make a DC 19 Fortitude save or be affected as if by the spell _contagion_. A leukodaemon can manifest arrows at will and never runs out of ammunition.

**Infectious Aura (Su)** All creatures within 50 feet of a leukodaemon take a –4 penalty on Fortitude saves against disease effects.

##### Description

Deacons of the Horseman of Pestilence, leukodaemons serve their lord in Abaddon as well as across the planes by spreading plagues and pandemics.

Leukodaemons stand upward of 14 feet tall but weigh just over 200 pounds. The skulls that serve as their heads can be replaced with any skulls, yet these creatures choose _horse_ skulls to show their loyalty to the Horsemen. The creature’s true head is merely a blistered knob between its shoulders.