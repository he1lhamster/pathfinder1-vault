---
cssclass: [monsters]
title1: Ercinee
is_3.5: true
desc_short: Beating its powerful wings, this massive multicolored bird circles purposefully.
  Its eyes are pits of greenish flame and its radiant feathers cause it to soar in
  stark relief against the comparably dull sky.
title2: Ercinee
CR: 4
sources:
- name: 'Pathfinder #5: Sins of the Saviors'
  page: 81
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy815o
alignment: N
size: Large
type: magical beast
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 11
  flat_footed: 15
  components:
    size: -1
    dex: 2
    natural: 6
HP:
  HP: 38
  long: 7d10
saves:
  fort: 5
  ref: 7
  will: 4
speeds:
  base: 10
  fly: 80
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +9 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: claws
      bonus:
      - 9
    - text: bite +4 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 4
  special:
  - unstable screech
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: searing light
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 6
    touch_attack_ranged: 8
ability_scores:
  STR: 17
  DEX: 15
  CON: 10
  INT: 10
  WIS: 14
  CHA: 13
BAB: 7
grapple_3.5: 14
feats:
- name: Alertness
- name: Flyby Attack
- name: Wingover
skills:
  Bluff: 8
  Listen: 10
  Spot: 11
languages:
- Auran
special_qualities:
- lighted way
- radiance
ecology:
  environment: temperate forests
  organization: solitary
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 8
    size: Large
    HD_max: 12
special_abilities:
  Lighted Way (Su): At will, an ercinee can shed drops of luminous fluid from its
    wings. This liquid falls behind it as it flies, with one droplet falling every
    25 feet. Where these droplets land, the area within 5 feet is lit by shadowy illumination.
    This fluid lasts for 1 hour, after which it evaporates to nothing.
  Unstable Screech (Su): An ercinee can, as a standard action, emit a shrill and bewildering
    screech. Any creature within 30 feet of the ercinee must make a DC 15 Will save
    or be confused for 1d4 rounds. Creatures who succeed at this save cannot be affected
    again by the same ercinee's screech for 24 hours. Creatures already confused take
    a -2 penalty on their save to resist additional unstable screeches. The save DC
    is Wisdom-based.
  Radiance (Sp): At night, an ercinee sheds light as the spell daylight. It can suppress
    or reactivate this ability as a free action.
desc_long: Also called alicanto, ercinee are enormous, multicolored creatures resembling
  giant birds of prey. Unlike normal birds, however, ercinee are infused with a magical
  luminescence that causes the tips of their feathers to emit green light as well
  as giving their green eyes a burning appearance. This luminescence is only apparent
  at night. On average, an ercinee stands about 6 feet tall from talons to beak and
  its wingspan measures 14 to 18 feet.

---

# Ercinee
Beating its _[[feats/Powerful Wings|powerful wings]]_, this massive multicolored bird circles purposefully. Its eyes are pits of greenish flame and its _[[items/Armor Magic Abilities/Radiant|radiant]]_ feathers cause it to soar in stark relief against the comparably dull sky.
**Source** Pathfinder #5: Sins of the Saviors pg. 81

N Large magical beast
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Listen +10, Spot +11

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (-1 size, +2 Dex, +6 natural)
**hp** 38 (7d10)
**Fort** +5, **Ref** +7, **Will** +4

##### Offense
**Speed** 10 ft., fly 80 ft. (good)
**Melee** 2 claws +9 (1d6+3) and bite +4 (1d4+1)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** unstable _[[spells/Screech|screech]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; +8 ranged touch)
At will - _[[spells/Dancing Lights|dancing lights]]_, light
3/day - _[[spells/Searing Light|searing light]]_

##### Statistics
**Str** 17, **Dex** 15, **Con** 10, **Int** 10, **Wis** 14, **Cha** 13
**Base Atk** +7; **Grapple** +14
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +8, Listen +10, Spot +11
**Languages** Auran
**SQ** lighted way, _[[items/Weapon/Radiance|radiance]]_

##### Ecology

**Environment** temperate forests
**Organization** solitary
**Treasure** none
**Advancement** 8-12 HD (Large)

### Special Abilities

**Lighted Way (Su)** At will, an _[[monsters/Ercinee|ercinee]]_ can shed drops of luminous fluid from its wings. This liquid falls behind it as it flies, with one droplet falling every 25 feet. Where these droplets land, the area within 5 feet is lit by shadowy illumination. This fluid lasts for 1 hour, after which it evaporates to nothing.

**Unstable _Screech_ (Su)** An _ercinee_ can, as a standard action, emit a shrill and _[[items/Weapon Magic Abilities/Bewildering|bewildering]]_ _screech_. Any creature within 30 feet of the _ercinee_ must make a DC 15 Will save or be _[[conditions/Confused|confused]]_ for 1d4 rounds. Creatures who succeed at this save cannot be affected again by the same _ercinee_’s _screech_ for 24 hours. Creatures already _confused_ take a –2 penalty on their save to resist additional unstable screeches. The save DC is Wisdom-based.

**_Radiance_ (Sp)** At night, an _ercinee_ sheds light as the spell _[[spells/Daylight|daylight]]_. It can suppress or reactivate this ability as a free action.

##### Description

Also _[[items/Weapon Magic Abilities/Called|called]]_ alicanto, _ercinee_ are enormous, multicolored creatures resembling giant birds of prey. Unlike normal birds, however, _ercinee_ are infused with a magical luminescence that causes the tips of their feathers to emit green light as well as giving their green eyes a _[[items/Weapon Magic Abilities/Burning|burning]]_ appearance. This luminescence is only apparent at night. On average, an _ercinee_ stands about 6 feet tall from talons to beak and its wingspan measures 14 to 18 feet.