---
cssclass: [monsters]
title1: Robot, Octopod Mechanic Drone
desc_short: This octopus-like robot has eight tentacles that it uses to repair multiple
  machines at a time.
title2: Octopod Mechanic Drone
CR: 13
sources:
- name: Construct Handbook
  page: 56
  link: https://paizo.com/products/btq01vam
XP: 25600
alignment: N
size: Medium
type: construct
subtypes:
- robot
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: crew boss
  radius: 30
AC:
  AC: 24
  touch: 14
  flat_footed: 20
  components:
    dex: 3
    dodge: 1
    natural: 10
HP:
  HP: 124
  long: 16d10+36
  other: force field (65 hp, fast healing 13)
saves:
  fort: 5
  ref: 10
  will: 2
defensive_abilities:
- hardness 10
immunities:
- construct traits
weaknesses:
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: 8 slams +22 (1d4+6/19-20 plus grab)
      entries:
      - - damage: 1d4+6
          crit_range: 19-20
        - effect: grab
      count: 8
      attack: slams
      bonus:
      - 22
  ranged:
  - - text: 2 integrated laser pistols +19 touch (2d6 fire)
      entries:
      - - damage: 2d6
          type: fire
      count: 2
      attack: integrated laser pistols
      bonus:
      - 19
      touch: true
  special:
  - combined arms
  - constrict (1d6+6)
space: 5
reach: 10
ability_scores:
  STR: 22
  DEX: 16
  CON:
  INT: 15
  WIS: 5
  CHA: 5
BAB: 16
CMB: 22
CMD: 36
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Improved Critical (slams)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Climb: 30
  Disable Device: 19
  Knowledge (engineering): 18
  Perception: 13
languages:
- Common
special_qualities:
- integrated weaponry
- mass repair
- mechanical expertise
- reboot system
- repair station
ecology:
  environment: any
  organization: solitary or pair
  treasure_type: none
special_abilities:
  Crew Boss (Ex): When working with other robots, an octopod mechanic drone can coordinate
    the group's efforts to maximize efficiency. All other robots with 30 feet of an
    octopod mechanic drone gain a +2 competence bonus on attack rolls and skill checks.
  Integrated Laser Pistols (Ex): An octopod mechanic drone has two integrated laser
    pistols with a range increment of 50 feet.
  Mass Repair (Ex): An octopod mechanic drone can use its tentacles to repair multiple
    robots at one time. As a full-round action that does not provoke attacks of opportunity,
    an octopod mechanic drone can restore 3d10 hit points to itself and each allied
    robot within 10 feet of it.
  Mechanical Expertise (Ex): An octopod mechanic drone is programmed with deep knowledge
    of machinery. The octopod mechanic drone is considered trained in all skills used
    against a technology-based subject.
  Reboot System (Ex): 'An octopod mechanic drone can reboot a robot's system, whether
    its own or an ally's. As a standard action, an octopod mechanic drone can remove
    all of the following conditions from either itself or a robot within 10 feet of
    it: blinded, confused, dazzled, deafened, shaken, sickened, and staggered.'
  Repair Station (Ex): As a full-round action, an octopod mechanic drone can anchor
    its body to the ground, freeing its robotic tentacles to focus on attacking and
    repairing rather than supporting itself. While it is anchored, it loses its Dexterity
    bonus and dodge bonus to AC, it cannot move, and it gains a +8 enhancement bonus
    to CMD against bull rush, drag, and reposition combat maneuvers. An anchored octopod
    mechanic drone doubles the number of hit points it restores using its mass repair
    ability, and it gains a +2 enhancement bonus on damage rolls with its slam attacks.
    Unanchoring itself from the ground is a full-round action.
desc_long: |-
  Octopod mechanic drones are the ultimate in repair-robot technology. These multilimbed robots can manipulate each of their metal tentacles with extreme precision, allowing them to perform delicate fixes and repair many machines at once. Octopod mechanic drones also have the ability to anchor themselves to the ground, allowing them to commit their tentacles entirely to repair rather than having to use them for support. Owners of octopod mechanic drones often rely on the robots to manage the rest of their mechanical workers; the robots communicate more loudly and directly than others of their kind, making them natural leaders, and they have a distinct ability to coordinate the group for maximum efficiency.

   An octopod mechanic drone is about 6 feet tall, with tentacles roughly 10 feet long, and weighs approximately 750 pounds.

---

# Robot, Octopod Mechanic Drone
This octopus-like robot has eight tentacles that it uses to repair multiple machines at a time.
**Source** Construct Handbook pg. 56
**XP** 25,600

N Medium construct (robot)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13
**Aura** crew boss (30 ft.)

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 124 (16d10+36); force field (65 hp, _[[universal monster rules/Fast Healing|fast healing]]_ 13)
**Fort** +5, **Ref** +10, **Will** +2
**Defensive Abilities** hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 8 slams +22 (1d4+6/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** 2 integrated laser pistols +19 touch (2d6 fire)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** combined arms, _[[universal monster rules/Constrict|constrict]]_ (1d6+6)

##### Statistics
**Str** 22, **Dex** 16, **Con** —, **Int** 15, **Wis** 5, **Cha** 5
**Base Atk** +16; **CMB** +22; **CMD** 36 (can't be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (slams), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** _Climb_ +30, Disable Device +19, Knowledge (engineering) +18, Perception +13
**Languages** Common
**SQ** integrated weaponry, mass repair, mechanical expertise, _[[spells/Reboot|reboot]]_ system, repair station

##### Ecology

**Environment** any
**Organization** solitary or pair
**Treasure** none

### Special Abilities

**Crew Boss (Ex)** When working with other robots, an octopod mechanic drone can coordinate the group’s efforts to maximize efficiency. All other robots with 30 feet of an octopod mechanic drone gain a +2 competence bonus on attack rolls and skill checks.

**Integrated Laser Pistols (Ex)** An octopod mechanic drone has two integrated laser pistols with a range increment of 50 feet.

**Mass Repair (Ex)** An octopod mechanic drone can use its tentacles to repair multiple robots at one time. As a full-round action that does not provoke attacks of opportunity, an octopod mechanic drone can restore 3d10 hit points to itself and each allied robot within 10 feet of it.

**Mechanical Expertise (Ex)** An octopod mechanic drone is programmed with deep knowledge of machinery. The octopod mechanic drone is considered trained in all skills used against a technology-based subject.

**_Reboot_ System (Ex)** An octopod mechanic drone can _reboot_ a robot’s system, whether its own or an ally’s. As a standard action, an octopod mechanic drone can remove all of the following conditions from either itself or a robot within 10 feet of it: _[[conditions/Blinded|blinded]]_, _[[conditions/Confused|confused]]_, _[[conditions/Dazzled|dazzled]]_, _[[conditions/Deafened|deafened]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Sickened|sickened]]_, and _[[conditions/Staggered|staggered]]_.

**Repair Station (Ex)** As a full-round action, an octopod mechanic drone can anchor its body to the ground, freeing its robotic tentacles to focus on attacking and repairing rather than supporting itself. While it is anchored, it loses its Dexterity bonus and _dodge_ bonus to AC, it cannot move, and it gains a +8 enhancement bonus to CMD against bull rush, drag, and reposition combat maneuvers. An anchored octopod mechanic drone doubles the number of hit points it restores using its mass repair ability, and it gains a +2 enhancement bonus on damage rolls with its slam attacks. Unanchoring itself from the ground is a full-round action.

##### Description

Octopod mechanic drones are the ultimate in repair-robot technology. These multilimbed robots can manipulate each of their metal tentacles with extreme precision, allowing them to perform delicate fixes and repair many machines at once. Octopod mechanic drones also have the ability to anchor themselves to the ground, allowing them to commit their tentacles entirely to repair rather than having to use them for support. Owners of octopod mechanic drones often rely on the robots to manage the rest of their mechanical workers; the robots communicate more loudly and directly than others of their kind, making them natural leaders, and they have a distinct ability to coordinate the group for maximum efficiency.

An octopod mechanic drone is about 6 feet tall, with tentacles roughly 10 feet long, and weighs approximately 750 pounds.