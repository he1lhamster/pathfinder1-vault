---
cssclass: [monsters]
title1: Dragon (Imperial, Sea), Adult Sea Dragon
title2: Adult Sea Dragon
CR: 12
sources:
- name: Bestiary 3
  page: 96
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 19200
alignment: CG
size: Huge
type: dragon
subtypes:
- water
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 22
AC:
  AC: 28
  touch: 8
  flat_footed: 28
  components:
    natural: 20
    size: -2
HP:
  HP: 172
  long: 15d12+75
saves:
  fort: 16
  ref: 11
  will: 14
DR:
- amount: 5
  weakness: magic
immunities:
- electricity
- paralysis
- sleep
SR: 23
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
  swim: 80
attacks:
  melee:
  - - text: bite +22 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: bite
      bonus:
      - 22
    - text: 2 claws +22 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 22
    - text: gore +21 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: gore
      bonus:
      - 21
    - text: tail slap +19 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: tail slap
      bonus:
      - 19
  special:
  - breath weapon (50-ft. cone, 12d6 fire damage, DC 22)
  - crush (DC 22, 2d8+12)
  - torrent breath
space: 15
reach: 10
reach_other: 15 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: call lightning
    source: default
    freq: At will
    DC: 18
  - name: create water
    source: default
    freq: At will
  - name: hydraulic push
    source: default
    freq: At will
  sources:
  - name: default
    CL: 15
    concentration: 20
spells:
  entries:
  - name: hold person
    source: '?'
    level: 3
    DC: 18
  - name: sleet storm
    source: '?'
    level: 3
  - name: gust of wind
    source: '?'
    level: 2
    DC: 17
  - name: mirror image
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 16
  - name: chill touch
    source: '?'
    level: 1
  - name: color spray
    source: '?'
    level: 1
    DC: 16
  - name: expeditious retreat
    source: '?'
    level: 1
  - name: sleep
    source: '?'
    level: 1
    DC: 16
  - name: acid splash
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: ray of frost
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 27
  DEX: 10
  CON: 21
  INT: 20
  WIS: 21
  CHA: 20
BAB: 15
CMB: 25
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Alertness
- name: Great Fortitude
- name: Improved Initiative
- name: Lightning Reflexes
- name: Lunge
- name: Multiattack
- name: Weapon Focus (bite and claw)
skills:
  Diplomacy: 23
  Fly: 10
  Intimidate: 23
  Knowledge (arcana): 23
  Knowledge (geography): 23
  Knowledge (nature): 23
  Perception: 27
  Sense Motive: 27
  Stealth: 10
  Survival: 23
  Swim: 34
languages:
- Aquan
- Auran
- Celestial
- Common
- Draconic
- Elven
special_qualities:
- change shape
- unfettered swimmer
- water breathing
ecology:
  environment: any water
  organization: solitary
  treasure_type: triple
desc_long: Infused with the power of waves and storms, sea dragons-or jiaolungs, as
  they are known in many lands-are draconic protectors of oceans and their creatures.
  Possessing tempestuous natures, sea dragons wander widely, sometimes claiming thousands
  of miles of ocean and coastlines as their protectorates.

---

# Dragon (Imperial, Sea), Adult Sea Dragon

**Source** Bestiary 3 pg. 96
**XP** 19,200

CG Huge dragon (water)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +27
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 22)

##### Defense

**AC** 28, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+20 natural, –2 size)
**hp** 172 (15d12+75)
**Fort** +16, **Ref** +11, **Will** +14
**DR** 5/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 23

##### Offense
**Speed** 40 ft., fly 200 ft. (poor), swim 80 ft.
**Melee** bite +22 (2d8+12), 2 claws +22 (2d6+8), gore +21 (2d6+12), tail slap +19 (2d6+12)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d6 fire damage, DC 22), crush (DC 22, 2d8+12), torrent breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
At will—_[[spells/Call Lightning|call lightning]]_ (DC 18), _[[spells/Create Water|create water]]_, _[[spells/Hydraulic Push|hydraulic push]]_
**Spells Known **(CL 7th; concentration +12)
3rd (5/day)—_[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Sleet Storm|sleet storm]]_
2nd (7/day)—_[[spells/Gust Of Wind|gust of wind]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_, _[[spells/See Invisibility|see invisibility]]_
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Chill Touch|chill touch]]_, _[[spells/Color Spray|color spray]]_ (DC 16), _[[spells/Expeditious Retreat|expeditious retreat]]_, sleep (DC 16)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 27, **Dex** 10, **Con** 21, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +15; **CMB** +25; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite and claw)
**Skills** Diplomacy +23, Fly +10, Intimidate +23, Knowledge (arcana, geography, nature) +23, Perception +27, Sense Motive +27, Stealth +10, Survival +23, Swim +34
**Languages** Aquan, Auran, Celestial, Common, Draconic, Elven
**SQ** _[[universal monster rules/Change Shape|change shape]]_, unfettered swimmer, _[[universal monster rules/Water Breathing|water breathing]]_

##### Ecology

**Environment** any water
**Organization** solitary
**Treasure** triple

Infused with the power of waves and storms, sea dragons—or jiaolungs, as they are known in many lands—are draconic protectors of oceans and their creatures. Possessing tempestuous natures, sea dragons wander widely, sometimes claiming thousands of miles of ocean and coastlines as their protectorates.