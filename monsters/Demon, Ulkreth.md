---
cssclass: [monsters]
title1: Demon, Ulkreth
desc_short: This towering monstrosity is clad in cracked boulders, jagged shards of
  rock, spars of crooked metal, and shredded steel. Four immense arms end in rocky
  fists, and bony wings protrude from its back.
title2: Ulkreth
CR: 15
sources:
- name: 'Pathfinder #73: The Worldwound Incursion'
  page: 82
  link: http://paizo.com/products/btpy90q9?Pathfinder-Adventure-Path-73-The-Worldwound-Incursion
XP: 51200
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 0
senses:
  darkvision: 60
  tremorsense: 60
AC:
  AC: 30
  touch: 6
  flat_footed: 30
  components:
    natural: 24
    size: -4
HP:
  HP: 229
  long: 17d10+136
saves:
  fort: 18
  ref: 5
  will: 12
defensive_abilities:
- rock catching
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
speeds:
  base: 30
  climb: 20
  fly: 50
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: gore +23 (2d8+10 plus 1d6 piercing)
      entries:
      - - damage: 2d8+10
        - damage: 1d6
          type: piercing
      attack: gore
      bonus:
      - 23
    - text: 4 slams +24 (2d6+10/19-20 plus 1d6 piercing)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
        - damage: 1d6
          type: piercing
      count: 4
      attack: slams
      bonus:
      - 24
  ranged:
  - - text: 4 rocks +14 (3d6+10)
      entries:
      - - damage: 3d6+10
      count: 4
      attack: rocks
      bonus:
      - 14
  special:
  - boulder barrage
  - ground pounder
  - punch through
  - rend (2 slams, 6d6+15)
  - rock throwing (120 ft.)
  - trample (3d6+10, DC 28)
  - wrecker
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: shatter
    source: default
    freq: At will
    DC: 14
  - name: move earth
    source: default
    freq: 3/day
  - name: earthquake
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: ulkreth
      amount: 1
    - name: omox
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 15
    concentration: 17
ability_scores:
  STR: 30
  DEX: 11
  CON: 26
  INT: 7
  WIS: 14
  CHA: 15
BAB: 17
CMB: 31
CMB_other: +35 overrun, +35 sunder
CMD: 43
CMD_other: 45 vs. overrun, 45 vs. sunder
feats:
- superscripts:
  - APG
  name: Charge Through
- name: Greater Overrun
- name: Greater Sunder
- name: Improved Critical (slams)
- name: Improved Overrun
- name: Improved Sunder
- name: Power Attack
- superscripts:
  - APG
  name: Sundering Strike
- name: Weapon Focus (slams)
skills:
  Climb: 28
  Intimidate: 22
  Knowledge (engineering): 18
  Perception: 30
  Swim: 23
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
ecology:
  environment: any (Abyss)
  organization: solitary or crew (2-4 ulkreths)
  treasure_type: standard
special_abilities:
  Boulder Barrage (Ex): An ulkreth can hurl up to four rocks as a full-round action
    or two rocks as a standard action. If rocks are available (as when the ulkreth
    uses its ground pounder ability to create rubble) it can pick up a single rock
    as a swift action, two rocks as a move action, or four rocks as a full-round action.
    If an ulkreth has a rock in each hand, it cannot use its rock catching ability.
  Ground Pounder (Ex): As a standard action, an ulkreth can strike the ground with
    its powerful fists, turning the area within a 10-foot radius into dense rubble
    (Pathfinder RPG Core Rulebook 412). Any creatures in this area at the time must
    succeed at a DC 26 Reflex save or fall prone. An ulkreth's movement is not slowed
    by the rubble it creates.
  Punch Through (Ex): An ulkreth can use a full-attack action to make its gore and
    slam attacks against the same opponent. The ulkreth then totals the damage from
    all hits before applying any damage reduction or hardness.
  Wrecker (Su): An ulkreth's rend special attack deals double damage to objects.
desc_long: Ulkreths are among the mightiest servants of the demon lord Xoveron, the
  Horned Prince of gargoyles and lord of ruination. They exist solely to destroy,
  carrying out his will of devastation to cities and civilization throughout the planes,
  tearing down monuments and buildings in the name of their unholy patron. Ulkreths
  are 25 feet tall and weigh 10 tons.

---

# Demon, Ulkreth
This towering monstrosity is clad in cracked boulders, jagged shards of rock, spars of crooked metal, and shredded steel. Four immense arms end in rocky fists, and bony wings protrude from its back.
**Source** Pathfinder #73: The Worldwound Incursion pg. 82
**XP** 51,200
CE Gargantuan outsider (chaotic, demon, evil, extraplanar)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +30

##### Defense

**AC** 30, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+24 natural, –4 size)
**hp** 229 (17d10+136)
**Fort** +18, **Ref** +5, **Will** +12
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **DR** 10/cold iron and good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 50 ft. (clumsy)
**Melee** gore +23 (2d8+10 plus 1d6 piercing), 4 slams +24 (2d6+10/19–20 plus 1d6 piercing)
**Ranged** 4 rocks +14 (3d6+10)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** boulder barrage, ground pounder, _[[feats/Punch Through|punch through]]_, _[[universal monster rules/Rend|rend]]_ (2 slams, 6d6+15), _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), _[[universal monster rules/Trample|trample]]_ (3d6+10, DC 28), wrecker
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +17)
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Shatter|shatter]]_ (DC 14)
3/day—_[[spells/Move Earth|move earth]]_
1/day—_[[spells/Earthquake|earthquake]]_, _[[universal monster rules/Summon|summon]]_ (level 5, 1 ulkreth or 1 omox 40%)

##### Statistics
**Str** 30, **Dex** 11, **Con** 26, **Int** 7, **Wis** 14, **Cha** 15
**Base Atk** +17; **CMB** +31 (+35 overrun, +35 sunder); **CMD** 43 (45 vs. overrun, 45 vs. sunder)
**Feats** _[[feats/Charge Through|Charge Through]]_, _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Critical|Improved Critical]]_ (slams), _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Sundering Strike|Sundering Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slams)
**Skills** _Climb_ +28, Intimidate +22, Knowledge (engineering) +18, Perception +30, Swim +23; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or crew (2–4 ulkreths)
**Treasure** standard

### Special Abilities

**Boulder Barrage (Ex)** An ulkreth can hurl up to four rocks as a full-round action or two rocks as a standard action. If rocks are available (as when the ulkreth uses its ground pounder ability to create rubble) it can pick up a single rock as a swift action, two rocks as a move action, or four rocks as a full-round action. If an ulkreth has a rock in each hand, it cannot use its _rock catching_ ability.

**Ground Pounder (Ex)** As a standard action, an ulkreth can strike the ground with its powerful fists, turning the area within a 10-foot radius into dense rubble (Pathfinder RPG Core Rulebook 412). Any creatures in this area at the time must succeed at a DC 26 Reflex save or fall _[[conditions/Prone|prone]]_. An ulkreth’s movement is not slowed by the rubble it creates.

**_Punch Through_ (Ex) **An ulkreth can use a full-attack action to make its gore and slam attacks against the same opponent. The ulkreth then totals the damage from all hits before applying any _[[universal monster rules/Damage Reduction|damage reduction]]_ or hardness.

**Wrecker (Su)** An ulkreth’s _rend_ special attack deals double damage to objects.

##### Description

Ulkreths are among the mightiest servants of the demon lord Xoveron, the Horned Prince of gargoyles and lord of ruination. They exist solely to destroy, carrying out his will of devastation to cities and civilization throughout the planes, tearing down monuments and buildings in the name of their _[[items/Weapon Magic Abilities/Unholy|unholy]]_ patron. Ulkreths are 25 feet tall and weigh 10 tons.