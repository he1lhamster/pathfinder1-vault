---
cssclass: [monsters]
title1: Dragon (Outer, Void), Ancient Void Dragon
title2: Ancient Void Dragon
CR: 18
sources:
- name: Bestiary 4
  page: 73
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 153600
alignment: NE
size: Gargantuan
type: dragon
initiative:
  bonus: 4
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 300
  DC: 29
AC:
  AC: 38
  touch: 6
  flat_footed: 38
  components:
    natural: 32
    size: -4
HP:
  HP: 324
  long: 24d12+168
saves:
  fort: 21
  ref: 16
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- cold
- confusion
- insanity effects
- paralysis
- sleep
SR: 29
speeds:
  base: 40
  fly: 250
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +33 (4d6+18/19-20 plus obliterate)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
        - effect: obliterate
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
  - breath weapon (60-ft. Cone, 20d8 cold, DC 29)
  - crush
  - obliterate (DC 29)
  - suffocating breath (DC 29)
  - tail sweep
  - void gaze (DC 29)
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
  - name: ray of enfeeblement
    source: default
    freq: At will
    DC: 18
  - name: ray of exhaustion
    source: default
    freq: At will
    DC: 20
  - name: nightmare
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 24
    concentration: 31
spells:
  entries:
  - name: prismatic spray
    source: Sorcerer
    level: 7
    DC: 24
  - name: vision
    source: Sorcerer
    level: 7
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 23
  - name: eyebite
    source: Sorcerer
    level: 6
    DC: 23
  - name: shadow walk
    source: Sorcerer
    level: 6
  - name: break enchantment
    source: Sorcerer
    level: 5
  - name: dismissal
    source: Sorcerer
    level: 5
    DC: 22
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 22
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 22
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 21
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 21
  - name: dimensional anchor
    source: Sorcerer
    level: 4
  - name: scrying
    source: Sorcerer
    level: 4
    DC: 21
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 20
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: locate object
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: touch of idiocy
    source: Sorcerer
    level: 2
    DC: 19
  - name: share memory
    source: Sorcerer
    level: 2
    DC: 19
  - name: alarm
    source: Sorcerer
    level: 1
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 18
  - name: hypnotism
    source: Sorcerer
    level: 1
    DC: 18
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: 6 more
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 35
  DEX: 10
  CON: 25
  INT: 24
  WIS: 21
  CHA: 24
BAB: 24
CMB: 40
CMD: 50
CMD_other: 54 vs. trip
feats:
- name: Combat Casting
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Multiattack
- name: Quicken Spell
- name: Skill Focus (Perception)
- name: Weapon Focus (bite)
- name: Wingover
skills:
  Acrobatics: 24
  Appraise: 16
  Bluff: 34
  Diplomacy: 25
  Fly: 25
  Intimidate: 34
  Knowledge (arcana): 34
  Knowledge (planes): 34
  Knowledge (religion): 34
  Perception: 38
  Sense Motive: 32
  Spellcraft: 34
  Stealth: 15
  Survival: 20
  Use Magic Device: 25
languages:
- Abyssal
- Aklo
- Auran
- Celestial
- Draconic
- Ignan
- Infernal
- Terran
special_qualities:
- agile
- no breath
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Void dragons have been tainted by long exposure to the terrible alien entities
  that dwell in deep space. Though some continue to struggle against the inevitable
  tide of annihilation, many have embraced the encroaching void and exist only to
  feed and destroy.

---

# Dragon (Outer, Void), Ancient Void Dragon

**Source** Bestiary 4 pg. 73
**XP** 153,600

NE Gargantuan dragon
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +38
**Aura** alien presence (300 ft., DC 29)

##### Defense

**AC** 38, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+32 natural, –4 size)
**hp** 324 (24d12+168)
**Fort** +21, **Ref** +16, **Will** +21
**DR** 15/magic; **Immune** cold, _[[spells/Confusion|confusion]]_, _[[spells/Insanity|insanity]]_ effects, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., fly 250 ft. (good)
**Melee** bite +33 (4d6+18/19–20 plus obliterate), 2 claws +32 (2d8+12), 2 wings +30 (2d6+6), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. Cone, 20d8 cold, DC 29), crush, obliterate (DC 29), suffocating breath (DC 29), tail sweep, void _[[universal monster rules/Gaze|gaze]]_ (DC 29)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +31)
At will—_[[spells/Blur|blur]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 18), _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 20)
1/day—_[[spells/Nightmare|nightmare]]_ (DC 22)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 15th; concentration +22)
7th (5/day)—_[[spells/Prismatic Spray|prismatic spray]]_ (DC 24), _[[spells/Vision|vision]]_
6th (7/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Eyebite|eyebite]]_ (DC 23), _[[spells/Shadow Walk|shadow walk]]_
5th (7/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dismissal|dismissal]]_ (DC 22), _[[spells/Dominate Person|dominate person]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 22)
4th (7/day)—_[[spells/Charm Monster|charm monster]]_ (DC 21), _confusion_ (DC 21), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Scrying|scrying]]_ (DC 21)
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_, _[[spells/Heroism|heroism]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20)
2nd (7/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_ (DC 19), _[[spells/Share Memory|share memory]]_ (DC 19)
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Cause Fear|cause fear]]_ (DC 18), _[[spells/Hypnotism|hypnotism]]_ (DC 18), _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, 6 more

##### Statistics
**Str** 35, **Dex** 10, **Con** 25, **Int** 24, **Wis** 21, **Cha** 24
**Base Atk** +24; **CMB** +40; **CMD** 50 (54 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _[[feats/Wingover|Wingover]]_
**Skills** Acrobatics +24, Appraise +16, Bluff +34, Diplomacy +25, Fly +25, Intimidate +34, Knowledge (arcana, planes, religion) +34, Perception +38, Sense Motive +32, Spellcraft +34, Stealth +15, Survival +20, Use Magic Device +25
**Languages** Abyssal, Aklo, Auran, Celestial, Draconic, Ignan, Infernal, Terran
**SQ** _[[items/Weapon Magic Abilities/Agile|agile]]_, _[[universal monster rules/No Breath|no breath]]_, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Void dragons have been tainted by long exposure to the terrible alien entities that dwell in deep space. Though some continue to struggle against the inevitable tide of annihilation, many have embraced the encroaching void and exist only to feed and destroy.