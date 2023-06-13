---
cssclass: [monsters]
title1: Zomok
desc_short: At first glance, this creature resembles a dragon, but its body is entirely
  made of plants and soil, and it exhales clouds of dirt.
title2: Zomok
CR: 16
sources:
- name: Bestiary 4
  page: 287
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #36: Sound of a Thousand Screams'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7x
XP: 76800
alignment: N
size: Gargantuan
type: plant
subtypes:
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 120
  low-light vision: true
  tremorsense: 60
AC:
  AC: 33
  touch: 6
  flat_footed: 33
  components:
    natural: 27
    size: -4
HP:
  HP: 246
  long: 17d8+170
saves:
  fort: 20
  ref: 7
  will: 13
immunities:
- sonic
- plant traits
weaknesses:
- vulnerable to fire
speeds:
  base: 40
  other_semicolon: forest step
  fly: 100
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +20 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: bite
      bonus:
      - 20
    - text: 2 claws +20 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: claws
      bonus:
      - 20
    - text: tail slap +15 (2d8+6)
      entries:
      - - damage: 2d8+6
      attack: tail slap
      bonus:
      - 15
    - text: 2 wings +15 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 15
  special:
  - breath weapon (60-ft. cone, 18d6 bludgeoning plus entangle, Reflex DC 28 partial,
    usable every 1d4 rounds)
  - swallow whole (6d6 bludgeoning damage, AC 23, 24 hp)
  - trample (2d8+18, DC 30)
space: 20
reach: 15
reach_other: 20 ft. with tail
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: command plants
    source: default
    freq: At will
    DC: 22
  - name: plant growth
    source: default
    freq: At will
  - name: quench
    source: default
    freq: At will
    DC: 21
  - name: entangle
    source: default
    freq: 3/day
    DC: 19
  - name: liveoak
    source: default
    freq: 3/day
  - name: transmute mud to rock
    source: default
    freq: 3/day
  - name: transmute rock to mud
    source: default
    freq: 3/day
  - name: wall of thorns
    source: default
    freq: 3/day
  - name: shambler
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 24
ability_scores:
  STR: 35
  DEX: 11
  CON: 30
  INT: 16
  WIS: 22
  CHA: 26
BAB: 12
CMB: 28
CMB_other: +30 sunder
CMD: 40
CMD_other: 42 vs. sunder, 44 vs. trip
feats:
- name: Awesome Blow
- name: Cleave
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Snatch
skills:
  Fly: 10
  Knowledge (nature): 20
  Perception: 26
  Stealth: 8
  Survival: 23
languages:
- Common
- Sylvan
- Terran
ecology:
  environment: any forests (primal land of fey)
  organization: solitary
  treasure_type: standard
special_abilities:
  Breath Weapon (Su): A zomok's breath weapon is a cone of flying dirt, bark, stones,
    and moss, which takes root as soon as it touches the ground. Creatures may attempt
    a saving throw for half damage. Any creature that fails its save and is touching
    the ground is entangled for 1d6 rounds by this material. A creature can break
    free with a DC 28 Strength or Escape Artist check. The save DC is Constitution-based.
  Forest Step (Su): A zomok in a forest area may teleport up to 120 feet by moving
    the essence of its being to another forested area. The zomok is cured of 60 points
    of damage when it does this. It may use this ability once every 1d6+1 rounds but
    no more than three times per day. If the zomok has swallowed a foe, the foe is
    left behind when the zomok teleports.
desc_long: |-
  Zomoks are dragonlike creatures made out of animate plant matter. Native to the realm of the fey, they are guardians of mystic forests. Some travel to the Material Plane and adapt to its woodlands, defending them against massive destruction-forest fires, logging, undead armies, and so on-and use their abilities to heal and regrow damaged areas.

  Rather than having a distinct physical body, a zomok is more like a spirit animating a collective mass of vegetation, and over time it sheds and acquires new material from its environment, changing its appearance to match its current location. Zomoks do not need to eat, and any creature they swallow is usually left behind as a mashed corpse to decay and provide nutrition for plants.

  A typical zomok is about 18 feet tall and 30 feet long, and weighs 30 tons.

---

# Zomok
At first glance, this creature resembles a dragon, but its body is entirely made of plants and soil, and it exhales clouds of dirt.
**Source** Bestiary 4 pg. 287, Pathfinder #36: Sound of a Thousand Screams pg. 88
**XP** 76,800

N Gargantuan plant (extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +26

##### Defense

**AC** 33, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+27 natural, –4 size)
**hp** 246 (17d8+170)
**Fort** +20, **Ref** +7, **Will** +13
**Immune** sonic, _[[universal monster rules/Plant Traits|plant traits]]_
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 40 ft., fly 100 ft. (poor); forest step
**Melee** bite +20 (2d8+12), 2 claws +20 (2d6+12), tail slap +15 (2d8+6), 2 wings +15 (2d6+6)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with tail)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 18d6 bludgeoning plus _[[spells/Entangle|entangle]]_, Reflex DC 28 partial, usable every 1d4 rounds), _[[universal monster rules/Swallow Whole|swallow whole]]_ (6d6 bludgeoning damage, AC 23, 24 hp), _[[universal monster rules/Trample|trample]]_ (2d8+18, DC 30)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +24)
Constant—_[[spells/Pass without Trace|pass without trace]]_
At will—_[[spells/Command Plants|command plants]]_ (DC 22), _[[spells/Plant Growth|plant growth]]_, _[[spells/Quench|quench]]_ (DC 21)
3/day—_entangle_ (DC 19), _[[spells/Liveoak|liveoak]]_, _[[spells/Transmute Mud to Rock|transmute mud to rock]]_, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
1/day—_[[spells/Shambler|shambler]]_

##### Statistics
**Str** 35, **Dex** 11, **Con** 30, **Int** 16, **Wis** 22, **Cha** 26
**Base Atk** +12; **CMB** +28 (+30 sunder); **CMD** 40 (42 vs. sunder, 44 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_
**Skills** Fly +10, Knowledge (nature) +20, Perception +26, Stealth +8, Survival +23
**Languages** Common, Sylvan, Terran

##### Ecology

**Environment** any forests (primal land of fey)
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Su)** A _[[monsters/Zomok|zomok]]_’s _breath weapon_ is a cone of flying dirt, bark, stones, and moss, which takes _[[spells/Root|root]]_ as soon as it touches the ground. Creatures may attempt a saving throw for half damage. Any creature that fails its save and is touching the ground is _[[conditions/Entangled|entangled]]_ for 1d6 rounds by this material. A creature can break free with a DC 28 Strength or Escape Artist check. The save DC is Constitution-based.

**Forest Step (Su)** A _zomok_ in a forest area may teleport up to 120 feet by moving the essence of its being to another forested area. The _zomok_ is cured of 60 points of damage when it does this. It may use this ability once every 1d6+1 rounds but no more than three times per day. If the _zomok_ has swallowed a foe, the foe is left behind when the _zomok_ teleports.

##### Description

Zomoks are dragonlike creatures made out of animate plant matter. Native to the realm of the fey, they are guardians of mystic forests. Some travel to the Material Plane and adapt to its woodlands, _[[items/Weapon Magic Abilities/Defending|defending]]_ them against massive _[[spells/Destruction|destruction]]_—forest fires, logging, undead armies, and so on—and use their abilities to _[[spells/Heal|heal]]_ and regrow damaged areas.

Rather than having a distinct physical body, a _zomok_ is more like a spirit animating a collective mass of vegetation, and over time it sheds and acquires new material from its environment, changing its appearance to match its current location. Zomoks do not need to eat, and any creature they swallow is usually left behind as a mashed corpse to decay and provide nutrition for plants.

A typical _zomok_ is about 18 feet tall and 30 feet long, and weighs 30 tons.