---
cssclass: [monsters]
title1: Seugathi
desc_short: This worm-like monster has a hideous face of eyes and hooked jaws. It
  wields a wand and a sword in its twin tentacle tails.
title2: Seugathi
CR: 6
sources:
- name: Bestiary 2
  page: 243
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: Into the Darklands
  page: 58
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/35E/v5748btpy85ej
XP: 2400
alignment: CE
size: Large
type: aberration
initiative:
  bonus: 9
senses:
  darkvision: 120
  detect thoughts: true
  tremorsense: 30
auras:
- name: madness
  radius: 30
AC:
  AC: 19
  touch: 14
  flat_footed: 14
  components:
    armor: 4
    dex: 5
    natural: 1
    size: -1
HP:
  HP: 67
  long: 9d8+27
  fast_healing: 5
saves:
  fort: 6
  ref: 8
  will: 9
DR:
- amount: 10
  weakness: slashing or piercing
immunities:
- mind-affecting effects
- poison
SR: 17
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk short sword +11/+6 (1d8+3/19-20)
      entries:
      - - damage: 1d8+3
          crit_range: 19-20
      attack: mwk short sword
      bonus:
      - 11
      - 6
    - text: bite +5 (1d8+1 plus poison)
      entries:
      - - damage: 1d8+1
        - effect: poison
      attack: bite
      bonus:
      - 5
  special:
  - confusion command
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 16
  - name: levitate
    source: default
    freq: At will
  - name: confusion
    source: default
    freq: 3/day
    DC: 18
  - name: dispel magic
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 17
  - name: mind fog
    source: default
    freq: 1/day
    DC: 19
  - name: phantasmal killer
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 6
    concentration: 10
ability_scores:
  STR: 16
  DEX: 20
  CON: 17
  INT: 14
  WIS: 17
  CHA: 19
BAB: 6
CMB: 10
CMD: 25
CMD_other: can't be tripped
feats:
- name: Ability Focus (aura of madness)
- name: Combat Casting
- name: Combat Reflexes
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Escape Artist: 17
  Knowledge (religion): 14
  Perception: 15
  Sense Motive: 12
  Stealth: 13
  Use Magic Device: 16
languages:
- Aklo
- Undercommon
- telepathy 100 ft.
special_qualities:
- item use
ecology:
  environment: any underground
  organization: single, pair, or expedition (3-8)
  treasure_type: double
  treasure:
  - masterwork short sword
  - wand of magic missile [CL 5th, 1d20+30 charges]
special_abilities:
  Aura of Madness (Su): Any sane being within 30 feet of a conscious seugathi must
    make a DC 20 Will save each round or become confused for 1 round. A creature that
    fails 5 saves in a row becomes permanently insane, as per the insanity spell.
    A seugathi can suppress or activate this aura as a free action. This is a mind-affecting
    effect. The save DC is Charisma-based.
  Confusion Command (Su): As an immediate action, a seugathi can issue a telepathic
    command to a confused creature within 30 feet. This allows the seugathi to pick
    a result from the confusion behavior table, rather than the confused creature
    rolling randomly for its actions that round.
  Item Use (Ex): A seugathi can utilize spell trigger devices as if it were a spellcaster
    of the appropriate class. As a free action by touch, it can identify all spell
    trigger properties an item has. Use Magic Device is a class skill for seugathis.
  Poison (Ex): Bite-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d2 Wis and deafness; cure 2 consecutive saves. Deafness persists as long as the
    ability damage caused by the poison lasts. The save DC is Constitution-based.
desc_long: Seugathi are spawned by the hundreds by a single neothelid that has performed
  rituals to impregnate itself. As part of the strange process of being spawned in
  such rituals, the seugathi assimilates an extensive list of missions from its parent-once
  the seugathi completes these missions, it perishes. No single seugathi knows the
  purpose of these commands, but they trust that their neothelid masters have a reason
  for sending them on these diverse and usually cruel missions. A seugathi is 14 feet
  long and weighs 650 pounds.

---

# Seugathi
This worm-like monster has a hideous face of eyes and hooked jaws. It wields a wand and a sword in its twin tentacle tails.
**Source** Bestiary 2 pg. 243, Into the Darklands pg. 58
**XP** 2,400
CE Large aberration
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Thoughts|detect thoughts]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +15
**Aura** madness (30 ft.)

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +5 Dex, +1 natural, –1 size)
**hp** 67 (9d8+27); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +6, **Ref** +8, **Will** +9
**DR** 10/slashing or piercing; **Immune** mind-affecting effects, poison; **SR** 17

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Short sword|short sword]]_ +11/+6 (1d8+3/19–20), bite +5 (1d8+1 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Confusion|confusion]]_ _[[spells/Command|command]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +10)
Constant—_[[spells/Mage Armor|mage armor]]_
At will—_detect thoughts_ (DC 16), _[[spells/Levitate|levitate]]_
3/day—_confusion_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Suggestion|suggestion]]_ (DC 17)
1/day—_[[spells/Mind Fog|mind fog]]_ (DC 19), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 18)

##### Statistics
**Str** 16, **Dex** 20, **Con** 17, **Int** 14, **Wis** 17, **Cha** 19
**Base Atk** +6; **CMB** +10; **CMD** 25 (can’t be tripped)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (aura of madness), _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Escape Artist +17, Knowledge (religion) +14, Perception +15, Sense Motive +12, Stealth +13, Use Magic Device +16
**Languages** Aklo, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** item use

##### Ecology

**Environment** any underground
**Organization** single, pair, or expedition (3–8)
**Treasure** double (masterwork _short sword_, wand of _[[spells/Magic Missile|magic missile]]_ [CL 5th, 1d20+30 charges])

### Special Abilities

**Aura of Madness (Su)** Any sane being within 30 feet of a conscious _[[monsters/Seugathi|seugathi]]_ must make a DC 20 Will save each round or become _[[conditions/Confused|confused]]_ for 1 round. A creature that fails 5 saves in a row becomes permanently insane, as per the _[[spells/Insanity|insanity]]_ spell. A _seugathi_ can suppress or activate this aura as a free action. This is a mind-affecting effect. The save DC is Charisma-based.

**_Confusion_ _Command_ (Su)** As an immediate action, a _seugathi_ can issue a telepathic _command_ to a _confused_ creature within 30 feet. This allows the _seugathi_ to pick a result from the _confusion_ behavior table, rather than the _confused_ creature rolling randomly for its actions that round.

**Item Use (Ex) **A _seugathi_ can utilize spell trigger devices as if it were a spellcaster of the appropriate class. As a free action by touch, it can _[[spells/Identify|identify]]_ all spell trigger properties an item has. Use Magic Device is a class skill for seugathis.

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Wis and deafness; cure 2 consecutive saves. Deafness persists as long as the ability damage caused by the poison lasts. The save DC is Constitution-based.

##### Description

_Seugathi_ are spawned by the hundreds by a single _[[monsters/Neothelid|neothelid]]_ that has performed rituals to impregnate itself. As part of the strange process of being spawned in such rituals, the _seugathi_ assimilates an extensive list of missions from its parent—once the _seugathi_ completes these missions, it perishes. No single _seugathi_ knows the purpose of these commands, but they trust that their _neothelid_ masters have a reason for _[[spells/Sending|sending]]_ them on these diverse and usually _[[items/Weapon Magic Abilities/Cruel|cruel]]_ missions. A _seugathi_ is 14 feet long and weighs 650 pounds.