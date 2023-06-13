---
cssclass: [monsters]
title1: Dragon (Gold), Ancient Gold Dragon
title2: Ancient Gold Dragon
CR: 20
sources:
- name: Pathfinder RPG Bestiary
  page: 109
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 307200
alignment: LG
size: Gargantuan
type: dragon
subtypes:
- fire
initiative:
  bonus: -1
senses:
  dragon senses: true
auras:
- name: fire
- name: frightful presence
  radius: 300
  DC: 30
AC:
  AC: 39
  touch: 5
  flat_footed: 39
  components:
    dex: -1
    natural: 34
    size: -4
HP:
  HP: 377
  long: 26d12+208
saves:
  fort: 23
  ref: 14
  will: 24
DR:
- amount: 15
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 31
weaknesses:
- vulnerability to cold
speeds:
  base: 60
  fly: 250
  fly_maneuverability: clumsy
  swim: 60
attacks:
  melee:
  - - text: bite +36 (4d6+21/19-20)
      entries:
      - - damage: 4d6+21
          crit_range: 19-20
      attack: bite
      bonus:
      - 36
    - text: 2 claws +36 (2d8+14/19-20)
      entries:
      - - damage: 2d8+14
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 36
    - text: 2 wings +34 (2d6+7/19-20)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
      count: 2
      attack: wings
      bonus:
      - 34
    - text: tail +34 (2d8+21/19-20)
      entries:
      - - damage: 2d8+21
          crit_range: 19-20
      attack: tail
      bonus:
      - 34
  special:
  - breath weapon (60-ft. cone, DC 31, 20d10 fire)
  - crush
  - tail sweep
  - weaken breath
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: bless
    source: default
    freq: At will
  - name: daylight
    source: default
    freq: At will
  - name: detect evil
    source: default
    freq: At will
  - name: geas/quest
    source: default
    freq: At will
  - name: sunburst
    source: default
    freq: At will
    DC: 25
  sources:
  - name: default
    CL: 26
spells:
  entries:
  - name: greater teleport
    source: '?'
    level: 7
  - name: resurrection
    source: '?'
    level: 7
  - name: antimagic field
    source: '?'
    level: 6
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: heal
    source: '?'
    level: 6
  - name: dispel evil
    source: '?'
    level: 5
  - name: plane shift
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: true seeing
    source: '?'
    level: 5
  - name: divination
    source: '?'
    level: 4
  - name: restoration
    source: '?'
    level: 4
  - name: spell immunity
    source: '?'
    level: 4
  - name: stoneskin
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: invisibility purge
    source: '?'
    level: 3
  - name: prayer
    source: '?'
    level: 3
  - name: aid
    source: '?'
    level: 2
  - name: cure moderate wounds
    source: '?'
    level: 2
  - name: lesser restoration
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: silence
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: divine favor
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: shield of faith
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  - name: 6 more
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 15
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 39
  DEX: 8
  CON: 27
  INT: 24
  WIS: 25
  CHA: 24
BAB: 26
CMB: 44
CMD: 53
CMD_other: 57 vs. trip
feats:
- name: Alertness
- name: Critical Focus
- name: Extend Spell
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Critical (wing)
- name: Improved Critical (tail)
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Quicken Spell
- name: Staggering Critical
- name: Vital Strike
skills:
  Diplomacy: 36
  Fly: 13
  Heal: 36
  Knowledge (arcana): 36
  Knowledge (history): 36
  Knowledge (local): 36
  Knowledge (nobility): 36
  Knowledge (planes): 36
  Knowledge (religion): 36
  Perception: 40
  Sense Motive: 40
  Spellcraft: 36
  Swim: 51
languages:
- Celestial
- Common
- Draconic
- 5 more
special_qualities:
- change shape
- detect gems
- fast flight
- luck
ecology:
  environment: warm plains
desc_long: Gold dragons are the epitome of virtue. Other metallic dragons revere their
  gold cousins as the agents of divine forces and the paragons of dragonkind, and
  often seek them for advice or aid.

---

# Dragon (Gold), Ancient Gold Dragon

**Source** Pathfinder RPG Bestiary pg. 109
**XP** 307,200

LG Gargantuan dragon (fire)
**Init** –1; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +40
**Aura** fire, _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 30)

##### Defense

**AC** 39, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 39 (–1 Dex, +34 natural, –4 size)
**hp** 377 (26d12+208)
**Fort** +23, **Ref** +14, **Will** +24
**DR** 15/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 31
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 60 ft., fly 250 ft. (clumsy), swim 60 ft.
**Melee** bite +36 (4d6+21/19–20), 2 claws +36 (2d8+14/19–20), 2 wings +34 (2d6+7/19–20), tail +34 (2d8+21/19–20)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, DC 31, 20d10 fire), crush, tail sweep, weaken breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 26th)
At will—_[[spells/Bless|bless]]_, _[[spells/Daylight|daylight]]_, _[[spells/Detect Evil|detect evil]]_, geas/quest, _[[spells/Sunburst|sunburst]]_ (DC 25)
**Spells Known **(CL 15th)
7th (5/day)—greater teleport, _[[spells/Resurrection|resurrection]]_
6th (7/day)—_[[spells/Antimagic Field|antimagic field]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heal|heal]]_
5th (7/day)—_[[spells/Dispel Evil|dispel evil]]_, _[[spells/Plane Shift|plane shift]]_, teleport, _[[spells/True Seeing|true seeing]]_
4th (7/day)—_[[spells/Divination|divination]]_, _[[spells/Restoration|restoration]]_, _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_dispel magic_, _[[spells/Haste|haste]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Prayer|prayer]]_
2nd (8/day)—aid, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, lesser _restoration_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Silence|silence]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Shield|shield]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mending|mending]]_, stabilize, 6 more

##### Statistics
**Str** 39, **Dex** 8, **Con** 27, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +26; **CMB** +44; **CMD** 53 (57 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claw, wing, tail), _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Diplomacy +36, Fly +13, _Heal_ +36, Knowledge (arcana, history, local, nobility, planes, religion) +36, Perception +40, Sense Motive +40, Spellcraft +36, Swim +51
**Languages** Celestial, Common, Draconic, 5 more
**SQ** _[[universal monster rules/Change Shape|change shape]]_, detect gems, fast _[[universal monster rules/Flight|flight]]_, luck

##### Ecology

**Environment** warm plains

Gold dragons are the epitome of _[[spells/Virtue|virtue]]_. Other metallic dragons revere their gold cousins as the agents of divine forces and the paragons of dragonkind, and often seek them for advice or aid.