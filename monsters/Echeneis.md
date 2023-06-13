---
cssclass: [monsters]
title1: Echeneis
desc_short: This thin, colorful fish has a broad, segmented sucker above its narrow
  mouth. A line of spines runs down its back.
title2: Echeneis
CR: 1
sources:
- name: Bestiary 5
  page: 103
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 400
alignment: N
size: Small
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 13
  touch: 11
  flat_footed: 13
  components:
    natural: 2
    size: 1
HP:
  HP: 19
  long: 3d10+3
saves:
  fort: 4
  ref: 5
  will: 1
speeds:
  base: 5
  swim: 20
attacks:
  melee:
  - - text: bite +5 (1d4+1 plus attach)
      entries:
      - - damage: 1d4+1
        - effect: attach
      attack: bite
      bonus:
      - 5
    - text: tail slap +0 (1d4)
      entries:
      - - damage: 1d4
      attack: tail slap
      bonus:
      - 0
  - - text: sucker +5 touch (attach)
      entries:
      - - effect: attach
      attack: sucker
      bonus:
      - 5
      touch: true
    - text: tail slap +0 (1d4)
      entries:
      - - damage: 1d4
      attack: tail slap
      bonus:
      - 0
  special:
  - attach
  - sap speed
ability_scores:
  STR: 12
  DEX: 11
  CON: 13
  INT: 2
  WIS: 10
  CHA: 13
BAB: 3
CMB: 3
CMB_other: +11 grapple while attached
CMD: 13
CMD_other: 17 vs. grapple while attached
feats:
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Perception: 5
  Stealth: 8
  Swim: 9
ecology:
  environment: warm or temperate water
  organization: solitary, pair, or school (3-8)
  treasure_type: none
special_abilities:
  Attach (Ex): An echeneis that hits with its bite or sucker attack automatically
    initiates a grapple against its target. While attached to a creature or vehicle,
    the echeneis gains a +8 bonus on combat maneuver checks to grapple and +4 bonus
    to its CMD against grapple attempts but loses any Dexterity bonus or dodge bonus
    to Armor Class. An echeneis that successfully maintains a grapple can make a free
    tail slap attack against any target except the one to which it is attached.
  Sap Speed (Su): Whenever an echeneis ends its turn attached to a creature or vehicle,
    it steals fragments of time from its host and gains the benefits of haste for
    as long as it is attached and for an equal amount of time thereafter (maximum
    3 hours). A creature with an attached echeneis takes a cumulative -1 penalty to
    Dexterity each round (which stacks with multiple echeneises) and must succeed
    at a DC 12 Will save or be affected as if by a slow spell until the end of the
    echeneis's next turn. The penalty to Dexterity ends at the end of the echeneis's
    turn if it is no longer attached to the creature. A vehicle with an attached echeneis
    has its speed reduced by half until the end of the echeneis's next turn. A creature
    or vehicle slowed by a second echeneis is reduced to one-quarter speed. A creature
    or vehicle slowed by three or more echeneises is reduced to a speed of 0 feet.
    The save DC is Charisma-based.
desc_long: |-
  The echeneis is a magical fish known to sailors in many parts of the world as a major pest due to its theft of speed from boats and large, swimming creatures alike. It ranges across large stretches of water, stopping every few hours to feed and sap velocity from large boats, sharks, whales, and other hosts that might overlook it. Although native to warm waters, echeneises sometimes follow trade vessels elsewhere. Because echeneises prefer murky shallows, sailors rarely notice one before it begins to slow a vessel. The sharp and sturdy spines atop the creatures' backs scrape the hulls of ships to which they are attached, so sailors lament both the short-term inconvenience and the long-term damage caused by these pests. Old boats with hundreds of scrape marks on their bottoms garner reputations as cursed, and their captains face a serious stigma when trying to recruit crews. It is true that some ships draw echeneises more than others, but apart from the ship's size there is no indication as to what else might attract the creatures.

   Like the remoras they resemble, echeneises are scavengers. However, they are aggressive and often retaliate when knocked off of creatures or vessels. In combat, echeneises attach themselves to enemies to slow them down while flailing with their tails against anyone attempting to remove them. If badly injured while attached, an echeneis releases its victim and uses the speed it has stolen to quickly escape.

   An echeneis averages over 3 feet in length and weighs at least 12 pounds.

---

# Echeneis
This thin, colorful fish has a broad, segmented sucker above its narrow mouth. A line of spines runs down its back.
**Source** Bestiary 5 pg. 103
**XP** 400

N Small magical beast (aquatic)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 13, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 natural, +1 size)
**hp** 19 (3d10+3)
**Fort** +4, **Ref** +5, **Will** +1

##### Offense
**Speed** 5 ft., swim 20 ft.
**Melee** bite +5 (1d4+1 plus _[[universal monster rules/Attach|attach]]_), tail slap +0 (1d4) or sucker +5 touch (_attach_), tail slap +0 (1d4)
**Special Attacks** _attach_, _[[items/Weapon/Sap|sap]]_ speed

##### Statistics
**Str** 12, **Dex** 11, **Con** 13, **Int** 2, **Wis** 10, **Cha** 13
**Base Atk** +3; **CMB** +3 (+11 grapple while attached); **CMD** 13 (17 vs. grapple while attached)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Perception +5, Stealth +8, Swim +9

##### Ecology

**Environment** warm or temperate water
**Organization** solitary, pair, or school (3–8)
**Treasure** none

### Special Abilities

**_Attach_ (Ex)** An _[[monsters/Echeneis|echeneis]]_ that hits with its bite or sucker attack automatically initiates a grapple against its target. While attached to a creature or vehicle, the _echeneis_ gains a +8 bonus on combat maneuver checks to grapple and +4 bonus to its CMD against grapple attempts but loses any Dexterity bonus or dodge bonus to Armor Class. An _echeneis_ that successfully maintains a grapple can make a free tail slap attack against any target except the one to which it is attached.
**_Sap_ Speed (Su)** Whenever an _echeneis_ ends its turn attached to a creature or vehicle, it steals fragments of time from its host and gains the benefits of _[[spells/Haste|haste]]_ for as long as it is attached and for an equal amount of time thereafter (maximum 3 hours). A creature with an attached _echeneis_ takes a cumulative –1 penalty to Dexterity each round (which stacks with multiple echeneises) and must succeed at a DC 12 Will save or be affected as if by a _[[spells/Slow|slow]]_ spell until the end of the _echeneis_’s next turn. The penalty to Dexterity ends at the end of the _echeneis_’s turn if it is no longer attached to the creature. A vehicle with an attached _echeneis_ has its speed reduced by half until the end of the _echeneis_’s next turn. A creature or vehicle slowed by a second _echeneis_ is reduced to one-quarter speed. A creature or vehicle slowed by three or more echeneises is reduced to a speed of 0 feet. The save DC is Charisma-based.

##### Description

The _echeneis_ is a magical fish known to sailors in many parts of the world as a major pest due to its theft of speed from boats and large, swimming creatures alike. It ranges across large stretches of water, stopping every few hours to feed and _sap_ velocity from large boats, sharks, whales, and other hosts that might _[[spells/Overlook|overlook]]_ it. Although native to warm waters, echeneises sometimes follow trade vessels elsewhere. Because echeneises prefer murky shallows, sailors rarely notice one before it begins to _slow_ a vessel. The sharp and sturdy spines atop the creatures’ backs scrape the hulls of ships to which they are attached, so sailors lament both the short-term inconvenience and the long-term damage caused by these pests. Old boats with hundreds of scrape marks on their bottoms garner reputations as cursed, and their captains face a serious stigma when trying to _[[npcs/Recruit|recruit]]_ crews. It is true that some ships draw echeneises more than others, but apart from the ship’s size there is no indication as to what else might attract the creatures.

Like the remoras they resemble, echeneises are scavengers. However, they are aggressive and often retaliate when knocked off of creatures or vessels. In combat, echeneises _attach_ themselves to enemies to _slow_ them down while flailing with their tails against anyone attempting to remove them. If badly injured while attached, an _echeneis_ releases its victim and uses the speed it has stolen to quickly escape.

An _echeneis_ averages over 3 feet in length and weighs at least 12 pounds.