---
cssclass: [monsters]
title1: Verdurous Ooze
desc_short: A pool of greenish muck, blossoming with weird vegetable-like growths
  and sap-seeping boils, twitches into unnatural motion as a pseudopod springs outward,
  dragging the entire grotesque mass forward with an ameboid life.
title2: Verdurous Ooze
CR: 6
sources:
- name: 'Pathfinder #35: War of the River Kings'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7u
XP: 2400
alignment: N
size: Medium
type: ooze
initiative:
  bonus: -5
senses:
  blindsight: 60
  tremorsense: 60
auras:
- name: enliven
  radius: 15
  DC: 20
- name: sleep aura
  radius: 30
  DC: 20
AC:
  AC: 5
  touch: 5
  flat_footed: 5
  components:
    dex: -5
HP:
  HP: 85
  long: 9d8+54
saves:
  fort: 9
  ref: -2
  will: -2
defensive_abilities:
- split
immunities:
- acid
- fire
- mind-affecting effects
- ooze traits
- slashing and piercing damage
speeds:
  base: 20
attacks:
  melee:
  - - text: slam +9 (1d6+4 plus 1d6 acid and grab)
      entries:
      - - damage: 1d6+4
        - damage: 1d6
          type: acid
        - effect: grab
      attack: slam
      bonus:
      - 9
  special:
  - acid
  - constrict (1d6+4 plus 1d6 acid)
  - enliven
ability_scores:
  STR: 16
  DEX: 1
  CON: 22
  INT:
  WIS: 1
  CHA: 1
BAB: 6
CMB: 9
CMB_other: +13 grapple
CMD: 14
CMD_other: can't be tripped
skills:
  Stealth: -4
    in forests and plains areas: 16
  Perception: -5
  _racial_mods:
    Stealth:
      _: 0
      in forest and plains environs: 20
ecology:
  environment: temperate forest or plains
  organization: solitary
  treasure_type: none
special_abilities:
  Acid (Ex): A verdurous ooze secretes a digestive acid that dissolves flesh and metal
    quickly. Each time a creature takes damage from a verdurous ooze's acid, the creature's
    metal equipment and armor take the same amount of damage from the acid. A DC 21
    Reflex save prevents damage to such items. A metal or natural weapon that strikes
    a verdurous ooze takes 1d6 points of acid damage unless the weapon's wielder succeeds
    on a DC 21 Reflex save. If a verdurous ooze remains in contact with a metal object
    for 1 full round, it inflicts 20 points of acid damage (no save) on the object.
    The save DCs are Constitution-based.
  Enliven (Sp): The chemicals emitted by a verdurous ooze cause nearby plants to twitch
    into life. While in areas covered in natural growth, all squares within 15 feet
    of the verdurous ooze are affected as if by the spell entangle. The verdurous
    ooze has no control over this effect, and if dispelled the effect renews after
    1d4 rounds. The save DC is Constitution-based.
  Sleep Aura (Su): The chemicals emitted by a verdurous ooze have a stronger and opposite
    effect on living, non-plant creatures that come within a 30-foot radius. All living
    creatures within the area must make a DC 21 Will save or fall asleep for a number
    of rounds equal to the ooze's HD. Creatures immune to poison are also immune to
    this effect. Whether or not the save is successful, that creature cannot be affected
    again by the same verdurous ooze's sleep aura for 24 hours. This is a nonmagical
    sleep effect. The save DC is Constitution-based.
  Split (Ex): Slashing and piercing weapons deal no damage to a verdurous ooze. Instead,
    if the verdurous ooze would have taken 10 or more points of damage from a single
    slashing or piercing attack, it splits into two identical oozes, each with half
    of the original's current hit points (round down). Slashing or piercing attacks
    that deal less than 10 points of damage do not cause a verdurous ooze to split.
    Damage from multiple slashing or piercing attacks is not cumulative. A verdurous
    ooze with 15 hit points or less cannot be further split and dies if reduced to
    0 hit points.
desc_long: |-
  Verdurous oozes are animate masses of protoplasm of a sickly green hue. At rest, their flat bodies stand roughly 5 inches tall and can stretch out to a wide diameter, their surfaces blossoming into what look like thick tangles of mossy roots and gnarled vegetation as they lie still. Known to emit invisible but dangerous chemicals, these masses of slinking muck cause nearby plants to writhe and coil as if alive, while shocking animals into a temporary but deathly torpor. As such, they rarely must hunt to find food, instead sensing passing creatures and preying upon them after they succumb to the oozes' sleep aura. Always ravenous, the powerful acids that comprise these oozes quickly dissolve the flesh of their meals.

  A verdurous ooze typically weighs 300 pounds and can easily spread to fill a 5-foot-square area. While moving, such crawling muck rises only a few inches tall, though its structure might grow and boil up to a height of 2 or 3 feet if let undisturbed for a matter of days. Spontaneously grown structures collapse and melt back into the ooze's body as soon as it begins moving again.

---

# Verdurous Ooze
A pool of greenish muck, blossoming with _[[spells/Weird|weird]]_ vegetable-like growths and sap-seeping boils, twitches into unnatural motion as a pseudopod springs outward, dragging the entire grotesque mass forward with an ameboid life.
**Source** Pathfinder #35: War of the River Kings pg. 86
**XP** 2,400

N Medium ooze
**Init** -5; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception -5
**Aura** enliven (15 ft., DC 20), sleep aura (30 ft., DC 20)

##### Defense

**AC** 5, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 5 (-5 Dex)
**hp** 85 (9d8+54)
**Fort** +9, **Ref** -2, **Will** -2
**Defensive Abilities** _[[universal monster rules/Split|split]]_; **Immune** acid, fire, mind-affecting effects, ooze traits, slashing and piercing damage

##### Offense
**Speed** 20 ft.
**Melee** slam +9 (1d6+4 plus 1d6 acid and _[[universal monster rules/Grab|grab]]_)
**Special Attacks** acid, _[[universal monster rules/Constrict|constrict]]_ (1d6+4 plus 1d6 acid), enliven

##### Statistics
**Str** 16, **Dex** 1, **Con** 22, **Int** —, **Wis** 1, **Cha** 1
**Base Atk** +6; **CMB** +9 (+13 grapple); **CMD** 14 (can't be tripped)
**Skills** Stealth -4 (+16 in forests and plains areas); **Racial Modifier** +0 Stealth (+20 in forest and plains environs)

##### Ecology

**Environment** temperate forest or plains
**Organization** solitary
**Treasure** none

### Special Abilities

**Acid (Ex)** A _[[monsters/Verdurous Ooze|verdurous ooze]]_ secretes a digestive acid that dissolves flesh and metal quickly. Each time a creature takes damage from a _verdurous ooze_’s acid, the creature’s metal equipment and armor take the same amount of damage from the acid. A DC 21 Reflex save prevents damage to such items. A metal or natural weapon that strikes a _verdurous ooze_ takes 1d6 points of acid damage unless the weapon’s wielder succeeds on a DC 21 Reflex save. If a _verdurous ooze_ remains in contact with a metal object for 1 full round, it inflicts 20 points of acid damage (no save) on the object. The save DCs are Constitution-based.

**Enliven (Sp)** The chemicals emitted by a _verdurous ooze_ cause nearby plants to twitch into life. While in areas covered in natural growth, all squares within 15 feet of the _verdurous ooze_ are affected as if by the spell _[[spells/Entangle|entangle]]_. The _verdurous ooze_ has no control over this effect, and if dispelled the effect renews after 1d4 rounds. The save DC is Constitution-based.
**Sleep Aura (Su)** The chemicals emitted by a _verdurous ooze_ have a stronger and opposite effect on living, non-plant creatures that come within a 30-foot radius. All living creatures within the area must make a DC 21 Will save or fall asleep for a number of rounds equal to the ooze’s HD. Creatures immune to poison are also immune to this effect. Whether or not the save is successful, that creature cannot be affected again by the same _verdurous ooze_’s sleep aura for 24 hours. This is a nonmagical sleep effect. The save DC is Constitution-based.
**_Split_ (Ex)** Slashing and piercing weapons deal no damage to a _verdurous ooze_. Instead, if the _verdurous ooze_ would have taken 10 or more points of damage from a single slashing or piercing attack, it splits into two identical oozes, each with half of the original’s current hit points (round down). Slashing or piercing attacks that deal less than 10 points of damage do not cause a _verdurous ooze_ to _split_. Damage from multiple slashing or piercing attacks is not cumulative. A _verdurous ooze_ with 15 hit points or less cannot be further _split_ and dies if reduced to 0 hit points.

##### Description

Verdurous oozes are animate masses of protoplasm of a sickly green hue. At rest, their flat bodies stand roughly 5 inches tall and can stretch out to a wide diameter, their surfaces blossoming into what look like thick tangles of mossy roots and gnarled vegetation as they lie still. Known to emit _[[conditions/Invisible|invisible]]_ but dangerous chemicals, these masses of slinking muck cause nearby plants to writhe and coil as if alive, while shocking animals into a temporary but deathly torpor. As such, they rarely must hunt to find food, instead _[[items/Armor Magic Abilities/Sensing|sensing]]_ passing creatures and preying upon them after they succumb to the oozes’ sleep aura. Always _[[curses/Ravenous|ravenous]]_, the powerful acids that comprise these oozes quickly dissolve the flesh of their meals.

A _verdurous ooze_ typically weighs 300 pounds and can easily spread to fill a 5-foot-square area. While moving, such crawling muck rises only a few inches tall, though its structure might grow and boil up to a height of 2 or 3 feet if let undisturbed for a matter of days. Spontaneously grown structures collapse and melt back into the ooze’s body as soon as it begins moving again.