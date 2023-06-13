---
cssclass: [monsters]
title1: Qlippoth, Iathavos
desc_short: This immense creature has four bat-like wings and a spherical body. Red
  eyes peer from all sides, and two huge claws dangle below.
title2: Iathavos
CR: 20
sources:
- name: Bestiary 2
  page: 222
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: CE
size: Colossal
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
- qlippoth
initiative:
  bonus: -1
senses:
  all-around vision: true
  darkvision: 60
  low-light vision: true
auras:
- name: stench
  DC: 32
  duration: 10 rounds
- name: cloak of chaos
  DC: 26
AC:
  AC: 37
  touch: 7
  flat_footed: 37
  components:
    deflection: 4
    dex: -1
    insight: 2
    natural: 30
    size: -8
HP:
  HP: 372
  long: 24d10+240
  fast_healing: 15
saves:
  fort: 28
  ref: 15
  will: 28
defensive_abilities:
- ichor
- never surprised or flat-footed
DR:
- amount: 15
  weakness: cold iron and lawful
immunities:
- cold
- poison
- mind-affecting effects
resistances:
  acid: 30
  electricity: 10
  fire: 10
SR: 31
speeds:
  base: 20
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +31 (4d6+15/19-20 plus grab)
      entries:
      - - damage: 4d6+15
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 31
    - text: 4 wings +26 (2d8+7)
      entries:
      - - damage: 2d8+7
      count: 4
      attack: wings
      bonus:
      - 26
  special:
  - abyssal transformation
  - entropic beams
  - horrific appearance (DC 30)
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 26
  - name: foresight
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
  - name: dispel law
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: magic missile
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 25
  - name: wind walk
    source: default
    freq: At will
  - name: word of recall
    source: default
    freq: At will
  - name: black tentacles
    source: default
    freq: 3/day
  - name: dimensional lock
    source: default
    freq: 3/day
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 26
  - name: insanity
    source: default
    freq: 3/day
    DC: 25
  - name: word of chaos
    source: default
    freq: 3/day
    DC: 25
  - name: quickened heal
    source: default
    freq: 1/day
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 27
  sources:
  - name: default
    CL: 20
    concentration: 28
ability_scores:
  STR: 40
  DEX: 8
  CON: 31
  INT: 29
  WIS: 30
  CHA: 27
BAB: 24
CMB: 47
CMB_other: +51 grapple
CMD: 62
CMD_other: can't be tripped
feats:
- name: Awesome Blow
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (heal)
- name: Spell Penetration
- name: Staggering Critical
- name: Vital Strike
skills:
  Bluff: 35
  Escape Artist: 23
  Fly: 26
  Intimidate: 35
  Knowledge (arcana): 36
  Knowledge (dungeoneering): 33
  Knowledge (geography): 33
  Knowledge (history): 33
  Knowledge (planes): 36
  Knowledge (religion): 33
  Perception: 37
  Sense Motive: 37
  Spellcraft: 36
  Stealth: 10
  Use Magic Device: 35
languages:
- Abyssal
- telepathy 300 ft.
ecology:
  environment: any (Abyss)
  organization: solitary
  treasure_type: double
special_abilities:
  Abyssal Transformation (Su): If an iathavos establishes a hold on a creature of
    Large or smaller size, it can place that creature deep within the bristly folds
    of its flesh. Treat this as an engulf attack, except that at the start of the
    iathavos's turn, an engulfed creature must make a DC 30 Fortitude save or be transformed
    into a nyogoth qlippoth that immediately squirms out of the iathavos's body to
    serve its new master. Creatures transformed into nyogoths are not controlled by
    the iathavos, but function and behave as if they were typical members of that
    species-they retain no memories or abilities they may have possessed in their
    previous lives. Items held or worn by the unfortunate victim remain lodged within
    the folds of the iathavos's body and can only be retrieved if the iathavos is
    helpless or dead. A creature transformed into a nyogoth in this manner can be
    restored to its true shape via break enchantment, miracle, or wish. Otherwise,
    slaying the nyogoth allows the poor soul to be restored to life via reincarnation,
    resurrection, or true resurrection. The save DC is Charisma-based.
  Entropic Beams (Su): As a standard action once every minute, an iathavos can fire
    beams of entropic energy from its 10 eyes. Each of these beams of energy can be
    directed at a single target within 300 feet of the iathavos, but no more than
    one beam may be directed at any one creature. Beams that are not directed at a
    creature are wasted. The qlippoth must make a +15 ranged touch attack to hit with
    each beam. Each beam has the same effect as a CL 20th disintegrate (40d6 damage,
    DC 32 Fortitude partial for 5d6 damage), except a creature killed by this damage
    explodes in a 5-foot burst of energy, flesh, shadow, and smoke instead of turning
    into dust. Any creature in this burst must make a DC 32 Will save or be staggered
    for 1 round. The save DCs are Constitution-based.
  Horrific Appearance (Su): Creatures that succumb to the iathavos's horrific appearance
    are affected by a feeblemind effect and permanently blinded.
  Ichor (Su): As long as the iathavos has taken any hit point damage, thick and stringy
    ropes of black ichor weep from the fissures and folds in its bristly hide. This
    ichor extrudes from the creature's body in a writhing nimbus of filaments at a
    rate of 5 feet per round, to a maximum range equal to its reach (30 feet). At
    the start the iathavos's turn, all creatures in reach of these strands of ichor
    must make a DC 32 Reflex save or become entangled. At the start the iathavos's
    turn, all creatures entangled by the ichor take 4d6 points of acid damage. If
    the qlippoth ends its turn with no hit point damage, the ichor melts away into
    harmless mist, releasing all entangled creatures. The save DC is Constitution-based.
  Stench (Su): The iathavos's stench ability is supernaturally disgusting-creatures
    that succumb to this ability are nauseated, while those that save are still sickened.
desc_long: |-
  The most terrible of the qlippoth, with the exception of the qlippoth lords, is doubtless the immense iathavos. Believed by many to be a singular entity, a unique qlippoth so abhorrent that even the Abyss cannot bear to allow more than one to exist at any one time, the iathavos is often encountered attended by numerous nyogoth qlippoth that squirm over its body or under its bulk, feeding upon the wastes and fragments left behind by its shuddersome passing. These nyogoths are invariably other creatures that the iathavos has absorbed and remade-they represent one of the most heinous fates that could await would-be explorers of the deepest Abyssal rifts.

  The iathavos crusades against the demonic scourge, but the monster does not limit its attentions to seeking out and destroying demons in preparation for the return of the Abyss to qlippoth rule. Indeed, the iathavos has the ability to shift among the various planes of the multiverse, and often travels to Material Plane worlds to systematically scour realms clean of mortal life, thus ensuring that these worlds can no longer provide the raw materials-sinful mortal souls-the Abyss relies upon to create new demons. Worlds visited by the iathavos are notable for the widespread devastation and the unusually large populations of nyogoths that remain behind to consume every last speck of decay the iathavos leaves behind.

  The iathavos can be called via the most powerful spells, such as gate, but its immunity to mind-affecting effects and its vast size ensure that only the most desperate or most insane ever attempt such a self-destructive act. In all known cases, the deliberate conjuration of the iathavos to another world has done little more than draw the attention of the powerful creature to that world, so that even if it is banished back to the Abyss before it can cause too much devastation, the iathavos remembers the visit. It often returns under its own power at a later date to pursue its own goals on the newly discovered world. Only if the iathavos is presented with defenders that prevent it from achieving its destructive ruin does it flee back to the Abyss via plane shift-in such cases, the qlippoth often waits for centuries or even millennia before returning to that world, for there are always easier realms to destroy.

  The iathavos is a powerful and horrifying monster made all the more devastating by its incredible intellect. The creature takes care to plan its major assaults on demonic enclaves or mortal cities, even though it is powerful enough that few creatures in the multiverse can give it pause.

  When the iathavos is slain, the multiverse typically has only a relatively short time before the Abyss births a replacement monstrosity for the defeated qlippoth. This newly born iathavos is an entirely new creature-it does not share the memories of the previous incarnation, nor does it possess any advanced hit dice or class levels the previous monster may have gained, yet its appetite and hatred for demonic life and the sins that create such life remain constant and unending.

  To call such an iathavos a “newborn” is somewhat misleading. Although technically a freshly created creature, newborn iathavoses do not undergo a “childhood.” They form fully grown, as presented here. Yet with each new incarnation of the qlippoth monstrosity, changes can occur. A new iathavos might have slightly different spell-like abilities, for example, or the nature of its horrific appearance might change from that presented here. As an iathavos continues to hunt and destroy, it grows more powerful-an advanced iathavos typically gains more racial Hit Dice as a result. An iathavos that gains power by taking class levels is not unheard of, but it is quite rare-most who do take levels in sorcerer.

---

# Qlippoth, Iathavos
This immense creature has four bat-like wings and a spherical body. Red eyes peer from all sides, and two huge claws dangle below.
**Source** Bestiary 2 pg. 222
**XP** 307,200
CE Colossal outsider (chaotic, evil, extraplanar, qlippoth)
**Init** –1; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +37
**Aura** _[[universal monster rules/Stench|stench]]_ (DC 32, 10 rounds), _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 26)

##### Defense

**AC** 37, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+4 deflection, –1 Dex, +2 insight, +30 natural, –8 size)
**hp** 372 (24d10+240); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +28, **Ref** +15, **Will** +28
**Defensive Abilities** ichor, never surprised or _flat-footed_; **DR** 15/cold iron and lawful; **Immune** cold, poison, mind-affecting effects; **Resist** acid 30, electricity 10, fire 10; **SR** 31

##### Offense
**Speed** 20 ft., fly 50 ft. (perfect)
**Melee** 2 claws +31 (4d6+15/19–20 plus _[[universal monster rules/Grab|grab]]_), 4 wings +26 (2d8+7)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** abyssal _[[spells/Transformation|transformation]]_, entropic beams, horrific appearance (DC 30)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +28)
Constant—_cloak of chaos_ (DC 26), _[[spells/Foresight|foresight]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/True Seeing|true seeing]]_
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Dispel Law|dispel law]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Plane Shift|plane shift]]_ (DC 25), _[[spells/Wind Walk|wind walk]]_, _[[spells/Word of Recall|word of recall]]_
3/day—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Dimensional Lock|dimensional lock]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (DC 26), _[[spells/Insanity|insanity]]_ (DC 25), _[[spells/Word Of Chaos|word of chaos]]_ (DC 25)
1/day—quickened _[[spells/Heal|heal]]_, _[[spells/Imprisonment|imprisonment]]_ (DC 27)

##### Statistics
**Str** 40, **Dex** 8, **Con** 31, **Int** 29, **Wis** 30, **Cha** 27
**Base Atk** +24; **CMB** +47 (+51 grapple); **CMD** 62 (can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_heal_), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +35, Escape Artist +23, Fly +26, Intimidate +35, Knowledge (arcana) +36, Knowledge (dungeoneering) +33, Knowledge (geography) +33, Knowledge (history) +33, Knowledge (planes) +36, Knowledge (religion) +33, Perception +37, Sense Motive +37, Spellcraft +36, Stealth +10, Use Magic Device +35
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary
**Treasure** double

### Special Abilities

**Abyssal _Transformation_ (Su)** If an iathavos establishes a hold on a creature of Large or smaller size, it can place that creature deep within the bristly folds of its flesh. Treat this as an _[[universal monster rules/Engulf|engulf]]_ attack, except that at the start of the iathavos’s turn, an engulfed creature must make a DC 30 Fortitude save or be transformed into a nyogoth qlippoth that immediately squirms out of the iathavos’s body to serve its new master. Creatures transformed into nyogoths are not controlled by the iathavos, but function and behave as if they were typical members of that species—they retain no memories or abilities they may have possessed in their previous lives. Items held or worn by the unfortunate victim remain lodged within the folds of the iathavos’s body and can only be retrieved if the iathavos is _[[conditions/Helpless|helpless]]_ or dead. A creature transformed into a nyogoth in this manner can be restored to its true shape via _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Miracle|miracle]]_, or _[[spells/Wish|wish]]_. Otherwise, slaying the nyogoth allows the poor soul to be restored to life via reincarnation, _[[spells/Resurrection|resurrection]]_, or _[[spells/True Resurrection|true resurrection]]_. The save DC is Charisma-based.

**Entropic Beams (Su)** As a standard action once every minute, an iathavos can fire beams of entropic energy from its 10 eyes. Each of these beams of energy can be directed at a single target within 300 feet of the iathavos, but no more than one beam may be directed at any one creature. Beams that are not directed at a creature are wasted. The qlippoth must make a +15 ranged touch attack to hit with each beam. Each beam has the same effect as a CL 20th _[[spells/Disintegrate|disintegrate]]_ (40d6 damage, DC 32 Fortitude partial for 5d6 damage), except a creature killed by this damage explodes in a 5-foot burst of energy, flesh, _[[items/Armor Magic Abilities/Shadow|shadow]]_, and smoke instead of turning into dust. Any creature in this burst must make a DC 32 Will save or be _[[conditions/Staggered|staggered]]_ for 1 round. The save DCs are Constitution-based.

**Horrific Appearance (Su)** Creatures that succumb to the iathavos’s horrific appearance are affected by a _[[spells/Feeblemind|feeblemind]]_ effect and permanently _[[conditions/Blinded|blinded]]_.

**Ichor (Su)** As long as the iathavos has taken any hit point damage, thick and stringy ropes of black ichor weep from the fissures and folds in its bristly hide. This ichor extrudes from the creature’s body in a writhing nimbus of filaments at a rate of 5 feet per round, to a maximum range equal to its reach (30 feet). At the start the iathavos’s turn, all creatures in reach of these strands of ichor must make a DC 32 Reflex save or become _[[conditions/Entangled|entangled]]_. At the start the iathavos’s turn, all creatures _entangled_ by the ichor take 4d6 points of acid damage. If the qlippoth ends its turn with no hit point damage, the ichor melts away into harmless mist, releasing all _entangled_ creatures. The save DC is Constitution-based.
**_Stench_ (Su) **The iathavos’s _stench_ ability is supernaturally disgusting—creatures that succumb to this ability are _[[conditions/Nauseated|nauseated]]_, while those that save are still _[[conditions/Sickened|sickened]]_.

##### Description

The most terrible of the qlippoth, with the exception of the qlippoth lords, is doubtless the immense iathavos. Believed by many to be a singular entity, a unique qlippoth so abhorrent that even the Abyss cannot bear to allow more than one to exist at any one time, the iathavos is often encountered attended by numerous nyogoth qlippoth that squirm over its body or under its bulk, feeding upon the wastes and fragments left behind by its shuddersome passing. These nyogoths are invariably other creatures that the iathavos has absorbed and remade—they represent one of the most heinous fates that could await would-be explorers of the deepest Abyssal rifts.

The iathavos crusades against the demonic scourge, but the monster does not limit its attentions to seeking out and destroying demons in preparation for the return of the Abyss to qlippoth rule. Indeed, the iathavos has the ability to shift among the various planes of the multiverse, and often travels to Material Plane worlds to systematically scour realms clean of mortal life, thus ensuring that these worlds can no longer provide the raw materials—sinful mortal souls—the Abyss relies upon to create new demons. Worlds visited by the iathavos are notable for the widespread devastation and the unusually large populations of nyogoths that remain behind to consume every last speck of decay the iathavos leaves behind.

The iathavos can be _[[items/Weapon Magic Abilities/Called|called]]_ via the most powerful spells, such as _[[spells/Gate|gate]]_, but its _[[universal monster rules/Immunity|immunity]]_ to mind-affecting effects and its vast size ensure that only the most desperate or most insane ever attempt such a self-destructive act. In all known cases, the deliberate conjuration of the iathavos to another world has done little more than draw the attention of the powerful creature to that world, so that even if it is banished back to the Abyss before it can cause too much devastation, the iathavos remembers the visit. It often returns under its own power at a later date to pursue its own goals on the newly discovered world. Only if the iathavos is presented with defenders that prevent it from achieving its destructive ruin does it flee back to the Abyss via _plane shift_—in such cases, the qlippoth often waits for centuries or even millennia before returning to that world, for there are always easier realms to destroy.

The iathavos is a powerful and horrifying monster made all the more devastating by its incredible intellect. The creature takes care to plan its major assaults on demonic enclaves or mortal cities, even though it is powerful enough that few creatures in the multiverse can give it pause.

When the iathavos is slain, the multiverse typically has only a relatively short time before the Abyss births a replacement monstrosity for the defeated qlippoth. This newly born iathavos is an entirely new creature—it does not share the memories of the previous incarnation, nor does it possess any advanced hit dice or class levels the previous monster may have gained, yet its appetite and hatred for demonic life and the sins that create such life remain constant and unending.

To call such an iathavos a “newborn” is somewhat misleading. Although technically a freshly created creature, newborn iathavoses do not undergo a “childhood.” They form fully grown, as presented here. Yet with each new incarnation of the qlippoth monstrosity, changes can occur. A new iathavos might have slightly different _spell-like abilities_, for example, or the nature of its horrific appearance might change from that presented here. As an iathavos continues to hunt and destroy, it grows more powerful—an advanced iathavos typically gains more racial Hit Dice as a result. An iathavos that gains power by taking class levels is not unheard of, but it is quite rare—most who do take levels in _[[classes/Sorcerer|sorcerer]]_.