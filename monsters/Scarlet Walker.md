---
cssclass: [monsters]
title1: Scarlet Walker
desc_short: 'This crimson horror walks upon six long, thin legs. Its face is neither
  that of a skull nor spider, but some horrid mix of the two. '
title2: Scarlet Walker
CR: 12
sources:
- name: Rise of the Runelords Anniversary Edition
  page: 414
  link: http://paizo.com/products/btpy8tc0?Pathfinder-Adventure-Path-Rise-of-the-Runelords-Anniversary-Edition
XP: 19200
alignment: LE
size: Huge
type: outsider
subtypes:
- evil
- extraplanar
- lawful
initiative:
  bonus: 9
senses:
  bloodsense: true
  darkvision: 60
  detect thoughts: true
AC:
  AC: 28
  touch: 18
  flat_footed: 18
  components:
    dex: 9
    dodge: 1
    natural: 10
    size: -2
HP:
  HP: 168
  long: 16d10+80
  fast_healing: 10
saves:
  fort: 10
  ref: 19
  will: 15
defensive_abilities:
- evasion
immunities:
- acid
- cold
- poison
SR: 23
weaknesses:
- vulnerable to electricity
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: 2 claws +23 (2d6+7/19-20 plus bleed)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
        - effect: bleed
      count: 2
      attack: claws
      bonus:
      - 23
    - text: tentacles +18 (4d6+3 plus bleed and paralysis)
      entries:
      - - damage: 4d6+3
        - effect: bleed
        - effect: paralysis
      attack: tentacles
      bonus:
      - 18
  special:
  - bleed (1d6)
  - blood-draining gaze
  - paralysis (1d4 rounds, DC 23)
space: 15
reach: 30
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: Constant
  - name: sending
    source: default
    freq: At will
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: demand
    source: default
    freq: 3/day
    DC: 23
  - name: quickened lesser confusion
    source: default
    freq: 3/day
    DC: 16
  - name: feeblemind
    source: default
    freq: 1/day
    DC: 20
  - name: insanity
    source: default
    freq: 1/day
    DC: 22
  - name: true seeing
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 17
ability_scores:
  STR: 24
  DEX: 29
  CON: 21
  INT: 14
  WIS: 20
  CHA: 21
BAB: 16
CMB: 25
CMD: 45
CMD_other: 53 vs. trip
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (claws)
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (lesser confusion)
- name: Spring Attack
- name: Weapon Finesse
skills:
  Acrobatics: 28
    when jumping: 32
  Climb: 15
  Intimidate: 24
  Knowledge (arcana): 21
  Knowledge (nature): 21
  Knowledge (planes): 21
  Perception: 24
  Sense Motive: 24
  Stealth: 20
languages:
- Aklo
- Infernal
- telepathy 300 ft.
special_qualities:
- compression
- no breath
ecology:
  environment: any
  organization: solitary, pair, or crowd (3-8)
  treasure_type: standard
special_abilities:
  Blood-Draining Gaze (Su): All creatures within 20 feet of a scarlet walker are subject
    to the monster's eerie blood-draining gaze. Affected creatures must succeed at
    a DC 23 Fortitude save or thin streams of blood pour from their eyes, flowing
    through the air and into the eye socket-like pits in the scarlet walker's face.
    This does not impact the victim's vision, but does deal 1 point of Constitution
    damage and sickens the victim for 1 round from the hideous pain. A creature already
    suffering from a bleed effect takes a -4 penalty on the saving throw. This is
    a bleed effect. The save DC is Constitution-based.
  Bloodsense (Su): A scarlet walker can sense living creatures with blood in their
    veins, or undead creatures that feed on blood (such as vampires). This ability
    functions like blindsight to a range of 60 feet.
desc_long: |-
  The scarlet walker is an alien entity from some other dimension, often conjured by the wizards of Thassilon to serve as a minion. Scarlet walkers were particularly favored for their adeptness at interrogating prisoners, either via torture, or via the creatures' uncanny ability to mentally compel both actions and compliance. Once an interrogation was over, the scarlet walker's master typically commanded the monster to render the victim insane or feebleminded if mere death wasn't appropriate. 

  Scarlet walkers themselves hail from the nightmare realm of Leng, where they walk amid strange, stony deserts and stride through the skies above. No mere predators, scarlet walkers build immense hives of coagulated blood and tissue in nameless mountain valleys, and the flavors of various creatures' blood is an inexhaustible topic of discussion among their kind.

---

# Scarlet Walker
This crimson horror walks upon six long, thin legs. Its face is
neither that of a skull nor spider, but some horrid mix of the two.

**Source** Rise of the Runelords Anniversary Edition pg. 414
**XP** 19,200

LE Huge outsider (evil, extraplanar, lawful)
**Init** +9; **Senses** bloodsense, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Thoughts|detect thoughts]]_;
Perception +24

##### Defense

**AC** 28, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+9 Dex, +1 dodge, +10 natural,
–2 size)
**hp** 168 (16d10+80); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +10, **Ref** +19, **Will** +15
**Defensive Abilities** evasion; **Immune** acid, cold, poison; **SR** 23
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** 2 claws +23 (2d6+7/19–20 plus _[[universal monster rules/Bleed|bleed]]_), tentacles +18
(4d6+3 plus _bleed_ and _[[universal monster rules/Paralysis|paralysis]]_)
**Space** 15 ft., **Reach** 30 ft.
**Special Attacks** _bleed_ (1d6), blood-draining _[[universal monster rules/Gaze|gaze]]_, _paralysis_
(1d4 rounds, DC 23)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
Constant—_[[spells/Air Walk|air walk]]_, _detect thoughts_
At will—_[[spells/Sending|sending]]_
3/day—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Demand|demand]]_ (DC 23),
quickened lesser _confusion_ (DC 16)
1/day—_[[spells/Feeblemind|feeblemind]]_ (DC 20),
_[[spells/Insanity|insanity]]_ (DC 22), _[[spells/True Seeing|true seeing]]_

##### Statistics
**Str** 24, **Dex** 29, **Con** 21, **Int** 14, **Wis** 20, **Cha** 21
**Base Atk** +16; **CMB** +25; **CMD** 45 (53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (lesser
_confusion_), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +28 (+32 when jumping), _Climb_ +15, Intimidate +24,
Knowledge (arcana) +21, Knowledge (nature) +21, Knowledge
(planes) +21, Perception +24, Sense Motive +24, Stealth +20
**Languages** Aklo, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or crowd (3–8)
**Treasure** standard

### Special Abilities

**Blood-Draining _Gaze_ (Su)** All creatures within 20 feet of a scarlet
walker are subject to the monster’s eerie blood-draining _gaze_.
Affected creatures must succeed at a DC 23 Fortitude save or
thin streams of blood pour from their eyes, flowing through the
air and into the eye socket-like pits in the _[[monsters/Scarlet Walker|scarlet walker]]_’s face.
This does not _[[items/Weapon Magic Abilities/Impact|impact]]_ the victim’s _[[spells/Vision|vision]]_, but does deal 1 point
of Constitution damage and sickens the victim for 1 round from
the hideous pain. A creature already suffering from a _bleed_
effect takes a –4 penalty on the saving throw. This is a _bleed_
effect. The save DC is Constitution-based.

**Bloodsense (Su)** A _scarlet walker_ can sense living creatures
with blood in their veins, or undead creatures that feed on
blood (such as vampires). This ability functions like _[[universal monster rules/Blindsight|blindsight]]_
to a range of 60 feet.

##### Description

The _scarlet walker_ is an alien entity
from some other dimension,
often conjured by the wizards
of Thassilon to serve as
a minion. Scarlet walkers
were particularly favored for
their adeptness at interrogating
prisoners, either via torture, or via the
creatures’ uncanny ability to mentally
compel both actions and compliance. Once
an _[[spells/Interrogation|interrogation]]_ was over, the _scarlet walker_’s
master typically commanded the monster to
render the victim insane or feebleminded if mere
death wasn’t appropriate.

Scarlet walkers themselves
hail from the _[[spells/Nightmare|nightmare]]_
realm of Leng, where they
walk amid strange, stony
deserts and stride through the
skies above. No mere predators,
scarlet walkers build immense hives of
coagulated blood and tissue in nameless
mountain valleys, and the flavors of various creatures’
blood is an inexhaustible topic of discussion among
their kind.