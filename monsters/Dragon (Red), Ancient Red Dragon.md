---
cssclass: [monsters]
title1: Dragon (Red), Ancient Red Dragon
title2: Ancient Red Dragon
CR: 19
sources:
- name: Pathfinder RPG Bestiary
  page: 99
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 204800
alignment: CE
size: Gargantuan
type: dragon
subtypes:
- fire
initiative:
  bonus: 3
senses:
  dragon senses: true
  smoke vision: true
auras:
- name: fire
- name: frightful presence
  radius: 300
  DC: 27
AC:
  AC: 38
  touch: 5
  flat_footed: 38
  components:
    dex: -1
    natural: 33
    size: -4
HP:
  HP: 362
  long: 25d12+200
saves:
  fort: 22
  ref: 13
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 30
weaknesses:
- vulnerability to cold
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +35 (4d6+21/19-20)
      entries:
      - - damage: 4d6+21
          crit_range: 19-20
      attack: bite
      bonus:
      - 35
    - text: 2 claws +35 (2d8+14)
      entries:
      - - damage: 2d8+14
      count: 2
      attack: claws
      bonus:
      - 35
    - text: 2 wings +33 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: wings
      bonus:
      - 33
    - text: tail slap +33 (2d8+21)
      entries:
      - - damage: 2d8+21
      attack: tail slap
      bonus:
      - 33
  special:
  - breath weapon (60-ft. cone, DC 30, 20d10 fire)
  - crush
  - manipulate flames
  - melt stone
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - name: find the path
    source: default
    freq: At will
  - name: pyrotechnics
    source: default
    freq: At will
    DC: 17
  - name: suggestion
    source: default
    freq: At will
    DC: 18
  - name: wall of fire
    source: default
    freq: At will
  sources:
  - name: default
    CL: 25
spells:
  entries:
  - name: limited wish
    source: '?'
    level: 7
  - name: spell turning
    source: '?'
    level: 7
  - name: antimagic field
    source: '?'
    level: 6
  - name: contingency
    source: '?'
    level: 6
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: polymorph
    source: '?'
    level: 5
  - name: telekinesis
    source: '?'
    level: 5
    DC: 20
  - name: teleport
    source: '?'
    level: 5
  - name: wall of force
    source: '?'
    level: 5
  - name: fear
    source: '?'
    level: 4
    DC: 19
  - name: fire shield
    source: '?'
    level: 4
  - name: greater invisibility
    source: '?'
    level: 4
  - name: stoneskin
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: displacement
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: tongues
    source: '?'
    level: 3
  - name: alter self
    source: '?'
    level: 2
  - name: detect thoughts
    source: '?'
    level: 2
    DC: 17
  - name: misdirection
    source: '?'
    level: 2
    DC: 17
  - name: resist energy
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: grease
    source: '?'
    level: 1
    DC: 16
  - name: magic missile
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 15
    slots:
      7: 4
      6: 6
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 39
  DEX: 8
  CON: 27
  INT: 20
  WIS: 21
  CHA: 20
BAB: 25
CMB: 43
CMD: 52
CMD_other: 56 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Quicken Spell
- name: Staggering Critical
- name: Vital Strike
skills:
  Appraise: 33
  Bluff: 33
  Diplomacy: 33
  Fly: 11
  Intimidate: 33
  Knowledge (arcana): 33
  Knowledge (history): 33
  Perception: 33
  Sense Motive: 33
  Spellcraft: 33
  Stealth: 15
ecology:
  environment: warm mountains
desc_long: Few creatures are more cruel and fearsome than the mighty red dragon. King
  of the chromatics, this terrible beast brings ruin and death to the lands that fall
  under its shadow.

---

# Dragon (Red), Ancient Red Dragon

**Source** Pathfinder RPG Bestiary pg. 99
**XP** 204,800
CE Gargantuan dragon (fire)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, smoke _[[spells/Vision|vision]]_; Perception +33
**Aura** fire, _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 27)

##### Defense

**AC** 38, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 38 (–1 Dex, +33 natural, –4 size)
**hp** 362 (25d12+200)
**Fort** +22, **Ref** +13, **Will** +21
**DR** 15/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 30
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy)
**Melee** bite +35 (4d6+21/19–20), 2 claws +35 (2d8+14), 2 wings +33 (2d6+7), tail slap +33 (2d8+21)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, DC 30, 20d10 fire), crush, manipulate flames, melt stone, tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th)
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Find the Path|find the path]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 17), _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Wall Of Fire|wall of fire]]_
**Spells Known **(CL 15th)
7th (4/day)—_[[spells/Limited Wish|limited wish]]_, _[[spells/Spell Turning|spell turning]]_
6th (6/day)—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Contingency|contingency]]_, greater _[[spells/Dispel Magic|dispel magic]]_
5th (7/day)—_[[spells/Polymorph|polymorph]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 20), teleport, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[universal monster rules/Fear|fear]]_ (DC 19), _[[spells/Fire Shield|fire shield]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_dispel magic_, _[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_, _[[spells/Tongues|tongues]]_
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Misdirection|misdirection]]_ (DC 17), _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Grease|grease]]_ (DC 16), _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 39, **Dex** 8, **Con** 27, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +25; **CMB** +43; **CMD** 52 (56 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Appraise +33, Bluff +33, Diplomacy +33, Fly +11, Intimidate +33, Knowledge (arcana) +33, Knowledge (history) +33, Perception +33, Sense Motive +33, Spellcraft +33, Stealth +15

##### Ecology

**Environment** warm mountains

Few creatures are more _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and fearsome than the mighty red dragon. _[[npcs/King|King]]_ of the chromatics, this terrible beast brings ruin and death to the lands that fall under its _[[items/Armor Magic Abilities/Shadow|shadow]]_.