---
cssclass: [monsters]
title1: Orsheval
desc_short: This short, iron-skinned horse is surrounded by a flickering light. A
  preternatural intelligence glitters in its metallic golden eyes.
title2: Orsheval
CR: 4
sources:
- name: Inner Sea Gods
  page: 277
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 1200
alignment: LN
size: Medium
type: outsider
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    dex: 1
    natural: 5
HP:
  HP: 37
  long: 5d10+10
saves:
  fort: 6
  ref: 2
  will: 5
DR:
- amount: 5
  weakness: magic
immunities:
- electricity
resistances:
  cold: 10
  fire: 5
SR: 15
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +8 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 8
    - text: 2 hooves +3 (1d4+1 plus 1d4 electricity)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: electricity
      count: 2
      attack: hooves
      bonus:
      - 3
  special:
  - glittering radiance
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: light
    source: default
    freq: At will
  - name: mage hand
    source: default
    freq: At will
  - superscripts:
    - APG
    name: ant haul
    source: default
    freq: 3/day
  - name: bless
    source: default
    freq: 3/day
  - name: expeditious retreat
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 1/day
    other: self and rider only
  - name: lesser restoration
    source: default
    freq: 1/day
  - name: zone of truth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 6
    concentration: 6
ability_scores:
  STR: 17
  DEX: 12
  CON: 15
  INT: 10
  WIS: 13
  CHA: 10
BAB: 5
CMB: 8
CMB_other: +10 overrun
CMD: 19
CMD_other: 21 vs. overrun, 23 vs. trip
feats:
- name: Alertness
- name: Endurance
- is_bonus: true
  name: Improved Overrun
- name: Run
skills:
  Acrobatics: 4
  Appraise: 6
  Knowledge (local): 3
  Knowledge (nobility): 6
  Knowledge (planes): 6
  Knowledge (religion): 6
  Perception: 11
  Sense Motive: 11
  Swim: 5
languages:
- Celestial
- Infernal
- truespeech
ecology:
  environment: any (Axis)
  organization: solitary, pair, or team (3-8)
  treasure_type: standard
special_abilities:
  Glittering Radiance (Su): An orsheval usually glows with a golden light equivalent
    to that of a candle. In battle, its glow increases, filling the area within 5
    feet of it with shining motes. These motes cling to all creatures in the affected
    area, outlining them as glitterdust for 6 rounds. Opponents in the area must succeed
    at a DC 14 Will save or be blinded; a blinded creature may attempt a new saving
    throw each round at the end of its turn to end the blindness. The motes persist
    for 1 round after the orsheval moves from a square, leaving a trailing cloud that
    can affect creatures that move into the affected area. The orsheval can suppress
    or reactivate the glow or motes as a free action. The save DC is Constitution-based.
desc_long: |-
  An orsheval is a patient, hard-working servitor of Abadar. Accustomed to bearing heavy loads and vulnerable riders, an orsheval fulfills its duties without complaint, glad to contribute to the long-term goals of its master. Its iron body shines with light, and it uses this natural glow to lead allies or continue work long into the night. Although only the size of ponies, orshevals can look like miniature, sculpted versions of full-grown horses of any kind, but most prefer the shape of a sturdy draft horse or warhorse.

  An orsheval is as intelligent as a typical human and quite familiar with the nature of trade, bargaining, and spotting liars and cheats. Many arrogant mortals have ignored or insulted orshevals, thinking them dumb beasts, only to have the servitors chastise them using truespeech. When dealing with such people, an orsheval might become as stubborn as a true horse, relenting only if the offender apologizes and makes appropriate financial restitution to the church of Abadar.

  Most orshevals stand about 4 feet tall and weigh about 700 pounds.

---

# Orsheval
This short, iron-skinned _[[monsters/Horse|horse]]_ is surrounded by a flickering light. A preternatural intelligence glitters in its metallic golden eyes.
**Source** Inner Sea Gods pg. 277
**XP** 1,200

LN Medium outsider (extraplanar, lawful)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 Dex, +5 natural)
**hp** 37 (5d10+10)
**Fort** +6, **Ref** +2, **Will** +5
**DR** 5/magic; **Immune** electricity; **Resist** cold 10, fire 5; **SR** 15

##### Offense
**Speed** 50 ft.
**Melee** bite +8 (1d6+3), 2 hooves +3 (1d4+1 plus 1d4 electricity)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** glittering _[[items/Weapon/Radiance|radiance]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +6)
At will—light, _[[spells/Mage Hand|mage hand]]_
3/day—_[[spells/Ant Haul|ant haul]]_, _[[spells/Bless|bless]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_
1/day—_[[spells/Dimension Door|dimension door]]_ (self and rider only), lesser _[[spells/Restoration|restoration]]_, _[[spells/Zone of Truth|zone of truth]]_

##### Statistics
**Str** 17, **Dex** 12, **Con** 15, **Int** 10, **Wis** 13, **Cha** 10
**Base Atk** +5; **CMB** +8 (+10 overrun); **CMD** 19 (21 vs. overrun, 23 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Overrun|Improved Overrun]]_, Run
**Skills** Acrobatics +4, Appraise +6, Knowledge (local) +3, Knowledge (nobility) +6, Knowledge (planes) +6, Knowledge (religion) +6, Perception +11, Sense Motive +11, Swim +5
**Languages** Celestial, Infernal; truespeech

##### Ecology

**Environment** any (Axis)
**Organization** solitary, pair, or team (3–8)
**Treasure** standard

### Special Abilities

**Glittering _Radiance_ (Su)** An _[[monsters/Orsheval|orsheval]]_ usually glows with a golden light equivalent to that of a _[[items/Mundane/Candle|candle]]_. In battle, its glow increases, filling the area within 5 feet of it with shining motes. These motes cling to all creatures in the affected area, outlining them as _[[spells/Glitterdust|glitterdust]]_ for 6 rounds. Opponents in the area must succeed at a DC 14 Will save or be _[[conditions/Blinded|blinded]]_; a _blinded_ creature may attempt a new saving throw each round at the end of its turn to end the blindness. The motes persist for 1 round after the _orsheval_ moves from a square, leaving a trailing cloud that can affect creatures that move into the affected area. The _orsheval_ can suppress or reactivate the glow or motes as a free action. The save DC is Constitution-based.

##### Description

An _orsheval_ is a patient, hard-working servitor of Abadar. Accustomed to bearing heavy loads and vulnerable riders, an _orsheval_ fulfills its duties without complaint, glad to contribute to the long-term goals of its master. Its _[[spells/Iron Body|iron body]]_ shines with light, and it uses this natural glow to lead allies or continue work long into the night. Although only the size of ponies, orshevals can look like miniature, sculpted versions of full-grown horses of any kind, but most prefer the shape of a sturdy draft _horse_ or warhorse.

An _orsheval_ is as intelligent as a typical human and quite familiar with the nature of trade, bargaining, and spotting liars and cheats. Many arrogant mortals have ignored or insulted orshevals, thinking them dumb beasts, only to have the servitors _[[spells/Chastise|chastise]]_ them using truespeech. When dealing with such people, an _orsheval_ might become as stubborn as a true _horse_, relenting only if the offender apologizes and makes appropriate financial restitution to the church of Abadar.

Most orshevals stand about 4 feet tall and weigh about 700 pounds.