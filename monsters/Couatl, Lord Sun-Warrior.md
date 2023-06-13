---
cssclass: [monsters]
title1: Couatl, Lord Sun-Warrior
desc_short: This brilliantly colored couatl radiates a palpable air of peace and wisdom.
title2: Lord Sun-Warrior
CR: 15
sources:
- name: Mythical Monsters Revisited
  page: 14
  link: http://paizo.com/products/btpy8pfw?Pathfinder-Campaign-Setting-Mythical-Monsters-Revisited
XP: 51200
race: Unique
classes:
- couatl
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
  AC: 28
  touch: 13
  flat_footed: 24
  components:
    dex: 3
    dodge: 1
    natural: 15
    size: -1
HP:
  HP: 230
  long: 20d10+120
saves:
  fort: 14
  ref: 17
  will: 19
immunities:
- mind-affecting effects
speeds:
  base: 20
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +26 (2d6+10 plus grab and poison)
      entries:
      - - damage: 2d6+10
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 26
  special:
  - constrict (2d6+10)
space: 10
reach: 10
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
  - name: alter self
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: ethereal jaunt
    source: default
    freq: At will
    CL: 18
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 23
  - name: wish
    source: default
    freq: 1/year
    CL: 20
  sources:
  - name: default
    CL: 9
    concentration: 15
spells:
  entries:
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 22
  - name: breath of life
    source: Sorcerer
    level: 5
  - name: flame strike
    source: Sorcerer
    level: 5
    DC: 21
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 20
  - name: freedom of movement
    source: Sorcerer
    level: 4
  - name: lesser geas
    source: Sorcerer
    level: 4
  - name: gaseous form
    source: Sorcerer
    level: 3
  - name: hold person
    source: Sorcerer
    level: 3
  - name: magic circle against evil
    source: Sorcerer
    level: 3
  - name: summon monster III
    source: Sorcerer
    level: 3
  - name: cure moderate wounds
    source: Sorcerer
    level: 2
  - name: eagle's splendor
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 18
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: silence
    source: Sorcerer
    level: 2
    DC: 18
  - name: endure elements
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: protection from chaos
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  - name: stabilize
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
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
  STR: 24
  DEX: 17
  CON: 22
  INT: 19
  WIS: 20
  CHA: 23
BAB: 20
CMB: 28
CMB_other: +32 grapple
CMD: 42
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Diehard
- name: Dodge
- name: Empower Spell
- is_bonus: true
  name: Eschew Materials
- name: Flyby Attack
- name: Great Fortitude
- name: Improved Initiative
- name: Improved Natural Attack (bite)
- name: Iron Will
- name: Lightning Reflexes
skills:
  Acrobatics: 26
    when jumping: 22
  Bluff: 19
  Diplomacy: 29
  Fly: 24
  Knowledge (arcana): 14
  Knowledge (planes): 17
  Knowledge (religion): 17
  Perception: 32
  Sense Motive: 32
  Spellcraft: 27
  Survival: 25
  Use Magic Device: 26
languages:
- Celestial
- Common
- Draconic
- Elven
- Polyglot
- telepathy 100 ft.
special_abilities:
  Poison (Ex): Injury-bite; save Fortitude DC 22; frequency 1/minute for 10 minutes;
    effect 1d4 Str; cure 2 consecutive saves. The DC is Constitution-based.
  Spells: Sun-Warrior casts spells as a 12th-level sorcerer, and can cast spells from
    the cleric list as well as from those normally available to a sorcerer. Cleric
    spells are considered arcane spells for couatls, meaning Sun-Warrior does not
    need a divine focus to cast them.
desc_long: |-
  Best known as the ancient guardian of the Utala tribe in the Mwangi Expanse, Mola Jushujaa (whose name means “Lord Sun-Warrior”) has appeared in many different lands and guises. He is a couatl of great age, and his pronouncements are well respected among the feathered serpents. Because of his venerable status, Jushujaa has a number of powers that lesser couatls do not possess, including the ability to change his appearance, create terrifying fire and lighting storms in combat, and even grant wishes (though only ever in service to the greatest possible good). He often takes the guise of an extremely old or young human, inoffensive and peaceful, visiting powerful rulers, priests, and nobles to either offer guidance or dissuade them from the path of evil.

  Lord Sun-Warrior acts independently of any deity, though he maintains positive relations with all of the good-aligned ones. His agenda is complex, but involves fostering the development of peaceful cultures and nations throughout many different worlds, and the discouragement or outright destruction of evil ones. In this he frequently recruits adventurers and other agents, dispatching them on quests that may not immediately make sense, and providing them with guidance and assistance as he is able. He is aided in his efforts by his champion, Jua Mfuasi (LG male human paladin of Iomedae 10), who was once a necromancer known as the Corpse-King until he was killed and returned to life by Sun-Warrior, after which he renounced his evil ways and abandoned arcane magic to become a paladin.

---

# Couatl, Lord Sun-Warrior
This brilliantly colored _[[monsters/Couatl|couatl]]_ radiates a palpable air of peace and wisdom.
**Source** Mythical Monsters Revisited pg. 14
**XP** 51,200
Unique _couatl_

LG Large outsider (native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., detect chaos/evil/good/law; Perception +32

##### Defense

**AC** 28, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+3 Dex, +1 dodge, +15 natural, –1 size)
**hp** 230 (20d10+120)
**Fort** +14, **Ref** +17, **Will** +19
**Immune** mind-affecting effects

##### Offense
**Speed** 20 ft., fly 60 ft. (average)
**Melee** bite +26 (2d6+10 plus _[[universal monster rules/Grab|grab]]_ and poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+10)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +15)
Constant—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_
At will—_[[spells/Alter Self|alter self]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Ethereal Jaunt|ethereal jaunt]]_ (CL 18th), _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 23)
1/year—_[[spells/Wish|wish]]_ (CL 20th)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(caster level 12th; concentration +18)
6th (4/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 22)
5th (6/day)—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Flame Strike|flame strike]]_ (DC 21)
4th (7/day)—_[[spells/Charm Monster|charm monster]]_ (DC 20), _[[spells/Freedom of Movement|freedom of movement]]_, lesser geas
3rd (7/day)—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Hold Person|hold person]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd (8/day)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Glitterdust|glitterdust]]_ (DC 18), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Silence|silence]]_ (DC 18)
1st (8/day)—_[[spells/Endure Elements|endure elements]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Chaos|protection from chaos]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, light, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 24, **Dex** 17, **Con** 22, **Int** 19, **Wis** 20, **Cha** 23
**Base Atk** +20; **CMB** +28 (+32 grapple); **CMD** 42 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Diehard|Diehard]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (bite), _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +26 (+22 when jumping), Bluff +19, Diplomacy +29, Fly +24, Knowledge (arcana) +14, Knowledge (planes) +17, Knowledge (religion) +17, Perception +32, Sense Motive +32, Spellcraft +27, Survival +25, Use Magic Device +26
**Languages** Celestial, Common, Draconic, Elven, Polyglot; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

### Special Abilities

**Poison (Ex)** Injury—bite; save Fortitude DC 22; frequency 1/minute for 10 minutes; effect 1d4 Str; cure 2 consecutive saves. The DC is Constitution-based.
**Spells **Sun-Warrior casts spells as a 12th-level _sorcerer_, and can cast spells from the _[[classes/Cleric|cleric]]_ list as well as from those normally available to a _sorcerer_. _Cleric_ spells are considered arcane spells for couatls, meaning Sun-Warrior does not need a divine focus to cast them.

##### Description

Best known as the ancient _[[items/Weapon Magic Abilities/Guardian|guardian]]_ of the Utala tribe in the Mwangi Expanse, Mola Jushujaa (whose name means “Lord Sun-Warrior”) has appeared in many different lands and guises. He is a _couatl_ of great age, and his pronouncements are well respected among the feathered serpents. Because of his venerable _[[spells/Status|status]]_, Jushujaa has a number of powers that lesser couatls do not possess, including the ability to change his appearance, create terrifying fire and lighting storms in combat, and even grant wishes (though only ever in service to the greatest possible good). He often takes the guise of an extremely old or young human, inoffensive and _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_, visiting powerful rulers, priests, and nobles to either offer _[[spells/Guidance|guidance]]_ or dissuade them from the path of evil.

Lord Sun-Warrior acts independently of any deity, though he maintains positive relations with all of the good-aligned ones. His agenda is complex, but involves fostering the development of _peaceful_ cultures and nations throughout many different worlds, and the discouragement or outright _[[spells/Destruction|destruction]]_ of evil ones. In this he frequently _[[feats/Recruits|recruits]]_ adventurers and other agents, dispatching them on quests that may not immediately make sense, and providing them with _guidance_ and assistance as he is able. He is aided in his efforts by his _[[items/Armor Magic Abilities/Champion|champion]]_, **Jua Mfuasi **(LG male human _[[classes/Paladin|paladin]]_ of Iomedae 10), who was once a necromancer known as the Corpse-King until he was killed and returned to life by Sun-Warrior, after which he renounced his evil ways and abandoned arcane magic to become a _paladin_.