---
cssclass: [monsters]
title1: Troll, Canopy Troll
desc_short: Prominent tusks and unruly green fur mark this fearsome creature as a
  troll despite its small size. It hangs overhead, swinging between its oversized
  forearms and lashing, claw-tipped tail.
title2: Canopy Troll
CR: 3
sources:
- name: 'Pathfinder #116: Fangs of War'
  page: 90
  link: http://paizo.com/products/btpy9npk
XP: 800
alignment: CE
size: Small
type: humanoid
subtypes:
- giant
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 15
  touch: 15
  flat_footed: 11
  components:
    dex: 4
    size: 1
HP:
  HP: 30
  long: 4d8+12
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 7
  ref: 5
  will: 2
speeds:
  base: 20
  climb: 30
attacks:
  melee:
  - - text: bite +5 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 5
    - text: 2 claws +5 (1d3+1)
      entries:
      - - damage: 1d3+1
      count: 2
      attack: claws
      bonus:
      - 5
    - text: sting +5 (1d3+1 plus poison)
      entries:
      - - damage: 1d3+1
        - effect: poison
      attack: sting
      bonus:
      - 5
  special:
  - poison
  - swarming
space: 5
reach: 5
reach_other: 10 ft. with sting
ability_scores:
  STR: 12
  DEX: 18
  CON: 17
  INT: 4
  WIS: 9
  CHA: 7
BAB: 3
CMB: 3
CMB_other: +6 grapple
CMD: 17
CMD_other: 20 vs. grapple
feats:
- is_bonus: true
  name: Improved Grapple
- name: Iron Will
- name: Weapon Finesse
skills:
  Acrobatics: 5
    when jumping: 13
  Climb: 10
  Perception: 4
  _racial_mods:
    Acrobatics:
      when jumping: 8
special_qualities:
- cradling
ecology:
  environment: temperate or warm forests
  organization: pair, gang (3-4), or troop (5-12)
  treasure_type: standard
special_abilities:
  Cradling (Ex): Thanks to their massive hands, prehensile feet, and dexterous tails,
    canopy trolls are treated as if they were one size category larger for the purposes
    of grappling. They gain Improved Grapple as a bonus feat.
  Poison (Ex): |-
    A canopy troll's tail sting injects a single tumorous lump of its own regenerating flesh into its target. On a failed Fortitude save, this tumor grows beneath the victim's skin, sprouting bristly hairs and stubby teeth that cause debilitating pain for its host. The sickened condition lasts 2d4 days before the mass dissolves, though a host can attempt a Fortitude saving throw each day to overcome the pain and ignore the condition. Alternatively, the tumor can be removed with a successful DC 20 Heal check.

    Sting-injury; save Fort DC 15; frequency 1/round for 3 rounds; effect sickened for 2d4 days; cure special.
  Swarming (Ex): Canopy trolls live and fight in tangled piles and are adept at swarming
    foes. Up to two canopy trolls can share the same square at the same time. If two
    canopy trolls in the same square attack the same foe, they are considered to be
    flanking that foe as if they were in two opposite squares.
desc_long: |-
  One of the most ravenous dangers of the Fangwood are the arboreal canopy trolls, who bound through the treetops in great troops, scavenging fruit and nuts and descending on much larger prey to tear it limb from limb. They share the legendary durability of larger trolls, and plummet fearlessly from great heights to take prey by surprise, often breaking bones only to heal by the time they begin to feed. These injuries rarely set properly, leaving most canopy trolls in constant pain, worsening their already vicious attitudes. Often underestimated, canopy trolls rely on great numbers and their ability to coordinate en masse, overwhelming prey by sheer numbers as they drag it kicking and screaming into their chaotic, howling maws.

  Canopy trolls stand 3-1/2 feet tall, and have prehensile tails nearly twice that length. Their densely muscled bodies weigh as much as 150 pounds.

---

# Troll, Canopy Troll
Prominent tusks and unruly green fur mark this fearsome creature as a _[[monsters/Troll|troll]]_ despite its small size. It hangs overhead, swinging between its oversized forearms and lashing, claw-tipped tail.
**Source** Pathfinder #116: Fangs of War pg. 90
**XP** 800
CE Small humanoid (giant)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +4

##### Defense

**AC** 15, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+4 Dex, +1 size)
**hp** 30 (4d8+12); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +7, **Ref** +5, **Will** +2

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +5 (1d4+1), 2 claws +5 (1d3+1), sting +5 (1d3+1 plus poison)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with sting)
**Special Attacks** poison, swarming

##### Statistics
**Str** 12, **Dex** 18, **Con** 17, **Int** 4, **Wis** 9, **Cha** 7
**Base Atk** +3; **CMB** +3 (+6 grapple); **CMD** 17 (20 vs. grapple)
**Feats** _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +5 (+13 when jumping), _Climb_ +10, Perception +4; **Racial Modifiers** +8 Acrobatics when jumping
**SQ** cradling

##### Ecology

**Environment** temperate or warm forests
**Organization** pair, gang (3–4), or troop (5–12)
**Treasure** standard

### Special Abilities

**Cradling (Ex)** Thanks to their massive hands, _[[items/Weapon Magic Abilities/Prehensile|prehensile]]_ feet, and dexterous tails, canopy trolls are treated as if they were one size category larger for the purposes of grappling. They gain _Improved Grapple_ as a bonus feat.

**Poison (Ex)** A canopy _troll_’s tail sting injects a single tumorous lump of its own regenerating flesh into its target. On a failed Fortitude save, this tumor grows beneath the victim’s skin, sprouting bristly hairs and stubby teeth that cause _[[spells/Debilitating Pain|debilitating pain]]_ for its host. The _[[conditions/Sickened|sickened]]_ condition lasts 2d4 days before the mass dissolves, though a host can attempt a Fortitude saving throw each day to overcome the pain and ignore the condition. Alternatively, the tumor can be removed with a successful DC 20 _[[spells/Heal|Heal]]_ check.

Sting—injury; save Fort DC 15; frequency 1/round for 3 rounds; effect _sickened_ for 2d4 days; cure special.
**Swarming (Ex)** Canopy trolls live and fight in tangled piles and are adept at swarming foes. Up to two canopy trolls can share the same square at the same time. If two canopy trolls in the same square attack the same foe, they are considered to be flanking that foe as if they were in two opposite squares.

##### Description

One of the most _[[curses/Ravenous|ravenous]]_ dangers of the Fangwood are the arboreal canopy trolls, who bound through the treetops in great troops, scavenging fruit and nuts and descending on much larger prey to tear it limb from limb. They share the legendary durability of larger trolls, and plummet fearlessly from great heights to take prey by surprise, often _[[items/Weapon Magic Abilities/Breaking|breaking]]_ bones only to _heal_ by the time they begin to feed. These injuries rarely set properly, leaving most canopy trolls in constant pain, worsening their already _[[items/Weapon Magic Abilities/Vicious|vicious]]_ attitudes. Often underestimated, canopy trolls rely on great numbers and their ability to coordinate en masse, overwhelming prey by sheer numbers as they drag it kicking and screaming into their chaotic, howling maws.

Canopy trolls stand 3-1/2 feet tall, and have _prehensile_ tails nearly twice that length. Their densely muscled bodies weigh as much as 150 pounds.