---
cssclass: [monsters]
title1: Zephyr
desc_short: This blue-furred horse with a cloudlike mane and tail has gray, humanlike
  eyes that show obvious intelligence.
title2: Zephyr
CR: 12
sources:
- name: 'Pathfinder #101: The Kintargo Contract'
  page: 90
  link: http://paizo.com/products/btpy9hdr?Pathfinder-Adventure-Path-101-The-Kintargo-Contract
XP: 19200
alignment: CN
size: Large
type: fey
subtypes:
- air
- shapechanger
initiative:
  bonus: 9
senses:
  low-light vision: true
  wind senses: true
AC:
  AC: 27
  touch: 19
  flat_footed: 17
  components:
    dex: 9
    dodge: 1
    natural: 8
    size: -1
HP:
  HP: 168
  long: 16d6+112
saves:
  fort: 11
  ref: 19
  will: 15
DR:
- amount: 10
  weakness: cold iron
immunities:
- electricity
resistances:
  cold: 10
  sonic: 10
speeds:
  base: 60
  fly: 200
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +16 (1d8+7 plus 2d6 sonic)
      entries:
      - - damage: 1d8+7
        - damage: 2d6
          type: sonic
      attack: bite
      bonus:
      - 16
    - text: 2 hooves +16 (1d8+7 plus 2d6 sonic)
      entries:
      - - damage: 1d8+7
        - damage: 2d6
          type: sonic
      count: 2
      attack: hooves
      bonus:
      - 16
  special:
  - breath weapon (90-ft. cone, 6d6 sonic plus wind blast, Reflex DC 24 for half,
    usable every 1d4 rounds)
  - pounce
  - powerful hooves
  - thundering blows
  - trample (1d8+10 plus 2d6 sonic, DC 25)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - superscripts:
    - APG
    name: cloak of winds
    source: default
    freq: Constant
    DC: 18
  - name: fog cloud
    source: default
    freq: At will
  - name: gust of wind
    source: default
    freq: At will
    DC: 17
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: whispering wind
    source: default
    freq: At will
  - name: control weather
    source: default
    freq: 3/day
  - name: plant growth
    source: default
    freq: 3/day
  - name: sleet storm
    source: default
    freq: 3/day
  - name: chain lightning
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 16
    concentration: 21
ability_scores:
  STR: 25
  DEX: 28
  CON: 23
  INT: 14
  WIS: 20
  CHA: 21
BAB: 8
CMB: 16
CMD: 36
CMD_other: 40 vs. trip
feats:
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Mobility
- name: Run
- name: Toughness
- name: Weapon Finesse
- name: Wind Stance
skills:
  Acrobatics: 28
  Fly: 34
  Knowledge (geography): 21
  Knowledge (nature): 21
  Perception: 24
  Sense Motive: 24
  Stealth: 24
  Survival: 21
languages:
- Auran
- Common
- Sylvan
special_qualities:
- change shape (Large humanoid; alter self)
- wind resistance
ecology:
  environment: any
  organization: solitary, pair, or herd (3-8)
  treasure_type: standard
special_abilities:
  Breath Weapon (Su): A zephyr's breath weapon is a thunderous blast of wind. Creatures
    in the area of the breath weapon take 6d6 points of electricity damage and are
    affected as by a windstorm (Pathfinder RPG Core Rulebook 439). Creatures that
    successfully save against this effect take half damage and avoid the effects of
    the wind. The save DC is Charisma-based.
  Change Shape (Su): A zephyr can shift between its equine shape and that of a unique
    Large, winged humanoid as a standard action. When a zephyr is in humanoid form,
    its land speed becomes 40 feet, and its fly speed remains unchanged. Its hoof
    and bite attacks are replaced with two slam attacks that deal 1d8+7 points of
    damage plus 2d6 points of sonic damage, and its reach increases to 10 feet. It
    can use all of its other abilities in this form. A zephyr doesn't revert to any
    particular form when killed (both shapes are considered its true form). A true
    seeing spell reveals both forms simultaneously.
  Powerful Hooves (Ex): A zephyr's hooves are primary attacks.
  Thundering Blows (Su): A zephyr's natural weapons (including its trample attack),
    as well as any bludgeoning weapons it wields, deal an additional 2d6 points of
    electricity damage.
  Wind Resistance (Ex): A zephyr is treated as if it were two size categories larger
    for the purposes of determining the effects high winds have upon it.
  Wind Senses (Su): A zephyr's vision is not obstructed by fog, mist, weather conditions,
    or wind-blown particles. This includes magical effects as well as natural effects.
desc_long: |-
  Zephyrs are nature spirits tied to the weather. Some more social zephyrs enjoy cavorting with athletic mortals, but their wanderlust means that their good graces last at most a matter of months before they vanish for at least as long, seeking new horizons and racing storms. Zephyrs are seen by some as minor divinities of weather or as servants of Gozreh or the Eldest.

  When attacked or provoked into aggression by a perceived offense, a zephyr uses its breath weapon to scatter foes and then takes advantage of its mobility to trample or pounce on whichever enemy seems most isolated or physically imposing. A zephyr uses its spelllike abilities to prevent foes from regrouping. True to its proud fey nature, a zephyr rarely admits defeat without planning to turn the weather against an adversary at a later time as part of a vengeful ambush.

  A zephyr in its equine form is the size of a large horse and weighs over 1,000 pounds. A zephyr in its humanoid form usually stands just over 8 feet tall and weighs around 400 pounds, possessing an athletic build with feathered wings spanning 15 feet.

---

# Zephyr
This blue-furred _[[monsters/Horse|horse]]_ with a cloudlike mane and tail has _[[monsters/Gray|gray]]_, humanlike eyes that show obvious intelligence.
**Source** Pathfinder #101: The Kintargo Contract pg. 90
**XP** 19,200

CN Large fey (air, shapechanger)
**Init** +9; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, wind senses; Perception +24

##### Defense

**AC** 27, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+9 Dex, +1 dodge, +8 natural, –1 size)
**hp** 168 (16d6+112)
**Fort** +11, **Ref** +19, **Will** +15
**DR** 10/cold iron; **Immune** electricity; **Resist** cold 10, sonic 10

##### Offense
**Speed** 60 ft., fly 200 ft. (perfect)
**Melee** bite +16 (1d8+7 plus 2d6 sonic), 2 hooves +16 (1d8+7 plus 2d6 sonic)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (90-ft. cone, 6d6 sonic plus wind blast, Reflex DC 24 for half, usable every 1d4 rounds), _[[universal monster rules/Pounce|pounce]]_, powerful hooves, _[[items/Weapon Magic Abilities/Thundering|thundering]]_ blows, _[[universal monster rules/Trample|trample]]_ (1d8+10 plus 2d6 sonic, DC 25)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +21)
Constant—_[[spells/Cloak of Winds|cloak of winds]]_ (DC 18)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 17), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Control Weather|control weather]]_, _[[spells/Plant Growth|plant growth]]_, _[[spells/Sleet Storm|sleet storm]]_
1/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 21)

##### Statistics
**Str** 25, **Dex** 28, **Con** 23, **Int** 14, **Wis** 20, **Cha** 21
**Base Atk** +8; **CMB** +16; **CMD** 36 (40 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Mobility|Mobility]]_, Run, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +28, Fly +34, Knowledge (geography) +21, Knowledge (nature) +21, Perception +24, Sense Motive +24, Stealth +24, Survival +21
**Languages** Auran, Common, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Large humanoid; _[[spells/Alter Self|alter self]]_), wind _[[universal monster rules/Resistance|resistance]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or herd (3–8)
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Su)** A _[[monsters/Zephyr|zephyr]]_’s _breath weapon_ is a thunderous blast of wind. Creatures in the area of the _breath weapon_ take 6d6 points of electricity damage and are affected as by a windstorm (Pathfinder RPG Core Rulebook 439). Creatures that successfully save against this effect take half damage and avoid the effects of the wind. The save DC is Charisma-based.

**_Change Shape_ (Su)** A _zephyr_ can shift between its equine shape and that of a unique Large, winged humanoid as a standard action. When a _zephyr_ is in humanoid form, its land speed becomes 40 feet, and its fly speed remains unchanged. Its hoof and bite attacks are replaced with two slam attacks that deal 1d8+7 points of damage plus 2d6 points of sonic damage, and its reach increases to 10 feet. It can use all of its other abilities in this form. A _zephyr_ doesn’t revert to any particular form when killed (both shapes are considered its _[[spells/True Form|true form]]_). A _[[spells/True Seeing|true seeing]]_ spell reveals both forms simultaneously.

**Powerful Hooves (Ex)** A _zephyr_’s hooves are primary attacks.

**_Thundering_ Blows (Su)** A _zephyr_’s natural weapons (including its _trample_ attack), as well as any bludgeoning weapons it wields, deal an additional 2d6 points of electricity damage.

**Wind _Resistance_ (Ex)** A _zephyr_ is treated as if it were two size categories larger for the purposes of determining the effects high winds have upon it.

**Wind Senses (Su)** A _zephyr_’s _[[spells/Vision|vision]]_ is not obstructed by fog, mist, weather conditions, or wind-blown particles. This includes magical effects as well as natural effects.

##### Description

Zephyrs are nature spirits tied to the weather. Some more social zephyrs enjoy cavorting with _[[feats/Athletic|athletic]]_ mortals, but their wanderlust means that their good graces last at most a matter of months before they _[[spells/Vanish|vanish]]_ for at least as long, seeking new horizons and racing storms. Zephyrs are seen by some as minor divinities of weather or as servants of Gozreh or the Eldest.

When attacked or provoked into aggression by a perceived offense, a _zephyr_ uses its _breath weapon_ to scatter foes and then takes advantage of its _mobility_ to _trample_ or _pounce_ on whichever enemy seems most isolated or physically imposing. A _zephyr_ uses its spelllike abilities to prevent foes from regrouping. True to its proud fey nature, a _zephyr_ rarely admits defeat without planning to turn the weather against an adversary at a later time as part of a vengeful ambush.

A _zephyr_ in its equine form is the size of a large _horse_ and weighs over 1,000 pounds. A _zephyr_ in its humanoid form usually stands just over 8 feet tall and weighs around 400 pounds, possessing an _athletic_ build with feathered wings spanning 15 feet.