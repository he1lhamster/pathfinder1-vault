---
cssclass: [monsters]
title1: Elemental (Fire), Elder Fire Elemental
title2: Mythic Elder Fire Elemental
CR: 14
MR: 5
sources:
- name: Mythic Adventures
  page: 195
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 38400
alignment: N
size: Huge
type: outsider
subtypes:
- elemental
- extraplanar
- fire
- mythic
initiative:
  bonus: 13
senses:
  darkvision: 60
auras:
- name: frightful presence
  radius: 60
  DC: 18
- name: shroud of flame
  radius: 15
  other:
  - 2d6 fire
  DC: 22
- name: smoke cloud
  radius: 10
  DC: 22
AC:
  AC: 32
  touch: 19
  flat_footed: 21
  components:
    dex: 9
    dodge: 2
    natural: 13
    size: -2
HP:
  HP: 202
  long: 16d10+114
saves:
  fort: 14
  ref: 19
  will: 8
DR:
- amount: 10
  weakness: '-'
immunities:
- elemental traits
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 60
attacks:
  melee:
  - - text: 2 slams +23 (2d8+8 plus burn)
      entries:
      - - damage: 2d8+8
        - effect: burn
      count: 2
      attack: slams
      bonus:
      - 23
  special:
  - blinding blaze
  - burn (2d10, DC 22)
  - inferno
  - mythic power (5/day, surge +1d8)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: produce flame
    source: default
    freq: At will
  - name: flame arrow
    source: default
    freq: 5/day
  - name: wall of fire
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 16
    concentration: 16
ability_scores:
  STR: 26
  DEX: 29
  CON: 18
  INT: 12
  WIS: 13
  CHA: 11
BAB: 16
CMB: 26
CMD: 47
feats:
- name: Blind-Fight
- is_mythic: true
  name: Combat Reflexes
- is_mythic: true
  name: Dodge
- is_bonus: true
  name: Improved Initiative
- is_mythic: true
  name: Iron Will
- name: Lightning Stance
- name: Mobility
- name: Spring Attack
- is_bonus: true
  name: Weapon Finesse
- name: Wind Stance
skills:
  Acrobatics: 28
    when jumping: 40
  Climb: 27
  Escape Artist: 28
  Intimidate: 19
  Knowledge (planes): 20
  Perception: 20
  Sense Motive: 20
languages:
- Ignan
ecology:
  environment: any (Plane of Fire)
  organization: solitary, pair, or gang (3-8)
  treasure_type: none
special_abilities:
  Blinding Blaze (Su): A mythic fire elemental can expend one use of mythic power
    as a swift action to burn brightly, granting it a blinding gaze attack. This gaze
    causes permanent blindness and has a range of 60 feet. A creature that succeeds
    at a DC 22 Fortitude save is instead dazzled for 1 round. Fire elementals are
    immune to this blindness. The save DC is Constitution-based.
  Inferno (Ex): A mythic fire elemental can expend one use of mythic power as an immediate
    action to lose its vulnerability to cold for 1 round. During this time, any fire
    damage it deals ignores fire resistance and fire immunity.
  Shroud of Flame (Ex): Any creature within a mythic fire elemental's reach must succeed
    at a DC 22 Reflex save at the start of its turn or take 2d6 points of fire damage.
    The elemental can suppress or reactivate this ability at will as a free action.
    The save DC is Constitution-based.
  Smoke Cloud (Ex): As a swift action, a mythic fire elemental can create a choking
    cloud of smoke. This cloud is equivalent to that of pyrotechnics and lasts 1 minute.
    Fire elementals are immune to the effects of this ability.
desc_long: A mythic elder fire elemental is a living fragment of the original fires
  at the heart of its home plane. Having learned the patience of a slow burn, it lacks
  both the recklessness of younger fire elementals and the urge to inspire fear in
  the hearts of flammable mortals. It enjoys using smoke to scatter opponents so it
  can chase them down and set them alight.

---

# Elemental (Fire), Elder Fire Elemental

**Source** Pathfinder RPG Bestiary pg. 125
**XP** 12,800

N Huge outsider (elemental, extraplanar, fire)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19

##### Defense

**AC** 26, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+9 Dex, +1 dodge, +8 natural, –2 size)
**hp** 152 (16d10+64)
**Fort** +14, **Ref** +19, **Will** +7
**DR** 10/—; **Immune** elemental traits, fire
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 60 ft.
**Melee** 2 slams +23 (2d8+8 plus _[[universal monster rules/Burn|burn]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _burn_ (2d10, DC 22)

##### Statistics
**Str** 26, **Dex** 29, **Con** 18, **Int** 10, **Wis** 11, **Cha** 11
**Base Atk** +16; **CMB** +26; **CMD** 46
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +28, _[[universal monster rules/Climb|Climb]]_ +27, Escape Artist +28, Intimidate +19, Knowledge (planes) +19, Perception +19

##### Ecology

**Environment** any (Plane of Fire)

Fire elementals are quick, _[[items/Weapon Magic Abilities/Cruel|cruel]]_ creatures of living flame. They enjoy frightening beings weaker than themselves, and terrorizing any creature they can set on fire.

A fire elemental cannot enter water or any other nonflammable liquid. A body of water is an impassible barrier unless the fire elemental can step or _[[spells/Jump|jump]]_ over it or the water is covered with a flammable material (such as a layer of oil).

Fire elementals vary in appearance—they usually manifest as coiling serpentine forms made of smoke and flame, but some fire elementals take on shapes more akin to humans, demons, or other monsters in order to increase the terror of their sudden appearance. Features on a fire elemental’s body are made by darker bits of flame or patches of semi-stable smoke, ash, and cinders.

**Elemental** **Height** **Weight** Small4 ft.1 lb. Medium8 ft.2 lbs. Large16 ft.4 lbs. Huge32 ft.8 lbs. Greater36 ft.10 lbs. Elder40 ft.12 lbs.