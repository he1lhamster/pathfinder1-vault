---
cssclass: [monsters]
title1: Tikbalang
desc_short: Merging the features of a horse and human, this monstrosity has an equine
  snout, sharp fangs, and long forelimbs with clawed fingers.
title2: Tikbalang
CR: 9
sources:
- name: Bestiary 4
  page: 260
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 6400
alignment: CE
size: Large
type: monstrous humanoid
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 22
  touch: 13
  flat_footed: 18
  components:
    dex: 3
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 10
  ref: 11
  will: 11
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +18 (2d4+7/19-20)
      entries:
      - - damage: 2d4+7
          crit_range: 19-20
      attack: bite
      bonus:
      - 18
    - text: 2 hooves +13 (1d8+10)
      entries:
      - - damage: 1d8+10
      count: 2
      attack: hooves
      bonus:
      - 13
  ranged:
  - - text: 4 spines +14 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 4
      attack: spines
      bonus:
      - 14
  special:
  - pounce
  - spines
  - trample (1d8+10, DC 23)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: spider climb
    source: default
    freq: Constant
  - name: ventriloquism
    source: default
    freq: At will
    DC: 15
  - name: invisibility
    source: default
    freq: At will
  - name: major image
    source: default
    freq: 3/day
    DC: 17
  - name: fly
    source: default
    freq: 1/day
    other: self only
  - name: mirage arcana
    source: default
    freq: 1/day
    DC: 19
  - name: maze
    source: default
    freq: 1/week
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 24
  DEX: 16
  CON: 19
  INT: 11
  WIS: 16
  CHA: 19
BAB: 12
CMB: 20
CMD: 34
feats:
- name: Combat Reflexes
- name: Deceitful
- name: Dodge
- name: Great Fortitude
- name: Improved Critical (bite)
- name: Power Attack
skills:
  Bluff: 20
  Disguise: 6
  Perception: 18
  Sense Motive: 9
  Stealth: 14
  Survival: 12
languages:
- Common
- Sylvan
special_qualities:
- change shape (Small or Medium humanoid, alter self)
- powerful blows (hooves)
- sound mimicry (sounds and voices)
ecology:
  environment: warm jungles or forests
  organization: solitary, pair, or gang (3-5)
  treasure_type: standard
special_abilities:
  Spines (Ex): As a standard action, a tikbalang can launch four spines from its mane,
    each dealing 1d6 points of damage plus its Strength bonus. This attack has a range
    of 120 feet with no range increment. All targets must be within 30 feet of each
    other. A tikbalang can launch only 24 spines in any 24-hour period.
desc_long: |-
  Dangerous protectors of deep forests and lush jungles, tikbalangs are malicious creatures that enjoy leading travelers astray. Tikbalangs mimic sounds to lure explorers off their determined path, even separating a single traveler from his group and kidnapping him. They use their magical abilities to make the forest confusing to those passing through, often weaving illusions around a path to hide important turns or cloaking the entire jungle in an unfamiliar appearance.

  Sometimes a tikbalang stalks intruders, spying on them from afar or from within the canopies of trees to learn more about its visitors. It then uses its change shape ability to appear as someone familiar to its first victim (such as another member of the group) and leads that person deeper into the woods to become lost. Once the victim is out of hearing range, the tikbalang drags it into a high tree, wraps it in vines, and packs its mouth with leaves and moss to stif le its screams. The tikbalang may eat its prisoner, offer to release it if the other intruders leave, or leave its corpse as a grisly warning to other travelers.

  Though sinister and always looking to bring ruin to explorers, tikbalangs can be bribed or mollified into allowing safe passage with offerings or the performance of strange rituals, such as singing a song, wearing a shirt inside out, or giving the monster bread and honey. The exact bribe is different each day, and the tikbalang never explains what it wants.

---

# Tikbalang
_[[items/Armor Magic Abilities/Merging|Merging]]_ the features of a _[[monsters/Horse|horse]]_ and human, this monstrosity has an equine snout, sharp fangs, and long forelimbs with clawed fingers.
**Source** Bestiary 4 pg. 260
**XP** 6,400
CE Large monstrous humanoid
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +18

##### Defense

**AC** 22, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +1 dodge, +9 natural, –1 size)
**hp** 114 (12d10+48)
**Fort** +10, **Ref** +11, **Will** +11

##### Offense
**Speed** 40 ft.
**Melee** bite +18 (2d4+7/19–20), 2 hooves +13 (1d8+10)
**Ranged** 4 spines +14 (1d6+8)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, spines, _[[universal monster rules/Trample|trample]]_ (1d8+10, DC 23)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_[[spells/Spider Climb|spider climb]]_
At will—_[[spells/Ventriloquism|ventriloquism]]_ (DC 15), _[[spells/Invisibility|invisibility]]_
3/day—_[[spells/Major Image|major image]]_ (DC 17)
1/day—fly (self only), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 19)
1/week—_[[spells/Maze|maze]]_

##### Statistics
**Str** 24, **Dex** 16, **Con** 19, **Int** 11, **Wis** 16, **Cha** 19
**Base Atk** +12; **CMB** +20; **CMD** 34
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +20, Disguise +6, Perception +18, Sense Motive +9, Stealth +14, Survival +12
**Languages** Common, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or _[[classes/Medium|Medium]]_ humanoid, _[[spells/Alter Self|alter self]]_), powerful blows (hooves), _[[universal monster rules/Sound Mimicry|sound mimicry]]_ (sounds and voices)

##### Ecology

**Environment** warm jungles or forests
**Organization** solitary, pair, or gang (3–5)
**Treasure** standard

### Special Abilities
**Spines (Ex)** As a standard action, a _[[monsters/Tikbalang|tikbalang]]_ can launch four spines from its mane, each dealing 1d6 points of damage plus its Strength bonus. This attack has a range of 120 feet with no range increment. All targets must be within 30 feet of each other. A _tikbalang_ can launch only 24 spines in any 24-hour period.

##### Description

Dangerous protectors of deep forests and lush jungles, tikbalangs are malicious creatures that enjoy leading travelers astray. Tikbalangs _[[monsters/Mimic|mimic]]_ sounds to lure explorers off their determined path, even separating a single traveler from his group and kidnapping him. They use their magical abilities to make the forest confusing to those passing through, often weaving illusions around a path to hide important turns or cloaking the entire jungle in an unfamiliar appearance.

Sometimes a _tikbalang_ stalks intruders, spying on them from afar or from within the canopies of trees to learn more about its visitors. It then uses its _change shape_ ability to appear as someone familiar to its first victim (such as another member of the group) and leads that person deeper into the woods to become lost. Once the victim is out of hearing range, the _tikbalang_ drags it into a high tree, wraps it in vines, and packs its mouth with leaves and moss to stif le its screams. The _tikbalang_ may eat its prisoner, offer to release it if the other intruders leave, or leave its corpse as a grisly warning to other travelers.

Though sinister and always looking to bring ruin to explorers, tikbalangs can be bribed or mollified into allowing safe passage with offerings or the performance of strange rituals, such as _[[items/Armor Magic Abilities/Singing|singing]]_ a song, wearing a shirt inside out, or giving the monster bread and honey. The exact bribe is different each day, and the _tikbalang_ never explains what it wants.