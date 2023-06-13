---
cssclass: [monsters]
title1: Forgefiend (Scanderig)
desc_short: 'A massive, fire-filled maw splits the belly of this lumbering iron-skinned
  fiend, whose short arms end in razor-sharp claws. '
title2: Forgefiend (Scanderig)
CR: 10
sources:
- name: Rise of the Runelords Anniversary Edition
  page: 409
  link: http://paizo.com/products/btpy8tc0?Pathfinder-Adventure-Path-Rise-of-the-Runelords-Anniversary-Edition
- name: 'Pathfinder #4: Fortress of the Stone Giants'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy80hm
XP: 9600
alignment: LE
size: Large
type: outsider
subtypes:
- earth
- extraplanar
initiative:
  bonus: 6
senses:
  see in darkness: true
AC:
  AC: 25
  touch: 11
  flat_footed: 23
  components:
    dex: 2
    natural: 14
    size: -1
HP:
  HP: 137
  long: 11d10+77
saves:
  fort: 14
  ref: 5
  will: 10
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
speeds:
  base: 20
  burrow: 20
  other:
  - earth glide
attacks:
  melee:
  - - text: bite +17 (2d6+7 plus rend armor)
      entries:
      - - damage: 2d6+7
        - effect: rend armor
      attack: bite
      bonus:
      - 17
    - text: bite +17 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: bite
      bonus:
      - 17
    - text: 2 claws +17 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 17
  special:
  - adamantine bite
  - searing spew
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: major image
    source: default
    freq: At will
    DC: 15
  - name: passwall
    source: default
    freq: At will
  - name: shatter
    source: default
    freq: At will
    DC: 14
  - name: stone shape
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: dimensional anchor
    source: default
    freq: 3/day
  - name: flesh to stone
    source: default
    freq: 3/day
    DC: 18
  - name: quickened produce flame
    source: default
    freq: 3/day
  - name: wall of fire
    source: default
    freq: 3/day
  - name: wall of stone
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 10
    concentration: 12
ability_scores:
  STR: 24
  DEX: 14
  CON: 25
  INT: 15
  WIS: 12
  CHA: 15
BAB: 11
CMB: 19
CMD: 31
feats:
- name: Combat Reflexes
- is_bonus: true
  name: Greater Sunder
- name: Improved Initiative
- name: Improved Iron Will
- is_bonus: true
  name: Improved Sunder
- name: Iron Will
- name: Quicken Spell-Like Ability (produce flame)
- name: Vital Strike
skills:
  Acrobatics: 16
    when jumping: 12
  Climb: 21
  Craft (traps): 16
  Disable Device: 16
  Knowledge (dungeoneering): 16
  Perception: 15
  Sense Motive: 15
  Stealth: 12
languages:
- Common
- Dwarven
- Infernal
- Terran
ecology:
  environment: any underground (Plane of Earth)
  organization: solitary or team (2-6)
  treasure_type: standard
special_abilities:
  Adamantine Bite (Ex): A forgefiend's bite attacks are treated as adamantine for
    the purposes of overcoming damage reduction.
  Rend Armor (Ex): When a forgefiend hits with a bite attack, it chews any armor worn
    by the target-this grants the forgefiend a free sunder attempt against armor worn
    by the target if the victim fails a DC 22 Reflex save. A forgefiend also gains
    Greater Sunder and Improved Sunder as bonus feats. The save DC is Strength-based.
  Searing Spew (Su): A forgefiend can belch forth a searing pile of slag from its
    body maw as a standard action once every 1d4 rounds. This blob of molten metal
    affects any 10-foot-square area adjacent to the forgefiend. Any creature in this
    area takes 14d6 points of fire damage (Reflex DC 22 halves). The slag quickly
    cools, forming a rugged pile of worthless scrap and misshapen metal that is treated
    as difficult terrain-this stuff crumbles to powder in 1 hour. The save DC is Constitution-based.
desc_long: |-
  Scanderigs, more commonly known as “forgefiends,” look like large, heavily armored, barrel-shaped giants, with enormous mouths in their bellies in addition to the normal-sized ones in their heads. They are native to the Plane of Earth, but sometimes make their way through subterranean portals onto the Material Plane, where they gorge themselves on rich and relatively uncontested mineral veins. A forgefiend might live quite happily inside a mountain's heart for centuries, only causing trouble when the ore runs out or interlopers attempt to mine its territory. 

  Forgefiends are particularly feared in many dwarven societies. In addition to their penchant for destroying deep forges, they are often portrayed as boogeymanlike figures for frightening dwarven children and instilling good smithing habits-for it is said, “For every scrap of slag you waste, a scanderig is making haste. Those who use excessive ore find forgefiends scratching at their door!”

---

# Forgefiend (Scanderig)
A massive, fire-filled maw splits the belly of this lumbering
iron-skinned fiend, whose short arms end in razor-sharp claws.

**Source** Rise of the Runelords Anniversary Edition pg. 409, Pathfinder #4: Fortress of the Stone Giants pg. 86
**XP** 9,600

LE Large outsider (earth, extraplanar)
**Init** +6; **Senses** _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +15

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+2 Dex, +14 natural, –1 size)
**hp** 137 (11d10+77)
**Fort** +14, **Ref** +5, **Will** +10
**Immune** fire, poison; **Resist** acid 10, cold 10

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Earth Glide|earth glide]]_
**Melee** bite +17 (2d6+7 plus _[[universal monster rules/Rend|rend]]_ armor), bite +17 (1d6+7), 2 claws
+17 (1d6+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** adamantine bite, searing spew
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
Constant—_[[spells/Pass without Trace|pass without trace]]_
At will—_[[spells/Major Image|major image]]_ (DC 15), _[[spells/Passwall|passwall]]_, _[[spells/Shatter|shatter]]_ (DC 14),
_[[spells/Stone Shape|stone shape]]_
3/day—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Flesh to Stone|flesh to stone]]_
(DC 18), quickened _[[spells/Produce Flame|produce flame]]_, _[[spells/Wall Of Fire|wall of fire]]_, _[[spells/Wall Of Stone|wall of stone]]_

##### Statistics
**Str** 24, **Dex** 14, **Con** 25, **Int** 15, **Wis** 12, **Cha** 15
**Base Atk** +11; **CMB** +19; **CMD** 31
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, Quicken
Spell-Like Ability (_produce flame_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +16 (+12 when jumping), _[[universal monster rules/Climb|Climb]]_ +21,
Craft (traps) +16, Disable Device +16, Knowledge
(dungeoneering) +16, Perception +15, Sense Motive +15,
Stealth +12
**Languages** Common, Dwarven, Infernal, Terran

##### Ecology

**Environment** any underground (Plane
of Earth)
**Organization** solitary or team (2–6)
**Treasure** standard

### Special Abilities

**Adamantine Bite (Ex)** A forgefiend’s bite
attacks are treated as adamantine for the purposes
of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.

**_Rend_ Armor (Ex)** When a forgefiend hits with a bite
attack, it chews any armor worn by the target—this
grants the forgefiend a free sunder attempt against
armor worn by the target if the victim fails a DC 22
Reflex save. A forgefiend also gains _Greater Sunder_
and _Improved Sunder_ as bonus feats. The save DC
is Strength-based.
**Searing Spew (Su)** A forgefiend can belch forth a
searing pile of slag from its body maw as a standard action
once every 1d4 rounds. This blob of molten metal affects any
 10-foot-square area adjacent to the forgefiend. Any creature
in this area takes 14d6 points of fire damage (Reflex DC 22
halves). The slag quickly cools, forming a rugged pile of
worthless scrap and misshapen metal that is treated as difficult
terrain—this stuff crumbles to _[[items/Mundane/Powder|powder]]_ in 1 hour. The save DC is
Constitution-based.

##### Description

Scanderigs, more commonly known as “forgefiends,”
look like large, heavily armored, barrel-shaped giants,
with enormous mouths in their bellies in addition to the
normal-sized ones in their heads. They are native to the
Plane of Earth, but sometimes make their way through
subterranean portals onto the Material Plane, where
they gorge themselves on rich and relatively uncontested
mineral veins. A forgefiend might live quite happily
inside a mountain’s heart for centuries, only causing
trouble when the ore runs out or interlopers attempt to
mine its territory.

Forgefiends are particularly feared in many dwarven
societies. In addition to their penchant for destroying
deep forges, they are often portrayed as boogeymanlike
figures for frightening dwarven children and
instilling good smithing habits—for it is said, “For
every scrap of slag you waste, a scanderig is making
_[[spells/Haste|haste]]_. Those who use excessive ore find forgefiends
scratching at their door!”