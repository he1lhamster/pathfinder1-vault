---
cssclass: [monsters]
title1: Robot, Director Robot
desc_short: A humanoid torso and four spindly legs sprout from the top of this black-paneled
  orb. Buzzing mechanical tentacles churn and writhe below its bulk.
title2: Director Robot
CR: 10
sources:
- name: 'Pathfinder #90: The Divinity Drive'
  page: 88
  link: http://paizo.com/products/btpy95bw?Pathfinder-Adventure-Path-90-The-Divinity-Drive
XP: 9600
alignment: N
size: Large
type: construct
subtypes:
- robot
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 23
  touch: 13
  flat_footed: 19
  components:
    dex: 3
    dodge: 1
    natural: 10
    size: -1
HP:
  HP: 121
  long: 14d10+44
saves:
  fort: 7
  ref: 10
  will: 9
defensive_abilities:
- all-around vision
- hardness 10
immunities:
- construct traits
resistances:
  cold: 10
  fire: 10
weaknesses:
- vulnerable to critical hits and electricity
speeds:
  base: 40
  climb: 30
attacks:
  melee:
  - - text: 2 tentacles +19 (1d10+6)
      entries:
      - - damage: 1d10+6
      count: 2
      attack: tentacles
      bonus:
      - 19
    - text: 2 slams +19 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: slams
      bonus:
      - 19
  ranged:
  - - text: integrated laser rifle +16 (2d6 fire)
      entries:
      - - damage: 2d6
          type: fire
      attack: integrated laser rifle
      bonus:
      - 16
  special:
  - electromagnetic pulse
  - grasping tentacles
  - override
space: 10
reach: 5
reach_other: 10 ft. with tentacles
ability_scores:
  STR: 22
  DEX: 17
  CON:
  INT: 16
  WIS: 15
  CHA: 1
BAB: 14
CMB: 21
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Dodge
- name: Mobility
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Spring Attack
- name: Toughness
skills:
  Acrobatics: 10
    when jumping: 14
  Climb: 15
  Craft (mechanical): 15
  Disable Device: 15
  Knowledge (engineering): 15
  Perception: 15
  Sense Motive: 15
languages:
- Androffan
- Common
- Hallit
special_qualities:
- advanced analytics
- cling
- repair robot
ecology:
  environment: any (Numeria)
  organization: solitary, patrol (1 director and 2-8 gearsmen), or unit (1 director,
    2-12 gearsmen, and 1 myrmidon)
  treasure_type: none
special_abilities:
  Advanced Analytics (Ex): A director robot gains a bonus equal to its Intelligence
    bonus on all saving throws.
  Cling (Ex): A combination of magnetic pads and electrostatic emitters in its feet
    allow a director robot to climb and travel on vertical or horizontal surfaces
    without having to attempt Climb checks, even allowing it to traverse these surfaces
    while upside down.
  Electromagnetic Pulse (Ex): Once per day as a standard action, a director robot
    can unleash an electromagnetic pulse that deals 6d6 points of electricity damage
    to any robots or creatures with cybernetic implants within a 20-foot radius (Reflex
    DC 20 half). This bypasses any active force fields or similar effects, but doesn't
    harm other living creatures or the director robot. Any technological item within
    this radius is drained of 1d6 charges unless it succeeds at a DC 20 Reflex save.
    The save DCs are Intelligence-based.
  Grasping Tentacles (Ex): A director robot's tentacles are primary attacks and have
    the grab special ability.
  Integrated Laser Rifle (Ex): A director robot has a built-in laser rifle. This weapon
    has a range of 150 feet and deals 2d6 points of fire damage on a hit. The weapon
    can fire once per round as a ranged touch attack. A laser attack can pass through
    force fields and force effects, such as a wall of force, to strike a foe beyond
    without damaging that field. Objects like glass or other transparent barriers
    don't provide cover from lasers, but unlike force barriers, a transparent physical
    barrier still takes damage when a laser passes through it. Invisible creatures
    and objects are immune to damage from lasers. Fog, smoke, and other clouds provide
    cover in addition to concealment from laser attacks. Darkness (magical or otherwise)
    has no effect on lasers other than providing concealment.
  Override (Ex): |-
    A director robot can usurp control of an otherwise functional robot. In order to gain control of a robot, the director robot must first make a ranged touch attack against a target robot within a range of 60 feet. If the attack is successful, the targeted robot must succeed at a DC 20 Will saving throw to prevent the director robot from linking to the target's command processor. On any subsequent turn after a link is established, the director robot can issue a command to the targeted robot as a standard action. The targeted robot can attempt another Will save (DC 20) to resist following each command.

     To command its target, the director robot must be within 60 feet of the targeted robot and must issue the command in a language the robot understands. The types of commands it can issue are similar to those allowed by a suggestion spell-once a command is successfully issued, the robot does its best to carry out the orders over the course of the next hour. Additionally, any robot affected by this ability also gains a +2 competence bonus on attack and weapon damage rolls. These save DCs are Intelligence-based.
  Repair Robot (Ex): As a standard action that doesn't provoke an attack of opportunity,
    a director robot can repair damage done to either itself or an adjacent creature
    with the robot subtype, healing the target for 1d10 points of damage.
desc_long: No society endures without order, and among robots that order is enforced
  by directors. Clad in gleaming metal and viewing the world through a rotating array
  of lenses, a director is a robotic overseer designed to maximize efficiency and
  command the loyalty of lesser automatons. Its torso rests upon a utilitarian egg-shaped
  pod loaded with manipulators, tools, and dozens of thin mechanical tendrils. Four
  long, mechanical legs support its bulk and carry it across any terrain, even allowing
  the robot to cling magnetically to vertical surfaces. While the upper frame sports
  human-like arms to manipulate traditional tools and weapons, two powerful tentacles
  extend from below its frame to facilitate combat and handle heavy lifting. Though
  its humanoid torso is barely larger than that of a human, the director's entire
  frame stands over 10 feet tall and weighs nearly half a ton.

---

# Robot, Director Robot
A humanoid torso and four spindly legs sprout from the top of this black-paneled orb. Buzzing mechanical tentacles churn and writhe below its bulk.
**Source** Pathfinder #90: The Divinity Drive pg. 88
**XP** 9,600

N Large construct (robot)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 Dex, +1 dodge, +10 natural, –1 size)
**hp** 121 (14d10+44)
**Fort** +7, **Ref** +10, **Will** +9
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** cold 10, fire 10
**Weaknesses** vulnerable to critical hits and electricity

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 tentacles +19 (1d10+6), 2 slams +19 (1d8+6)
**Ranged** integrated laser _[[items/Weapon/Rifle|rifle]]_ +16 (2d6 fire)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with tentacles)
**Special Attacks** electromagnetic pulse, _[[spells/Grasping Tentacles|grasping tentacles]]_, override

##### Statistics
**Str** 22, **Dex** 17, **Con** —, **Int** 16, **Wis** 15, **Cha** 1
**Base Atk** +14; **CMB** +21; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +10 (+14 when jumping), _Climb_ +15, Craft (mechanical) +15, Disable Device +15, Knowledge (engineering) +15, Perception +15, Sense Motive +15
**Languages** Androffan, Common, Hallit
**SQ** advanced analytics, cling, repair robot

##### Ecology

**Environment** any (Numeria)
**Organization** solitary, patrol (1 director and 2–8 gearsmen), or unit (1 director, 2–12 gearsmen, and 1 myrmidon)
**Treasure** none

### Special Abilities

**Advanced Analytics (Ex)** A director robot gains a bonus equal to its Intelligence bonus on all saving throws.

**Cling (Ex)** A combination of magnetic pads and electrostatic emitters in its feet allow a director robot to _climb_ and travel on vertical or horizontal surfaces without having to attempt _Climb_ checks, even allowing it to traverse these surfaces while upside down.

**Electromagnetic Pulse (Ex)** Once per day as a standard action, a director robot can unleash an electromagnetic pulse that deals 6d6 points of electricity damage to any robots or creatures with cybernetic implants within a 20-foot radius (Reflex DC 20 half). This bypasses any active force fields or similar effects, but doesn’t _[[spells/Harm|harm]]_ other living creatures or the director robot. Any technological item within this radius is drained of 1d6 charges unless it succeeds at a DC 20 Reflex save. The save DCs are Intelligence-based.

**_Grasping Tentacles_ (Ex)** A director robot’s tentacles are primary attacks and have the _[[universal monster rules/Grab|grab]]_ special ability.

**Integrated Laser _Rifle_ (Ex)** A director robot has a built-in laser _rifle_. This weapon has a range of 150 feet and deals 2d6 points of fire damage on a hit. The weapon can fire once per round as a ranged touch attack. A laser attack can pass through force fields and force effects, such as a _[[spells/Wall Of Force|wall of force]]_, to strike a foe beyond without damaging that field. Objects like glass or other transparent barriers don’t provide cover from lasers, but unlike force barriers, a transparent physical barrier still takes damage when a laser passes through it. _[[conditions/Invisible|Invisible]]_ creatures and objects are immune to damage from lasers. Fog, smoke, and other clouds provide cover in addition to concealment from laser attacks. _[[spells/Darkness|Darkness]]_ (magical or otherwise) has no effect on lasers other than providing concealment.

**Override (Ex)** A director robot can usurp control of an otherwise functional robot. In order to gain control of a robot, the director robot must first make a ranged touch attack against a target robot within a range of 60 feet. If the attack is successful, the targeted robot must succeed at a DC 20 Will saving throw to prevent the director robot from linking to the target’s _[[spells/Command|command]]_ processor. On any subsequent turn after a link is established, the director robot can issue a _command_ to the targeted robot as a standard action. The targeted robot can attempt another Will save (DC 20) to resist following each _command_.

To _command_ its target, the director robot must be within 60 feet of the targeted robot and must issue the _command_ in a language the robot understands. The types of commands it can issue are similar to those allowed by a _[[spells/Suggestion|suggestion]]_ spell—once a _command_ is successfully issued, the robot does its best to carry out the orders over the course of the next hour. Additionally, any robot affected by this ability also gains a +2 competence bonus on attack and weapon damage rolls. These save DCs are Intelligence-based.

**Repair Robot (Ex)** As a standard action that doesn’t provoke an attack of opportunity, a director robot can repair damage done to either itself or an adjacent creature with the robot subtype, healing the target for 1d10 points of damage.

##### Description

No society endures without order, and among robots that order is enforced by directors. Clad in gleaming metal and viewing the world through a rotating array of lenses, a director is a robotic overseer designed to maximize efficiency and _command_ the loyalty of lesser automatons. Its torso rests upon a utilitarian egg-shaped pod loaded with manipulators, tools, and dozens of thin mechanical tendrils. Four long, mechanical legs support its bulk and carry it across any terrain, even allowing the robot to cling magnetically to vertical surfaces. While the upper frame sports human-like arms to manipulate traditional tools and weapons, two powerful tentacles extend from below its frame to facilitate combat and handle heavy lifting. Though its humanoid torso is barely larger than that of a human, the director’s entire frame stands over 10 feet tall and weighs nearly half a ton.