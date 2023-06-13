---
cssclass: [monsters]
title1: Dragon (Primal, Cloud), Adult Cloud Dragon
title2: Adult Cloud Dragon
CR: 13
sources:
- name: Bestiary 2
  page: 96
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 25600
alignment: CN
size: Huge
type: dragon
subtypes:
- air
- extraplanar
initiative:
  bonus: 3
senses:
  dragon senses: true
  mist vision: true
auras:
- name: frightful presence
  radius: 180
  DC: 22
AC:
  AC: 29
  touch: 7
  flat_footed: 29
  components:
    dex: -1
    natural: 22
    size: -2
HP:
  HP: 184
  long: 16d12+80
saves:
  fort: 15
  ref: 9
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- electricity
- paralysis
- sleep
SR: 24
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
  swim: 40
attacks:
  melee:
  - - text: bite +22 (2d8+10/19-20)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
      attack: bite
      bonus:
      - 22
    - text: 2 claws +22 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: claws
      bonus:
      - 22
    - text: tail slap +19 (2d6+10)
      entries:
      - - damage: 2d6+10
      attack: tail slap
      bonus:
      - 19
    - text: 2 wings +19 (1d8+3)
      entries:
      - - damage: 1d8+3
      count: 2
      attack: wings
      bonus:
      - 19
  special:
  - breath weapon (50-ft. cone, 12d8 electricity, DC 23)
  - crush
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: At will
  - name: obscuring mist
    source: default
    freq: At will
  - name: solid fog
    source: default
    freq: At will
  sources:
  - name: default
    CL: 16
    concentration: 20
spells:
  entries:
  - name: blur
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 15
  - name: detect secret doors
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: message
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
    CL: 5
    concentration: 9
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 24
  DEX: 9
  CON: 21
  INT: 16
  WIS: 20
  CHA: 19
BAB: 16
CMB: 25
CMD: 34
CMD_other: 38 vs. trip
feats:
- name: Critical Focus
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Diplomacy)
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
skills:
  Appraise: 22
  Diplomacy: 29
  Fly: 10
  Intimidate: 23
  Knowledge (planes): 22
  Perception: 24
  Sense Motive: 24
  Stealth: 10
  Survival: 24
  Swim: 15
languages:
- Auran
- Common
- Draconic
- Elven
special_qualities:
- cloud form (16 rounds/day)
ecology:
  environment: any sky (Plane of Air)
  organization: solitary
  treasure_type: triple
desc_long: Cloud dragons stay out of the complicated political schemes and obsessions
  of other dragons (especially the chromatic dragons), preferring to live their lives
  freely and as the whim to travel strikes them. Exploration and viewing new lands
  from far above are the cloud dragon's greatest joy, rivaled only by speaking with
  new creatures and gaining exotic treasures from them. They keep lairs on high mountain
  peaks, but are often away on journeys of discovery, returning home only when they've
  claimed a new treasure that needs to be placed in safekeeping back home.

---

# Dragon (Primal, Cloud), Adult Cloud Dragon

**Source** Bestiary 2 pg. 96
**XP** 25,600

CN Huge dragon (air, extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, mist _[[spells/Vision|vision]]_; Perception +24
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 22)

##### Defense

**AC** 29, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 29 (–1 Dex, +22 natural, –2 size)
**hp** 184 (16d12+80)
**Fort** +15, **Ref** +9, **Will** +15
**DR** 5/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 24

##### Offense
**Speed** 40 ft., fly 200 ft. (poor), swim 40 ft.
**Melee** bite +22 (2d8+10/19–20), 2 claws +22 (2d6+7), tail slap +19 (2d6+10), 2 wings +19 (1d8+3)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d8 electricity, DC 23), crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +20)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Solid Fog|solid fog]]_
**Spells Known **(CL 5th; concentration +9)
2nd (5/day)—_[[spells/Blur|blur]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Detect Secret Doors|detect secret doors]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 24, **Dex** 9, **Con** 21, **Int** 16, **Wis** 20, **Cha** 19
**Base Atk** +16; **CMB** +25; **CMD** 34 (38 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Diplomacy), _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claws)
**Skills** Appraise +22, Diplomacy +29, Fly +10, Intimidate +23, Knowledge (planes) +22, Perception +24, Sense Motive +24, Stealth +10, Survival +24, Swim +15
**Languages** Auran, Common, Draconic, Elven
**SQ** cloud form (16 rounds/day)

##### Ecology

**Environment** any sky (Plane of Air)
**Organization** solitary
**Treasure** triple

Cloud dragons stay out of the complicated political schemes and obsessions of other dragons (especially the chromatic dragons), preferring to live their lives freely and as the whim to travel strikes them. Exploration and viewing new lands from far above are the cloud dragon’s greatest joy, rivaled only by speaking with new creatures and gaining exotic treasures from them. They keep lairs on high mountain peaks, but are often away on journeys of discovery, returning home only when they’ve claimed a new treasure that needs to be placed in safekeeping back home.