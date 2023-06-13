---
cssclass: [monsters]
title1: Dragon (Imperial, Sea), Ancient Sea Dragon
title2: Ancient Sea Dragon
CR: 17
sources:
- name: Bestiary 3
  page: 97
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 102400
alignment: CG
size: Gargantuan
type: dragon
subtypes:
- water
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 28
AC:
  AC: 37
  touch: 5
  flat_footed: 37
  components:
    dex: -1
    natural: 32
    size: -4
HP:
  HP: 310
  long: 23d12+161
saves:
  fort: 22
  ref: 14
  will: 20
DR:
- amount: 15
  weakness: magic
immunities:
- electricity
- paralysis
- sleep
SR: 28
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
  swim: 100
attacks:
  melee:
  - - text: bite +32 (4d6+18)
      entries:
      - - damage: 4d6+18
      attack: bite
      bonus:
      - 32
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
    - text: tail slap +29 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 29
  special:
  - breath weapon (60-ft. cone, 20d6 fire damage, DC 28)
  - crush (DC 28, 4d6+18)
  - tail sweep (DC 28, 2d6+18)
  - torrent breath
space: 20
reach: 15
reach_other: 20 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: control water
    source: default
    freq: At will
  - name: call lightning
    source: default
    freq: At will
    DC: 20
  - name: create water
    source: default
    freq: At will
  - name: hydraulic push
    source: default
    freq: At will
  - name: water walk
    source: default
    freq: At will
  sources:
  - name: default
    CL: 23
    concentration: 30
spells:
  entries:
  - name: insanity
    source: '?'
    level: 7
    DC: 24
  - name: plane shift
    source: '?'
    level: 7
    DC: 24
  - name: chain lightning
    source: '?'
    level: 6
    DC: 23
  - name: freezing sphere
    source: '?'
    level: 6
    DC: 23
  - name: forceful hand
    source: '?'
    level: 6
  - name: cone of cold
    source: '?'
    level: 5
    DC: 22
  - name: dream
    source: '?'
    level: 5
  - name: mind fog
    source: '?'
    level: 5
    DC: 22
  - name: persistent image
    source: '?'
    level: 5
    DC: 22
  - name: black tentacles
    source: '?'
    level: 4
  - name: confusion
    source: '?'
    level: 4
    DC: 21
  - name: lesser geas
    source: '?'
    level: 4
    DC: 21
  - name: rainbow pattern
    source: '?'
    level: 4
    DC: 21
  - name: haste
    source: '?'
    level: 3
  - name: hold person
    source: '?'
    level: 3
    DC: 20
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 20
  - name: sleet storm
    source: '?'
    level: 3
  - name: gust of wind
    source: '?'
    level: 2
    DC: 19
  - name: mirror image
    source: '?'
    level: 2
  - name: obscure object
    source: '?'
    level: 2
  - name: scare
    source: '?'
    level: 2
    DC: 19
  - name: see invisibility
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 18
  - name: chill touch
    source: '?'
    level: 1
  - name: color spray
    source: '?'
    level: 1
    DC: 18
  - name: expeditious retreat
    source: '?'
    level: 1
  - name: sleep
    source: '?'
    level: 1
  - name: acid splash
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 17
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
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
  - name: resistance
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
BAB: 23
CMB: 39
CMD: 48
CMD_other: 52 vs. trip
feats:
- name: Alertness
- name: Flyby Attack
- name: Great Fortitude
- name: Improved Initiative
- name: Lightning Reflexes
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Snatch
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
- name: Weapon Focus (gore)
skills:
  Bluff: 33
  Diplomacy: 33
  Fly: 11
  Intimidate: 33
  Knowledge (arcana): 33
  Knowledge (geography): 33
  Knowledge (history): 33
  Knowledge (nature): 33
  Perception: 37
  Sense Motive: 37
  Stealth: 13
  Survival: 33
  Swim: 46
languages:
- Aquan
- Auran
- Celestial
- Common
- Draconic
- Elven
- Gnome
- Sylvan
special_qualities:
- change shape
- sea strider
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

# Dragon (Imperial, Sea), Ancient Sea Dragon

**Source** Bestiary 3 pg. 97
**XP** 102,400

CG Gargantuan dragon (water)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +37
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 28)

##### Defense

**AC** 37, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–1 Dex, +32 natural, –4 size)
**hp** 310 (23d12+161)
**Fort** +22, **Ref** +14, **Will** +20
**DR** 15/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 28

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy), swim 100 ft.
**Melee** bite +32 (4d6+18), 2 claws +32 (2d8+12), gore +32 (2d8+18), tail slap +29 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d6 fire damage, DC 28), crush (DC 28, 4d6+18), tail sweep (DC 28, 2d6+18), torrent breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +30)
At will—_[[spells/Control Water|control water]]_, _[[spells/Call Lightning|call lightning]]_ (DC 20), _[[spells/Create Water|create water]]_, _[[spells/Hydraulic Push|hydraulic push]]_, _[[spells/Water Walk|water walk]]_
**Spells Known **(CL 15th; concentration +22)
7th (5/day)—_[[spells/Insanity|insanity]]_ (DC 24), _[[spells/Plane Shift|plane shift]]_ (DC 24)
6th (7/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Freezing Sphere|freezing sphere]]_ (DC 23), _[[spells/Forceful Hand|forceful hand]]_
5th (7/day)—_[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Dream|dream]]_, _[[spells/Mind Fog|mind fog]]_ (DC 22), _[[spells/Persistent Image|persistent image]]_ (DC 22)
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Confusion|confusion]]_ (DC 21), lesser geas (DC 21), _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 21)
3rd (8/day)—_[[spells/Haste|haste]]_, _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20), _[[spells/Sleet Storm|sleet storm]]_
2nd (8/day)—_[[spells/Gust Of Wind|gust of wind]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_, _[[spells/Obscure Object|obscure object]]_, _[[spells/Scare|scare]]_ (DC 19), _[[spells/See Invisibility|see invisibility]]_
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Chill Touch|chill touch]]_, _[[spells/Color Spray|color spray]]_ (DC 18), _[[spells/Expeditious Retreat|expeditious retreat]]_, sleep
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +23; **CMB** +39; **CMD** 48 (52 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claws, gore)
**Skills** Bluff +33, Diplomacy +33, Fly +11, Intimidate +33, Knowledge (arcana, geography, history, nature) +33, Perception +37, Sense Motive +37, Stealth +13, Survival +33, Swim +46
**Languages** Aquan, Auran, Celestial, Common, Draconic, Elven, Gnome, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_, sea strider, unfettered swimmer, _[[universal monster rules/Water Breathing|water breathing]]_

##### Ecology

**Environment** any water
**Organization** solitary
**Treasure** triple

Infused with the power of waves and storms, sea dragons—or jiaolungs, as they are known in many lands—are draconic protectors of oceans and their creatures. Possessing tempestuous natures, sea dragons wander widely, sometimes claiming thousands of miles of ocean and coastlines as their protectorates.