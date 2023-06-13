---
cssclass: [monsters]
title1: Nightshade, Nightwing
desc_short: This enormous, bat-like creature is shaped from utter darkness, its eyes
  tiny red stars in the blackest night.
title2: Nightwing
CR: 14
sources:
- name: Bestiary 2
  page: 203
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 38400
alignment: CE
size: Huge
type: undead
subtypes:
- extraplanar
- nightshade
initiative:
  bonus: 8
senses:
  darksense: true
  darkvision: 60
  detect magic: true
  low-light vision: true
auras:
- name: desecrating aura
  radius: 30
AC:
  AC: 29
  touch: 12
  flat_footed: 25
  components:
    dex: 4
    natural: 17
    size: -2
HP:
  HP: 195
  long: 17d8+119
saves:
  fort: 12
  ref: 11
  will: 17
DR:
- amount: 15
  weakness: good and silver
immunities:
- cold
- undead traits
SR: 25
weaknesses:
- light aversion
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +23 (4d10+18/19-20 plus 4d6 cold and magic drain)
      entries:
      - - damage: 4d10+18
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: magic drain
      attack: bite
      bonus:
      - 23
  special:
  - channel energy (7d6, DC 28, 8/day)
space: 15
reach: 15
spell_like_abilities:
  entries:
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
  - name: unholy blight
    source: default
    freq: At will
    DC: 19
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: greater dispel magic
    source: default
    freq: 3/day
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
    level: 6
    summons:
    - name: greater shadows
      amount: 2
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 31
  DEX: 18
  CON:
  INT: 18
  WIS: 21
  CHA: 21
BAB: 12
CMB: 24
CMD: 38
feats:
- name: Cleave
- name: Combat Reflexes
- name: Command Undead
- name: Great Cleave
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Sunder
- name: Power Attack
- name: Snatch
skills:
  Fly: 24
  Knowledge (arcana): 24
  Knowledge (religion): 24
  Perception: 25
  Sense Motive: 25
  Spellcraft: 24
  Stealth: 16
    in darkness: 24
  Swim: 27
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
  organization: solitary, pair, or flight (3-6)
  treasure_type: standard
special_abilities:
  Magic Drain (Su): The bite of a nightwing drains magical power and energy. When
    a nightwing bites a foe, the victim must make a DC 23 Will save or one spell effect
    currently affecting him immediately ends-determine which spell is drained randomly
    if the target is under the effects of more than one spell. The nightwing heals
    damage equal to twice the level of the spell drained-hit points in excess of its
    maximum are instead gained as temporary hit points that last for 1 hour. If a
    nightwing attempts to sunder a magic item with its bite, its magic-draining bite
    renders the item nonmagical for 1d4 rounds (if the item is a permanent magic item),
    drains 1d8 charges (if the item has charges), or renders it permanently nonmagical
    (if the item is a one-use item). The item (or its wielder, if the item is attended)
    can resist this effect with a DC 23 Will save. Damage dealt to an item is applied
    after the effects of magic drain are applied. The save DC is Charisma-based.
desc_long: |-
  The least of the known types of nightshade, the nightwing is nevertheless a deadly foe. Nightwings often serve more powerful nightshades as aerial support. These nightshades are also the most likely to be found serving a non-undead master-nightwings are often used by powerful mortals as guardians or sentinels. Despite this, nightwings still hope to someday slay any master they serve. They enter servitude primarily as a method of aiding a destructive or murderous mortal in their task of mass murder; once this task is over, or if at any point the nightwing believes its master is slacking in its murderous duties, the nightwing is swift to turn on its one-time ally.

  A nightwing found on the Material Plane not in the employ of a more powerful master is typically encountered in rugged terrain where there are numerous locations that can provide shelter when the sun rises. The monsters prefer caves and abandoned buildings for this purpose.

  A nightwing's body is 20 feet long, but its wingspan is 80 feet. It weighs 4,500 pounds.

---

# Nightshade, Nightwing
This enormous, bat-like creature is shaped from utter _[[spells/Darkness|darkness]]_, its eyes tiny red stars in the blackest night.
**Source** Bestiary 2 pg. 203
**XP** 38,400
CE Huge undead (extraplanar, nightshade)
**Init** +8; **Senses** darksense, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +25
**Aura** desecrating aura (30 ft.)

##### Defense

**AC** 29, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +17 natural, –2 size)
**hp** 195 (17d8+119)
**Fort** +12, **Ref** +11, **Will** +17
**DR** 15/good and silver; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 25
**Weaknesses** light _[[spells/Aversion|aversion]]_

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** bite +23 (4d10+18/19–20 plus 4d6 cold and magic drain)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** channel energy (7d6, DC 28, 8/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
Constant—_detect magic_, _[[spells/Magic Fang|magic fang]]_
At will—_[[spells/Contagion|contagion]]_ (DC 19), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3/day—_[[spells/Confusion|confusion]]_ (DC 19), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Invisibility|invisibility]]_
1/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 20), _[[spells/Finger Of Death|finger of death]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 6, 2 greater shadows)

##### Statistics
**Str** 31, **Dex** 18, **Con** —, **Int** 18, **Wis** 21, **Cha** 21
**Base Atk** +12; **CMB** +24; **CMD** 38
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_
**Skills** Fly +24, Knowledge (arcana) +24, Knowledge (religion) +24, Perception +25, Sense Motive +25, Spellcraft +24, Stealth +16 (+24 in _darkness_), Swim +27; **Racial Modifiers** +8 Stealth in dim light and _darkness_
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–6)
**Treasure** standard

### Special Abilities

**Magic Drain (Su)** The bite of a nightwing drains magical power and energy. When a nightwing bites a foe, the victim must make a DC 23 Will save or one spell effect currently affecting him immediately ends—determine which spell is drained randomly if the target is under the effects of more than one spell. The nightwing heals damage equal to twice the level of the spell drained—hit points in excess of its maximum are instead gained as temporary hit points that last for 1 hour. If a nightwing attempts to sunder a magic item with its bite, its magic-draining bite renders the item nonmagical for 1d4 rounds (if the item is a permanent magic item), drains 1d8 charges (if the item has charges), or renders it permanently nonmagical (if the item is a one-use item). The item (or its wielder, if the item is attended) can resist this effect with a DC 23 Will save. Damage dealt to an item is applied after the effects of magic drain are applied. The save DC is Charisma-based.

##### Description

The least of the known types of nightshade, the nightwing is nevertheless a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ foe. Nightwings often serve more powerful nightshades as aerial support. These nightshades are also the most likely to be found serving a non-undead master—nightwings are often used by powerful mortals as guardians or sentinels. Despite this, nightwings still hope to someday slay any master they serve. They enter servitude primarily as a method of aiding a destructive or murderous mortal in their task of mass murder; once this task is over, or if at any point the nightwing believes its master is slacking in its murderous duties, the nightwing is swift to turn on its one-time ally.

A nightwing found on the Material Plane not in the employ of a more powerful master is typically encountered in rugged terrain where there are numerous locations that can provide shelter when the sun rises. The monsters prefer caves and abandoned buildings for this purpose.

A nightwing’s body is 20 feet long, but its wingspan is 80 feet. It weighs 4,500 pounds.