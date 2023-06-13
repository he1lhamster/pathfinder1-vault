---
cssclass: [monsters]
title1: Couatl
desc_short: This great serpent has multicolored wings and eyes that glimmer with intense
  awareness.
title2: Couatl
CR: 10
sources:
- name: Pathfinder RPG Bestiary
  page: 49
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 9600
alignment: LG
size: Large
type: outsider
subtypes:
- native
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect chaos/evil/good/law: true
AC:
  AC: 22
  touch: 13
  flat_footed: 18
  components:
    dex: 3
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 126
  long: 12d10+60
saves:
  fort: 9
  ref: 13
  will: 14
speeds:
  base: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +16 (1d8+7 plus grab and poison)
      entries:
      - - damage: 1d8+7
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 16
  special:
  - constrict (1d8+7)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: ethereal jaunt
    source: default
    freq: At will
    CL: 16
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 20
  sources:
  - name: default
    CL: 9
spells:
  entries:
  - name: charm monster
    source: '?'
    level: 4
    DC: 17
  - name: freedom of movement
    source: '?'
    level: 4
  - name: gaseous form
    source: '?'
    level: 3
  - name: magic circle against evil
    source: '?'
    level: 3
  - name: summon monster III
    source: '?'
    level: 3
  - name: cure moderate wounds
    source: '?'
    level: 2
  - name: eagle's splendor
    source: '?'
    level: 2
  - name: scorching ray
    source: '?'
    level: 2
  - name: silence
    source: '?'
    level: 2
    DC: 15
  - name: endure elements
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
  - name: protection from chaos
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: daze
    source: '?'
    level: 0
  - name: disrupt undead
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: ray of frost
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 9
    slots:
      4: 4
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 20
  DEX: 16
  CON: 20
  INT: 17
  WIS: 19
  CHA: 17
BAB: 12
CMB: 18
CMB_other: +22 grapple
CMD: 32
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Dodge
- name: Empower Spell
- is_bonus: true
  name: Eschew Materials
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
skills:
  Acrobatics: 18
  Bluff: 9
  Diplomacy: 18
  Fly: 20
  Knowledge (arcana): 9
  Knowledge (religion): 12
  Perception: 23
  Sense Motive: 15
  Spellcraft: 15
  Survival: 16
  Use Magic Device: 18
languages:
- Celestial
- Common
- Draconic
- telepathy 100 ft.
ecology:
  environment: warm forests
  organization: solitary, pair, or flight (3-6)
  treasure_type: standard
special_abilities:
  Spells: A couatl casts spells as a 9th-level sorcerer, and can cast spells from
    the cleric list as well as those normally available to a sorcerer. Cleric spells
    are considered arcane spells for a couatl, meaning that the creature does not
    need a divine focus to cast them.
  Poison (Ex): Injury-bite; save Fortitude DC 16; frequency 1/minute for 10 minutes;
    effect 1d4 Str; cure 2 consecutive saves. The DC is Constitution-based.
desc_long: |-
  Couatls are servants of lawful and good deities, though some operate independently of any greater being. Respected and admired for their wisdom and beauty, they try to steer mortals onto the right path and use their powers to fight evil, particularly those known to shift between the planes. Some couatls are viewed as benevolent gods by isolated societies, and while most couatls cringe at the thought of pretending to be a god, they allow such misconceptions to continue since they allow the couatls to guide and coax these societies onto paths of peace and cooperation with their neighbors. A couatl is about 12 feet long, with a wingspan of about 15 feet. It weighs 1,800 pounds.

  As native outsiders, couatls must eat. They prefer the same foods as true snakes, such as mammals and birds, though they have been known to eat evil humanoids.

  As they would rather spend their time promoting their agenda than hunting, couatls appreciate offers of food, particularly small boars and large game fowl.

  A couatl sometimes shows its favor to an adventurer or party that has done it a service by gifting the group with 1d4 of its brightly colored feathers. Such a freely given feather, if used as an additional material component, allows a spellcaster to cast planar ally to conjure that specific couatl without expending the typical payment of gold or other valuables-provided the the couatl approves of the service asked for by the spellcaster.

---

# Couatl
This great serpent has multicolored wings and eyes that glimmer with intense awareness.
**Source** Pathfinder RPG Bestiary pg. 49
**XP** 9,600

LG Large outsider (native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., detect chaos/evil/good/law; Perception +23

##### Defense

**AC** 22, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +1 dodge, +9 natural, –1 size)
**hp** 126 (12d10+60)
**Fort** +9, **Ref** +13, **Will** +14

##### Offense
**Speed** 20 ft., fly 60 ft. (good)
**Melee** bite +16 (1d8+7 plus _[[universal monster rules/Grab|grab]]_ and poison)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+7)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
Constant—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[spells/Ethereal Jaunt|ethereal jaunt]]_ (CL 16th), _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 20)
**Spells Known **(CL 9th)
4th (4/day)—_[[spells/Charm Monster|charm monster]]_ (DC 17), _[[spells/Freedom of Movement|freedom of movement]]_
3rd (7/day)—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd (7/day)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Silence|silence]]_ (DC 15)
1st (7/day)—_[[spells/Endure Elements|endure elements]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Chaos|protection from chaos]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Daze|daze]]_, _[[spells/Disrupt Undead|disrupt undead]]_, light, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 20, **Dex** 16, **Con** 20, **Int** 17, **Wis** 19, **Cha** 17
**Base Atk** +12; **CMB** +18 (+22 grapple); **CMD** 32 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +18, Bluff +9, Diplomacy +18, Fly +20, Knowledge (arcana) +9, Knowledge (religion) +12, Perception +23, Sense Motive +15, Spellcraft +15, Survival +16, Use Magic Device +18
**Languages** Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** warm forests
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–6)
**Treasure** standard

### Special Abilities
**Spells **A _[[monsters/Couatl|couatl]]_ casts spells as a 9th-level _[[classes/Sorcerer|sorcerer]]_, and can cast spells from the _[[classes/Cleric|cleric]]_ list as well as those normally available to a _sorcerer_. _Cleric_ spells are considered arcane spells for a _couatl_, meaning that the creature does not need a divine focus to cast them.

**Poison (Ex)** Injury—bite; save Fortitude DC 16; frequency 1/minute for 10 minutes; effect 1d4 Str; cure 2 consecutive saves. The DC is Constitution-based.

##### Description

Couatls are servants of lawful and good deities, though some operate independently of any greater being. Respected and admired for their wisdom and beauty, they try to steer mortals onto the right path and use their powers to fight evil, particularly those known to shift between the planes. Some couatls are viewed as _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ gods by isolated societies, and while most couatls cringe at the thought of pretending to be a god, they allow such misconceptions to continue since they allow the couatls to guide and coax these societies onto paths of peace and cooperation with their neighbors. A _couatl_ is about 12 feet long, with a wingspan of about 15 feet. It weighs 1,800 pounds.

As native outsiders, couatls must eat. They prefer the same foods as true snakes, such as mammals and birds, though they have been known to eat evil humanoids.

As they would rather spend their time promoting their agenda than hunting, couatls appreciate offers of food, particularly small boars and large game fowl.

A _couatl_ sometimes shows its favor to an adventurer or party that has done it a service by gifting the group with 1d4 of its brightly colored feathers. Such a freely given feather, if used as an additional material component, allows a spellcaster to cast _[[spells/Planar Ally|planar ally]]_ to conjure that specific _couatl_ without expending the typical payment of gold or other valuables—provided the the _couatl_ approves of the service asked for by the spellcaster.