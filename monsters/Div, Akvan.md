---
cssclass: [monsters]
title1: Div, Akvan
desc_short: Ornate armor covers this hulking creature, rocky protrusions jutting from
  its hide and fierce horns crowning its broad head.
title2: Akvan
CR: 20
sources:
- name: Bestiary 3
  page: 84
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 307200
alignment: NE
size: Gargantuan
type: outsider
subtypes:
- div
- evil
- extraplanar
initiative:
  bonus: 12
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: hopelessness
  radius: 30
  DC: 30
AC:
  AC: 38
  touch: 10
  flat_footed: 34
  components:
    armor: 13
    dex: 4
    natural: 15
    size: -4
HP:
  HP: 372
  long: 24d10+240
saves:
  fort: 18
  ref: 22
  will: 21
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- fire
- poison
resistances:
  acid: 10
  electricity: 10
SR: 31
speeds:
  base: 50
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +32 (2d8+12 plus grab/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: claws
      bonus:
      - 32
    - text: tail slap +30 (2d10+6)
      entries:
      - - damage: 2d10+6
      attack: tail slap
      bonus:
      - 30
  special:
  - create ghul
  - rend (2 claws, 2d6+18)
  - shake faith
  - swallow whole (6d6+18 plus 4d6 energy damage, AC 25, 37 hp)
  - torturous gullet
  - trample (2d8+18, DC 34)
space: 20
reach: 20
reach_other: 25 ft. with tail
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: align weapon
    source: default
    freq: At will
  - name: detect magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: magic circle against good
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 23
  - name: blasphemy
    source: default
    freq: 3/day
    DC: 25
  - name: disintegrate
    source: default
    freq: 3/day
    DC: 24
  - name: dispel magic
    source: default
    freq: 3/day
  - name: forcecage
    source: default
    freq: 3/day
    DC: 25
  - name: protection from energy
    source: default
    freq: 3/day
  - name: geas/quest
    source: default
    freq: 1/day
  - name: plane shift
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: sepids
      amount: 1d2
      chance: 100%
  sources:
  - name: default
    CL: 20
    concentration: 28
ability_scores:
  STR: 35
  DEX: 26
  CON: 30
  INT: 19
  WIS: 24
  CHA: 27
BAB: 24
CMB: 40
CMD: 58
feats:
- name: Awesome Blow
- name: Cleave
- name: Combat Reflexes
- name: Critical Focus
- name: Great Cleave
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Critical (bite)
- name: Multiattack
- name: Power Attack
- name: Staggering Critical
- name: Stunning Critical
skills:
  Acrobatics: 28
    when jumping: 36
  Bluff: 43
  Diplomacy: 31
  Fly: 27
  Intimidate: 31
  Knowledge (arcana): 31
  Knowledge (planes): 31
  Knowledge (religion): 19
  Perception: 34
  Sense Motive: 30
  Spellcraft: 19
  Use Magic Device: 23
  _racial_mods:
    Acrobatics:
      when jumping: 8
    Bluff:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- armor training 4
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: standard
  treasure:
  - +5 half-plate
  - other treasure
special_abilities:
  Armor Training (Ex): An akvan is created wearing armor, and is naturally experienced
    in its use. An akvan possesses the armor training ability of a 15th-level fighter.
  Aura of Hopelessness (Su): All creatures except divs within 30 feet of an akvan
    must make a successful DC 30 Will save or take a -4 penalty on attack rolls, saving
    throws, skill checks, and ability checks. This is a mind-affecting effect. The
    save DC is Charisma-based.
  Create Ghul (Su): Any genie that is slain by an akvan becomes a ghul (see page 125)
    in 1d4 rounds. Such ghuls are under the command of the akvan that created them
    and remain enslaved until it dies, at which point they become free-willed ghuls.
    They do not possess any of the abilities they had in life.
  Shake Faith (Su): Anytime an akvan strikes a divine spellcaster with any of its
    melee attacks, the target must make a DC 30 Will save or be shaken for 1d4 rounds.
    If the save is successful, the target is instead shaken for 1 round. The save
    DC is Charisma-based.
  Torturous Gullet (Su): As hunters of otherworldly beings, akvans are uniquely drawn
    to digest creatures with a variety of resistances. In addition to the damage dealt
    by crushing internal organs, creatures swallowed by an akvan take 4d6 points of
    acid, cold, electricity, or fire damage per round. The akvan chooses what type
    of energy damage those in its stomach will take every round, and may change this
    from round to round. Additionally, an akvan's stomach is thickly armored, allowing
    it to benefit from its entire natural armor bonus instead of merely half.
desc_long: |-
  Akvans number among the most physically powerful and openly destructive servants of Ahriman, directly carrying out his ancient plans for oblivion. Their twisted minds bend toward desolation, ruin, and blasphemy, and their hatred of the gods of creation and beings renowned for inspiring art and wonder knows few equals. Whereas most divs turn their cruelty and vengefulness exclusively upon mortals, akvans broaden the scope of their hatred to encompass geniekind as well.

  Akvans seek out wonders to destroy-monuments from lost ages that have long inspired awe and pride or beings and establishments said to be invincible. While divs typically spread their taint through more subtle ways, akvans target symbols for destruction, bringing down not just stone and mortar but hopes and dreams. Additionally, these masters of destruction promote the creation of new horrors, transforming their most hated victims, genies, into nightmares known as ghuls. Thus, an akvan's evil does not end with its victim's death, as slain genies arise from the battlefield-or are belched up from an akvan's gullet-as blasphemous undead servants. These undead minions serve their terrifying master and, over the ages, gather around it as an army of profane slaves.

  Hatred and hunger for genies and those allied with them constitute the racial compulsion to which all akvans bow. These divs always go out of their way to hunt, destroy, and consume any genie they encounter. While wise enough to not waste their lives in combat against foes obviously more powerful then they, akvans seek to bring low any such opponents, if not by brute strength, then by guile.

  Akvans stand approximately 40 feet tall and weigh over 30,000 pounds.

---

# Div, Akvan
Ornate armor covers this hulking creature, rocky protrusions jutting from its hide and fierce horns crowning its broad head.
**Source** Bestiary 3 pg. 84
**XP** 307,200

NE Gargantuan outsider (div, evil, extraplanar)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +34
**Aura** hopelessness (30 ft., DC 30)

##### Defense

**AC** 38, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+13 armor, +4 Dex, +15 natural, –4 size)
**hp** 372 (24d10+240)
**Fort** +18, **Ref** +22, **Will** +21
**DR** 15/cold iron and good; **Immune** fire, poison; **Resist** acid 10, electricity 10; **SR** 31

##### Offense
**Speed** 50 ft., fly 120 ft. (good)
**Melee** bite +32 (2d8+12 plus grab/19–20), 2 claws +32 (2d6+12), tail slap +30 (2d10+6)
**Space** 20 ft., **Reach** 20 ft. (25 ft. with tail)
**Special Attacks** create _[[monsters/Ghul|ghul]]_, _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+18), shake faith, _[[universal monster rules/Swallow Whole|swallow whole]]_ (6d6+18 plus 4d6 energy damage, AC 25, 37 hp), torturous gullet, _[[universal monster rules/Trample|trample]]_ (2d8+18, DC 34)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +28)
Constant—_true seeing_
At will—_[[spells/Align Weapon|align weapon]]_, _[[spells/Detect Magic, Greater|detect magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 23)
3/day—_[[spells/Blasphemy|blasphemy]]_ (DC 25), _[[spells/Disintegrate|disintegrate]]_ (DC 24), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Forcecage|forcecage]]_ (DC 25), _[[spells/Protection from Energy|protection from energy]]_
1/day—geas/quest, _[[spells/Plane Shift|plane shift]]_, _[[universal monster rules/Summon|summon]]_ (level 6, 1d2 sepids 100%)

##### Statistics
**Str** 35, **Dex** 26, **Con** 30, **Int** 19, **Wis** 24, **Cha** 27
**Base Atk** +24; **CMB** +40; **CMD** 58
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** Acrobatics +28 (+36 when jumping), Bluff +43, Diplomacy +31, Fly +27, Intimidate +31, Knowledge (arcana) +31, Knowledge (planes) +31, Knowledge (religion) +19, Perception +34, Sense Motive +30, Spellcraft +19, Use Magic Device +23; **Racial Modifiers** +8 Acrobatics when jumping, +8 Bluff
**Languages** Abyssal, Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** armor _[[items/Weapon Magic Abilities/Training|training]]_ 4

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** standard (+5 _[[items/Armor/Half-plate|half-plate]]_, other treasure)

### Special Abilities

**Armor _Training_ (Ex)** An akvan is created wearing armor, and is naturally experienced in its use. An akvan possesses the armor _training_ ability of a 15th-level _[[classes/Fighter|fighter]]_.

**Aura of Hopelessness (Su)** All creatures except divs within 30 feet of an akvan must make a successful DC 30 Will save or take a –4 penalty on attack rolls, saving throws, skill checks, and ability checks. This is a mind-affecting effect. The save DC is Charisma-based.

**Create _Ghul_ (Su)** Any genie that is slain by an akvan becomes a _ghul_ (see page 125) in 1d4 rounds. Such ghuls are under the _[[spells/Command|command]]_ of the akvan that created them and remain enslaved until it dies, at which point they become free-willed ghuls. They do not possess any of the abilities they had in life.
**Shake Faith (Su) **Anytime an akvan strikes a divine spellcaster with any of its melee attacks, the target must make a DC 30 Will save or be _[[conditions/Shaken|shaken]]_ for 1d4 rounds. If the save is successful, the target is instead _shaken_ for 1 round. The save DC is Charisma-based.

**Torturous Gullet (Su)** As hunters of otherworldly beings, akvans are uniquely drawn to digest creatures with a variety of resistances. In addition to the damage dealt by crushing internal organs, creatures swallowed by an akvan take 4d6 points of acid, cold, electricity, or fire damage per round. The akvan chooses what type of energy damage those in its stomach will take every round, and may change this from round to round. Additionally, an akvan’s stomach is thickly armored, allowing it to benefit from its entire natural armor bonus instead of merely half.

##### Description

Akvans number among the most physically powerful and openly destructive servants of Ahriman, directly carrying out his ancient plans for _[[monsters/Oblivion|oblivion]]_. Their twisted minds bend toward desolation, ruin, and _blasphemy_, and their hatred of the gods of creation and beings renowned for inspiring art and wonder knows few equals. Whereas most divs turn their _[[feats/Cruelty|cruelty]]_ and vengefulness exclusively upon mortals, akvans broaden the scope of their hatred to encompass _[[spells/Geniekind|geniekind]]_ as well.

Akvans seek out wonders to destroy—monuments from lost ages that have long _[[items/Weapon Magic Abilities/Inspired|inspired]]_ awe and pride or beings and establishments said to be invincible. While divs typically spread their taint through more subtle ways, akvans target symbols for _[[spells/Destruction|destruction]]_, bringing down not just stone and mortar but hopes and dreams. Additionally, these masters of _destruction_ promote the creation of new horrors, transforming their most hated victims, genies, into nightmares known as ghuls. Thus, an akvan’s evil does not end with its victim’s death, as slain genies arise from the battlefield—or are belched up from an akvan’s gullet—as blasphemous undead servants. These undead minions serve their terrifying master and, over the ages, gather around it as an army of profane slaves.

Hatred and hunger for genies and those allied with them constitute the racial compulsion to which all akvans bow. These divs always go out of their way to hunt, destroy, and consume any genie they encounter. While wise enough to not waste their lives in combat against foes obviously more powerful then they, akvans seek to bring low any such opponents, if not by brute strength, then by guile.

Akvans stand approximately 40 feet tall and weigh over 30,000 pounds.