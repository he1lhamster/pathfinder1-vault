---
cssclass: [monsters]
title1: Nightshade, Nightprowler
desc_short: This bulky predator's feline form is cloaked in shadows, save for its
  red eyes, which glow with a baleful hatred.
title2: Nightprowler
CR: 10
sources:
- name: 'Pathfinder #102: Breaking the Bones of Hell'
  page: 90
  link: http://paizo.com/products/btpy9i8d?Pathfinder-Adventure-Path-102-Breaking-the-Bones-of-Hell
XP: 9600
alignment: CE
size: Large
type: undead
subtypes:
- extraplanar
- nightshade
initiative:
  bonus: 9
senses:
  darksense: 30
  darkvision: 60
  detect magic: true
  low-light vision: true
  scent: true
auras:
- name: desecrating aura
  radius: 30
AC:
  AC: 25
  touch: 15
  flat_footed: 19
  components:
    dex: 5
    dodge: 1
    natural: 10
    size: -1
HP:
  HP: 136
  long: 13d8+78
saves:
  fort: 10
  ref: 11
  will: 14
DR:
- amount: 10
  weakness: good and silver
immunities:
- cold
- undead traits
SR: 21
weaknesses:
- light aversion
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +18 (3d6+10/19-20 plus creeping dark and grab)
      entries:
      - - damage: 3d6+10
          crit_range: 19-20
        - effect: creeping dark
        - effect: grab
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (1d8+10 plus creeping dark)
      entries:
      - - damage: 1d8+10
        - effect: creeping dark
      count: 2
      attack: claws
      bonus:
      - 18
  special:
  - channel negative energy (DC 20, 5d6, 7/day)
  - creeping dark
  - rake (2 claws +18, 1d6+10)
  - shadowpounce
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: magic fang
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 18
  - name: dispel magic
    source: default
    freq: 3/day
  - name: contagion
    source: default
    freq: 3/day
    DC: 18
  - name: invisibility
    source: default
    freq: 3/day
  - name: air walk
    source: default
    freq: 1/day
  - name: confusion
    source: default
    freq: 1/day
    DC: 18
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 19
  - name: haste
    source: default
    freq: 1/day
  - name: hold monster
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: shadows
      amount: 2
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 25
  DEX: 20
  CON:
  INT: 14
  WIS: 19
  CHA: 19
BAB: 9
CMB: 17
CMD: 33
feats:
- name: Combat Reflexes
- name: Command Undead
- name: Dodge
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Power Attack
- name: Skill Focus (Stealth)
skills:
  Acrobatics: 18
  Climb: 23
  Knowledge (religion): 18
  Perception: 20
  Stealth: 23
    in dim light and darkness: 31
  Survival: 17
  _racial_mods:
    Stealth:
      in dim light and darkness: 8
languages:
- Abyssal
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Negative Energy Plane)
  organization: solitary, pair, or pride (3-9)
  treasure_type: standard
special_abilities:
  Creeping Dark (Su): The nightprowler's natural attacks leave a stain of dark shadows
    that linger in and around the wounds, known as the creeping dark-this condition
    can be resisted with a successful DC 20 Fortitude save. If the victim fails, it
    becomes staggered for 1 round, after which the creeping dark affects the victim
    further by preventing healing and hampering vision. A character attempting to
    use magical healing on a creature damaged by the nightprowler's creeping dark
    must succeed at a DC 26 caster level check, or the healing has no effect on the
    injured creature. As long as a creature suffers the creeping dark, its vision
    is obscured with shadows as well-all creatures gain a 20% miss chance from attacks
    by the victim. The creeping dark is a curse effect that lasts until removed or
    until all damage afflicting the victim is healed. The save DC is Charisma-based.
  Shadowpounce (Su): Nightprowlers have the pounce ability, and when they use this
    ability, they can also make rake attacks. Up to three times per day when a nightprowler
    pounces from an area of dim illumination, it generates a shimmering aura of false
    images that grants it a 50% miss chance, as if under the effects of a displacement
    spell, for 1d4 rounds.
desc_long: |-
  Only a fool would underestimate the danger presented by the hateful nightprowler, despite its position as the least powerful of the undead monsters collectively known as nightshades. The bestial nightprowler is a fearsome opponent armed with the same cruel and calculating intelligence possessed by all nightshades.

  Nightprowlers are feline quadrupeds that seem to be composed of living shadow. Their eyes, like the eyes of all nightshades, glow with red light. A nightprowler is 16 feet long from head to tail and weighs 8,000 pounds. Nightprowlers have all the nightshade traits found on page 308 of Pathfinder RPG Bestiary 2, except that they have darksense out to only 30 feet.

---

# Nightshade, Nightprowler
This bulky predator’s feline form is cloaked in shadows, save for its red eyes, which glow with a baleful hatred.
**Source** Pathfinder #102: _[[items/Weapon Magic Abilities/Breaking|Breaking]]_ the Bones of Hell pg. 90
**XP** 9,600
CE Large undead (extraplanar, nightshade)
**Init** +9; **Senses** darksense 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +20
**Aura** desecrating aura (30 ft.)

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 Dex, +1 dodge, +10 natural, –1 size)
**hp** 136 (13d8+78)
**Fort** +10, **Ref** +11, **Will** +14
**DR** 10/good and silver; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 21
**Weaknesses** light _[[spells/Aversion|aversion]]_

##### Offense
**Speed** 50 ft.
**Melee** bite +18 (3d6+10/19–20 plus _[[items/Armor Magic Abilities/Creeping|creeping]]_ dark and _[[universal monster rules/Grab|grab]]_), 2 claws +18 (1d8+10 plus _creeping_ dark)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy (DC 20, 5d6, 7/day), _creeping_ dark, _[[universal monster rules/Rake|rake]]_ (2 claws +18, 1d6+10), shadowpounce
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_detect magic_, _[[spells/Magic Fang|magic fang]]_
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 18)
3/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Contagion|contagion]]_ (DC 18), _[[spells/Invisibility|invisibility]]_
1/day—_[[spells/Air Walk|air walk]]_, _[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Cone of Cold|cone of cold]]_ (DC 19), _[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 4, 2 shadows)

##### Statistics
**Str** 25, **Dex** 20, **Con** —, **Int** 14, **Wis** 19, **Cha** 19
**Base Atk** +9; **CMB** +17; **CMD** 33
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[spells/Command Undead|Command Undead]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Acrobatics +18, _[[universal monster rules/Climb|Climb]]_ +23, Knowledge (religion) +18, Perception +20, Stealth +23 (+31 in dim light and _[[spells/Darkness|darkness]]_), Survival +17; **Racial Modifiers** +8 Stealth in dim light and _darkness_
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary, pair, or pride (3–9)
**Treasure** standard

### Special Abilities

**_Creeping_ Dark (Su)** The nightprowler’s _[[universal monster rules/Natural Attacks|natural attacks]]_ leave a stain of dark shadows that linger in and around the wounds, known as the _creeping_ dark—this condition can be resisted with a successful DC 20 Fortitude save. If the victim fails, it becomes _[[conditions/Staggered|staggered]]_ for 1 round, after which the _creeping_ dark affects the victim further by preventing healing and hampering _[[spells/Vision|vision]]_. A character attempting to use magical healing on a creature damaged by the nightprowler’s _creeping_ dark must succeed at a DC 26 caster level check, or the healing has no effect on the injured creature. As long as a creature suffers the _creeping_ dark, its _vision_ is obscured with shadows as well—all creatures gain a 20% miss chance from attacks by the victim. The _creeping_ dark is a curse effect that lasts until removed or until all damage afflicting the victim is healed. The save DC is Charisma-based.
**Shadowpounce (Su)** Nightprowlers have the _[[universal monster rules/Pounce|pounce]]_ ability, and when they use this ability, they can also make _rake_ attacks. Up to three times per day when a nightprowler pounces from an area of dim illumination, it generates a shimmering aura of false images that grants it a 50% miss chance, as if under the effects of a _[[spells/Displacement|displacement]]_ spell, for 1d4 rounds.

##### Description

Only a fool would underestimate the danger presented by the hateful nightprowler, despite its position as the least powerful of the undead monsters collectively known as nightshades. The bestial nightprowler is a fearsome opponent armed with the same _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and calculating intelligence possessed by all nightshades.

Nightprowlers are feline quadrupeds that seem to be composed of living _[[items/Armor Magic Abilities/Shadow|shadow]]_. Their eyes, like the eyes of all nightshades, glow with red light. A nightprowler is 16 feet long from head to tail and weighs 8,000 pounds. Nightprowlers have all the nightshade traits found on page 308 of Pathfinder RPG Bestiary 2, except that they have darksense out to only 30 feet.