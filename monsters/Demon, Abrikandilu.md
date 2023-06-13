---
cssclass: [monsters]
title1: Demon, Abrikandilu
desc_short: This deformed, horned, hunchbacked humanoid has a forked, ratlike tail
  and two thumbs on each taloned hand.
title2: Abrikandilu
CR: 3
sources:
- name: Bestiary 5
  page: 74
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: The Worldwound
  page: 42
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    natural: 5
HP:
  HP: 32
  long: 5d10+5
saves:
  fort: 5
  ref: 4
  will: 3
DR:
- amount: 5
  weakness: cold iron
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
weaknesses:
- hatred of mirrors
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +7 (1d6+2 plus mutilation)
      entries:
      - - damage: 1d6+2
        - effect: mutilation
      attack: bite
      bonus:
      - 7
    - text: 2 claws +7 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: claws
      bonus:
      - 7
  ranged:
  - - text: improvised weapon +5 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: improvised weapon
      bonus:
      - 5
  special:
  - destructive attacks
  - mutilation
spell_like_abilities:
  entries:
  - name: cause fear
    source: default
    freq: 3/day
    DC: 12
  - name: shatter
    source: default
    freq: 3/day
    DC: 13
  - name: summon
    source: default
    freq: 1/day
    level: 1
    summons:
    - name: abrikandilu
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 5
    concentration: 6
ability_scores:
  STR: 15
  DEX: 11
  CON: 12
  INT: 6
  WIS: 10
  CHA: 13
BAB: 5
CMB: 7
CMB_other: +9 sunder
CMD: 17
CMD_other: 19 vs. sunder
feats:
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- name: Throw Anything
skills:
  Appraise: 6
  Climb: 10
  Disable Device: 8
  Perception: 12
  _racial_mods:
    Perception:
      _: 4
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or gang (3-12)
  treasure_type: standard
  treasure:
  - thieves' tools
  - other treasure
  - but any art objects are broken
special_abilities:
  Destructive Attacks (Ex): An abrikandilu's natural attacks can threaten and confirm
    critical hits against objects. In addition, an abrikandilu gains a +5 racial bonus
    on Strength checks to break or destroy objects.
  Hatred of Mirrors (Ex): An abrikandilu loathes the sight of its own reflection.
    Using a mirror grants a +5 bonus on Intimidate checks against an abrikandilu.
    An abrikandilu adjacent to a mirror or attacked by a mirror-carrying creature
    (at the GM's discretion, some shields could be considered mirrors) must attempt
    a DC 15 Will save at the start of its turn. If it fails, it must focus all of
    its actions that round on attempts to destroy the mirror.
  Mutilation (Su): An abrikandilu's bite causes horrific and hideous wounds that not
    only mar beauty but supernaturally diminish a creature's sense of self-worth.
    A creature bitten by an abrikandilu must succeed at a DC 13 Fortitude save or
    gain a -1 penalty on all Charisma-based checks. This penalty stacks, up to a -5
    penalty, and it lasts even after the wounds are healed. The penalty slowly fades
    with time, diminishing by 1 every 24 hours until it reaches 0. This is a curse
    effect. The save DC is Constitution-based.
desc_long: |-
  Known as wrecker demons, abrikandilus delight in destroying beauty, be it by rending a fine painting to shreds, reducing a magnificent statue to rubble, or scarring a lovely face. Abrikandilus are formed from the souls of mortals who vandalized art or defaced objects of exquisiteness, particularly those whose acts of destruction were born from jealousy. All abrikandilus loathe only one thing more than beauty-their own reflections. Curiously, the faces of other abrikandilus do not vex a wrecker demon, but the sight of its own deformed shape drives an abrikandilu into a furious, brutish anger, impelling it to focus all of its energy on breaking the object, usually a mirror, in which it can see itself.

  Abrikandilus are often used as ground troops in demonic wars, for they are excellent grunts on the battlefield and don't require weapons or armor to excel at combat. Their penchant for demolishing works of art functions as an additional demoralizing element in battle, for even when abrikandilus are defeated, the damage they have dealt endures as a constant reminder of the value of what they destroyed.

  An abrikandilu stands 4 feet tall and weighs 200 pounds.

---

# Demon, Abrikandilu
This deformed, horned, hunchbacked humanoid has a forked, ratlike tail and two thumbs on each taloned hand.
**Source** Bestiary 5 pg. 74, The Worldwound pg. 42
**XP** 800
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 natural)
**hp** 32 (5d10+5)
**Fort** +5, **Ref** +4, **Will** +3
**DR** 5/cold iron; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10
**Weaknesses** hatred of mirrors

##### Offense
**Speed** 30 ft.
**Melee** bite +7 (1d6+2 plus mutilation), 2 claws +7 (1d4+2)
**Ranged** improvised weapon +5 (1d6+2)
**Special Attacks** destructive attacks, mutilation
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +6)
3/day—_[[spells/Cause Fear|cause fear]]_ (DC 12), _[[spells/Shatter|shatter]]_ (DC 13)
1/day—_[[universal monster rules/Summon|summon]]_ (level 1, 1 abrikandilu 50%)

##### Statistics
**Str** 15, **Dex** 11, **Con** 12, **Int** 6, **Wis** 10, **Cha** 13
**Base Atk** +5; **CMB** +7 (+9 sunder); **CMD** 17 (19 vs. sunder)
**Feats** _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Appraise +6, _[[universal monster rules/Climb|Climb]]_ +10, Disable Device +8, Perception +12; **Racial Modifiers** +4 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or gang (3-12)
**Treasure** standard (thieves’ tools, other treasure, but any art objects are _[[conditions/Broken|broken]]_)

### Special Abilities

**Destructive Attacks (Ex)** An abrikandilu’s _[[universal monster rules/Natural Attacks|natural attacks]]_ can threaten and confirm critical hits against objects. In addition, an abrikandilu gains a +5 racial bonus on Strength checks to break or destroy objects.

**Hatred of Mirrors (Ex)** An abrikandilu loathes the sight of its own reflection. Using a _[[items/Mundane/Mirror|mirror]]_ grants a +5 bonus on Intimidate checks against an abrikandilu. An abrikandilu adjacent to a _mirror_ or attacked by a mirror-carrying creature (at the GM’s discretion, some shields could be considered mirrors) must attempt a DC 15 Will save at the start of its turn. If it fails, it must focus all of its actions that round on attempts to destroy the _mirror_.

**Mutilation (Su)** An abrikandilu’s bite causes horrific and hideous wounds that not only mar beauty but supernaturally diminish a creature’s sense of self-worth. A creature bitten by an abrikandilu must succeed at a DC 13 Fortitude save or gain a -1 penalty on all Charisma-based checks. This penalty stacks, up to a -5 penalty, and it lasts even after the wounds are healed. The penalty slowly fades with time, diminishing by 1 every 24 hours until it reaches 0. This is a curse effect. The save DC is Constitution-based.

##### Description

Known as wrecker demons, abrikandilus delight in destroying beauty, be it by rending a fine painting to shreds, reducing a magnificent _[[spells/Statue|statue]]_ to rubble, or scarring a lovely face. Abrikandilus are formed from the souls of mortals who vandalized art or defaced objects of exquisiteness, particularly those whose acts of _[[spells/Destruction|destruction]]_ were born from jealousy. All abrikandilus loathe only one thing more than beauty—their own reflections. Curiously, the faces of other abrikandilus do not vex a wrecker demon, but the sight of its own deformed shape drives an abrikandilu into a _[[items/Weapon Magic Abilities/Furious|furious]]_, brutish anger, impelling it to focus all of its energy on _[[items/Weapon Magic Abilities/Breaking|breaking]]_ the object, usually a _mirror_, in which it can see itself.

Abrikandilus are often used as ground troops in demonic wars, for they are excellent grunts on the battlefield and don’t require weapons or armor to excel at combat. Their penchant for demolishing works of art functions as an additional demoralizing element in battle, for even when abrikandilus are defeated, the damage they have dealt endures as a constant reminder of the value of what they destroyed.

An abrikandilu stands 4 feet tall and weighs 200 pounds.