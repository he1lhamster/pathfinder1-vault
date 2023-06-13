---
cssclass: [monsters]
title1: Herald, Tarrasque
desc_short: This immense reptilian beast towers over its surroundings, all teeth and
  horns and claws and thrashing spiked tail.
title2: Tarrasque
CR: 25
sources:
- name: Inner Sea Gods
  page: 304
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
- name: Pathfinder RPG Bestiary
  page: 262
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 1638400
alignment: CE
size: Colossal
type: magical beast
subtypes:
- spawn of Rovagug [see page 275]
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: frightful presence
  radius: 300
  DC: 27
AC:
  AC: 40
  touch: 5
  flat_footed: 37
  components:
    dex: 3
    natural: 35
    size: -8
HP:
  HP: 525
  long: 30d10+360
  regeneration: 40
saves:
  fort: 31
  ref: 22
  will: 12
DR:
- amount: 15
  weakness: epic
immunities:
- ability damage
- ability drain
- acid
- bleed
- disease
- energy drain
- fire
- mind-affecting effects
- paralysis
- permanent wounds
- petrification
- poison
- polymorph
SR: 36
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +37 (4d8+15/15-20/×3 plus grab)
      entries:
      - - damage: 4d8+15
          crit_range: 15-20
          crit_multiplier: 3
        - effect: grab
      attack: bite
      bonus:
      - 37
    - text: 2 claws +37 (1d12+15)
      entries:
      - - damage: 1d12+15
      count: 2
      attack: claws
      bonus:
      - 37
    - text: 2 gores +37 (1d10+15)
      entries:
      - - damage: 1d10+15
      count: 2
      attack: gores
      bonus:
      - 37
    - text: tail slap +32 (3d8+7)
      entries:
      - - damage: 3d8+7
      attack: tail slap
      bonus:
      - 32
  ranged:
  - - text: 6 spines +25 (2d10+15/×3)
      entries:
      - - damage: 2d10+15
          crit_multiplier: 3
      count: 6
      attack: spines
      bonus:
      - 25
  special:
  - rush
  - spines
  - swallow whole (6d6+22 plus 6d6 acid, AC 27, hp 52)
space: 30
reach: 30
reach_other: 60 ft. with tail slap
ability_scores:
  STR: 41
  DEX: 16
  CON: 34
  INT: 3
  WIS: 15
  CHA: 14
BAB: 30
CMB: 53
CMB_other: +57 grapple
CMD: 66
feats:
- name: Awesome Blow
- name: Blind-Fight
- name: Bleeding Critical
- name: Cleave
- name: Combat Reflexes
- name: Critical Focus
- name: Great Cleave
- name: Great Fortitude
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Run
- name: Staggering Critical
skills:
  Acrobatics: 3
    when jumping: 43
  Perception: 43
  _racial_mods:
    Perception:
      _: 8
languages:
- Aklo (can't speak)
special_qualities:
- carapace
- hibernation
- powerful leaper
- unstoppable force
ecology:
  environment: any
  organization: solitary
  treasure_type: none
special_abilities:
  Carapace (Su): The tarrasque's scales deflect cones, lines, rays, and magic missile
    spells, rendering the tarrasque immune to such effects. There is a 30% chance
    a deflected effect reflects back in full force at the caster; otherwise it is
    simply negated.
  Powerful Leaper (Ex): The tarrasque uses its Strength to modify Acrobatics checks
    made to jump, and has a +24 racial bonus on Acrobatics checks made to jump.
  Rush (Ex): Once per minute, for 1 round, the tarrasque's speed increases to 150
    feet, and its Acrobatics bonus on checks made to jump increases to +87.
  Spines (Ex): The tarrasque can loose a volley of six spear-like spines from its
    body as a standard action with a toss of its head or a lash of its tail. Make
    an attack roll for each spine- all targets must be within 30 feet of each other.
    The spines have a range increment of 120 ft.
desc_long: |-
  The Tarrasque, referred to in ancient texts as the “Armageddon Engine,” is the greatest of Rovagug's spawn. Its previously recorded devastation of Ninshabur and Avistan occurred in -632 AR, and culminated in the destruction of the flying Shory city of Kho. It was sealed away in a cavern somewhere in the Inner Sea region. Although the location of this cavern has been lost, rumors of possible locations include nearly every mountainous region, the Mwangi Expanse, and even under the Isle of Kortos itself.

  The statistics presented here for the Tarrasque differ slightly from those in the Bestiary-this version more accurately represents the Tarrasque as the mightiest of Rovagug's spawn.

---

# Herald, Tarrasque
This immense reptilian beast towers over its surroundings, all teeth and horns and claws and thrashing spiked tail.
**Source** Inner Sea Gods pg. 304, Pathfinder RPG Bestiary pg. 262
**XP** 1,638,400
CE Colossal magical beast (spawn of Rovagug [see page 275])
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +43
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 27)

##### Defense

**AC** 40, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+3 Dex, +35 natural, –8 size)
**hp** 525 (30d10+360); _[[universal monster rules/Regeneration|regeneration]]_ 40
**Fort** +31, **Ref** +22, **Will** +12
**DR** 15/epic; **Immune** ability damage, ability drain, acid, _[[universal monster rules/Bleed|bleed]]_, disease, _[[universal monster rules/Energy Drain|energy drain]]_, fire, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, permanent wounds, petrification, poison, _[[spells/Polymorph|polymorph]]_; **SR** 36

##### Offense
**Speed** 40 ft.
**Melee** bite +37 (4d8+15/15–20/×3 plus _[[universal monster rules/Grab|grab]]_), 2 claws +37 (1d12+15), 2 gores +37 (1d10+15), tail slap +32 (3d8+7)
**Ranged** 6 spines +25 (2d10+15/×3)
**Space** 30 ft., **Reach** 30 ft. (60 ft. with tail slap)
**Special Attacks** rush, spines, _[[universal monster rules/Swallow Whole|swallow whole]]_ (6d6+22 plus 6d6 acid, AC 27, hp 52)

##### Statistics
**Str** 41, **Dex** 16, **Con** 34, **Int** 3, **Wis** 15, **Cha** 14
**Base Atk** +30; **CMB** +53 (+57 grapple); **CMD** 66
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, Run, _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Acrobatics +3 (+43 when jumping), Perception +43; **Racial Modifiers** +8 Perception
**Languages** Aklo (can’t speak)
**SQ** carapace, hibernation, powerful leaper, unstoppable force

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

### Special Abilities

**Carapace (Su)** The tarrasque’s scales deflect cones, lines, rays, and _[[spells/Magic Missile|magic missile]]_ spells, rendering the tarrasque immune to such effects. There is a 30% chance a deflected effect reflects back in full force at the caster; otherwise it is simply negated.

**Powerful Leaper (Ex)** The tarrasque uses its Strength to modify Acrobatics checks made to _[[spells/Jump|jump]]_, and has a +24 racial bonus on Acrobatics checks made to _jump_.

**Rush (Ex)** Once per minute, for 1 round, the tarrasque’s speed increases to 150 feet, and its Acrobatics bonus on checks made to _jump_ increases to +87.
**Spines (Ex)** The tarrasque can loose a volley of six spear-like spines from its body as a standard action with a toss of its head or a lash of its tail. Make an attack roll for each spine— all targets must be within 30 feet of each other. The spines have a range increment of 120 ft.

##### Description

The Tarrasque, referred to in ancient texts as the “Armageddon Engine,” is the greatest of Rovagug’s spawn. Its previously recorded devastation of Ninshabur and Avistan occurred in –632 AR, and culminated in the _[[spells/Destruction|destruction]]_ of the flying Shory city of Kho. It was sealed away in a cavern somewhere in the Inner Sea region. Although the location of this cavern has been lost, rumors of possible locations include nearly every mountainous region, the Mwangi Expanse, and even under the Isle of Kortos itself.

The statistics presented here for the Tarrasque differ slightly from those in the Bestiary—this version more accurately represents the Tarrasque as the mightiest of Rovagug’s spawn.