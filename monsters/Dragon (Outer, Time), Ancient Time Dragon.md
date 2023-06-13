---
cssclass: [monsters]
title1: Dragon (Outer, Time), Ancient Time Dragon
title2: Ancient Time Dragon
CR: 20
sources:
- name: Bestiary 4
  page: 71
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 307200
alignment: N
size: Gargantuan
type: dragon
initiative:
  bonus: 14
senses:
  detect magic: true
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 300
  DC: 29
AC:
  AC: 37
  touch: 6
  flat_footed: 37
  components:
    natural: 31
    size: -4
HP:
  HP: 418
  long: 27d12+243
saves:
  fort: 24
  ref: 17
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- cold
- paralysis
- sleep
- staggered
SR: 31
speeds:
  base: 50
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +38 (4d6+21)
      entries:
      - - damage: 4d6+21
      attack: bite
      bonus:
      - 38
    - text: 2 claws +38 (2d8+14/19-20)
      entries:
      - - damage: 2d8+14
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 38
    - text: 2 wings +35 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: wings
      bonus:
      - 35
    - text: tail slap +35 (2d8+21)
      entries:
      - - damage: 2d8+21
      attack: tail slap
      bonus:
      - 35
  special:
  - breath weapon (60-ft. cone, 20d10 electricity, DC 32)
  - crush
  - second chance
  - shifting breath (5 rounds)
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - name: legend lore
    source: default
    freq: At will
  - name: locate creature
    source: default
    freq: At will
  - superscripts:
    - UM
    name: share memory
    source: default
    freq: At will
  sources:
  - name: default
    CL: 27
    concentration: 33
spells:
  entries:
  - name: plane shift
    source: Sorcerer
    level: 7
    DC: 23
  - name: sequester
    source: Sorcerer
    level: 7
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 22
  - name: greater dispel magic
    source: Sorcerer
    level: 6
  - name: true seeing
    source: Sorcerer
    level: 6
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 21
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 21
  - name: telepathic bond
    source: Sorcerer
    level: 5
  - name: teleport
    source: Sorcerer
    level: 5
  - name: fear
    source: Sorcerer
    level: 4
    DC: 20
  - name: scrying
    source: Sorcerer
    level: 4
    DC: 20
  - name: stone shape
    source: Sorcerer
    level: 4
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: blink
    source: Sorcerer
    level: 3
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: slow
    source: Sorcerer
    level: 3
    DC: 19
  - name: tongues
    source: Sorcerer
    level: 3
  - name: arcane lock
    source: Sorcerer
    level: 2
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 18
  - name: blur
    source: Sorcerer
    level: 2
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 18
  - superscripts:
    - APG
    name: memory lapse
    source: Sorcerer
    level: 2
    DC: 18
  - name: erase
    source: Sorcerer
    level: 1
  - name: feather fall
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: 5 more
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 15
    concentration: 21
    slots:
      7: 4
      6: 7
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 38
  DEX: 11
  CON: 28
  INT: 23
  WIS: 22
  CHA: 23
BAB: 27
CMB: 45
CMB_other: +47 sunder
CMD: 57
CMD_other: 59 vs. sunder, 61 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Sunder
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Quicken Spell
- name: Skill Focus (Knowledge [history])
- name: Spell Penetration
- name: Step Up
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Bluff: 36
  Diplomacy: 36
  Fly: 16
  Knowledge (arcana): 36
  Knowledge (geography): 36
  Knowledge (nobility): 36
  Knowledge (planes): 36
  Knowledge (religion): 36
  Knowledge (history): 42
  Perception: 36
  Sense Motive: 36
  Spellcraft: 36
languages:
- Celestial
- Common
- Draconic
- Dwarven
- Elven
- Infernal
- Sylvan
special_qualities:
- immortal
- no breath
- read the threads
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Guardians of history, time dragons are the most powerful of the outer dragons.
  Watchers and waiters, time dragons guard the universe against those that would interfere
  with the natural temporal order.

---

# Dragon (Outer, Time), Ancient Time Dragon

**Source** Bestiary 4 pg. 71
**XP** 307,200

N Gargantuan dragon
**Init** +14; **Senses** _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +36
**Aura** alien presence (300 ft., DC 29)

##### Defense

**AC** 37, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+31 natural, –4 size)
**hp** 418 (27d12+243)
**Fort** +24, **Ref** +17, **Will** +21
**DR** 15/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep, _[[conditions/Staggered|staggered]]_; **SR** 31

##### Offense
**Speed** 50 ft., fly 250 ft. (clumsy)
**Melee** bite +38 (4d6+21), 2 claws +38 (2d8+14/19–20), 2 wings +35 (2d6+7), tail slap +35 (2d8+21)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d10 electricity, DC 32), crush, _[[feats/Second Chance|second chance]]_, shifting breath (5 rounds), tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th; concentration +33)
Constant—_detect magic_
At will—clairaudience/clairvoyance, _[[spells/Legend Lore|legend lore]]_, _[[spells/Locate Creature|locate creature]]_, _[[spells/Share Memory|share memory]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 15th; concentration +21)
7th (4/day)—_[[spells/Plane Shift|plane shift]]_ (DC 23), _[[spells/Sequester|sequester]]_
6th (7/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 22), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/True Seeing|true seeing]]_
5th (7/day)—_[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Feeblemind|feeblemind]]_ (DC 21), _[[spells/Telepathic Bond|telepathic bond]]_, teleport
4th (7/day)—_[[universal monster rules/Fear|fear]]_ (DC 20), _[[spells/Scrying|scrying]]_ (DC 20), _[[spells/Stone Shape|stone shape]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_[[spells/Blink|blink]]_, _dispel magic_, _[[spells/Slow|slow]]_ (DC 19), _[[spells/Tongues|tongues]]_
2nd (8/day)—_[[spells/Arcane Lock|arcane lock]]_, blindness/deafness (DC 18), _[[spells/Blur|blur]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Memory Lapse|memory lapse]]_ (DC 18)
1st (8/day)—_[[spells/Erase|erase]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Identify|identify]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, 5 more

##### Statistics
**Str** 38, **Dex** 11, **Con** 28, **Int** 23, **Wis** 22, **Cha** 23
**Base Atk** +27; **CMB** +45 (+47 sunder); **CMD** 57 (59 vs. sunder, 61 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [history]), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw)
**Skills** Bluff +36, Diplomacy +36, Fly +16, Knowledge (arcana, geography, nobility, planes, religion) +36, Knowledge (history) +42, Perception +36, Sense Motive +36, Spellcraft +36
**Languages** Celestial, Common, Draconic, Dwarven, Elven, Infernal, Sylvan
**SQ** immortal, _[[universal monster rules/No Breath|no breath]]_, read the threads, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Guardians of history, time dragons are the most powerful of the outer dragons. Watchers and waiters, time dragons _[[npcs/Guard|guard]]_ the universe against those that would interfere with the natural temporal order.