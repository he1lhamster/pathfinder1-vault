---
cssclass: [monsters]
title1: Unicorn
desc_short: This magnificent beast looks like a white horse, but with a goat's beard
  and a single long ivory horn on its brow.
title2: Unicorn
CR: 3
sources:
- name: Pathfinder RPG Bestiary
  page: 269
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 800
alignment: CG
size: Large
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: magic circle against evil
AC:
  AC: 15
  touch: 12
  flat_footed: 12
  components:
    dex: 3
    natural: 3
    size: -1
    deflection vs. evil: 2
HP:
  HP: 34
  long: 4d10+12
saves:
  fort: 7
  ref: 7
  will: 6
  other: +2 resistance vs. evil
immunities:
- charm
- compulsion
- poison
speeds:
  base: 60
attacks:
  melee:
  - - text: gore +8 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: gore
      bonus:
      - 8
    - text: 2 hooves +5 (1d3+2)
      entries:
      - - damage: 1d3+2
      count: 2
      attack: hooves
      bonus:
      - 5
  special:
  - powerful charge (gore, 2d8+8)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
    other: as free action
  - name: light
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: cure moderate wounds
    source: default
    freq: 1/day
  - name: greater teleport
    source: default
    freq: 1/day
    other: within its forest territory
  - name: neutralize poison
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 9
ability_scores:
  STR: 18
  DEX: 17
  CON: 16
  INT: 11
  WIS: 21
  CHA: 24
BAB: 4
CMB: 9
CMD: 22
CMD_other: 26 vs. trip
feats:
- name: Multiattack
- name: Weapon Focus (horn)
skills:
  Acrobatics: 8
  Perception: 10
  Stealth: 8
  Survival: 7
    in forests: 10
  _racial_mods:
    Survival:
      in forests: 3
    Stealth:
      _: 4
languages:
- Common
- Sylvan
special_qualities:
- magical strike
- wild empathy +17
ecology:
  environment: temperate forests
  organization: solitary, mated pair, or blessing (3-6)
  treasure_type: none
special_abilities:
  Magic Circle against Evil (Su): This ability continually duplicates the effect of
    the spell. The unicorn cannot suppress this ability.
  Magical Strike (Ex): A unicorn's gore attack is treated as a magic good weapon for
    the purposes of damage reduction.
  Wild Empathy (Su): This works like the druid's wild empathy class feature, except
    the unicorn has a +6 racial bonus on the check. Unicorns with druid levels add
    this racial modifier to their wild empathy checks.
desc_long: |-
  Unicorns are fierce, intelligent creatures of the forest, noble beasts who keep their own counsel and typically appear only to defend their homes against evil. They universally shun all creatures except for good-aligned fey, good-aligned humanoid women, and the woodlands' native animals, though they may fight alongside other good creatures against common enemies. A typical unicorn is 8 feet long and 5 feet tall at the shoulder, weighing 1,200 pounds.

  Unicorns mate for life, and the pairs generally make their homes in specific glades or dells within the vast forests they protect (these regions can cover anywhere from a few dozen square miles to hundreds). They allow good and neutral creatures to pass through, hunt for food, or reside in their woods unharmed, but evil creatures and those who damage the local ecosystem more than necessary through sport hunting or commercial logging are swiftly driven out or killed. On rare occasions, lone unicorns without mates or whose partners have been slain have been known to adopt young women of exceptionally pure virtue as surrogates, allowing the women to ride on their backs and becoming their guardians and protectors for life. This bond generally ends amiably if the woman becomes more committed to someone else-such as a lover or child-giving rise to the myth that unicorns only befriend virgins.

  A unicorn's horn is the focus for its powers, and in order to use its spell-like abilities on other creatures the unicorn must touch them with it. Evil creatures greatly value unicorn horns as reagents for healing potions and other dark rites, and a single powdered unicorn horn counts as 1,600 gp when used as a component for crafting healing magic.

---

# Unicorn
This magnificent beast looks like a white _[[monsters/Horse|horse]]_, but with a goat’s beard and a single long ivory horn on its brow.
**Source** Pathfinder RPG Bestiary pg. 269
**XP** 800

CG Large magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +10
**Aura** _[[spells/Magic Circle against Evil|magic circle against evil]]_

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +3 natural, –1 size; +2 deflection vs. evil)
**hp** 34 (4d10+12)
**Fort** +7, **Ref** +7, **Will** +6; +2 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**Immune** charm, compulsion, poison

##### Offense
**Speed** 60 ft.
**Melee** gore +8 (1d8+4), 2 hooves +5 (1d3+2)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d8+8)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
At will—_[[spells/Detect Evil|detect evil]]_ (as free action), light
3/day—_[[spells/Cure Light Wounds|cure light wounds]]_
1/day—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, greater teleport (within its forest territory), _[[spells/Neutralize Poison|neutralize poison]]_ (DC 21)

##### Statistics
**Str** 18, **Dex** 17, **Con** 16, **Int** 11, **Wis** 21, **Cha** 24
**Base Atk** +4; **CMB** +9; **CMD** 22 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (horn)
**Skills** Acrobatics +8, Perception +10, Stealth +8, Survival +7 (+10 in forests); **Racial Modifiers** +3 Survival in forests, +4 Stealth
**Languages** Common, Sylvan
**SQ** magical strike, wild _[[feats/Empathy|empathy]]_ +17

##### Ecology

**Environment** temperate forests
**Organization** solitary, mated pair, or blessing (3–6)
**Treasure** none

### Special Abilities

**_Magic Circle against Evil_ (Su)** This ability continually duplicates the effect of the spell. The _[[monsters/Unicorn|unicorn]]_ cannot suppress this ability.

**Magical Strike (Ex)** A _unicorn_’s gore attack is treated as a magic good weapon for the purposes of _[[universal monster rules/Damage Reduction|damage reduction]]_.

**Wild _Empathy_ (Su)** This works like the _[[classes/Druid|druid]]_’s wild _empathy_ class feature, except the _unicorn_ has a +6 racial bonus on the check. Unicorns with _druid_ levels add this racial modifier to their wild _empathy_ checks.

##### Description

Unicorns are fierce, intelligent creatures of the forest, noble beasts who keep their own counsel and typically appear only to defend their homes against evil. They universally shun all creatures except for good-aligned fey, good-aligned humanoid women, and the woodlands’ native animals, though they may fight alongside other good creatures against common enemies. A typical _unicorn_ is 8 feet long and 5 feet tall at the shoulder, weighing 1,200 pounds.

Unicorns mate for life, and the pairs generally make their homes in specific glades or dells within the vast forests they protect (these regions can cover anywhere from a few dozen square miles to hundreds). They allow good and neutral creatures to pass through, hunt for food, or reside in their woods unharmed, but evil creatures and those who damage the local ecosystem more than necessary through sport hunting or commercial logging are swiftly driven out or killed. On rare occasions, lone unicorns without mates or whose partners have been slain have been known to adopt young women of exceptionally pure _[[spells/Virtue|virtue]]_ as surrogates, allowing the women to ride on their backs and becoming their guardians and protectors for life. This bond generally ends amiably if the woman becomes more committed to someone else—such as a lover or child—giving rise to the myth that unicorns only befriend virgins.

A _unicorn_’s horn is the focus for its powers, and in order to use its _spell-like abilities_ on other creatures the _unicorn_ must touch them with it. Evil creatures greatly value _unicorn_ horns as reagents for healing potions and other dark rites, and a single powdered _unicorn_ horn counts as 1,600 gp when used as a component for crafting healing magic.