---
cssclass: [monsters]
title1: Robot, Surgeon Robot
desc_short: This robot has the general appearance of a skeletal preying mantis fashioned
  entirely from gleaming metal. An array of limbs fitted with laser scalpels, syringes,
  and other surgical devices spring from its body.
title2: Surgeon Robot
CR: 14
sources:
- name: 'Pathfinder #89: Palace of Fallen Stars'
  page: 90
  link: http://paizo.com/products/btpy99si?Pathfinder-Adventure-Path-89-Palace-of-Fallen-Stars
XP: 38400
alignment: N
size: Medium
type: construct
subtypes:
- robot
initiative:
  bonus: 11
senses:
  darkvision: 60
  low-light vision: true
  superior optics: true
AC:
  AC: 27
  touch: 17
  flat_footed: 20
  components:
    dex: 7
    natural: 10
HP:
  HP: 254
  long: 18d10+80 plus 75 hp force field
saves:
  fort: 6
  ref: 13
  will: 7
defensive_abilities:
- hardness 10
immunities:
- construct traits
weaknesses:
- vulnerable to critical hits and electricity
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +25 (1d6+6 plus grab)
      entries:
      - - damage: 1d6+6
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 25
    - text: 4 scalpels +25 (1d6+6/19-20)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
      count: 4
      attack: scalpels
      bonus:
      - 25
    - text: syringe +25 (1d4+6/19-20 plus poison)
      entries:
      - - damage: 1d4+6
          crit_range: 19-20
        - effect: poison
      attack: syringe
      bonus:
      - 25
  ranged:
  - - text: integrated surgical laser +25 touch (1d6 fire/19-20)
      entries:
      - - damage: 1d6
          type: fire
          crit_range: 19-20
      attack: integrated surgical laser
      bonus:
      - 25
      touch: true
  special:
  - constrict (1d6+9)
  - sneak attack +3d6
  - syringe
ability_scores:
  STR: 22
  DEX: 25
  CON:
  INT: 14
  WIS: 13
  CHA: 1
BAB: 18
CMB: 24
CMD: 41
CMD_other: 45 vs. trip
feats:
- name: Bleeding Critical
- name: Blinding Critical
- name: Critical Focus
- name: Improved Critical (integrated surgical laser)
- name: Improved Critical (scalpel)
- name: Improved Critical (syringe)
- name: Improved Initiative
- name: Vital Strike
- name: Weapon Finesse
skills:
  Disable Device: 11
  Heal: 27
  Knowledge (engineering): 15
  Knowledge (local): 15
  Knowledge (nature): 15
  Perception: 22
  Sense Motive: 9
  _racial_mods:
    Heal:
      _: 8
languages:
- Androffan
- Common
- Hallit
special_qualities:
- master surgeon
- specialized programming
ecology:
  environment: any (Numeria)
  organization: solitary or team (2-6)
  treasure_type: none
special_abilities:
  Force Field (Ex): A surgeon robot is sheathed in a thin layer of shimmering energy
    that grants it 75 bonus hit points. All damage dealt to a surgeon robot with an
    active force field is deducted from these hit points first. As long as the force
    field is active, the surgeon robot is immune to critical hits. A surgeon robot's
    force field has fast healing 15, but once these bonus hit points are reduced to
    0, the force field shuts down and doesn't reactivate for 24 hours.
  Master Surgeon (Ex): 'Programmed to execute advanced medical procedures, a surgeon
    robot can perform surgeries and other procedures that heal humanoid creatures
    of all manner of maladies. A surgeon robot can heal wounds, set broken bones,
    cure diseases, treat burns, remove poison, and even install cybertech items. These
    procedures take varying amounts of time for the surgeon robot to complete and
    require different Heal check DCs. The DCs for these surgical procedures increase
    by 10 when they're performed on a non-humanoid creature. These procedures leave
    the patient with the exhausted condition. If the surgeon robot fails any of its
    Heal checks, the surgery fails and the patient takes 1d4 points of Constitution
    damage and is exhausted for 24 hours. The procedures a surgeon robot can perform
    are as follows: Cure Blindness/Deafness (DC 35): The patient's sight or hearing
    is restored. Required Time: 30 minutes.Install Cybertech (DC = 5 + the cybertech
    install DC): Cybernetic equipment is installed safely. Required Time: 20 minutes
    per point of implantation of the cybertech being installed.Minor Surgery (DC 25):
    The patient is healed of 1d8+1 points of damage. Required Time: 5 minutes.Moderate
    Surgery (DC 30): The patient is healed of 2d8+3 points of damage and 1d4+1 points
    of ability damage to a selected ability score. Required Time: 10 minutes.Major
    Surgery (DC 35): The patient is healed of 3d8+5 points of damage and is cured
    of blindness and deafness. Required Time: 15 minutes.Critical Surgery (DC 40):
    The patient is healed of 4d8+7 points of damage and either all ability damage
    to all ability scores or all ability drain to one ability score. Required Time:
    30 minutes.Treat Toxin (DC = 10 + the save DC of disease or poison): One disease
    or poison currently afflicting the patient is removed. Required Time: 10 minutes.'
  Specialized Programming (Ex): Heal is always a class skill for surgeon robots, and
    they gain a +8 racial bonus on Heal checks.
  Superior Optics (Ex): Surgeon robots see invisible creatures or objects as if they
    were visible.
  Syringe (Ex): 'When a surgeon robot makes a successful attack with its syringe,
    it can inject the target with pharmaceuticals. The robot contains nanites that
    fabricate the pharmaceuticals stored within its body. Up to 10 doses of these
    pharmaceuticals can be administered per day. The surgeon robot can choose to affect
    its target with cardioamp, cureall, hemochem (grade III), torpinal, or zortaphen
    each time it uses this ability. Rules for these pharmaceuticals can be found on
    pages 33-34 of Pathfinder Campaign Setting: Technology Guide.'
desc_long: These large, insectoid-looking robots were designed to perform incredibly
  complicated surgeries with flawless results. Possessing a data bank filled with
  advanced surgical techniques, these robots produce nearly supernatural effects,
  and the recovery time from their procedures is often nothing short of miraculous.
  These robots were originally stationed on Divinity to care for the humanoid crew
  of the ship during their long voyage, and some were even employed to treat the aliens
  the ship collected during its journey. Surgeon robots stand 7 feet tall and weigh
  a bit more than 600 pounds.

---

# Robot, Surgeon Robot
This robot has the general appearance of a skeletal preying mantis fashioned entirely from gleaming metal. An array of limbs fitted with laser scalpels, syringes, and other surgical devices spring from its body.
**Source** Pathfinder #89: Palace of _[[monsters/Fallen|Fallen]]_ Stars pg. 90
**XP** 38,400

N Medium construct (robot)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, superior optics; Perception +22

##### Defense

**AC** 27, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 Dex, +10 natural)
**hp** 254 (18d10+80 plus 75 hp force field)
**Fort** +6, **Ref** +13, **Will** +7
**Defensive Abilities** hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to critical hits and electricity

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 claws +25 (1d6+6 plus _[[universal monster rules/Grab|grab]]_), 4 scalpels +25 (1d6+6/19–20), syringe +25 (1d4+6/19–20 plus poison)
**Ranged** integrated surgical laser +25 touch (1d6 fire/19–20)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d6+9), sneak attack +3d6, syringe

##### Statistics
**Str** 22, **Dex** 25, **Con** —, **Int** 14, **Wis** 13, **Cha** 1
**Base Atk** +18; **CMB** +24; **CMD** 41 (45 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (integrated surgical laser), _Improved Critical_ (scalpel), _Improved Critical_ (syringe), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Disable Device +11, _[[spells/Heal|Heal]]_ +27, Knowledge (engineering) +15, Knowledge (local) +15, Knowledge (nature) +15, Perception +22, Sense Motive +9; **Racial Modifiers** +8 _Heal_
**Languages** Androffan, Common, Hallit
**SQ** master surgeon, specialized programming

##### Ecology

**Environment** any (Numeria)
**Organization** solitary or team (2–6)
**Treasure** none

### Special Abilities

**Force Field (Ex)** A surgeon robot is sheathed in a thin layer of shimmering energy that grants it 75 bonus hit points. All damage dealt to a surgeon robot with an active force field is deducted from these hit points first. As long as the force field is active, the surgeon robot is immune to critical hits. A surgeon robot’s force field has _[[universal monster rules/Fast Healing|fast healing]]_ 15, but once these bonus hit points are reduced to 0, the force field shuts down and doesn’t reactivate for 24 hours.

**Master Surgeon (Ex)** Programmed to execute advanced medical procedures, a surgeon robot can perform surgeries and other procedures that _heal_ humanoid creatures of all manner of maladies. A surgeon robot can _heal_ wounds, set _[[conditions/Broken|broken]]_ bones, cure diseases, treat burns, remove poison, and even install cybertech items. These procedures take varying amounts of time for the surgeon robot to complete and require different _Heal_ check DCs. The DCs for these surgical procedures increase by 10 when they’re performed on a non-humanoid creature. These procedures leave the patient with the _[[conditions/Exhausted|exhausted]]_ condition. If the surgeon robot fails any of its _Heal_ checks, the surgery fails and the patient takes 1d4 points of Constitution damage and is _exhausted_ for 24 hours. The procedures a surgeon robot can perform are as follows:

* Cure Blindness/Deafness (DC 35): The patient’s sight or hearing is restored. Required Time: 30 minutes.
* Install Cybertech (DC = 5 + the cybertech install DC): Cybernetic equipment is installed safely. Required Time: 20 minutes per point of implantation of the cybertech being installed.
* Minor Surgery (DC 25): The patient is healed of 1d8+1 points of damage. Required Time: 5 minutes.
* Moderate Surgery (DC 30): The patient is healed of 2d8+3 points of damage and 1d4+1 points of ability damage to a selected ability score. Required Time: 10 minutes.
* Major Surgery (DC 35): The patient is healed of 3d8+5 points of damage and is cured of blindness and deafness. Required Time: 15 minutes.
* Critical Surgery (DC 40): The patient is healed of 4d8+7 points of damage and either all ability damage to all ability scores or all ability drain to one ability score. Required Time: 30 minutes.
* Treat Toxin (DC = 10 + the save DC of disease or poison): One disease or poison currently afflicting the patient is removed. Required Time: 10 minutes.
**Specialized Programming (Ex)** _Heal_ is always a class skill for surgeon robots, and they gain a +8 racial bonus on _Heal_ checks.
**Superior Optics (Ex)** Surgeon robots see _[[conditions/Invisible|invisible]]_ creatures or objects as if they were visible.
**Syringe (Ex)** When a surgeon robot makes a successful attack with its syringe, it can inject the target with pharmaceuticals. The robot contains nanites that _[[spells/Fabricate|fabricate]]_ the pharmaceuticals stored within its body. Up to 10 doses of these pharmaceuticals can be administered per day. The surgeon robot can choose to affect its target with cardioamp, cureall, hemochem (grade III), torpinal, or zortaphen each time it uses this ability. Rules for these pharmaceuticals can be found on pages 33–34 of Pathfinder Campaign Setting: Technology Guide.

##### Description

These large, insectoid-looking robots were designed to perform incredibly complicated surgeries with flawless results. Possessing a data bank filled with advanced surgical techniques, these robots produce nearly supernatural effects, and the recovery time from their procedures is often nothing short of miraculous. These robots were originally stationed on Divinity to care for the humanoid crew of the ship during their long voyage, and some were even employed to treat the aliens the ship collected during its journey. Surgeon robots stand 7 feet tall and weigh a bit more than 600 pounds.