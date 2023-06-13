---
cssclass: [monsters]
title1: Dragon (Green), Adult Green Dragon
title2: Adult Green Dragon
CR: 12
sources:
- name: Pathfinder RPG Bestiary
  page: 96
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 19200
alignment: LE
size: Huge
type: dragon
subtypes:
- air
initiative:
  bonus: 0
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 20
AC:
  AC: 27
  touch: 8
  flat_footed: 27
  components:
    natural: 19
    size: -2
HP:
  HP: 172
  long: 15d12+75
saves:
  fort: 14
  ref: 9
  will: 14
DR:
- amount: 5
  weakness: magic
immunities:
- acid
- paralysis
- sleep
SR: 23
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
  swim: 40
attacks:
  melee:
  - - text: bite +21 (2d8+12/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
      attack: bite
      bonus:
      - 21
    - text: 2 claws +21 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 21
    - text: 2 wings +16 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 16
    - text: tail slap +16 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: tail slap
      bonus:
      - 16
  special:
  - breath weapon (50-ft. cone, DC 22, 12d6 acid)
  - crush (Small creatures, DC 22, 2d8+12)
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: charm person
    source: default
    freq: At will
    DC: 14
  - name: entangle
    source: default
    freq: At will
    DC: 14
  - name: suggestion
    source: default
    freq: At will
    DC: 16
  sources:
  - name: default
    CL: 15
spells:
  entries:
  - name: alter self
    source: '?'
    level: 2
  - name: mirror image
    source: '?'
    level: 2
  - name: shield
    source: '?'
    level: 1
  - name: silent image
    source: '?'
    level: 1
    DC: 14
  - name: summon monster I
    source: '?'
    level: 1
  - name: ventriloquism
    source: '?'
    level: 1
    DC: 14
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
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 5
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 27
  DEX: 10
  CON: 21
  INT: 16
  WIS: 17
  CHA: 16
BAB: 15
CMB: 25
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Alertness
- name: Cleave
- name: Flyby Attack
- name: Great Cleave
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Iron Will
- name: Power Attack
skills:
  Fly: 10
  Knowledge (arcane): 21
  Knowledge (nature): 21
  Perception: 25
  Spellcraft: 21
  Stealth: 10
  Survival: 21
  Swim: 34
  Use Magic Device: 21
languages:
- Common
- Draconic
- Elven
- Sylvan
special_qualities:
- trackless step
- water breathing
- woodland stride
ecology:
  environment: temperate forests
desc_long: Green dragons dwell in the ancient forests of the world, prowling under
  towering canopies in search of prey. Of all the chromatic dragons, green dragons
  are perhaps the easiest to deal with diplomatically.

---

# Dragon (Green), Adult Green Dragon

**Source** Pathfinder RPG Bestiary pg. 96
**XP** 19,200

LE Huge dragon (air)
**Init** +0; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +25
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 20)

##### Defense

**AC** 27, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+19 natural, –2 size)
**hp** 172 (15d12+75)
**Fort** +14, **Ref** +9, **Will** +14
**DR** 5/magic; **Immune** acid, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 23

##### Offense
**Speed** 40 ft., fly 200 ft. (poor), swim 40 ft.
**Melee** bite +21 (2d8+12/19–20), 2 claws +21 (2d6+8/19–20), 2 wings +16 (1d8+4), tail slap +16 (2d6+12)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 22, 12d6 acid), crush (Small creatures, DC 22, 2d8+12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th)
At will—_[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Entangle|entangle]]_ (DC 14), _[[spells/Suggestion|suggestion]]_ (DC 16)
**Spells Known **(CL 5th)
2nd (5/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Mirror Image|mirror image]]_
1st (7/day)—_[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_ (DC 14), _[[spells/Summon Monster I|summon monster I]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 27, **Dex** 10, **Con** 21, **Int** 16, **Wis** 17, **Cha** 16
**Base Atk** +15; **CMB** +25; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claws), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +10, Knowledge (arcane) +21, Knowledge (nature) +21, Perception +25, Spellcraft +21, Stealth +10, Survival +21, Swim +34, Use Magic Device +21
**Languages** Common, Draconic, Elven, Sylvan
**SQ** _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, _[[universal monster rules/Water Breathing|water breathing]]_, woodland stride

##### Ecology

**Environment** temperate forests

Green dragons dwell in the ancient forests of the world, prowling under towering canopies in search of prey. Of all the chromatic dragons, green dragons are perhaps the easiest to deal with diplomatically.