---
cssclass: [monsters]
title1: Dragon (White), Ancient White Dragon
title2: Ancient White Dragon
CR: 15
sources:
- name: Pathfinder RPG Bestiary
  page: 101
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 51200
alignment: CE
size: Huge
type: dragon
subtypes:
- cold
initiative:
  bonus: 4
senses:
  dragon senses: true
  snow vision: true
auras:
- name: cold
  radius: 10
  other:
  - 2d6 cold damage
- name: frightful presence
  radius: 300
  DC: 23
AC:
  AC: 37
  touch: 8
  flat_footed: 37
  components:
    natural: 29
    size: -2
HP:
  HP: 283
  long: 21d12+147
saves:
  fort: 19
  ref: 14
  will: 16
DR:
- amount: 15
  weakness: magic
immunities:
- cold
- paralysis
- sleep
SR: 26
weaknesses:
- vulnerability to fire
speeds:
  base: 30
  burrow: 30
  fly: 200
  fly_maneuverability: poor
  swim: 60
attacks:
  melee:
  - - text: bite +31 (2d8+16/19-20)
      entries:
      - - damage: 2d8+16
          crit_range: 19-20
      attack: bite
      bonus:
      - 31
    - text: 2 claws +30 (2d6+11)
      entries:
      - - damage: 2d6+11
      count: 2
      attack: claws
      bonus:
      - 30
    - text: 2 wings +25 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 25
    - text: tail slap +25 (2d6+16)
      entries:
      - - damage: 2d6+16
      attack: tail slap
      bonus:
      - 25
  special:
  - blizzard
  - breath weapon (50-ft. cone, DC 27, 20d4 cold)
  - crush
  - freezing fog (3/day, DC 19)
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: At will
  - name: gust of wind
    source: default
    freq: At will
  - name: wall of ice
    source: default
    freq: At will
    DC: 17
  sources:
  - name: default
    CL: 21
spells:
  entries:
  - name: charm monster
    source: '?'
    level: 4
    DC: 17
  - name: dimension door
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: displacement
    source: '?'
    level: 3
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 16
  - name: invisibility
    source: '?'
    level: 2
  - name: fog cloud
    source: '?'
    level: 2
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
    DC: 14
  - name: magic aura
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: acid splash
    source: '?'
    level: 0
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
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
  - name: ray of frost
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 9
    slots:
      4: 4
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 33
  DEX: 10
  CON: 25
  INT: 16
  WIS: 19
  CHA: 16
BAB: 21
CMB: 34
CMD: 44
CMD_other: 48 vs. trip
feats:
- name: Alertness
- name: Flyby Attack
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Sunder
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Fly: 16
  Intimidate: 27
  Knowledge (arcane): 27
  Knowledge (history): 27
  Perception: 32
  Sense Motive: 32
  Spellcraft: 27
  Stealth: 16
  Swim: 43
languages:
- Common
- Draconic
special_qualities:
- icewalking
- ice shape
ecology:
  environment: cold mountains
desc_long: Although most consider it to be the weakest and most feral of the chromatic
  dragons, the white dragon makes up for its lack of cunning with sheer ferocity.
  White dragons dwell on remote, frozen mountaintops and in arctic lowlands, making
  their home in glittering caves full of ice and snow. They prefer their meals completely
  frozen.

---

# Dragon (White), Ancient White Dragon

**Source** Pathfinder RPG Bestiary pg. 101
**XP** 51,200
CE Huge dragon (cold)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, snow _[[spells/Vision|vision]]_; Perception +32
**Aura** cold (10 ft., 2d6 cold damage), _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 23)

##### Defense

**AC** 37, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+29 natural, –2 size)
**hp** 283 (21d12+147)
**Fort** +19, **Ref** +14, **Will** +16
**DR** 15/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 26
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 200 ft. (poor), swim 60 ft.
**Melee** bite +31 (2d8+16/19–20), 2 claws +30 (2d6+11), 2 wings +25 (1d8+5), tail slap +25 (2d6+16)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** blizzard, _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 27, 20d4 cold), crush, freezing fog (3/day, DC 19)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 21st)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 17)
**Spells Known **(CL 9th)
4th (4/day)—_[[spells/Charm Monster|charm monster]]_ (DC 17), _[[spells/Dimension Door|dimension door]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 16)
2nd (7/day)—_[[spells/Invisibility|invisibility]]_, _fog cloud_, _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Grease|grease]]_ (DC 14), _[[spells/Magic Aura|magic aura]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_

##### Statistics
**Str** 33, **Dex** 10, **Con** 25, **Int** 16, **Wis** 19, **Cha** 16
**Base Atk** +21; **CMB** +34; **CMD** 44 (48 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Fly +16, Intimidate +27, Knowledge (arcane) +27, Knowledge (history) +27, Perception +32, Sense Motive +32, Spellcraft +27, Stealth +16, Swim +43
**Languages** Common, Draconic
**SQ** icewalking, ice shape

##### Ecology

**Environment** cold mountains

Although most consider it to be the weakest and most feral of the chromatic dragons, the white dragon makes up for its lack of _[[items/Weapon Magic Abilities/Cunning|cunning]]_ with sheer _[[universal monster rules/Ferocity|ferocity]]_. White dragons dwell on remote, frozen mountaintops and in arctic lowlands, making their home in glittering caves full of ice and snow. They prefer their meals completely frozen.