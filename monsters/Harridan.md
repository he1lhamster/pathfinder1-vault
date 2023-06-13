---
cssclass: [monsters]
title1: Harridan
is_3.5: true
desc_short: This massive beast is a beautiful giantess from the waist up and a vicious
  hunting cat from the waist down. Somehow, the look of abject cruelty in her eyes
  is more unsettling than the feral claws of her lower half.
title2: Harridan
CR: 12
sources:
- name: 'Pathfinder #6: Spires of Xin-Shalast'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy817c
alignment: Usually CE
size: Huge
type: magical beast
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 8
  flat_footed: 25
  components:
    armor: 5
    dex: 2
    natural: 14
    size: -2
HP:
  HP: 161
  long: 17d10+68
saves:
  fort: 14
  ref: 12
  will: 10
DR:
- amount: 10
  weakness: magic
SR: 23
speeds:
  base: 60
attacks:
  melee:
  - - text: touch +23 (1d8 Wisdom drain)
      entries:
      - - damage: 1d8
          type: Wisdom drain
      attack: touch
      bonus:
      - 23
  - - text: mwk greatsword +24 (4d6+8/19-20)
      entries:
      - - damage: 4d6+8
          crit_range: 19-20
      attack: mwk greatsword
      bonus:
      - 24
    - text: 2 claws +22 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 22
  special:
  - pounce
  - rake
  - spells
  - Wisdom drain
space: 15
reach: 10
spell_like_abilities:
  entries:
  - name: blade barrier
    source: default
    freq: 6th
    DC: 19
  - name: greater dispel magic
    source: default
    freq: 6th
  - is_domain_spell: true
    name: harm
    source: default
    freq: 6th
    DC: 19
  - is_domain_spell: true
    name: dispel good
    source: default
    freq: 5th
    DC: 18
  - name: flame strike
    source: default
    freq: 5th
    DC: 18
  - name: greater command
    source: default
    freq: 5th
    DC: 18
  - name: true seeing
    source: default
    freq: 5th
  - name: air walk
    source: default
    freq: 4th
  - name: dimensional anchor
    source: default
    freq: 4th
    DC: 17
  - name: freedom of movement
    source: default
    freq: 4th
  - is_domain_spell: true
    name: inflict critical wounds
    source: default
    freq: 4th
  - name: blindness/deafness
    source: default
    freq: 3rd
    DC: 16
  - is_domain_spell: true
    name: contagion
    source: default
    freq: 3rd
    DC: 16
  - name: dispel magic
    source: default
    freq: 3rd
  - name: invisibility purge
    source: default
    freq: 3rd
  - name: meld into stone
    source: default
    freq: 3rd
  - name: prayer
    source: default
    freq: 3rd
  - name: aid
    source: default
    freq: 2nd
  - name: cure moderate wounds
    source: default
    freq: 2nd
    other: '3'
  - name: death knell
    source: default
    freq: 2nd
    DC: 15
  - is_domain_spell: true
    name: desecrate
    source: default
    freq: 2nd
  - name: command
    source: default
    freq: 1st
    DC: 14
  - name: comprehend languages
    source: default
    freq: 1st
  - name: cure light wounds
    source: default
    freq: 1st
  - name: doom
    source: default
    freq: 1st
    DC: 14
  - name: obscuring mist
    source: default
    freq: 1st
  - is_domain_spell: true
    name: protection from good
    source: default
    freq: 1st
  - name: shield of faith
    source: default
    freq: 1st
  - name: detect magic
    source: default
    freq: '0'
  - name: detect poison
    source: default
    freq: '0'
  - name: inflict minor wounds
    source: default
    freq: '0'
  - name: light
    source: default
    freq: '0'
  - name: read magic
    source: default
    freq: '0'
  - name: resistance
    source: default
    freq: '0'
  sources:
  - name: default
    CL: 12
    domains:
    - destruction
    - evil
ability_scores:
  STR: 26
  DEX: 15
  CON: 19
  INT: 13
  WIS: 16
  CHA: 16
BAB: 17
grapple_3.5: 33
feats:
- name: Altitude Affinity
- name: Dodge
- name: Iron Will
- name: Mobility
- name: Multiattack
- name: Spring Attack
skills:
  Bluff: 16
  Climb: 12
  Concentration: 14
  Diplomacy: 10
  Hide: 12
  Knowledge (arcana): 6
  Listen: 13
  Move Silently: 7
  Spot: 13
  _racial_mods:
    Climb:
      _: 4
    Bluff:
      _: 8
    Hide:
      _: 8
languages:
- Common
- Giant
- Thassilonian
gear:
  gear:
  - masterwork breastplate
  - masterwork greatsword
ecology:
  environment: any mountain or desert
  organization: solitary, pair, or gang (3-4)
  treasure:
  - double standard
  advancement_3.5:
  - type: class
    favored_class: cleric
special_abilities:
  Pounce (Ex): If a harridan charges, she can attack with both of her claws and make
    two rake attacks.
  Rake (Ex): Attack bonus +23, damage 1d6+4.
  Spells: A harridan casts spells as a 12th-level cleric. Her save DCs are Wisdom-based.
  Wisdom Drain (Su): A harridan drains 1d8 points of Wisdom each time she hits with
    her melee touch attack. (Unlike with other kinds of ability drain attacks, a harridan
    does not heal any damage when she uses her Wisdom drain.)
desc_long: |-
  Harridans are manipulators and slave takers, the spiritual leaders of the lamyros race's dark faith. Megalomaniacal and corrupt, these giant lamias obsess over control, seeking to bend all they encounter to their will through lies and subtlety, brute force, or magic. Fewer in number than even the rare lamia matriarchs (see Pathfinder #2), harridans are the cunning masterminds of their race and all other lamias rightly fear and obey these powerful and cruel despots.

   A harridan is a massive creature with the torso of a gigantic female humanoid sprouting from the body of a 20-foot-long dire lion. Her fur is darker than that of a normal dire lion, making it easier for her to blend in with the rocks of the mountains and deserts where harridans reside, and her upper body is hairless save for a luxurious mane of thick hair growing from her scalp. Harridans often weigh upwards of 6,000 pounds and can live to be more than 500 years old.

---

# Harridan
This massive beast is a beautiful giantess from the waist up and a _[[items/Weapon Magic Abilities/Vicious|vicious]]_ hunting cat from the waist down. Somehow, the look of abject _[[feats/Cruelty|cruelty]]_ in her eyes is more unsettling than the feral claws of her lower half.
**Source** Pathfinder #6: Spires of Xin-Shalast pg. 82
Usually CE Huge magical beast
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Listen +13, Spot +13

##### Defense

**AC** 25, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+5 armor, +2 Dex, +14 natural, -2 size)
**hp** 161 (17d10+68)
**Fort** +14, **Ref** +12, **Will** +10
**DR** 10/magic; **SR** 23

##### Offense
**Speed** 60 ft.
**Melee** touch +23 (1d8 Wisdom drain) or mwk _[[items/Weapon/Greatsword|greatsword]]_ +24 (4d6+8/19-20) and 2 claws +22 (1d6+4)
**Space** 15 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_, spells, Wisdom drain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
6th — _[[spells/Blade Barrier|blade barrier]]_ (DC 19), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Harm|harm]]_ (DC 19)
5th — _[[spells/Dispel Good|dispel good]]_ (DC 18), _[[spells/Flame Strike|flame strike]]_ (DC 18), greater _[[spells/Command|command]]_ (DC 18), _[[spells/True Seeing|true seeing]]_
4th — _[[spells/Air Walk|air walk]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_ (DC 17), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_
3rd — blindness/deafness (DC 16), _[[spells/Contagion|contagion]]_ (DC 16), _dispel magic_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Prayer|prayer]]_
2nd — aid, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (3), _[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Desecrate|desecrate]]_
1st — _command_ (DC 14), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Doom|doom]]_ (DC 14), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 — _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, inflict minor wounds, light, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains** _[[spells/Destruction|Destruction]]_, Evil

##### Statistics
**Str** 26, **Dex** 15, **Con** 19, **Int** 13, **Wis** 16, **Cha** 16
**Base Atk** +17; **Grapple** +33
**Feats** _[[feats/Altitude Affinity|Altitude Affinity]]_, Dodge, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Bluff +16, _[[universal monster rules/Climb|Climb]]_ +12, Concentration +14, Diplomacy +10, Hide +12, Knowledge (arcana) +6, Listen +13, Move Silently +7, Spot +13; **Racial Modifiers** +4 _Climb_, +8 Bluff, +8 Hide
**Languages** Common, Giant, Thassilonian
**Gear** masterwork _[[items/Armor/Breastplate|breastplate]]_, masterwork _greatsword_

##### Ecology

**Environment** any mountain or desert
**Organization** solitary, pair, or gang (3-4)
**Treasure** double standard
**Advancement** by character class; **Favored Class** _[[classes/Cleric|cleric]]_

### Special Abilities

**_Pounce_ (Ex)** If a _[[monsters/Harridan|harridan]]_ charges, she can attack with both of her claws and make two _rake_ attacks.

**_Rake_ (Ex)** Attack bonus +23, damage 1d6+4.
**Spells** A _harridan_ casts spells as a 12th-level _cleric_. Her save DCs are Wisdom-based.

**Wisdom Drain (Su)** A _harridan_ drains 1d8 points of Wisdom each time she hits with her melee touch attack. (Unlike with other kinds of ability drain attacks, a _harridan_ does not _[[spells/Heal|heal]]_ any damage when she uses her Wisdom drain.)

##### Description

Harridans are manipulators and _[[items/Mundane/Slave|slave]]_ takers, the spiritual leaders of the lamyros race’s dark faith. Megalomaniacal and corrupt, these giant lamias obsess over control, seeking to bend all they encounter to their will through lies and subtlety, brute force, or magic. Fewer in number than even the rare _[[monsters/Lamia|lamia]]_ matriarchs (see Pathfinder #2), harridans are the _[[items/Weapon Magic Abilities/Cunning|cunning]]_ masterminds of their race and all other lamias rightly _[[universal monster rules/Fear|fear]]_ and obey these powerful and _[[items/Weapon Magic Abilities/Cruel|cruel]]_ despots.

A _harridan_ is a massive creature with the torso of a gigantic female humanoid sprouting from the body of a 20-foot-long dire _[[monsters/Lion|lion]]_. Her fur is darker than that of a normal dire _lion_, making it easier for her to _[[spells/Blend|blend]]_ in with the rocks of the mountains and deserts where harridans reside, and her upper body is hairless save for a luxurious mane of thick hair _[[items/Weapon Magic Abilities/Growing|growing]]_ from her scalp. Harridans often weigh upwards of 6,000 pounds and can live to be more than 500 years old.