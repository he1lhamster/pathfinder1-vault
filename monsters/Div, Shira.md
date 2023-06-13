---
cssclass: [monsters]
title1: Div, Shira
desc_short: Moving with deadly grace, this brutal, thickly furred humanoid figure's
  head is that of a lioness with dead black eyes.
title2: Shira
CR: 12
sources:
- name: Bestiary 3
  page: 90
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: "Pathfinder #21: The Jackal's Price"
  page: 78
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy87uv
XP: 19200
alignment: NE
size: Large
type: outsider
subtypes:
- div
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
AC:
  AC: 27
  touch: 16
  flat_footed: 20
  components:
    dex: 7
    natural: 11
    size: -1
HP:
  HP: 150
  long: 12d10+84
saves:
  fort: 11
  ref: 15
  will: 14
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- fire
- poison
resistances:
  acid: 10
  electricity: 10
SR: 23
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +21 (1d8+9/19-20)
      entries:
      - - damage: 1d8+9
          crit_range: 19-20
      attack: bite
      bonus:
      - 21
    - text: 2 claws +21 (1d8+9 plus grab)
      entries:
      - - damage: 1d8+9
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 21
  special:
  - consume essence
  - dusty pelt
  - rake (2 claws +21, 1d8+9)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: magic circle against good
    source: default
    freq: 3/day
  - name: waves of fatigue
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: pairakas
      amount: 1d2
    - name: shira
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 13
    concentration: 18
ability_scores:
  STR: 28
  DEX: 25
  CON: 25
  INT: 13
  WIS: 22
  CHA: 20
BAB: 12
CMB: 22
CMB_other: +26 grapple
CMD: 39
feats:
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Power Attack
- name: Run
- name: Weapon Focus (claw)
- name: Weapon Focus (bite)
skills:
  Acrobatics: 22
    when jumping: 30
  Bluff: 20
  Climb: 24
  Intimidate: 20
  Perception: 21
  Stealth: 18
  Survival: 21
languages:
- Abyssal
- Celestial
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: standard
special_abilities:
  Consume Essence (Su): A shira's deadliest attacks drain away a portion of its victim's
    essence. Whenever a shira hits with a coup de grace attack using its bite, or
    confirms a critical hit with its claws or bite, the target must succeed at a DC
    23 Fortitude save or take 1d4 points of Constitution drain. The save is Constitution-based.
  Dusty Pelt (Ex): A shira collects and produces copious amounts of dust and ash within
    the coarse hairs of its furry hide. As a move action, it can shake itself, creating
    a cloud of dust that fills its space, providing it concealment. Any attack that
    deals at least 10 points of bludgeoning, piercing, or slashing damage to the shira
    (before DR) automatically activates this ability. The dust cloud lasts for 1 round.
    A light wind disperses this cloud immediately.
desc_long: |-
  Bestial stalkers, shiras live to hunt and feed. Resembling anthropomorphic lionesses, these divs use their powerful builds, keen senses, and deadly instincts to track the proudest mortals and slay the most formidable foes. They embody the deadly nature of the wilds and the dispassion with which beast and land might turn against mortals, delighting in proving to civilized beings how small and helpless they are in the face of a savage world.

  Shiras prefer hunting alone, keeping company with even others of their own kind only long enough to form temporary hunting bands. With a hunger for intelligent prey, they savor the taste of mortal souls, savaging not just victims' bodies but also their vital essences. Despite being the most feral of all divs, shiras sometimes serve as scouts and assassins for div hordes. Such arrangements usually prove to be temporary, however, lasting only until the shiras' savage instincts or lust for the hunt again takes hold.

  Shiras never go after an easy kill, and instead target the most obviously powerful of the possible targets. When acting on this compulsion, a shira weighs its chances for survival and the glory of its intended kill, planning its tactics carefully and not necessarily charging savagely forth. Though savage, a shira is also a cunning hunter and might wait weeks for the perfect opportunity to bring down its chosen prey.

  Most shiras stand 10 feet tall and weigh approximately 1,200 pounds.

---

# Div, Shira
Moving with _[[items/Weapon Magic Abilities/Deadly|deadly]]_ _[[spells/Grace|grace]]_, this brutal, thickly furred humanoid figure’s head is that of a lioness with dead black eyes.
**Source** Bestiary 3 pg. 90, Pathfinder #21: The _[[monsters/Jackal|Jackal]]_'s Price pg. 78
**XP** 19,200

NE Large outsider (div, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +21

##### Defense

**AC** 27, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 Dex, +11 natural, –1 size)
**hp** 150 (12d10+84)
**Fort** +11, **Ref** +15, **Will** +14
**DR** 10/cold iron and good; **Immune** fire, poison; **Resist** acid 10, electricity 10; **SR** 23

##### Offense
**Speed** 50 ft.
**Melee** bite +21 (1d8+9/19–20), 2 claws +21 (1d8+9 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[feats/Consume Essence|consume essence]]_, dusty pelt, _[[universal monster rules/Rake|rake]]_ (2 claws +21, 1d8+9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +18)
Constant—_true seeing_
At will—greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1d2 pairakas or 1 shira 35%)

##### Statistics
**Str** 28, **Dex** 25, **Con** 25, **Int** 13, **Wis** 22, **Cha** 20
**Base Atk** +12; **CMB** +22 (+26 grapple); **CMD** 39
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, Run, _[[feats/Weapon Focus|Weapon Focus]]_ (claw), _Weapon Focus_ (bite)
**Skills** Acrobatics +22 (+30 when jumping), Bluff +20, _[[universal monster rules/Climb|Climb]]_ +24, Intimidate +20, Perception +21, Stealth +18, Survival +21
**Languages** Abyssal, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Consume Essence_ (Su)** A shira’s deadliest attacks drain away a portion of its victim’s essence. Whenever a shira hits with a coup de _grace_ attack using its bite, or confirms a critical hit with its claws or bite, the target must succeed at a DC 23 Fortitude save or take 1d4 points of Constitution drain. The save is Constitution-based.

**Dusty Pelt (Ex)** A shira collects and produces copious amounts of dust and ash within the coarse hairs of its furry hide. As a move action, it can shake itself, creating a cloud of dust that fills its space, providing it concealment. Any attack that deals at least 10 points of bludgeoning, piercing, or slashing damage to the shira (before DR) automatically activates this ability. The dust cloud lasts for 1 round. A light wind disperses this cloud immediately.

##### Description

Bestial stalkers, shiras live to hunt and feed. Resembling anthropomorphic lionesses, these divs use their powerful builds, _[[spells/Keen Senses|keen senses]]_, and _deadly_ instincts to track the proudest mortals and slay the most formidable foes. They embody the _deadly_ nature of the wilds and the dispassion with which beast and land might turn against mortals, delighting in proving to civilized beings how small and _[[conditions/Helpless|helpless]]_ they are in the face of a savage world.

Shiras prefer hunting alone, keeping company with even others of their own kind only long enough to form temporary hunting bands. With a hunger for intelligent prey, they savor the taste of mortal souls, savaging not just victims’ bodies but also their vital essences. Despite being the most feral of all divs, shiras sometimes serve as scouts and assassins for div hordes. Such arrangements usually prove to be temporary, however, lasting only until the shiras’ savage instincts or lust for the hunt again takes hold.

Shiras never go after an easy kill, and instead target the most obviously powerful of the possible targets. When acting on this compulsion, a shira weighs its chances for survival and the glory of its intended kill, planning its tactics carefully and not necessarily charging savagely forth. Though savage, a shira is also a _[[items/Weapon Magic Abilities/Cunning|cunning]]_ _[[classes/Hunter|hunter]]_ and might wait weeks for the perfect opportunity to bring down its chosen prey.

Most shiras stand 10 feet tall and weigh approximately 1,200 pounds.