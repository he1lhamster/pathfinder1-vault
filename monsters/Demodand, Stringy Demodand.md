---
cssclass: [monsters]
title1: Demodand, Stringy Demodand
desc_short: This lanky, winged humanoid is covered in layers of long, ropy skin growths.
title2: Stringy Demodand
CR: 15
sources:
- name: Bestiary 5
  page: 73
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Pathfinder #77: Herald of the Ivory Labyrinth'
  page: 84
  link: http://paizo.com/products/btpy92lh?Pathfinder-Adventure-Path-77-Herald-of-the-Ivory-Labyrinth
XP: 51200
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demodand
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 120
  detect good: true
  detect magic: true
AC:
  AC: 30
  touch: 18
  flat_footed: 22
  components:
    dex: 8
    natural: 12
HP:
  HP: 230
  long: 20d10+120
saves:
  fort: 18
  ref: 14
  will: 13
  other: +4 vs. divine spells
DR:
- amount: 10
  weakness: good and magic
immunities:
- acid
- poison
resistances:
  cold: 10
  fire: 10
SR: 26
speeds:
  base: 40
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +29 (2d6+9 plus 2d6 nonlethal/19-20)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
        - damage: 2d6
          type: nonlethal
          crit_range: 19-20
      attack: bite
      bonus:
      - 29
    - text: 2 claws +29 (1d10+9 plus 2d6 nonlethal/19-20)
      entries:
      - - damage: 1d10+9
          crit_range: 19-20
        - damage: 2d6
          type: nonlethal
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 29
  special:
  - entangling folds
  - faith-stealing strike (DC 24)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 16
  - name: fear
    source: default
    freq: 3/day
    DC: 18
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: tarry demodands
      amount: 1d4
    - name: stringy demodands
      amount: 1d2
      chance: 40%
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 28
  DEX: 27
  CON: 23
  INT: 12
  WIS: 13
  CHA: 18
BAB: 20
CMB: 29
CMD: 47
feats:
- name: Blind-Fight
- name: Cleave
- name: Combat Reflexes
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Vital Strike
- name: Intimidating Prowess
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 26
  Bluff: 27
  Climb: 22
  Fly: 21
  Intimidate: 36
  Knowledge (planes): 14
  Perception: 24
  Sense Motive: 14
  Stealth: 26
  Survival: 14
languages:
- Abyssal
- Celestial
- Common
special_qualities:
- heretical soul
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or tangle (3-8)
  treasure_type: standard
special_abilities:
  Entangling Folds (Ex): Although the disgusting growths on a stringy demodand are
    technically part of its skin, the demodand has a small measure of control over
    these ropy appendages. As a swift action, a stringy demodand can use its growths
    to entangle any adjacent creatures of its size or smaller. To resist being entangled,
    a target must succeed at a DC 25 Reflex save. As long as the stringy demodand
    is entangling one or more creatures, any creature that moves adjacent to the demodand
    must successfully save or likewise be entangled. Entangled creatures can't move
    farther than 5 feet from the stringy demodand until they break free from its growths.
    An entangled creature can break free as a move action by succeeding at a DC 25
    Strength or Escape Artist check. The save DCs are Constitution-based.
desc_long: |-
  Stringy demodands fulfill their duty to their titan masters as kidnappers and slave masters throughout the Abyssal realms. Stringy demodands' agility allows them to quickly snatch up targets and prevent slave revolts before they start.

  The stringy demodands' long, obsidian-colored skin growths give the abhorrent outsiders their name. These fibers resemble nothing so much as elongated skin tags the girth of a human finger and are roughly 4 feet in length. The fibrous outgrowths sprout from their heads and the tips of their wings. These ropy feelers bob and sway wildly as a stringy demodand moves, creating a truly disturbing image for those victims who glimpse back at their Abyssal pursuer.

  Because these rubbery strands cover most of the creatures' bodies, they provide a measure of natural protection that allows stringy demodands to eschew armor. Stringy demodands are typically 6 feet tall and weigh 300 pounds.

---

# Demodand, Stringy Demodand
This lanky, winged humanoid is covered in layers of long, ropy skin growths.
**Source** Bestiary 5 pg. 73, Pathfinder #77: Herald of the Ivory Labyrinth pg. 84
**XP** 51,200
CE Medium outsider (chaotic, demodand, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +24

##### Defense

**AC** 30, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+8 Dex, +12 natural)
**hp** 230 (20d10+120)
**Fort** +18, **Ref** +14, **Will** +13; +4 vs. divine spells
**DR** 10/good and magic; **Immune** acid, poison; **Resist** cold 10, fire 10; **SR** 26

##### Offense
**Speed** 40 ft., fly 40 ft. (average)
**Melee** bite +29 (2d6+9 plus 2d6 nonlethal/19-20), 2 claws +29 (1d10+9 plus 2d6 nonlethal/19-20)
**Special Attacks** entangling folds, faith-stealing strike (DC 24)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
Constant—_detect good_, _detect magic_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16)
3/day—_[[universal monster rules/Fear|fear]]_ (DC 18), greater _[[spells/Dispel Magic|dispel magic]]_
1/day—_[[spells/Hold Monster|hold monster]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 6, 1d4 tarry demodands or 1d2 stringy demodands 40%)

##### Statistics
**Str** 28, **Dex** 27, **Con** 23, **Int** 12, **Wis** 13, **Cha** 18
**Base Atk** +20; **CMB** +29; **CMD** 47
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +26, Bluff +27, _[[universal monster rules/Climb|Climb]]_ +22, Fly +21, Intimidate +36, Knowledge (planes) +14, Perception +24, Sense Motive +14, Stealth +26, Survival +14
**Languages** Abyssal, Celestial, Common
**SQ** _[[items/Weapon Magic Abilities/Heretical|heretical]]_ soul

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or tangle (3-8)
**Treasure** standard

### Special Abilities

**Entangling Folds (Ex)** Although the disgusting growths on a stringy demodand are technically part of its skin, the demodand has a small measure of control over these ropy appendages. As a swift action, a stringy demodand can use its growths to _[[spells/Entangle|entangle]]_ any adjacent creatures of its size or smaller. To resist being _[[conditions/Entangled|entangled]]_, a target must succeed at a DC 25 Reflex save. As long as the stringy demodand is entangling one or more creatures, any creature that moves adjacent to the demodand must successfully save or likewise be _entangled_. _Entangled_ creatures can’t move farther than 5 feet from the stringy demodand until they break free from its growths. An _entangled_ creature can break free as a move action by succeeding at a DC 25 Strength or Escape Artist check. The save DCs are Constitution-based.

##### Description

Stringy demodands fulfill their duty to their titan masters as kidnappers and _[[items/Mundane/Slave|slave]]_ masters throughout the Abyssal realms. Stringy demodands’ agility allows them to quickly _[[feats/Snatch|snatch]]_ up targets and prevent _slave_ revolts before they start.

The stringy demodands’ long, obsidian-colored skin growths give the abhorrent outsiders their name. These fibers resemble nothing so much as elongated skin tags the girth of a human finger and are roughly 4 feet in length. The fibrous outgrowths sprout from their heads and the tips of their wings. These ropy feelers bob and sway wildly as a stringy demodand moves, creating a truly disturbing image for those victims who glimpse back at their Abyssal pursuer.

Because these rubbery strands cover most of the creatures’ bodies, they provide a measure of natural protection that allows stringy demodands to eschew armor. Stringy demodands are typically 6 feet tall and weigh 300 pounds.