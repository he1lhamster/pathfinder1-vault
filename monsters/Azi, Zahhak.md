---
cssclass: [monsters]
title1: Azi, Zahhak
is_3.5: true
desc_short: Like the darkness of the deepest abyss come to terrifying life, this gigantic
  dragon-serpent moves with deadly silence. Two rockcrushing forelimbs extend from
  its serpentine body and shadowy wings eclipse all in its path. A many horned visage
  glares down with glowing golden eyes, while two smaller snake-like heads sway upon
  dark, serpentine necks.
title2: Zahhak
CR: 19
sources:
- name: 'Pathfinder #24: The Final Wish'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy89a2
alignment: NE
size: Gargantuan
type: dragon
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: frightful presence
  radius: 100
AC:
  AC: 40
  touch: 9
  flat_footed: 37
  components:
    dex: 3
    natural: 31
    size: -4
HP:
  HP: 359
  long: 26d12+182
saves:
  fort: 22
  ref: 20
  will: 19
DR:
- amount: 15
  weakness: magic and good
immunities:
- paralysis effects
- poison
- sleep
SR: 29
speeds:
  base: 60
  fly: 100
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +34 (4d6+12)
      entries:
      - - damage: 4d6+12
      attack: bite
      bonus:
      - 34
    - text: 2 vipers +32 (2d8+6 plus poison)
      entries:
      - - damage: 2d8+6
        - effect: poison
      count: 2
      attack: vipers
      bonus:
      - 32
    - text: 2 claws +32 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +32 (2d8+6)
      entries:
      - - damage: 2d8+6
      attack: tail slap
      bonus:
      - 32
  special:
  - breath weapon
  - cursed to earth
  - poison
  - slain to serve
space: 20
reach: 15
reach_other: 20 ft. with bite, 25 ft. with vipers
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  - name: freedom of movement
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    DC: 18
  - name: see invisibility
    source: default
    freq: At will
  - name: control undead
    source: default
    freq: 3/day
    DC: 22
  - name: creeping doom
    source: default
    freq: 3/day
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: dispel good
    source: default
    freq: 3/day
    DC: 21
  - name: fog cloud
    source: default
    freq: 3/day
  - name: greater shout
    source: default
    freq: 3/day
    DC: 24
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 24
  - name: transmute rock to mud
    source: default
    freq: 3/day
    DC: 21
  - name: veil
    source: default
    freq: 3/day
    DC: 22
  - name: control weather
    source: default
    freq: 1/day
  - name: hallucinatory terrain
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 17
ability_scores:
  STR: 34
  DEX: 17
  CON: 25
  INT: 17
  WIS: 19
  CHA: 22
BAB: 26
grapple_3.5: 50
feats:
- name: Alertness
- name: Awesome Blow
- name: Combat Reflexes
- name: Improved Initiative
- name: Improved Overrun
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Run
skills:
  Appraise: 18
  Bluff: 35
  Climb: 27
  Hide: 6
  Intimidation: 39
  Jump: 39
  Knowledge (arcana): 18
  Knowledge (geography): 18
  Knowledge (the planes): 18
  Listen: 35
  Move Silently: 18
  Sense Motive: 14
  Spot: 35
  Swim: 27
languages:
- Abyssal
- Common
- Draconic
- Infernal
special_qualities:
- blasphemous boon
ecology:
  environment: warm hills
  organization: solitary
  treasure:
  - double standard
  advancement_3.5:
  - type: size
    HD_min: 27
    size: Gargantuan
    HD_max: 36
  - type: size
    HD_min: 37
    size: Colossal
    HD_max: 46
special_abilities:
  Blasphemous Boon (Su): Once per day a zahhak can grant a single terrible wish. This
    ability is treated as a wish that a zahhak can cast for any willing nondragon.
    While the ability initially seems to grant the desired effect, it invariably brings
    hardship and sorrow to whoever made the wish. This hardship typically manifests
    within a month, and may take any form the GM desires. (See the Wishcraft article
    on page 56 for suggestions on corrupting wishes.)
  Breath Weapon (Su): A zahhak can unleash a gout of noxious flame that both burns
    and poisons any creature it touches (60-foot cone, once every 1d4 rounds, damage
    18d8 fire, Reflex DC 30 half). In addition, any creature damaged by the flames
    must make an additional DC 30 Fortitude save or be poisoned (initial and secondary
    damage 2d6 Dex). Creatures immune to fire or that take no damage from a zahhak's
    breath due to damage reduction are not affected by the fire's poison. Both save
    DCs are Constitution-based.
  Cursed to Earth (Su): Zahhaks detest all creatures capable of flight. Once every
    minute, a zahhak can rasp a terrible curse that causes any single flying creature
    or object it can see to plummet to the ground and be unable to fly for the next
    10 minutes. The target must make a DC 29 Will save or immediately fall, regardless
    of its method of flight (natural, magical, by magic item, or otherwise), and takes
    full damage from the fall. In cases where multiple creatures might be using a
    single object to fly, the passenger with the highest Will save modifier makes
    this check to avoid having the entire conveyance fall. In situations where a creature
    rides another flying creature, the flying creature, not the rider, makes this
    save. After falling, a cursed creature cannot take to the air again by any means
    for 10 minutes, even through the use of an additional spell, magic item, or flying
    conveyance-spells fail, magic refuses to work, items malfunction. A remove curse
    spell ends this curse's effects immediately, but cannot prevent a target from
    falling unless the spellcaster prepares to cast the spell as a readied action.
    The save DC is Charisma-based.
  Frightful Presence (Su): A zahhak unsettles its foes with its mere presence. Any
    creatures with fewer HD than the azi that comes within 100 feet must succeed on
    a DC 29 Will save. On a failure, creatures with 4 or less HD become panicked for
    4d6 rounds and those with 5 or more HD become shaken for 4d6 rounds. Any creature
    that succeeds on its save is immune to that zahhak's frightful presence for 24
    hours. Zahhaks ignore the frightful presence of other dragons. This is a mind-affecting
    fear effect. The save DC is Charisma-based.
  Poison (Ex): The vipers flanking a zahhak's primary head drip with a vicious poison
    (injury, Fortitude DC 30, initial and secondary damage 1d6 Con). The save is Constitution-based.
  Slain to Serve (Su): Any humanoid slain by a zahhak animates as a ghoul after 1d4
    rounds. These ghouls are under the command of the zahhak that created them and
    remain enslaved until their destruction. They do not possess any of the abilities
    they had in life.
desc_long: Lords among the abominations of dragonkind, zahhaks rule as the most powerful
  race of azi dragons. First spawned by the corruptions wreaked by Ahriman, Lord of
  the Divs, and the foul dragon god Dahak, these bitter wyrms are named in honor of
  their draconic master and seek to sow fear and spread slaughter. Their very breaths
  are tainted with corruption, a vile double boon, half draconic flame, and half lethal
  poison, and from their claws seeps such depravity as to raise the dead from their
  graves. Enormous beasts, zahhaks resemble primeval wyrms with two black-scaled vipers
  lashing from each side of their necks. These smaller, serpentine heads are unthinking
  appendages, which lash out at any creature that comes too near. A zahhak measures
  upward of 35 feet from its muzzle to the base of its tail, and weighs over 18 tons.

---

# Azi, Zahhak
Like the _[[spells/Darkness|darkness]]_ of the deepest abyss come to terrifying life, this gigantic dragon-serpent moves with _[[items/Weapon Magic Abilities/Deadly|deadly]]_ _[[spells/Silence|silence]]_. Two rockcrushing forelimbs extend from its serpentine body and shadowy wings eclipse all in its path. A many horned visage glares down with glowing golden eyes, while two smaller snake-like heads sway upon dark, serpentine necks.
**Source** Pathfinder #24: The Final _[[spells/Wish|Wish]]_ pg. 82

NE Gargantuan dragon
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Listen +35, Spot +35
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (100 ft.)

##### Defense

**AC** 40, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+3 Dex, +31 natural, -4 size)
**hp** 359 (26d12+182)
**Fort** +22, **Ref** +20, **Will** +19
**DR** 15/magic and good; **Immune** _[[universal monster rules/Paralysis|paralysis]]_ effects, poison, sleep; **SR** 29

##### Offense
**Speed** 60 ft., fly 100 ft. (clumsy)
**Melee** bite +34 (4d6+12) and 2 vipers +32 (2d8+6 plus poison) and 2 claws +32 (2d6+6) and tail slap +32 (2d8+6)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite, 25 ft. with vipers)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, cursed to earth, poison, slain to serve
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th)
At will — _darkness_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Invisibility|invisibility]]_ (DC 18), _[[spells/See Invisibility|see invisibility]]_
3/day — _[[spells/Control Undead|control undead]]_ (DC 22), _[[spells/Creeping Doom|creeping doom]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Good|dispel good]]_ (DC 21), _[[spells/Fog Cloud|fog cloud]]_, greater _[[spells/Shout|shout]]_ (DC 24), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 24), _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ (DC 21), _[[spells/Veil|veil]]_ (DC 22)
1/day — _[[spells/Control Weather|control weather]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 20)

##### Statistics
**Str** 34, **Dex** 17, **Con** 25, **Int** 17, **Wis** 19, **Cha** 22
**Base Atk** +26; **Grapple** +50
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, Run
**Skills** Appraise +18, Bluff +35, _[[universal monster rules/Climb|Climb]]_ +27, Hide +6, Intimidate +39, _[[spells/Jump|Jump]]_ +39, Knowledge (arcana) +18, Knowledge (geography) +18, Knowledge (the planes) +18, Listen +35, Move Silently +18, Sense Motive +14, Spot +35, Swim +27
**Languages** Abyssal, Common, Draconic, Infernal
**SQ** blasphemous boon

##### Ecology

**Environment** warm hills
**Organization** solitary
**Treasure** double standard
**Advancement** 27-36 HD (Gargantuan), 37-46 HD (Colossal)

### Special Abilities

**Blasphemous Boon (Su)** Once per day a zahhak can grant a single terrible _wish_. This ability is treated as a _wish_ that a zahhak can cast for any willing nondragon. While the ability initially seems to grant the desired effect, it invariably brings hardship and sorrow to whoever made the _wish_. This hardship typically manifests within a month, and may take any form the GM desires. (See the Wishcraft article on page 56 for suggestions on corrupting wishes.)

**_Breath Weapon_ (Su)** A zahhak can unleash a gout of noxious flame that both burns and poisons any creature it touches (60-foot cone, once every 1d4 rounds, damage 18d8 fire, Reflex DC 30 half). In addition, any creature damaged by the flames must make an additional DC 30 Fortitude save or be poisoned (initial and secondary damage 2d6 Dex). Creatures immune to fire or that take no damage from a zahhak’s breath due to _[[universal monster rules/Damage Reduction|damage reduction]]_ are not affected by the fire’s poison. Both save DCs are Constitution-based.

**Cursed to Earth (Su)** Zahhaks detest all creatures capable of _[[universal monster rules/Flight|flight]]_. Once every minute, a zahhak can rasp a terrible curse that causes any single flying creature or object it can see to plummet to the ground and be unable to fly for the next 10 minutes. The target must make a DC 29 Will save or immediately fall, regardless of its method of _flight_ (natural, magical, by magic item, or otherwise), and takes full damage from the fall. In cases where multiple creatures might be using a single object to fly, the passenger with the highest Will save modifier makes this check to avoid having the entire conveyance fall. In situations where a creature rides another flying creature, the flying creature, not the rider, makes this save. After falling, a cursed creature cannot take to the air again by any means for 10 minutes, even through the use of an additional spell, magic item, or flying conveyance—spells fail, magic refuses to work, items _[[spells/Malfunction|malfunction]]_. A _[[spells/Remove Curse|remove curse]]_ spell ends this curse’s effects immediately, but cannot prevent a target from falling unless the spellcaster prepares to cast the spell as a readied action. The save DC is Charisma-based.

**_Frightful Presence_ (Su)** A zahhak unsettles its foes with its mere presence. Any creatures with fewer HD than the azi that comes within 100 feet must succeed on a DC 29 Will save. On a failure, creatures with 4 or less HD become _[[conditions/Panicked|panicked]]_ for 4d6 rounds and those with 5 or more HD become _[[conditions/Shaken|shaken]]_ for 4d6 rounds. Any creature that succeeds on its save is immune to that zahhak’s _frightful presence_ for 24 hours. Zahhaks ignore the _frightful presence_ of other dragons. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DC is Charisma-based.

**Poison (Ex)** The vipers flanking a zahhak’s primary head drip with a _[[items/Weapon Magic Abilities/Vicious|vicious]]_ poison (injury, Fortitude DC 30, initial and secondary damage 1d6 Con). The save is Constitution-based.
**Slain to Serve (Su)** Any humanoid slain by a zahhak animates as a _[[monsters/Ghoul|ghoul]]_ after 1d4 rounds. These ghouls are under the _[[spells/Command|command]]_ of the zahhak that created them and remain enslaved until their _[[spells/Destruction|destruction]]_. They do not possess any of the abilities they had in life.

##### Description

Lords among the abominations of dragonkind, zahhaks rule as the most powerful race of azi dragons. First spawned by the corruptions wreaked by Ahriman, Lord of the Divs, and the foul dragon god Dahak, these _[[items/Armor Magic Abilities/Bitter|bitter]]_ wyrms are named in honor of their draconic master and seek to sow _fear_ and spread slaughter. Their very breaths are tainted with corruption, a vile double boon, half draconic flame, and half lethal poison, and from their claws seeps such depravity as to raise the dead from their graves. Enormous beasts, zahhaks resemble primeval wyrms with two black-scaled vipers lashing from each side of their necks. These smaller, serpentine heads are unthinking appendages, which lash out at any creature that comes too near. A zahhak measures upward of 35 feet from its muzzle to the base of its tail, and weighs over 18 tons.