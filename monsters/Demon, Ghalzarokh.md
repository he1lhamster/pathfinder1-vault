---
cssclass: [monsters]
title1: Demon, Ghalzarokh
desc_short: This corpulent, four-armed fiend is covered in yellow-orange dragon scales,
  and draconic wings sprout from its back.
title2: Ghalzarokh
CR: 15
sources:
- name: Book of the Damned
  page: 246
  link: http://paizo.com/products/btpy9tok
XP: 51200
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  scent: true
  see invisibility: true
AC:
  AC: 30
  touch: 12
  flat_footed: 27
  components:
    dex: 3
    natural: 18
    size: -1
HP:
  HP: 218
  long: 19d10+114
saves:
  fort: 17
  ref: 11
  will: 18
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- electricity
- fire
- mind-affecting effects
- poison
resistances:
  acid: 10
  cold: 10
SR: 26
speeds:
  base: 20
  burrow: 20
  fly: 50
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +25 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: bite
      bonus:
      - 25
    - text: 4 claws +25 (2d4+7/19-20)
      entries:
      - - damage: 2d4+7
          crit_range: 19-20
      count: 4
      attack: claws
      bonus:
      - 25
  special:
  - breath weapon (30-foot cone, once every 1d4 rounds, 10d6 acid and 10d6 fire, Reflex
    DC 25 half)
  - project blame
  - rend (2 claws, 2d4+10)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: charm monster
    source: default
    freq: At will
    DC: 20
  - name: greater command
    source: default
    freq: At will
    DC: 21
  - name: dominate person
    source: default
    freq: 3/day
    DC: 21
  - name: quickened fireball
    source: default
    freq: 3/day
    DC: 19
  - name: rage
    source: default
    freq: 3/day
    DC: 19
  - name: song of discord
    source: default
    freq: 3/day
    DC: 21
  - name: demand
    source: default
    freq: 1/day
    DC: 24
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 22
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: succubus
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 15
    concentration: 21
ability_scores:
  STR: 25
  DEX: 16
  CON: 22
  INT: 16
  WIS: 25
  CHA: 22
BAB: 19
CMB: 27
CMD: 40
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Hover
- name: Improved Critical (claw)
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (fireball)
- name: Staggering Critical
- name: Wingover
skills:
  Bluff: 28
  Fly: 19
  Intimidate: 35
  Knowledge (arcana): 25
  Knowledge (planes): 25
  Perception: 37
  Sense Motive: 29
  Spellcraft: 25
  Stealth: 21
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- telepathy 100 ft.
- truespeech
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or trio
  treasure_type: double
special_abilities:
  Project Blame (Su): When a ghalzarokh misses with a melee attack against a creature,
    that creature suffers a -1 penalty to AC for 1 round. Whenever a creature succeeds
    at a saving throw against a ghalzarokh's spell-like abilities or breath weapon,
    that creature suffers a -1 penalty on saving throws for 1 round. These penalties
    can stack up to three times per target, so a creature can take up to a -3 penalty
    to AC and a -3 penalty on saving throws. At the end of a creature's turn, it can
    attempt a DC 25 Will saving throw to reduce one of these penalties by 1 as a free
    action. This is a mind-affecting curse effect. The save DC is Charisma-based.
desc_long: Ghalzarokhs, or tyranny demons, act as commanders of Abyssal forces. These
  demons are formed from the souls of petty tyrants and would-be dictators. Notoriously
  egotistical and prone to lashing out, a ghalzarokh keeps its minions in line through
  fear of its cruel whims.

---

# Demon, Ghalzarokh
This corpulent, four-armed fiend is covered in yellow-orange dragon scales, and draconic wings sprout from its back.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 246
**XP** 51,200
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +37

##### Defense

**AC** 30, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+3 Dex, +18 natural, -1 size)
**hp** 218 (19d10+114)
**Fort** +17, **Ref** +11, **Will** +18
**DR** 10/cold iron and good; **Immune** electricity, fire, mind-affecting effects, poison; **Resist** acid 10, cold 10; **SR** 26

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 50 ft. (poor)
**Melee** bite +25 (1d8+7), 4 claws +25 (2d4+7/19-20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-foot cone, once every 1d4 rounds, 10d6 acid and 10d6 fire, Reflex DC 25 half), project blame, _[[universal monster rules/Rend|rend]]_ (2 claws, 2d4+10)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
Constant—_see invisibility_
 At will—_[[spells/Charm Monster|charm monster]]_ (DC 20), greater _[[spells/Command|command]]_ (DC 21)
 3/day—_[[spells/Dominate Person|dominate person]]_ (DC 21), quickened _[[spells/Fireball|fireball]]_ (DC 19), _[[spells/Rage|rage]]_ (DC 19), _[[spells/Song of Discord|song of discord]]_ (DC 21)
 1/day—_[[spells/Demand|demand]]_ (DC 24), mass _[[spells/Suggestion|suggestion]]_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 6, 1 succubus 35%)

##### Statistics
**Str** 25, **Dex** 16, **Con** 22, **Int** 16, **Wis** 25, **Cha** 22
**Base Atk** +19; **CMB** +27; **CMD** 40
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_fireball_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +28, Fly +19, Intimidate +35, Knowledge (arcana, planes) +25, Perception +37, Sense Motive +29, Spellcraft +25, Stealth +21; **Racial Modifiers** +8 Perception
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.; truespeech

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or trio
**Treasure** double

### Special Abilities

**Project Blame (Su)** When a ghalzarokh misses with a melee attack against a creature, that creature suffers a –1 penalty to AC for 1 round. Whenever a creature succeeds at a saving throw against a ghalzarokh’s _spell-like abilities_ or _breath weapon_, that creature suffers a –1 penalty on saving throws for 1 round. These penalties can stack up to three times per target, so a creature can take up to a –3 penalty to AC and a –3 penalty on saving throws. At the end of a creature’s turn, it can attempt a DC 25 Will saving throw to reduce one of these penalties by 1 as a free action. This is a mind-affecting curse effect. The save DC is Charisma-based.

##### Description

Ghalzarokhs, or tyranny demons, act as commanders of Abyssal forces. These demons are formed from the souls of petty tyrants and would-be dictators. Notoriously egotistical and _[[conditions/Prone|prone]]_ to lashing out, a ghalzarokh keeps its minions in line through _[[universal monster rules/Fear|fear]]_ of its _[[items/Weapon Magic Abilities/Cruel|cruel]]_ whims.