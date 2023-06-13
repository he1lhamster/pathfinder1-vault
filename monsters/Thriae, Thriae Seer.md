---
cssclass: [monsters]
title1: Thriae, Thriae Seer
desc_short: Lithe and beautiful, this half-bee, half-woman creature wears elaborate
  makeup and wields an ornate staff.
title2: Thriae Seer
CR: 11
sources:
- name: Bestiary 3
  page: 264
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 12800
alignment: LN
size: Medium
type: monstrous humanoid
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect secret doors: true
  low-light vision: true
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    dex: 5
    natural: 10
HP:
  HP: 133
  long: 14d10+56
saves:
  fort: 8
  ref: 16
  will: 15
immunities:
- poison
- sonic
resistances:
  acid: 10
SR: 22
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +2 quarterstaff +16/+11/+6 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: +2 quarterstaff
      bonus:
      - 16
      - 11
      - 6
    - text: +2 quarterstaff +16/+11 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: +2 quarterstaff
      bonus:
      - 16
      - 11
    - text: sting +11 (1d8+1 plus mind sting)
      entries:
      - - damage: 1d8+1
        - effect: mind sting
      attack: sting
      bonus:
      - 11
  special:
  - merope consumption
spell_like_abilities:
  entries:
  - name: detect secret doors
    source: default
    freq: Constant
  - name: calm emotions
    source: default
    freq: At will
    DC: 20
  - name: detect thoughts
    source: default
    freq: At will
    DC: 20
  - name: sound burst
    source: default
    freq: At will
    DC: 20
  - name: divination
    source: default
    freq: 3/day
  - name: invisibility purge
    source: default
    freq: 3/day
  - name: locate object
    source: default
    freq: 3/day
  - name: misdirection
    source: default
    freq: 3/day
    DC: 20
  - name: symbol of sleep
    source: default
    freq: 3/day
    DC: 23
  - name: summon bees
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: giant queen bees
      amount: 1d3
    - name: wasp swarms
      amount: 1d4
  - name: true seeing
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 22
ability_scores:
  STR: 14
  DEX: 20
  CON: 19
  INT: 19
  WIS: 22
  CHA: 27
BAB: 14
CMB: 19
CMD: 31
feats:
- name: Agile Maneuvers
- name: Alertness
- name: Combat Casting
- name: Combat Reflexes
- name: Improved Two-Weapon Fighting
- name: Lightning Reflexes
- name: Two-Weapon Fighting
skills:
  Bluff: 22
  Diplomacy: 22
  Fly: 26
  Knowledge (arcana): 18
  Perception: 27
  Sense Motive: 24
  Spellcraft: 18
  Use Magic Device: 22
languages:
- Common
- Sylvan
- Thriae
ecology:
  environment: any
  organization: solitary, pair, or triad
  treasure_type: double
  treasure:
  - +2 quarterstaff
  - 3 doses of merope
  - other treasure
special_abilities:
  Merope Consumption (Su): Three times per day as a standard action, a thriae seer
    can consume a dose of merope in order to further tap into her spiritual powers
    for 1d6+3 rounds. Starting on the round after she consumes the merope, the thriae
    seer gains an insight bonus to her AC and on damage done with melee attacks equal
    to her Wisdom modifier (+6 for most thriae seers).
  Mind Sting (Su): A target stung by a thriae seer becomes confused for 1d4 rounds
    unless it makes a successful DC 21 Will save. This is a mind-affecting effect.
    The save DC is Constitution-based.
desc_long: |-
  Sought after for their wisdom and guidance as well as their enchanting beauty, thriae seers are among the most spiritually gifted members of their colony. Their prowess for foretelling the future and deciding upon the soundest courses of action in dire situations earns them respect from other thriae as well as outsiders from other societies, and seers wield their gift with a stoic humbleness. Nonetheless, most seers expect an offering before they will grant an audience a divination. These offerings usually consist of ornate jewelry and sums of gold, though some seers desire the company of humanoid male or female consorts, many of whom gladly oblige the captivating seer with their presence.

  While their combative abilities mainly comprise their magical powers and they appear at first glance to be thin and frail, seers still possess the trademark strength and resilience of all thriae.

  Thriae seers spend most of their time meditating in one of the many chambers in the colony's hive dedicated to such activities. Consuming large amounts of their queen's merope to enhance their powers of divination, seers ponder the best solutions to their colony's problems, and often act as a sort of spiritual political council for the queen. If a particularly wealthy group of outsiders has sought the counsel of several thriae seers, this council of prophetesses will combine their powers in order to read a difficult divination.

  Thriae seers are 6 feet from head to toe and weigh 150 pounds. The thriae seer presented here represents the least of her kind. Many thriae seers take levels of monk or rogue so as to be even more adept at protecting their queen. Thriae oracles and sorcerers are also relatively common-such thriae are particularly valued by their hive for their magical abilities.

---

# Thriae, Thriae Seer
Lithe and beautiful, this half-bee, half-woman creature wears elaborate makeup and wields an ornate staff.
**Source** Bestiary 3 pg. 264
**XP** 12,800

LN Medium monstrous humanoid
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Secret Doors|detect secret doors]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +27

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 Dex, +10 natural)
**hp** 133 (14d10+56)
**Fort** +8, **Ref** +16, **Will** +15
**Immune** poison, sonic; **Resist** acid 10; **SR** 22

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** +2 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +16/+11/+6 (1d6+4), +2 _quarterstaff_ +16/+11 (1d6+3), sting +11 (1d8+1 plus mind sting)
**Special Attacks** merope _[[feats/Consumption|consumption]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +22)
Constant—_detect secret doors_
At will—_[[spells/Calm Emotions|calm emotions]]_ (DC 20), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 20), _[[spells/Sound Burst|sound burst]]_ (DC 20)
3/day—_[[spells/Divination|divination]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Misdirection|misdirection]]_ (DC 20), _[[spells/Symbol of Sleep|symbol of sleep]]_ (DC 23)
1/day—_[[universal monster rules/Summon|summon]]_ bees (level 5, 1d3 giant queen bees or 1d4 wasp swarms), _[[spells/True Seeing|true seeing]]_

##### Statistics
**Str** 14, **Dex** 20, **Con** 19, **Int** 19, **Wis** 22, **Cha** 27
**Base Atk** +14; **CMB** +19; **CMD** 31
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_
**Skills** Bluff +22, Diplomacy +22, Fly +26, Knowledge (arcana) +18, Perception +27, Sense Motive +24, Spellcraft +18, Use Magic Device +22
**Languages** Common, Sylvan, Thriae

##### Ecology

**Environment** any
**Organization** solitary, pair, or triad
**Treasure** double (+2 _quarterstaff_, 3 doses of merope, other treasure)

### Special Abilities

**Merope _Consumption_ (Su)** Three times per day as a standard action, a thriae seer can consume a dose of merope in order to further tap into her spiritual powers for 1d6+3 rounds. Starting on the round after she consumes the merope, the thriae seer gains an insight bonus to her AC and on damage done with melee attacks equal to her Wisdom modifier (+6 for most thriae seers).

**Mind Sting (Su)** A target stung by a thriae seer becomes _[[conditions/Confused|confused]]_ for 1d4 rounds unless it makes a successful DC 21 Will save. This is a mind-affecting effect. The save DC is Constitution-based.

##### Description

Sought after for their wisdom and _[[spells/Guidance|guidance]]_ as well as their enchanting beauty, thriae seers are among the most spiritually gifted members of their colony. Their prowess for foretelling the future and deciding upon the soundest courses of action in dire situations earns them respect from other thriae as well as outsiders from other societies, and seers wield their gift with a _[[feats/Stoic|stoic]]_ humbleness. Nonetheless, most seers expect an offering before they will grant an audience a _divination_. These offerings usually consist of ornate _[[items/Mundane/Jewelry|jewelry]]_ and sums of gold, though some seers desire the company of humanoid male or female consorts, many of whom gladly oblige the captivating seer with their presence.

While their combative abilities mainly comprise their magical powers and they appear at first glance to be thin and frail, seers still possess the trademark strength and resilience of all thriae.

Thriae seers spend most of their time meditating in one of the many chambers in the colony’s hive dedicated to such activities. Consuming large amounts of their queen’s merope to enhance their powers of _divination_, seers ponder the best solutions to their colony’s problems, and often act as a sort of spiritual political council for the queen. If a particularly wealthy group of outsiders has sought the counsel of several thriae seers, this council of prophetesses will combine their powers in order to read a difficult _divination_.

Thriae seers are 6 feet from head to toe and weigh 150 pounds. The thriae seer presented here represents the least of her kind. Many thriae seers take levels of _[[classes/Monk|monk]]_ or _[[classes/Rogue|rogue]]_ so as to be even more adept at protecting their queen. Thriae oracles and sorcerers are also relatively common—such thriae are particularly valued by their hive for their magical abilities.