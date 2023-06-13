---
cssclass: [monsters]
title1: Inevitable, Yarahkut
desc_short: Metallic plating and stone make up this creature's body. Sharpened brass
  wings stretch from its back, and its head bears three faces.
title2: Yarahkut
CR: 14
sources:
- name: 'Pathfinder #90: The Divinity Drive'
  page: 84
  link: http://paizo.com/products/btpy95bw?Pathfinder-Adventure-Path-90-The-Divinity-Drive
XP: 38400
alignment: LN
size: Large
type: outsider
subtypes:
- extraplanar
- inevitable
- lawful
initiative:
  bonus: 6
senses:
  arcane sight: true
  darkvision: 60
  low-light vision: true
  true seeing: true
auras:
- name: malfunctioning
  radius: 100
AC:
  AC: 29
  touch: 15
  flat_footed: 23
  components:
    dex: 6
    natural: 14
    size: -1
HP:
  HP: 187
  long: 15d10+105
  regeneration: 10
  regeneration_weakness: chaotic
saves:
  fort: 14
  ref: 11
  will: 14
defensive_abilities:
- all-around vision
- constructed
SR: 25
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +21 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: claws
      bonus:
      - 21
    - text: 2 slams +21 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: slams
      bonus:
      - 21
    - text: 2 wings +21 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: wings
      bonus:
      - 21
  special:
  - dismantling gaze
  - rend (2 wings, 2d6+10)
  - wings
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: chill metal
    source: default
    freq: At will
    DC: 16
  - name: heat metal
    source: default
    freq: At will
    DC: 16
  - name: locate object
    source: default
    freq: 3/day
  - name: modify memory
    source: default
    freq: 3/day
    DC: 18
  - name: rusting grasp
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  - name: disintegrate
    source: default
    freq: 1/day
    DC: 20
  - name: feeblemind
    source: default
    freq: 1/day
  - name: mark of justice
    source: default
    freq: 1/day
  - name: lesser geas
    source: default
    freq: 1/week
    DC: 18
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 24
  DEX: 23
  CON: 20
  INT: 13
  WIS: 20
  CHA: 19
BAB: 15
CMB: 23
CMB_other: +27 disarm, +27 steal
CMD: 39
CMD_other: 41 vs. disarm, 41 vs. steal
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Flyby Attack
- name: Greater Disarm
- superscripts:
  - APG
  name: Greater Steal
- name: Improved Disarm
- superscripts:
  - APG
  name: Improved Steal
- superscripts:
  - UC
  name: Quick Steal
skills:
  Diplomacy: 16
  Disable Device: 16
  Fly: 16
  Intimidate: 16
  Knowledge (engineering): 15
  Knowledge (planes): 10
  Perception: 18
  Sense Motive: 16
  Sleight of Hand: 20
  Survival: 14
  Use Magic Device: 14
languages:
- truespeech
ecology:
  environment: any
  organization: solitary, pair, or intervention (3-6)
  treasure_type: none
special_abilities:
  Dismantling Gaze (Su): Once per round as a swift action, a yarahkut can concentrate
    its gaze on any item within 100 feet and damage that item. Attended items must
    succeed at a DC 21 Fortitude save or lose half their hit points and gain the broken
    condition. Items that already possess the broken condition and fail this save
    are destroyed. Items that successfully save against this effect are immune to
    that yarahkut's dismantling gaze for 24 hours. Unattended non-magical items don't
    receive a saving throw. The save DC is Charisma-based.
  Malfunctioning Aura (Su): A yarahkut radiates a disruptive aura that is harmful
    to ranged weapons within 100 feet. Mechanical projectile weapons-such as crossbows,
    firearms, siege weapons, and many technological weapons-have a 20% chance of not
    firing on each attack made within the aura's area. If a weapon in this aura has
    a misfire value, its misfire value increases by 2.
  Wings (Ex): A yarahkut's wings are primary attacks.
desc_long: |-
  Yarahkuts are inevitables (Pathfinder RPG Bestiary 2 161) tasked with preventing magic and technology throughout the cosmos from falling into the wrong hands. Their mandate is to track objects that could disrupt the development of cultures that are not yet ready to wield such power. In most cases, yarahkuts monitor the movement of advanced technologies and magical items from lost civilizations, ensuring they aren't introduced to regions where they could have a disruptive impact.

  Noted for their intricate brass wings, yarahkuts have superb control of these appendages and are able to use them as effective weapons. Three identical faces surround a yarahkut's head, staring impassively in separate directions with glowing golden eyes. Of its two sets of arms, one set bears claws for combat, while the remaining set is more humanoid and is used to manipulate objects-including those items it confiscates. A yarahkut stands 11 feet tall and weighs 3,000 pounds.

---

# Inevitable, Yarahkut
Metallic plating and stone make up this creature’s body. Sharpened brass wings stretch from its back, and its head bears three faces.
**Source** Pathfinder #90: The Divinity Drive pg. 84
**XP** 38,400

LN Large outsider (extraplanar, inevitable, lawful)
**Init** +6; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +18
**Aura** malfunctioning (100 ft.)

##### Defense

**AC** 29, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+6 Dex, +14 natural, –1 size)
**hp** 187 (15d10+105); _[[universal monster rules/Regeneration|regeneration]]_ 10 (chaotic)
**Fort** +14, **Ref** +11, **Will** +14
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, constructed; **SR** 25

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** 2 claws +21 (2d6+7), 2 slams +21 (1d6+7), 2 wings +21 (1d6+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** dismantling _[[universal monster rules/Gaze|gaze]]_, _[[universal monster rules/Rend|rend]]_ (2 wings, 2d6+10), wings
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
Constant—_arcane sight_, _true seeing_
At will—_[[spells/Chill Metal|chill metal]]_ (DC 16), _[[spells/Heat Metal|heat metal]]_ (DC 16)
3/day—_[[spells/Locate Object|locate object]]_, _[[spells/Modify Memory|modify memory]]_ (DC 18), _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Wall Of Force|wall of force]]_
1/day—_[[spells/Disintegrate|disintegrate]]_ (DC 20), _[[spells/Feeblemind|feeblemind]]_, _[[spells/Mark of Justice|mark of justice]]_
1/week—lesser geas (DC 18)

##### Statistics
**Str** 24, **Dex** 23, **Con** 20, **Int** 13, **Wis** 20, **Cha** 19
**Base Atk** +15; **CMB** +23 (+27 disarm, +27 steal); **CMD** 39 (41 vs. disarm, 41 vs. steal)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Steal|Greater Steal]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Steal|Improved Steal]]_, _[[feats/Quick Steal|Quick Steal]]_
**Skills** Diplomacy +16, Disable Device +16, Fly +16, Intimidate +16, Knowledge (engineering) +15, Knowledge (planes) +10, Perception +18, Sense Motive +16, Sleight of Hand +20, Survival +14, Use Magic Device +14
**Languages** truespeech

##### Ecology

**Environment** any
**Organization** solitary, pair, or intervention (3–6)
**Treasure** none

### Special Abilities

**Dismantling _Gaze_ (Su)** Once per round as a swift action, a yarahkut can concentrate its _gaze_ on any item within 100 feet and damage that item. Attended items must succeed at a DC 21 Fortitude save or lose half their hit points and gain the _[[conditions/Broken|broken]]_ condition. Items that already possess the _broken_ condition and fail this save are destroyed. Items that successfully save against this effect are immune to that yarahkut’s dismantling _gaze_ for 24 hours. Unattended non-magical items don’t receive a saving throw. The save DC is Charisma-based.

**Malfunctioning Aura (Su)** A yarahkut radiates a _[[feats/Disruptive|disruptive]]_ aura that is harmful to ranged weapons within 100 feet. Mechanical projectile weapons—such as crossbows, firearms, siege weapons, and many technological weapons—have a 20% chance of not firing on each attack made within the aura’s area. If a weapon in this aura has a misfire value, its misfire value increases by 2.

**Wings (Ex)** A yarahkut’s wings are primary attacks.

##### Description

Yarahkuts are inevitables (Pathfinder RPG Bestiary 2 161) tasked with preventing magic and technology throughout the cosmos from falling into the wrong hands. Their mandate is to track objects that could disrupt the development of cultures that are not yet ready to wield such power. In most cases, yarahkuts monitor the movement of advanced technologies and magical items from lost civilizations, ensuring they aren’t introduced to regions where they could have a _disruptive_ _[[items/Weapon Magic Abilities/Impact|impact]]_.

Noted for their intricate brass wings, yarahkuts have superb control of these appendages and are able to use them as effective weapons. Three identical faces surround a yarahkut’s head, staring impassively in separate directions with glowing golden eyes. Of its two sets of arms, one set bears claws for combat, while the remaining set is more humanoid and is used to manipulate objects—including those items it confiscates. A yarahkut stands 11 feet tall and weighs 3,000 pounds.