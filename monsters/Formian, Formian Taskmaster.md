---
cssclass: [monsters]
title1: Formian, Formian Taskmaster
desc_short: This centaurlike creature is equipped with an ant's mandibles and antennae.
title2: Formian Taskmaster
CR: 7
sources:
- name: Bestiary 4
  page: 111
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 3200
alignment: LN
size: Medium
type: monstrous humanoid
initiative:
  bonus: 2
  other:
    with hive mind: 6
senses:
  blindsight: 30
  darkvision: 60
  hive mind: true
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    dex: 2
    natural: 8
HP:
  HP: 85
  long: 10d10+30
saves:
  fort: 6
  ref: 9
  will: 10
resistances:
  sonic: 10
speeds:
  base: 40
attacks:
  melee:
  - - text: sting +13 (1d4+3 plus poison)
      entries:
      - - damage: 1d4+3
        - effect: poison
      attack: sting
      bonus:
      - 13
    - text: 2 claws +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 13
  ranged:
  - - text: dart +12/+7 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: dart
      bonus:
      - 12
      - 7
  special:
  - poison
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 16
  - name: sending
    source: default
    freq: 3/day
    other: to the hive queen only
  sources:
  - name: default
    CL: 10
    concentration: 14
spells:
  entries:
  - name: confusion
    source: Bard
    level: 3
    DC: 18
  - name: good hope
    source: Bard
    level: 3
  - name: heroism
    source: Bard
    level: 2
  - name: invisibility
    source: Bard
    level: 2
  - name: sound burst
    source: Bard
    level: 2
    DC: 16
  - name: suggestion
    source: Bard
    level: 2
    DC: 17
  - name: charm person
    source: Bard
    level: 1
    DC: 16
  - name: comprehend languages
    source: Bard
    level: 1
  - name: cure light wounds
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 16
  - name: silent image
    source: Bard
    level: 1
    DC: 15
  - name: dancing lights
    source: Bard
    level: 0
  - name: daze
    source: Bard
    level: 0
    DC: 15
  - name: detect magic
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 7
    concentration: 11
    slots:
      3: 2
      2: 4
      1: 5
      0: at-will
ability_scores:
  STR: 17
  DEX: 14
  CON: 16
  INT: 13
  WIS: 16
  CHA: 19
BAB: 10
CMB: 13
CMD: 26
CMD_other: 30 vs. trip
feats:
- name: Combat Casting
- name: Point-Blank Shot
- name: Quick Draw
- name: Rapid Shot
- name: Spell Focus (enchantment)
skills:
  Appraise: 6
  Bluff: 9
  Climb: 11
  Craft (armor): 9
  Diplomacy: 14
  Perception: 16
    with hive mind: 20
  Sense Motive: 8
  Spellcraft: 6
languages:
- Common
- telepathy 120 ft.
special_qualities:
- formian traits
- mental motivator (20 rounds/day)
ecology:
  environment: warm or temperate land or underground
  organization: solitary, work crew (1 plus 6-12 workers), band (1 plus 3-15 workers
    and 5-8 warriors), embassy (2-6)
  treasure_type: standard
  treasure:
  - 10 darts
  - other treasure
special_abilities:
  Mental Motivator (Su): A formian taskmaster can inspire competence or inspire courage
    as a 7th-level bard (typically 20 rounds/day). The taskmaster's performance is
    purely mental and only affects formians from its own hive within telepathic range.
  Poison (Ex): Sting-injury; save Fort DC 18; frequency 1/round for 6 rounds; effect
    1d4 Dexterity; cure 2 consecutive saves.
  Spells: A formian taskmaster casts spells as a 7th-level bard. It favors enchantment
    and illusion spells.
desc_long: |-
  Formian taskmasters are merchants, traders, diplomats, and spies, and particularly talented taskmasters may even advise the queen. Taskmasters can often be found outside the hive engaging in commerce or routine diplomatic missions. While traveling, a taskmaster is usually accompanied by 3-5 workers and at least 5 warriors.

  When dealing with other creatures, formians recognize that their telepathy can be offputting and use normal speech, although their mandibles are not well suited for the task and their voices are often hoarse and difficult to understand.

  Like myrmarchs, taskmasters are highly competitive and take great pride in their successes. Notable accomplishments are carved into their carapaces and highlighted with the use of bright inks, precious metals, or gems. Formian society is largely free of the crime that is common in other humanoid societies, but formians do have occasional duels within a caste.

  Two taskmasters might have a duel over promotions, a trade route, or an insult. These duels are rarely lethal for fear of weakening the hive, and taskmasters who are too aggressive attract the wrong kind of attention from the myrmarchs. Dueling victories are often recorded on taskmasters' carapaces alongside their other major accomplishments.

---

# Formian, Formian Taskmaster
This centaurlike creature is equipped with an ant’s mandibles and antennae.
**Source** Bestiary 4 pg. 111
**XP** 3,200

LN Medium monstrous humanoid
**Init** +2 (+6 with hive mind); **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., hive mind; Perception +16 (+20 with hive mind)

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 Dex, +8 natural)
**hp** 85 (10d10+30)
**Fort** +6, **Ref** +9, **Will** +10
**Resist** sonic 10

##### Offense
**Speed** 40 ft.
**Melee** sting +13 (1d4+3 plus poison), 2 claws +13 (1d4+3)
**Ranged** _[[items/Weapon/Dart|dart]]_ +12/+7 (1d4+3)
**Special Attacks** poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Sending|sending]]_ (to the hive queen only)
**_[[classes/Bard|Bard]]_ Spells Known **(caster level 7th; concentration +11)
3rd (2)—_[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Good Hope|good hope]]_
2nd (4)—_[[spells/Heroism|heroism]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Sound Burst|sound burst]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 17)
1st (5)—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 16), _[[spells/Silent Image|silent image]]_ (DC 15)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 17, **Dex** 14, **Con** 16, **Int** 13, **Wis** 16, **Cha** 19
**Base Atk** +10; **CMB** +13; **CMD** 26 (30 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Appraise +6, Bluff +9, _[[universal monster rules/Climb|Climb]]_ +11, Craft (armor) +9, Diplomacy +14, Perception +16 (+20 with hive mind), Sense Motive +8, Spellcraft +6
**Languages** Common; _[[universal monster rules/Telepathy|telepathy]]_ 120 ft.
**SQ** formian traits, mental motivator (20 rounds/day)

##### Ecology

**Environment** warm or temperate land or underground
**Organization** solitary, work crew (1 plus 6–12 workers), band (1 plus 3–15 workers and 5–8 warriors), embassy (2–6)
**Treasure** standard (10 darts, other treasure)

### Special Abilities

**Mental Motivator (Su)** A formian _[[feats/Taskmaster|taskmaster]]_ can inspire competence or inspire courage as a 7th-level _bard_ (typically 20 rounds/day). The _taskmaster_’s performance is purely mental and only affects formians from its own hive within telepathic range.

**Poison (Ex)** Sting—injury; save Fort DC 18; frequency 1/round for 6 rounds; effect 1d4 Dexterity; cure 2 consecutive saves.
**Spells** A formian _taskmaster_ casts spells as a 7th-level _bard_. It favors enchantment and illusion spells.

##### Description

Formian taskmasters are merchants, traders, diplomats, and spies, and particularly talented taskmasters may even advise the queen. Taskmasters can often be found outside the hive engaging in commerce or routine diplomatic missions. While traveling, a _taskmaster_ is usually accompanied by 3–5 workers and at least 5 warriors.

When dealing with other creatures, formians recognize that their _telepathy_ can be offputting and use normal speech, although their mandibles are not well suited for the task and their voices are often hoarse and difficult to understand.

Like myrmarchs, taskmasters are highly competitive and take great pride in their successes. Notable accomplishments are carved into their carapaces and highlighted with the use of bright inks, precious metals, or gems. Formian society is largely free of the crime that is common in other humanoid societies, but formians do have occasional duels within a caste.

Two taskmasters might have a duel over promotions, a trade route, or an insult. These duels are rarely lethal for _[[universal monster rules/Fear|fear]]_ of weakening the hive, and taskmasters who are too aggressive attract the wrong kind of attention from the myrmarchs. _[[items/Weapon Magic Abilities/Dueling|Dueling]]_ victories are often recorded on taskmasters’ carapaces alongside their other major accomplishments.