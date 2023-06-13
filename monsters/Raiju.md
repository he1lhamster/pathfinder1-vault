---
cssclass: [monsters]
title1: Raiju
desc_short: The air around this strange, pale animal sparks with erratic flashes of
  static electricity, its body constantly twitching as if filled to capacity with
  the energy. It suddenly perks up, alert and seemingly ready to bolt.
title2: Raiju
CR: 5
sources:
- name: 'Pathfinder #53: Tide of Honor'
  page: 90
  link: http://paizo.com/pathfinder/v5748btpy8mh0
XP: 1600
alignment: CN
size: Small
type: outsider
subtypes:
- air
- extraplanar
- shapechanger
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 15
  flat_footed: 15
  components:
    dex: 4
    natural: 4
    size: 1
HP:
  HP: 51
  long: 6d10+18
saves:
  fort: 8
  ref: 11
  will: 2
immunities:
- electricity
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claw +8 (1d3+1 plus 1d6 electricity)
      entries:
      - - damage: 1d3+1
        - damage: 1d6
          type: electricity
      count: 2
      attack: claw
      bonus:
      - 8
    - text: tail slap +3 (1d4 plus 1d6 electricity)
      entries:
      - - damage: 1d4
        - damage: 1d6
          type: electricity
      attack: tail slap
      bonus:
      - 3
  special:
  - shocking burst
spell_like_abilities:
  entries:
  - name: call lightning
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
    other: thunderstorm only
  sources:
  - name: default
    CL: 5
ability_scores:
  STR: 12
  DEX: 19
  CON: 16
  INT: 5
  WIS: 11
  CHA: 10
BAB: 6
CMB: 6
CMD: 20
CMD_other: 24 vs. trip
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Acrobatics: 10
    when jumping: 14
  Fly: 19
  Perception: 9
languages:
- Auran
special_qualities:
- change shape (Small animal only)
- electric body
ecology:
  environment: any land or sky (lightning storms)
  organization: solitary, pair, or group (3-12)
  treasure_type: none
special_abilities:
  Change Shape (Su): On the Material Plane, a raiju typically assumes the form of
    a badger, cat, giant rat, monkey, weasel, or wolf (as per beast shape II) to blend
    in with native wildlife. Even in these forms, however, it typically has pale coloration
    and lightninglike patterns.
  Electric Body (Su): As an immediate action, a raiju can transform itself into a
    ball of living lightning. While in this form, the raiju gains the incorporeal
    subtype and incorporeal quality. It only takes half damage from corporeal sources
    if they are magical (it takes no damage from nonmagical weapons and objects).
    Additionally, it sparks with electricity while it is in this form. Any creature
    that touches the raiju with a natural or unarmed attack or whose square the raiju
    passes through during its movement must succeed at a DC 17 Reflex save or take
    2d6 points of electricity damage. The save DC is Dexterity-based. In normal weather,
    a raiju can remain incorporeal for a number of rounds per day equal to its Hit
    Dice, though it can remain incorporeal for as long as it pleases during a thunderstorm.
  Shocking Burst (Su): Besides dealing normal slashing damage, the claw and tail of
    a raiju are considered to have the shocking burst weapon special quality. They
    deal 1d6 extra points of electrical damage on a normal hit and an additional 1d10
    points on a critical hit.
desc_long: |-
  Raijus are beings of living electricity that cross the border between the mundane world and their native plane, a region of the Plane of Air alive with endless thunderstorms. Raijus can be involuntarily hurled across the dimensions by a powerful lightning bolt originating in the Plane of Air, or might be called by magic users to do their bidding. When the weather is calm, raijus are quiet, and assume the forms of Tiny or Small animals such as cats, raccoon dogs, monkeys, or weasels. As weather gets worse, however, so do their tempers. In their real form, raijus appear as lean, foxlike creatures with long, sharp claws and luminous eyes, shrouded by crackling electricity. These swift, even panicky, creatures are charged with the electricity of their native realm, and those who touch them risk receiving a deadly shock. In times of great distress, they transform entirely into living electricity, a force that few barriers can contain and even fewer creatures can survive the passage of.

  In their natural forms, raijus measure about 3-1/2 feet long and weigh 40 pounds, but they often take the form of small mammals when not on the Plane of Air. They can be still recognized as raijus in this form, however, as they bear markings suggestive of jagged lightning.

---

# Raiju
The air around this strange, pale animal sparks with erratic flashes of static electricity, its body constantly twitching as if filled to capacity with the energy. It suddenly perks up, alert and seemingly ready to bolt.
**Source** Pathfinder #53: Tide of Honor pg. 90
**XP** 1,600

CN Small outsider (air, extraplanar, shapechanger)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +9

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +4 natural, +1 size)
**hp** 51 (6d10+18)
**Fort** +8, **Ref** +11, **Will** +2
**Immune** electricity

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** 2 claw +8 (1d3+1 plus 1d6 electricity), tail slap +3 (1d4 plus 1d6 electricity)
**Special Attacks** _[[items/Weapon Magic Abilities/Shocking Burst|shocking burst]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5)
3/day—_[[spells/Call Lightning|call lightning]]_
1/day—_[[spells/Control Weather|control weather]]_ (thunderstorm only)

##### Statistics
**Str** 12, **Dex** 19, **Con** 16, **Int** 5, **Wis** 11, **Cha** 10
**Base Atk** +6; **CMB** +6; **CMD** 20 (24 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +10 (+14 when jumping), Fly +19, Perception +9
**Languages** Auran
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small animal only), electric body

##### Ecology

**Environment** any land or sky (lightning storms)
**Organization** solitary, pair, or group (3–12)
**Treasure** None

### Special Abilities

**_Change Shape_ (Su) **On the Material Plane, a _[[monsters/Raiju|raiju]]_ typically assumes the form of a _[[monsters/Badger|badger]]_, cat, giant rat, monkey, weasel, or _[[monsters/Wolf|wolf]]_ (as per _[[spells/Beast Shape II|beast shape II]]_) to _[[spells/Blend|blend]]_ in with native wildlife. Even in these forms, however, it typically has pale coloration and lightninglike patterns.

**Electric Body (Su) **As an immediate action, a _raiju_ can transform itself into a ball of living lightning. While in this form, the _raiju_ gains the _[[universal monster rules/Incorporeal|incorporeal]]_ subtype and _incorporeal_ quality. It only takes half damage from corporeal sources if they are magical (it takes no damage from nonmagical weapons and objects). Additionally, it sparks with electricity while it is in this form. Any creature that touches the _raiju_ with a natural or unarmed attack or whose square the _raiju_ passes through during its movement must succeed at a DC 17 Reflex save or take 2d6 points of electricity damage. The save DC is Dexterity-based. In normal weather, a _raiju_ can remain _incorporeal_ for a number of rounds per day equal to its Hit Dice, though it can remain _incorporeal_ for as long as it pleases during a thunderstorm.
**_Shocking Burst_ (Su) **Besides dealing normal slashing damage, the claw and tail of a _raiju_ are considered to have the _shocking burst_ weapon special quality. They deal 1d6 extra points of electrical damage on a normal hit and an additional 1d10 points on a critical hit.

##### Description

Raijus are beings of living electricity that cross the border between the mundane world and their native plane, a region of the Plane of Air alive with endless thunderstorms. Raijus can be involuntarily hurled across the dimensions by a powerful _[[spells/Lightning Bolt|lightning bolt]]_ originating in the Plane of Air, or might be _[[items/Weapon Magic Abilities/Called|called]]_ by magic users to do their bidding. When the weather is calm, raijus are quiet, and assume the forms of Tiny or Small animals such as cats, raccoon dogs, monkeys, or weasels. As weather gets worse, however, so do their tempers. In their real form, raijus appear as lean, foxlike creatures with long, sharp claws and luminous eyes, shrouded by crackling electricity. These swift, even panicky, creatures are charged with the electricity of their native realm, and those who touch them risk receiving a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ _[[items/Weapon Magic Abilities/Shock|shock]]_. In times of great distress, they transform entirely into living electricity, a force that few barriers can contain and even fewer creatures can survive the passage of.

In their natural forms, raijus measure about 3-1/2 feet long and weigh 40 pounds, but they often take the form of small mammals when not on the Plane of Air. They can be still recognized as raijus in this form, however, as they bear markings suggestive of jagged lightning.