---
cssclass: [monsters]
title1: Lamia-Kin, Hungerer
desc_short: 'A hideous mound of shuddering, pustule-encrusted flesh, this bloated
  creature's gaping maw is filled with terrible teeth. '
title2: Hungerer
CR: 15
sources:
- name: Rise of the Runelords Anniversary Edition
  page: 410
  link: http://paizo.com/products/btpy8tc0?Pathfinder-Adventure-Path-Rise-of-the-Runelords-Anniversary-Edition
- name: 'Pathfinder #6: Spires of Xin-Shalast'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy817c
XP: 51200
alignment: CE
size: Huge
type: monstrous humanoid
initiative:
  bonus: 5
senses:
  darkvision: 90
  low-light vision: true
auras:
- name: stench
  radius: 30
  DC: 25
AC:
  AC: 31
  touch: 10
  flat_footed: 29
  components:
    dex: 1
    dodge: 1
    natural: 21
    size: -2
HP:
  HP: 220
  long: 21d10+105
saves:
  fort: 12
  ref: 15
  will: 18
DR:
- amount: 10
  weakness: cold iron and piercing
immunities:
- acid
- poison
resistances:
  electricity: 10
  fire: 10
SR: 26
speeds:
  base: 10
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +29 (2d8+10/19-20/×4 plus 2d6 acid damage and 2 Wisdom drain)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
          crit_multiplier: 4
        - damage: 2d6
          type: acid damage
        - damage: '2'
          type: Wisdom drain
      attack: bite
      bonus:
      - 29
    - text: 2 claws +29 (1d8+10 plus 2 Wisdom drain)
      entries:
      - - damage: 1d8+10
        - damage: '2'
          type: Wisdom drain
      count: 2
      attack: claws
      bonus:
      - 29
  special:
  - devastating bite
  - vile spew
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: grease
    source: default
    freq: At will
    DC: 15
  - name: major image
    source: default
    freq: At will
    DC: 17
  - name: ventriloquism
    source: default
    freq: At will
    DC: 15
  - name: charm monster
    source: default
    freq: 3/day
    DC: 18
  - name: gust of wind
    source: default
    freq: 3/day
    DC: 16
  - name: quickened stinking cloud
    source: default
    freq: 3/day
    DC: 17
  - name: suggestion
    source: default
    freq: 3/day
    DC: 17
  - name: deep slumber
    source: default
    freq: 1/day
    DC: 17
  - name: mass charm monster
    source: default
    freq: 1/day
    DC: 22
  - name: mirror image
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 30
  DEX: 13
  CON: 20
  INT: 13
  WIS: 18
  CHA: 19
BAB: 21
CMB: 33
CMD: 45
CMD_other: can't be tripped
feats:
- name: Critical Focus
- name: Dodge
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (stinking cloud)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 32
  Intimidate: 28
  Perception: 28
  Sense Motive: 25
  Stealth: 17
languages:
- Abyssal
- Common
- Giant
- Thassilonian
ecology:
  environment: cold mountains
  organization: solitary or feast (2-5)
  treasure_type: standard
special_abilities:
  Devastating Bite (Ex): A hungerer's bite deals ×4 damage on a successful critical
    hit. If this damage is enough to reduce a victim to negative hit points, the victim
    must succeed at a DC 30 Fortitude save to avoid being decapitated, bitten in half,
    or otherwise instantly killed by the horrific wound. The save DC is Strength-based.
  Vile Spew (Su): Whenever a hungerer takes damage, the resulting wound spews a great
    gout of vile blood and acid. Any creature adjacent to a hungerer when it is wounded
    takes 2d6 points of acid damage (Reflex DC 25 negates). The save DC is Constitution-based.
  Wisdom Drain (Su): A hungerer drains 2 points of Wisdom each time it strikes a foe
    with its bite or claw attacks. Unlike with other kinds of ability drain attacks,
    a hungerer does not heal any damage when it uses its Wisdom drain.
desc_long: |-
  Once regular lamias, these hideously deformed creatures are the result of terrible f leshwarping experiments that have rarely been repeated since the fall of Thassilon. The heads and torsos of these creatures are nearly 10 feet in diameter, and a typical hungerer weighs about 20,000 pounds.

   Hungerers are unnatural creatures, re-released into the world with Karzoug's awakening. These terrors live in constant pain and serve as living embodiments of hunger, insatiable in their constant quests for sustenance. Although they prefer to tear and rend living f lesh, hungerers can consume almost any organic material, and might even gnaw on stone or metal without ill effect when nothing else is available.

---

# Lamia-Kin, Hungerer
A hideous mound of shuddering, pustule-encrusted flesh, this
bloated creature’s gaping maw is filled with terrible teeth.

**Source** Rise of the Runelords Anniversary Edition pg. 410, Pathfinder #6: Spires of Xin-Shalast pg. 84
**XP** 51,200
CE Huge monstrous humanoid
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +28
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 25)

##### Defense

**AC** 31, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+1 Dex, +1 dodge, +21 natural,
–2 size)
**hp** 220 (21d10+105)
**Fort** +12, **Ref** +15, **Will** +18
**DR** 10/cold iron and piercing; **Immune** acid, poison; **Resist** electricity 10, fire 10; **SR** 26

##### Offense
**Speed** 10 ft., fly 60 ft. (good)
**Melee** bite +29 (2d8+10/19–20/×4 plus 2d6 acid damage and
 2 Wisdom drain), 2 claws +29 (1d8+10 plus 2 Wisdom drain)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** devastating bite, vile spew
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
Constant—fly
At will—_[[spells/Grease|grease]]_ (DC 15), _[[spells/Major Image|major image]]_ (DC 17), _[[spells/Ventriloquism|ventriloquism]]_
(DC 15)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Gust Of Wind|gust of wind]]_ (DC 16),
quickened _[[spells/Stinking Cloud|stinking cloud]]_ (DC 17), _[[spells/Suggestion|suggestion]]_ (DC 17)
1/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 17), mass _charm monster_ (DC 22),
_[[spells/Mirror Image|mirror image]]_

##### Statistics
**Str** 30, **Dex** 13, **Con** 20, **Int** 13, **Wis** 18, **Cha** 19
**Base Atk** +21; **CMB** +33; **CMD** 45 (can’t be tripped)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), Improved
Initiative, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_stinking cloud_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +32, Intimidate +28, Perception +28, Sense Motive +25,
Stealth +17
**Languages** Abyssal, Common, Giant, Thassilonian

##### Ecology

**Environment** cold mountains
**Organization** solitary or feast (2–5)
**Treasure** standard

### Special Abilities

**Devastating Bite (Ex)** A hungerer’s bite deals ×4 damage on
a successful critical hit. If this damage is enough to reduce a
victim to negative hit points, the victim must succeed at a DC
 30 Fortitude save to avoid being decapitated, bitten in half, or
otherwise instantly killed by the horrific wound. The save DC
is Strength-based.

**Vile Spew (Su)** Whenever a hungerer takes damage, the
resulting wound spews a great gout of vile blood and acid.
Any creature adjacent to a hungerer when it is wounded takes
 2d6 points of acid damage (Reflex DC 25 negates). The save
DC is Constitution-based.

**Wisdom Drain (Su) **A hungerer drains 2 points of Wisdom each
time it strikes a foe with its bite or claw attacks. Unlike with
other kinds of ability drain attacks, a hungerer does not _[[spells/Heal|heal]]_
any damage when it uses its Wisdom drain.

##### Description

Once regular lamias, these hideously deformed creatures are the result of terrible f leshwarping experiments that have rarely been repeated since the fall of Thassilon. The heads and torsos of these creatures are nearly 10 feet in diameter, and a typical hungerer weighs about 20,000 pounds.

Hungerers are unnatural creatures, re-released into the world with Karzoug's awakening. These terrors live in constant pain and serve as living embodiments of hunger, insatiable in their constant quests for sustenance. Although they prefer to tear and _[[universal monster rules/Rend|rend]]_ living f lesh, hungerers can consume almost any organic material, and might even gnaw on stone or metal without ill effect when nothing else is available.