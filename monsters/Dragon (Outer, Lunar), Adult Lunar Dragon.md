---
cssclass: [monsters]
title1: Dragon (Outer, Lunar), Adult Lunar Dragon
title2: Adult Lunar Dragon
CR: 13
sources:
- name: Bestiary 4
  page: 66
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 25600
alignment: CN
size: Huge
type: dragon
initiative:
  bonus: 3
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 180
  DC: 23
AC:
  AC: 28
  touch: 7
  flat_footed: 28
  components:
    dex: -1
    natural: 21
    size: -2
HP:
  HP: 200
  long: 16d12+96
saves:
  fort: 15
  ref: 9
  will: 16
defensive_abilities:
- reflected light
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- paralysis
- sleep
SR: 24
speeds:
  base: 40
  burrow: 20
  fly: 200
  fly_maneuverability: poor
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
    - text: 2 wings +20 (2d6+4)
      entries:
      - - damage: 2d6+4
      count: 2
      attack: wings
      bonus:
      - 20
    - text: tail slap +20 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: tail slap
      bonus:
      - 20
  special:
  - bewildering breath
  - breath weapon (100-ft. line, 12d8 cold, DC 23)
  - crush
  - moonsilver
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: At will
  - superscripts:
    - APG
    name: life bubble
    source: default
    freq: At will
  - superscripts:
    - APG
    name: moonstruck
    source: default
    freq: At will
  sources:
  - name: default
    CL: 16
    concentration: 21
spells:
  entries:
  - name: haste
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: blur
    source: Sorcerer
    level: 2
  - name: hypnotic pattern
    source: Sorcerer
    level: 2
    DC: 17
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: comprehend languages
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: protection from evil
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - superscripts:
    - APG
    name: vanish
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 12
    slots:
      3: 3
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 27
  DEX: 9
  CON: 20
  INT: 20
  WIS: 22
  CHA: 21
BAB: 16
CMB: 26
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Arcane Strike
- superscripts:
  - APG
  name: Dazing Assault
- name: Flyby Attack
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Toughness
- name: Wingover
skills:
  Bluff: 12
  Diplomacy: 24
  Fly: 10
  Intimidate: 24
  Knowledge (arcana): 20
  Knowledge (geography): 20
  Knowledge (history): 20
  Knowledge (local): 20
  Knowledge (nature): 20
  Perception: 25
  Sense Motive: 25
  Spellcraft: 24
  Use Magic Device: 24
languages:
- Aklo
- Aquan
- Auran
- Common
- Draconic
- Ignan
special_qualities:
- no breath
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Lunar dragons frequently interact with mortals, spending long hours watching
  the activities occurring on planets that interest them.

---

# Dragon (Outer, Lunar), Adult Lunar Dragon

**Source** Bestiary 4 pg. 66
**XP** 25,600

CN Huge dragon
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +25
**Aura** alien presence (180 ft., DC 23)

##### Defense

**AC** 28, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 28 (–1 Dex, +21 natural, –2 size)
**hp** 200 (16d12+96)
**Fort** +15, **Ref** +9, **Will** +16
**Defensive Abilities** reflected light; **DR** 5/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 24

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 200 ft. (poor)
**Melee** bite +22 (2d8+12), 2 claws +22 (2d6+8), 2 wings +20 (2d6+4), tail slap +20 (2d8+12)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[items/Weapon Magic Abilities/Bewildering|bewildering]]_ breath, _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, 12d8 cold, DC 23), crush, moonsilver
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +21)
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Life Bubble|life bubble]]_, _[[spells/Moonstruck|moonstruck]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 7th; concentration +12)
3rd (3/day)—_[[spells/Haste|haste]]_, _[[spells/Heroism|heroism]]_
2nd (5/day)—_[[spells/Blur|blur]]_, _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_
1st (7/day)—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Shocking Grasp|shocking grasp]]_, _[[spells/Vanish|vanish]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 27, **Dex** 9, **Con** 20, **Int** 20, **Wis** 22, **Cha** 21
**Base Atk** +16; **CMB** +26; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Dazing Assault|Dazing Assault]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +12, Diplomacy +24, Fly +10, Intimidate +24, Knowledge (arcana, geography, history, local, nature) +20, Perception +25, Sense Motive +25, Spellcraft +24, Use Magic Device +24
**Languages** Aklo, Aquan, Auran, Common, Draconic, Ignan
**SQ** _[[universal monster rules/No Breath|no breath]]_, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Lunar dragons frequently interact with mortals, spending long hours watching the activities occurring on planets that interest them.