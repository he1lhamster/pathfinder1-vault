---
cssclass: [monsters]
title1: Robot, Observer Robot
desc_short: This small robot is reminiscent of a beetle with a pair of pincers extending
  from the front of its body.
title2: Observer Robot
CR: 2
sources:
- name: 'Pathfinder #86: Lords of Rust'
  page: 88
  link: http://paizo.com/products/btpy97az?Pathfinder-Adventure-Path-86-Lords-of-Rust
XP: 600
alignment: N
size: Tiny
type: construct
subtypes:
- robot
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 18
  touch: 14
  flat_footed: 16
  components:
    dex: 2
    natural: 4
    size: 2
HP:
  HP: 16
  long: 3d10
saves:
  fort: 1
  ref: 5
  will: 4
defensive_abilities:
- all-around vision
- hardness 5
immunities:
- construct traits
weaknesses:
- vulnerable to critical hits and electricity
speeds:
  base: 20
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +6 (1d2+1)
      entries:
      - - damage: 1d2+1
      count: 2
      attack: claws
      bonus:
      - 6
    - text: integrated laser torch +6 (1d10)
      entries:
      - - damage: 1d10
      attack: integrated laser torch
      bonus:
      - 6
  ranged:
  - - text: integrated stun gun +7 (1d8 plus nonlethal)
      entries:
      - - damage: 1d8
        - effect: nonlethal
      attack: integrated stun gun
      bonus:
      - 7
  special:
  - integrated laser torch
  - integrated stun gun
space: 2.5
reach: 0
reach_other: 5 ft. with integrated laser torch
ability_scores:
  STR: 12
  DEX: 15
  CON:
  INT: 10
  WIS: 17
  CHA: 1
BAB: 3
CMB: 3
CMD: 14
CMD_other: 22 vs. trip
feats:
- name: Alertness
- name: Lightning Reflexes
skills:
  Fly: 14
  Perception: 15
  Sense Motive: 5
  Stealth: 11
  Survival: 5
  _racial_mods:
    Perception:
      _: 4
languages:
- Androffan
- Common
special_qualities:
- camouflage
- transmit senses
ecology:
  environment: any (Numeria)
  organization: solitary or deployment (2-12)
  treasure_type: none
special_abilities:
  Camouflage (Ex): An observer robot's outer shell contains color-shifting screens
    that allow the creature to blend into any background. Though not truly invisible,
    they are hard to pinpoint. While using this ability, an observer robot gains a
    +8 racial bonus on Stealth checks and has concealment from creatures more than
    5 feet away.
  Integrated Laser Torch (Ex): An observer robot is outfitted with an integrated laser
    torch used to bypass barriers or restraints. When activated, the torch emits a
    beam of highly focused light, cutting and burning through surfaces up to 6 inches
    away. Attacks from a laser torch resolve as touch attacks and deal 1d10 points
    of fire damage. This damage is not modified further by Strength. An observer robot's
    integrated laser torch is mounted on an extending arm that allows it greater reach.
    When the laser torch is used as a tool or as a weapon to sunder, its damage bypasses
    hardness up to 20 points, and damage is not halved (as is normally the case for
    energy damage applied to objects) unless the object is particularly fire-resistant.
    A laser torch's cutting beam passes through force fields and force effects without
    damaging the field. Invisible objects and creatures can't be harmed by a laser
    torch.
  Integrated Stun Gun (Ex): An observer robot has an integrated stun gun built into
    its head. This weapon uses a sonic amplifier to produce powerful low-frequency
    blasts of energy that can pummel targets. This weapon has a range increment of
    20 feet, and it deals 1d8 points of nonlethal damage. When it scores a critical
    hit, the robot can attempt a free trip combat maneuver (CMB +13) against the target,
    which does not provoke attacks of opportunity.
  Transmit Senses (Ex): An observer robot is outfitted with a number of sensors, cameras,
    and microphones that allow it to record events and transmit them to another location.
    An observer robot can record up to 12 hours of audio and video. An observer robot's
    communications can be keyed to a commsetTG or other similar device, and it can
    broadcast everything it can see or hear to this device as long as it is within
    1 mile. The signal strength can be enhanced with a signal boosterTG. An observer
    robot can also transmit its senses to another observer robot. A signal has difficulty
    penetrating solid barriers. A signal is blocked by 1 foot of metal, 5 feet of
    stone, or 20 feet of organic matter. Force fields do not block signals. Broadcasting
    functions like a scrying sensor, allowing the viewer to hear and see what the
    observer robot is experiencing. The viewer gains the benefits of any nonmagical
    special abilities the observer robot has tied to its senses (such as low-light
    vision), but the viewer uses her own Perception skill. This ability doesn't allow
    magically or supernaturally enhanced senses to work through it, even if both the
    observer robot and the viewer possess them.
desc_long: |-
  Designed for reconnaissance, observer robots are deployed to serve as the eyes and ears of their controllers. Because they're intelligent and able to make their own decisions, observer robots are suited for exploring without supervision, recording their observations so that they can relay the images and sounds to their creators. The outer hull of an observer robot and its wings are covered in a network of tiny screens that can display images of the robots' surroundings, which grants the observer robot a form of camouflage that allows it to clandestinely observe its subjects.

  The statistics above represent the most common observer robots, but some models have enhanced senses that allow them to see in darkness or see invisible creatures. Some even have olfactory sensors that effectively smell their environment and test the surrounding air for impurities that would harm their creators. Observer robots deployed in hostile environments might be outfitted with more formidable weaponry than the standard stun gun and laser torch.

  An observer robot is approximately 20 inches long and weighs 8 pounds.

---

# Robot, Observer Robot
This small robot is reminiscent of a beetle with a pair of pincers extending from the front of its body.
**Source** Pathfinder #86: Lords of Rust pg. 88
**XP** 600

N Tiny construct (robot)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 Dex, +4 natural, +2 size)
**hp** 16 (3d10)
**Fort** +1, **Ref** +5, **Will** +4
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, hardness 5; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to critical hits and electricity

##### Offense
**Speed** 20 ft., fly 60 ft. (perfect)
**Melee** 2 claws +6 (1d2+1), integrated laser _[[items/Mundane/Torch|torch]]_ +6 (1d10)
**Ranged** integrated stun gun +7 (1d8 plus nonlethal)
**Space** 2 1/2 ft., **Reach** 0 ft. (5 ft. with integrated laser _torch_)
**Special Attacks** integrated laser _torch_, integrated stun gun

##### Statistics
**Str** 12, **Dex** 15, **Con** —, **Int** 10, **Wis** 17, **Cha** 1
**Base Atk** +3; **CMB** +3; **CMD** 14 (22 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Fly +14, Perception +15, Sense Motive +5, Stealth +11, Survival +5; **Racial Modifiers** +4 Perception
**Languages** Androffan, Common
**SQ** camouflage, transmit senses

##### Ecology

**Environment** any (Numeria)
**Organization** solitary or deployment (2–12)
**Treasure** none

### Special Abilities

**Camouflage (Ex)** An observer robot’s outer shell contains color-shifting screens that allow the creature to _[[spells/Blend|blend]]_ into any background. Though not truly _[[conditions/Invisible|invisible]]_, they are hard to pinpoint. While using this ability, an observer robot gains a +8 racial bonus on Stealth checks and has concealment from creatures more than 5 feet away.

**Integrated Laser _Torch_ (Ex)** An observer robot is outfitted with an integrated laser _torch_ used to bypass barriers or restraints. When activated, the _torch_ emits a beam of highly focused light, cutting and _[[items/Weapon Magic Abilities/Burning|burning]]_ through surfaces up to 6 inches away. Attacks from a laser _torch_ resolve as touch attacks and deal 1d10 points of fire damage. This damage is not modified further by Strength. An observer robot’s integrated laser _torch_ is mounted on an extending arm that allows it greater reach. When the laser _torch_ is used as a tool or as a weapon to sunder, its damage bypasses hardness up to 20 points, and damage is not halved (as is normally the case for energy damage applied to objects) unless the object is particularly fire-resistant. A laser _torch_’s cutting beam passes through force fields and force effects without damaging the field. _Invisible_ objects and creatures can’t be harmed by a laser _torch_.

**Integrated Stun Gun (Ex)** An observer robot has an integrated stun gun built into its head. This weapon uses a sonic amplifier to produce powerful low-frequency blasts of energy that can pummel targets. This weapon has a range increment of 20 feet, and it deals 1d8 points of nonlethal damage. When it scores a critical hit, the robot can attempt a free _trip_ combat maneuver (CMB +13) against the target, which does not provoke attacks of opportunity.

**Transmit Senses (Ex)** An observer robot is outfitted with a number of sensors, cameras, and microphones that allow it to record events and transmit them to another location. An observer robot can record up to 12 hours of audio and video. An observer robot’s communications can be keyed to a commset or other similar device, and it can broadcast everything it can see or hear to this device as long as it is within 1 mile. The signal strength can be enhanced with a signal booster. An observer robot can also transmit its senses to another observer robot. A signal has difficulty penetrating solid barriers. A signal is blocked by 1 foot of metal, 5 feet of stone, or 20 feet of organic matter. Force fields do not block signals. Broadcasting functions like a _[[spells/Scrying|scrying]]_ sensor, allowing the viewer to hear and see what the observer robot is experiencing. The viewer gains the benefits of any nonmagical special abilities the observer robot has tied to its senses (such as _low-light vision_), but the viewer uses her own Perception skill. This ability doesn’t allow magically or supernaturally enhanced senses to work through it, even if both the observer robot and the viewer possess them.

##### Description

Designed for reconnaissance, observer robots are deployed to serve as the eyes and ears of their controllers. Because they’re intelligent and able to make their own decisions, observer robots are suited for exploring without supervision, recording their observations so that they can relay the images and sounds to their creators. The outer hull of an observer robot and its wings are covered in a network of tiny screens that can display images of the robots’ surroundings, which grants the observer robot a form of camouflage that allows it to clandestinely observe its subjects.

The statistics above represent the most common observer robots, but some models have enhanced senses that allow them to _[[universal monster rules/See in Darkness|see in darkness]]_ or see _invisible_ creatures. Some even have olfactory sensors that effectively smell their environment and test the surrounding air for impurities that would _[[spells/Harm|harm]]_ their creators. Observer robots deployed in hostile environments might be outfitted with more formidable weaponry than the standard stun gun and laser _torch_.

An observer robot is approximately 20 inches long and weighs 8 pounds.