---
cssclass: [monsters]
title1: Jabberwock
desc_short: This dragon has a long neck and terrible claws. The beast shrieks and
  babbles, thrashing its tail and wings in a violent manner.
title2: Jabberwock
CR: 23
sources:
- name: Bestiary 2
  page: 168
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 819200
alignment: CE
size: Huge
type: dragon
subtypes:
- air
- fire
initiative:
  bonus: 5
senses:
  blindsight: 120
  darkvision: 120
  low-light vision: true
  scent: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 31
AC:
  AC: 40
  touch: 14
  flat_footed: 34
  components:
    dex: 5
    dodge: 1
    natural: 26
    size: -2
HP:
  HP: 455
  long: 26d12+286
  fast_healing: 15
saves:
  fort: 26
  ref: 20
  will: 24
DR:
- amount: 15
  weakness: vorpal
immunities:
- fire
- paralysis
- sleep
resistances:
  acid: 30
  electricity: 30
  sonic: 30
SR: 31
weaknesses:
- fear of vorpal weapons
- vulnerable to cold
speeds:
  base: 40
  fly: 80
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +37 (4d8+19/19-20/×3)
      entries:
      - - damage: 4d8+19
          crit_range: 19-20
          crit_multiplier: 3
      attack: bite
      bonus:
      - 37
    - text: 2 claws +37 (3d6+13/19-20 plus grab)
      entries:
      - - damage: 3d6+13
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 37
    - text: tail slap +32 (2d8+19)
      entries:
      - - damage: 2d8+19
      attack: tail slap
      bonus:
      - 32
    - text: 2 wings +32 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: wings
      bonus:
      - 32
  ranged:
  - - text: 2 eye rays +29 touch (15d6 fire/19-20 plus burn)
      entries:
      - - damage: 15d6
          type: fire
          crit_range: 19-20
        - effect: burn
      count: 2
      attack: eye rays
      bonus:
      - 29
      touch: true
  special:
  - burble
  - burn (6d6, DC 34)
  - eye rays
  - whiffling
space: 15
reach: 15
ability_scores:
  STR: 37
  DEX: 20
  CON: 33
  INT: 12
  WIS: 29
  CHA: 26
BAB: 26
CMB: 41
CMB_other: +45 grapple
CMD: 57
feats:
- name: Awesome Blow
- name: Bleeding Critical
- name: Critical Focus
- name: Dodge
- name: Flyby Attack
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Critical (eye rays)
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Vital Strike
skills:
  Acrobatics: 31
    jump: 35
  Escape Artist: 31
  Fly: 26
  Intimidate: 37
  Knowledge (nature): 30
  Perception: 38
  Sense Motive: 38
languages:
- Aklo
- Common
- Draconic
- Gnome
- Sylvan
special_qualities:
- planar acclimation
ecology:
  environment: any forests
  organization: solitary
  treasure_type: triple
special_abilities:
  Burble (Su): A jabberwock can burble once every 1d4 rounds as a standard action.
    This blast of strange noises and shouted nonsense in the various languages known
    to the jabberwock (and invariably some languages it doesn't know) affects all
    creatures within a 60-foot-radius spread-these creatures must make a DC 31 Will
    save or become confused for 1d4 rounds. Alternatively, the jabberwock can focus
    its burble attack to create a 60-foot line of sonic energy that deals 20d6 points
    of sonic damage (DC 31 Reflex save for half). The confusion effect is mind-affecting;
    both are sonic effects. The save DC is Charisma-based.
  Damage Reduction (Ex): A jabberwock's damage reduction can be bypassed only by weapons
    that possess the vorpal weapon enhancement.
  Eye Rays (Su): The jabberwock can project beams of fire from its eyes as a ranged
    touch attack as a standard action, with a range increment of 60 feet. It projects
    two beams, and can target different creatures with these beams if it wishes as
    long as both targets are within 30 feet of each other. A creature that takes damage
    from an eye beam suffers burn.
  Fear of Vorpal Weapons (Ex): A jabberwock knows that a vorpal weapon can kill it
    swiftly. As soon as it takes damage from a vorpal weapon, a jabberwock becomes
    shaken for 1 round. If it is hit by a critical threat from a vorpal weapon, whether
    or not the critical hit is confirmed, the jabberwock is staggered for 1 round.
  Planar Acclimation (Ex): A jabberwock is always considered to be on its home plane,
    regardless of what plane it finds itself upon. It never gains the extraplanar
    subtype.
  Whiffling (Ex): A jabberwock's wings and violent motions create a significant amount
    of wind whenever it makes a full attack action. These winds surround the monster
    to a radius of 30 feet, and are treated as severe winds-ranged attacks take a
    -4 penalty when targeting a jabberwock while it is whiffling, and Medium creatures
    must make a DC 10 Strength check to approach the creature. Small or smaller creatures
    in this area that fail a DC 15 Strength check are blown away. See page the wind
    effects table for further details on the effects of severe winds.
desc_long: |-
  The jabberwock is a true creature of legend-a subject of poetry, song, and myth in many cultures. It is known to be a devastating creature in combat whose arrival presages times of ruin and violence; these stories also tell of the creature's fear of the tools some say were created in ancient times for the sole purpose of defeating them-vorpal weapons. A jabberwock is 35 feet tall and weighs 8,000 pounds.

  The jabberwock is not a creature of the Material Plane, but one from the primal world of the fey. It comes from a region of reality where life is more robust, where emotions are more potent, and where dreams and nightmares can come alive. Even in such incredible realms, though, the jabberwock is a creature to be feared. It belongs to a category of powerful creatures whose shapes and types run the gamut of possibility-a group known collectively as the “Tane.” Of the Tane, the jabberwock is said to be the most powerful, but the others in this grouping are far from helpless. Said to have been created as goliaths of war and madness, dreamt and stitched into being by the strange gods of this primeval reality, the Tane are as mysterious as they are powerful. Two other creatures of the Tane are presented in this book-the sard and the thrasfyr. None of the Tane are lower than CR 16 in power and all possess the planar acclimation special quality, but beyond that, they generally share no specific abilities or characteristics save for their common source in the primal world.

  When a jabberwock comes to the Material Plane, it does so to spread destruction and ruin. Typically, the monster seeks out a remote forest lair at least a day's flight from civilization, then emerges from this den once a week to seek out a new place to destroy. It has no true interest in amassing treasure, but often gathers objects of obvious value to bring back to its den in order to encourage heroes to seek it out-to a jabberwock, it makes no difference whether it seeks out things to destroy or lets those things come to it.

  Jabberwocks age, eat, drink, and sleep like any living creature, but they do not reproduce in the classic sense of the word. The creation of a new jabberwock-or of any of the Tane, in fact-is regulated by the strange and unknowable godlike entities that dwell in the primeval world. These fey lords create new jabberwocks as they are needed-sometimes varying the exact particulars (see Variant Jabberwocks, below), but always creating a fully formed adult creature. No young jabberwock has ever been encountered as a result.

  The strange vulnerability a jabberwock possesses against vorpal weapons has long been a matter of intrigue and speculation among scholars. Most believe that, once upon a time, only one jabberwock existed, a creature of such great power that nothing could hurt it. Nothing, that is, save for a legendary sword forged for a mortal hero by a now-forgotten artisan or god. So epic was this battle that it created strange echoes throughout reality, and as a result, these echoes, in the form of the vorpal swords and jabberwocks known today, can be found on many worlds.

---

# Jabberwock
This dragon has a long neck and terrible claws. The beast shrieks and babbles, thrashing its tail and wings in a violent manner.
**Source** Bestiary 2 pg. 168
**XP** 819,200
CE Huge dragon (air, fire)
**Init** +5; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +38
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 31)

##### Defense

**AC** 40, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+5 Dex, +1 dodge, +26 natural, –2 size)
**hp** 455 (26d12+286); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +26, **Ref** +20, **Will** +24
**DR** 15/vorpal; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **Resist** acid 30, electricity 30, sonic 30; **SR** 31
**Weaknesses** _[[universal monster rules/Fear|fear]]_ of _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ weapons, vulnerable to cold

##### Offense
**Speed** 40 ft., fly 80 ft. (poor)
**Melee** bite +37 (4d8+19/19–20/×3), 2 claws +37 (3d6+13/19–20 plus _[[universal monster rules/Grab|grab]]_), tail slap +32 (2d8+19), 2 wings +32 (1d8+6)
**Ranged** 2 eye rays +29 touch (15d6 fire/19–20 plus _[[universal monster rules/Burn|burn]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** burble, _burn_ (6d6, DC 34), eye rays, whiffling

##### Statistics
**Str** 37, **Dex** 20, **Con** 33, **Int** 12, **Wis** 29, **Cha** 26
**Base Atk** +26; **CMB** +41 (+45 grapple); **CMD** 57
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claws, eye rays), _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +31 (+35 _[[spells/Jump|jump]]_), Escape Artist +31, Fly +26, Intimidate +37, Knowledge (nature) +30, Perception +38, Sense Motive +38
**Languages** Aklo, Common, Draconic, Gnome, Sylvan
**SQ** _[[items/Weapon Magic Abilities/Planar|planar]]_ acclimation

##### Ecology

**Environment** any forests
**Organization** solitary
**Treasure** triple

### Special Abilities

**Burble (Su)** A _[[monsters/Jabberwock|jabberwock]]_ can burble once every 1d4 rounds as a standard action. This blast of strange noises and shouted nonsense in the various languages known to the _jabberwock_ (and invariably some languages it doesn’t know) affects all creatures within a 60-foot-radius spread—these creatures must make a DC 31 Will save or become _[[conditions/Confused|confused]]_ for 1d4 rounds. Alternatively, the _jabberwock_ can focus its burble attack to create a 60-foot line of sonic energy that deals 20d6 points of sonic damage (DC 31 Reflex save for half). The _[[spells/Confusion|confusion]]_ effect is mind-affecting; both are sonic effects. The save DC is Charisma-based.

**_[[universal monster rules/Damage Reduction|Damage Reduction]]_ (Ex)** A _jabberwock_’s _damage reduction_ can be bypassed only by weapons that possess the _vorpal_ weapon enhancement.

**Eye Rays (Su)** The _jabberwock_ can project beams of fire from its eyes as a ranged touch attack as a standard action, with a range increment of 60 feet. It projects two beams, and can target different creatures with these beams if it wishes as long as both targets are within 30 feet of each other. A creature that takes damage from an eye beam suffers _burn_.

**_Fear_ of _Vorpal_ Weapons (Ex)** A _jabberwock_ knows that a _vorpal_ weapon can kill it swiftly. As soon as it takes damage from a _vorpal_ weapon, a _jabberwock_ becomes _[[conditions/Shaken|shaken]]_ for 1 round. If it is hit by a critical threat from a _vorpal_ weapon, whether or not the critical hit is confirmed, the _jabberwock_ is _[[conditions/Staggered|staggered]]_ for 1 round.

**_Planar_ Acclimation (Ex) **A _jabberwock_ is always considered to be on its home plane, regardless of what plane it finds itself upon. It never gains the extraplanar subtype.

**Whiffling (Ex)** A _jabberwock_’s wings and violent motions create a significant amount of wind whenever it makes a full attack action. These winds surround the monster to a radius of 30 feet, and are treated as severe winds—ranged attacks take a –4 penalty when targeting a _jabberwock_ while it is whiffling, and _[[classes/Medium|Medium]]_ creatures must make a DC 10 Strength check to approach the creature. Small or smaller creatures in this area that fail a DC 15 Strength check are blown away. See page the wind effects table for further details on the effects of severe winds.

##### Description

The _jabberwock_ is a true creature of legend—a subject of poetry, song, and myth in many cultures. It is known to be a devastating creature in combat whose arrival presages times of ruin and violence; these stories also tell of the creature’s _fear_ of the tools some say were created in ancient times for the sole purpose of defeating them—_vorpal_ weapons. A _jabberwock_ is 35 feet tall and weighs 8,000 pounds.

The _jabberwock_ is not a creature of the Material Plane, but one from the primal world of the fey. It comes from a region of reality where life is more robust, where emotions are more _[[items/Weapon Magic Abilities/Potent|potent]]_, and where dreams and nightmares can come alive. Even in such incredible realms, though, the _jabberwock_ is a creature to be feared. It belongs to a category of powerful creatures whose shapes and types run the gamut of possibility—a group known collectively as the “Tane.” Of the Tane, the _jabberwock_ is said to be the most powerful, but the others in this grouping are far from _[[conditions/Helpless|helpless]]_. Said to have been created as goliaths of war and madness, dreamt and stitched into being by the strange gods of this primeval reality, the Tane are as mysterious as they are powerful. Two other creatures of the Tane are presented in this book—the _[[monsters/Sard|sard]]_ and the _[[monsters/Thrasfyr|thrasfyr]]_. None of the Tane are lower than CR 16 in power and all possess the _planar_ acclimation special quality, but beyond that, they generally share no specific abilities or characteristics save for their common source in the primal world.

When a _jabberwock_ comes to the Material Plane, it does so to spread _[[spells/Destruction|destruction]]_ and ruin. Typically, the monster seeks out a remote forest lair at least a day’s _[[universal monster rules/Flight|flight]]_ from civilization, then emerges from this den once a week to seek out a new place to destroy. It has no true interest in amassing treasure, but often gathers objects of obvious value to bring back to its den in order to encourage heroes to seek it out—to a _jabberwock_, it makes no difference whether it seeks out things to destroy or lets those things come to it.

Jabberwocks age, eat, drink, and sleep like any living creature, but they do not reproduce in the classic sense of the word. The creation of a new _jabberwock_—or of any of the Tane, in fact—is regulated by the strange and unknowable godlike entities that dwell in the primeval world. These fey lords create new jabberwocks as they are needed—sometimes varying the exact particulars (see Variant Jabberwocks, below), but always creating a fully formed adult creature. No young _jabberwock_ has ever been encountered as a result.

The strange _[[curses/Vulnerability|vulnerability]]_ a _jabberwock_ possesses against _vorpal_ weapons has long been a matter of intrigue and speculation among scholars. Most believe that, once upon a time, only one _jabberwock_ existed, a creature of such great power that nothing could hurt it. Nothing, that is, save for a legendary sword forged for a mortal hero by a now-forgotten artisan or god. So epic was this battle that it created strange echoes throughout reality, and as a result, these echoes, in the form of the _vorpal_ swords and jabberwocks known today, can be found on many worlds.