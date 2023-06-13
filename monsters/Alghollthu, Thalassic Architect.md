---
cssclass: [monsters]
title1: Alghollthu, Thalassic Architect
desc_short: This piscine nightmare glares with five eyes. Four tentacles, two of them
  terminating in small claws, flank its fanged jaws.
title2: Thalassic Architect
CR: 10
sources:
- name: 'Pathfinder #121: The Lost Outpost'
  page: 88
  link: http://paizo.com/products/btpy9trj?Pathfinder-Adventure-Path-121-The-Lost-Outpost
XP: 9600
alignment: LE
size: Large
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 8
senses:
  darkvision: 60
  tremorsense: 60
AC:
  AC: 24
  touch: 13
  flat_footed: 20
  components:
    dex: 4
    natural: 11
    size: -1
HP:
  HP: 126
  long: 12d8+72
saves:
  fort: 10
  ref: 10
  will: 14
immunities:
- electricity
- mind-affecting effects
- sonic
resistances:
  cold: 10
SR: 21
speeds:
  base: 15
  swim: 60
attacks:
  melee:
  - - text: bite +13 (1d8+5 plus slime)
      entries:
      - - damage: 1d8+5
        - effect: slime
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+5 plus slime)
      entries:
      - - damage: 1d6+5
        - effect: slime
      count: 2
      attack: claws
      bonus:
      - 13
    - text: 2 tentacles +11 (1d6+2 plus 2d6 sonic)
      entries:
      - - damage: 1d6+2
        - damage: 2d6
          type: sonic
      count: 2
      attack: tentacles
      bonus:
      - 11
  special:
  - deadlight
  - glyph carver
  - mucus cloud
  - water manipulation (DC 20)
space: 10
reach: 10
reach_other: 15 ft. with claws and tentacles
spell_like_abilities:
  entries:
  - name: read magic
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 16
  - name: hydraulic torrent
    source: default
    freq: At will
  - name: project image
    source: default
    freq: At will
    DC: 21
  - name: telekinesis
    source: default
    freq: At will
  - name: illusory wall
    source: default
    freq: 3/day
    DC: 18
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 19
  - name: quickened hydraulic torrent
    source: default
    freq: 3/day
  - name: stone shape
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  - name: disintegrate
    source: default
    freq: 1/day
    DC: 20
  - name: fabricate
    source: default
    freq: 1/day
  - name: make whole
    source: default
    freq: 1/day
  - name: move earth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 18
ability_scores:
  STR: 20
  DEX: 18
  CON: 23
  INT: 17
  WIS: 18
  CHA: 19
BAB: 9
CMB: 15
CMB_other: +17 sunder
CMD: 29
CMD_other: 31 vs. sunder
feats:
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- is_bonus: true
  name: Quicken Spell-Like Ability (hydraulic torrent)
skills:
  Craft (stonemasonry): 13
  Knowledge (arcana): 16
  Knowledge (dungeoneering): 11
  Knowledge (engineering): 13
  Knowledge (history): 13
  Knowledge (nature): 13
  Stealth: 11
  Swim: 26
  Use Magic Device: 12
  Perception: 4
languages:
- Aboleth
- Aklo
- Aquan
- Undercommon
- telepathy 100 ft.
ecology:
  environment: any water
  organization: solitary, pair, or crew (1 thalassic architect plus 2-30 aboleths,
    skum, and other dominated creatures)
  treasure_type: double
special_abilities:
  Deadlight (Su): Once per round as a free action, the thalassic architect can affix
    its center eye on one target. The target must succeed at a DC 20 Will saving throw
    or become transfixed as per lock gaze  at caster level 14th. Once a creature has
    been affected by this ability, it becomes immune to it for 24 hours. The save
    DC is Charisma-based.
  Glyph Carver (Su): A thalassic architect can cause its tentacles to vibrate at an
    intense frequency when it rends through solid matter, such that the tips can engrave
    inhuman patterns into solid stone. When activated, the tentacles count as adamantine
    for the purpose of bypassing DR and hardness. Furthermore, the additional sonic
    damage caused by the tentacles is treated as energy damage when used as part of
    a melee attack (as per normal) but is treated as additional normal physical damage
    when used to perform a sunder combat maneuver. The thalassic architect can turn
    this ability on or off as a free action. While this ability is activated, the
    tentacles can't be used to manipulate physical objects, nor can the thalassic
    architect attempt Stealth checks. While this ability is deactivated, the tentacles
    cause no sonic damage.
  Mucus Cloud (Ex): While underwater, a thalassic architect exudes a cloud of transparent
    slime in a 100-foot-radius spread. All creatures in this area must succeed at
    a DC 22 Fortitude save each round or lose the ability to breathe air (and gain
    the ability to breathe water) for 8 hours. If a creature comes into contact with
    this mucus cloud again and fails another save, the effect extends for another
    8 hours. The save DC is Constitution-based.
  Slime (Ex): A creature hit by a thalassic architect's tentacle must succeed at a
    DC 22 Fortitude save or its skin and flesh transform into a clear, slimy membrane
    over the course of 1d4 rounds. The target's new “flesh” is soft and tender, reducing
    the creature's Constitution score by 4 as long as the effect persists. If the
    creature's flesh isn't kept moist, it dries out quickly and the victim takes 1d12
    points of damage every 10 minutes. Remove disease and similar effects can restore
    an afflicted creature to normal, but immunity to disease offers no protection
    from this attack. The save DC is Constitution-based.
  Water Manipulation (Su): |-
    A thalassic architect is adept at the telekinetic manipulation of matter, including the waters it inhabits. This at-will ability is a standard action with a duration of concentration + 1 round. The ability functions in two different modes that can be used only one at a time.

     The architect can force the water around a creature to lock in place and act as a solid, paralyzing the target as per hold monster unless the target succeeds at a DC 20 Reflex save. Aside from using effects such as freedom of movement or remove paralysis, the target can also break free with a DC 20 Strength check. This ability can affect a creature more than once, but each casting grants a new saving throw.

     Alternatively, it can thicken water to the consistency of gelatin in a 20-foot radius. Creatures with a swim speed treat this area as difficult terrain. Creatures without a swim speed increase the DC for Swim checks to move through the affected area by 10 (for example, calm underwater areas, usually DC 10, become DC 20). In either case, 5-foot steps become impossible. The save DC is Charisma-based.
desc_long: |-
  "Thalassic architect” is a human term for a racial subspecies of aboleth, known as uldraaghus in the language of alghollthus. Uldraaghus were engineered and bred by the mysterious entities that rule the alghollthu race from the deepest oceanic trenches. Whereas aboleths and veiled masters are adept at using telepathy and mental domination, thalassic architects use telekinetic powers to manipulate-even create or destroy-physical matter.

   Uldraaghus more closely resemble veiled masters than they do standard aboleths. They're smaller, being about 15 feet long and weighing 2,800 pounds. Furthermore, they have five eyes instead of three; four are set to either side of their head, while a larger fifth eye is set in the center and glows with a brilliant white light. Thalassic architects have four tentacles, two of which end in clawed appendages capable of manipulating objects. Dark bands of scales typically ring their silvery bodies. 

---

# Alghollthu, Thalassic Architect
This piscine _[[spells/Nightmare|nightmare]]_ glares with five eyes. Four tentacles, two of them terminating in small claws, flank its fanged jaws.
**Source** Pathfinder #121: The Lost Outpost pg. 88
**XP** 9,600

LE Large aberration (aquatic)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +4

##### Defense

**AC** 24, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 Dex, +11 natural, -1 size)
**hp** 126 (12d8+72)
**Fort** +10, **Ref** +10, **Will** +14
**Immune** electricity, mind-affecting effects, sonic; **Resist** cold 10; **SR** 21

##### Offense
**Speed** 15 ft., swim 60 ft.
**Melee** bite +13 (1d8+5 plus slime), 2 claws +13 (1d6+5 plus slime), 2 tentacles +11 (1d6+2 plus 2d6 sonic)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with claws and tentacles)
**Special Attacks** deadlight, glyph carver, mucus cloud, water manipulation (DC 20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +18)
Constant—_[[spells/Read Magic|read magic]]_ 
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Hydraulic Torrent|hydraulic torrent]]_, _[[spells/Project Image|project image]]_ (DC 21), _[[spells/Telekinesis|telekinesis]]_ 
3/day—_[[spells/Illusory Wall|illusory wall]]_ (DC 18), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 19), quickened _hydraulic torrent_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Wall Of Force|wall of force]]_ 
1/day—_[[spells/Disintegrate|disintegrate]]_ (DC 20), _[[spells/Fabricate|fabricate]]_, _[[spells/Make Whole|make whole]]_, _[[spells/Move Earth|move earth]]_

##### Statistics
**Str** 20, **Dex** 18, **Con** 23, **Int** 17, **Wis** 18, **Cha** 19
**Base Atk** +9; **CMB** +15 (+17 sunder); **CMD** 29 (31 vs. sunder)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_hydraulic torrent_)
**Skills** Craft (stonemasonry) +13, Knowledge (arcana) +16, Knowledge (dungeoneering) +11, Knowledge (engineering) +13, Knowledge (history) +13, Knowledge (nature) +13, Stealth +11, Swim +26, Use Magic Device +12
**Languages** Aboleth, Aklo, Aquan, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any water
**Organization** solitary, pair, or crew (1 thalassic architect plus 2–30 aboleths, _[[monsters/Skum|skum]]_, and other dominated creatures)
**Treasure** double

### Special Abilities

**Deadlight (Su)** Once per round as a free action, the thalassic architect can affix its center eye on one target. The target must succeed at a DC 20 Will saving throw or become transfixed as per _[[spells/Lock Gaze|lock gaze]]_ at caster level 14th. Once a creature has been affected by this ability, it becomes immune to it for 24 hours. The save DC is Charisma-based.

**Glyph Carver (Su)** A thalassic architect can cause its tentacles to vibrate at an intense frequency when it rends through solid matter, such that the tips can engrave inhuman patterns into solid stone. When activated, the tentacles count as adamantine for the purpose of bypassing DR and hardness. Furthermore, the additional sonic damage caused by the tentacles is treated as energy damage when used as part of a melee attack (as per normal) but is treated as additional normal physical damage when used to perform a sunder combat maneuver. The thalassic architect can turn this ability on or off as a free action. While this ability is activated, the tentacles can’t be used to manipulate physical objects, nor can the thalassic architect attempt Stealth checks. While this ability is deactivated, the tentacles cause no sonic damage.

**Mucus Cloud (Ex)** While _[[items/Weapon Magic Abilities/Underwater|underwater]]_, a thalassic architect exudes a cloud of transparent slime in a 100-foot-radius spread. All creatures in this area must succeed at a DC 22 Fortitude save each round or lose the ability to breathe air (and gain the ability to breathe water) for 8 hours. If a creature comes into contact with this mucus cloud again and fails another save, the effect extends for another 8 hours. The save DC is Constitution-based.
**Slime (Ex)** A creature hit by a thalassic architect’s tentacle must succeed at a DC 22 Fortitude save or its skin and flesh transform into a clear, slimy membrane over the course of 1d4 rounds. The target’s new “flesh” is soft and tender, reducing the creature’s Constitution score by 4 as long as the effect persists. If the creature’s flesh isn’t kept moist, it dries out quickly and the victim takes 1d12 points of damage every 10 minutes. _[[spells/Remove Disease|Remove disease]]_ and similar effects can restore an afflicted creature to normal, but _[[universal monster rules/Immunity|immunity]]_ to disease offers no protection from this attack. The save DC is Constitution-based.

**Water Manipulation (Su)** A thalassic architect is adept at the telekinetic manipulation of matter, including the waters it inhabits. This at-will ability is a standard action with a duration of concentration + 1 round. The ability functions in two different modes that can be used only one at a time.

The architect can force the water around a creature to lock in place and act as a solid, paralyzing the target as per _[[spells/Hold Monster|hold monster]]_ unless the target succeeds at a DC 20 Reflex save. Aside from using effects such as _[[spells/Freedom of Movement|freedom of movement]]_ or _[[spells/Remove Paralysis|remove paralysis]]_, the target can also break free with a DC 20 Strength check. This ability can affect a creature more than once, but each casting grants a new saving throw.

Alternatively, it can thicken water to the consistency of gelatin in a 20-foot radius. Creatures with a swim speed treat this area as difficult terrain. Creatures without a swim speed increase the DC for Swim checks to move through the affected area by 10 (for example, calm _underwater_ areas, usually DC 10, become DC 20). In either case, 5-foot steps become impossible. The save DC is Charisma-based.

##### Description

"Thalassic architect” is a human term for a racial subspecies of aboleth, known as uldraaghus in the language of alghollthus. Uldraaghus were engineered and bred by the mysterious entities that rule the alghollthu race from the deepest oceanic trenches. Whereas aboleths and veiled masters are adept at using _telepathy_ and mental domination, thalassic architects use telekinetic powers to manipulate—even create or destroy—physical matter.

Uldraaghus more closely resemble veiled masters than they do standard aboleths. They’re smaller, being about 15 feet long and weighing 2,800 pounds. Furthermore, they have five eyes instead of three; four are set to either side of their head, while a larger fifth eye is set in the center and glows with a brilliant white light. Thalassic architects have four tentacles, two of which end in clawed appendages capable of manipulating objects. Dark bands of scales typically ring their silvery bodies.