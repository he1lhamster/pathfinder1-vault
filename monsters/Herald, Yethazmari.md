---
cssclass: [monsters]
title1: Herald, Yethazmari
is_3.5: true
desc_short: Double the size of a man at its shoulder, this creature looks like a gigantic,
  starving jackal, but from its back beat the tattered black wings of a monstrous
  bat. A canine head sprouts from where it would be natural for one to rest, but behind,
  where the creature's tail should begin, instead sways the sleek, strong coils of
  a viper, ending in a fanged head that arcs over the monster's back. Twin trails
  of thin smoke, like those from dying embers, rise from where the thing's jackal
  eyes should be, roiling up from depthless hollows gaping in the horror's snarling
  visage.
title2: Yethazmari
CR: 15
sources:
- name: 'Pathfinder #5: Sins of the Saviors'
  page: 90
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy815o
- name: Inner Sea Gods
  page: 296
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- evil
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 32
  touch: 14
  flat_footed: 27
  components:
    dex: 5
    natural: 18
    size: -1
HP:
  HP: 189
  long: 18d8+108
saves:
  fort: 17
  ref: 16
  will: 17
DR:
- amount: 15
  weakness: good
immunities:
- fire
SR: 27
speeds:
  base: 50
  fly: 100
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +24 (1d8+7/19-20)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
      attack: bite
      bonus:
      - 24
    - text: tail +19 (1d6+3 plus poison)
      entries:
      - - damage: 1d6+3
        - effect: poison
      attack: tail
      bonus:
      - 19
  ranged:
  - - text: poison gout +22 (6d10 acid plus poison)
      entries:
      - - damage: 6d10
          type: acid
        - effect: poison
      attack: poison gout
      bonus:
      - 22
  special:
  - bay
  - maddening vision
spell_like_abilities:
  entries:
  - name: blindness/deafness
    source: default
    freq: At will
    DC: 17
  - name: locate creature
    source: default
    freq: At will
  - name: rage
    source: default
    freq: At will
    DC: 18
  - name: veil
    source: default
    freq: At will
    DC: 22
  - name: baleful polymorph
    source: default
    freq: 3/day
    DC: 20
  - name: feeblemind
    source: default
    freq: 3/day
    DC: 20
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    other: self and willing targets only
  - name: summon monster IV
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
  - name: unhallow
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 15
ability_scores:
  STR: 24
  DEX: 20
  CON: 22
  INT: 17
  WIS: 23
  CHA: 22
BAB: 18
grapple_3.5: 29
feats:
- name: Alertness
- name: Flyby Attack
- name: Hover
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Power Attack
skills:
  Balance: 17
  Bluff: 27
  Climb: 17
  Intimidation: 29
  Knowledge (religion): 14
  Knowledge (the planes): 14
  Listen: 29
  Move Silently: 26
  Search: 24
  Spellcraft: 24
  Spot: 29
  Survival: 27
    to follow tracks: 29
  Tumble: 28
languages:
- Abyssal
- Common
- Infernal
special_qualities:
- soul scream
ecology:
  environment: any
  organization: solitary
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 19
    size: Large
    HD_max: 26
  - type: size
    HD_min: 27
    size: Huge
special_abilities:
  Bay (Su): When a yethazmari howls or barks, all creatures except other evil outsiders
    within a 300-foot-radius spread must succeed on a DC 25 Will save or become panicked
    for 2d4 rounds. This is a sonic, mind-affecting fear effect. Whether or not the
    save is successful, an affected creature is immune to the same yethazmari's bay
    for 24 hours. The save DC is Charisma-based.
  Maddening Vision (Su): A yethazmari can unleash a blast of abyssal smoke from its
    eyes (25-foot cone, once every 1d4 rounds, damage 12d10 fire, Reflex DC 25 half).
    Creatures of an alignment other than chaotic that are damaged by this effect must
    make additional DC 25 Will saves as their minds are assaulted with unspeakable
    visions. Those who fail this save are affected as per the spell confusion for
    1d6 rounds. These save DCs are Constitution-based.
  Poison (Su): Contact or injury, Fortitude DC 25, initial damage 2d6 Str, secondary
    damage 2d6 Str. The save DC is Constitution-based.
  Poison Gout (Su): A yethazmari can use its serpentine head to spit a gout of burning,
    acidic poison at a creature within 30 feet as a standard action. This is a ranged
    touch attack that deals 6d10 points of acid damage. Any creature damaged by the
    attack is affected by the yethazmari's poison.
  Soul Scream (Su): Any time a yethazmari takes piercing or slashing damage from any
    source, the wounds created in its flesh unleash a terrifying cacophony. This is
    terrible noise has the same effects as the creature's bay special attack. Creatures
    within 10 feet of the yethazmari take a -4 penalty on their save versus this effect.
desc_long: Said to howl through the lightless sky on the nights of lunar eclipses,
  hunting for lone travelers to drag back to Lamashtu's realm, the yethazmari is the
  herald of the Mother of Monsters. A 14-foot-tall poisonous jackal with a snake for
  a tail and wings as black as pitch, the yethazmari is known to be among Lamashtu's
  favorite offspring, as well as her lapdog. Having hunted at the Demon Queen's side
  for untold centuries and witnessed some of her most profane atrocities, the thing's
  eyes have burnt to smoldering coals, loose in the depths of its skull. Now it sees
  only worlds undone, endless ruinous visions of reality rent at the claws of the
  Mother of Monsters.

---

# Herald, Yethazmari
Double the size of a man at its shoulder, this creature looks like a gigantic, starving _[[monsters/Jackal|jackal]]_, but from its back beat the tattered black wings of a monstrous bat. A canine head sprouts from where it would be natural for one to rest, but behind, where the creature’s tail should begin, instead sways the sleek, strong coils of a viper, ending in a fanged head that arcs over the monster’s back. Twin trails of thin smoke, like those from _[[conditions/Dying|dying]]_ embers, rise from where the thing’s _jackal_ eyes should be, roiling up from depthless hollows gaping in the horror’s snarling visage.
**Source** Pathfinder #5: Sins of the Saviors pg. 90, Inner Sea Gods pg. 296
CE Large outsider (chaotic, extraplanar, evil)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +29, Spot +29

##### Defense

**AC** 32, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+5 Dex, +18 natural, -1 size)
**hp** 189 (18d8+108)
**Fort** +17, **Ref** +16, **Will** +17
**DR** 15/good; **Immune** fire; **SR** 27

##### Offense
**Speed** 50 ft., fly 100 ft. (good)
**Melee** bite +24 (1d8+7/19-20) and tail +19 (1d6+3 plus poison)
**Ranged** poison gout +22 (6d10 acid plus poison)
**Special Attacks** bay, maddening _[[spells/Vision|vision]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th)
At will - blindness/deafness (DC 17), _[[spells/Locate Creature|locate creature]]_, _[[spells/Rage|rage]]_ (DC 18), _[[spells/Veil|veil]]_ (DC 22)
3/day - _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Feeblemind|feeblemind]]_ (DC 20), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Plane Shift|plane shift]]_ (self and willing targets only), _[[spells/Summon Monster IV|summon monster IV]]_
1/day - _[[spells/Control Weather|control weather]]_, _[[spells/Unhallow|unhallow]]_ (DC 20)

##### Statistics
**Str** 24, **Dex** 20, **Con** 22, **Int** 17, **Wis** 23, **Cha** 22
**Base Atk** +18; **Grapple** +29
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Balance +17, Bluff +27, _[[universal monster rules/Climb|Climb]]_ +17, Intimidate +29, Knowledge (religion) +14, Knowledge (the planes) +14, Listen +29, Move Silently +26, Search +24, Spellcraft +24, Spot +21, Survival +27 (+29 to follow tracks), Tumble +28
**Languages** Abyssal, Common, Infernal
**SQ** soul scream

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none
**Advancement** 19-26 HD (Large), 27+ HD (Huge)

### Special Abilities

**Bay (Su)** When a yethazmari howls or barks, all creatures except other evil outsiders within a 300-foot-radius spread must succeed on a DC 25 Will save or become _[[conditions/Panicked|panicked]]_ for 2d4 rounds. This is a sonic, mind-affecting _[[universal monster rules/Fear|fear]]_ effect. Whether or not the save is successful, an affected creature is immune to the same yethazmari’s bay for 24 hours. The save DC is Charisma-based.

**Maddening _Vision_ (Su)** A yethazmari can unleash a blast of abyssal smoke from its eyes (25-foot cone, once every 1d4 rounds, damage 12d10 fire, Reflex DC 25 half). Creatures of an alignment other than chaotic that are damaged by this effect must make additional DC 25 Will saves as their minds are assaulted with unspeakable visions. Those who fail this save are affected as per the spell _[[spells/Confusion|confusion]]_ for 1d6 rounds. These save DCs are Constitution-based.

**Poison (Su)** Contact or injury, Fortitude DC 25, initial damage 2d6 Str, secondary damage 2d6 Str. The save DC is Constitution-based.

**Poison Gout (Su)** A yethazmari can use its serpentine head to spit a gout of _[[items/Weapon Magic Abilities/Burning|burning]]_, acidic poison at a creature within 30 feet as a standard action. This is a ranged touch attack that deals 6d10 points of acid damage. Any creature damaged by the attack is affected by the yethazmari’s poison.
**Soul Scream (Su)** Any time a yethazmari takes piercing or slashing damage from any source, the wounds created in its flesh unleash a terrifying cacophony. This is terrible noise has the same effects as the creature’s bay special attack. Creatures within 10 feet of the yethazmari take a –4 penalty on their save versus this effect.

##### Description

Said to howl through the lightless sky on the nights of lunar eclipses, hunting for lone travelers to drag back to Lamashtu’s realm, the yethazmari is the herald of the Mother of Monsters. A 14-foot-tall poisonous _jackal_ with a snake for a tail and wings as black as pitch, the yethazmari is known to be among Lamashtu’s favorite offspring, as well as her lapdog. Having hunted at the Demon Queen’s side for untold centuries and witnessed some of her most profane atrocities, the thing’s eyes have burnt to smoldering coals, loose in the depths of its skull. Now it sees only worlds undone, endless ruinous visions of reality rent at the claws of the Mother of Monsters.