---
cssclass: [monsters]
title1: Robot, Repair Robot
desc_short: This quadruped robot has glowing eyes and dexterous hands capable of examining
  and fixing machinery.
title2: Repair Robot
CR: 2
sources:
- name: Construct Handbook
  page: 56
  link: https://paizo.com/products/btq01vam
XP: 600
alignment: N
size: Medium
type: construct
subtypes:
- robot
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 14
  touch: 12
  flat_footed: 12
  components:
    dex: 2
    natural: 2
HP:
  HP: 31
  long: 2d10+20
saves:
  fort: 0
  ref: 2
  will: 0
immunities:
- construct traits
weaknesses:
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +6 (1d4+6)
      entries:
      - - damage: 1d4+6
      attack: slam
      bonus:
      - 6
  ranged:
  - - text: net +4 touch (entangle)
      entries:
      - - effect: entangle
      attack: net
      bonus:
      - 4
      touch: true
  special:
  - net
ability_scores:
  STR: 19
  DEX: 14
  CON:
  INT: 10
  WIS: 11
  CHA: 1
BAB: 2
CMB: 5
CMD: 18
CMD_other: 22 vs. trip
feats:
- name: Skill Focus (Knowledge [engineering])
skills:
  Disable Device: 6
  Knowledge (engineering): 8
  Perception: 4
languages:
- Common
special_qualities:
- refresh system
- repair robot
ecology:
  environment: any
  organization: solitary, pair, or union (3-12)
  treasure_type: none
special_abilities:
  Net (Ex): Five times per day, a repair robot can throw a polymer mesh net at a target
    within 10 feet, making a ranged touch attack against that target. On a hit, the
    target becomes entangled. The target creature can escape the net with a successful
    DC 20 Escape Artist check, which requires a full-round action. The polymer net
    has 10 hit points and can be burst with a DC 27 Strength check, which requires
    a full-round action. The net has no effect on creatures that are more than one
    size category larger or smaller than the repair robot.
  Refresh System (Ex): 'Once per day as a standard action, a repair robot can refresh
    its system and remove a condition affecting it. The condition removed must be
    one of the following: blinded, confused, dazzled, deafened, shaken, sickened,
    or staggered.'
  Repair Robot (Ex): Five times per day, as a standard action that does not provoke
    an attack of opportunity, a repair robot can restore 1d10 hit points to either
    itself or an adjacent robot.
desc_long: |-
  Repair robots are technologically skilled robots capable of fixing all manner of machinery with their surprisingly nimble hands. Repair robots are single-minded in their motivations, following their programming to repair anything they deem fixable. Many repair robot owners have returned to their workshops to find all of their in-progress inventions optimized or completely rebuilt by their robot servants.

   Although most commonly encountered in urban settings, repair robots have been known to survive, and even thrive, in other environments. If abandoned by its owner, a repair robot continues its repair duties as long as there are things to fix. Once it runs out of machinery to repair, the repair robot often wanders away from its place of employ, roaming the land in search for more repair opportunities. Repair robots that leave their homes often form unions with other abandoned repair robots; the robots in such unions satisfy their programming by repairing one another as they journey together.

   A typical repair robot is about 5 feet tall and weighs approximately 500 pounds.

---

# Robot, Repair Robot
This quadruped robot has glowing eyes and dexterous hands capable of examining and fixing machinery.
**Source** Construct Handbook pg. 56
**XP** 600

N Medium construct (robot)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 natural)
**hp** 31 (2d10+20)
**Fort** +0, **Ref** +2, **Will** +0
**Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 30 ft.
**Melee** slam +6 (1d4+6)
**Ranged** _[[items/Mundane/Net|net]]_ +4 touch (_[[spells/Entangle|entangle]]_)
**Special Attacks** _net_

##### Statistics
**Str** 19, **Dex** 14, **Con** —, **Int** 10, **Wis** 11, **Cha** 1
**Base Atk** +2; **CMB** +5; **CMD** 18 (22 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [engineering])
**Skills** Disable Device +6, Knowledge (engineering) +8, Perception +4
**Languages** Common
**SQ** refresh system, repair robot

##### Ecology

**Environment** any
**Organization** solitary, pair, or union (3-12)
**Treasure** none

### Special Abilities

**_Net_ (Ex)** Five times per day, a repair robot can throw a polymer mesh _net_ at a target within 10 feet, making a ranged touch attack against that target. On a hit, the target becomes _[[conditions/Entangled|entangled]]_. The target creature can escape the _net_ with a successful DC 20 Escape Artist check, which requires a full-round action. The polymer _net_ has 10 hit points and can be burst with a DC 27 Strength check, which requires a full-round action. The _net_ has no effect on creatures that are more than one size category larger or smaller than the repair robot.

**Refresh System (Ex)** Once per day as a standard action, a repair robot can refresh its system and remove a condition affecting it. The condition removed must be one of the following: _[[conditions/Blinded|blinded]]_, _[[conditions/Confused|confused]]_, _[[conditions/Dazzled|dazzled]]_, _[[conditions/Deafened|deafened]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Sickened|sickened]]_, or _[[conditions/Staggered|staggered]]_.

**Repair Robot (Ex)** Five times per day, as a standard action that does not provoke an attack of opportunity, a repair robot can restore 1d10 hit points to either itself or an adjacent robot.

##### Description

Repair robots are technologically skilled robots capable of fixing all manner of machinery with their surprisingly nimble hands. Repair robots are single-minded in their motivations, following their programming to repair anything they deem fixable. Many repair robot owners have returned to their workshops to find all of their in-progress inventions optimized or completely rebuilt by their robot servants.

Although most commonly encountered in urban settings, repair robots have been known to survive, and even thrive, in other environments. If abandoned by its owner, a repair robot continues its repair duties as long as there are things to fix. Once it runs out of machinery to repair, the repair robot often wanders away from its place of employ, roaming the land in search for more repair opportunities. Repair robots that leave their homes often form unions with other abandoned repair robots; the robots in such unions satisfy their programming by repairing one another as they journey together.

A typical repair robot is about 5 feet tall and weighs approximately 500 pounds.