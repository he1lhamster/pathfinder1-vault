---
cssclass: [monsters]
title1: Dragon (Primal, Cloud), Ancient Cloud Dragon
title2: Ancient Cloud Dragon
CR: 18
sources:
- name: Bestiary 2
  page: 97
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 153600
alignment: CN
size: Gargantuan
type: dragon
subtypes:
- air
- extraplanar
initiative:
  bonus: 2
senses:
  dragon senses: true
  mist vision: true
auras:
- name: frightful presence
  radius: 300
  DC: 28
AC:
  AC: 36
  touch: 4
  flat_footed: 36
  components:
    dex: -2
    natural: 32
    size: -4
HP:
  HP: 324
  long: 24d12+168
saves:
  fort: 21
  ref: 12
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
  fly_maneuverability: clumsy
  swim: 40
attacks:
  melee:
  - - text: bite +32 (4d6+16/19-20 plus 2d6 sonic)
      entries:
      - - damage: 4d6+16
          crit_range: 19-20
        - damage: 2d6
          type: sonic
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d8+11)
      entries:
      - - damage: 2d8+11
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +29 (2d8+16)
      entries:
      - - damage: 2d8+16
      attack: tail slap
      bonus:
      - 29
    - text: 2 wings +29 (2d6+5)
      entries:
      - - damage: 2d6+5
      count: 2
      attack: wings
      bonus:
      - 29
  special:
  - breath weapon (60-ft. cone, 20d8 electricity, DC 29)
  - crush
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
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
  - name: wind walk
    source: default
    freq: At will
  - name: cloudkill
    source: default
    freq: 3/day
    DC: 21
  sources:
  - name: default
    CL: 24
    concentration: 30
spells:
  entries:
  - name: chain lightning
    source: '?'
    level: 6
    DC: 22
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: cone of cold
    source: '?'
    level: 5
    DC: 21
  - name: dismissal
    source: '?'
    level: 5
    DC: 21
  - name: teleport
    source: '?'
    level: 5
  - name: elemental body I
    source: '?'
    level: 4
  - name: ice storm
    source: '?'
    level: 4
  - name: lesser geas
    source: '?'
    level: 4
    DC: 20
  - name: river of wind
    source: '?'
    level: 4
  - name: arcane sight
    source: '?'
    level: 3
  - name: cloak of winds
    source: '?'
    level: 3
  - name: stinking cloud
    source: '?'
    level: 3
    DC: 19
  - name: suggestion
    source: '?'
    level: 3
    DC: 19
  - name: eagle's splendor
    source: '?'
    level: 2
  - name: glitterdust
    source: '?'
    level: 2
    DC: 18
  - name: gust of wind
    source: '?'
    level: 2
  - name: locate object
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: alter winds
    source: '?'
    level: 1
  - name: charm person
    source: '?'
    level: 1
    DC: 17
  - name: detect secret doors
    source: '?'
    level: 1
  - name: erase
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
  - name: mage hand
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
  - name: resistance
    source: '?'
    level: 0
  - name: touch of fatigue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 13
    concentration: 19
    slots:
      6: 5
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 32
  DEX: 7
  CON: 25
  INT: 20
  WIS: 24
  CHA: 23
BAB: 24
CMB: 39
CMD: 47
CMD_other: 51 vs. trip
feats:
- name: Critical Focus
- name: Dazzling Display
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Diplomacy)
- name: Snatch
- name: Staggering Critical
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
skills:
  Appraise: 32
  Diplomacy: 39
  Fly: 11
  Intimidate: 33
  Knowledge (local): 32
  Knowledge (planes): 32
  Perception: 34
  Sense Motive: 34
  Stealth: 13
  Survival: 34
  Swim: 46
languages:
- Auran
- Common
- Draconic
- Elven
special_qualities:
- cloud form (24 rounds/day)
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

# Dragon (Primal, Cloud), Ancient Cloud Dragon

**Source** Bestiary 2 pg. 97
**XP** 153,600

CN Gargantuan dragon (air, extraplanar)
**Init** +2; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, mist _[[spells/Vision|vision]]_; Perception +34
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 28)

##### Defense

**AC** 36, touch 4, _[[conditions/Flat-Footed|flat-footed]]_ 36 (–2 Dex, +32 natural, –4 size)
**hp** 324 (24d12+168)
**Fort** +21, **Ref** +12, **Will** +21
**DR** 15/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy), swim 40 ft.
**Melee** bite +32 (4d6+16/19–20 plus 2d6 sonic), 2 claws +32 (2d8+11), tail slap +29 (2d8+16), 2 wings +29 (2d6+5)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d8 electricity, DC 29), crush, tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +30)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Solid Fog|solid fog]]_, _[[spells/Wind Walk|wind walk]]_
3/day—_[[spells/Cloudkill|cloudkill]]_ (DC 21)
**Spells Known **(CL 13th; concentration +19)
6th (5/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 22), greater _[[spells/Dispel Magic|dispel magic]]_
5th (7/day)—_[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Dismissal|dismissal]]_ (DC 21), teleport
4th (7/day)—_[[spells/Elemental Body I|elemental body I]]_, _[[spells/Ice Storm|ice storm]]_, lesser geas (DC 20), _[[spells/River of Wind|river of wind]]_
3rd (7/day)—_[[spells/Arcane Sight|arcane sight]]_, _[[spells/Cloak of Winds|cloak of winds]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 19), _[[spells/Suggestion|suggestion]]_ (DC 19)
2nd (8/day)—_[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Glitterdust|glitterdust]]_ (DC 18), _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Locate Object|locate object]]_, _[[spells/See Invisibility|see invisibility]]_
1st (8/day)—_[[spells/Alter Winds|alter winds]]_, _[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Detect Secret Doors|detect secret doors]]_, _[[spells/Erase|erase]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 32, **Dex** 7, **Con** 25, **Int** 20, **Wis** 24, **Cha** 23
**Base Atk** +24; **CMB** +39; **CMD** 47 (51 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Diplomacy), _[[feats/Snatch|Snatch]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claws)
**Skills** Appraise +32, Diplomacy +39, Fly +11, Intimidate +33, Knowledge (local) +32, Knowledge (planes) +32, Perception +34, Sense Motive +34, Stealth +13, Survival +34, Swim +46
**Languages** Auran, Common, Draconic, Elven
**SQ** cloud form (24 rounds/day)

##### Ecology

**Environment** any sky (Plane of Air)
**Organization** solitary
**Treasure** triple

Cloud dragons stay out of the complicated political schemes and obsessions of other dragons (especially the chromatic dragons), preferring to live their lives freely and as the whim to travel strikes them. Exploration and viewing new lands from far above are the cloud dragon’s greatest joy, rivaled only by speaking with new creatures and gaining exotic treasures from them. They keep lairs on high mountain peaks, but are often away on journeys of discovery, returning home only when they’ve claimed a new treasure that needs to be placed in safekeeping back home.