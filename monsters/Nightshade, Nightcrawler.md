---
cssclass: [monsters]
title1: Nightshade, Nightcrawler
desc_short: This immense worm is covered with plates of dead-black, chitinous armor.
  Its toothy maw yawns like a cave.
title2: Nightcrawler
CR: 18
sources:
- name: Bestiary 2
  page: 200
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 153600
alignment: CE
size: Gargantuan
type: undead
subtypes:
- extraplanar
- nightshade
initiative:
  bonus: 4
senses:
  darksense: true
  darkvision: 120
  detect magic: true
  low-light vision: true
  tremorsense: 120
auras:
- name: desecrating aura
  radius: 30
AC:
  AC: 33
  touch: 6
  flat_footed: 33
  components:
    natural: 27
    size: -4
HP:
  HP: 312
  long: 25d8+200
saves:
  fort: 16
  ref: 10
  will: 23
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
  base: 30
  burrow: 60
attacks:
  melee:
  - - text: bite +32 (4d10+18/19-20 plus 4d6 cold and grab)
      entries:
      - - damage: 4d10+18
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: grab
      attack: bite
      bonus:
      - 32
    - text: sting +32 (4d6+18/19-20 plus 4d6 cold and poison)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: poison
      attack: sting
      bonus:
      - 32
  special:
  - channel negative energy (9d6, DC 31, 9/day)
  - energy drain (1 level, DC 28)
  - swallow whole (4d10+22 bludgeoning plus energy drain, AC 23, 31 hp)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: magic fang
    source: default
    freq: Constant
  - name: contagion
    source: default
    freq: At will
    DC: 20
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
    DC: 20
  - name: quickened cone of cold
    source: default
    freq: 3/day
    DC: 21
  - name: confusion
    source: default
    freq: 3/day
    DC: 20
  - name: haste
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 3/day
    DC: 21
  - name: finger of death
    source: default
    freq: 1/day
    DC: 23
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 25
  - name: plane shift
    source: default
    freq: 1/day
    DC: 23
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: greater shadows
      amount: 6
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 41
  DEX: 10
  CON:
  INT: 20
  WIS: 21
  CHA: 23
BAB: 18
CMB: 37
CMB_other: +41 grapple
CMD: 47
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Command Undead
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (cone of cold)
- name: Staggering Critical
- name: Vital Strike
skills:
  Intimidate: 34
  Knowledge (arcana): 33
  Knowledge (planes): 30
  Knowledge (religion): 33
  Perception: 33
  Sense Motive: 33
  Spellcraft: 33
  Stealth: 16
    in darkness: 24
  Swim: 40
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
  organization: solitary or pair
  treasure_type: standard
special_abilities:
  Energy Drain (Su): A creature that has been swallowed whole by a nightcrawler gains
    1 negative level each round.
  Poison (Su): Sting-injury; save Fort DC 28; frequency 1/round for 6 rounds; effect
    1d4 Constitution drain and 1 negative level; cure 3 consecutive saves. The save
    DC is Charisma-based.
desc_long: |-
  Although the nightcrawler might appear to be little more than an immense and frightening vermin, with its centipede-like body and numerous glowing eyes, it is actually incredibly intelligent. When not cleansing the deep caverns of life, the nightcrawler spends its time plotting how best to carry out its own private stages of the overall nightshade plan to expunge life from all worlds, conferring with its undead minions and, when necessary, observing living creatures from afar while invisible to learn about hidden enclaves that its depredations might otherwise have missed.

  It would be one thing if the nightcrawlers remained in the deep caverns, for these regions are rife with foul life the world is better off without. Yet unfortunately for those who dwell upon the surface, nightcrawlers often crawl up through the tunnels to bring their devastation to the night above. Although they always retreat underground before the first tentative rays of dawn color the eastern skies, they can spread an incredible amount of ruin in the span of a few short hours each night.

  A nightcrawler is 60 feet long and weighs 10,000 pounds.

---

# Nightshade, Nightcrawler
This immense worm is covered with plates of dead-black, chitinous armor. Its toothy maw yawns like a cave.
**Source** Bestiary 2 pg. 200
**XP** 153,600
CE Gargantuan undead (extraplanar, nightshade)
**Init** +4; **Senses** darksense, _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +33
**Aura** desecrating aura (30 ft.)

##### Defense

**AC** 33, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+27 natural, –4 size)
**hp** 312 (25d8+200)
**Fort** +16, **Ref** +10, **Will** +23
**DR** 15/good and silver; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 29
**Weaknesses** light _[[spells/Aversion|aversion]]_

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 60 ft.
**Melee** bite +32 (4d10+18/19–20 plus 4d6 cold and _[[universal monster rules/Grab|grab]]_), sting +32 (4d6+18/19–20 plus 4d6 cold and poison)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** channel negative energy (9d6, DC 31, 9/day), _[[universal monster rules/Energy Drain|energy drain]]_ (1 level, DC 28), _[[universal monster rules/Swallow Whole|swallow whole]]_ (4d10+22 bludgeoning plus _energy drain_, AC 23, 31 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_[[spells/Air Walk|air walk]]_, _detect magic_, _[[spells/Magic Fang|magic fang]]_
At will—_[[spells/Contagion|contagion]]_ (DC 20), _[[spells/Deeper Darkness|deeper darkness]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3/day—quickened _[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Confusion|confusion]]_ (DC 20), _[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 21)
1/day—_[[spells/Finger Of Death|finger of death]]_ (DC 23), mass _hold monster_ (DC 25), _[[spells/Plane Shift|plane shift]]_ (DC 23), _[[universal monster rules/Summon|summon]]_ (level 8, 6 greater shadows)

##### Statistics
**Str** 41, **Dex** 10, **Con** —, **Int** 20, **Wis** 21, **Cha** 23
**Base Atk** +18; **CMB** +37 (+41 grapple); **CMD** 47 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_cone of cold_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Intimidate +34, Knowledge (arcana) +33, Knowledge (planes) +30, Knowledge (religion) +33, Perception +33, Sense Motive +33, Spellcraft +33, Stealth +16 (+24 in _[[spells/Darkness|darkness]]_), Swim +40; **Racial Modifiers** +8 Stealth in dim light and _darkness_
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary or pair
**Treasure** standard

### Special Abilities

**_Energy Drain_ (Su)** A creature that has been swallowed whole by a nightcrawler gains 1 negative level each round.

**Poison (Su)** Sting—injury; save Fort DC 28; frequency 1/round for 6 rounds; effect 1d4 Constitution drain and 1 negative level; cure 3 consecutive saves. The save DC is Charisma-based.

##### Description

Although the nightcrawler might appear to be little more than an immense and frightening vermin, with its centipede-like body and numerous glowing eyes, it is actually incredibly intelligent. When not cleansing the deep caverns of life, the nightcrawler spends its time plotting how best to carry out its own private stages of the overall nightshade plan to expunge life from all worlds, conferring with its undead minions and, when necessary, observing living creatures from afar while _[[conditions/Invisible|invisible]]_ to learn about hidden enclaves that its depredations might otherwise have missed.

It would be one thing if the nightcrawlers remained in the deep caverns, for these regions are rife with foul life the world is better off without. Yet unfortunately for those who dwell upon the surface, nightcrawlers often crawl up through the tunnels to bring their devastation to the night above. Although they always retreat underground before the first tentative rays of dawn color the eastern skies, they can spread an incredible amount of ruin in the span of a few short hours each night.

A nightcrawler is 60 feet long and weighs 10,000 pounds.