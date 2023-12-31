﻿---
cssclass: [monsters]
title1: Capramace
desc_short: This twisted amalgamation of human and goat is covered in matted fur,
  its teeth sharp and eyes eerily blank.
title2: Capramace
CR: 7
sources:
- name: Bestiary 5
  page: 50
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Wardens of the Reborn Forge
  page: 61
  link: http://paizo.com/products/btpy92lr?Pathfinder-Module-Wardens-of-the-Reborn-Forge
XP: 3200
alignment: N
size: Large
type: aberration
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 10
  flat_footed: 17
  components:
    dex: 1
    natural: 8
    size: -1
HP:
  HP: 85
  long: 9d8+45
saves:
  fort: 9
  ref: 6
  will: 8
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +13 (2d6+8 plus disease)
      entries:
      - - damage: 2d6+8
        - effect: disease
      attack: bite
      bonus:
      - 13
    - text: 2 hooves +8 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: hooves
      bonus:
      - 8
  special:
  - disease
  - rage call
space: 10
reach: 10
ability_scores:
  STR: 26
  DEX: 13
  CON: 18
  INT: 1
  WIS: 14
  CHA: 5
BAB: 6
CMB: 15
CMB_other: +17 bull rush
CMD: 26
CMD_other: 28 vs. bull rush
feats:
- name: Great Fortitude
- name: Improved Bull Rush
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Climb: 15
  Perception: 10
ecology:
  environment: temperate plains
  organization: solitary, pack (2-11), or herd (12-25)
  treasure_type: none
special_abilities:
  Disease (Su): 'Waste Trembles: Bite-injury; save Fort DC 18; onset 1d3 days; frequency
    1/day; effect 1d3 Str and 1d3 Dex damage, target must succeed at a second Fortitude
    save or 1 point of each type of ability damage is drain instead; cure 2 consecutive
    saves-the secondary save to keep damage from becoming drain does not count toward
    this requirement. The save DC is Constitution-based.'
  Rage Call (Su): |-
    Once per day as a standard action, a capramace can open its mouth and emit a horrible, ear-piercing scream to call for its herd. Maintaining a rage call on any round after the first round is a free action, and there is no limit to the duration of a sustained rage call. Non-capramaces within 120 feet that fail a DC 18 Fortitude saving throw are deafened as long as the capramace maintains its call and for 1d4 minutes afterward.

    Any other capramaces within 1 mile can hear this high-pitched cry regardless of external noise conditions, and instinctively react by sprinting to the capramace in need, continuing to move as fast as possible to the capramace as long as it maintains its rage call. A capramace moving toward the source of a rage call is treated as though it possesses the Run feat. Any capramace that comes within 60 feet of another capramace's rage call goes wild with fear and anger, attacking the nearest non-capramace creature in sight for as long as the rage call lasts.

    Sound-mitigating effects such as silence can prevent a capramace from performing its rage call, as can effects that suffocate a capramace. Similarly, a capramace with the deafened condition cannot be affected by the rage call of another capramace. The save DC is Constitution-based.
desc_long: While the capramaces' exact origins are unknown, many legends hold them
  to be abominations resulting from some magical combination of goat and human. Certainly
  their humanoid shape suggests such a melding, although they show no signs of humanoid
  intelligence. Farmers who find their fields beset by capramaches must be careful
  not to startle them, lest their terrible, deafening screams call more of these monstrosities
  to their aid. Brave inhabitants of remote settlements sometimes entice capramaces
  into service as work animals, but most people regard this a foolish endeavor at
  best. While these creatures are both strong and hardy, they are difficult to control,
  and even the slightest mistreatment can cause them to turn on their would-be masters
  with little warning.

---

# Capramace
This twisted amalgamation of human and goat is covered in matted fur, its teeth sharp and eyes eerily blank.
**Source** Bestiary 5 pg. 50, Wardens of the Reborn Forge pg. 61
**XP** 3,200

N Large aberration
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 18, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+1 Dex, +8 natural, -1 size)
**hp** 85 (9d8+45)
**Fort** +9, **Ref** +6, **Will** +8

##### Offense
**Speed** 50 ft.
**Melee** bite +13 (2d6+8 plus disease), 2 hooves +8 (1d8+4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** disease, _[[spells/Rage|rage]]_ call

##### Statistics
**Str** 26, **Dex** 13, **Con** 18, **Int** 1, **Wis** 14, **Cha** 5
**Base Atk** +6; **CMB** +15 (+17 bull rush); **CMD** 26 (28 vs. bull rush)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +15, Perception +10

##### Ecology

**Environment** temperate plains
**Organization** solitary, pack (2-11), or herd (12-25)
**Treasure** none

### Special Abilities

**Disease (Su)** Waste Trembles: Bite—injury; save Fort DC 18; onset 1d3 days; frequency 1/day; effect 1d3 Str and 1d3 Dex damage, target must succeed at a second Fortitude save or 1 point of each type of ability damage is drain instead; cure 2 consecutive saves—the secondary save to keep damage from becoming drain does not count toward this requirement. The save DC is Constitution-based.

**_Rage_ Call (Su)** Once per day as a standard action, a _[[monsters/Capramace|capramace]]_ can open its mouth and emit a horrible, _[[spells/Ear-Piercing Scream|ear-piercing scream]]_ to call for its herd. Maintaining a _rage_ call on any round after the first round is a free action, and there is no limit to the duration of a sustained _rage_ call. Non-capramaces within 120 feet that fail a DC 18 Fortitude saving throw are _[[conditions/Deafened|deafened]]_ as long as the _capramace_ maintains its call and for 1d4 minutes afterward.

Any other capramaces within 1 mile can hear this high-pitched cry regardless of external noise conditions, and instinctively react by sprinting to the _capramace_ in need, continuing to move as fast as possible to the _capramace_ as long as it maintains its _rage_ call. A _capramace_ moving toward the source of a _rage_ call is treated as though it possesses the Run feat. Any _capramace_ that comes within 60 feet of another _capramace_’s _rage_ call goes wild with _[[universal monster rules/Fear|fear]]_ and anger, attacking the nearest non-capramace creature in sight for as long as the _rage_ call lasts.

Sound-mitigating effects such as _[[spells/Silence|silence]]_ can prevent a _capramace_ from performing its _rage_ call, as can effects that suffocate a _capramace_. Similarly, a _capramace_ with the _deafened_ condition cannot be affected by the _rage_ call of another _capramace_. The save DC is Constitution-based.

##### Description

While the capramaces’ exact origins are _[[monsters/Unknown|unknown]]_, many legends hold them to be abominations resulting from some magical combination of goat and human. Certainly their humanoid shape suggests such a melding, although they show no signs of humanoid intelligence. Farmers who find their fields beset by capramaches must be careful not to startle them, lest their terrible, deafening screams call more of these monstrosities to their aid. Brave inhabitants of remote settlements sometimes entice capramaces into service as work animals, but most people regard this a foolish endeavor at best. While these creatures are both strong and hardy, they are difficult to control, and even the slightest mistreatment can cause them to turn on their would-be masters with little warning.