---
cssclass: [monsters]
title1: Demon, Omox
desc_short: 'This rancid-smelling mound of animated ooze has about its shifting countenance
  the hideous shape of a half-melted man. '
title2: Omox
CR: 12
sources:
- name: Bestiary 2
  page: 79
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #16: Endless Night'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy85er
XP: 19200
alignment: CE
size: Medium
type: outsider
subtypes:
- aquatic
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 120
AC:
  AC: 28
  touch: 18
  flat_footed: 20
  components:
    dex: 7
    dodge: 1
    natural: 10
HP:
  HP: 162
  long: 13d10+91
saves:
  fort: 15
  ref: 13
  will: 12
DR:
- amount: 10
  weakness: good
immunities:
- acid
- critical hits
- disease
- electricity
- paralysis
- poison
- polymorph
- sleep effects
- stunning
resistances:
  cold: 10
  fire: 10
SR: 23
speeds:
  base: 40
  climb: 20
  swim: 80
attacks:
  melee:
  - - text: 2 slams +21 (1d6+8 plus 3d6 acid and grab)
      entries:
      - - damage: 1d6+8
        - damage: 3d6
          type: acid
        - effect: grab
      count: 2
      attack: slams
      bonus:
      - 21
  ranged:
  - - text: slime +20 (1d6 plus 3d6 acid and entangle)
      entries:
      - - damage: 1d6
        - damage: 3d6
          type: acid
        - effect: entangle
      attack: slime
      bonus:
      - 20
  special:
  - smothering
spell_like_abilities:
  entries:
  - name: create water
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: liquid leap
    source: default
    freq: At will
    other: see below
  - name: telekinesis
    source: default
    freq: At will
    DC: 19
  - name: gaseous form
    source: default
    freq: 3/day
  - name: control water
    source: default
    freq: 3/day
  - name: poison
    source: default
    freq: 3/day
    DC: 18
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 17
  - name: acid fog
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: omox
      amount: 1
      chance: 30%
    - name: babaus
      amount: 1d4
      chance: 60%
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 26
  DEX: 25
  CON: 24
  INT: 15
  WIS: 19
  CHA: 18
BAB: 13
CMB: 21
CMD: 39
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
- name: Spring Attack
- name: Vital Strike
skills:
  Acrobatics: 23
    jump: 27
  Climb: 32
  Escape Artist: 23
  Knowledge (dungeoneering): 18
  Knowledge (planes): 18
  Perception: 28
  Sense Motive: 20
  Stealth: 23
    when submerged: 33
  Swim: 32
  _racial_mods:
    Escape Artist:
      _: 16
    Perception:
      _: 8
    Stealth:
      when submerged: 10
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- amorphous
- amphibious
- compression
ecology:
  environment: any (the Abyss)
  organization: solitary or clot (2-6)
  treasure_type: standard
special_abilities:
  Liquid Leap (Sp): As long as an omox is in contact with liquid, it can use dimension
    door as a swift action (CL 12th); its starting and ending points must be connected
    by a contiguous mass of liquid.
  Slime (Su): An omox's nauseating body is composed of sticky, acidic slime. As an
    attack action, it can hurl a glob of slime (range increment 20 feet). Any creature
    that is struck by the glob must make a DC 23 Reflex save or become entangled for
    1d6 rounds. The save DC is Constitution-based.
  Smothering (Ex): An omox can use its grab ability against a creature of any size.
    When it grabs a foe, it attempts to flow over and into the victim's mouth and
    nose to smother it. Each round the omox maintains its grapple, its victim cannot
    breathe or speak. See page 445 of the Pathfinder RPG Core Rulebook for rules on
    how long a victim can hold its breath and the consequences of suffocation.
desc_long: |-
  Amorphous beings of living slime, these repulsive demons lurk in fetid pools and lakes of filth, eager to drown unwary passersby. When summoned to the Material Plane, omoxes typically guard places of sacred filth or waters watched over by cults of Jubilex, the demon lord with which these foul demons are most commonly associated. 

  A typical omox stands 7 feet tall and weighs 1,200 pounds. They form from the souls of those who destroyed beautiful things in life, or who befouled and desecrated objects of purity.

---

# Demon, Omox
This rancid-smelling mound of _[[items/Armor Magic Abilities/Animated|animated]]_ ooze has about its shifting countenance the hideous shape of a half-melted man.

**Source** Bestiary 2 pg. 79, Pathfinder #16: Endless Night pg. 82
**XP** 19,200
CE Medium outsider (aquatic, chaotic, demon, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +28

##### Defense

**AC** 28, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 162 (13d10+91)
**Fort** +15, **Ref** +13, **Will** +12
**DR** 10/good; **Immune** acid, critical hits, disease, electricity, _[[universal monster rules/Paralysis|paralysis]]_, poison, _[[spells/Polymorph|polymorph]]_, sleep effects, stunning; **Resist** cold 10, fire 10; **SR** 23

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., swim 80 ft.
**Melee** 2 slams +21 (1d6+8 plus 3d6 acid and _[[universal monster rules/Grab|grab]]_)
**Ranged** slime +20 (1d6 plus 3d6 acid and _[[spells/Entangle|entangle]]_)
**Special Attacks** smothering
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
At will—_[[spells/Create Water|create water]]_, greater teleport (self plus 50 lbs. of objects only), liquid leap (see below), _[[spells/Telekinesis|telekinesis]]_ (DC 19)
3/day—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Control Water|control water]]_, poison (DC 18), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 17)
1/day—_[[spells/Acid Fog|acid fog]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 omox 30% or 1d4 babaus 60%)

##### Statistics
**Str** 26, **Dex** 25, **Con** 24, **Int** 15, **Wis** 19, **Cha** 18
**Base Atk** +13; **CMB** +21; **CMD** 39 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +23 (+27 _[[spells/Jump|jump]]_), _Climb_ +32, Escape Artist +23, Knowledge (dungeoneering) +18, Knowledge (planes) +18, Perception +28, Sense Motive +20, Stealth +23 (+33 when submerged), Swim +32; **Racial Modifiers** +16 Escape Artist, +8 Perception, +10 Stealth when submerged
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amorphous|amorphous]]_, _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Compression|compression]]_

##### Ecology

**Environment** any (the Abyss)
**Organization** solitary or clot (2–6)
**Treasure** standard

### Special Abilities

**Liquid Leap (Sp)** As long as an omox is in contact with liquid, it can use _[[spells/Dimension Door|dimension door]]_ as a swift action (CL 12th); its starting and ending points must be connected by a contiguous mass of liquid.
**Slime (Su)** An omox’s nauseating body is composed of _[[items/Weapon Magic Abilities/Sticky|sticky]]_, acidic slime. As an attack action, it can hurl a glob of slime (range increment 20 feet). Any creature that is struck by the glob must make a DC 23 Reflex save or become _[[conditions/Entangled|entangled]]_ for 1d6 rounds. The save DC is Constitution-based.
**Smothering (Ex)** An omox can use its _grab_ ability against a creature of any size. When it grabs a foe, it attempts to flow over and into the victim’s mouth and nose to _[[universal monster rules/Smother|smother]]_ it. Each round the omox maintains its grapple, its victim cannot breathe or speak. See page 445 of the Pathfinder RPG Core Rulebook for rules on how long a victim can hold its breath and the consequences of _[[spells/Suffocation|suffocation]]_.

##### Description

_Amorphous_ beings of living slime, these repulsive demons lurk in fetid pools and lakes of filth, eager to drown unwary passersby. When summoned to the Material Plane, omoxes typically _[[npcs/Guard|guard]]_ places of _[[items/Weapon Magic Abilities/Sacred|sacred]]_ filth or waters watched over by cults of Jubilex, the demon lord with which these foul demons are most commonly associated.

A typical omox stands 7 feet tall and weighs 1,200 pounds. They form from the souls of those who destroyed beautiful things in life, or who befouled and desecrated objects of purity.