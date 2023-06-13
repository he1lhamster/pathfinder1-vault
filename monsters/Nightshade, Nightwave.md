---
cssclass: [monsters]
title1: Nightshade, Nightwave
desc_short: Immense almost beyond belief, this sleek, midnight-black shark rises from
  the sea like an unholy island heaved up from below.
title2: Nightwave
CR: 20
sources:
- name: Bestiary 2
  page: 202
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: CE
size: Colossal
type: undead
subtypes:
- aquatic
- extraplanar
- nightshade
initiative:
  bonus: 7
senses:
  darksense: true
  darkvision: 120
  detect magic: true
  low-light vision: true
auras:
- name: blackest depths
  radius: 60
- name: desecrating aura
  radius: 30
AC:
  AC: 36
  touch: 5
  flat_footed: 33
  components:
    dex: 3
    natural: 31
    size: -8
HP:
  HP: 391
  long: 29d8+261
saves:
  fort: 18
  ref: 16
  will: 25
DR:
- amount: 15
  weakness: good and silver
immunities:
- cold
- undead traits
SR: 29
weaknesses:
- light aversion
speeds:
  fly: 60
  fly_maneuverability: good
  swim: 60
attacks:
  melee:
  - - text: bite +35 (5d10+22/19-20 plus 4d6 cold, energy drain, and grab)
      entries:
      - - damage: 5d10+22
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: energy drain
        - effect: grab
      attack: bite
      bonus:
      - 35
    - text: tail slap +30 (4d8+12/19-20 plus 4d6 cold)
      entries:
      - - damage: 4d8+12
          crit_range: 19-20
        - damage: 4d6
          type: cold
      attack: tail slap
      bonus:
      - 30
  special:
  - channel energy (10d6, DC 33, 10/day)
  - energy drain (2 levels, DC 31)
  - swallow whole (5d10+28 bludgeoning plus energy drain, AC 25, 39 hp)
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: magic fang
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: confusion
    source: default
    freq: At will
    DC: 21
  - name: contagion
    source: default
    freq: At will
    DC: 21
  - name: deeper darkness
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 21
  - name: quickened cone of cold
    source: default
    freq: 3/day
    DC: 22
  - name: finger of death
    source: default
    freq: 3/day
    DC: 24
  - name: haste
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 3/day
    DC: 22
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 26
  - name: plane shift
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: nightwing
      amount: 1
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 49
  DEX: 16
  CON:
  INT: 22
  WIS: 21
  CHA: 25
BAB: 21
CMB: 48
CMB_other: +52 grapple
CMD: 61
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Command Undead
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (cone of cold)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 31
  Intimidate: 39
  Knowledge (arcana): 38
  Knowledge (planes): 35
  Knowledge (religion): 38
  Perception: 37
  Sense Motive: 37
  Spellcraft: 38
  Stealth: 19
    in darkness: 27
  Swim: 59
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
  organization: solitary
  treasure_type: standard
special_abilities:
  Blackest Depths (Su): The waters in which a nightwave swims become as chill, dark,
    and heavy as those in the ocean's deepest reaches. All waters within 60 feet are
    completely dark (as deeper darkness), and creatures within this radius take 6d6
    points of damage (half cold, half bludgeoning) at the end of their turn each round
    if they remain in the area at this time. A DC 31 Fortitude save negates the crushing
    damage. Incorporeal creatures and creatures with the aquatic or water subtypes
    native to deep waters do not take this damage, and freedom of movement protects
    completely against the damage. Any magical light effect within this radius at
    the beginning of the nightwave's turn is dispelled (treat as greater dispel magic).
    This effect does not extend out of the water. The save DC is Charisma-based.
  Energy Drain (Su): A creature that has been swallowed whole by a nightwave gains
    2 negative levels each round.
desc_long: |-
  The most powerful of the known types of nightshade is the ravenous nightwave, an unholy personification of the remorseless gluttony of death given the form of a shark the size of the largest whales. Although the nightwave is most at home in the ocean's deeps, it has no need to breathe, and its constant fly spell-like ability allows it to bring ruin above the waves as the need presents itself.

  A nightwave is 100 feet long and weighs 200 tons.

---

# Nightshade, Nightwave
Immense almost beyond belief, this sleek, midnight-black _[[monsters/Shark|shark]]_ rises from the sea like an _[[items/Weapon Magic Abilities/Unholy|unholy]]_ island heaved up from below.
**Source** Bestiary 2 pg. 202
**XP** 307,200
CE Colossal undead (aquatic, extraplanar, nightshade)
**Init** +7; **Senses** darksense, _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +37
**Aura** blackest depths (60 ft.), desecrating aura (30 ft.)

##### Defense

**AC** 36, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+3 Dex, +31 natural, –8 size)
**hp** 391 (29d8+261)
**Fort** +18, **Ref** +16, **Will** +25
**DR** 15/good and silver; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 29
**Weaknesses** light _[[spells/Aversion|aversion]]_

##### Offense
**Speed** fly 60 ft. (good), swim 60 ft.
**Melee** bite +35 (5d10+22/19–20 plus 4d6 cold, _[[universal monster rules/Energy Drain|energy drain]]_, and _[[universal monster rules/Grab|grab]]_), tail slap +30 (4d8+12/19–20 plus 4d6 cold)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** channel energy (10d6, DC 33, 10/day), _energy drain_ (2 levels, DC 31), _[[universal monster rules/Swallow Whole|swallow whole]]_ (5d10+28 bludgeoning plus _energy drain_, AC 25, 39 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_detect magic_, _[[spells/Magic Fang|magic fang]]_, _[[spells/See Invisibility|see invisibility]]_
At will—_[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Contagion|contagion]]_ (DC 21), _[[spells/Deeper Darkness|deeper darkness]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 21)
3/day—quickened _[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Finger Of Death|finger of death]]_ (DC 24), _[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 22)
1/day—mass _hold monster_ (DC 26), _[[spells/Plane Shift|plane shift]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 9, 1 nightwing), _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 26)

##### Statistics
**Str** 49, **Dex** 16, **Con** —, **Int** 22, **Wis** 21, **Cha** 25
**Base Atk** +21; **CMB** +48 (+52 grapple); **CMD** 61 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_cone of cold_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +31, Intimidate +39, Knowledge (arcana) +38, Knowledge (planes) +35, Knowledge (religion) +38, Perception +37, Sense Motive +37, Spellcraft +38, Stealth +19 (+27 in _[[spells/Darkness|darkness]]_), Swim +59; **Racial Modifiers** +8 Stealth in dim light and _darkness_
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Blackest Depths (Su)** The waters in which a nightwave swims become as chill, dark, and heavy as those in the ocean’s deepest reaches. All waters within 60 feet are completely dark (as _deeper darkness_), and creatures within this radius take 6d6 points of damage (half cold, half bludgeoning) at the end of their turn each round if they remain in the area at this time. A DC 31 Fortitude save negates the crushing damage. _[[universal monster rules/Incorporeal|Incorporeal]]_ creatures and creatures with the aquatic or water subtypes native to deep waters do not take this damage, and _[[spells/Freedom of Movement|freedom of movement]]_ protects completely against the damage. Any magical light effect within this radius at the beginning of the nightwave’s turn is dispelled (treat as greater _dispel magic_). This effect does not extend out of the water. The save DC is Charisma-based.

**_Energy Drain_ (Su)** A creature that has been swallowed whole by a nightwave gains 2 negative levels each round.

##### Description

The most powerful of the known types of nightshade is the _[[curses/Ravenous|ravenous]]_ nightwave, an _unholy_ personification of the remorseless gluttony of death given the form of a _shark_ the size of the largest whales. Although the nightwave is most at home in the ocean’s deeps, it has no need to breathe, and its constant fly spell-like ability allows it to bring ruin above the waves as the need presents itself.

A nightwave is 100 feet long and weighs 200 tons.