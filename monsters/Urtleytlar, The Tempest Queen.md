---
cssclass: [monsters]
title1: Urtleytlar, The Tempest Queen
desc_short: This writhing terror is made of tentacles and the heads of multiple hounds.
  The figure of a beautiful woman extends from the monster's center, though its fiendish
  visage is far from welcoming.
title2: Urtleytlar, The Tempest Queen
CR: 20
sources:
- name: "Pathfinder #60: From Hell's Heart"
  page: 68
  link: http://paizo.com/pathfinder/adventurePath/skullAndShackles/v5748btpy8moi
XP: 307200
race: Female
classes:
- scylla cleric of Rovagug 8
alignment: CE
size: Huge
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 14
senses:
  all-around vision: true
  blindsight: 30
  darkvision: 60
  low-light vision: true
  see invisibility: true
auras:
- name: frightful presence
  radius: 30
  DC: 27
AC:
  AC: 38
  touch: 28
  flat_footed: 23
  components:
    deflection: 5
    dex: 14
    dodge: 1
    natural: 10
    size: -2
HP:
  HP: 406
  long: 20d8+8d8+280
  HD: 28
  fast_healing: 10
saves:
  fort: 22
  ref: 22
  will: 27
defensive_abilities:
- freedom of movement
- improved evasion
DR:
- amount: 10
  weakness: cold iron and lawful
immunities:
- charm effects
- cold
- confusion and insanity effects
resistances:
  acid: 20
  fire: 20
SR: 31
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
  swim: 50
attacks:
  melee:
  - - text: 3 bites +37 (1d8+12/19-20 plus bleed)
      entries:
      - - damage: 1d8+12
          crit_range: 19-20
        - effect: bleed
      count: 3
      attack: bites
      bonus:
      - 37
    - text: 4 tentacles +35 (1d6+6 plus grab)
      entries:
      - - damage: 1d6+6
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 35
  special:
  - bleed (1d6)
  - channel negative energy 10/day (DC 21, 4d6)
  - constrict (1d6+10)
  - deadly weather (8 rounds/day)
  - gale aura (8 rounds/day)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: nondetection
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: acid arrow
    source: default
    freq: At will
  - name: control water
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 20
  - name: black tentacles
    source: default
    freq: 3/day
  - name: charm monster
    source: default
    freq: 3/day
    DC: 21
  - name: insanity
    source: default
    freq: 3/day
    DC: 24
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 22
  - name: solid fog
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
  - name: power word stun
    source: default
    freq: 1/day
  - name: project image
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: charybdis
      amount: 1
      chance: 100%
  sources:
  - name: default
    CL: 16
    concentration: 23
spells:
  entries:
  - name: cure critical wounds
    source: Cleric
    level: 4
    DC: 23
  - name: divine power
    source: Cleric
    level: 4
  - name: inflict critical wounds
    source: Cleric
    level: 4
    DC: 23
  - name: tongues
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 23
  - name: call lightning
    source: Cleric
    level: 3
    DC: 22
  - name: cure serious wounds
    source: Cleric
    level: 3
    DC: 22
    count: 2
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: magic circle against good
    source: Cleric
    level: 3
  - name: water breathing
    source: Cleric
    level: 3
  - name: darkness
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 21
  - name: gust of wind
    source: Cleric
    level: 2
    DC: 21
  - name: shatter
    source: Cleric
    level: 2
    count: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    DC: 20
  - name: command
    source: Cleric
    level: 1
    DC: 20
    count: 2
  - name: divine favor
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: true strike
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 19
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 8
    concentration: 17
    slots:
      0: at-will
    domains:
    - destruction (catastrophe subdomain)
    - weather (storms subdomain)
ability_scores:
  STR: 35
  DEX: 38
  CON: 31
  INT: 18
  WIS: 29
  CHA: 24
BAB: 21
CMB: 35
CMB_other: +39 grapple
CMD: 65
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Improved Critical (bite)
- name: Mobility
- name: Multiattack
- name: Power Attack
- name: Selective Channeling
- name: Staggering Critical
- name: Stunning Critical
- name: Vital Strike
- name: Weapon Finesse
- name: Weapon Focus (bite)
- name: Weapon Focus (tentacle)
skills:
  Acrobatics: 35
  Bluff: 25
  Fly: 35
  Knowledge (nature): 22
  Knowledge (planes): 25
  Perception: 34
  Sense Motive: 30
  Spellcraft: 31
  Stealth: 27
  Swim: 45
  Use Magic Device: 29
languages:
- Aboleth
- Abyssal
- Aklo
- Aquan
- Common
special_qualities:
- amphibious
- aura
- change shape (1 humanoid form; alter self)
- undersized weapons
gear:
  gear:
  - amulet of mighty fists +3
  - belt of physical perfection +4
  - ring of protection +5
desc_long: |-
  An awakened horror shaken from the depths of the sea by the catastrophic calling of Earthfall, the beast known as Urtleytlar swims the Arcadian Ocean, wreaking havoc wherever she treads. Urtleytlar is one of the Lesser Spawn of Rovagug, having escaped the Rough Beast's prison deep beneath the earth like those before her. The drow of Sekamina tell legends of a terrible many-headed beast crawling from the depths of the Dying Sea to prey upon their coastal settlements, and scholars among the dark elves hypothesize that this beast may have originated from somewhere in Orv. In this instance, their legends hold true, for Urtleytlar indeed swam the lightless depths of the Sightless Sea for centuries until she made it up the Braid, raided the aboleth population guarding the Inverted Sea, and emerged into a broken Azlant already claimed by the Arcadian Ocean.

  Urtleytlar spent her first millennia on Golarion's surface terrorizing the eastern coasts of Arcadia, after which the foul beast felt an irresistible call to the lands of the east. The world rippled with destruction after the passing of Aroden, and this surge of chaos washed over Urtleytlar as she felt the pull of her lord Rovagug in the Inner Sea region. She swam eastward, weaving through the shattered continent of Azlant, and as she headed toward the Eye of Abendego, she saw the storm as a manifestation of the Rough Beast's destructive power. The monstrous scylla delights in the powerful storm, and preaches Rovagug's words of destruction through the ruin she sows.

  Since making the Abendego Gulf her home, Urtleytlar has gathered numerous evil aquatic humanoids (and even depraved sailors) to her wretched bosom. The boggards and skum that make up the greatest number of her minions extend her reach to the broken shores of the Sodden Lands and Shackles. Some say she guides foolish sailors hoping to sail into the hurricane, providing them temporary safety in exchange for a taste of their souls.

  A handful of boggard tribes swear fealty to the Tempest Queen by capturing slaves and dragging them to the shores as sacrifices. Urtleytlar makes choice selections from among her minions' offerings, leaving the scraps for the boggards themselves to enjoy. Though she doesn't need the froglike humanoids for her conquests, she nonetheless enjoys their adoration. In addition to these minions, she counts a number of skum armies-left masterless after their abandonment by their aboleth rulers-as her thralls. Beneath the howling winds of the Eye of Abendego, hundreds of skum dwell in the ruins of Lirgen, now sunken beneath the sea. From this base, they make deals with both boggards and humans who have managed to survive in the f looded wastes of the Sodden Lands. These tribes and gangs provide Urtleytlar with slaves and food, and she strengthens their reach by aiding them in their destructive endeavors. In addition to these humanoids, Urtleytlar uses Megrexti, her charybdis counterpart and favorite plaything, as a living weapon, sending it into the middle of f leets of ships or other attackers and laughing in delight as it tears her victims to pieces.

  Urtleytlar chose as her alternate form a strangely beautiful Cyclops woman. As old a creature as she is, perhaps Urtleytlar feels a kinship with the giants who once ruled the land and waters she now calls home. Regardless, her alternate form has tricked many explorers searching for the ruins of Ghol-Gan, easing them into an odd complacency before she utterly destroys them and their crews.

---

# Urtleytlar, The Tempest Queen
This writhing terror is made of tentacles and the heads of multiple hounds. The figure of a beautiful woman extends from the monster’s center, though its fiendish visage is far from welcoming.


**Source** Pathfinder #60: From Hell's Heart pg. 68
**XP** 307,200
Female _[[monsters/Scylla|scylla]]_ _[[classes/Cleric|cleric]]_ of Rovagug 8
CE Huge aberration (aquatic)
**Init** +14; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +34

**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 27)

##### Defense

**AC** 38, touch 28, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+5 deflection, +14 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural, –2 size)

**hp** 406 (28 HD; 20d8+8d8+280); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +22, **Ref** +22, **Will** +27
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, improved evasion; **DR** 10/cold iron and lawful; **Immune** charm effects, cold, _[[spells/Confusion|confusion]]_ and _[[spells/Insanity|insanity]]_ effects; **Resist** acid 20, fire 20; **SR** 31

##### Offense
**Speed** 30 ft., fly 60 ft. (good), swim 50 ft.
**Melee** 3 bites +37 (1d8+12/19–20 plus _[[universal monster rules/Bleed|bleed]]_), 4 tentacles +35 (1d6+6 plus _[[universal monster rules/Grab|grab]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _bleed_ (1d6), channel negative energy 10/day (DC 21, 4d6), _[[universal monster rules/Constrict|constrict]]_ (1d6+10), _[[items/Weapon Magic Abilities/Deadly|deadly]]_ weather (8 rounds/day), gale aura (8 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
Constant—fly, _freedom of movement_, _[[spells/Nondetection|nondetection]]_, _see invisibility_
At will—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Control Water|control water]]_, _[[spells/Fog Cloud|fog cloud]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Major Image|major image]]_ (DC 20)
3/day—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Charm Monster|charm monster]]_ (DC 21), _insanity_ (DC 24), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 22), _[[spells/Solid Fog|solid fog]]_
1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Project Image|project image]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 8, 1 _[[monsters/Charybdis|charybdis]]_ 100%)
**_Cleric_ Spells Prepared** (CL 8th; concentration +17)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (DC 23), _[[spells/Divine Power|divine power]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 23), _[[spells/Tongues|tongues]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 23)
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 22), _[[spells/Cure Serious Wounds|cure serious wounds]]_ (DC 22, 2), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Darkness|darkness]]_, _[[spells/Death Knell|death knell]]_ (DC 21), _[[spells/Gust Of Wind|gust of wind]]_ (DC 21), _[[spells/Shatter|shatter]]_ (2), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 20), _[[spells/Command|command]]_ (DC 20, 2), _[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_bleed_ (DC 19), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Virtue|virtue]]_
**D** Domain spell; **Domains** _[[spells/Destruction|Destruction]]_ (Catastrophe subdomain), Weather (Storms subdomain)

##### Statistics
**Str** 35, **Dex** 38, **Con** 31, **Int** 18, **Wis** 29, **Cha** 24
**Base Atk** +21; **CMB** +35 (+39 grapple); **CMD** 65
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (tentacle)
**Skills** Acrobatics +35, Bluff +25, Fly +35, Knowledge (nature) +22, Knowledge (planes) +25, Perception +34, Sense Motive +30, Spellcraft +31, Stealth +27, Swim +45, Use Magic Device +29
**Languages** Aboleth, Abyssal, Aklo, Aquan, Common
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, aura, _[[universal monster rules/Change Shape|change shape]]_ (1 humanoid form; _[[spells/Alter Self|alter self]]_), _[[universal monster rules/Undersized Weapons|undersized weapons]]_

**Gear** _[[items/Wondrous Item/Amulet of Mighty Fists +3|amulet of mighty fists +3]]_, _[[items/Wondrous Item/Belt of Physical Perfection +4|belt of physical perfection +4]]_, _[[items/Ring/Ring of Protection +5|ring of protection +5]]_

##### Description

An awakened horror _[[conditions/Shaken|shaken]]_ from the depths of the sea by the catastrophic calling of Earthfall, the beast known as Urtleytlar swims the Arcadian Ocean, wreaking havoc wherever she treads. Urtleytlar is one of the Lesser Spawn of Rovagug, having escaped the Rough Beast’s prison deep beneath the earth like those before her. The _[[monsters/Drow|drow]]_ of Sekamina tell legends of a terrible many-headed beast crawling from the depths of the _[[conditions/Dying|Dying]]_ Sea to prey upon their coastal settlements, and scholars among the dark elves hypothesize that this beast may have originated from somewhere in Orv. In this instance, their legends hold true, for Urtleytlar indeed swam the lightless depths of the Sightless Sea for centuries until she made it up the Braid, raided the aboleth population _[[items/Armor Magic Abilities/Guarding|guarding]]_ the Inverted Sea, and emerged into a _[[conditions/Broken|broken]]_ Azlant already claimed by the Arcadian Ocean.

Urtleytlar spent her first millennia on Golarion’s surface terrorizing the eastern coasts of Arcadia, after which the foul beast felt an irresistible call to the lands of the east. The world rippled with _destruction_ after the passing of Aroden, and this surge of chaos washed over Urtleytlar as she felt the _[[universal monster rules/Pull|pull]]_ of her lord Rovagug in the Inner Sea region. She swam eastward, weaving through the shattered continent of Azlant, and as she headed toward the Eye of Abendego, she _[[items/Mundane/Saw|saw]]_ the storm as a manifestation of the Rough Beast’s destructive power. The monstrous _scylla_ delights in the powerful storm, and preaches Rovagug’s words of _destruction_ through the ruin she sows.

Since making the Abendego Gulf her home, Urtleytlar has gathered numerous evil aquatic humanoids (and even depraved sailors) to her wretched bosom. The boggards and _[[monsters/Skum|skum]]_ that make up the greatest number of her minions extend her reach to the _broken_ shores of the Sodden Lands and Shackles. Some say she guides foolish sailors hoping to sail into the hurricane, providing them temporary safety in exchange for a taste of their souls.

A handful of _[[monsters/Boggard|boggard]]_ tribes swear fealty to the Tempest Queen by capturing slaves and dragging them to the shores as sacrifices. Urtleytlar makes choice selections from among her minions’ offerings, leaving the scraps for the boggards themselves to enjoy. Though she doesn’t need the froglike humanoids for her conquests, she nonetheless enjoys their _[[spells/Adoration|adoration]]_. In addition to these minions, she counts a number of _skum_ armies—left masterless after their abandonment by their aboleth rulers—as her thralls. Beneath the howling winds of the Eye of Abendego, hundreds of _skum_ dwell in the ruins of Lirgen, now sunken beneath the sea. From this base, they make deals with both boggards and humans who have managed to survive in the f looded wastes of the Sodden Lands. These tribes and gangs provide Urtleytlar with slaves and food, and she strengthens their reach by aiding them in their destructive endeavors. In addition to these humanoids, Urtleytlar uses Megrexti, her _charybdis_ counterpart and favorite plaything, as a living weapon, _[[spells/Sending|sending]]_ it into the middle of f leets of ships or other attackers and laughing in delight as it tears her victims to pieces.

Urtleytlar chose as her alternate form a strangely beautiful _[[monsters/Cyclops|Cyclops]]_ woman. As old a creature as she is, perhaps Urtleytlar feels a kinship with the giants who once ruled the land and waters she now calls home. Regardless, her alternate form has tricked many explorers searching for the ruins of Ghol-Gan, easing them into an odd complacency before she utterly destroys them and their crews.