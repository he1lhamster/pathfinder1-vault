---
cssclass: [monsters]
title1: Dragon (Planar, Havoc), Adult Havoc Dragon
desc_short: This dragon's scales and insectile wings dance with color, while itswhiplike
  tail waves as if stirred by an unseen breeze.
title2: Adult Havoc Dragon
CR: 16
sources:
- name: Bestiary 6
  page: 100
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 76800
alignment: CG
size: Huge
type: dragon
subtypes:
- chaotic
- extraplanar
- good
initiative:
  bonus: 6
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 26
AC:
  AC: 32
  touch: 10
  flat_footed: 30
  components:
    dex: 2
    natural: 22
    size: -2
HP:
  HP: 230
  long: 20d12+100
saves:
  fort: 17
  ref: 16
  will: 16
DR:
- amount: 5
  weakness: lawful
immunities:
- confused
- nauseated
- paralysis
- sickened,sleep
- sonic
SR: 27
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +27 (2d8+12/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
      attack: bite
      bonus:
      - 27
    - text: 2 claws +26 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 26
    - text: tail slap+25 (2d6+12/19-20 plus trip)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
        - effect: trip
      attack: tail slap
      bonus:
      - 25
    - text: 2 wings +24 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 24
  special:
  - breath weapon (50-ft. cone, 12d10 sonicdamage, Reflex DC 25 half)
  - crush
  - delirium breath
  - lashing tail
space: 15
reach: 10
reach_other: 15 ft. with bite and tail slap
spells:
  entries:
  - name: charm monster
    source: Oracle
    level: 3
    DC: 18
  - name: dispel magic
    source: Oracle
    level: 3
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: grace
    source: Oracle
    level: 2
  - name: sound burst
    source: Oracle
    level: 2
    DC: 18
  - name: detect evil
    source: Oracle
    level: 1
  - name: divine favor
    source: Oracle
    level: 1
  - name: entropic shield
    source: Oracle
    level: 1
  - name: grease
    source: Oracle
    level: 1
    DC: 15
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: mage hand
    source: Oracle
    level: 0
  - name: open/close
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 7
    concentration: 13
    slots:
      3: 5
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 27
  DEX: 14
  CON: 21
  INT: 20
  WIS: 19
  CHA: 22
BAB: 20
CMB: 30
CMD: 42
CMD_other: 46 vs. trip
feats:
- name: Critical Focus
- name: Improved Critical (bite)
- name: Improved Critical (tail slap)
- name: ImprovedInitiative
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (bite)
- name: Weapon Focus (tail slap)
- name: Wingover
skills:
  Bluff: 29
  Diplomacy: 29
  Fly: 17
  Knowledge (local,planes): 28
  Perception: 27
  Perform (comedy): 29
  Perform (sing): 29
  Sense Motive: 27
  Spellcraft: 28
  Use Magic Device: 29
languages:
- Celestial
- Common
- Draconic
- Sylvan
special_qualities:
- change shape (3/day)
- planar infusion (180 ft.)
desc_long: Despite their best intentions,the appropriately named havocdragons often
  cause collateraldamage as they develop whimsicalwonderlands of revelry and relaxation.

---

# Dragon (Planar, Havoc), Adult Havoc Dragon
This dragon’s scales and insectile wings dance with color, while its

whiplike tail waves as if stirred by an _[[items/Weapon Magic Abilities/Unseen|unseen]]_ _[[spells/Breeze|breeze]]_.
**Source** Bestiary 6 pg. 100
**XP** 76,800

CG Huge dragon (chaotic, extraplanar, good)
**Init** +6; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +27
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 26)

##### Defense

**AC** 32, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+2 Dex, +22 natural, –2 size)
**hp** 230 (20d12+100)
**Fort** +17, **Ref** +16, **Will** +16
**DR** 5/lawful; **Immune** _[[conditions/Confused|confused]]_, _[[conditions/Nauseated|nauseated]]_, _[[universal monster rules/Paralysis|paralysis]]_, _[[conditions/Sickened|sickened]]_,

sleep, sonic; **SR** 27

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +27 (2d8+12/19–20), 2 claws +26 (2d6+8), tail slap

+25 (2d6+12/19–20 plus _[[universal monster rules/Trip|trip]]_), 2 wings +24 (1d8+4)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite and tail slap)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d10 sonic

damage, Reflex DC 25 half), crush, delirium breath, _[[feats/Lashing Tail|lashing tail]]_
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 7th; concentration +13)
3rd (5)—_[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_ 
2nd (8)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Grace|grace]]_, _[[spells/Sound Burst|sound burst]]_ (DC 18) 
1st (8)—_[[spells/Detect Evil|detect evil]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Grease|grease]]_ (DC 15), _[[spells/Obscuring Mist|obscuring mist]]_ 
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, open/close, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 27, **Dex** 14, **Con** 21, **Int** 20, **Wis** 19, **Cha** 22
**Base Atk** +20; **CMB** +30; **CMD** 42 (46 vs. _trip_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, tail slap), Improved

Initiative, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, tail slap), _[[feats/Wingover|Wingover]]_
**Skills** Bluff +29, Diplomacy +29, Fly +17, Knowledge (local,

planes) +28, Perception +27, Perform (comedy, sing) +29,

Sense Motive +27, Spellcraft +28, Use Magic Device +29
**Languages** Celestial, Common, Draconic, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (3/day), _[[feats/Planar Infusion|planar infusion]]_ (180 ft.)

##### Description

Despite their best intentions,

the appropriately named havoc

dragons often cause collateral

damage as they develop whimsical

wonderlands of revelry and relaxation.