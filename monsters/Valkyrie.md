---
cssclass: [monsters]
title1: Valkyrie
desc_short: Surrounded by lightning, this impressive female warrior wears a gleaming
  golden breastplate and carries a shining spear.
title2: Valkyrie
CR: 12
sources:
- name: Bestiary 3
  page: 277
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 19200
alignment: CN
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  deathwatch: true
AC:
  AC: 27
  touch: 19
  flat_footed: 24
  components:
    armor: 8
    deflection: 6
    dex: 3
HP:
  HP: 168
  long: 16d10+80
saves:
  fort: 10
  ref: 13
  will: 15
DR:
- amount: 10
  weakness: cold iron and lawful
immunities:
- cold
- electricity
- poison
resistances:
  acid: 10
  fire: 10
SR: 23
speeds:
  base: 30
  fly: 100
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +2 returning spear +23/+18/+13/+8 (1d8+8/×3)
      entries:
      - - damage: 1d8+8
          crit_multiplier: 3
      attack: +2 returning spear
      bonus:
      - 23
      - 18
      - 13
      - 8
  ranged:
  - - text: +2 returning spear +22 (1d8+6/×3)
      entries:
      - - damage: 1d8+6
          crit_multiplier: 3
      attack: +2 returning spear
      bonus:
      - 22
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: death ward
    source: default
    freq: At will
  - name: gentle repose
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    other: self and mount only
  - name: call lightning storm
    source: default
    freq: 3/day
    DC: 21
  - name: divine power
    source: default
    freq: 3/day
  - name: geas/quest
    source: default
    freq: 3/day
  - name: breath of life
    source: default
    freq: 1/day
  - name: heal
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: sleipnir
      amount: 1
      chance: 100%
  sources:
  - name: default
    CL: 12
    concentration: 18
ability_scores:
  STR: 18
  DEX: 17
  CON: 20
  INT: 13
  WIS: 20
  CHA: 23
BAB: 16
CMB: 20
CMD: 39
feats:
- name: Mounted Combat
- name: Power Attack
- name: Ride-By Attack
- name: Skill Focus (Ride)
- name: Spirited Charge
- name: Trample
- name: Vital Strike
- name: Weapon Focus (spear)
skills:
  Fly: 27
  Handle Animal: 25
  Heal: 24
  Knowledge (planes): 20
  Perception: 24
  Ride: 28
  Sense Motive: 24
languages:
- Celestial
- Common
- tongues
special_qualities:
- battle trained
- choose the slain
- holy zeal
ecology:
  environment: any
  organization: solitary or ride (2-8 valkyries)
  treasure_type: triple
  treasure:
  - +2 breastplate
  - +2 returning spear
  - other treasure
special_abilities:
  Battle Trained (Ex): A valkyrie is proficient with all armor. Armor never impacts
    a valkyrie's speed, nor does a valkyrie take armor check penalties on Ride checks.
  Choose the Slain (Su): A valkyrie can draw the soul from a newly dead body and store
    it in her spear for transport to the Outer Planes. This functions as soul bind,
    but the dead creature must be willing to have its soul taken. If the creature
    is unwilling, this ability has no effect.
  Holy Zeal (Su): A valkyrie adds her Charisma modifier as a deflection bonus to her
    Armor Class.
desc_long: |-
  Valkyries are outsiders who scour the battlefields of the Material Plane for warriors of great prowess and legendary renown. With a glance, a valkyrie can tell who is near death and ready to give up life and who fights on to live another day, and can either claim the soul of the slain or aid the living to continue the fight.

  Valkyries are always female, and appear as strong and beautiful human, dwarven, or elven women. A human valkyrie is 6 feet tall and weighs close to 200 pounds.

  Valkyries serve a variety of deities, though they are most often associated with the gods of war, conflict, valor, and courage. Although capable combatants in their own right, valkyries are almost always encountered mounted, typically on flying steeds such as dragon horses, pegasi, or sleipnirs.

---

# Valkyrie
Surrounded by lightning, this impressive female warrior wears a gleaming golden _[[items/Armor/Breastplate|breastplate]]_ and carries a shining _[[items/Weapon/Spear|spear]]_.
**Source** Bestiary 3 pg. 277
**XP** 19,200

CN Medium outsider (extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_; Perception +24

##### Defense

**AC** 27, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+8 armor, +6 _[[spells/Deflection|deflection]]_, +3 Dex)
**hp** 168 (16d10+80)
**Fort** +10, **Ref** +13, **Will** +15
**DR** 10/cold iron and lawful; **Immune** cold, electricity, poison; **Resist** acid 10, fire 10; **SR** 23

##### Offense
**Speed** 30 ft., fly 100 ft. (perfect)
**Melee** +2 returning _spear_ +23/+18/+13/+8 (1d8+8/×3)
**Ranged** +2 returning _spear_ +22 (1d8+6/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +18)
Constant—_deathwatch_, _[[spells/Tongues|tongues]]_
At will—aid, _[[spells/Death Ward|death ward]]_, _[[spells/Gentle Repose|gentle repose]]_, _[[spells/Plane Shift|plane shift]]_ (self and _[[spells/Mount|mount]]_ only)
3/day—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 21), _[[spells/Divine Power|divine power]]_, geas/quest
1/day—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Heal|heal]]_, _[[universal monster rules/Summon|summon]]_ (level 8, 1 _[[monsters/Sleipnir|sleipnir]]_ 100%)

##### Statistics
**Str** 18, **Dex** 17, **Con** 20, **Int** 13, **Wis** 20, **Cha** 23
**Base Atk** +16; **CMB** +20; **CMD** 39
**Feats** _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Ride-By Attack|Ride-By Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Ride), _[[feats/Spirited Charge|Spirited Charge]]_, _[[universal monster rules/Trample|Trample]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Fly +27, Handle Animal +25, _Heal_ +24, Knowledge (planes) +20, Perception +24, Ride +28, Sense Motive +24
**Languages** Celestial, Common; _tongues_
**SQ** battle trained, choose the slain, holy zeal

##### Ecology

**Environment** any
**Organization** solitary or ride (2–8 valkyries)
**Treasure** triple (+2 _breastplate_, +2 returning _spear_, other treasure)

### Special Abilities

**Battle Trained (Ex)** A _[[monsters/Valkyrie|valkyrie]]_ is proficient with all armor. Armor never impacts a _valkyrie_’s speed, nor does a _valkyrie_ take armor check penalties on Ride checks.

**Choose the Slain (Su)** A _valkyrie_ can draw the soul from a newly dead body and store it in her _spear_ for transport to the Outer Planes. This functions as _[[spells/Soul Bind|soul bind]]_, but the dead creature must be willing to have its soul taken. If the creature is unwilling, this ability has no effect.

**Holy Zeal (Su)** A _valkyrie_ adds her Charisma modifier as a _deflection_ bonus to her Armor Class.

##### Description

Valkyries are outsiders who scour the battlefields of the Material Plane for warriors of great prowess and legendary _[[feats/Renown|renown]]_. With a glance, a _valkyrie_ can tell who is near death and ready to give up life and who fights on to live another day, and can either claim the soul of the slain or aid the living to continue the fight.

Valkyries are always female, and appear as strong and beautiful human, dwarven, or elven women. A human _valkyrie_ is 6 feet tall and weighs close to 200 pounds.

Valkyries serve a variety of deities, though they are most often associated with the gods of war, conflict, valor, and courage. Although capable combatants in their own right, valkyries are almost always encountered mounted, typically on flying steeds such as dragon horses, pegasi, or sleipnirs.