---
cssclass: [monsters]
title1: Fell Flotsam
is_3.5: true
desc_short: Bobbing along the surface of the water is a patch of oily blackness, like
  a piece of the night sky afloat on the waves. Vaguely discernable are lumps and
  protrusions, as if it were a tangle of bracken and flotsam. It has a slight sheen
  and, most disturbingly of all, seems to be floating along against the current.
title2: Fell Flotsam
CR: 6
sources:
- name: Rivers into Darkness
  page: 28
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy82qf
alignment: NE
size: Large
type: undead
initiative:
  bonus: -1
senses:
  blind: true
  blindsight: 60
AC:
  AC: 4
  touch: 4
  flat_footed: 4
  components:
    dex: -5
    size: -1
HP:
  HP: 91
  long: 14d12
saves:
  fort: 4
  ref: -1
  will: 6
DR:
- amount: 10
  weakness: bludgeoning and magic
immunities:
- acid
- cold
- ooze traits
- undead traits
resistances:
  electricity: 10
  sonic: 10
weaknesses:
- fire vulnerability
speeds:
  base: 10
  climb: 10
  swim: 40
attacks:
  melee:
  - - text: 2 slams +13 (2d4+6 plus 1d6 acid)
      entries:
      - - damage: 2d4+6
        - damage: 1d6
          type: acid
      count: 2
      attack: slams
      bonus:
      - 13
  special:
  - acid
  - constrict (4d4+6 plus 1d6 acid)
  - hypnotic pattern
  - improved grab
space: 10
reach: 5
ability_scores:
  STR: 22
  DEX: 1
  CON:
  INT: 2
  WIS: 1
  CHA: 16
BAB: 7
grapple_3.5: 17
feats:
- name: Ability Focus (hypnotic pattern)
- name: Improved Initiative
- name: Iron Will
- name: Stealthy
- name: Weapon Focus (slam)
skills:
  Climb: 14
  Hide: 7
    in water: 15
  Listen: 0
  Move Silently: 9
  Swim: 14
  Spot: -5
  _racial_mods:
    Hide:
      _: 8
      in water: 16
    Move Silently:
      _: 8
ecology:
  environment: tropical marshes
  organization: solitary
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 15
    size: Large
    HD_max: 18
  - type: size
    HD_min: 19
    size: Huge
    HD_max: 24
  - type: size
    HD_min: 25
    size: Gargantuan
    HD_max: 34
special_abilities:
  Acid (Ex): A fell flotsam secretes a powerful acid that dissolves only flesh. Any
    melee hit or successful grapple check deals acid damage.
  Constrict (Ex): A fell flotsam deals automatic slam and acid damage with a successful
    grapple check.
  Hypnotic Pattern (Su): As a standard action, a fell flotsam can cause the oily sheen
    of its surface to swirl and undulate in a strangely compelling manner. This affects
    anyone who views this display as with a hypnotic pattern spell (caster level 6th).
    Those who fail a Dc 18 Will save have an overwhelming urge to approach and touch
    the swirling lights unless prevented by others. Those who approach enter the fell
    flotsam's area and allow it to make automatic constrict attacks until the victim
    is freed or dies. This constrict attack does not allow a new saving throw, as
    the fascinated individual willingly enters its embrace. The save Dc is charisma-based.
  Improved Grab (Ex): To use this ability, a fell flotsam must hit with its slam attack.
    it can then start a grapple as a free action without provoking an attack of opportunity.
    if it wins the grapple check, it establishes a hold and can constrict.
desc_long: |-
  A fell flotsam is a hideous undead creature that takes the form of a floating ooze. As such, it shares many ooze characteristics and traits. A fell flotsam is formed from the combined psyches of the deaths of many sentient creatures in some swampy area. These souls merge with the primordial muck and fecund undergrowth of the marsh to create an undead predator of limited intelligence, capable of little more than hunting living creatures in order to consume them and deposit their bleached bones on the floor of swamp pools. The creatures gain no true sustenance from such predations, but each such creature slain allows a little bit of growth in the flotsam, so after many years a fell flotsam might advance to truly prodigious size. Fell flotsam's prefer sentient prey and often ignore the natural fauna of their swamps unless they have not fed in some time.

  Environment: Fell flotsams are typically only found in jungle swamps, where both the ever-present danger that creates the requisite number of deaths and the truly prodigious amounts of plant growth can combine in the deep, fermenting muck to spawn such an abomination of undeath.

  Typical physical Characteristics: A fell flotsam resembles nothing so much as a 10-foot-diameter oil slick floating on the surface of the water. It is only a few inches thick but weighs around 3,000 pounds due to its compact mass. Though typically smooth in appearance, occasional protuberances resembling broken flotsam and debris press outward through its outer membrane, as if some primordial memory of the jungle wrack from which it is composed occasionally tries to emerge, only to be quickly reabsorbed.

---

# Fell Flotsam
Bobbing along the surface of the water is a patch of oily blackness, like a piece of the night sky afloat on the waves. Vaguely discernable are lumps and protrusions, as if it were a tangle of bracken and flotsam. It has a slight sheen and, most disturbingly of all, seems to be floating along against the current.
**Source** Rivers into _[[spells/Darkness|Darkness]]_ pg. 28

NE Large undead
**Init** -1; **Senses** blind, _[[universal monster rules/Blindsight|blindsight]]_ 60 ft.; Listen +0, Spot -5

##### Defense

**AC** 4, touch 4, _[[conditions/Flat-Footed|flat-footed]]_ 4 (-5 Dex, -1 size)
**hp** 91 (14d12)
**Fort** +4, **Ref** -1, **Will** +6
**DR** 10/bludgeoning and magic; **Immune** acid, cold, ooze traits, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** electricity 10, sonic 10
**Weaknesses** fire _[[curses/Vulnerability|vulnerability]]_

##### Offense
**Speed** 10 ft., _[[universal monster rules/Climb|climb]]_ 10 ft., swim 40 ft.
**Melee** 2 slams +13 (2d4+6 plus 1d6 acid)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** acid, _[[universal monster rules/Constrict|constrict]]_ (4d4+6 plus 1d6 acid), _[[spells/Hypnotic Pattern|hypnotic pattern]]_, improved _[[universal monster rules/Grab|grab]]_

##### Statistics
**Str** 22, **Dex** 1, **Con** —, **Int** 2, **Wis** 1, **Cha** 16
**Base Atk** +7; **Grapple** +17
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_hypnotic pattern_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** _Climb_ +14, Hide +7 (+15 in water), Listen +0, Move Silently +9, Swim +14; **Racial Modifiers** +8 Hide (+16 in water), +8 Move Silently

##### Ecology

**Environment** tropical marshes
**Organization** solitary
**Treasure** none
**Advancement** 15-18 HD (Large), 19-24 HD (Huge), 25-34 HD (Gargantuan)

### Special Abilities

**Acid (Ex)** A _[[monsters/Fell Flotsam|fell flotsam]]_ secretes a powerful acid that dissolves only flesh. Any melee hit or successful grapple check deals acid damage.

**_Constrict_ (Ex)** A _fell flotsam_ deals automatic slam and acid damage with a successful grapple check.

**_Hypnotic Pattern_ (Su)** As a standard action, a _fell flotsam_ can cause the oily sheen of its surface to swirl and undulate in a strangely compelling manner. This affects anyone who views this display as with a _hypnotic pattern_ spell (caster level 6th). Those who fail a Dc 18 Will save have an overwhelming urge to approach and touch the swirling lights unless prevented by others. Those who approach enter the _fell flotsam_’s area and allow it to make automatic _constrict_ attacks until the victim is freed or dies. This _constrict_ attack does not allow a new saving throw, as the _[[conditions/Fascinated|fascinated]]_ individual willingly enters its embrace. The save Dc is charisma-based.

**Improved _Grab_ (Ex)** To use this ability, a _fell flotsam_ must hit with its slam attack. it can then start a grapple as a free action without provoking an attack of opportunity. if it wins the grapple check, it establishes a hold and can _constrict_.

##### Description

A _fell flotsam_ is a hideous undead creature that takes the form of a floating ooze. As such, it shares many ooze characteristics and traits. A _fell flotsam_ is formed from the combined psyches of the deaths of many sentient creatures in some swampy area. These souls merge with the primordial muck and fecund undergrowth of the marsh to create an undead predator of limited intelligence, capable of little more than hunting living creatures in order to consume them and deposit their bleached bones on the floor of swamp pools. The creatures gain no true sustenance from such predations, but each such creature slain allows a little bit of growth in the flotsam, so after many years a _fell flotsam_ might advance to truly prodigious size. _Fell flotsam_’s prefer sentient prey and often ignore the natural fauna of their swamps unless they have not fed in some time.

**Environment**: Fell flotsams are typically only found in jungle swamps, where both the ever-present danger that creates the requisite number of deaths and the truly prodigious amounts of _[[spells/Plant Growth|plant growth]]_ can combine in the deep, fermenting muck to spawn such an abomination of undeath.

**Typical physical Characteristics**: A _fell flotsam_ resembles nothing so much as a 10-foot-diameter oil _[[items/Armor Magic Abilities/Slick|slick]]_ floating on the surface of the water. It is only a few inches thick but weighs around 3,000 pounds due to its compact mass. Though typically smooth in appearance, occasional protuberances resembling _[[conditions/Broken|broken]]_ flotsam and debris press outward through its outer membrane, as if some primordial memory of the jungle wrack from which it is composed occasionally tries to emerge, only to be quickly reabsorbed.