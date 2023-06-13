---
cssclass: [monsters]
title1: Dragon (Imperial, Sky), Ancient Sky Dragon
title2: Ancient Sky Dragon
CR: 18
sources:
- name: Bestiary 3
  page: 99
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 153600
alignment: LG
size: Gargantuan
type: dragon
subtypes:
- air
initiative:
  bonus: 3
senses:
  cloud sight: true
  dragon senses: true
AC:
  AC: 38
  touch: 5
  flat_footed: 38
  components:
    dex: -1
    natural: 33
    size: -4
HP:
  HP: 348
  long: 24d12+192
saves:
  fort: 21
  ref: 15
  will: 23
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
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +33 (4d6+18/19-20)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
      attack: bite
      bonus:
      - 33
    - text: 2 claws +32 (2d8+12)
      entries:
      - - damage: 2d8+12
      count: 2
      attack: claws
      bonus:
      - 32
    - text: gore +32 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: gore
      bonus:
      - 32
    - text: tail slap +30 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 30
  special:
  - breath weapon (60-ft. cone, 20d8 electricity, DC 29) crush (DC 29; 4d6+18)
  - grounding breath
  - primal lightning
  - tail sweep (DC 29; 2d6+18),
space: 20
reach: 15
reach_other: 20 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: call lightning storm
    source: default
    freq: At will
    DC: 22
  - name: control winds
    source: default
    freq: At will
    DC: 22
  - name: detect evil
    source: default
    freq: At will
  - name: feather fall
    source: default
    freq: At will
  - name: gust of wind
    source: default
    freq: At will
    DC: 19
  sources:
  - name: default
    CL: 24
    concentration: 31
spells:
  entries:
  - name: forcecage
    source: '?'
    level: 7
    DC: 24
  - name: mass hold person
    source: '?'
    level: 7
    DC: 24
  - name: acid fog
    source: '?'
    level: 6
  - name: chain lightning
    source: '?'
    level: 6
    DC: 23
  - name: legend lore
    source: '?'
    level: 6
  - name: break enchantment
    source: '?'
    level: 5
  - name: cloudkill
    source: '?'
    level: 5
    DC: 22
  - name: dream
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: dimension door
    source: '?'
    level: 4
  - name: greater invisibility
    source: '?'
    level: 4
  - name: ice storm
    source: '?'
    level: 4
  - name: rainbow pattern
    source: '?'
    level: 4
    DC: 21
  - name: blink
    source: '?'
    level: 3
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 20
  - name: sleet storm
    source: '?'
    level: 3
    DC: 20
  - name: wind wall
    source: '?'
    level: 3
  - name: daze monster
    source: '?'
    level: 2
    DC: 19
  - name: fog cloud
    source: '?'
    level: 2
  - name: glitterdust
    source: '?'
    level: 2
    DC: 19
  - name: invisibility
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: endure elements
    source: '?'
    level: 1
  - name: expeditious retreat
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
  - name: shocking grasp
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 17
  - name: detect magic
    source: '?'
    level: 0
  - name: disrupt undead
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
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
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
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Lunge
- name: Multiattack
- name: Skill Focus (Perception)
- name: Toughness
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Acrobatics: 22
    when jumping: 26
  Appraise: 33
  Diplomacy: 33
  Fly: 27
  Heal: 33
  Knowledge (arcana): 33
  Knowledge (geography): 33
  Knowledge (planes): 33
  Knowledge (religion): 33
  Perception: 39
  Perform (sing): 30
  Sense Motive: 33
  Spellcraft: 33
  Use Magic Device: 23
languages:
- Auran
- Celestial
- Common
- Draconic
- Elven
- Gnome
- Infernal
- Sylvan
special_qualities:
- borne aloft
- change shape
ecology:
  environment: temperate or warm mountains
  organization: solitary
  treasure_type: triple
desc_long: Benevolent and noble, sky dragons, or tienlungs, are fearsome champions
  of good and protectors of those in need. They are often sought out for their wise
  council, which they grant only to the deserving and true.

---

# Dragon (Imperial, Sky), Ancient Sky Dragon

**Source** Bestiary 3 pg. 99
**XP** 153,600

LG Gargantuan dragon (air)
**Init** +3; **Senses** cloud sight, _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +39

##### Defense

**AC** 38, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 38 (–1 Dex, +33 natural, –4 size)
**hp** 348 (24d12+192)
**Fort** +21, **Ref** +15, **Will** +23
**DR** 15/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., fly 250 ft. (perfect)
**Melee** bite +33 (4d6+18/19–20), 2 claws +32 (2d8+12), gore +32 (2d8+18), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d8 electricity, DC 29) crush (DC 29; 4d6+18), _[[items/Weapon Magic Abilities/Grounding|grounding]]_ breath, primal lightning, tail sweep (DC 29; 2d6+18),
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +31)
At will—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 22), _[[spells/Control Winds|control winds]]_ (DC 22), _[[spells/Detect Evil|detect evil]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 19)
**Spells Known **(caster level 15th; concentration +22)
7th (5/day)—_[[spells/Forcecage|forcecage]]_ (DC 24), mass _[[spells/Hold Person|hold person]]_ (DC 24)
6th (7/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Legend Lore|legend lore]]_
5th (7/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Cloudkill|cloudkill]]_ (DC 22), _[[spells/Dream|dream]]_, teleport
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 21)
3rd (8/day)—_[[spells/Blink|blink]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20), _[[spells/Sleet Storm|sleet storm]]_ (DC 20), _[[spells/Wind Wall|wind wall]]_
2nd (8/day)—_[[spells/Daze Monster|daze monster]]_ (DC 19), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 19), _invisibility_, _[[spells/Resist Energy|resist energy]]_
1st (8/day)—_[[spells/Endure Elements|endure elements]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +24; **CMB** +40; **CMD** 49 (53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +22 (+26 when jumping), Appraise +33, Diplomacy +33, Fly +27, _[[spells/Heal|Heal]]_ +33, Knowledge (arcana) +33, Knowledge (geography) +33, Knowledge (planes) +33, Knowledge (religion) +33, Perception +39, Perform (sing) +30, Sense Motive +33, Spellcraft +33, Use Magic Device +23
**Languages** Auran, Celestial, Common, Draconic, Elven, Gnome, Infernal, Sylvan
**SQ** borne aloft, _[[universal monster rules/Change Shape|change shape]]_

##### Ecology

**Environment** temperate or warm mountains
**Organization** solitary
**Treasure** triple

_[[items/Weapon Magic Abilities/Benevolent|Benevolent]]_ and noble, sky dragons, or tienlungs, are fearsome champions of good and protectors of those in need. They are often sought out for their wise council, which they grant only to the deserving and true.