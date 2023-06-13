---
cssclass: [monsters]
title1: Robot, Scrapyard Robot
desc_short: Frayed wires and broken-off protrusions sprout from mechanical construct',
  and one of its salvaged arms ends in a spinning blade.
title2: Scrapyard Robot
CR: 3
sources:
- name: Numeria, Land of Fallen Stars
  page: 58
  link: http://paizo.com/products/btpy978l?Pathfinder-Campaign-Setting-Numeria-Land-of-Fallen-Stars
XP: 800
alignment: N
size: Medium
type: construct
subtypes:
- robot
initiative:
  bonus: -1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 14
  touch: 9
  flat_footed: 14
  components:
    dex: -1
    natural: 5
HP:
  HP: 42
  long: 4d10+20
saves:
  fort: 1
  ref: 0
  will: 1
defensive_abilities:
- hardness 5
immunities:
- construct traits
weaknesses:
- fall to pieces
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +7 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: slam
      bonus:
      - 7
  - - text: rotary saw +8 (2d4+4/×3)
      entries:
      - - damage: 2d4+4
          crit_multiplier: 3
      attack: rotary saw
      bonus:
      - 8
ability_scores:
  STR: 17
  DEX: 8
  CON:
  INT: 5
  WIS: 10
  CHA: 1
BAB: 4
CMB: 7
CMD: 16
CMD_other: 20 vs. trip
feats:
- name: Power Attack
- name: Weapon Focus (rotary saw)
skills:
  Knowledge (engineering): 2
  Perception: 5
languages:
- Common
- Hallit
special_qualities:
- repair
- staggered
ecology:
  environment: any ruin (Numeria)
  organization: solitary
  treasure_type: none
special_abilities:
  Fall to Pieces (Ex): |-
    Attacks and effects that deal more than 25% of a scrapyard robot's maximum hit points in damage (10 hit points for a standard scrapyard robot) impair one of the robot's components. Determine which subsystem randomly by rolling 1d6. If the subsystem has already been impaired, there is no further effect.

    1 CPU: The robot is confused (Pathfinder RPG Core Rulebook 566)

    2 Fractured Plating: Reduce the robot's natural armor bonus by 3.

    3 Power Core: Attacks against the robot with natural weapons, unarmed strikes, or metal weapons deal 1d6 points of electricity damage to the attacker, and the robot's slam attack deals an additional 1d6 points of electricity damage. The robot shuts down from power loss in 1d4+1 rounds.

    4 Rotary Saw: The robot loses its rotary saw attack.

    5 Servos: The robot's speed is reduced to 15 feet and its CMD against trip combat maneuvers is reduced by 8.

    6 Sensors: The robot is blinded.
  Repair (Ex): A scrapyard robot can use the inactive bodies of other robots to repair
    damage to itself. Doing so restores 10 hit points and removes one condition imparted
    by its fall to pieces ability per 8-hour period of uninterrupted work. Eight hours
    of repair expends all salvageable parts from 1 Medium robot. For each size category
    a scrapped robot is above Medium, the scrapyard robot can perform another 8 hours
    of repairs using that robot's parts. For each size category smaller than Medium
    scrapped robots are, the scrapyard robot requires twice as many robots to complete
    8 hours of work.
  Staggered (Ex): The poor construction of a scrapyard robot allows it to take only
    a single move or standard action each round. In effect, it always has the staggered
    condition. A scrapyard robot can move up to its speed and attack in the same round
    as a charge action.
desc_long: Pieced together from broken technology, these constructs lack the balance
  to stand upright, the motor control to use their hands (if they have any), and the
  intelligence possessed by advanced robots, but they still retain a halting consciousness
  and the ability to obey simple commands.

---

# Robot, Scrapyard Robot
Frayed wires and broken-off protrusions sprout from mechanical construct’, and one of its salvaged arms ends in a spinning blade.
**Source** Numeria, Land of _[[monsters/Fallen|Fallen]]_ Stars pg. 58
**XP** 800

N Medium construct (robot)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 14, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 14 (–1 Dex, +5 natural)
**hp** 42 (4d10+20)
**Fort** +1, **Ref** +0, **Will** +1
**Defensive Abilities** hardness 5; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** fall to pieces, vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 30 ft.
**Melee** slam +7 (1d4+4) or rotary _[[items/Mundane/Saw|saw]]_ +8 (2d4+4/×3)

##### Statistics
**Str** 17, **Dex** 8, **Con** —, **Int** 5, **Wis** 10, **Cha** 1
**Base Atk** +4; **CMB** +7; **CMD** 16 (20 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (rotary _saw_)
**Skills** Knowledge (engineering) +2, Perception +5
**Languages** Common, Hallit
**SQ** repair, _[[conditions/Staggered|staggered]]_

##### Ecology

**Environment** any ruin (Numeria)
**Organization** solitary
**Treasure** none

### Special Abilities

**Fall to Pieces (Ex)** Attacks and effects that deal more than 25% of a scrapyard robot’s maximum hit points in damage (10 hit points for a standard scrapyard robot) impair one of the robot’s components. Determine which subsystem randomly by rolling 1d6. If the subsystem has already been impaired, there is no further effect.

1 CPU: The robot is _[[conditions/Confused|confused]]_ (Pathfinder RPG Core Rulebook 566)

2 Fractured Plating: Reduce the robot’s natural armor bonus by 3.

3 Power Core: Attacks against the robot with natural weapons, unarmed strikes, or metal weapons deal 1d6 points of electricity damage to the attacker, and the robot’s slam attack deals an additional 1d6 points of electricity damage. The robot shuts down from power loss in 1d4+1 rounds.

4 Rotary _Saw_: The robot loses its rotary _saw_ attack.

5 Servos: The robot’s speed is reduced to 15 feet and its CMD against _trip_ combat maneuvers is reduced by 8.

6 Sensors: The robot is _[[conditions/Blinded|blinded]]_.

**Repair (Ex)** A scrapyard robot can use the inactive bodies of other robots to repair damage to itself. Doing so restores 10 hit points and removes one condition imparted by its fall to pieces ability per 8-hour period of uninterrupted work. Eight hours of repair expends all salvageable parts from 1 _Medium_ robot. For each size category a scrapped robot is above _Medium_, the scrapyard robot can perform another 8 hours of repairs using that robot’s parts. For each size category smaller than _Medium_ scrapped robots are, the scrapyard robot requires twice as many robots to complete 8 hours of work.
**_Staggered_ (Ex)** The poor construction of a scrapyard robot allows it to take only a single move or standard action each round. In effect, it always has the _staggered_ condition. A scrapyard robot can move up to its speed and attack in the same round as a charge action.

##### Description

Pieced together from _[[conditions/Broken|broken]]_ technology, these constructs lack the balance to stand upright, the motor control to use their hands (if they have any), and the intelligence possessed by advanced robots, but they still retain a halting consciousness and the ability to obey simple commands.