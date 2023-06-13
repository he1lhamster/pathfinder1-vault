---
cssclass: [monsters]
title1: Qlippoth, Thulgant
desc_short: This monster has ten spidery legs, a head writhing with dripping tentacles
  above a clutch of red eyes, and three whipping stingers.
title2: Thulgant
CR: 18
sources:
- name: Bestiary 2
  page: 226
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 153600
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
- qlippoth
initiative:
  bonus: 12
senses:
  darkvision: 60
  true seeing: true
auras:
- name: cloak of chaos
  DC: 25
AC:
  AC: 33
  touch: 25
  flat_footed: 21
  components:
    deflection: 4
    dex: 12
    natural: 8
    size: -1
HP:
  HP: 290
  long: 20d10+180
  fast_healing: 10
saves:
  fort: 25
  ref: 30
  will: 18
defensive_abilities:
- displacement
- evasion
- freedom of movement
DR:
- amount: 15
  weakness: cold iron and lawful
immunities:
- acid
- cold
- poison
- mind-affecting effects
resistances:
  electricity: 10
  fire: 10
SR: 25 vs. lawful spells and creatures
speeds:
  base: 40
  climb: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 3 stings +27 (1d6+8/19-20 plus ability drain)
      entries:
      - - damage: 1d6+8
          crit_range: 19-20
        - effect: ability drain
      count: 3
      attack: stings
      bonus:
      - 27
    - text: 5 tentacles +22 (1d6+4 plus 2d6 acid)
      entries:
      - - damage: 1d6+4
        - damage: 2d6
          type: acid
      count: 5
      attack: tentacles
      bonus:
      - 22
  special:
  - horrific appearance (DC 27)
  - savage stingers
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 25
  - name: displacement
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 22
  - name: quickened dimension door
    source: default
    freq: 3/day
  - name: flesh to stone
    source: default
    freq: 3/day
    DC: 23
  - name: word of chaos
    source: default
    freq: 3/day
    DC: 24
  - name: binding
    source: default
    freq: 1/day
    DC: 25
  - name: plane shift
    source: default
    freq: 1/day
    DC: 24
  - name: telekinetic sphere
    source: default
    freq: 1/day
    DC: 25
  - name: temporal stasis
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 18
    concentration: 25
ability_scores:
  STR: 26
  DEX: 34
  CON: 29
  INT: 24
  WIS: 27
  CHA: 25
BAB: 20
CMB: 29
CMD: 55
CMD_other: 71 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Critical (sting)
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Quicken Spell-Like Ability (dimension door)
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 35
    jump: 39
  Bluff: 30
  Climb: 36
  Fly: 33
  Intimidate: 27
  Knowledge (arcana): 27
  Knowledge (history): 30
  Knowledge (planes): 30
  Perception: 31
  Sense Motive: 31
  Spellcraft: 27
  Stealth: 31
  Use Magic Device: 30
languages:
- Abyssal
- telepathy 100 ft.
special_qualities:
- demon hunter
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or patrol (3-4)
  treasure_type: double
special_abilities:
  Ability Drain (Su): A thulgant's stingers each drain a different ability score on
    a hit. One stinger drains 1d4 points of Strength, another drains 1d4 points of
    Dexterity, and the third drains 1d4 points of Charisma. Any sting's drain is negated
    by a DC 29 Fortitude save. The save DC is Constitution-based.
  Demon Hunter (Ex): A thulgant gains a +10 racial bonus on caster level checks to
    penetrate the spell resistance of any demon. Its attacks are treated as cold iron
    and good against demons.
  Horrific Appearance (Su): Creatures that succumb to a thulgant's horrific appearance
    are stunned for 1d4 rounds and take 1d6 points of Wisdom damage.
  Savage Stingers (Ex): If a thulgant hits a single target with all three stings in
    the same round, it tears through the victim's body, dealing an extra 3d6+12 points
    of damage and draining an additional 2 ability points from all six of the victim's
    ability scores. A single DC 29 Fortitude save negates all of this additional ability
    drain. The save DC is Constitution-based.
desc_long: |-
  The dreaded thulgant is among the most dangerous of the qlippoth, for it supports an array of deadly and painful physical attacks with a wide range of potent magical powers. Born from the cannibalistic orgies of augnagar qlippoth, each thulgant exists for one purpose only-the eradication of all demons from the Abyss.

  Yet thulgants do not spend all of their lives hunting and destroying demons. They rule horrific hives deep in the Abyss populated by all manner of hideous minions, many of which are bound into servitude via binding spells. These qlippoth are fond of decorating their lairs with petrified or enstasised victims of great power-the more powerful the victims, the greater the prestige held by the thulgant.

---

# Qlippoth, Thulgant
This monster has ten spidery legs, a head writhing with dripping tentacles above a clutch of red eyes, and three whipping stingers.
**Source** Bestiary 2 pg. 226
**XP** 153,600
CE Large outsider (chaotic, evil, extraplanar, qlippoth)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +31
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 25)

##### Defense

**AC** 33, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 deflection, +12 Dex, +8 natural, –1 size)
**hp** 290 (20d10+180); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +25, **Ref** +30, **Will** +18
**Defensive Abilities** _[[spells/Displacement|displacement]]_, evasion, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron and lawful; **Immune** acid, cold, poison, mind-affecting effects; **Resist** electricity 10, fire 10; **SR** 25 vs. lawful spells and creatures

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft., fly 60 ft. (good)
**Melee** 3 stings +27 (1d6+8/19–20 plus ability drain), 5 tentacles +22 (1d6+4 plus 2d6 acid)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** horrific appearance (DC 27), savage stingers
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +25)
Constant—_cloak of chaos_ (DC 25), _displacement_, _freedom of movement_, _true seeing_
At will—_[[spells/Dimension Door|dimension door]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 22)
3/day—quickened _dimension door_, _[[spells/Flesh to Stone|flesh to stone]]_ (DC 23), _[[spells/Word Of Chaos|word of chaos]]_ (DC 24)
1/day—_[[spells/Binding|binding]]_ (DC 25), _[[spells/Plane Shift|plane shift]]_ (DC 24), _[[spells/Telekinetic Sphere|telekinetic sphere]]_ (DC 25), _[[spells/Temporal Stasis|temporal stasis]]_ (DC 25)

##### Statistics
**Str** 26, **Dex** 34, **Con** 29, **Int** 24, **Wis** 27, **Cha** 25
**Base Atk** +20; **CMB** +29; **CMD** 55 (71 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (sting), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dimension door_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +35 (+39 _[[spells/Jump|jump]]_), Bluff +30, _Climb_ +36, Fly +33, Intimidate +27, Knowledge (arcana) +27, Knowledge (history) +30, Knowledge (planes) +30, Perception +31, Sense Motive +31, Spellcraft +27, Stealth +31, Use Magic Device +30
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[feats/Demon Hunter|demon hunter]]_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or patrol (3–4)
**Treasure** double

### Special Abilities

**Ability Drain (Su)** A thulgant’s stingers each drain a different ability score on a hit. One stinger drains 1d4 points of Strength, another drains 1d4 points of Dexterity, and the third drains 1d4 points of Charisma. Any sting’s drain is negated by a DC 29 Fortitude save. The save DC is Constitution-based.

**_Demon Hunter_ (Ex)** A thulgant gains a +10 racial bonus on caster level checks to penetrate the _[[universal monster rules/Spell Resistance|spell resistance]]_ of any demon. Its attacks are treated as cold iron and good against demons.

**Horrific Appearance (Su)** Creatures that succumb to a thulgant’s horrific appearance are _[[conditions/Stunned|stunned]]_ for 1d4 rounds and take 1d6 points of Wisdom damage.
**Savage Stingers (Ex)** If a thulgant hits a single target with all three stings in the same round, it tears through the victim’s body, dealing an extra 3d6+12 points of damage and draining an additional 2 ability points from all six of the victim’s ability scores. A single DC 29 Fortitude save negates all of this additional ability drain. The save DC is Constitution-based.

##### Description

The dreaded thulgant is among the most dangerous of the qlippoth, for it supports an array of _[[items/Weapon Magic Abilities/Deadly|deadly]]_ and painful physical attacks with a wide range of _[[items/Weapon Magic Abilities/Potent|potent]]_ magical powers. Born from the cannibalistic orgies of augnagar qlippoth, each thulgant exists for one purpose only—the eradication of all demons from the Abyss.

Yet thulgants do not spend all of their lives hunting and destroying demons. They rule horrific hives deep in the Abyss populated by all manner of hideous minions, many of which are bound into servitude via _binding_ spells. These qlippoth are fond of decorating their lairs with _[[conditions/Petrified|petrified]]_ or enstasised victims of great power—the more powerful the victims, the greater the prestige held by the thulgant.