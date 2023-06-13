---
cssclass: [monsters]
title1: Dragon (Bronze), Ancient Bronze Dragon
title2: Ancient Bronze Dragon
CR: 18
sources:
- name: Pathfinder RPG Bestiary
  page: 105
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 153600
alignment: LG
size: Gargantuan
type: dragon
subtypes:
- water
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: electricity aura
- name: frightful presence
  radius: 300
  DC: 29
AC:
  AC: 37
  touch: 5
  flat_footed: 37
  components:
    dex: -1
    natural: 32
    size: -4
HP:
  HP: 324
  long: 24d12+168
saves:
  fort: 21
  ref: 13
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- electricity
- paralysis
- sleep
SR: 29
speeds:
  base: 40
  fly: 250
  fly_other: clum.
  sw.: 60
attacks:
  melee:
  - - text: bite +32 (4d6+18/19-20)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d8+12/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 30
    - text: tail slap +30 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 30
  special:
  - br. weapon (120-ft. line, DC 29, 20d6 elect.)
  - crush
  - repul. breath
  - tail sweep
  - vortex
space: 20
reach: 15
reach_other: 20 ft. w/bite
spell_like_abilities:
  entries:
  - name: control water
    source: default
    freq: At will
  - name: create food and water
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: fog cloud
    source: default
    freq: At will
  - name: speak with animals
    source: default
    freq: At will
  sources:
  - name: default
    CL: 24
spells:
  entries:
  - name: spell turning
    source: '?'
    level: 7
  - name: statue
    source: '?'
    level: 7
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: mass suggestion
    source: '?'
    level: 6
    DC: 23
  - name: mislead
    source: '?'
    level: 6
  - name: dismissal
    source: '?'
    level: 5
  - name: interposing hand
    source: '?'
    level: 5
  - name: mind fog
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: dimension door
    source: '?'
    level: 4
  - name: ice storm
    source: '?'
    level: 4
  - name: solid fog
    source: '?'
    level: 4
  - name: stoneskin
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: heroism
    source: '?'
    level: 3
  - name: slow
    source: '?'
    level: 3
    DC: 20
  - name: suggestion
    source: '?'
    level: 3
  - name: blur
    source: '?'
    level: 2
  - name: gust of wind
    source: '?'
    level: 2
  - name: invisibility
    source: '?'
    level: 2
  - name: mirror image
    source: '?'
    level: 2
  - name: web
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  - name: 2 more
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
  STR: 35
  DEX: 8
  CON: 25
  INT: 24
  WIS: 25
  CHA: 24
BAB: 24
CMB: 40
CMD: 49
CMD_other: 53 vs. trip
feats:
- name: Alertness
- name: Cleave
- name: Flyby Attack
- name: Great Cleave
- name: Hover
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Diplomacy: 34
  Fly: 10
  Handle Animal: 31
  Heal: 34
  Intimidate: 34
  Knowledge (arcana): 34
  Knowledge (geography): 34
  Knowledge (history): 34
  Perception: 38
  Sense Motive: 38
  Spellcraft: 34
  Stealth: 14
  Swim: 47
languages:
- Aquan
- Common
- Draconic
- Elven
- Gnome
- 3 more
special_qualities:
- change shape
- water breathing
- wave mastery
ecology:
  environment: temperate coastlines
desc_long: 'Bronze dragons have been known to ally with travelers and adventurers
  if the cause and reward is right and just. '

---

# Dragon (Bronze), Ancient Bronze Dragon

**Source** Pathfinder RPG Bestiary pg. 105
**XP** 153,600

LG Gargantuan dragon (water)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +38
**Aura** electricity aura, _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 29)

##### Defense

**AC** 37, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–1 Dex, +32 natural, –4 size)
**hp** 324 (24d12+168)
**Fort** +21, **Ref** +13, **Will** +21
**DR** 15/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., fly 250 ft. (clum.), sw. 60 ft.
**Melee** bite +32 (4d6+18/19–20), 2 claws +32 (2d8+12/19–20), 2 wings +30 (2d6+6), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. w/bite)
**Special Attacks** br. weapon (120-ft. line, DC 29, 20d6 elect.), crush, repul. breath, tail sweep, _[[spells/Vortex|vortex]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th)
At will—_[[spells/Control Water|control water]]_, _[[spells/Create Food and Water|create food and water]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Speak with Animals|speak with animals]]_
**Spells Known **(CL 15th)
7th (5/day)—_[[spells/Spell Turning|spell turning]]_, _[[spells/Statue|statue]]_
6th (7/day)—greater _[[spells/Dispel Magic|dispel magic]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 23), _[[spells/Mislead|mislead]]_
5th (7/day)—_[[spells/Dismissal|dismissal]]_, _[[spells/Interposing Hand|interposing hand]]_, _[[spells/Mind Fog|mind fog]]_, teleport
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Solid Fog|solid fog]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_dispel magic_, _[[spells/Heroism|heroism]]_, _[[spells/Slow|slow]]_ (DC 20), _suggestion_
2nd (8/day)—_[[spells/Blur|blur]]_, _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, web
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_, 2 more

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +24; **CMB** +40; **CMD** 49 (53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Diplomacy +34, Fly +10, Handle Animal +31, _[[spells/Heal|Heal]]_ +34, Intimidate +34, Knowledge (arcana, geography, history) +34, Percep. +38, S. Motive +38, Spellcraft +34, Stealth +14, Swim +47
**Languages** Aquan, Common, Draconic, Elven, Gnome, 3 more
**SQ** _[[universal monster rules/Change Shape|change shape]]_, _[[universal monster rules/Water Breathing|water breathing]]_, wave mastery

##### Ecology

**Environment** temperate coastlines

Bronze dragons have been known to ally with travelers and adventurers if the cause and reward is right and just.