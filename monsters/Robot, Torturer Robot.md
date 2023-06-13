---
cssclass: [monsters]
title1: Robot, Torturer Robot
desc_short: Spinning blades, long needles, and crystal-tipped rods stud the surface
  of this hovering metallic sphere.
title2: Torturer Robot
CR: 8
sources:
- name: Numeria, Land of Fallen Stars
  page: 59
  link: http://paizo.com/products/btpy978l?Pathfinder-Campaign-Setting-Numeria-Land-of-Fallen-Stars
XP: 4800
alignment: N
size: Small
type: construct
subtypes:
- robot
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 23
  touch: 17
  flat_footed: 17
  components:
    dex: 5
    dodge: 1
    natural: 6
    size: 1
HP:
  HP: 105
  long: 10d10+10 plus 40-hp force field
saves:
  fort: 3
  ref: 8
  will: 5
defensive_abilities:
- all-around vision
- hardness 10
immunities:
- construct traits
weaknesses:
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 4 rotating blades +16 (1d4+5/18-20)
      entries:
      - - damage: 1d4+5
          crit_range: 18-20
      count: 4
      attack: rotating blades
      bonus:
      - 16
  ranged:
  - - text: 4 surgical lasers +16 touch (1d8/19-20 plus fire)
      entries:
      - - damage: 1d8
          crit_range: 19-20
        - effect: fire
      count: 4
      attack: surgical lasers
      bonus:
      - 16
      touch: true
  special:
  - agile
  - interrogate
  - nanosurgeon
ability_scores:
  STR: 8
  DEX: 21
  CON:
  INT: 10
  WIS: 15
  CHA: 1
BAB: 10
CMB: 8
CMD: 24
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Dodge
- name: Mobility
- name: Vital Strike
- name: Weapon Finesse
skills:
  Fly: 15
  Heal: 17
  Perception: 19
  Sense Motive: 19
  _racial_mods:
    Heal:
      _: 15
languages:
- Common
- Hallit
ecology:
  environment: any (Numeria)
  organization: solitary
  treasure_type: none
special_abilities:
  Agile (Ex): A torturer robot adds its Dexterity modifier to its damage rolls in
    place of its Strength modifier when using its rotating blades attack.
  Force Field (Ex): A field of shimmering energy surrounds a torturer robot. Damage
    dealt to the robot is applied to the force field first. As long as the field is
    active, the robot is immune to critical hits. The force field has fast healing
    8, but once the field's hit points are reduced to 0, the field collapses and does
    not reactive for 24 hours.
  Interrogate (Ex): As a standard action, the torturer robot can attempt a Heal check
    to deal 1d4 points of damage to an ability of its choice possessed by an adjacent,
    helpless target. A successful Fortitude saving throw with a DC equal to the robot's
    Heal check result negates this damage.
  Nanosurgeon (Ex): 'As a standard action, a torturer robot can inject purpose-programmed
    nanites into a target as a melee touch attack. The nanites produce one of the
    following effects or conditions (CL 10th, where applicable): cure serious wounds,
    lesser restoration, neutralize poison, remove disease, exhaustion, nauseated for
    1d4 rounds, or paralyzed (nauseated targets only, for remainder of original duration).
    If the victim succeeds at a DC 17 Fortitude saving throw, exhaustion is reduced
    to fatigue, nauseated is reduced to sickened, and other effects are negated. The
    torturer robot carries 5 doses of nanites, and it constructs replacements at a
    rate of 1 dose per hour. The save DC is Wisdom-based.'
  Surgical Lasers (Ex): The torturer robot's lasers have a range of 50 feet with no
    range increment, and threaten a critical hit on a 19 or 20. Lasers pass through
    transparent creatures and objects without causing harm (including force fields,
    force effects, and invisible creatures; it can pass through glass, but the glass
    takes damage), and can strike targets behind them normally. Fog, smoke, and other
    clouds provide cover in addition to concealment from laser attacks.
desc_long: Torturer robots, nicknamed “murderballs” by enemies of the Technic League,
  were built to extract information from prisoners. Murderballs administer pain in
  a detached fashion, repeating questions over and over while their heuristic programming
  analyzes the truth and completeness of responses. Their job demands detailed knowledge
  of human anatomy and the capacity to revive a dying patient, leading some to serve
  double-duty as field medics and surgeons.

---

# Robot, Torturer Robot
Spinning blades, long needles, and crystal-tipped rods stud the surface of this hovering metallic sphere.
**Source** Numeria, Land of _[[monsters/Fallen|Fallen]]_ Stars pg. 59
**XP** 4,800

N Small construct (robot)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 Dex, +1 dodge, +6 natural, +1 size)
**hp** 105 (10d10+10 plus 40-hp force field)
**Fort** +3, **Ref** +8, **Will** +5
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 4 rotating blades +16 (1d4+5/18–20)
**Ranged** 4 surgical lasers +16 touch (1d8/19–20 plus fire)
**Special Attacks** _[[items/Weapon Magic Abilities/Agile|agile]]_, interrogate, nanosurgeon

##### Statistics
**Str** 8, **Dex** 21, **Con** —, **Int** 10, **Wis** 15, **Cha** 1
**Base Atk** +10; **CMB** +8; **CMD** 24 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Fly +15, _[[spells/Heal|Heal]]_ +17, Perception +19, Sense Motive +19; **Racial Modifiers** +15 _Heal_
**Languages** Common, Hallit

##### Ecology

**Environment** any (Numeria)
**Organization** solitary
**Treasure** none

### Special Abilities

**_Agile_ (Ex)** A torturer robot adds its Dexterity modifier to its damage rolls in place of its Strength modifier when using its rotating blades attack.

**Force Field (Ex)** A field of shimmering energy surrounds a torturer robot. Damage dealt to the robot is applied to the force field first. As long as the field is active, the robot is immune to critical hits. The force field has _[[universal monster rules/Fast Healing|fast healing]]_ 8, but once the field’s hit points are reduced to 0, the field collapses and does not reactive for 24 hours.

**Interrogate (Ex)** As a standard action, the torturer robot can attempt a _Heal_ check to deal 1d4 points of damage to an ability of its choice possessed by an adjacent, _[[conditions/Helpless|helpless]]_ target. A successful Fortitude saving throw with a DC equal to the robot’s _Heal_ check result negates this damage.

**Nanosurgeon (Ex)** As a standard action, a torturer robot can inject purpose-programmed nanites into a target as a melee touch attack. The nanites produce one of the following effects or conditions (CL 10th, where applicable): _[[spells/Cure Serious Wounds|cure serious wounds]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Disease|remove disease]]_, exhaustion, _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds, or _[[conditions/Paralyzed|paralyzed]]_ (_nauseated_ targets only, for remainder of original duration). If the victim succeeds at a DC 17 Fortitude saving throw, exhaustion is reduced to fatigue, _nauseated_ is reduced to _[[conditions/Sickened|sickened]]_, and other effects are negated. The torturer robot carries 5 doses of nanites, and it constructs replacements at a rate of 1 dose per hour. The save DC is Wisdom-based.
**Surgical Lasers (Ex)** The torturer robot’s lasers have a range of 50 feet with no range increment, and threaten a critical hit on a 19 or 20. Lasers pass through transparent creatures and objects without causing _[[spells/Harm|harm]]_ (including force fields, force effects, and _[[conditions/Invisible|invisible]]_ creatures; it can pass through glass, but the glass takes damage), and can strike targets behind them normally. Fog, smoke, and other clouds provide cover in addition to concealment from laser attacks.

##### Description

Torturer robots, nicknamed “murderballs” by enemies of the Technic League, were built to extract information from prisoners. Murderballs administer pain in a detached fashion, repeating questions over and over while their heuristic programming analyzes the truth and completeness of responses. Their job demands detailed knowledge of human anatomy and the capacity to revive a _[[conditions/Dying|dying]]_ patient, leading some to serve double-duty as field medics and surgeons.