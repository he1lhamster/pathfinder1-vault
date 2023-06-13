---
cssclass: [monsters]
title1: Daemon, Olethrodaemon
desc_short: 'Crowned with a wicked array of twisted horns, this wide-mouthed, spherical
  behemoth stands on four stout legs. '
title2: Olethrodaemon
CR: 20
sources:
- name: Bestiary 2
  page: 70
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: NE
size: Gargantuan
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 12
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
AC:
  AC: 38
  touch: 18
  flat_footed: 30
  components:
    deflection: 4
    dex: 8
    natural: 20
    size: -4
HP:
  HP: 370
  long: 20d10+260
saves:
  fort: 29
  ref: 18
  will: 26
DR:
- amount: 10
  weakness: good and silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 31
speeds:
  base: 40
  burrow: 50
attacks:
  melee:
  - - text: 2 bites +28 (2d8+12/19-20 plus grab)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: bites
      bonus:
      - 28
    - text: 4 claws +28 (2d6+12 plus grab)
      entries:
      - - damage: 2d6+12
        - effect: grab
      count: 4
      attack: claws
      bonus:
      - 28
    - text: gore +28 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: gore
      bonus:
      - 28
  special:
  - drain soul
  - soul-drained breath
  - trample (2d8+18, DC 32)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 25
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. objects only
  - name: telekinesis
    source: default
    freq: At will
  - name: wall of fire
    source: default
    freq: At will
  - name: wall of ice
    source: default
    freq: At will
  - name: quickened disintegrate
    source: default
    freq: 3/day
    DC: 23
  - name: wall of force
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 1 CR 19
      chance: 100%
    - name: lower daemon
      chance: 100%
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 35
  DEX: 26
  CON: 37
  INT: 12
  WIS: 26
  CHA: 25
BAB: 20
CMB: 36
CMB_other: +40 grapple
CMD: 54
CMD_other: 58 vs. trip
feats:
- name: Awesome Blow
- name: Cleave
- name: Great Cleave
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (disintegrate)
skills:
  Climb: 35
  Intimidate: 30
  Knowledge (planes): 24
  Perception: 31
  Sense Motive: 31
  Stealth: 19
  Survival: 31
languages:
- Abyssal
- Infernal
- telepathy 100 ft.
special_qualities:
- adamantine claws
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or apocalypse (3-5)
  treasure_type: standard
special_abilities:
  Adamantine Claws (Ex): Able to tear through stone, an olethrodaemon's claws are
    treated as though they were adamantine. This ability also allows an olethrodaemon
    to make use of its burrow speed through stone.
  Drain Soul (Su): A creature grappled by an olethrodaemon's grab attack from its
    claws can be transferred to its mouth as a move action requiring no combat maneuver
    check. As a standard action, an olethrodaemon that begins its turn with an opponent
    grappled in either of its mouths can swallow the opponent by succeeding on another
    grapple check. If successful, the creature is swallowed into one of the olethrodaemon's
    many stomachs. These stomachs grind their contents and drain the life force from
    living creatures. Every round a creature remains in an olethrodaemon's stomach,
    it takes 4d8+18 points of damage and gains 1d4 negative levels. The creature can
    attempt to cut its way out of the olethrodaemon's stomach, but it suffers the
    chance of just cutting into another stomach chamber. An olethrodaemon's stomach
    is AC 20 and has 40 hit points. Once a creature deals enough damage to allow escape,
    it has a 50% chance to end up in another stomach chamber instead of escaping.
    Due to the multiple stomach chambers, an olethrodaemon can house and drain up
    to four medium creatures at one time. This ability otherwise functions as the
    swallow whole special attack. It is a DC 33 Fortitude save to remove negative
    levels gained in this fashion. This save is Constitution-based.
  Soul-Drained Breath (Su): An olethrodaemon can convert life energy it has consumed
    into a potent breath weapon. Up to three times per day, but no more often than
    once every 1d4 rounds, an olethrodaemon can expel a 120-foot line or a 60-foot
    cone of shrieking black smoke and wind from one of its mouths as a standard action.
    Any living creature in the area of this attack takes 20d10 points of damage from
    negative energy, or half on a successful DC 27 Reflex save. Undead creatures caught
    in this negative energy are healed for the same amount instead of damaged. The
    save DC for this effect is Charisma-based.
desc_long: |-
  While some of the more powerful daemons are servitors to one of the Four Horsemen, olethrodaemons serve as juggernauts for all of the Four. These massive creatures are the embodiment of death and destruction-the very vessels of apocalypse that daemons wish to see wrought upon the multiverse. These nihilistic behemoths roam the gray expanses of Abaddon, feasting on the souls of evil mortals damned to their realm. When on the Material Plane, olethrodaemons act as agents of destruction, spreading ruin and devouring mortal souls as they plow through cities and countrysides, bent on devastation. It's rare for a mortal to be able to control such a potent force, but sometimes mad spellcasters utilize effects like gate to urge an olethrodaemon to visit a devastating holocaust upon an enemy region-the olethrodaemon generally does not hold a grudge against a mortal that asks such a service from it.

  These immense creatures stand over 25 feet tall and weigh close to 12,000 pounds, their powerful, muscular bodies covered by durable plates and head thronged with dangerous, twisted horns. Olethrodaemons stand on four stout legs, and possess an equal number of arms, each ending in wickedly sharp claws able to tear through stone as easily as flesh. The creature's eyes, as well as its two mouths, glow like coals in a kiln. The creature feeds on souls and has multiple stomachs to digest mortal essences.

  While not as intelligent or scheming as many other powerful daemons (or other fiends who match their power, for that matter), olethrodaemons remain dangerous foes. They do not generally wish to lead armies and gain power by control, but rather to revel in the evil purity of annihilation. Among olethrodaemons, the greatest desire is to be the one to devour the very last mortal soul. They angle and shove for this honor, often ceding a city or group of victims to a rival if they believe that, in so doing, they might gain the advantage of positioning to consume the final soul once the multiverse has been devoured.

---

# Daemon, Olethrodaemon
Crowned with a wicked array of twisted horns, this wide-mouthed, spherical behemoth stands on four stout legs.

**Source** Bestiary 2 pg. 70
**XP** 307,200

NE Gargantuan outsider (daemon, evil, extraplanar)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +31
**Aura** _[[spells/Unholy Aura|unholy aura]]_

##### Defense

**AC** 38, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+4 deflection, +8 Dex, +20 natural, –4 size)
**hp** 370 (20d10+260)
**Fort** +29, **Ref** +18, **Will** +26
**DR** 10/good and silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 31

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 50 ft.
**Melee** 2 bites +28 (2d8+12/19–20 plus _[[universal monster rules/Grab|grab]]_), 4 claws +28 (2d6+12 plus _grab_), gore +28 (2d8+12)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** drain soul, soul-drained breath, _[[universal monster rules/Trample|trample]]_ (2d8+18, DC 32)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Air Walk|air walk]]_, _true seeing_, _unholy aura_ (DC 25) 
At will—greater teleport (self plus 50 lbs. objects only), _[[spells/Telekinesis|telekinesis]]_, _[[spells/Wall Of Fire|wall of fire]]_, _[[spells/Wall Of Ice|wall of ice]]_ 
3/day—quickened _[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Wall Of Force|wall of force]]_ 
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 9, any 1 CR 19 or lower daemon, 100%), _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 26)

##### Statistics
**Str** 35, **Dex** 26, **Con** 37, **Int** 12, **Wis** 26, **Cha** 25
**Base Atk** +20; **CMB** +36 (+40 grapple); **CMD** 54 (58 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_disintegrate_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +35, Intimidate +30, Knowledge (planes) +24, Perception +31, Sense Motive +31, Stealth +19, Survival +31
**Languages** Abyssal, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** adamantine claws

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or apocalypse (3–5)
**Treasure** standard

### Special Abilities

**Adamantine Claws (Ex)** Able to tear through stone, an olethrodaemon’s claws are treated as though they were adamantine. This ability also allows an olethrodaemon to make use of its _burrow_ speed through stone.

**Drain Soul (Su)** A creature _[[conditions/Grappled|grappled]]_ by an olethrodaemon’s _grab_ attack from its claws can be transferred to its mouth as a move action requiring no combat maneuver check. As a standard action, an olethrodaemon that begins its turn with an opponent _grappled_ in either of its mouths can swallow the opponent by succeeding on another grapple check. If successful, the creature is swallowed into one of the olethrodaemon’s many stomachs. These stomachs grind their contents and drain the life force from living creatures. Every round a creature remains in an olethrodaemon’s stomach, it takes 4d8+18 points of damage and gains 1d4 negative levels. The creature can attempt to cut its way out of the olethrodaemon’s stomach, but it suffers the chance of just cutting into another stomach chamber. An olethrodaemon’s stomach is AC 20 and has 40 hit points. Once a creature deals enough damage to allow escape, it has a 50% chance to end up in another stomach chamber instead of escaping. Due to the multiple stomach chambers, an olethrodaemon can house and drain up to four _[[classes/Medium|medium]]_ creatures at one time. This ability otherwise functions as the _[[universal monster rules/Swallow Whole|swallow whole]]_ special attack. It is a DC 33 Fortitude save to remove negative levels gained in this fashion. This save is Constitution-based.
**Soul-Drained Breath (Su) **An olethrodaemon can convert life energy it has consumed into a _[[items/Weapon Magic Abilities/Potent|potent]]_ _[[universal monster rules/Breath Weapon|breath weapon]]_. Up to three times per day, but no more often than once every 1d4 rounds, an olethrodaemon can expel a 120-foot line or a 60-foot cone of shrieking black smoke and wind from one of its mouths as a standard action. Any living creature in the area of this attack takes 20d10 points of damage from negative energy, or half on a successful DC 27 Reflex save. Undead creatures caught in this negative energy are healed for the same amount instead of damaged. The save DC for this effect is Charisma-based.

##### Description

While some of the more powerful daemons are servitors to one of the Four Horsemen, olethrodaemons serve as juggernauts for all of the Four. These massive creatures are the embodiment of death and _[[spells/Destruction|destruction]]_—the very vessels of apocalypse that daemons _[[spells/Wish|wish]]_ to see wrought upon the multiverse. These nihilistic behemoths roam the _[[monsters/Gray|gray]]_ expanses of Abaddon, feasting on the souls of evil mortals _[[feats/Damned|damned]]_ to their realm. When on the Material Plane, olethrodaemons act as agents of _destruction_, spreading ruin and devouring mortal souls as they plow through cities and countrysides, bent on devastation. It’s rare for a mortal to be able to control such a _potent_ force, but sometimes mad spellcasters utilize effects like _[[spells/Gate|gate]]_ to urge an olethrodaemon to visit a devastating holocaust upon an enemy region—the olethrodaemon generally does not hold a grudge against a mortal that asks such a service from it.

These immense creatures stand over 25 feet tall and weigh close to 12,000 pounds, their powerful, muscular bodies covered by durable plates and head thronged with dangerous, twisted horns. Olethrodaemons stand on four stout legs, and possess an equal number of arms, each ending in wickedly sharp claws able to tear through stone as easily as flesh. The creature’s eyes, as well as its two mouths, glow like coals in a kiln. The creature feeds on souls and has multiple stomachs to digest mortal essences.

While not as intelligent or scheming as many other powerful daemons (or other fiends who match their power, for that matter), olethrodaemons remain dangerous foes. They do not generally _wish_ to lead armies and gain power by control, but rather to revel in the evil purity of annihilation. Among olethrodaemons, the greatest desire is to be the one to devour the very last mortal soul. They angle and shove for this honor, often ceding a city or group of victims to a _[[feats/Rival|rival]]_ if they believe that, in so doing, they might gain the advantage of positioning to consume the final soul once the multiverse has been devoured.