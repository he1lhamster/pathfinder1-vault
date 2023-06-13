---
cssclass: [monsters]
title1: Demon, Kithangian
desc_short: 'This creature combines the features of a scorpion and a horse- slavering
  humanoid faces peer from between its two pincers. '
title2: Kithangian
CR: 9
sources:
- name: The Worldwound
  page: 47
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 6400
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 60
  all-around vision: true
AC:
  AC: 25
  touch: 9
  flat_footed: 25
  components:
    natural: 16
    size: -1
HP:
  HP: 115
  long: 11d10+55
saves:
  fort: 12
  ref: 9
  will: 7
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- fear
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 20
speeds:
  base: 50
attacks:
  melee:
  - - text: 2 claws +16 (1d6+6/19-20 plus grab)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 16
    - text: 2 stings +16 (1d6+6/19-20 plus poison)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
        - effect: poison
      count: 2
      attack: stings
      bonus:
      - 16
  special:
  - hatred
  - rasping tongues
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: Constant
  - name: hold animal
    source: default
    freq: At will
    DC: 15
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - superscripts:
    - UM
    name: unnatural lust
    source: default
    freq: At will
    DC: 14
  - name: air walk
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: quickened unnatural lust
    source: default
    freq: 3/day
    DC: 14
  - name: baleful polymorph
    source: default
    freq: 1/day
    DC: 18
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: kithangian
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 22
  DEX: 11
  CON: 20
  INT: 7
  WIS: 19
  CHA: 16
BAB: 11
CMB: 18
CMB_other: +22 grapple
CMD: 28
feats:
- name: Improved Critical (claw)
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (unnatural lust)
skills:
  Handle Animal: 17
  Intimidate: 17
  Perception: 18
  Stealth: 10
languages:
- Abyssal
- Celestial
- Draconic
- speak with animals
- telepathy 100 ft.
special_qualities:
- change shape (beast shape II, Medium or Large animal)
- swift transformation
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or pack (3-8)
  treasure_type: standard
special_abilities:
  Hatred (Ex): A kithangian gains a +2 bonus on all attack rolls and damage rolls
    made against all creatures of the animal type. In addition, animals take a -2
    penalty on all saving throws against a kithangian's supernatural or spell-like
    abilities.
  Poison (Ex): Sting-injury; save Fort DC 20; frequency 1/round for 6 rounds; effect
    1d4 Str plus nauseated; cure 2 consecutive saves.
  Rasping Tongues (Su): The faces between a kithangian's claws have long rasping tongues
    covered with tiny teeth. Whenever a kithangian successfully grapples a foe with
    its claws, a rasping tongue slithers out from the face within and burrows into
    the creature's body. Each round that the creature is grappled, it takes 1d6 points
    of damage and 1d4 points of Charisma damage as its sense of self-identity is warped
    and twisted. A successful DC 18 Will save negates the Charisma damage. The save
    DC is Charisma-based.
  Swift Transformation (Su): A kithangian can use its change shape ability as a swift
    action.
desc_long: Kithangians, also known as beast demons, are reprehensible monstrosities
  born from the souls of those who abused and tormented animals in life. Universally
  male, the sudden spread of fiendish elements through within an area's fauna is a
  sure indication of a kithangian's presence in a region. The fact that most creatures
  that birth litters of young with the half-fiendish template die in the process is
  of little concern to the kithangian, for it merely moves on to new hunting grounds
  when uncorrupted animal victims grow too rare.

---

# Demon, Kithangian
This creature combines the features of a scorpion and a _[[monsters/Horse|horse]]_—
slavering humanoid faces peer from between its two pincers.

**Source** The Worldwound pg. 47
**XP** 6,400
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/All-Around Vision|all-around vision]]_; Perception +18

##### Defense

**AC** 25, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+16 natural, –1 size)
**hp** 115 (11d10+55)
**Fort** +12, **Ref** +9, **Will** +7
**DR** 10/good; **Immune** electricity, _[[universal monster rules/Fear|fear]]_, poison; **Resist** acid 10,
cold 10, fire 10; **SR** 20

##### Offense
**Speed** 50 ft.
**Melee** 2 claws +16 (1d6+6/19–20 plus _[[universal monster rules/Grab|grab]]_), 2 stings +16
(1d6+6/19–20 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** hatred, rasping _[[spells/Tongues|tongues]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
Constant—_[[spells/Speak with Animals|speak with animals]]_
At will—_[[spells/Hold Animal|hold animal]]_ (DC 15), greater teleport (self plus
 50 lbs. of objects only), _[[spells/Unnatural Lust|unnatural lust]]_ (DC 14)
3/day—_[[spells/Air Walk|air walk]]_, quickened _unnatural lust_ (DC 14)
1/day—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 18), _[[universal monster rules/Summon|summon]]_ (level 3,
 1 kithangian 35%)

##### Statistics
**Str** 22, **Dex** 11, **Con** 20, **Int** 7, **Wis** 19, **Cha** 16
**Base Atk** +11; **CMB** +18 (+22 grapple); **CMD** 28
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (claw), _Improved Critical_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_unnatural lust_)
**Skills** Handle Animal +17, Intimidate +17, Perception +18,
Stealth +10
**Languages** Abyssal, Celestial, Draconic; _speak with animals_,
_[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Beast Shape II|beast shape II]]_, Medium or Large animal),
swift _[[spells/Transformation|transformation]]_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or pack (3–8)
**Treasure** standard

### Special Abilities

**Hatred (Ex)** A kithangian gains a +2 bonus on all attack rolls and
damage rolls made against all creatures of the animal type.
In addition, animals take a –2 penalty on all saving throws
against a kithangian’s supernatural or _spell-like abilities_.

**Poison (Ex)** Sting—injury; save Fort DC 20; frequency 1/round for
 6 rounds; effect 1d4 Str plus _[[conditions/Nauseated|nauseated]]_; cure 2 consecutive saves.

**Rasping _Tongues_ (Su)** The faces between a kithangian’s
claws have long rasping _tongues_ covered with tiny teeth.
Whenever a kithangian successfully grapples a foe with its
claws, a rasping tongue slithers out from the face within
and burrows into the creature’s body. Each round that the
creature is _[[conditions/Grappled|grappled]]_, it takes 1d6 points of damage and 1d4
points of Charisma damage as its sense of self-identity is
warped and twisted. A successful DC 18 Will save negates
the Charisma damage. The save DC is Charisma-based.
**Swift _Transformation_ (Su)** A kithangian can use its change
shape ability as a swift action.

##### Description

Kithangians, also known as beast demons, are reprehensible
monstrosities born from the souls of those who abused
and tormented animals in life. Universally male, the
sudden spread of fiendish elements through within an
area’s fauna is a sure indication of a kithangian’s presence in
a region. The fact that most creatures that birth litters of
young with the half-fiendish template die in the process
is of little concern to the kithangian, for it merely moves
on to new hunting grounds when uncorrupted animal
victims grow too rare.