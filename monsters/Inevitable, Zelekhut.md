---
cssclass: [monsters]
title1: Inevitable, Zelekhut
desc_short: This creature looks like a mechanical centaur. Golden, clockwork wings
  sprout from its back, and its arms end in barbed chains.
title2: Zelekhut
CR: 9
sources:
- name: Bestiary 2
  page: 167
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 6400
alignment: LN
size: Large
type: outsider
subtypes:
- extraplanar
- inevitable
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 24
  touch: 15
  flat_footed: 18
  components:
    dex: 5
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 115
  long: 10d10+60
  regeneration: 5
  regeneration_weakness: chaotic
saves:
  fort: 10
  ref: 8
  will: 10
defensive_abilities:
- constructed
DR:
- amount: 10
  weakness: chaotic
SR: 20
speeds:
  base: 50
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 chains +17 (2d6+7 plus 1d6 electricity and trip)
      entries:
      - - damage: 2d6+7
        - damage: 1d6
          type: electricity
        - effect: trip
      count: 2
      attack: chains
      bonus:
      - 17
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - name: dimensional anchor
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: fear
    source: default
    freq: At will
    DC: 17
  - name: hold person
    source: default
    freq: At will
    DC: 16
  - name: locate creature
    source: default
    freq: At will
  - name: hold monster
    source: default
    freq: 3/day
    DC: 18
  - name: mark of justice
    source: default
    freq: 3/day
  - name: lesser geas
    source: default
    freq: 1/week
    DC: 17
  sources:
  - name: default
    CL: 10
    concentration: 13
ability_scores:
  STR: 25
  DEX: 20
  CON: 16
  INT: 10
  WIS: 17
  CHA: 17
BAB: 10
CMB: 18
CMD: 34
CMD_other: 38 vs. trip
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Weapon Focus (chain)
- name: Vital Strike
skills:
  Acrobatics: 18
    jump: 26
  Diplomacy: 16
  Fly: 16
  Perception: 20
  Sense Motive: 20
  Survival: 16
  _racial_mods:
    Perception:
      _: 4
    Sense Motive:
      _: 4
languages:
- truespeech
special_qualities:
- chains
ecology:
  environment: any land (lawful plane)
  organization: solitary
  treasure_type: none
special_abilities:
  Chains (Ex): A zelekhut's arms end in long lengths of barbed metal. These chains
    deal slashing damage and 1d6 points of electricity damage with each hit.
desc_long: |-
  Zelekhuts are bounty hunters and executioners all rolled into one. They seek out those beings who continually evade justice-either through active flight, or through power and station-and bring law and justice to the multiverse's most notorious fugitives and criminals.

  Ironically, while zelekhuts are implacable and unrelenting in their duty, they have little interest in passing judgment of their own, a fact that often confuses other races. Rather, a zelekhut is content to enforce the laws of any given society, and while it might hunt a condemned serial killer or notorious thief across half a dozen planes, it will not shift a single hoof to capture a corrupt ruler whose offenses are 10 times worse, so long as the atrocities are within her technical rights as ruler. All zelekhuts understand that laws can and must differ from place to place, and it is not the zelekhut's job to moralize, merely to track down those who seek to flee their punishment.

---

# Inevitable, Zelekhut
This creature looks like a mechanical _[[monsters/Centaur|centaur]]_. Golden, clockwork wings sprout from its back, and its arms end in _[[spells/Barbed Chains|barbed chains]]_.
**Source** Bestiary 2 pg. 167
**XP** 6,400

LN Large outsider (extraplanar, inevitable, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +20

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 Dex, +1 dodge, +9 natural, –1 size)
**hp** 115 (10d10+60); _[[universal monster rules/Regeneration|regeneration]]_ 5 (chaotic)
**Fort** +10, **Ref** +8, **Will** +10
**Defensive Abilities** constructed; **DR** 10/chaotic; **SR** 20

##### Offense
**Speed** 50 ft., fly 60 ft. (average)
**Melee** 2 chains +17 (2d6+7 plus 1d6 electricity and _[[universal monster rules/Trip|trip]]_)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
Constant—_true seeing_
At will—clairaudience/clairvoyance, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[universal monster rules/Fear|fear]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Locate Creature|locate creature]]_
3/day—_[[spells/Hold Monster|hold monster]]_ (DC 18), _[[spells/Mark of Justice|mark of justice]]_
1/week—lesser geas (DC 17)

##### Statistics
**Str** 25, **Dex** 20, **Con** 16, **Int** 10, **Wis** 17, **Cha** 17
**Base Atk** +10; **CMB** +18; **CMD** 34 (38 vs. _trip_)
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (chain), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +18 (+26 _[[spells/Jump|jump]]_), Diplomacy +16, Fly +16, Perception +20, Sense Motive +20, Survival +16; **Racial Modifiers** +4 Perception, +4 Sense Motive
**Languages** truespeech
**SQ** chains

##### Ecology

**Environment** any land (lawful plane)
**Organization** solitary
**Treasure** none

### Special Abilities

**Chains (Ex) **A zelekhut’s arms end in long lengths of barbed metal. These chains deal slashing damage and 1d6 points of electricity damage with each hit.

##### Description

Zelekhuts are bounty hunters and executioners all rolled into one. They seek out those beings who continually evade justice—either through active _[[universal monster rules/Flight|flight]]_, or through power and station—and bring law and justice to the multiverse’s most notorious fugitives and criminals.

Ironically, while zelekhuts are implacable and unrelenting in their duty, they have little interest in passing judgment of their own, a fact that often confuses other races. Rather, a zelekhut is content to enforce the laws of any given society, and while it might hunt a condemned serial killer or notorious thief across half a dozen planes, it will not shift a single hoof to capture a corrupt ruler whose offenses are 10 times worse, so long as the atrocities are within her technical rights as ruler. All zelekhuts understand that laws can and must differ from place to place, and it is not the zelekhut’s job to moralize, merely to track down those who seek to flee their punishment.