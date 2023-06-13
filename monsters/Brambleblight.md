---
cssclass: [monsters]
second_statblock: true
title1: Brambleblight
desc_short: Two long vines covered in sharp thorns protrude from what appears to be
  a massive rotting bundle of barbs that's topped with a heap of berry-red eyes.
title2: Brambleblight
CR: 7
sources:
- name: "Pathfinder #92: The Hill Giant's Pledge"
  page: 84
  link: http://paizo.com/products/btpy9c1v?Pathfinder-Adventure-Path-92-The-Hill-Giants-Pledge
XP: 3200
alignment: N
size: Large
type: plant
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  plantsense: 120
auras:
- name: blight
  radius: 40
  DC: 19
AC:
  AC: 20
  touch: 12
  flat_footed: 17
  components:
    dex: 3
    natural: 8
    size: -1
HP:
  HP: 85
  long: 10d8+40
saves:
  fort: 11
  ref: 6
  will: 5
defensive_abilities:
- thorny
immunities:
- plant traits
speeds:
  base: 20
attacks:
  melee:
  - - text: 2 slams +13 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: slams
      bonus:
      - 13
  ranged:
  - - text: 4 thorns +10 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 4
      attack: thorns
      bonus:
      - 10
  special:
  - animate brambles
  - rain of thorns
space: 10
reach: 10
ability_scores:
  STR: 25
  DEX: 16
  CON: 18
  INT: 6
  WIS: 14
  CHA: 8
BAB: 7
CMB: 15
CMD: 28
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Power Attack
- name: Stand Still
- name: Weapon Focus (thorns)
skills:
  Perception: 10
  Stealth: 7
    in forests: 19
  _racial_mods:
    Stealth:
      in forests: 12
languages:
- Sylvan
special_qualities:
- bramble infestation
- improved woodland stride
ecology:
  environment: temperate or warm forests or underground
  organization: solitary
  treasure_type: incidental
special_abilities:
  Animate Brambles (Su): As a standard action, a brambleblight can animate any of
    the dead, thorny brambles created by its bramble infestation ability. For 1 minute,
    the animated bramble (see page 85) then attacks as though it were a Large animated
    object. The animated bramble is under the control of the brambleblight, which
    can change the animated bramble's target as a move action. The brambleblight can
    instead cause the brambles to entwine around creatures as if by the entangle spell
    (the brambles are considered to be covered in thorns). This effect lasts for 1
    hour.
  Blight Aura (Su): A brambleblight radiates a palpable aura of rot and decay in a
    40-foot radius. Living creatures entering the aura must succeed at a DC 19 Fortitude
    save or be sickened for 1 round. A creature of the animal, fey, or plant type
    that fails its save is nauseated for 1 round and sickened for 1 minute thereafter.
    If a creature succeeds at this saving throw, it is immune to this effect for 24
    hours. In addition, any plant creature entering this aura takes 1d6 points of
    damage each round it is within the area (Fortitude DC 19 half). Creatures that
    are immune to disease are immune to this aura, and the resist nature's lure class
    feature applies to the aura's effects. The save DC is Constitution-based.
  Bramble Infestation (Su): A brambleblight can devastate its surroundings, creating
    an area of dead, thorny brambles. To do so, the brambleblight must root itself
    in the ground and remain motionless for 24 hours. Over the next day, all plants
    that are not creatures in a 40-foot radius around the brambleblight sprout thorny
    brambles, then wither and die. This infestation of brambles persists and nothing
    grows in this area for as long as the brambleblight remains in the area. If the
    brambleblight leaves the area, normal growth returns after 1 week.
  Improved Woodland Stride (Ex): A brambleblight can move through any sort of undergrowth
    (such as natural thorns, briars, overgrown areas, and similar terrain) at its
    normal speed without taking damage or suffering other impairments. However, it
    can also move without harm or impediment through thorns, briars, and overgrown
    areas that are magically manipulated to impede motion.
  Plantsense (Ex): A brambleblight can automatically pinpoint the location of anything
    within 120 feet that is in contact with vegetation.
  Rain of Thorns (Ex): With a snap of its thorny vines, a brambleblight can loose
    a volley of four thorns as a standard action (make an attack roll for each thorn).
    This attack has a range of 120 feet with no range increment. All targets must
    be within 30 feet of each other. A brambleblight can launch up to 36 thorns in
    any 24-hour period.
  Thorny (Ex): A brambleblight's surface is covered in a host of thorns. A creature
    that strikes a brambleblight with a natural weapon, a melee weapon without reach,
    or an unarmed strike takes 1d6 points of piercing damage. Creatures that grapple
    a brambleblight automatically take 1d6 points of piercing damage each round they
    maintain the grapple.
desc_long: |-
  A stain on the land it infests, a brambleblight slowly alters its environment, infecting the local vegetation with sickness through its blight aura. When the native vegetation dies, the area becomes choked with slashing plants tangled together much like a giant briar patch. It is within this prickly terrain that the brambleblight dwells. Where most would find themselves at the mercy of the hungry barbs found within this thorn-filled region, the brambleblight traverses this area with ease. A brambleblight is a deviant thing of decay, a tangle of rotting vegetation rising in a roughly pyramidal heap, crowned with an asymmetrical cluster of berry-red eyes. Its main body resembles a bundle of fetid mulch with several thorn-covered branches spilling forth like the intestines of a gutted pig. These branches provide the plant with locomotion akin to that of a slithering serpent.

  A brambleblight typically covers an area about 10 feet in diameter. From the creature's base to its crown of crimson eyes, it piles upon itself to a height of no more than 10 feet. A brambleblight weighs about 500 pounds.

---

# Brambleblight
Two long vines covered in sharp thorns protrude from what appears to be a massive rotting bundle of barbs that’s topped with a heap of berry-red eyes.
**Source** Pathfinder #92: The Hill Giant's Pledge pg. 84
**XP** 3,200

N Large plant
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, plantsense 120 ft.; Perception +10
**Aura** _[[spells/Blight|blight]]_ (40 ft., DC 19)

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 Dex, +8 natural, –1 size)
**hp** 85 (10d8+40)
**Fort** +11, **Ref** +6, **Will** +5
**Defensive Abilities** thorny; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 20 ft.
**Melee** 2 slams +13 (2d6+7)
**Ranged** 4 thorns +10 (1d6+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** animate brambles, rain of thorns

##### Statistics
**Str** 25, **Dex** 16, **Con** 18, **Int** 6, **Wis** 14, **Cha** 8
**Base Atk** +7; **CMB** +15; **CMD** 28 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (thorns)
**Skills** Perception +10, Stealth +7 (+19 in forests); **Racial Modifiers** +12 Stealth in forests
**Languages** Sylvan
**SQ** bramble infestation, improved woodland stride

##### Ecology

**Environment** temperate or warm forests or underground
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Animate Brambles (Su)** As a standard action, a _[[monsters/Brambleblight|brambleblight]]_ can animate any of the dead, thorny brambles created by its bramble infestation ability. For 1 minute, the _[[items/Armor Magic Abilities/Animated|animated]]_ bramble (see page 85) then attacks as though it were a Large _[[monsters/Animated Object|animated object]]_. The _animated_ bramble is under the control of the _brambleblight_, which can change the _animated_ bramble’s target as a move action. The _brambleblight_ can instead cause the brambles to entwine around creatures as if by the _[[spells/Entangle|entangle]]_ spell (the brambles are considered to be covered in thorns). This effect lasts for 1 hour.

**_Blight_ Aura (Su)** A _brambleblight_ radiates a palpable aura of rot and decay in a 40-foot radius. Living creatures entering the aura must succeed at a DC 19 Fortitude save or be _[[conditions/Sickened|sickened]]_ for 1 round. A creature of the animal, fey, or plant type that fails its save is _[[conditions/Nauseated|nauseated]]_ for 1 round and _sickened_ for 1 minute thereafter. If a creature succeeds at this saving throw, it is immune to this effect for 24 hours. In addition, any plant creature entering this aura takes 1d6 points of damage each round it is within the area (Fortitude DC 19 half). Creatures that are immune to disease are immune to this aura, and the resist nature’s lure class feature applies to the aura’s effects. The save DC is Constitution-based.

**Bramble Infestation (Su)** A _brambleblight_ can devastate its surroundings, creating an area of dead, thorny brambles. To do so, the _brambleblight_ must _[[spells/Root|root]]_ itself in the ground and remain motionless for 24 hours. Over the next day, all plants that are not creatures in a 40-foot radius around the _brambleblight_ sprout thorny brambles, then wither and die. This infestation of brambles persists and nothing grows in this area for as long as the _brambleblight_ remains in the area. If the _brambleblight_ leaves the area, normal growth returns after 1 week.

**Improved Woodland Stride (Ex)** A _brambleblight_ can move through any sort of undergrowth (such as natural thorns, briars, overgrown areas, and similar terrain) at its normal speed without taking damage or suffering other impairments. However, it can also move without _[[spells/Harm|harm]]_ or impediment through thorns, briars, and overgrown areas that are magically manipulated to impede motion.

**Plantsense (Ex)** A _brambleblight_ can automatically pinpoint the location of anything within 120 feet that is in contact with vegetation.

**Rain of Thorns (Ex)** With a snap of its thorny vines, a _brambleblight_ can loose a volley of four thorns as a standard action (make an attack roll for each thorn). This attack has a range of 120 feet with no range increment. All targets must be within 30 feet of each other. A _brambleblight_ can launch up to 36 thorns in any 24-hour period.

**Thorny (Ex)** A _brambleblight_’s surface is covered in a host of thorns. A creature that strikes a _brambleblight_ with a natural weapon, a melee weapon without reach, or an unarmed strike takes 1d6 points of piercing damage. Creatures that grapple a _brambleblight_ automatically take 1d6 points of piercing damage each round they maintain the grapple.

##### Description

A stain on the land it infests, a _brambleblight_ slowly alters its environment, infecting the local vegetation with sickness through its _blight_ aura. When the native vegetation dies, the area becomes choked with slashing plants tangled together much like a giant _[[items/Weapon/Briar|briar]]_ patch. It is within this prickly terrain that the _brambleblight_ dwells. Where most would find themselves at the mercy of the hungry barbs found within this thorn-filled region, the _brambleblight_ traverses this area with ease. A _brambleblight_ is a deviant thing of decay, a tangle of rotting vegetation rising in a roughly pyramidal heap, crowned with an asymmetrical cluster of berry-red eyes. Its main body resembles a bundle of fetid mulch with several thorn-covered branches spilling forth like the intestines of a gutted pig. These branches provide the plant with locomotion akin to that of a _[[items/Weapon Magic Abilities/Slithering|slithering]]_ serpent.

A _brambleblight_ typically covers an area about 10 feet in diameter. From the creature’s base to its crown of crimson eyes, it piles upon itself to a height of no more than 10 feet. A _brambleblight_ weighs about 500 pounds.