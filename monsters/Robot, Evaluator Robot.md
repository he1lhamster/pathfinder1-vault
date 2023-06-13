---
cssclass: [monsters]
title1: Robot, Evaluator Robot
desc_short: With wings and an unearthly glow, this mechanical being could easily be
  mistaken for an angel.
title2: Evaluator Robot
CR: 12
sources:
- name: 'Pathfinder #90: The Divinity Drive'
  page: 90
  link: http://paizo.com/products/btpy95bw?Pathfinder-Adventure-Path-90-The-Divinity-Drive
XP: 19200
alignment: N
size: Medium
type: construct
subtypes:
- robot
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  superior optics: true
AC:
  AC: 27
  touch: 15
  flat_footed: 22
  components:
    dex: 5
    natural: 12
HP:
  HP: 158
  long: 16d10+20 plus 50 hp force field
saves:
  fort: 5
  ref: 10
  will: 10
defensive_abilities:
- hardness 10
immunities:
- construct traits
speeds:
  base: 50
  fly: 120
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bastard sword +22/+17/+12/+7 (1d10+6/19-20 plus stun)
      entries:
      - - damage: 1d10+6
          crit_range: 19-20
        - effect: stun
      attack: bastard sword
      bonus:
      - 22
      - 17
      - 12
      - 7
  - - text: 2 slams +22 (1d4+6 plus stun)
      entries:
      - - damage: 1d4+6
        - effect: stun
      count: 2
      attack: slams
      bonus:
      - 22
  ranged:
  - - text: integrated laser rifle +21 ranged touch (4d6 fire)
      entries:
      - - damage: 4d6
          type: fire
      attack: integrated laser rifle
      bonus:
      - 21
      touch: true
  special:
  - memory wipe
  - stun (DC 19, 1d4 rounds)
ability_scores:
  STR: 22
  DEX: 21
  CON:
  INT: 12
  WIS: 17
  CHA: 1
BAB: 16
CMB: 22
CMD: 37
feats:
- name: Blind-Fight
- name: Cleave
- name: Flyby Attack
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Skill Focus (Sense Motive)
- name: Vital Strike
skills:
  Fly: 17
  Knowledge (local): 12
  Perception: 18
  Sense Motive: 25
  Stealth: 10
languages:
- Androffan
- Common
- process languages
ecology:
  environment: any (Numeria)
  organization: solitary
  treasure_type: none
special_abilities:
  Force Field (Ex): An evaluator robot is sheathed in a thin layer of shimmering energy
    that grants it 50 bonus hit points. All damage dealt to an evaluator robot with
    an active force field is deducted from these hit points first. As long as the
    force field is active, the evaluator robot is immune to critical hits. An evaluator
    robot's force field has fast healing 10, but once these hit points are reduced
    to 0, the force field shuts down and does not reactivate for 24 hours.
  Integrated Laser Rifle (Ex): An evaluator robot has a built-in laser rifle. This
    weapon has a range of 150 feet and deals 4d6 points of fire damage on a hit. The
    weapon can fire once per round as a ranged touch attack. A laser attack can pass
    through force fields and force effects, such as a wall of force, to strike a foe
    beyond without damaging that field. Objects like glass or other transparent barriers
    don't provide cover from lasers, but unlike force barriers, a transparent physical
    barrier still takes damage when a laser passes through it. Invisible creatures
    and objects are immune to damage from lasers. Fog, smoke, and other clouds provide
    cover in addition to concealment from laser attacks. Darkness (magical or otherwise)
    has no effect on lasers other than providing concealment.
  Memory Wipe (Ex): As a standard action, an evaluator robot can make a touch attack
    that, if it hits, injects nanites into a target and erases the last 12 hours of
    its memories. A successful DC 19 Will save negates this effect. This is a mind-affecting
    effect, and the save DC is Intelligence-based.
  Process Languages (Ex): Exceptional processing and data stores allows an evaluator
    robot to parse language in a way that lets it permanently speak and understand
    any spoken or written language it observes for at least 1 minute.
  Stun (Ex): An evaluator robot's melee attacks deliver a nonlethal jolt of electricity
    with each strike. If the robot strikes a creature twice in one round with its
    bastard sword or slam attack, that target must succeed at a DC 19 Fortitude save
    or be stunned for 1d4 rounds. The save DC is Intelligence-based.
  Superior Optics (Ex): An evaluator robot can see invisible creatures or objects
    as if they were visible.
desc_long: |-
  Androffans, the race responsible for the presence of robots on Golarion, were a spacefaring people who visited dozens of worlds. Masters of engineering, they created robots that could perform a wide array of tasks, even trusting their creations to perform complex surgeries on the Androffans' own organic forms. In the course of their interplanetary explorations, the Androffans quickly learned that not every world was ready to comprehend the awesome experience of leaving one's home planet to visit others. Not wanting to risk valuable crew members, the Androffans created evaluator robots as an alternative to sending a shuttle mission to alien planets and interacting in person. When sensors aboard Androffan ships orbiting foreign worlds discovered other humanoid species, evaluator robots would be dispatched to assess the planets' alien cultures.

  Taking forms designed to be recognizable to a planet's general populace, evaluator robots would drop from orbiting surveillance ships onto alien worlds to collect data so that their masters could determine the readiness of the planets' inhabitants to accept the existence of creatures from other worlds. Androffans also used evaluator robots to determine how violent or superstitious the indigenous populations were so that they could carefully plan direct contact. Evaluator robots were fashioned into pleasing and majestic forms to command respect and admiration from the humanoids they interacted with, and were usually made slightly taller than the planet's primary race so as to seem properly impressive. These robots' advanced construction utilizes sophisticated lightweight materials, making their durable frames weigh in under 400 pounds. The model presented here is the most common design-a radiant humanoid angel with gleaming feathers of brushed metal.

---

# Robot, Evaluator Robot
With wings and an unearthly glow, this mechanical being could easily be mistaken for an angel.
**Source** Pathfinder #90: The Divinity Drive pg. 90
**XP** 19,200

N Medium construct (robot)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, superior optics; Perception +18

##### Defense

**AC** 27, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+5 Dex, +12 natural)
**hp** 158 (16d10+20 plus 50 hp force field)
**Fort** +5, **Ref** +10, **Will** +10
**Defensive Abilities** hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** 50 ft., fly 120 ft. (perfect)
**Melee** _[[items/Weapon/Bastard sword|bastard sword]]_ +22/+17/+12/+7 (1d10+6/19–20 plus stun) or 2 slams +22 (1d4+6 plus stun)
**Ranged** integrated laser _[[items/Weapon/Rifle|rifle]]_ +21 ranged touch (4d6 fire)
**Special Attacks** memory wipe, stun (DC 19, 1d4 rounds)

##### Statistics
**Str** 22, **Dex** 21, **Con** —, **Int** 12, **Wis** 17, **Cha** 1
**Base Atk** +16; **CMB** +22; **CMD** 37
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Sense Motive), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +17, Knowledge (local) +12, Perception +18, Sense Motive +25, Stealth +10
**Languages** Androffan, Common; process languages

##### Ecology

**Environment** any (Numeria)
**Organization** solitary
**Treasure** none

### Special Abilities

**Force Field (Ex)** An evaluator robot is sheathed in a thin layer of shimmering energy that grants it 50 bonus hit points. All damage dealt to an evaluator robot with an active force field is deducted from these hit points first. As long as the force field is active, the evaluator robot is immune to critical hits. An evaluator robot’s force field has _[[universal monster rules/Fast Healing|fast healing]]_ 10, but once these hit points are reduced to 0, the force field shuts down and does not reactivate for 24 hours.

**Integrated Laser _Rifle_ (Ex)** An evaluator robot has a built-in laser _rifle_. This weapon has a range of 150 feet and deals 4d6 points of fire damage on a hit. The weapon can fire once per round as a ranged touch attack. A laser attack can pass through force fields and force effects, such as a _[[spells/Wall Of Force|wall of force]]_, to strike a foe beyond without damaging that field. Objects like glass or other transparent barriers don’t provide cover from lasers, but unlike force barriers, a transparent physical barrier still takes damage when a laser passes through it. _[[conditions/Invisible|Invisible]]_ creatures and objects are immune to damage from lasers. Fog, smoke, and other clouds provide cover in addition to concealment from laser attacks. _[[spells/Darkness|Darkness]]_ (magical or otherwise) has no effect on lasers other than providing concealment.

**Memory Wipe (Ex)** As a standard action, an evaluator robot can make a touch attack that, if it hits, injects nanites into a target and erases the last 12 hours of its memories. A successful DC 19 Will save negates this effect. This is a mind-affecting effect, and the save DC is Intelligence-based.

**Process Languages (Ex)** Exceptional processing and data stores allows an evaluator robot to parse language in a way that lets it permanently speak and understand any spoken or written language it observes for at least 1 minute.
**Stun (Ex)** An evaluator robot’s melee attacks deliver a nonlethal _[[spells/Jolt|jolt]]_ of electricity with each strike. If the robot strikes a creature twice in one round with its _bastard sword_ or slam attack, that target must succeed at a DC 19 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1d4 rounds. The save DC is Intelligence-based.
**Superior Optics (Ex)** An evaluator robot can see _invisible_ creatures or objects as if they were visible.

##### Description

Androffans, the race responsible for the presence of robots on Golarion, were a spacefaring people who visited dozens of worlds. Masters of engineering, they created robots that could perform a wide array of tasks, even trusting their creations to perform complex surgeries on the Androffans’ own organic forms. In the course of their interplanetary explorations, the Androffans quickly learned that not every world was ready to comprehend the awesome experience of leaving one’s home planet to visit others. Not wanting to risk valuable crew members, the Androffans created evaluator robots as an alternative to _[[spells/Sending|sending]]_ a shuttle mission to alien planets and interacting in person. When sensors aboard Androffan ships orbiting foreign worlds discovered other humanoid species, evaluator robots would be dispatched to assess the planets’ alien cultures.

Taking forms designed to be recognizable to a planet’s general populace, evaluator robots would drop from orbiting surveillance ships onto alien worlds to collect data so that their masters could determine the readiness of the planets’ inhabitants to accept the existence of creatures from other worlds. Androffans also used evaluator robots to determine how violent or superstitious the indigenous populations were so that they could carefully plan direct contact. Evaluator robots were fashioned into pleasing and majestic forms to _[[spells/Command|command]]_ respect and admiration from the humanoids they interacted with, and were usually made slightly taller than the planet’s primary race so as to seem properly impressive. These robots’ advanced construction utilizes sophisticated lightweight materials, making their durable frames weigh in under 400 pounds. The model presented here is the most common design—a _[[items/Armor Magic Abilities/Radiant|radiant]]_ humanoid angel with gleaming feathers of brushed metal.