---
cssclass: [monsters]
title1: Demon, Nabasu
desc_short: This lanky fiend's mouth is filled with sharp fangs, while great bat-like
  wings stretch from its scaly hide.
title2: Nabasu
CR: 8
sources:
- name: Pathfinder RPG Bestiary
  page: 64
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 4800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- native
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 14
  flat_footed: 18
  components:
    dex: 3
    dodge: 1
    natural: 8
HP:
  HP: 103
  long: 9d10+54
saves:
  fort: 9
  ref: 9
  will: 9
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- death effects
- electricity
- paralysis
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 19
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +15 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 15
    - text: bite +15 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 15
  special:
  - consume life
  - death-stealing gaze
  - sneak attack +2d6
spell_like_abilities:
  entries:
  - name: deeper darkness
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 19
  - name: enervation
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 16
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: mass hold person
    source: default
    freq: 1/day
    DC: 21
  - name: regenerate
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: nabasu
      amount: 1
      chance: 30%
    - name: babaus
      amount: 1d4
      chance: 30%
  sources:
  - name: default
    CL: 8
ability_scores:
  STR: 22
  DEX: 17
  CON: 22
  INT: 15
  WIS: 16
  CHA: 19
BAB: 9
CMB: 15
CMD: 29
feats:
- name: Cleave
- name: Combat Expertise
- name: Dodge
- name: Improved Initiative
- name: Power Attack
skills:
  Acrobatics: 15
  Fly: 15
  Knowledge (arcana): 14
  Knowledge (planes): 14
  Perception: 23
  Sense Motive: 15
  Stealth: 15
    in shadowy conditions: 23
  Survival: 15
  _racial_mods:
    Perception:
      _: 8
    Stealth:
      in shadowy areas: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary
  treasure_type: standard
special_abilities:
  Consume Life (Su): When a nabasu creates a ghoul with its gaze attack, it gains
    a growth point. It gains a bonus equal to its growth point total on attack rolls,
    CMB rolls, saving throws, caster level checks, and skill checks. Its maximum hit
    points increase by 10 for each growth point, and its caster level for spell-like
    abilities increases by 1. For every 2 growth points, its natural armor bonus,
    SR, and CR increase by 1. Every time it gains a growth point it makes a DC 30
    caster level check-success indicates it matures (gaining both the advanced and
    the giant simple templates) and plane shifts to the Abyss in a burst of smoke.
    A nabasu can have a maximum of 20 growth points-it automatically matures if it
    has not done so already when it reaches 20 growth points.
  Death-Stealing Gaze (Su): As a free action once per day per growth point (minimum
    of 1/day), a nabasu can activate its death-stealing gaze for a full round. All
    living creatures within 30 feet must succeed on a DC 18 Fortitude save or gain
    a negative level. A humanoid slain in this manner immediately transforms into
    a ghoul under the nabasu's control. A nabasu's gaze can only create one ghoul
    per round-if multiple humans perish from the gaze in a round, the nabasu picks
    which human becomes a ghoul. The save DC is Charisma-based.
desc_long: Nabasus are birthed directly into the Material Plane from the Abyss, where
  they feed on innocent souls to mature. Only when finally sated can a nabasu return
  to the Abyss. Rumor holds that even then the nabasu's lifecycle does not change,
  and that further developments await them as they continue to grow. These vile demons
  form from the souls of evil gluttons, particularly from cannibals, blood-drinkers,
  and those who prefer the tang of undead flesh.

---

# Demon, Nabasu
This lanky fiend’s mouth is filled with sharp fangs, while great bat-like wings stretch from its scaly hide.
**Source** Pathfinder RPG Bestiary pg. 64
**XP** 4,800
CE Medium outsider (chaotic, demon, evil, native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +23

##### Defense

**AC** 22, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural)
**hp** 103 (9d10+54)
**Fort** +9, **Ref** +9, **Will** +9
**DR** 10/cold iron or good; **Immune** death effects, electricity, _[[universal monster rules/Paralysis|paralysis]]_, poison; **Resist** acid 10, cold 10, fire 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** 2 claws +15 (1d6+6), bite +15 (1d8+6)
**Special Attacks** consume life, death-stealing _[[universal monster rules/Gaze|gaze]]_, sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th)
At will—_[[spells/Deeper Darkness|deeper darkness]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 19)
3/day—_[[spells/Enervation|enervation]]_, _[[spells/Silence|silence]]_ (DC 16), _[[spells/Vampiric Touch|vampiric touch]]_
1/day—mass _[[spells/Hold Person|hold person]]_ (DC 21), _[[spells/Regenerate|regenerate]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 nabasu 30% or 1d4 babaus 30%)

##### Statistics
**Str** 22, **Dex** 17, **Con** 22, **Int** 15, **Wis** 16, **Cha** 19
**Base Atk** +9; **CMB** +15; **CMD** 29
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +15, Fly +15, Knowledge (arcana) +14, Knowledge (planes) +14, Perception +23, Sense Motive +15, Stealth +15 (+23 in shadowy conditions), Survival +15; **Racial Modifiers** +8 Perception, +8 Stealth in shadowy areas
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Consume Life (Su)** When a nabasu creates a _[[monsters/Ghoul|ghoul]]_ with its _gaze_ attack, it gains a growth point. It gains a bonus equal to its growth point total on attack rolls, CMB rolls, saving throws, caster level checks, and skill checks. Its maximum hit points increase by 10 for each growth point, and its caster level for _spell-like abilities_ increases by 1. For every 2 growth points, its natural armor bonus, SR, and CR increase by 1. Every time it gains a growth point it makes a DC 30 caster level check—success indicates it matures (gaining both the advanced and the giant simple templates) and plane shifts to the Abyss in a burst of smoke. A nabasu can have a maximum of 20 growth points—it automatically matures if it has not done so already when it reaches 20 growth points.

**Death-Stealing _Gaze_ (Su)** As a free action once per day per growth point (minimum of 1/day), a nabasu can activate its death-stealing _gaze_ for a full round. All living creatures within 30 feet must succeed on a DC 18 Fortitude save or gain a negative level. A humanoid slain in this manner immediately transforms into a _ghoul_ under the nabasu’s control. A nabasu’s _gaze_ can only create one _ghoul_ per round—if multiple humans perish from the _gaze_ in a round, the nabasu picks which human becomes a _ghoul_. The save DC is Charisma-based.

##### Description

Nabasus are birthed directly into the Material Plane from the Abyss, where they feed on innocent souls to mature. Only when finally sated can a nabasu return to the Abyss. Rumor holds that even then the nabasu’s lifecycle does not change, and that further developments await them as they continue to grow. These vile demons form from the souls of evil gluttons, particularly from cannibals, blood-drinkers, and those who prefer the tang of undead flesh.