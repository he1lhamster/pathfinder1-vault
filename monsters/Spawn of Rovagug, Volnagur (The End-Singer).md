---
cssclass: [monsters]
title1: Spawn of Rovagug, Volnagur (The End-Singer)
desc_short: This immense creature's warty body is shaped like a many-pointed star,
  and from it sprout nearly a dozen different wings.
title2: Volnagur (The End-Singer)
CR: 22
sources:
- name: Inner Sea Bestiary
  page: 48
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 614400
alignment: CE
size: Colossal
type: magical beast
initiative:
  bonus: 10
senses:
  all-around vision: true
  blindsense: 300
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: frightful presence
  radius: 300
  DC: 27
AC:
  AC: 39
  touch: 9
  flat_footed: 32
  components:
    dex: 6
    dodge: 1
    natural: 30
    size: -8
HP:
  HP: 437
  long: 25d10+300
  regeneration: 30
saves:
  fort: 26
  ref: 20
  will: 12
DR:
- amount: 15
  weakness: epic
immunities:
- ability damage
- acid
- bleed
- disease
- electricity
- energy drain
- mind-affecting effects
- paralysis
- permanent wounds
- petrification
- poison
- polymorph
SR: 33
speeds:
  base: 20
  fly: 100
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +29 (4d6+12)
      entries:
      - - damage: 4d6+12
      attack: bite
      bonus:
      - 29
    - text: 3 razor tongues +29 (2d6+12/18-20/×3 plus 1d6 bleed, 1 Con bleed, and
        blood rage)
      entries:
      - - damage: 2d6+12
          crit_range: 18-20
          crit_multiplier: 3
        - damage: 1d6
          type: bleed
        - damage: '1'
          type: Con bleed
        - effect: blood rage
      count: 3
      attack: razor tongues
      bonus:
      - 29
    - text: 6 wings +24 (2d8+6)
      entries:
      - - damage: 2d8+6
      count: 6
      attack: wings
      bonus:
      - 24
  ranged:
  - - text: 4 eye rays +23 (4d6 sonic/18-20 plus nausea)
      entries:
      - - damage: 4d6
          type: sonic
          crit_range: 18-20
        - effect: nausea
      count: 4
      attack: eye rays
      bonus:
      - 23
space: 30
reach: 30
reach_other: 50 ft. with razor tongues
spell_like_abilities:
  entries:
  - name: acid fog
    source: default
    freq: At will
  - name: greater invisibility
    source: default
    freq: At will
  - name: song of discord
    source: default
    freq: At will
    DC: 20
  - superscripts:
    - APG
    name: winds of vengeance
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 25
    concentration: 30
ability_scores:
  STR: 34
  DEX: 22
  CON: 35
  INT: 7
  WIS: 14
  CHA: 21
BAB: 25
CMB: 45
CMD: 62
CMD_other: can't be tripped
feats:
- name: Ability Focus (eye ray)
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Improved Precise Shot
- name: Improved Vital Strike
- name: Iron Will
- name: Mobility
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Snatch
- name: Vital Strike
skills:
  Fly: 19
  Perception: 20
languages:
- Aklo
special_qualities:
- hibernation
- shatter silence
- unstoppable force
ecology:
  environment: any (Casmaron)
  organization: solitary
  treasure_type: none
special_abilities:
  Blood Rage (Ex): Any creature taking bleed damage from Volnagur's razor tongues
    takes a -4 penalty on Will saves and is affected as the murderous commandUM spell
    (Will DC 16 negates) each round that bleeding continues, ignoring allies that
    are also taking bleed damage from Volnagur.
  Eye Rays (Su): 'Volnagur fires eye rays at a range of up to 120 feet. Creatures
    struck by his eye rays are nauseated for 1 minute (Fortitude DC 29 negates). In
    addition, if the target fails a second Fortitude save against the same DC, it
    gains one of the following conditions, lasting as long as the nauseated condition,
    as its mind and body begin to unravel (roll 1d6): 1-confused, 2-fatigued (exhausted
    if already fatigued), 3-shaken (increase severity of fear effect if already present),
    4-sickened, 5-staggered, 6-stunned. Reroll if an identical condition already exists.
    This is a sonic effect. The save DC is Charisma-based.'
  Shatter Silence (Su): Volnagur's presence unravels magical silence effects or effects
    that provide energy resistance against sonic attacks. At the beginning of its
    turn, any such effect within 60 feet is targeted as dispel magic (caster level
    25th).
desc_long: Volnagur, the End-Singer, is an alien thing whose very presence brings
  turbulence, disturbance, and cacophony wherever he soars. He flits with effortless
  grace upon a hideous assortment of mismatched wings that constantly molt and rot
  from within, the oldest wings falling off as new ones spring up and grow in their
  place. His skirling cry awakens madness and blood fury in those who listen, as does
  the touch of his impossibly long, jagged-razor tongues. Alien harmonics induced
  by his grotesque gaze cripple those upon whom he gazes.

---

# Spawn of Rovagug, Volnagur (The End-Singer)
This immense creature’s warty body is shaped like a many-pointed star, and from it sprout nearly a dozen different wings.
**Source** Inner Sea Bestiary pg. 48
**XP** 614,400
CE Colossal magical beast
**Init** +10; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsense|blindsense]]_ 300 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +20
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 27)

##### Defense

**AC** 39, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+6 Dex, +1 dodge, +30 natural, –8 size)
**hp** 437 (25d10+300); _[[universal monster rules/Regeneration|regeneration]]_ 30
**Fort** +26, **Ref** +20, **Will** +12
**DR** 15/epic; **Immune** ability damage, acid, _[[universal monster rules/Bleed|bleed]]_, disease, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, permanent wounds, petrification, poison, _[[spells/Polymorph|polymorph]]_; **SR** 33

##### Offense
**Speed** 20 ft., fly 100 ft. (perfect)
**Melee** bite +29 (4d6+12), 3 razor _[[spells/Tongues|tongues]]_ +29 (2d6+12/18–20/×3 plus 1d6 _bleed_, 1 Con _bleed_, and _[[universal monster rules/Blood Rage|blood rage]]_), 6 wings +24 (2d8+6)
**Ranged** 4 eye rays +23 (4d6 sonic/18–20 plus nausea)
**Space** 30 ft., **Reach** 30 ft. (50 ft. with razor _tongues_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +30)
At will—_[[spells/Acid Fog|acid fog]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Song of Discord|song of discord]]_ (DC 20)
3/day—_[[spells/Winds of Vengeance|winds of vengeance]]_

##### Statistics
**Str** 34, **Dex** 22, **Con** 35, **Int** 7, **Wis** 14, **Cha** 21
**Base Atk** +25; **CMB** +45; **CMD** 62 (can’t be tripped)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (eye ray), _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +19, Perception +20
**Languages** Aklo
**SQ** hibernation, _[[spells/Shatter|shatter]]_ _[[spells/Silence|silence]]_, unstoppable force

##### Ecology

**Environment** any (Casmaron)
**Organization** solitary
**Treasure** none

### Special Abilities

**_Blood Rage_ (Ex) **Any creature taking _bleed_ damage from Volnagur’s razor _tongues_ takes a –4 penalty on Will saves and is affected as the _[[spells/Murderous Command|murderous command]]_ spell (Will DC 16 negates) each round that bleeding continues, ignoring allies that are also taking _bleed_ damage from Volnagur.

**Eye Rays (Su) **Volnagur fires eye rays at a range of up to 120 feet. Creatures struck by his eye rays are _[[conditions/Nauseated|nauseated]]_ for 1 minute (Fortitude DC 29 negates). In addition, if the target fails a second Fortitude save against the same DC, it gains one of the following conditions, lasting as long as the _nauseated_ condition, as its mind and body begin to unravel (roll 1d6): 1—_[[conditions/Confused|confused]]_, 2—_[[conditions/Fatigued|fatigued]]_ (_[[conditions/Exhausted|exhausted]]_ if already _fatigued_), 3—_[[conditions/Shaken|shaken]]_ (increase severity of _[[universal monster rules/Fear|fear]]_ effect if already present), 4—_[[conditions/Sickened|sickened]]_, 5—_[[conditions/Staggered|staggered]]_, 6—_[[conditions/Stunned|stunned]]_. Reroll if an identical condition already exists. This is a sonic effect. The save DC is Charisma-based.
**_Shatter_ _Silence_ (Su)** Volnagur’s presence unravels magical _silence_ effects or effects that provide _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ against sonic attacks. At the beginning of its turn, any such effect within 60 feet is targeted as _[[spells/Dispel Magic|dispel magic]]_ (caster level 25th).

##### Description

Volnagur, the End-Singer, is an alien thing whose very presence brings turbulence, disturbance, and cacophony wherever he soars. He flits with effortless _[[spells/Grace|grace]]_ upon a hideous assortment of mismatched wings that constantly molt and rot from within, the oldest wings falling off as new ones spring up and grow in their place. His skirling cry awakens madness and blood fury in those who listen, as does the touch of his impossibly long, jagged-razor _tongues_. Alien harmonics induced by his grotesque _[[universal monster rules/Gaze|gaze]]_ cripple those upon whom he gazes.