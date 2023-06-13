---
cssclass: [monsters]
title1: Kraken
desc_short: This tremendous leviathan resembles a vast squid, yet the markings on
  its body are strangely unsettling to look upon.
title2: Kraken
CR: 18
sources:
- name: Pathfinder RPG Bestiary
  page: 184
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 153600
alignment: NE
size: Gargantuan
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 4
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 32
  touch: 6
  flat_footed: 32
  components:
    natural: 26
    size: -4
HP:
  HP: 290
  long: 20d10+180
saves:
  fort: 21
  ref: 12
  will: 11
immunities:
- cold
- mind-affecting effects
- poison
speeds:
  base: 10
  swim: 40
  jet: 280
attacks:
  melee:
  - - text: 2 arms +26 (2d6+10/19-20 plus grab)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: arms
      bonus:
      - 26
    - text: 8 tentacles +24 (1d8+5 plus grab)
      entries:
      - - damage: 1d8+5
        - effect: grab
      count: 8
      attack: tentacles
      bonus:
      - 24
    - text: bite +26 (2d8+10)
      entries:
      - - damage: 2d8+10
      attack: bite
      bonus:
      - 26
  special:
  - constrict (tentacles, 1d8+10)
  - ink cloud
  - rend ship
space: 20
reach: 20
reach_other: 60 ft. with arm, 40 ft. with tentacle
spell_like_abilities:
  entries:
  - name: control weather
    source: default
    freq: 1/day
  - name: control winds
    source: default
    freq: 1/day
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 24
    other: animal only
  - name: resist energy
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 15
ability_scores:
  STR: 30
  DEX: 10
  CON: 29
  INT: 21
  WIS: 20
  CHA: 21
BAB: 20
CMB: 34
CMB_other: +38 grappling
CMD: 44
CMD_other: can't be tripped
feats:
- name: Bleeding Critical
- name: Blind-Fight
- name: Cleave
- name: Combat Expertise
- name: Critical Focus
- name: Improved Critical (arm)
- name: Improved Initiative
- name: Improved Trip
- name: Multiattack
- name: Power Attack
skills:
  Intimidate: 25
  Knowledge (geography): 25
  Knowledge (nature): 25
  Perception: 28
  Stealth: 11
  Swim: 41
  Use Magic Device: 25
languages:
- Aquan
- Common
special_qualities:
- tenacious grapple
ecology:
  environment: any ocean
  organization: solitary
  treasure_type: triple
special_abilities:
  Ink Cloud (Ex): 'A kraken can emit a cloud of black, venomous ink in an 80-foot
    spread once per minute as a free action while underwater. This cloud provides
    total concealment, which the kraken can use to escape a fight that is going badly.
    Creatures within the cloud are considered to be in darkness. In addition, the
    ink is toxic, functioning as contact poison against all creatures caught within
    it. The ink cloud persists for 1 minute before dispersing. The save DC against
    the poison effect is Constitution-based.Kraken Ink: Ink cloud-contact; save Fort
    DC 29; frequency 1/round for 10 rounds; effect 1 Str damage plus nausea; cure
    2 consecutive saves.'
  Jet (Ex): A kraken can jet backward as a full-round action, at a speed of 280 feet.
    It must move in a straight line, but does not provoke attacks of opportunity while
    jetting.
  Rend Ship (Ex): As a full-round action, a kraken can attempt to use four of its
    tentacles to grapple a ship of its size or smaller. It makes a CMB check opposed
    by the ship's captain's Profession (sailor) check, but the kraken gets a cumulative
    +4 bonus on the check for each size category smaller than Gargantuan the ship
    is. If the kraken grapples the ship, it holds the ship motionless; it can attack
    targets anywhere on or within the ship with its tentacles, but can only attack
    foes on deck with its free arms and can't attack foes at all with its beak. Each
    round it maintains its hold on the ship, it automatically inflicts bite damage
    on the ship's hull.
  Tenacious Grapple (Ex): A kraken does not gain the grappled condition if it grapples
    a foe with its arms or tentacles.
desc_long: |-
  The legendary kraken is one of the greatest of sailors' fears, for here is a creature the size of a whale, one that can strike from the unseen depths below, can command the winds and weather that a ship needs to move, and possesses the cruel intellect of the world's most creative and spiteful criminals. Some believe krakens to be a punishment of the gods, while others hold them to be the true lords of the deep, with the air-breathing races naught but their cattle.

  A kraken measures nearly 100 feet in length and weighs 4,000 pounds.

---

# Kraken
This tremendous _[[monsters/Leviathan|leviathan]]_ resembles a vast _[[monsters/Squid|squid]]_, yet the markings on its body are strangely unsettling to look upon.
**Source** Pathfinder RPG Bestiary pg. 184
**XP** 153,600

NE Gargantuan magical beast (aquatic)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +28

##### Defense

**AC** 32, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+26 natural, -4 size)
**hp** 290 (20d10+180)
**Fort** +21, **Ref** +12, **Will** +11
**Immune** cold, mind-affecting effects, poison

##### Offense
**Speed** 10 ft., swim 40 ft., _[[universal monster rules/Jet|jet]]_ 280 ft.
**Melee** 2 arms +26 (2d6+10/19-20 plus _[[universal monster rules/Grab|grab]]_), 8 tentacles +24 (1d8+5 plus _grab_), bite +26 (2d8+10)
**Space** 20 ft., **Reach** 20 ft. (60 ft. with arm, 40 ft. with tentacle)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (tentacles, 1d8+10), _[[items/Mundane/Ink|ink]]_ cloud, _[[universal monster rules/Rend|rend]]_ ship
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th)
1/day-control weather, _[[spells/Control Winds|control winds]]_, _[[spells/Dominate Monster|dominate monster]]_ (DC 24, animal only), _[[spells/Resist Energy|resist energy]]_

##### Statistics
**Str** 30, **Dex** 10, **Con** 29, **Int** 21, **Wis** 20, **Cha** 21
**Base Atk** +20; **CMB** +34 (+38 grappling); **CMD** 44 (can’t be tripped)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (arm), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Intimidate +25, Knowledge (geography) +25, Knowledge (nature) +25, Perception +28, Stealth +11, Swim +41, Use Magic Device +25
**Languages** Aquan, Common
**SQ** tenacious grapple

##### Ecology

**Environment** any ocean
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Ink_ Cloud (Ex)** A _[[monsters/Kraken|kraken]]_ can emit a cloud of black, venomous _ink_ in an 80-foot spread once per minute as a free action while _[[items/Weapon Magic Abilities/Underwater|underwater]]_. This cloud provides total concealment, which the _kraken_ can use to escape a fight that is going badly. Creatures within the cloud are considered to be in _[[spells/Darkness|darkness]]_. In addition, the _ink_ is _[[items/Weapon Magic Abilities/Toxic|toxic]]_, functioning as contact poison against all creatures caught within it. The _ink_ cloud persists for 1 minute before dispersing. The save DC against the poison effect is Constitution-based._Kraken_ _Ink_: _Ink_ cloud-contact; save Fort DC 29; frequency 1/round for 10 rounds; effect 1 Str damage plus nausea; cure 2 consecutive saves.

**_Jet_ (Ex) **A _kraken_ can _jet_ backward as a full-round action, at a speed of 280 feet. It must move in a straight line, but does not provoke attacks of opportunity while jetting.

**_Rend_ Ship (Ex)** As a full-round action, a _kraken_ can attempt to use four of its tentacles to grapple a ship of its size or smaller. It makes a CMB check opposed by the ship’s captain’s Profession (sailor) check, but the _kraken_ gets a cumulative +4 bonus on the check for each size category smaller than Gargantuan the ship is. If the _kraken_ grapples the ship, it holds the ship motionless; it can attack targets anywhere on or within the ship with its tentacles, but can only attack foes on deck with its free arms and can’t attack foes at all with its beak. Each round it maintains its hold on the ship, it automatically inflicts bite damage on the ship’s hull.

**Tenacious Grapple (Ex)** A _kraken_ does not gain the _[[conditions/Grappled|grappled]]_ condition if it grapples a foe with its arms or tentacles.

##### Description

The legendary _kraken_ is one of the greatest of sailors’ fears, for here is a creature the size of a _[[monsters/Whale|whale]]_, one that can strike from the _[[items/Weapon Magic Abilities/Unseen|unseen]]_ depths below, can _[[spells/Command|command]]_ the winds and weather that a ship needs to move, and possesses the _[[items/Weapon Magic Abilities/Cruel|cruel]]_ intellect of the world’s most creative and _[[items/Armor Magic Abilities/Spiteful|spiteful]]_ criminals. Some believe krakens to be a punishment of the gods, while others hold them to be the true lords of the deep, with the air-breathing races naught but their cattle.

A _kraken_ measures nearly 100 feet in length and weighs 4,000 pounds.