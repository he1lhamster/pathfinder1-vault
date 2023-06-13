---
cssclass: [monsters]
title1: Heart Thief
desc_short: Dozens of antlers crown this slender biped's masked head. Its wicked claws
  clutch a bloodstained sack.
title2: Heart Thief
CR: 9
sources:
- name: Seers of the Drowned City
  page: 57
  link: http://paizo.com/products/btpy9op2?Pathfinder-Module-Seers-of-the-Drowned-City
XP: 6400
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- evil
- native
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 12
  flat_footed: 21
  components:
    dex: 3
    natural: 12
    size: -1
HP:
  HP: 115
  long: 12d10+48
saves:
  fort: 12
  ref: 7
  will: 12
DR:
- amount: 10
  weakness: silver
immunities:
- disease
- fire
- poison
- fear
resistances:
  acid: 10
  cold: 10
SR: 20
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: 2 claws +17 (1d8+6/19-20 plus grab)
      entries:
      - - damage: 1d8+6
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 17
    - text: gore +17 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: gore
      bonus:
      - 17
  special:
  - disemboweling critical
  - harvest heart
  - rend (2 claws, 2d6+6)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: atavism
    source: default
    freq: At will
    DC: 19
  - name: dominate animal
    source: default
    freq: At will
    DC: 18
  - name: transport via plants
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: air walk
    source: default
    freq: 3/day
  - name: snare
    source: default
    freq: 3/day
  - name: spike stones
    source: default
    freq: 3/day
    DC: 19
  - name: summon nature's ally VII
    source: default
    freq: 3/day
    other: animals only
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: baykok
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 9
    concentration: 14
ability_scores:
  STR: 23
  DEX: 16
  CON: 19
  INT: 17
  WIS: 18
  CHA: 20
BAB: 12
CMB: 19
CMD: 32
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 20
  Climb: 14
  Craft (trap): 18
  Handle Animal: 20
  Knowledge (nature): 18
  Perception: 19
  Sense Motive: 19
  Spellcraft: 18
  Stealth: 14
  Survival: 19
languages:
- Abyssal
- Aklo
- Common
- Druidic
- Sylvan
- speak with animals
ecology:
  environment: any forest
  organization: solitary, pair, or hunt (3-5)
  treasure_type: standard
special_abilities:
  Disemboweling Critical (Ex): When a heart thief confirms a critical hit with a claw,
    the target must succeed at a DC 22 Fortitude save or take 1d4 points of Constitution
    damage as its organs are savaged (this ability damage counts as precision damage).
    The save DC is Strength-based.
  Harvest Heart (Ex): Once a heart thief has pinned a Medium or smaller living creature,
    it can attempt to rip the creature's still-beating heart from its chest. This
    attempt is made as part of the grapple check to maintain an existing pin, and
    if successful, it deals 4d6+12 points of damage to the target and affects the
    target with the heart thief's disemboweling critical. If this damage kills the
    creature, as a free action, the heart thief harvests the extracted heart and places
    it in the bloodstained sack it carries, gaining the benefit of a heal spell (CL
    9th) in the process. The save DC is Strength-based.
desc_long: |-
  Originally created by Curchanus as both shepherds and stewards for his many animals, these creatures were corrupted by Lamashtu when she slew their god. Their true name and purpose abandoned, they have existed from that point on as heart thieves, tormenters of the deep forest who enjoy slaughtering any who dare wander their woods.

   A heart thief follows its prey from afar, harassing its targets for days or even weeks at a time. Only once its quarry is exhausted from unprovoked animal attacks and waylaid by snares and traps will a heart thief make itself known, attacking with a company of feral beasts. Lone hunters slain by a heart thief often rise as baykoks after enduring painful torments.

   Those who manage to flee are fortunate indeed, for those who remain are subjected to the heart thief 's curious and horrific practice of harvesting organs from sentient creatures. What heart thieves do with these macabre collections remains a mystery, but it's agreed that they are not used for consumption, for the most prolific heart thieves carry multiple sacks, each stuffed to bursting with rotting hearts.

---

# Heart Thief
Dozens of antlers crown this slender biped’s masked head. Its wicked claws clutch a bloodstained _[[items/Mundane/Sack|sack]]_.
**Source** Seers of the Drowned City pg. 57
**XP** 6,400
CE Large outsider (chaotic, evil, native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19

##### Defense

**AC** 24, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+3 Dex, +12 natural, –1 size)
**hp** 115 (12d10+48)
**Fort** +12, **Ref** +7, **Will** +12
**DR** 10/silver; **Immune** disease, fire, poison, _[[universal monster rules/Fear|fear]]_; **Resist** acid 10, cold 10; **SR** 20

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** 2 claws +17 (1d8+6/19–20 plus _[[universal monster rules/Grab|grab]]_), gore +17 (2d6+6)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** disemboweling critical, harvest heart, _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +14)
Constant—_[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_ 
At will—_[[spells/Atavism|atavism]]_ (DC 19), _[[spells/Dominate Animal|dominate animal]]_ (DC 18), _[[spells/Transport via Plants|transport via plants]]_ (self plus 50 lbs. of objects only) 
3/day—_[[spells/Air Walk|air walk]]_, _[[spells/Snare|snare]]_, _[[spells/Spike Stones|spike stones]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ nature’s ally VII (animals only) 
1/day—_summon_ (level 3, 1 _[[monsters/Baykok|baykok]]_ 35%)

##### Statistics
**Str** 23, **Dex** 16, **Con** 19, **Int** 17, **Wis** 18, **Cha** 20
**Base Atk** +12; **CMB** +19; **CMD** 32
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +20, _Climb_ +14, Craft (trap) +18, Handle Animal +20, Knowledge (nature) +18, Perception +19, Sense Motive +19, Spellcraft +18, Stealth +14, Survival +19
**Languages** Abyssal, Aklo, Common, Druidic, Sylvan; _speak with animals_

##### Ecology

**Environment** any forest
**Organization** solitary, pair, or hunt (3-5)
**Treasure** standard

### Special Abilities

**Disemboweling Critical (Ex)** When a _[[monsters/Heart Thief|heart thief]]_ confirms a critical hit with a claw, the target must succeed at a DC 22 Fortitude save or take 1d4 points of Constitution damage as its organs are savaged (this ability damage counts as precision damage). The save DC is Strength-based.

**Harvest Heart (Ex)** Once a _heart thief_ has _[[conditions/Pinned|pinned]]_ a Medium or smaller living creature, it can attempt to rip the creature’s still-beating heart from its chest. This attempt is made as part of the grapple check to maintain an existing pin, and if successful, it deals 4d6+12 points of damage to the target and affects the target with the _heart thief_’s disemboweling critical. If this damage kills the creature, as a free action, the _heart thief_ harvests the extracted heart and places it in the bloodstained _sack_ it carries, gaining the benefit of a _[[spells/Heal|heal]]_ spell (CL 9th) in the process. The save DC is Strength-based.

##### Description

Originally created by Curchanus as both shepherds and stewards for his many animals, these creatures were corrupted by Lamashtu when she slew their god. Their _[[feats/True Name|true name]]_ and purpose abandoned, they have existed from that point on as heart thieves, tormenters of the deep forest who enjoy slaughtering any who dare wander their woods.

A _heart thief_ follows its prey from afar, harassing its targets for days or even weeks at a time. Only once its quarry is _[[conditions/Exhausted|exhausted]]_ from unprovoked animal attacks and waylaid by snares and traps will a _heart thief_ make itself known, attacking with a company of feral beasts. Lone hunters slain by a _heart thief_ often rise as baykoks after enduring painful torments.

Those who manage to flee are fortunate indeed, for those who remain are subjected to the _heart thief_ ’s curious and horrific practice of _[[items/Weapon Magic Abilities/Harvesting|harvesting]]_ organs from sentient creatures. What heart thieves do with these macabre collections remains a mystery, but it’s agreed that they are not used for _[[feats/Consumption|consumption]]_, for the most prolific heart thieves carry multiple sacks, each stuffed to bursting with rotting hearts.