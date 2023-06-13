---
cssclass: [monsters]
title1: Protean, Izfiitar
desc_short: This serpentine monster has six arms and is crowned by a halo ofever-changing
  symbols.
title2: Izfiitar
CR: 20
sources:
- name: Bestiary 6
  page: 210
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 307200
alignment: CN
size: Medium
type: outsider
subtypes:
- chaotic
- extraplanar
- protean,shapechanger
initiative:
  bonus: 14
senses:
  blindsense: 60
  darkvision: 60
  detect law: true
  true seeing: true
auras:
- name: cloak of chaos
  DC: 27
AC:
  AC: 36
  touch: 24
  flat_footed: 26
  components:
    dex: 10
    deflection,+12 natural: 4
HP:
  HP: 362
  long: 25d10+225
saves:
  fort: 27
  ref: 22
  will: 26
defensive_abilities:
- amorphous anatomy
- freedom ofmovement
DR:
- amount: 15
  weakness: lawful
immunities:
- acid
- polymorph effects
resistances:
  electricity: 10
  sonic: 10
SR: 31
speeds:
  base: 40
  fly: 50
  fly_maneuverability: perfect
  swim: 40
attacks:
  melee:
  - - text: bite +34 (4d6+9/19-20 plus greater warpwave)
      entries:
      - - damage: 4d6+9
          crit_range: 19-20
        - effect: greater warpwave
      attack: bite
      bonus:
      - 34
    - text: 6 claws +34(1d6+9 plus greater warpwave)
      entries:
      - - damage: 1d6+9
        - effect: greater warpwave
      count: 6
      attack: claws
      bonus:
      - 34
    - text: 2 tail slaps +32 (1d8+4 plus grab)
      entries:
      - - damage: 1d8+4
        - effect: grab
      count: 2
      attack: tail slaps
      bonus:
      - 32
  special:
  - constrict (1d8+13)
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 27
  - name: detect law
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: confusion
    source: default
    freq: At will
    DC: 23
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
  - name: plane shift
    source: default
    freq: At will
    DC: 26
  - name: telekinesis
    source: default
    freq: At will
    DC: 34
  - name: quickened confusion
    source: default
    freq: 3/day
    DC: 23
  - name: quickened disintegrate
    source: default
    freq: 3/day
    DC: 25
  - name: prismatic spray
    source: default
    freq: 3/day
    DC: 26
  - name: reshape reality
    source: default
    freq: 3/day
    DC: 26
  - name: quickened telekinesis
    source: default
    freq: 3/day
    DC: 24
  - name: word of chaos
    source: default
    freq: 3/day
    DC: 26
  - name: heal
    source: default
    freq: 1/day
  - name: implosion
    source: default
    freq: 1/day
    DC: 28
  - name: mage's disjunction
    source: default
    freq: 1/day
  - name: prismatic sphere
    source: default
    freq: 1/day
    DC: 28
  - name: miracle
    source: default
    freq: 1/year
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 29
  DEX: 31
  CON: 28
  INT: 24
  WIS: 27
  CHA: 28
BAB: 25
CMB: 34
CMD: 58
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Flyby Attack
- name: GreaterVital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (confusion)
- name: Quicken Spell-Like Ability (disintegrate)
- name: Quicken Spell-Like Ability (telekinesis)
- name: Vital Strike
skills:
  Acrobatics: 38
  Bluff: 37
  Diplomacy: 37
  Fly: 46
  Knowledge (arcana): 35
  Knowledge (planes): 35
  Knowledge (history,religion): 32
  Perception: 36
  Sense Motive: 36
  Spellcraft: 35
  Stealth: 38
  Swim: 42
languages:
- Abyssal
- Protean
- telepathy 100 ft.
special_qualities:
- change shape (shapechange)
ecology:
  environment: any (Maelstrom)
  organization: solitary or chorus (2-3)
  treasure_type: double
special_abilities:
  Greater Warpwave (Su): A creature struck by an izfiitar's bite or claw must succeed
    at a DC 31 Fortitude save or be affected by a greater warpwave. Roll 1d20 and
    consult the following list for exact effects on the creature. The save DC is Constitution-based.
    d20 Warpwave Effect 1 Target takes 4 points of Strength damage. 2 Target takes
    4 points of Dexterity damage. 3 Target takes 4 points of Constitution damage.
    4 Target takes 4 points of Intelligence damage. 5 Target takes 4 points of Wisdom
    damage. 6 Target takes 4 points of Charisma damage. 7 Target gains 1d4 negative
    levels. 8 Target is blinded or deafened for 1d4+1 rounds. 9 Target is confused
    for 1d4 rounds, and all non-proteans that are within 20 feet are affected by confusion
    (Will DC 23 negates). 10 Target is struck by a fireball (Reflex DC 22 half) centered
    on its location that deals acid damage rather than fire. 11 Target is affected
    by greater dispel magic (CL 20th). 12 Target is sickened for 1d4+1 rounds. 13
    Target is nauseated for 1d4+1 rounds. 14 Target is staggered for 1d4+1 rounds.
    15 Target is stunned for 1d4+1 rounds. 16 Target gains 8d6 temporary hit points.
    17 Target is affected by a heal spell (CL 20th). 18 Target is permanently turned
    to stone. 19 Target is temporarily shifted outside of the normal flow of time,
    as per temporal stasis, for 1d3 rounds. 20 Target is affected by imprisonment
    (CL 20th), and a keketar protean loyal to the izfiitar appears in the target's
    place.
  Kiss of the Speakers (Ex): 'Moment by moment, an izfiitar tinkers with the myriad
    possibilities in which it can act or move, granting it the prescience to choose
    whichever possible moment best suits it. As a move action once every other round,
    an izfiitar can grant itself one of the following options on its next round's
    action: double all of its speeds for 1 round, gain the ability to roll one d20
    roll twice in the next round and choose which result to use, or gain an additional
    standard action that can be used only to activate a spell-like ability.'
  Reshape Reality (Sp): This ability functions as mirage arcana heightened to a 9th-level
    spell, except the changes created are quasi-real, like those created by shadow
    conjuration. A creature that interacts with reshaped reality can attempt a DC
    26 Will save to see through the illusion. Terrain thus created can provide concealment,
    and against foes who fail the Will save to see through it, reshaped reality can
    provide cover. For disbelievers, quasi-real objects and terrain have only 20%
    of the normal hardness and hit points, and break DCs are 10 lower than normal.
    Damage caused by dangerous terrain can't exceed 5d6 points of damage per round
    (1d6 per round against disbelievers). This ability can't damage existing structures,
    nor does it function in areas where planar travel is prohibited.
desc_long: |-
  While the keketar proteans (Pathfinder RPG Bestiary 2 215) hold vague ideological sway over their kind's infinite choruses, the izfiitars loom above them, cardinals among the slithering clergy. Aloof and distant even compared to the keketars, izfiitars rarely venture beyond the Maelstrom's deepest reaches, content to divine the will of the plane's unknowable dualistic godhead, the Speakers of the Depths. 

  Bound to a single chorus, izfiitars are and yet are not distinct from the keketars who pay them obeisance, leading many to speculate that they are essentially elevated keketars, chosen for reasons unknown and propelled along a path of apotheosis either by the Maelstrom itself or by one of the so-called protean lords. Yet their position remains paradoxical, befitting the Maelstrom's rejection of stability and consistency. Not every chorus contains an izfiitar, while some contain multiple, and the size and influence of any given chorus is entirely independent of their presence. 

  Although smaller in size than keketars, izfiitars have monstrous physical attacks and stupendous magical powers. They wield a more powerful version of lesser proteans' warpwave, as well as abilities that bend reality and alter probability, focused on the proteans' desire to return all of reality to the freedom of pure, unbound chaos.

---

# Protean, Izfiitar
This serpentine monster has six arms and is crowned by a halo of

ever-changing symbols.
**Source** Bestiary 6 pg. 210
**XP** 307,200

CN Medium outsider (chaotic, extraplanar, protean,

shapechanger)
**Init** +14; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Law|detect law]]_,

_[[spells/True Seeing|true seeing]]_; Perception +36
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 27)

##### Defense

**AC** 36, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+10 Dex, +4 _[[spells/Deflection|deflection]]_,

+12 natural)
**hp** 362 (25d10+225)
**Fort** +27, **Ref** +22, **Will** +26
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_ anatomy, _[[spells/Freedom|freedom]]_ of

movement; **DR** 15/lawful; **Immune** acid, _[[spells/Polymorph|polymorph]]_ effects; **Resist** electricity 10, sonic 10; **SR** 31

##### Offense
**Speed** 40 ft., fly 50 ft. (perfect), swim 40 ft.
**Melee** bite +34 (4d6+9/19–20 plus greater warpwave), 6 claws +34

(1d6+9 plus greater warpwave), 2 tail slaps +32 (1d8+4 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+13)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
Constant—_cloak of chaos_ (DC 27), _detect law_, _true seeing_ 
At will—_[[spells/Confusion|confusion]]_ (DC 23), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Major Creation|major creation]]_, _[[spells/Plane Shift|plane shift]]_ (DC 26), _[[spells/Telekinesis|telekinesis]]_ (DC 34) 
3/day—quickened _confusion_ (DC 23), quickened _[[spells/Disintegrate|disintegrate]]_ (DC 25), _[[spells/Prismatic Spray|prismatic spray]]_ (DC 26), reshape reality (DC 26), quickened _telekinesis_ (DC 24), _[[spells/Word Of Chaos|word of chaos]]_ (DC 26) 
1/day—_[[spells/Heal|heal]]_, _[[spells/Implosion|implosion]]_ (DC 28), mage’s disjunction, _[[spells/Prismatic Sphere|prismatic sphere]]_ (DC 28) 
1/year—_[[spells/Miracle|miracle]]_

##### Statistics
**Str** 29, **Dex** 31, **Con** 28, **Int** 24, **Wis** 27, **Cha** 28
**Base Atk** +25; **CMB** +34; **CMD** 58 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Flyby Attack|Flyby Attack]]_, Greater

_[[feats/Vital Strike|Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, Quicken Spell-

Like Ability (_confusion_, _disintegrate_, _telekinesis_), _Vital Strike_
**Skills** Acrobatics +38, Bluff +37, Diplomacy +37, Fly +46,

Knowledge (arcana, planes) +35, Knowledge (history,

religion) +32, Perception +36, Sense Motive +36,

Spellcraft +35, Stealth +38, Swim +42
**Languages** Abyssal, Protean; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Shapechange|shapechange]]_)

##### Ecology

**Environment** any (Maelstrom)
**Organization** solitary or chorus (2–3)
**Treasure** double

### Special Abilities

**Greater Warpwave (Su)** A creature struck by an izfiitar’s bite or claw must succeed at a DC 31 Fortitude save or be affected by a greater warpwave. Roll 1d20 and consult the following list for exact effects on the creature. The save DC is Constitution-based.

<th>d20</th> <th>Warpwave Effect</th> 1 Target takes 4 points of Strength damage. 2 Target takes 4 points of Dexterity damage. 3 Target takes 4 points of Constitution damage. 4 Target takes 4 points of Intelligence damage. 5 Target takes 4 points of Wisdom damage. 6 Target takes 4 points of Charisma damage. 7 Target gains 1d4 negative levels. 8 Target is _[[conditions/Blinded|blinded]]_ or _[[conditions/Deafened|deafened]]_ for 1d4+1 rounds. 9 Target is _[[conditions/Confused|confused]]_ for 1d4 rounds, and all non-proteans that are within 20 feet are affected by _confusion_ (Will DC 23 negates). 10 Target is struck by a _[[spells/Fireball|fireball]]_ (Reflex DC 22 half) centered on its location that deals acid damage rather than fire. 11 Target is affected by greater _[[spells/Dispel Magic|dispel magic]]_ (CL 20th). 12 Target is _[[conditions/Sickened|sickened]]_ for 1d4+1 rounds. 13 Target is _[[conditions/Nauseated|nauseated]]_ for 1d4+1 rounds. 14 Target is _[[conditions/Staggered|staggered]]_ for 1d4+1 rounds. 15 Target is _[[conditions/Stunned|stunned]]_ for 1d4+1 rounds. 16 Target gains 8d6 temporary hit points. 17 Target is affected by a _heal_ spell (CL 20th). 18 Target is permanently turned to stone. 19 Target is temporarily shifted outside of the normal flow of time, as per _[[spells/Temporal Stasis|temporal stasis]]_, for 1d3 rounds. 20 Target is affected by _[[spells/Imprisonment|imprisonment]]_ (CL 20th), and a keketar protean loyal to the izfiitar appears in the target’s place.

**Kiss of the Speakers (Ex)** Moment by moment, an izfiitar tinkers with the myriad possibilities in which it can act or move, granting it the prescience to choose whichever possible moment best suits it. As a move action once every other round, an izfiitar can grant itself one of the following options on its next round’s action: double all of its speeds for 1 round, gain the ability to roll one d20 roll twice in the next round and choose which result to use, or gain an additional standard action that can be used only to activate a spell-like ability.

**Reshape Reality (Sp)** This ability functions as _[[spells/Mirage Arcana|mirage arcana]]_ heightened to a 9th-level spell, except the changes created are quasi-real, like those created by _[[spells/Shadow Conjuration|shadow conjuration]]_. A creature that interacts with reshaped reality can attempt a DC 26 Will save to see through the illusion. Terrain thus created can provide concealment, and against foes who fail the Will save to see through it, reshaped reality can provide cover. For disbelievers, quasi-real objects and terrain have only 20% of the normal hardness and hit points, and break DCs are 10 lower than normal. Damage caused by dangerous terrain can’t exceed 5d6 points of damage per round (1d6 per round against disbelievers). This ability can’t damage existing structures, nor does it function in areas where _[[items/Weapon Magic Abilities/Planar|planar]]_ travel is prohibited.

##### Description

While the keketar proteans (Pathfinder RPG Bestiary 2 215) hold vague ideological sway over their kind’s infinite choruses, the izfiitars loom above them, cardinals among the _[[items/Weapon Magic Abilities/Slithering|slithering]]_ clergy. Aloof and distant even compared to the keketars, izfiitars rarely venture beyond the Maelstrom’s deepest reaches, content to divine the will of the plane’s unknowable dualistic godhead, the Speakers of the Depths.

Bound to a single chorus, izfiitars are and yet are not distinct from the keketars who pay them obeisance, leading many to speculate that they are essentially elevated keketars, chosen for reasons _[[monsters/Unknown|unknown]]_ and propelled along a path of _[[feats/Apotheosis|apotheosis]]_ either by the Maelstrom itself or by one of the so-called protean lords. Yet their position remains paradoxical, befitting the Maelstrom’s rejection of stability and consistency. Not every chorus contains an izfiitar, while some contain multiple, and the size and influence of any given chorus is entirely independent of their presence.

Although smaller in size than keketars, izfiitars have monstrous physical attacks and stupendous magical powers. They wield a more powerful version of lesser proteans’ warpwave, as well as abilities that bend reality and alter probability, focused on the proteans’ desire to return all of reality to the _freedom_ of pure, _[[items/Armor Magic Abilities/Unbound|unbound]]_ chaos.