---
cssclass: [monsters]
title1: Emkrah
is_3.5: true
desc_short: Lashing furiously, this semi-gelatinous abomination surges forward upon
  a wave of tentacular legs. These artery-like legs knot into a single stalk capped
  by a bulbous, fleshy head dominated by a huge mouth and a yawning, empty eyesocket.
  The thing's disgusting trunk and head float within a transparent body of vein-riddled
  ooze, like a gigantic jellyfish.
title2: Emkrah
CR: 9
sources:
- name: "Pathfinder #21: The Jackal's Price"
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy87uv
alignment: Always CE
size: Large
type: aberration
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 12
  flat_footed: 9
  components:
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 126
  long: 12d8+72
saves:
  fort: 12
  ref: 7
  will: 11
immunities:
- acid
- cold
- critical hits
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +15 (1d8+7 plus 1d8 acid)
      entries:
      - - damage: 1d8+7
        - damage: 1d8
          type: acid
      attack: bite
      bonus:
      - 15
    - text: 4 tentacle slams +13 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 4
      attack: tentacle slams
      bonus:
      - 13
  ranged:
  - - text: acid spittle +11 touch (1d8 acid)
      entries:
      - - damage: 1d8
          type: acid
      attack: acid spittle
      bonus:
      - 11
      touch: true
  special:
  - acid spittle
  - doom gaze
  - improved grab
  - swallow whole
space: 10
reach: 10
ability_scores:
  STR: 25
  DEX: 17
  CON: 22
  INT: 8
  WIS: 17
  CHA: 18
BAB: 9
grapple_3.5: 20
feats:
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Mobility
skills:
  Climb: 10
  Spot: 12
  Swim: 10
  Listen: 3
special_qualities:
- acidic
- amorphous
ecology:
  environment: any
  organization: solitary
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 12
    size: Large
    HD_max: 19
  - type: size
    HD_min: 20
    size: Huge
    HD_max: 31
  - type: size
    HD_min: 32
    size: Gargantuan
special_abilities:
  Acid Spittle (Ex): An emkrah can spit a glob of its highly corrosive goo up to 30
    feet as a standard action. This is a ranged touch attack with no range increment.
    Creatures struck by this acid spittle take 1d8 points of acid damage.
  Acidic (Ex): An emkrah's body is little more than a shell of gelatinous digestive
    acid that dissolves organic material quickly. Any fleshy, living creature that
    attacks an emkrah with a natural weapon or an unarmed strike, or attempts to grapple
    a emkrah, takes 1d8 points of acid damage.
  Amorphous (Ex): An emkrah is not subject to critical hits. It cannot be flanked.
  Doom Gaze (Su): Deals 1d6 points of damage, 30 feet, Will DC 20 negates. If an emkrah
    actively uses its gaze upon a creature, it deals 1d8 points of damage. Evil creatures
    gain a +2 bonus on their saves versus an emkrah's doom gaze. The save DC is Charisma-based.
  Improved Grab (Ex): To use this ability, an emkrah must hit with one of its tentacle
    attacks. It can then attempt to start a grapple as a free action without provoking
    an attack of opportunity.
  Swallow Whole (Ex): An emkrah can attempt to swallow a grappled opponent of Medium
    or smaller size by making a successful grapple check. (A emkrah doesn't actually
    “swallow” the opponent-it engulfs it within its gelatinous form-but the effect
    is essentially the same.) Once inside, the opponent takes an automatic 8 points
    of acid damage per round from the beast's corrosive body. An emkrah can continue
    to bite a creature that has been swallowed whole. A swallowed creature can cut
    its way out by dealing 5 points of damage to the emkrah (AC 22). An emkrah's body
    can hold 1 Medium, 2 Small, 8 Tiny, 32 Diminutive or smaller creatures.
desc_long: |-
  The misbegotten offspring of the god of destruction, emkrahs are the Spawn of Rovagug that will never be. Taking their names from the Kelish word for wrongful births, these horrendous beings hatch from the repulsive egg sacks known as Rough Seeds, grotesque expulsions of Rovagug himself. While not all seeds hatch, those that do draw upon the life force of destructive beings nearby, using such creatures' essences to fuel their grotesque metamorphoses. Once hatched, emkrahs never develop into full-fledged Spawn of Rovagug, but their smaller size and strange births do nothing to curb their destructive natures, which mark them as true scions of the god of disaster.

  Emkrahs vary widely in size and form, with many having excess tentacles, strange colorations, multiple eyes, and other abnormalities. Most, however, measure 10 feet tall from their tentacles to the top of their gelatinous shells and weigh approximately 400 pounds.

---

# Emkrah
Lashing furiously, this semi-gelatinous abomination surges forward upon a wave of tentacular legs. These artery-like legs knot into a single stalk capped by a bulbous, fleshy head dominated by a huge mouth and a yawning, empty eyesocket. The thing’s disgusting trunk and head float within a transparent body of vein-riddled ooze, like a gigantic jellyfish.
**Source** Pathfinder #21: The _[[monsters/Jackal|Jackal]]_'s Price pg. 80
Always CE Large aberration
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +3, Spot +12

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 9 (+3 Dex, +10 natural, -1 size)
**hp** 126 (12d8+72)
**Fort** +12, **Ref** +7, **Will** +11
**Immune** acid, cold, critical hits

##### Offense
**Speed** 30 ft.
**Melee** bite +15 (1d8+7 plus 1d8 acid) and 4 tentacle slams +13 (1d6+3)
**Ranged** acid spittle +11 touch (1d8 acid)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** acid spittle, _[[spells/Doom|doom]]_ _[[universal monster rules/Gaze|gaze]]_, improved _[[universal monster rules/Grab|grab]]_, _[[universal monster rules/Swallow Whole|swallow whole]]_

##### Statistics
**Str** 25, **Dex** 17, **Con** 22, **Int** 8, **Wis** 17, **Cha** 18
**Base Atk** +9; **Grapple** +20
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, Dodge, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +10, Spot +12, Swim +10
**SQ** acidic, _[[universal monster rules/Amorphous|amorphous]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none
**Advancement** 12-19 HD (Large), 20-31 HD (Huge), 32+ HD (Gargantuan)

### Special Abilities

**Acid Spittle (Ex)** An _[[monsters/Emkrah|emkrah]]_ can spit a glob of its highly _[[items/Weapon Magic Abilities/Corrosive|corrosive]]_ goo up to 30 feet as a standard action. This is a ranged touch attack with no range increment. Creatures struck by this acid spittle take 1d8 points of acid damage.

**Acidic (Ex)** An _emkrah_’s body is little more than a shell of gelatinous digestive acid that dissolves organic material quickly. Any fleshy, living creature that attacks an _emkrah_ with a natural weapon or an unarmed strike, or attempts to grapple a _emkrah_, takes 1d8 points of acid damage.

**_Amorphous_ (Ex)** An _emkrah_ is not subject to critical hits. It cannot be flanked.

**_Doom_ _Gaze_ (Su)** Deals 1d6 points of damage, 30 feet, Will DC 20 negates. If an _emkrah_ actively uses its _gaze_ upon a creature, it deals 1d8 points of damage. Evil creatures gain a +2 bonus on their saves versus an _emkrah_’s _doom_ _gaze_. The save DC is Charisma-based.

**Improved _Grab_ (Ex)** To use this ability, an _emkrah_ must hit with one of its tentacle attacks. It can then attempt to start a grapple as a free action without provoking an attack of opportunity.
**_Swallow Whole_ (Ex)** An _emkrah_ can attempt to swallow a _[[conditions/Grappled|grappled]]_ opponent of _[[classes/Medium|Medium]]_ or smaller size by making a successful grapple check. (A _emkrah_ doesn’t actually “swallow” the opponent—it engulfs it within its gelatinous form—but the effect is essentially the same.) Once inside, the opponent takes an automatic 8 points of acid damage per round from the beast’s _corrosive_ body. An _emkrah_ can continue to bite a creature that has been swallowed whole. A swallowed creature can cut its way out by dealing 5 points of damage to the _emkrah_ (AC 22). An _emkrah_’s body can hold 1 _Medium_, 2 Small, 8 Tiny, 32 Diminutive or smaller creatures.

##### Description

The misbegotten offspring of the god of _[[spells/Destruction|destruction]]_, emkrahs are the Spawn of Rovagug that will never be. Taking their names from the Kelish word for wrongful births, these horrendous beings hatch from the repulsive egg sacks known as Rough Seeds, grotesque expulsions of Rovagug himself. While not all seeds hatch, those that do draw upon the life force of destructive beings nearby, using such creatures’ essences to fuel their grotesque metamorphoses. Once hatched, emkrahs never develop into full-fledged Spawn of Rovagug, but their smaller size and strange births do nothing to curb their destructive natures, which mark them as true scions of the god of disaster.

Emkrahs vary widely in size and form, with many having excess tentacles, strange colorations, multiple eyes, and other abnormalities. Most, however, measure 10 feet tall from their tentacles to the top of their gelatinous shells and weigh approximately 400 pounds.