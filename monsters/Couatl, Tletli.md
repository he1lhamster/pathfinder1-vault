---
cssclass: [monsters]
title1: Couatl, Tletli
desc_short: This massive flying serpent's iridescent scales glimmer like opals, and
  white-hot flames dance along the feathers of its burning wings.
title2: Tletli
CR: 14
sources:
- name: "Pathfinder #143: Borne by the Sun's Grace"
  page: 84
  link: https://paizo.com/products/btq01vyh
XP: 38400
alignment: NG
size: Huge
type: outsider
subtypes:
- native
initiative:
  bonus: 8
senses:
  darkvision: 120
  detect chaos/evil/good/ law: true
AC:
  AC: 30
  touch: 13
  flat_footed: 25
  components:
    dex: 4
    dodge: 1
    natural: 17
    size: -2
HP:
  HP: 200
  long: 16d10+112
saves:
  fort: 12
  ref: 16
  will: 17
immunities:
- fire
resistances:
  acid: 15
  cold: 15
  electricity: 15
SR: 25
speeds:
  base: 30
  fly: 120
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +25 (2d8+11/19-20 plus grab and poison)
      entries:
      - - damage: 2d8+11
          crit_range: 19-20
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 25
    - text: 2 wings +20 (1d8+5 plus burn and stoke fire)
      entries:
      - - damage: 1d8+5
        - effect: burn
        - effect: stoke fire
      count: 2
      attack: wings
      bonus:
      - 20
  special:
  - breath weapon (50-ft. cone, 12d6 fire, Reflex DC 25 half, usable every 1d4 rounds)
  - burn (2d6 fire, DC 25)
  - constrict (2d8+11 plus burn)
space: 15
reach: 15
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
    DC: 17
  - name: ethereal jaunt
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 22
  - name: sunburst
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 12
    concentration: 18
spells:
  entries:
  - name: holy word
    source: '?'
    level: 6
    DC: 22
  - name: dismissal
    source: '?'
    level: 5
    DC: 21
  - name: flame strike
    source: '?'
    level: 5
  - name: dispel evil
    source: '?'
    level: 4
    DC: 20
  - name: holy smite
    source: '?'
    level: 4
  - name: wall of fire
    source: '?'
    level: 4
  - name: daylight
    source: '?'
    level: 3
  - name: dispel magic
    source: '?'
    level: 3
  - name: fireball
    source: '?'
    level: 3
    DC: 19
  - name: searing light
    source: '?'
    level: 3
    DC: 19
  - name: castigate
    source: '?'
    level: 2
    DC: 18
  - name: eagle's splendor
    source: '?'
    level: 2
  - name: flaming sphere
    source: '?'
    level: 2
    DC: 18
  - name: gust of wind
    source: '?'
    level: 2
    DC: 18
  - name: scorching ray
    source: '?'
    level: 2
  - name: burning hands
    source: '?'
    level: 1
    DC: 17
  - name: charm person
    source: '?'
    level: 1
    DC: 17
  - name: comprehend languages
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: protection from evil
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 16
  - name: detect magic
    source: '?'
    level: 0
  - name: flare
    source: '?'
    level: 0
    DC: 16
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 12
    concentration: 18
    slots:
      6: 4
      5: 6
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 32
  DEX: 19
  CON: 24
  INT: 17
  WIS: 24
  CHA: 23
BAB: 16
CMB: 29
CMB_other: +33 grapple
CMD: 44
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Dodge
- name: Eschew MaterialsB
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Vital Strike
skills:
  Bluff: 25
  Fly: 15
  Intimidate: 25
  Knowledge (arcana): 22
  Knowledge (planes): 22
  Perception: 30
  Sense Motive: 30
  Spellcraft: 19
  Stealth: 15
languages:
- Celestial
- Common
- Draconic
- telepathy 100 ft.
special_qualities:
- holy fire
ecology:
  environment: any
  organization: solitary, pair, or revelation (3-6 plus 1-2 angels and 1 chicome couatl)
  treasure_type: standard
special_abilities:
  Holy Fire (Su): Fire damage dealt by a tletli, including that of its breath weapon
    and spells, is infused with divine energy. Half the damage of such attacks is
    fire damage, but the other half is the result of holy power and thus not subject
    to being reduced by resistance to fire-based attacks. Fire damage dealt by a tletli
    is considered good-aligned for the purpose of overcoming damage reduction.
  Poison (Ex): Injury-bite; save Fort DC 25; frequency 1/minute for 10 minutes; effect
    1d6 Str; cure 2 consecutive saves.
  Spells: A tletli casts spells as a 12th-level sorcerer, and can cast spells from
    the inquisitor and paladin spell lists as well as those normally available to
    a sorcerer. These divine spells are considered arcane spells for the tletli, meaning
    that the creature does not need a divine focus to cast them.
  Stoke Flames (Ex): Once per round when a tletli attacks with its wings, it can cause
    areas of active fire within 30 feet to spread as a free action. An affected 5-foot
    square of fire spreads to one adjacent square that is not on fire, possibly burning
    objects or creatures in that space. The tletli determines which adjacent squares
    are set on fire.
desc_long: |-
  Of all the couatls, tletlis are among the most vengeful and easily the most actively destructive, channeling their righteous fury to rid Golarion of large swaths of evildoers. While some couatls may offer redemption to evil individuals, a tletli withholds salvation and exacts punishment on whole sects of people whose crimes they deem warrant oblivion. Tletlis do not hunt down individuals, instead targeting gangs, corrupt governments, and even entire settlements that they believe have fallen beyond redemption.

   The tletli is a terrifying sight to behold. Its wings are continually shrouded in flame, ranging from warm orange at the base to hot blue at the tips, causing the air around the couatl to radiate with an ominous light best described as apocalyptic. Further magnifying the effect, the beast's opalescent scales seem to reflect a divine light. A typical tletli is 35 long with a wingspan of 25 feet. It is one of the heaviest couatls, weighing nearly 6,000 pounds.

---

# Couatl, Tletli
This massive flying serpent’s iridescent scales glimmer like opals, and white-hot flames dance along the feathers of its _[[items/Weapon Magic Abilities/Burning|burning]]_ wings.
**Source** Pathfinder #143: Borne by the Sun's _[[spells/Grace|Grace]]_ pg. 84
**XP** 38,400

NG Huge outsider (native)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., detect chaos/evil/good/ law; Perception +30

##### Defense

**AC** 30, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +1 dodge, +17 natural, –2 size)
**hp** 200 (16d10+112)
**Fort** +12, **Ref** +16, **Will** +17
**Immune** fire; **Resist** acid 15, cold 15, electricity 15; **SR** 25

##### Offense
**Speed** 30 ft., fly 120 ft. (poor)
**Melee** bite +25 (2d8+11/19–20 plus _[[universal monster rules/Grab|grab]]_ and poison), 2 wings +20 (1d8+5 plus _[[universal monster rules/Burn|burn]]_ and stoke fire)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d6 fire, Reflex DC 25 half, usable every 1d4 rounds), _burn_ (2d6 fire, DC 25), _[[universal monster rules/Constrict|constrict]]_ (2d8+11 plus _burn_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +18)
Constant—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_
 At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 22)
 1/day—_[[spells/Sunburst|sunburst]]_ (DC 24)
**Spells Known** (CL 12th; concentration +18)
6th (4/day)—_[[spells/Holy Word|holy word]]_ (DC 22)
 5th (6/day)—_[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Flame Strike|flame strike]]_ 
4th (7/day)—_[[spells/Dispel Evil|dispel evil]]_ (DC 20), _[[spells/Holy Smite|holy smite]]_, _[[spells/Wall Of Fire|wall of fire]]_ 
3rd (7/day)—_[[spells/Daylight|daylight]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 19), _[[spells/Searing Light|searing light]]_ (DC 19) 
2nd (8/day)—_[[spells/Castigate|castigate]]_ (DC 18), _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 18), _[[spells/Gust Of Wind|gust of wind]]_ (DC 18), _[[spells/Scorching Ray|scorching ray]]_ 
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 17), _[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Protection From Evil|protection from evil]]_ 
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 16), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 32, **Dex** 19, **Con** 24, **Int** 17, **Wis** 24, **Cha** 23
**Base Atk** +16; **CMB** +29 (+33 grapple); **CMD** 44 (can't be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, Eschew MaterialsB, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +25, Fly +15, Intimidate +25, Knowledge (arcana) +22, Knowledge (planes) +22, Perception +30, Sense Motive +30, Spellcraft +19, Stealth +15
**Languages** Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** holy fire

##### Ecology

**Environment** any
**Organization** solitary, pair, or _[[spells/Revelation|revelation]]_ (3–6 plus 1–2 angels and 1 chicome _[[monsters/Couatl|couatl]]_)
**Treasure** standard

### Special Abilities

**Holy Fire (Su)** Fire damage dealt by a tletli, including that of its _breath weapon_ and spells, is infused with divine energy. Half the damage of such attacks is fire damage, but the other half is the result of holy power and thus not subject to being reduced by _resistance_ to fire-based attacks. Fire damage dealt by a tletli is considered good-aligned for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.

**Poison (Ex)** Injury—bite; save Fort DC 25; frequency 1/minute for 10 minutes; effect 1d6 Str; cure 2 consecutive saves.
**Spells** A tletli casts spells as a 12th-level _[[classes/Sorcerer|sorcerer]]_, and can cast spells from the _[[classes/Inquisitor|inquisitor]]_ and _[[classes/Paladin|paladin]]_ spell lists as well as those normally available to a _sorcerer_. These divine spells are considered arcane spells for the tletli, meaning that the creature does not need a divine focus to cast them.
**Stoke Flames (Ex)** Once per round when a tletli attacks with its wings, it can cause areas of active fire within 30 feet to spread as a free action. An affected 5-foot square of fire spreads to one adjacent square that is not on fire, possibly _burning_ objects or creatures in that space. The tletli determines which adjacent squares are set on fire.

##### Description

Of all the couatls, tletlis are among the most vengeful and easily the most actively destructive, _[[items/Armor Magic Abilities/Channeling|channeling]]_ their _[[items/Armor Magic Abilities/Righteous|righteous]]_ fury to rid Golarion of large swaths of evildoers. While some couatls may offer _[[feats/Redemption|redemption]]_ to evil individuals, a tletli withholds salvation and exacts punishment on whole sects of people whose crimes they deem warrant _[[monsters/Oblivion|oblivion]]_. Tletlis do not hunt down individuals, instead targeting gangs, corrupt governments, and even entire settlements that they believe have _[[monsters/Fallen|fallen]]_ beyond _redemption_.

The tletli is a terrifying sight to behold. Its wings are continually shrouded in flame, ranging from warm orange at the base to hot blue at the tips, causing the air around the _couatl_ to radiate with an _[[items/Weapon Magic Abilities/Ominous|ominous]]_ light best described as apocalyptic. Further magnifying the effect, the beast’s opalescent scales seem to reflect a divine light. A typical tletli is 35 long with a wingspan of 25 feet. It is one of the heaviest couatls, weighing nearly 6,000 pounds.