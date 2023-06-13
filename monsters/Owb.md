---
cssclass: [monsters]
title1: Owb
desc_short: This thing looks like a skeletal human torso coated in liquid shadow,
  obscuring its bones but clearly revealing its shape.
title2: Owb
CR: 6
sources:
- name: Bestiary 4
  page: 210
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 2400
alignment: NE
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 17
  touch: 17
  flat_footed: 10
  components:
    dex: 6
    dodge: 1
HP:
  HP: 76
  long: 8d10+32
  fast_healing: 2
saves:
  fort: 10
  ref: 8
  will: 8
immunities:
- cold
weaknesses:
- light sensitivity
speeds:
  base: 5
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +12 (1d8+4 plus 1d6 cold)
      entries:
      - - damage: 1d8+4
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 12
  ranged:
  - - text: burning cold +14 touch (3d6 cold)
      entries:
      - - damage: 3d6
          type: cold
      attack: burning cold
      bonus:
      - 14
      touch: true
  special:
  - burning cold
  - curse of darkness
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
  - superscripts:
    - APG
    name: dust of twillight
    source: default
    freq: At will
    DC: 15
  - superscripts:
    - UM
    name: shadow step
    source: default
    freq: 5/day
  - name: plane shift
    source: default
    freq: 1/day
    paren_text: self only, to or from the Shadow Plane only
  sources:
  - name: default
    CL: 8
    concentration: 11
ability_scores:
  STR: 18
  DEX: 22
  CON: 19
  INT: 11
  WIS: 15
  CHA: 16
BAB: 8
CMB: 12
CMD: 29
feats:
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Point-Blank Shot
skills:
  Bluff: 12
  Diplomacy: 11
  Fly: 18
  Knowledge (planes): 11
  Perception: 13
  Sense Motive: 13
  Spellcraft: 7
  Stealth: 17
languages:
- Dark Folk (can't speak)
- telepathy 100 ft.
ecology:
  environment: any land or underground (Plane of Shadow)
  organization: solitary or cabal (2-4)
  treasure_type: none
special_abilities:
  Burning Cold (Su): As a standard action, an owb can conjure a ball of flickering
    flames and hurl it at an opponent. The flames can be thrown as a ranged touch
    attack at a range of 120 feet with no range increment, and deal 3d6 points of
    cold damage.
  Curse of Darkness (Su): With a touch, an owb can make bright light unbearable to
    the victim. Any creature touched must succeed at a DC 17 Fortitude save or gain
    the light blindness weakness. This ability also robs the victim of its coloration,
    leaving the creature and its equipment in washed-out shades of gray. This effect
    can be removed with break enchantment or remove curse, unless the target has the
    dark folk subtype, in which case the effect can only be removed by wish or similar
    magic. The save DC is Charisma-based.
desc_long: |-
  An owb is a sinister visitor from the Shadow Plane, a creature resembling a humanoid torso draped in darkness. Alien in nature, this mysterious shade never speaks audible words, but it constantly uses its telepathy to project mumbles of curses and threats into the minds of those it encounters.

  The race's closest relationship is with the dark folk, who worship owbs as proxies to gods of the shadows. Most dark folk believe the first of their kind were created by owbs-or more powerful owb-like beings.

  An owb despises any light other than the dim flicker created by its burning cold ability, and shrinks from its presence. It often seeks to destroy those who bring light near it, relentlessly attacking the perpetrators until its enemies flee or die.

  An owb usually keeps its presence hidden from mortals. Lurking nearby, the shadowy creature listens in on nearby thoughts, always searching for a collection of fears and worries it can capitalize on for its own machinations. It may serve as an intermediary between doppelgangers on the surface world and dark folk in subterranean lands. An owb associated with a tribe of dark folk may scrutinize newborns and tune the children's connection to the Shadow Plane so they eventually grow into a different type of dark folk than the type they were born (allowing a dark creeper to become a dark stalker, and so on).

  An owb loves manipulation and runs conspiratorial plots involving denizens of the Shadow Plane and those of the Material Plane. An owb or cabal of owbs may control entire clans of dark folk, and use them as spies and pawns in some inscrutable plan.

  Though most of an owb's form measures only 3-1/2 feet tall, it typically floats so its head is level with that of a Medium humanoid. Deceptively light, an owb weighs only 20 pounds.

---

# Owb
This thing looks like a skeletal human torso coated in liquid _[[items/Armor Magic Abilities/Shadow|shadow]]_, obscuring its bones but clearly revealing its shape.
**Source** Bestiary 4 pg. 210
**XP** 2,400

NE Medium outsider (extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +13

##### Defense

**AC** 17, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 10 (+6 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 76 (8d10+32); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +10, **Ref** +8, **Will** +8
**Immune** cold
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 5 ft., fly 60 ft. (perfect)
**Melee** 2 claws +12 (1d8+4 plus 1d6 cold)
**Ranged** _[[items/Weapon Magic Abilities/Burning|burning]]_ cold +14 touch (3d6 cold)
**Special Attacks** _burning_ cold, curse of _[[spells/Darkness|darkness]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
Constant—_[[spells/Blur|blur]]_
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Detect Thoughts|detect thoughts]]_, dust of twillight (DC 15)
5/day—_[[spells/Shadow Step|shadow step]]_
1/day—_[[spells/Plane Shift|plane shift]]_ (self only, to or from the _Shadow_ Plane only)

##### Statistics
**Str** 18, **Dex** 22, **Con** 19, **Int** 11, **Wis** 15, **Cha** 16
**Base Atk** +8; **CMB** +12; **CMD** 29
**Feats** _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_
**Skills** Bluff +12, Diplomacy +11, Fly +18, Knowledge (planes) +11, Perception +13, Sense Motive +13, Spellcraft +7, Stealth +17
**Languages** Dark Folk (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any land or underground (Plane of _Shadow_)
**Organization** solitary or cabal (2–4)
**Treasure** none

### Special Abilities

**_Burning_ Cold (Su)** As a standard action, an _[[monsters/Owb|owb]]_ can conjure a ball of flickering flames and hurl it at an opponent. The flames can be thrown as a ranged touch attack at a range of 120 feet with no range increment, and deal 3d6 points of cold damage.

**Curse of _Darkness_ (Su)** With a touch, an _owb_ can make bright light unbearable to the victim. Any creature touched must succeed at a DC 17 Fortitude save or gain the _[[universal monster rules/Light Blindness|light blindness]]_ weakness. This ability also robs the victim of its coloration, leaving the creature and its equipment in washed-out _[[spells/Shades|shades]]_ of _[[monsters/Gray|gray]]_. This effect can be removed with _[[spells/Break Enchantment|break enchantment]]_ or _[[spells/Remove Curse|remove curse]]_, unless the target has the dark folk subtype, in which case the effect can only be removed by _[[spells/Wish|wish]]_ or similar magic. The save DC is Charisma-based.

##### Description

An _owb_ is a sinister visitor from the _Shadow_ Plane, a creature resembling a humanoid torso draped in _darkness_. Alien in nature, this mysterious shade never speaks audible words, but it constantly uses its _telepathy_ to project mumbles of curses and threats into the minds of those it encounters.

The race’s closest relationship is with the dark folk, who worship owbs as proxies to gods of the shadows. Most dark folk believe the first of their kind were created by owbs—or more powerful owb-like beings.

An _owb_ despises any light other than the dim flicker created by its _burning_ cold ability, and shrinks from its presence. It often seeks to destroy those who bring light near it, relentlessly attacking the perpetrators until its enemies flee or die.

An _owb_ usually keeps its presence hidden from mortals. Lurking nearby, the shadowy creature listens in on nearby thoughts, always searching for a collection of fears and worries it can capitalize on for its own machinations. It may serve as an intermediary between doppelgangers on the surface world and dark folk in subterranean lands. An _owb_ associated with a tribe of dark folk may scrutinize newborns and tune the children’s connection to the _Shadow_ Plane so they eventually grow into a different type of dark folk than the type they were born (allowing a dark creeper to become a dark stalker, and so on).

An _owb_ loves manipulation and runs conspiratorial plots involving denizens of the _Shadow_ Plane and those of the Material Plane. An _owb_ or cabal of owbs may control entire clans of dark folk, and use them as spies and pawns in some inscrutable plan.

Though most of an _owb_’s form measures only 3-1/2 feet tall, it typically floats so its head is level with that of a _Medium_ humanoid. Deceptively light, an _owb_ weighs only 20 pounds.