---
cssclass: [monsters]
title1: Demon, Vrolikai
desc_short: 'This black-skinned, bat-winged demon has four arms; a long, thin tail;
  and a leering, fanged face with dead, white eyes. '
title2: Vrolikai
CR: 19
sources:
- name: Bestiary 2
  page: 81
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 204800
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 120
  low-light vision: true
  true seeing: true
AC:
  AC: 35
  touch: 16
  flat_footed: 28
  components:
    dex: 6
    dodge: 1
    natural: 19
    size: -1
HP:
  HP: 332
  long: 19d10+228
saves:
  fort: 18
  ref: 17
  will: 17
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- death effects
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 30
speeds:
  base: 40
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +1 black flame knife +29/+24/+19/+14 (1d6+11/19-20 plus energy drain)
      entries:
      - - damage: 1d6+11
          crit_range: 19-20
        - effect: energy drain
      attack: +1 black flame knife
      bonus:
      - 29
      - 24
      - 19
      - 14
    - text: 3 +1 black flame knives +29 (1d6+6/19-20 plus energy drain)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
        - effect: energy drain
      count: 3
      attack: +1 black flame knives
      bonus:
      - 29
    - text: bite +23 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 23
    - text: sting +23 (1d6+5 plus madness)
      entries:
      - - damage: 1d6+5
        - effect: madness
      attack: sting
      bonus:
      - 23
  - - text: bite +28 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: bite
      bonus:
      - 28
    - text: 4 claws +28 (1d6+10)
      entries:
      - - damage: 1d6+10
      count: 4
      attack: claws
      bonus:
      - 28
    - text: sting +28 (1d6+10 plus madness)
      entries:
      - - damage: 1d6+10
        - effect: madness
      attack: sting
      bonus:
      - 28
  special:
  - black flame knives
  - death-stealing gaze
  - multiweapon mastery
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: enervation
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 23
  - name: quickened enervation
    source: default
    freq: 3/day
  - name: regenerate
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 20
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 27
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: marilith
      amount: 1
      chance: 50%
    - name: glabrezus
      amount: 1d4
      chance: 75%
  - name: symbol of death
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 19
    concentration: 27
ability_scores:
  STR: 30
  DEX: 23
  CON: 35
  INT: 22
  WIS: 23
  CHA: 26
BAB: 19
CMB: 30
CMD: 47
feats:
- name: Cleave
- name: Combat Expertise
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Improved Vital Strike
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (enervation)
- name: Vital Strike
skills:
  Acrobatics: 25
    jump: 29
  Bluff: 30
  Fly: 34
  Intimidate: 27
  Knowledge (arcana): 25
  Knowledge (planes): 28
  Perception: 36
  Sense Motive: 28
  Spellcraft: 25
  Stealth: 24
    in shadowy areas: 32
  Survival: 25
  Use Magic Device: 27
  _racial_mods:
    Perception:
      _: 8
    Stealth:
      in shadowy areas: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (the Abyss)
  organization: solitary
  treasure_type: double
special_abilities:
  Black Flame Knives (Su): A vrolikai can manifest daggers made of crystallized black
    flames in each of its four hands as a free action. These weapons function as +1
    daggers that bestow one permanent negative level on a successful hit. A DC 27
    Fortitude negates the negative level, although on a critical hit, no save is allowed.
    The save DC is Charisma-based.
  Death-Stealing Gaze (Su): 1 permanent negative level, 30 ft., Fort DC 27 negates.
    Creatures slain by these negative levels become juju zombies under the vrolikai's
    control. The save DC is Charisma-based.
  Madness (Su): A creature stung by a vrolikai's tail must make a DC 27 Will save
    to resist taking 1d6 points of Charisma drain and becoming confused for 1d4 rounds.
    On a successful save, the victim is instead staggered for 1d4 rounds as strange
    visions assault its mind. This is a mind-affecting effect. The save DC is Charisma-based.
  Multiweapon Mastery (Ex): A vrolikai never takes penalties on its attack roll when
    fighting with multiple weapons.
desc_long: A vrolikai is 14 feet tall but weighs only 500 pounds. Unlike other demons,
  it does not form from a sinful soul-it instead manifests from a nabasu demon that
  returns to the Abyss after growing to maturity on the Material Plane. Not all nabasus
  survive this transformation, but those who do become powerful indeed-vrolikai usually
  rule large regions of unclaimed Abyssal land, and often serve as assassins or ambassadors
  to demon lords in need of an agent in a distant realm.

---

# Demon, Vrolikai
This black-skinned, bat-winged demon has four arms; a long, thin tail; and a leering, fanged face with dead, white eyes.

**Source** Bestiary 2 pg. 81
**XP** 204,800
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +36

##### Defense

**AC** 35, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+6 Dex, +1 dodge, +19 natural, –1 size)
**hp** 332 (19d10+228)
**Fort** +18, **Ref** +17, **Will** +17
**DR** 15/cold iron and good; **Immune** death effects, electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 30

##### Offense
**Speed** 40 ft., fly 60 ft. (perfect)
**Melee** +1 black flame knife +29/+24/+19/+14 (1d6+11/19–20 plus _[[universal monster rules/Energy Drain|energy drain]]_), 3 +1 black flame knives +29 (1d6+6/19–20 plus _energy drain_), bite +23 (1d8+5), sting +23 (1d6+5 plus madness) or bite +28 (1d8+10), 4 claws +28 (1d6+10), sting +28 (1d6+10 plus madness)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** black flame knives, death-stealing _[[universal monster rules/Gaze|gaze]]_, _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +27)
Constant—_true seeing_
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Enervation|enervation]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 23)
3/day—quickened _enervation_, _[[spells/Regenerate|regenerate]]_, _[[spells/Silence|silence]]_ (DC 20), _[[spells/Vampiric Touch|vampiric touch]]_
1/day—mass _[[spells/Hold Monster|hold monster]]_ (DC 27), _[[universal monster rules/Summon|summon]]_ (level 6, 1 marilith 50% or 1d4 glabrezus 75%), _[[spells/Symbol of Death|symbol of death]]_ (DC 26)

##### Statistics
**Str** 30, **Dex** 23, **Con** 35, **Int** 22, **Wis** 23, **Cha** 26
**Base Atk** +19; **CMB** +30; **CMD** 47
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_enervation_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +25 (+29 _[[spells/Jump|jump]]_), Bluff +30, Fly +34, Intimidate +27, Knowledge (arcana) +25, Knowledge (planes) +28, Perception +36, Sense Motive +28, Spellcraft +25, Stealth +24 (+32 in shadowy areas), Survival +25, Use Magic Device +27; **Racial Modifiers** +8 Perception, +8 Stealth in shadowy areas
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (the Abyss)
**Organization** solitary
**Treasure** double

### Special Abilities

**Black Flame Knives (Su) **A vrolikai can manifest daggers made of crystallized black flames in each of its four hands as a free action. These weapons function as +1 daggers that bestow one permanent negative level on a successful hit. A DC 27 Fortitude negates the negative level, although on a critical hit, no save is allowed. The save DC is Charisma-based.

**Death-Stealing _Gaze_ (Su)** 1 permanent negative level, 30 ft., Fort DC 27 negates. Creatures slain by these negative levels become juju zombies under the vrolikai’s control. The save DC is Charisma-based.

**Madness (Su)** A creature stung by a vrolikai’s tail must make a DC 27 Will save to resist taking 1d6 points of Charisma drain and becoming _[[conditions/Confused|confused]]_ for 1d4 rounds. On a successful save, the victim is instead _[[conditions/Staggered|staggered]]_ for 1d4 rounds as strange visions assault its mind. This is a mind-affecting effect. The save DC is Charisma-based.

**_Multiweapon Mastery_ (Ex)** A vrolikai never takes penalties on its attack roll when fighting with multiple weapons.

##### Description

A vrolikai is 14 feet tall but weighs only 500 pounds. Unlike other demons, it does not form from a sinful soul—it instead manifests from a nabasu demon that returns to the Abyss after _[[items/Weapon Magic Abilities/Growing|growing]]_ to maturity on the Material Plane. Not all nabasus survive this _[[spells/Transformation|transformation]]_, but those who do become powerful indeed—vrolikai usually rule large regions of unclaimed Abyssal land, and often serve as assassins or ambassadors to demon lords in need of an agent in a distant realm.