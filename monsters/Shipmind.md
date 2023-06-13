---
cssclass: [monsters]
title1: Shipmind
desc_short: This yellowy viscous liquid bubbles in a large tank suspended by strangely
  organic cables. Wisps of white gas occasionally escape the roiling fluid.
title2: Shipmind
CR: 13
sources:
- name: 'Pathfinder #88: Valley of the Brain Collectors'
  page: 86
  link: http://paizo.com/products/btpy99sg?Pathfinder-Adventure-Path-88-Valley-of-the-Brain-Collectors
XP: 25600
alignment: CE
size: Huge
type: ooze
initiative:
  bonus: 13
senses:
  blindsight: 60
  detect good: true
  detect law: true
  detect magic: true
AC:
  AC: 27
  touch: 17
  flat_footed: 18
  components:
    dex: 9
    armor: 10
    size: -2
HP:
  HP: 161
  long: 14d8+98
saves:
  fort: 11
  ref: 13
  will: 12
defensive_abilities:
- amorphous
- thought disruption
DR:
- amount: 10
  weakness: '-'
immunities:
- bludgeoning
- charm effects
- electricity
- fire
- ooze traits
SR: 24
weaknesses:
- limited mobility
- vulnerable to cold
speeds:
  0 ft. or: 10
  0 ft. or_other: limited mobility
attacks:
  melee:
  - - text: 3 slams +20 (1d8+12 plus 1d4 Int damage and grab)
      entries:
      - - damage: 1d8+12
        - damage: 1d4
          type: Int damage
        - effect: grab
      count: 3
      attack: slams
      bonus:
      - 20
  ranged:
  - - text: plasma bolt +17 touch (10d6 plasma/19-20)
      entries:
      - - damage: 10d6
          type: plasma
          crit_range: 19-20
      attack: plasma bolt
      bonus:
      - 17
      touch: true
  special:
  - immerse
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: enthrall
    source: default
    freq: At will
    DC: 17
  - name: sending
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: quickened touch of idiocy
    source: default
    freq: 3/day
  - name: confusion
    source: default
    freq: 1/day
    DC: 19
  - name: crushing despair
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 13
    concentration: 18
ability_scores:
  STR: 34
  DEX: 28
  CON: 24
  INT: 21
  WIS: 23
  CHA: 21
BAB: 10
CMB: 24
CMD: 43
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Improved Critical (plasma bolt)
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (touch of idiocy)
skills:
  Knowledge (engineering): 19
  Knowledge (geography): 19
  Knowledge (nature): 19
  Knowledge (planes): 19
  Knowledge (religion): 19
  Perception: 20
  Sense Motive: 20
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Infernal
- Undercommon
- Protean
- telepathy 60 ft.
special_qualities:
- container
- ship interface
ecology:
  environment: any (Dominion of the Black ships)
  organization: solitary
  treasure_type: standard
  treasure:
  - mostly gemstones
special_abilities:
  Container (Ex): A shipmind dwells within an immobile container of partially organic
    material grown by its Dominion masters. This container functions somewhat like
    a suit of armor for the shipmind. A shipmind container has hardness 10 and 240
    hit points, and can be damaged by sunder attempts. A shipmind container that gains
    the broken quality grants only a +5 armor bonus to the shipmind within, and does
    not allow the shipmind to heal negative levels gained during a prolonged period
    outside of the container (see Limited Mobility). The partially crystalline nature
    of a shipmind container makes it vulnerable to shatter spells, and sonic damage
    bypasses the container's hardness and inflicts full damage.
  Immerse (Ex): When a shipmind in its container successfully grabs a Large or smaller
    target with one of its slam attacks, it can attempt to drag that target into its
    body as a swift action. To immerse a creature, the shipmind must attempt a combat
    maneuver check (as though attempting to pin the opponent). If it succeeds, the
    prey is pulled into the container with the shipmind and immediately takes 6d6
    points of plasma damage (half of which is electricity and half of which is fire)
    and 1d4 points of Intelligence damage-a successful DC 24 Fortitude save halves
    the plasma damage and negates the Intelligence damage. A creature that remains
    immersed takes this damage again every following round at the start of the shipmind's
    turn. In addition, an immersed creature is in danger of suffocating. A creature
    can attempt to escape immersion by making a successful combat maneuver check or
    Escape Artist check, as if it were attempting to escape a pin. If the shipmind's
    container has the broken condition, attempts to escape in this manner gain a +8
    bonus.
  Limited Mobility (Ex): Unlike most oozes, a shipmind cannot exist outside of the
    partially organic container it was originally created in-this container serves
    the shipmind as its “skin.” While inside its container, a shipmind has a speed
    of 0 feet. When it leaves its container, it gains a speed of 10 feet, but loses
    its armor bonus to AC. A shipmind can exist outside of its container for 1 hour
    without consequences, but at the start of each subsequent hour it gains 1 negative
    level as its body starts to dissolve. These negative levels cannot be restored
    by any means save by returning to an appropriate shipmind container, at which
    point they are removed at a rate of 1 level per hour.
  Plasma Bolt (Su): As a standard action, a shipmind can fire a bolt of plasma at
    a target within 300 feet (no range increment). On a hit, a blast of plasma deals
    10d6 damage, half of which is electricity damage and half of which is fire damage.
  Ship Interface (Ex): As long as a shipmind is interfaced with a Dominion vessel,
    it can observe events within the ship or within 90 feet of its exterior hull as
    if via clairaudience/clairvoyance for as long as the shipmind concentrates. While
    concentrating on an area, the shipmind can activate traps or other ship systems
    in the area as a swift action; it can even converse with creatures in the area
    by vibrating the metal and strange membranes in the walls.
  Thought Disruption (Su): The substance that makes up a shipmind ooze is charged
    with alien psychic energy that is toxic to the minds of most life forms. A creature
    who willfully touches an ooze (via a touch attack, natural weapon attack, or unarmed
    strike) or is struck by its slam attack must make a DC 22 Will save or take 1d4
    points of Intelligence damage. This is a mind-affecting confusion effect. The
    save DC is Charisma-based.
desc_long: |-
  The enigmatic shipminds are painstakingly engineered creations of Dominion fleshfarms, molded and formed over the course of years to pilot the massive organic spacecraft the aliens use to navigate the Dark Tapestry.

  Intimately bound to their vessels, shipminds oversee the health and function of the ships they control. They maintain this single-minded task for as long as a thousand years before they must be recycled and rebuilt.

  A shipmind resides within a specially designed containers on a craft, connected to the ship's greater workings via varying forms of physical interface. These oozes generally follow orders from superiors stationed on their spacecraft, though coaxing is sometimes necessary in order to get these strange creatures to follow direct orders. This is due in part to the fact that these engineered creatures are fanatically devoted to the Dominion's inscrutable faith, with rigid beliefs regarding orthodoxy. Rumors persist of especially radical shipmind oozes going beyond defiance and actually slaying their passengers, a task made frightfully easy due to the mastery each ooze has over every aspect of its spacecraft's function (such as life support and internal security appendages and creatures). Some have been known to plunge their vessel into a star or black hole in moments of defiance or religious ecstasy, leaving the rest of the ship's crew helpless and unable to convince the shipmind to abandon its actions.

  As a shipmind reaches more advanced age, it becomes increasingly pedantic and difficult to control. Such oozes often demand small offerings, sacrifices of lesser creatures, or the powering down of ship's systems they deem superf luous or “unpure.” At a certain point, the shipmind is recycled, poured from its container into vats to serve as nutrients for the cultivation of a replacement. Fragments of the previous shipmind's intellect and skills carry over into the newly created ooze, ensuring that a sort of entrenched memory and institutional knowledge persist through the generations.

---

# Shipmind
This yellowy viscous liquid bubbles in a large tank suspended by strangely organic cables. Wisps of white gas occasionally escape the roiling fluid.
**Source** Pathfinder #88: Valley of the Brain Collectors pg. 86
**XP** 25,600
CE Huge ooze
**Init** +13; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/Detect Magic|detect magic]]_; Perception +20

##### Defense

**AC** 27, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+9 Dex, +10 armor, –2 size)
**hp** 161 (14d8+98)
**Fort** +11, **Ref** +13, **Will** +12
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_, thought _[[items/Weapon Magic Abilities/Disruption|disruption]]_; **DR** 10/—; **Immune** bludgeoning, charm effects, electricity, fire, ooze traits; **SR** 24
**Weaknesses** limited _[[feats/Mobility|mobility]]_, vulnerable to cold

##### Offense
**Speed** 0 ft. or 10 ft. (limited _mobility_)
**Melee** 3 slams +20 (1d8+12 plus 1d4 Int damage and _[[universal monster rules/Grab|grab]]_)
**Ranged** plasma bolt +17 touch (10d6 plasma/19–20)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** immerse
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +18)
Constant—_detect good_, _detect law_, _detect magic_
At will—_[[spells/Enthrall|enthrall]]_ (DC 17), _[[spells/Sending|sending]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 20)
3/day—quickened _[[spells/Touch of Idiocy|touch of idiocy]]_
1/day—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Crushing Despair|crushing despair]]_ (DC 19)

##### Statistics
**Str** 34, **Dex** 28, **Con** 24, **Int** 21, **Wis** 23, **Cha** 21
**Base Atk** +10; **CMB** +24; **CMD** 43 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (plasma bolt), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_touch of idiocy_)
**Skills** Knowledge (engineering) +19, Knowledge (geography) +19, Knowledge (nature) +19, Knowledge (planes) +19, Knowledge (religion) +19, Perception +20, Sense Motive +20
**Languages** Abyssal, Aklo, Common, Draconic, Infernal, Undercommon, Protean; _[[universal monster rules/Telepathy|telepathy]]_ 60 ft.
**SQ** container, ship interface

##### Ecology

**Environment** any (Dominion of the Black ships)
**Organization** solitary
**Treasure** standard (mostly gemstones)

### Special Abilities

**Container (Ex)** A _[[monsters/Shipmind|shipmind]]_ dwells within an immobile container of partially organic material grown by its Dominion masters. This container functions somewhat like a suit of armor for the _shipmind_. A _shipmind_ container has hardness 10 and 240 hit points, and can be damaged by sunder attempts. A _shipmind_ container that gains the _[[conditions/Broken|broken]]_ quality grants only a +5 armor bonus to the _shipmind_ within, and does not allow the _shipmind_ to _[[spells/Heal|heal]]_ negative levels gained during a prolonged period outside of the container (see Limited _Mobility_). The partially crystalline nature of a _shipmind_ container makes it vulnerable to _[[spells/Shatter|shatter]]_ spells, and sonic damage bypasses the container’s hardness and inflicts full damage.

**Immerse (Ex)** When a _shipmind_ in its container successfully grabs a Large or smaller target with one of its slam attacks, it can attempt to drag that target into its body as a swift action. To immerse a creature, the _shipmind_ must attempt a combat maneuver check (as though attempting to pin the opponent). If it succeeds, the prey is pulled into the container with the _shipmind_ and immediately takes 6d6 points of plasma damage (half of which is electricity and half of which is fire) and 1d4 points of Intelligence damage—a successful DC 24 Fortitude save halves the plasma damage and negates the Intelligence damage. A creature that remains immersed takes this damage again every following round at the start of the _shipmind_’s turn. In addition, an immersed creature is in danger of suffocating. A creature can attempt to escape immersion by making a successful combat maneuver check or Escape Artist check, as if it were attempting to escape a pin. If the _shipmind_’s container has the _broken_ condition, attempts to escape in this manner gain a +8 bonus.

**Limited _Mobility_ (Ex)** Unlike most oozes, a _shipmind_ cannot exist outside of the partially organic container it was originally created in—this container serves the _shipmind_ as its “skin.” While inside its container, a _shipmind_ has a speed of 0 feet. When it leaves its container, it gains a speed of 10 feet, but loses its armor bonus to AC. A _shipmind_ can exist outside of its container for 1 hour without consequences, but at the start of each subsequent hour it gains 1 negative level as its body starts to dissolve. These negative levels cannot be restored by any means save by returning to an appropriate _shipmind_ container, at which point they are removed at a rate of 1 level per hour.

**Plasma Bolt (Su)** As a standard action, a _shipmind_ can fire a bolt of plasma at a target within 300 feet (no range increment). On a hit, a blast of plasma deals 10d6 damage, half of which is electricity damage and half of which is fire damage.
**Ship Interface (Ex)** As long as a _shipmind_ is interfaced with a Dominion vessel, it can observe events within the ship or within 90 feet of its exterior hull as if via clairaudience/clairvoyance for as long as the _shipmind_ concentrates. While concentrating on an area, the _shipmind_ can activate traps or other ship systems in the area as a swift action; it can even converse with creatures in the area by vibrating the metal and strange membranes in the walls.

**Thought _Disruption_ (Su)** The substance that makes up a _shipmind_ ooze is charged with alien _[[classes/Psychic|psychic]]_ energy that is _[[items/Weapon Magic Abilities/Toxic|toxic]]_ to the minds of most life forms. A creature who willfully touches an ooze (via a touch attack, natural weapon attack, or unarmed strike) or is struck by its slam attack must make a DC 22 Will save or take 1d4 points of Intelligence damage. This is a mind-affecting _confusion_ effect. The save DC is Charisma-based.

##### Description

The enigmatic shipminds are painstakingly engineered creations of Dominion fleshfarms, molded and formed over the course of years to pilot the massive organic spacecraft the aliens use to navigate the Dark Tapestry.

Intimately bound to their vessels, shipminds oversee the health and function of the ships they control. They maintain this single-minded task for as long as a thousand years before they must be recycled and rebuilt.

A _shipmind_ resides within a specially designed containers on a craft, connected to the ship’s greater workings via varying forms of physical interface. These oozes generally follow orders from superiors stationed on their spacecraft, though coaxing is sometimes necessary in order to get these strange creatures to follow direct orders. This is due in part to the fact that these engineered creatures are fanatically devoted to the Dominion’s inscrutable faith, with rigid beliefs regarding orthodoxy. Rumors persist of especially radical _shipmind_ oozes going beyond defiance and actually slaying their passengers, a task made frightfully easy due to the mastery each ooze has over every aspect of its spacecraft’s function (such as life support and internal security appendages and creatures). Some have been known to plunge their vessel into a star or black hole in moments of defiance or religious ecstasy, leaving the rest of the ship’s crew _[[conditions/Helpless|helpless]]_ and unable to convince the _shipmind_ to abandon its actions.

As a _shipmind_ reaches more advanced age, it becomes increasingly pedantic and difficult to control. Such oozes often _[[spells/Demand|demand]]_ small offerings, sacrifices of lesser creatures, or the powering down of ship’s systems they deem superf luous or “unpure.” At a certain point, the _shipmind_ is recycled, poured from its container into vats to serve as nutrients for the cultivation of a replacement. Fragments of the previous _shipmind_’s intellect and skills carry over into the newly created ooze, ensuring that a sort of entrenched memory and institutional knowledge persist through the generations.