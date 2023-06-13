---
cssclass: [monsters]
title1: Sahkil, Zohanil
desc_short: This monster is vaguely humanoid, but stands on three legs. Afoul liquid
  drips from the needlelike tips of its long, hooked arms.
title2: Zohanil
CR: 10
sources:
- name: Bestiary 6
  page: 246
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9600
alignment: NE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- sahkil
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  low-light vision: true
  see invisibility: true
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    dex: 4
    dodge: 1
    natural: 10
HP:
  HP: 138
  long: 12d10+72
saves:
  fort: 14
  ref: 8
  will: 14
DR:
- amount: 10
  weakness: good
immunities:
- death effects
- disease
- fear effects,poison
resistances:
  cold: 10
  electricity: 10
  sonic: 10
SR: 21
speeds:
  base: 50
  climb: 50
attacks:
  melee:
  - - text: bite +19 (1d10+7)
      entries:
      - - damage: 1d10+7
      attack: bite
      bonus:
      - 19
    - text: 2 talons +19 (2d6+7/19-20plus addiction)
      entries:
      - - damage: 2d6+7
          type: /19-20plus addiction
      count: 2
      attack: talons
      bonus:
      - 19
  special:
  - look of fear (30 ft., DC 22)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: foe to friend
    source: default
    freq: 3/day
    DC: 19
  - name: greater invisibility
    source: default
    freq: 3/day
  - name: overwhelming grief
    source: default
    freq: 3/day
    DC: 20
  - name: protection from good
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 17
  - name: nightmare
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 25
  DEX: 18
  CON: 22
  INT: 15
  WIS: 18
  CHA: 19
BAB: 12
CMB: 19
CMD: 34
CMD_other: 36 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: ImprovedCritical (talon)
- name: Improved Initiative
- name: Iron Will
skills:
  Acrobatics: 19
  Climb: 30
  Craft (alchemy): 17
  Intimidate: 19
  Knowledge (arcana): 11
  Knowledge (planes): 11
  Perception: 19
  Sense Motive: 19
  Stealth: 19
languages:
- Abyssal
- Celestial
- Infernal
- telepathy 100 ft.
special_qualities:
- easy to call
- emotional focus
- skip between,spirit touch
ecology:
  environment: any (Ethereal Plane)
  organization: solitary, pair, or gang (3-12)
  treasure_type: standard
special_abilities:
  Addiction (Ex): When a zohanil damages a creature with its talons, it injects the
    target with a severely addictive fluid that blurs vision and deadens reflexes.
    A creature can resist the effects of this injected toxin with a successful DC
    22 Fortitude save. On a failed save, the victim takes a -2 penalty to all Wisdom-
    and Dexterity-based checks for 1 hour. After this hour passes, the penalty fades
    but the victim suffers the effects of withdrawal, taking a -2 penalty to Strength,
    Dexterity, Constitution, and Wisdom. These ability score penalties are negated
    on any round the victim takes the Wisdom- and Dexterity-based check penalty from
    further addiction attacks from the zohanil, but are otherwise permanent (as per
    a severe addiction; see page 236 of the Pathfinder RPG GameMastery Guide for details).
    This is a disease effect. The save DC is Constitution-based.
  Look of Fear (Su): A creature affected by a zohanil's gaze is panicked for 1 round
    and shaken for 1d4 rounds thereafter. A creature that successfully saves is instead
    shaken for 1 round.
desc_long: Zohanils delight in haunting those who fear needles and invasive medical
  procedures. They also enjoy sowing addiction in hopes of heightening despair. A
  zohanil stands over 6 feet tall and weighs roughly 200 pounds.

---

# Sahkil, Zohanil
This monster is vaguely humanoid, but stands on three legs. A

foul liquid drips from the needlelike tips of its long, hooked arms.
**Source** Bestiary 6 pg. 246
**XP** 9,600

NE Medium outsider (evil, extraplanar, sahkil)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_,

_[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +19

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 138 (12d10+72)
**Fort** +14, **Ref** +8, **Will** +14
**DR** 10/good; **Immune** death effects, disease, _[[universal monster rules/Fear|fear]]_ effects,

poison; **Resist** cold 10, electricity 10, sonic 10; **SR** 21

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** bite +19 (1d10+7), 2 talons +19 (2d6+7/19–20

plus addiction)
**Special Attacks** look of _fear_ (30 ft., DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_detect good_, _detect magic_, _see invisibility_ 
At will—greater teleport (self plus 50 lbs. of objects only) 
3/day—_[[spells/Foe to Friend|foe to friend]]_ (DC 19), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Overwhelming Grief|overwhelming grief]]_ (DC 20), _[[spells/Protection From Good|protection from good]]_, _[[spells/Suggestion|suggestion]]_ (DC 17) 
1/day—_[[spells/Nightmare|nightmare]]_ (DC 19)

##### Statistics
**Str** 25, **Dex** 18, **Con** 22, **Int** 15, **Wis** 18, **Cha** 19
**Base Atk** +12; **CMB** +19; **CMD** 34 (36 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, Improved

Critical (talon), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_
**Skills** Acrobatics +19, _Climb_ +30, Craft (alchemy) +17,

Intimidate +19, Knowledge (arcana, planes) +11,

Perception +19, Sense Motive +19, Stealth +19
**Languages** Abyssal, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** easy to call, emotional focus, skip between,

spirit touch

##### Ecology

**Environment** any (Ethereal Plane)
**Organization** solitary, pair, or gang (3–12)
**Treasure** standard

### Special Abilities

**Addiction (Ex)** When a zohanil damages a creature with its talons, it injects the target with a severely addictive fluid that blurs _[[spells/Vision|vision]]_ and deadens reflexes. A creature can resist the effects of this injected toxin with a successful DC 22 Fortitude save. On a failed save, the victim takes a –2 penalty to all Wisdom- and Dexterity-based checks for 1 hour. After this hour passes, the penalty fades but the victim suffers the effects of withdrawal, taking a –2 penalty to Strength, Dexterity, Constitution, and Wisdom. These ability score penalties are negated on any round the victim takes the Wisdom- and Dexterity-based check penalty from further addiction attacks from the zohanil, but are otherwise permanent (as per a severe addiction; see page 236 of the Pathfinder RPG GameMastery Guide for details). This is a disease effect. The save DC is Constitution-based.

**Look of _Fear_ (Su)** A creature affected by a zohanil’s _[[universal monster rules/Gaze|gaze]]_ is _[[conditions/Panicked|panicked]]_ for 1 round and _[[conditions/Shaken|shaken]]_ for 1d4 rounds thereafter. A creature that successfully saves is instead _shaken_ for 1 round.

##### Description

Zohanils delight in haunting those who _fear_ needles and invasive medical procedures. They also enjoy sowing addiction in hopes of heightening despair. A zohanil stands over 6 feet tall and weighs roughly 200 pounds.