---
cssclass: [monsters]
title1: Protean, Keketar
desc_short: Colors dance over this serpentine creature's scales. A strange crown of
  energy glows above the thing's reptilian head.
title2: Keketar
CR: 17
sources:
- name: Bestiary 2
  page: 215
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: The Great Beyond - A Guide to the Multiverse
  page: 60
  link: http://paizo.com/store/byCompany/p/paizoPublishingLLC/pathfinder/campaignSetting/35E/v5748btpy87uz
XP: 102400
alignment: CN
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- protean
- shapechanger
initiative:
  bonus: 5
senses:
  blindsense: 60
  darkvision: 60
auras:
- name: spatial riptide
  radius: 30
AC:
  AC: 32
  touch: 14
  flat_footed: 27
  components:
    dex: 5
    natural: 18
    size: -1
HP:
  HP: 287
  long: 23d10+161
  fast_healing: 10
saves:
  fort: 22
  ref: 14
  will: 22
defensive_abilities:
- amorphous anatomy
- freedom of movement
DR:
- amount: 15
  weakness: lawful
immunities:
- acid
- polymorph
resistances:
  electricity: 10
  sonic: 10
SR: 28
speeds:
  base: 40
  fly: 40
  fly_maneuverability: perfect
  swim: 40
attacks:
  melee:
  - - text: bite +31 (4d8+9 plus warpwave)
      entries:
      - - damage: 4d8+9
        - effect: warpwave
      attack: bite
      bonus:
      - 31
    - text: 2 claws +31 (2d6+9 plus warpwave)
      entries:
      - - damage: 2d6+9
        - effect: warpwave
      count: 2
      attack: claws
      bonus:
      - 31
    - text: tail slap +29 (2d8+4 plus grab)
      entries:
      - - damage: 2d8+4
        - effect: grab
      attack: tail slap
      bonus:
      - 29
  special:
  - constrict 1d8+9
  - reshape reality
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect law
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: chaos hammer
    source: default
    freq: At will
    DC: 21
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: major creation
    source: default
    freq: At will
  - name: move earth
    source: default
    freq: At will
  - name: shatter
    source: default
    freq: At will
    DC: 19
  - name: quickened confusion
    source: default
    freq: 3/day
    DC: 21
  - name: dispel law
    source: default
    freq: 3/day
    DC: 22
  - name: empowered chaos hammer
    source: default
    freq: 3/day
    DC: 21
  - name: polymorph any object
    source: default
    freq: 3/day
    DC: 25
  - name: disintegrate
    source: default
    freq: 1/day
    DC: 23
  - name: prismatic spray
    source: default
    freq: 1/day
    DC: 24
  - name: prismatic sphere
    source: default
    freq: 1/day
    DC: 26
  - name: reshape reality
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 24
ability_scores:
  STR: 29
  DEX: 21
  CON: 24
  INT: 20
  WIS: 25
  CHA: 24
BAB: 23
CMB: 33
CMB_other: +35 bull rush, +37 grapple
CMD: 48
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Empower Spell-like Ability (chaos hammer)
- name: Great Fortitude
- name: Improved Bull Rush
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-like Ability (confusion)
- name: Vital Strike
skills:
  Acrobatics: 31
  Bluff: 33
  Diplomacy: 33
  Fly: 11
  Intimidate: 33
  Knowledge (arcana): 31
  Knowledge (planes): 31
  Knowledge (any two): 28
  Perception: 33
  Stealth: 27
  Swim: 40
languages:
- Abyssal
- Protean
- telepathy 100 ft.
special_qualities:
- change shape (greater polymorph)
ecology:
  environment: any (Limbo)
  organization: solitary or chorus (2-4)
  treasure_type: standard
special_abilities:
  Reshape Reality (Sp): This ability functions as the spell mirage arcana heightened
    to a 9th-level spell, except the changes created are quasi-real, like those created
    by shadow conjuration. A creature that interacts with reshaped reality may make
    a DC 26 Will save to see through the semi-real illusion. Terrain can provide concealment,
    and against foes who do not make the Will save to see through the facade, reshaped
    reality can provide cover. For disbelievers, quasi-real objects and terrain have
    only 20% normal hardness and hit points, and break DCs are 10 lower than normal.
    Dangerous terrain cannot exceed 5d6 points of damage per round (1d6 per round
    against disbelievers). This ability cannot damage existing structures, nor does
    it function in areas where planar travel is prohibited.
  Spatial Riptide (Su): Any non-protean teleporting into or out of the protean's aura
    must make a DC 28 Fortitude save or enter a state of suspended animation (identical
    to temporal stasis) for 1d3 rounds; success means the creature is merely nauseated
    for 1 round. The save DC is Constitution-based.
  Warpwave (Su): A creature struck by a keketar's claw or bite must make a DC 28 Fortitude
    save or be affected by a warpwave. The save DC is Constitution-based.
desc_long: Priests and prophets, keketars are the leaders of their race, guiding proteans
  in their sacred mission to return all existence to primal chaos.

---

# Protean, Keketar
Colors dance over this serpentine creature’s scales. A strange crown of energy glows above the thing’s reptilian head.
**Source** Bestiary 2 pg. 215, The Great Beyond - A Guide to the Multiverse pg. 60
**XP** 102,400

CN Large outsider (chaotic, extraplanar, protean, shapechanger)
**Init** +5; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +33
**Aura** spatial riptide (30 ft.)

##### Defense

**AC** 32, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+5 Dex, +18 natural, –1 size)
**hp** 287 (23d10+161); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +22, **Ref** +14, **Will** +22
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_ anatomy, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/lawful; **Immune** acid, _[[spells/Polymorph|polymorph]]_; **Resist** electricity 10, sonic 10; **SR** 28

##### Offense
**Speed** 40 ft., fly 40 ft. (perfect), swim 40 ft.
**Melee** bite +31 (4d8+9 plus warpwave), 2 claws +31 (2d6+9 plus warpwave), tail slap +29 (2d8+4 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ 1d8+9, reshape reality
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +24)
Constant—_[[spells/Detect Law|detect law]]_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 21), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Major Creation|major creation]]_, _[[spells/Move Earth|move earth]]_, _[[spells/Shatter|shatter]]_ (DC 19)
3/day—quickened _[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Dispel Law|dispel law]]_ (DC 22), empowered _chaos hammer_ (DC 21), _[[spells/Polymorph Any Object|polymorph any object]]_ (DC 25)
1/day—_[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Prismatic Spray|prismatic spray]]_ (DC 24), _[[spells/Prismatic Sphere|prismatic sphere]]_ (DC 26), reshape reality

##### Statistics
**Str** 29, **Dex** 21, **Con** 24, **Int** 20, **Wis** 25, **Cha** 24
**Base Atk** +23; **CMB** +33 (+35 bull rush, +37 grapple); **CMD** 48 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-like Ability]]_ (_chaos hammer_), _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-like Ability]]_ (_confusion_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +31, Bluff +33, Diplomacy +33, Fly +11, Intimidate +33, Knowledge (arcana, planes) +31, Knowledge (any two) +28, Perception +33, Stealth +27, Swim +40
**Languages** Abyssal, Protean; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (greater _polymorph_)

##### Ecology

**Environment** any (Limbo)
**Organization** solitary or chorus (2–4)
**Treasure** standard

### Special Abilities

**Reshape Reality (Sp)** This ability functions as the spell _[[spells/Mirage Arcana|mirage arcana]]_ heightened to a 9th-level spell, except the changes created are quasi-real, like those created by _[[spells/Shadow Conjuration|shadow conjuration]]_. A creature that interacts with reshaped reality may make a DC 26 Will save to see through the semi-real illusion. Terrain can provide concealment, and against foes who do not make the Will save to see through the facade, reshaped reality can provide cover. For disbelievers, quasi-real objects and terrain have only 20% normal hardness and hit points, and break DCs are 10 lower than normal. Dangerous terrain cannot exceed 5d6 points of damage per round (1d6 per round against disbelievers). This ability cannot damage existing structures, nor does it function in areas where _[[items/Weapon Magic Abilities/Planar|planar]]_ travel is prohibited.
**Spatial Riptide (Su)** Any non-protean teleporting into or out of the protean’s aura must make a DC 28 Fortitude save or enter a state of suspended animation (identical to _[[spells/Temporal Stasis|temporal stasis]]_) for 1d3 rounds; success means the creature is merely _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Constitution-based.

**Warpwave (Su) **A creature struck by a keketar’s claw or bite must make a DC 28 Fortitude save or be affected by a warpwave. The save DC is Constitution-based.

##### Description

Priests and prophets, keketars are the leaders of their race, guiding proteans in their _[[items/Weapon Magic Abilities/Sacred|sacred]]_ mission to return all existence to primal chaos.