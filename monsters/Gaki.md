---
cssclass: [monsters]
title1: Gaki
desc_short: This skeletal creature with a long, thin neck seems to float above the
  ground. Its jaw is elongated, showing sharp, worn teeth.
title2: Gaki
CR: 7
sources:
- name: Bestiary 4
  page: 118
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 3200
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect evil: true
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    dex: 2
    dodge: 1
    natural: 7
HP:
  HP: 74
  long: 9d8+32
saves:
  fort: 5
  ref: 7
  will: 9
immunities:
- undead traits
weaknesses:
- aversion to sun and moon
- compulsive hunger
- vulnerable to cold and fire
speeds:
  base: 30
  fly: 30
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +9 (2d6+3)
      entries:
      - - damage: 2d6+3
      count: 2
      attack: claws
      bonus:
      - 9
    - text: bite +9 (2d6+3 plus grab)
      entries:
      - - damage: 2d6+3
        - effect: grab
      attack: bite
      bonus:
      - 9
  special:
  - blood drain (1d2 Constitution)
  - fear cone (30 ft., DC 16)
space: 5
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
  - name: disguise self
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 9
ability_scores:
  STR: 16
  DEX: 15
  CON:
  INT: 9
  WIS: 12
  CHA: 18
BAB: 6
CMB: 9
CMB_other: +13 grapple
CMD: 22
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
skills:
  Intimidate: 14
  Perception: 13
  Stealth: 14
languages:
- Common
ecology:
  environment: any land
  organization: solitary or gang (2-4)
  treasure_type: incidental
special_abilities:
  Aversion to Sun and Moon (Ex): A gaki takes 1d4 points of fire damage every round
    it's exposed to the light of a full moon. It takes 1d4 points of cold damage every
    round it is exposed to direct sunlight.
  Compulsive Hunger (Ex): Despite being undead, a gaki is plagued by an insatiable
    hunger, and believes it can gain a normal body or rest in peace if it consumes
    the right mixture of flesh, food, and drink. A gaki that finds a corpse or is
    offered food, wine, holy water, or flowers must succeed at a DC 20 Will save or
    spend one turn trying to grab and consume it. Its narrow neck prevents it from
    swallowing more than a tiny amount, and it gives up after 1 round of attempting
    to do so. A gaki that consumes holy water in this way is not harmed by it.
desc_long: |-
  When an especially jealous or greedy evil person dies, it sometimes returns as a gaki-a misshapen creature with a supernatural hunger for things of the material world. Mistakenly called “hungry ghosts” because of their ability to fly and turn invisible, gakis believe that if they consume the right material-typically meat, wine, blood, flowers, and souls-they can form a new body resembling their former mortal shapes. Its long, thin neck restricts how much it can eat, and the creature is perpetually starving. It prefers to consume evil creatures, believing it gains more sustenance from a sinful being than a righteous one, but it won't pass up any mortal flesh. Some gakis believe they must consume flesh from demons or undead, and fixate on these creatures to the aversion of all others.

  Gakis are cursed, pitiable creatures with nothing to lose, which makes them very dangerous. Some that have existed for many years as undead grow desperate and try consuming earth, sewage, or more vile substances in an attempt to find the missing ingredient for their transformation. Particularly unfortunate ones bear an onerous curse that causes anything they try to eat to burst into flame or wither away into dust.

  These creatures have short memories and little sense of perspective. They're smart enough to pursue what they want cannily, but fail at making long-term plans. Most gakis wander alone, pursuing their search for nourishment in solitude. When they do form packs, they use their numbers to surround and bring down large animals or groups of people, but then throw cooperation aside to squabble and shove as each one greedily tries to claim the entire prize they've taken.

  Strangely, gakis are scorched by moonlight and frozen by sunlight. Because of this, they're forced to lurk in the shadows of ruins. Some wander the deep caves and tunnels below the surface, scrounging whatever meals they can find. In urban areas, they group together to stalk the slums, often leaping upon victims, tearing away small morsels of flesh before they retreat, leaving victims bleeding and disoriented. They find hiding places- often in abandoned buildings or sewers- to stay during the day, turning invisible and biding their time till the dark of night comes.

---

# Gaki
This skeletal creature with a long, thin neck seems to float above the ground. Its jaw is elongated, showing sharp, worn teeth.
**Source** Bestiary 4 pg. 118
**XP** 3,200

NE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_; Perception +13

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 74 (9d8+32)
**Fort** +5, **Ref** +7, **Will** +9
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** _[[spells/Aversion|aversion]]_ to sun and moon, compulsive hunger, vulnerable to cold and fire

##### Offense
**Speed** 30 ft., fly 30 ft. (average)
**Melee** 2 claws +9 (2d6+3), bite +9 (2d6+3 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Constitution), _[[universal monster rules/Fear|fear]]_ cone (30 ft., DC 16)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
Constant—_detect evil_
At will—_[[spells/Invisibility|invisibility]]_
1/day—_[[spells/Disguise Self|disguise self]]_

##### Statistics
**Str** 16, **Dex** 15, **Con** —, **Int** 9, **Wis** 12, **Cha** 18
**Base Atk** +6; **CMB** +9 (+13 grapple); **CMD** 22 
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Intimidate +14, Perception +13, Stealth +14
**Languages** Common

##### Ecology

**Environment** any land
**Organization** solitary or gang (2–4)
**Treasure** incidental

### Special Abilities

**_Aversion_ to Sun and Moon (Ex)** A _[[monsters/Gaki|gaki]]_ takes 1d4 points of fire damage every round it’s exposed to the light of a full moon. It takes 1d4 points of cold damage every round it is exposed to direct sunlight.

**Compulsive Hunger (Ex)** Despite being undead, a _gaki_ is plagued by an insatiable hunger, and believes it can gain a normal body or rest in peace if it consumes the right mixture of flesh, food, and drink. A _gaki_ that finds a corpse or is offered food, wine, _[[items/Mundane/Holy water|holy water]]_, or flowers must succeed at a DC 20 Will save or spend one turn trying to _grab_ and consume it. Its narrow neck prevents it from swallowing more than a tiny amount, and it gives up after 1 round of attempting to do so. A _gaki_ that consumes _holy water_ in this way is not harmed by it.

##### Description

When an especially jealous or greedy evil person dies, it sometimes returns as a _gaki_—a misshapen creature with a supernatural hunger for things of the material world. Mistakenly _[[items/Weapon Magic Abilities/Called|called]]_ “hungry ghosts” because of their ability to fly and turn _[[conditions/Invisible|invisible]]_, gakis believe that if they consume the right material—typically meat, wine, blood, flowers, and souls—they can form a new body resembling their former mortal shapes. Its long, thin neck restricts how much it can eat, and the creature is perpetually starving. It prefers to consume evil creatures, believing it gains more sustenance from a sinful being than a _[[items/Armor Magic Abilities/Righteous|righteous]]_ one, but it won’t pass up any mortal flesh. Some gakis believe they must consume flesh from demons or undead, and fixate on these creatures to the _aversion_ of all others.

Gakis are cursed, pitiable creatures with nothing to lose, which makes them very dangerous. Some that have existed for many years as undead grow desperate and try consuming earth, sewage, or more vile substances in an attempt to find the missing ingredient for their _[[spells/Transformation|transformation]]_. Particularly unfortunate ones bear an onerous curse that causes anything they try to eat to burst into flame or wither away into dust.

These creatures have short memories and little sense of perspective. They’re smart enough to pursue what they want cannily, but fail at making long-term plans. Most gakis wander alone, pursuing their search for nourishment in solitude. When they do form packs, they use their numbers to surround and bring down large animals or groups of people, but then throw cooperation aside to squabble and shove as each one greedily tries to claim the entire prize they’ve taken.

Strangely, gakis are scorched by moonlight and frozen by sunlight. Because of this, they’re forced to lurk in the shadows of ruins. Some wander the deep caves and tunnels below the surface, scrounging whatever meals they can find. In urban areas, they group together to stalk the slums, often leaping upon victims, tearing away small morsels of flesh before they retreat, leaving victims bleeding and disoriented. They find hiding places— often in abandoned buildings or sewers— to stay during the day, turning _invisible_ and biding their time till the dark of night comes.