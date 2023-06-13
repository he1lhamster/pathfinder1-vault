---
cssclass: [monsters]
title1: Nightshade, Nightwalker
desc_short: This towering, night-black giant has demonic features, including a huge
  pair of ram-like horns. Its arms end in massive blades.
title2: Nightwalker
CR: 16
sources:
- name: Bestiary 2
  page: 201
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 76800
alignment: CE
size: Huge
type: undead
subtypes:
- extraplanar
- nightshade
initiative:
  bonus: 2
senses:
  darksense: true
  darkvision: 60
  detect magic: true
  low-light vision: true
auras:
- name: desecrating aura
  radius: 30
AC:
  AC: 31
  touch: 10
  flat_footed: 29
  components:
    dex: 2
    natural: 21
    size: -2
HP:
  HP: 241
  long: 21d8+147
saves:
  fort: 14
  ref: 11
  will: 19
DR:
- amount: 15
  weakness: good and silver
immunities:
- cold
- undead traits
SR: 27
weaknesses:
- light aversion
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 claws +28 (3d6+15/19-20 plus 4d6 cold)
      entries:
      - - damage: 3d6+15
          crit_range: 19-20
        - damage: 4d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 28
  special:
  - channel energy (8d6, DC 29, 8/day)
  - fear gaze
  - swift sundering
space: 15
reach: 15
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
    DC: 19
  - name: deeper darkness
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 19
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: haste
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 3/day
    DC: 20
  - name: invisibility
    source: default
    freq: 3/day
  - name: quickened unholy blight
    source: default
    freq: 3/day
    DC: 19
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 20
  - name: finger of death
    source: default
    freq: 1/day
    DC: 22
  - name: plane shift
    source: default
    freq: 1/day
    DC: 22
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: greater shadows
      amount: 4
  sources:
  - name: default
    CL: 16
    concentration: 21
ability_scores:
  STR: 35
  DEX: 14
  CON:
  INT: 20
  WIS: 21
  CHA: 21
BAB: 15
CMB: 29
CMD: 41
feats:
- name: Combat Expertise
- name: Command Undead
- name: Greater Sunder
- name: Greater Vital Strike
- name: Improved Critical (claws)
- name: Improved Disarm
- name: Improved Sunder
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (unholy blight)
- name: Vital Strike
skills:
  Intimidate: 29
  Knowledge (arcana): 29
  Knowledge (planes): 26
  Knowledge (religion): 29
  Perception: 29
  Sense Motive: 29
  Spellcraft: 29
  Stealth: 18
    in darkness: 26
  Swim: 33
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
  organization: solitary, pair, or gang (3-4)
  treasure_type: standard
special_abilities:
  Fear Gaze (Su): Cower in fear for 1 round, 30 feet, Will DC 25 negates. This is
    a mind-affecting fear effect. The save DC is Charisma-based.
  Swift Sundering (Su): A nightwalker can make a sunder attempt as a swift action
    with one of its claws.
desc_long: |-
  The most commonly encountered nightshade is the giant-like nightwalker. This powerful foe leads armies of undead against the living, but unlike most mortal generals the nightwalker is not content to stand back and observe the battles from safety. The undead creature is ever eager to put its tactics and plans to the test itself, and takes part in battles in every possible occurrence save for those that the creature has determined are self-destructive. This is not to say that the nightwalker never sacrifices its troops to gain a tactical advantage-just that these attacks are the only ones the monster feels no urge to participate in directly.

  Nightwalkers enjoy inflicting despair before death, particularly by destroying valued objects or murdering loved ones before delivering the final blow to a foe.

  A nightwalker is 20 feet tall and weighs 5,000 pounds.

---

# Nightshade, Nightwalker
This towering, night-black giant has demonic features, including a huge pair of ram-like horns. Its arms end in massive blades.
**Source** Bestiary 2 pg. 201
**XP** 76,800
CE Huge undead (extraplanar, nightshade)
**Init** +2; **Senses** darksense, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +29
**Aura** desecrating aura (30 ft.)

##### Defense

**AC** 31, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+2 Dex, +21 natural, –2 size)
**hp** 241 (21d8+147)
**Fort** +14, **Ref** +11, **Will** +19
**DR** 15/good and silver; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 27
**Weaknesses** light _[[spells/Aversion|aversion]]_

##### Offense
**Speed** 40 ft.
**Melee** 2 claws +28 (3d6+15/19–20 plus 4d6 cold)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** channel energy (8d6, DC 29, 8/day), _[[universal monster rules/Fear|fear]]_ _[[universal monster rules/Gaze|gaze]]_, swift sundering
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +21)
Constant—_[[spells/Air Walk|air walk]]_, _detect magic_, _[[spells/Magic Fang|magic fang]]_
At will—_[[spells/Contagion|contagion]]_ (DC 19), _[[spells/Deeper Darkness|deeper darkness]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3/day—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Invisibility|invisibility]]_, quickened _unholy blight_ (DC 19)
1/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 20), _[[spells/Finger Of Death|finger of death]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 7, 4 greater shadows)

##### Statistics
**Str** 35, **Dex** 14, **Con** —, **Int** 20, **Wis** 21, **Cha** 21
**Base Atk** +15; **CMB** +29; **CMD** 41
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_unholy blight_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Intimidate +29, Knowledge (arcana) +29, Knowledge (planes) +26, Knowledge (religion) +29, Perception +29, Sense Motive +29, Spellcraft +29, Stealth +18 (+26 in _[[spells/Darkness|darkness]]_), Swim +33; **Racial Modifiers** +8 Stealth in dim light and _darkness_
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary, pair, or gang (3–4)
**Treasure** standard

### Special Abilities

**_Fear_ _Gaze_ (Su)** Cower in _fear_ for 1 round, 30 feet, Will DC 25 negates. This is a mind-affecting _fear_ effect. The save DC is Charisma-based.
**Swift Sundering (Su)** A nightwalker can make a sunder attempt as a swift action with one of its claws.

##### Description

The most commonly encountered nightshade is the giant-like nightwalker. This powerful foe leads armies of undead against the living, but unlike most mortal generals the nightwalker is not content to stand back and observe the battles from safety. The undead creature is ever eager to put its tactics and plans to the test itself, and takes part in battles in every possible occurrence save for those that the creature has determined are self-destructive. This is not to say that the nightwalker never sacrifices its troops to gain a tactical advantage—just that these attacks are the only ones the monster feels no urge to participate in directly.

Nightwalkers enjoy inflicting despair before death, particularly by destroying valued objects or murdering loved ones before delivering the final blow to a foe.

A nightwalker is 20 feet tall and weighs 5,000 pounds.