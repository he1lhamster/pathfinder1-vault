---
cssclass: [monsters]
title1: Ahriman, Lord of All Divs
desc_short: This humanoid creature has the head of a ravening, horned lion. A chorus
  of anguished screams echoes from his gaping maw.
title2: Ahriman, Lord of All Divs
CR: 26
sources:
- name: Mythic Realms
  page: 48
  link: http://paizo.com/products/btpy90q7?Pathfinder-Campaign-Setting-Mythic-Realms
- name: 'Pathfinder #24: The Final Wish'
  page: 76
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy89a2
XP: 2457600
alignment: NE
size: Huge
type: outsider
subtypes:
- div
- evil
- extraplanar
initiative:
  bonus: 20
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: hopelessness
  radius: 30
  DC: 38
- name: frightful presence
  radius: 60
  DC: 38
AC:
  AC: 46
  touch: 21
  flat_footed: 37
  components:
    dex: 8
    dodge: 1
    natural: 15
    profane: 14
    size: -2
HP:
  HP: 610
  long: 33d10+429
  regeneration: 20
  regeneration_weakness: mythic and epic or good
saves:
  fort: 24
  ref: 26
  will: 25
defensive_abilities:
- freeing chains
- skin of serpents
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage and drain
- charm and compulsion effects
- death effects
- energy drain
- fire
- petrification
- poison
resistances:
  acid: 30
  electricity: 30
SR: 37 (41 vs. good)
speeds:
  base: 40
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: Ahriman's scourge +47/+42/+37/+32 (3d6+16/19-20/×3)
      entries:
      - - damage: 3d6+16
          crit_range: 19-20
          crit_multiplier: 3
      attack: Ahriman's scourge
      bonus:
      - 47
      - 42
      - 37
      - 32
    - text: bite +45 (3d6+8/19-20 plus grab and bottomless maw)
      entries:
      - - damage: 3d6+8
          crit_range: 19-20
        - effect: grab
        - effect: bottomless maw
      attack: bite
      bonus:
      - 45
    - text: claw +45 (1d8+8)
      entries:
      - - damage: 1d8+8
      attack: claw
      bonus:
      - 45
    - text: gore +45 (2d6+8 plus crown of fourfold curses)
      entries:
      - - damage: 2d6+8
        - effect: crown of fourfold curses
      attack: gore
      bonus:
      - 45
    - text: 2 talons +45 (1d8+8)
      entries:
      - - damage: 1d8+8
      count: 2
      attack: talons
      bonus:
      - 45
  special:
  - bleed (2d6)
  - bottomless maw
  - consume essence
  - pounce
  - rend (2 claws, 1d8+24)
  - shake faith
  - symbolic prison
space: 15
reach: 10
reach_other: 15 ft. with Ahriman's scourge
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
  - name: speak with dead
    source: default
    freq: At will
    DC: 25
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 26
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 30
  - name: implosion
    source: default
    freq: 3/day
    DC: 31
  - name: maze
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    DC: 29
  - name: summon
    source: default
    freq: 3/day
    level: 9
    summons:
    - name: see below
  - name: wish
    source: default
    freq: 3/day
  - name: demand
    source: default
    freq: 1/day
    DC: 30
  - name: symbol of fear
    source: default
    freq: 1/day
    DC: 28
  - name: symbol of persuasion
    source: default
    freq: 1/day
    DC: 28
  - name: symbol of stunning
    source: default
    freq: 1/day
    DC: 29
  - name: symbol of weakness
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 20
    concentration: 32
ability_scores:
  STR: 43
  DEX: 26
  CON: 36
  INT: 19
  WIS: 24
  CHA: 35
BAB: 33
CMB: 51
CMB_other: +53 bull rush, +55 grapple
CMD: 74
CMD_other: 76 vs. bull rush
feats:
- name: Awesome Blow
- name: Bleeding Critical
- name: Cleave
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Improved Bull Rush
- name: Improved Critical (Ahriman's scourge)
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Natural Attack (bite)
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Multiattack
- name: Power Attack
skills:
  Bluff: 48
  Diplomacy: 48
  Fly: 12
  Intimidate: 48
  Knowledge (arcana): 32
  Knowledge (religion): 32
  Knowledge (engineering): 14
  Knowledge (history): 14
  Knowledge (nature): 14
  Knowledge (planes): 40
  Linguistics: 9
  Perception: 43
  Sense Motive: 43
  Spellcraft: 37
  Stealth: 17
languages:
- Abyssal
- Aquan
- Auran
- Celestial
- Common
- Draconic
- Ignan
- Infernal
- Terran
- telepathy 300 ft.
special_qualities:
- Ahriman's scourge
- Lord of All Divs
- slaughtered slave
special_abilities:
  Ahriman's Scourge (Su): Ahriman's Huge scourge is made from the spines of genies.
    It deals 3d6 points of damage, and gains the bane weapon special ability when
    used it to attack a genie. The scourge only functions for Ahriman. If his scourge
    is lost or destroyed, Ahriman can magically create a new one from the skeletons
    of four genies.
  Aura of Hopelessness (Su): Any creature that comes within 30 feet of Ahriman must
    succeed at a DC 38 Will save or take a -4 penalty on attack rolls, saving throws,
    skill checks, and ability checks. The save DC is Charisma-based.
  Bottomless Maw (Su): |-
    When Ahriman bites a creature and successfully grabs it, he magically banishes the creature to an extraplanar bottomless pit. Ahriman can't swallow a creature that has the good subtype or is affected by holy aura.

    A swallowed creature takes 2d8+12 points of sonic damage each round as it plummets endlessly through Ahriman's cacophonous interior-a repulsive, lightless pit where heresies and praises to Ahriman are screamed in all languages at once. The creature must also succeed at a DC 39 Will save each round or be dominated, as dominate monster, for 1 day. Ahriman knows when a creature becomes dominated, and can expel any creature as a move action, causing it to appear in any adjacent square. The save DC is Constitution-based.

    A swallowed creature can't cut its way out. Any creature in the area of silence or a similar affect is unaffected by the sonic damage and domination. A swallowed creature can escape by using plane shift or similar magic. The Lord of All Divs is stunned for 1 round and forced to expel all creatures in his stomach if a creature in his stomach casts holy aura or summons a creature with the good subtype, or if a creature either inside or out of his stomach casts atonement, freedom, holy word, limited wish, miracle, or wish.
  Consume Essence (Su): Ahriman's soul-rending savagery erodes the fundamental essence
    of his victims. When he confirms a critical hit with a natural weapon, the target
    takes 1d6 points of ability drain to a random ability score (Fortitude DC 39 half).
    The save DC is Constitution-based.
  Crown of Fourfold Curses (Su): The ancient curses graven on the horns crowning Ahriman's
    head grant him a +14 profane bonus to AC and a +4 profane bonus to spell resistance
    against spells or spell-like abilities with the good descriptor or those cast
    by good creatures. If Ahriman confirms a critical hit with his gore attack, the
    target is stricken with bestow curse (DC 36). The save DC is Charisma-based.
  Freeing Chains (Su): Multiple chains wrap around Ahriman's body, and three select
    links can free him if he's bound. Ahriman can break one of these links to gain
    the benefits of freedom. He can do this as an immediate action to negate an applicable
    effect being cast on him.
  Lord of All Divs: Ahriman gains a suite of traits as Lord of the Divs. Regeneration
    (Ex) Only epic and good damage, good damage from a mythic source, or damage from
    a creature of equal or greater power (such as an archdevil, deity, or demon lord)
    interrupts Ahriman's regeneration.Immunity to ability damage and drain, charm
    and compulsion effects, death effects, energy drain, and petrification.Resistance
    to acid 30 and electricity 30.Resurrection (Ex) Ahriman's power is rooted in his
    domain in Abaddon. If he is slain, his body collapses into a mass of writhing
    snakes and is restored to life (as true resurrection) at the foot of his mountain.
    Once this occurs, Ahriman can't use this ability until a full year has passed;
    if slain again before that time, he is forever destroyed.Frightful Presence (Su)
    Ahriman can activate his frightful presence as a free action as part of any attack,
    spell-like ability, special attack, or by speaking aloud.Summon Divs (Sp) Three
    times per day as a swift action, Ahriman can summon any div or combination of
    divs whose total combined CR is 20 or lower, or summon a unique div of his choice.
    This otherwise works like the summon universal monster rule, with a 100% chance
    of success, and counts as a 9th-level spell effect.Telepathy 300 feet.Ahriman's
    natural weapons and any weapons he wields are treated as epic and evil for the
    purpose of overcoming damage reduction.Ahriman can grant spells to his worshipers
    as if he were a deity. His domains are Darkness, Death, Destruction, and Evil.
    His favored weapon is the whip.
  Shake Faith (Su): When Ahriman strikes a divine spellcaster with a melee attack,
    the target is shaken for 1d4 rounds (Will DC 38 reduces the duration to 1 round).
    On a critical hit, the target is frightened instead of shaken for the same duration.
    The save DC is Charisma-based.
  Skin of Serpents (Su): Ahriman's flesh writhes with countless vipers, embodiments
    of ancient and forgotten evils. Any creature striking Ahriman in melee (unless
    using a reach weapon) must succeed at a DC 38 Fortitude save or take 1d6 points
    of Strength drain. The save DC is Charismabased. If the creature fails its save,
    Ahriman gains 5 temporary hit points.
  Slaughtered Slave (Su): Any humanoid slain by Ahriman becomes a cairn wight (or
    brute wight if it was a giant) in 1d4 rounds. A genie killed by Ahriman instead
    rises as a ghul in 1d4 rounds. The creature is enslaved to Ahriman's will and
    loses all abilities and memories it had in life.
  Symbolic Prison (Su): When Ahriman entraps a creature in his bottomless maw or in
    a maze spell, he can use one of his symbol spell-like abilities as a swift action.
    The symbol affects all creatures within the prison, and ends when all creatures
    have escaped the maw or maze.
desc_long: Ahriman sprang from the darkest shadows of the elements at the birth of
  the genie races. Though he towers nearly 20 feet tall and weighs 7,000 pounds, Ahriman
  moves with uncanny swiftness. Ahriman's rampages leave legions of undead in his
  wake that, alongside nihilistic Usij cultists, tear down life, culture, and civilization.
  To the Lord of All Divs, suffering and pain are meat and drink, corruption and murder
  useful tools, and the end of all things the only worthwhile goal.

---

# Ahriman, Lord of All Divs
This humanoid creature has the head of a ravening, horned _[[monsters/Lion|lion]]_. A chorus of anguished screams echoes from his gaping maw.
**Source** Mythic Realms pg. 48, Pathfinder #24: The Final _[[spells/Wish|Wish]]_ pg. 76
**XP** 2,457,600

NE Huge outsider (div, evil, extraplanar)
**Init** +20; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +43
**Aura** hopelessness (30 ft., DC 38), _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 38)

##### Defense

**AC** 46, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+8 Dex, +1 dodge, +15 natural, +14 profane, –2 size)
**hp** 610 (33d10+429); _[[universal monster rules/Regeneration|regeneration]]_ 20 (mythic and epic or good)
**Fort** +24, **Ref** +26, **Will** +25
**Defensive Abilities** freeing chains, skin of serpents; **DR** 20/cold iron, epic, and good; **Immune** _[[universal monster rules/Ability Damage and Drain|ability damage and drain]]_, charm and compulsion effects, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, fire, petrification, poison; **Resist** acid 30, electricity 30; **SR** 37 (41 vs. good)

##### Offense
**Speed** 40 ft., fly 60 ft. (perfect)
**Melee** Ahriman’s scourge +47/+42/+37/+32 (3d6+16/19–20/×3), bite +45 (3d6+8/19–20 plus _[[universal monster rules/Grab|grab]]_ and bottomless maw), claw +45 (1d8+8), gore +45 (2d6+8 plus crown of fourfold curses), 2 talons +45 (1d8+8)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with Ahriman’s scourge)
**Special Attacks** _[[universal monster rules/Bleed|bleed]]_ (2d6), bottomless maw, _[[feats/Consume Essence|consume essence]]_, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rend|rend]]_ (2 claws, 1d8+24), shake faith, symbolic prison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +32)
Constant—_[[spells/Arcane Sight|arcane sight]]_, _true seeing_
At will—greater teleport, _[[spells/Speak with Dead|speak with dead]]_ (DC 25), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 26)
3/day—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 30), _[[spells/Implosion|implosion]]_ (DC 31), _[[spells/Maze|maze]]_, _[[spells/Plane Shift|plane shift]]_ (DC 29), _[[universal monster rules/Summon|summon]]_ (level 9, see below), _wish_
1/day—_[[spells/Demand|demand]]_ (DC 30), _[[spells/Symbol of Fear|symbol of fear]]_ (DC 28), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 28), _[[spells/Symbol of Stunning|symbol of stunning]]_ (DC 29), _[[spells/Symbol Of Weakness|symbol of weakness]]_ (DC 29)

##### Statistics
**Str** 43, **Dex** 26, **Con** 36, **Int** 19, **Wis** 24, **Cha** 35
**Base Atk** +33; **CMB** +51 (+53 bull rush, +55 grapple); **CMD** 74 (76 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (Ahriman’s scourge), _Improved Critical_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (bite), _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +48, Diplomacy +48, Fly +12, Intimidate +48, Knowledge (arcana, religion) +32, Knowledge (engineering, history, nature) +14, Knowledge (planes) +40, Linguistics +9, Perception +43, Sense Motive +43, Spellcraft +37, Stealth +17
**Languages** Abyssal, Aquan, Auran, Celestial, Common, Draconic, Ignan, Infernal, Terran; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** Ahriman’s scourge, Lord of All Divs, slaughtered _[[items/Mundane/Slave|slave]]_

### Special Abilities

**Ahriman’s Scourge (Su)** Ahriman’s Huge scourge is made from the spines of genies. It deals 3d6 points of damage, and gains the _[[spells/Bane|bane]]_ weapon special ability when used it to attack a genie. The scourge only functions for Ahriman. If his scourge is lost or destroyed, Ahriman can magically create a new one from the skeletons of four genies.

**Aura of Hopelessness (Su)** Any creature that comes within 30 feet of Ahriman must succeed at a DC 38 Will save or take a –4 penalty on attack rolls, saving throws, skill checks, and ability checks. The save DC is Charisma-based.

**Bottomless Maw (Su)** When Ahriman bites a creature and successfully grabs it, he magically banishes the creature to an extraplanar bottomless pit. Ahriman can’t swallow a creature that has the good subtype or is affected by _[[spells/Holy Aura|holy aura]]_.

A swallowed creature takes 2d8+12 points of sonic damage each round as it plummets endlessly through Ahriman’s cacophonous interior—a repulsive, lightless pit where heresies and praises to Ahriman are screamed in all languages at once. The creature must also succeed at a DC 39 Will save each round or be dominated, as _[[spells/Dominate Monster|dominate monster]]_, for 1 day. Ahriman knows when a creature becomes dominated, and can expel any creature as a move action, causing it to appear in any adjacent square. The save DC is Constitution-based.

A swallowed creature can’t cut its way out. Any creature in the area of _[[spells/Silence|silence]]_ or a similar affect is unaffected by the sonic damage and domination. A swallowed creature can escape by using _plane shift_ or similar magic. The Lord of All Divs is _[[conditions/Stunned|stunned]]_ for 1 round and forced to expel all creatures in his stomach if a creature in his stomach casts _holy aura_ or summons a creature with the good subtype, or if a creature either inside or out of his stomach casts _[[spells/Atonement|atonement]]_, _[[spells/Freedom|freedom]]_, _[[spells/Holy Word|holy word]]_, _[[spells/Limited Wish|limited wish]]_, _[[spells/Miracle|miracle]]_, or _wish_.

**_Consume Essence_ (Su)** Ahriman’s soul-rending savagery erodes the fundamental essence of his victims. When he confirms a critical hit with a natural weapon, the target takes 1d6 points of ability drain to a random ability score (Fortitude DC 39 half). The save DC is Constitution-based.

**Crown of Fourfold Curses (Su)** The ancient curses graven on the horns crowning Ahriman’s head grant him a +14 profane bonus to AC and a +4 profane bonus to _[[universal monster rules/Spell Resistance|spell resistance]]_ against spells or _spell-like abilities_ with the good descriptor or those cast by good creatures. If Ahriman confirms a critical hit with his gore attack, the target is stricken with _[[spells/Bestow Curse|bestow curse]]_ (DC 36). The save DC is Charisma-based.

**Freeing Chains (Su)** Multiple chains wrap around Ahriman’s body, and three select links can free him if he’s bound. Ahriman can break one of these links to gain the benefits of _freedom_. He can do this as an immediate action to negate an applicable effect being cast on him.

**Lord of All Divs** Ahriman gains a suite of traits as Lord of the Divs.

* _Regeneration_ (Ex) Only epic and good damage, good damage from a mythic source, or damage from a creature of equal or greater power (such as an archdevil, deity, or demon lord) interrupts Ahriman’s _regeneration_.
* _[[universal monster rules/Immunity|Immunity]]_ to _ability damage and drain_, charm and compulsion effects, death effects, _energy drain_, and petrification.
* _[[universal monster rules/Resistance|Resistance]]_ to acid 30 and electricity 30.
* _[[spells/Resurrection|Resurrection]]_ (Ex) Ahriman’s power is rooted in his domain in Abaddon. If he is slain, his body collapses into a mass of writhing snakes and is restored to life (as _[[spells/True Resurrection|true resurrection]]_) at the foot of his mountain. Once this occurs, Ahriman can’t use this ability until a full year has passed; if slain again before that time, he is forever destroyed.
* _Frightful Presence_ (Su) Ahriman can activate his _frightful presence_ as a free action as part of any attack, spell-like ability, special attack, or by speaking aloud.
* _Summon_ Divs (Sp) Three times per day as a swift action, Ahriman can _summon_ any div or combination of divs whose total combined CR is 20 or lower, or _summon_ a unique div of his choice. This otherwise works like the _summon_ universal monster rule, with a 100% chance of success, and counts as a 9th-level spell effect.
* _Telepathy_ 300 feet.
* Ahriman’s natural weapons and any weapons he wields are treated as epic and evil for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.
* Ahriman can grant spells to his worshipers as if he were a deity. His domains are _[[spells/Darkness|Darkness]]_, Death, _[[spells/Destruction|Destruction]]_, and Evil. His favored weapon is the _[[items/Weapon/Whip|whip]]_.
**Shake Faith (Su)** When Ahriman strikes a divine spellcaster with a melee attack, the target is _[[conditions/Shaken|shaken]]_ for 1d4 rounds (Will DC 38 reduces the duration to 1 round). On a critical hit, the target is _[[conditions/Frightened|frightened]]_ instead of _shaken_ for the same duration. The save DC is Charisma-based.
**Skin of Serpents (Su)** Ahriman’s flesh writhes with countless vipers, embodiments of ancient and forgotten evils. Any creature striking Ahriman in melee (unless using a reach weapon) must succeed at a DC 38 Fortitude save or take 1d6 points of Strength drain. The save DC is Charismabased. If the creature fails its save, Ahriman gains 5 temporary hit points.
**Slaughtered _Slave_ (Su)** Any humanoid slain by Ahriman becomes a cairn _[[monsters/Wight|wight]]_ (or brute _wight_ if it was a giant) in 1d4 rounds. A genie killed by Ahriman instead rises as a _[[monsters/Ghul|ghul]]_ in 1d4 rounds. The creature is enslaved to Ahriman’s will and loses all abilities and memories it had in life.
**Symbolic Prison (Su)** When Ahriman entraps a creature in his bottomless maw or in a _maze_ spell, he can use one of his symbol _spell-like abilities_ as a swift action. The symbol affects all creatures within the prison, and ends when all creatures have escaped the maw or _maze_.

##### Description

Ahriman sprang from the darkest shadows of the elements at the birth of the genie races. Though he towers nearly 20 feet tall and weighs 7,000 pounds, Ahriman moves with uncanny swiftness. Ahriman’s rampages leave legions of undead in his wake that, alongside nihilistic Usij cultists, tear down life, culture, and civilization. To the Lord of All Divs, suffering and pain are meat and drink, corruption and murder useful tools, and the end of all things the only worthwhile goal.