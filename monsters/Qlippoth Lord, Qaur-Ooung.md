---
cssclass: [monsters]
title1: Qlippoth Lord, Qaur-Ooung
desc_short: The sides of this tentacled monstrosity-part jellyfish, part mushroom
  forest-swell with opaque, pulsing blisters.
title2: Qaur-Ooung
CR: 23
sources:
- name: Bestiary 6
  page: 236
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 819200
alignment: CE
size: Colossal
type: outsider
subtypes:
- aquatic
- chaotic
- evil
- extraplanar
- qlippoth
initiative:
  bonus: 12
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: cloak of chaos
  DC: 24
AC:
  AC: 40
  touch: 14
  flat_footed: 32
  components:
    deflection: 4
    dex: 8
    natural: 26
    size: -8
HP:
  HP: 481
  long: 26d10+338
  regeneration: 15
  regeneration_weakness: lawful
saves:
  fort: 32
  ref: 27
  will: 18
defensive_abilities:
- freedom of movement
- reactive swarms
DR:
- amount: 15
  weakness: cold iron and lawful
immunities:
- cold
- death effects
- mind-affecting effects
- poison
resistances:
  cid: 30
  electricity: 30
  fire: 30
SR: 34
speeds:
  base: 20
  fly: 60
  fly_maneuverability: good
  swim: 80
attacks:
  melee:
  - - text: slam +35 (6d6+17/19-20 plus poison)
      entries:
      - - damage: 6d6+17
          crit_range: 19-20
        - effect: poison
      attack: slam
      bonus:
      - 35
    - text: 6 tentacles +30 (2d8+8/19-20 plus grab and poison)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
        - effect: grab
        - effect: poison
      count: 6
      attack: tentacles
      bonus:
      - 30
  special:
  - blisterwomb
  - constrict (2d8+17 plus poison)
  - create spawn
  - horrific appearance (DC 29)
space: 60
reach: 60
reach_other: plus prodigious reach
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 24
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: fly
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - is_mythic_spell: true
    name: black tentacles
    source: default
    freq: At will
  - is_mythic_spell: true
    name: cloudkill
    source: default
    freq: At will
    DC: 21
  - name: control water
    source: default
    freq: At will
  - is_mythic_spell: true
    name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: control plants
    source: default
    freq: 3/day
    DC: 24
  - is_mythic_spell: true
    name: quickened heal
    source: default
    freq: 3/day
  - is_mythic_spell: true
    name: horrid wilting
    source: default
    freq: 3/day
    DC: 24
  - name: plundered power
    source: default
    freq: 3/day
    DC: 23
  - name: vortex
    source: default
    freq: 3/day
    DC: 23
  - is_mythic_spell: true
    name: tsunami
    source: default
    freq: 1/day
    DC: 25
  - name: summon qlippoth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 23
    concentration: 29
    mythic_restriction: Oaur-Ooung can use the mythic version of this ability within
      her sanctum.
ability_scores:
  STR: 44
  DEX: 27
  CON: 36
  INT: 21
  WIS: 23
  CHA: 22
BAB: 26
CMB: 51
CMB_other: +53 bull rush
CMD: 73
CMD_other: 75 vs. bull rush, can't be tripped
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (slam)
- name: Improved Critical (tentacle)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (heal)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 44
  Knowledge (arcana): 34
  Knowledge (geography): 34
  Knowledge (nature): 34
  Knowledge (planes): 34
  Knowledge (religion): 34
  Perception: 35
  Sense Motive: 35
  Spellcraft: 31
  Stealth: 21
  Swim: 54
languages:
- Abyssal
- telepathy 300 ft.
special_qualities:
- amphibious
- compression
- massive
- swarm mastery
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Blisterwomb (Su): Once per day as a standard action, Oaur-Ooung can cause one of
    the immense, pulsating blisters on her body to erupt. This creates a 30-foot cone
    of freezing fluid that deals 20d6 points of cold damage and knocks creatures standing
    in the area prone. With a successful DC 36 Reflex save, a creature takes half
    the damage and avoids being knocked prone. At the same time, a number of fully-grown
    qlippoth equal to a CR 20 encounter emerge from the blister- typically, this consists
    of four catabolignes (see page 225), but Oaur-Ooung can create any qlippoth she
    wishes with this ability. The save DC is Constitution-based.
  Create Spawn (Su): Once per round as a swift action as she slays a living non-outsider
    with her slam attack, Oaur-Ooung can transform that slain creature into a qlippoth.
    The qlippoth she creates must be of a CR no greater than the slain creature's
    CR - 2, but otherwise the nature of the new qlippoth is chosen by Oaur-Ooung.
    Once created, the new qlippoth is free-willed and retains no memories of its previous
    life. A slain creature subjected to this transformation can resist the change
    with a successful DC 29 Will save. If the save fails, the slain creature cannot
    be restored to life until the qlippoth it spawned is slain, and even then, only
    via miracle, true resurrection, or wish. The save DC is Charisma-based.
  Horrific Appearance (Su): A creature that succumbs to OaurOoung's horrific appearance
    is overwhelmed by the scope and size of the immense qlippoth lord, and falls prone
    in a stupor. In addition to falling prone, the victim is dazed for 1d6 rounds.
    Each round the victim remains dazed, it takes 1d4 points of Constitution damage.
    If a creature is killed by this damage, its body splits open and a new qlippoth
    (of a CR equal to no more than that of the target) emerges from the remains.
  Massive (Ex): Oaur-Ooung is unhindered by uneven ground and other environmental
    features that qualify as difficult terrain, though settlements and forested areas
    are considered difficult terrain for her. A Huge or smaller creature can move
    through any square occupied by Oaur-Ooung, and vice versa. Unlike kaiju, which
    are similarly massive, Oaur-Ooung can make attacks of opportunity against foes
    of any size and can be flanked by foes of any size. She gains a bonus for being
    on higher ground only if her entire space is on higher ground than the target.
    A Huge or smaller creature can climb Oaur-Ooung, but this requires a successful
    DC 30 Climb check.
  Poison (Su): 'Slam, tentacle, or constrict-injury: save Fort DC 36; frequency 1/round
    for 6 rounds; effect 1d4 Con drain; cure 2 consecutive saves. A creature slain
    by this poison splits open to spawn a new qlippoth (of a type chosen by Oaur-Ooung
    and of a CR no greater than that of the victim). The save DC is Constitution-based.'
  Prodigious Reach (Ex): Once per round as an immediate action, Oaur-Ooung can unfurl
    her central tentacle to attack any creature she can see within 600 feet with her
    slam attack. This attack can be used to make an attack of opportunity. She cannot
    grapple a foe outside of her normal reach of 60 feet.
  Reactive Swarms (Ex): Once per round when a creature strikes Oaur-Ooung with a melee
    weapon, her flesh splits and releases a nauseating spray of swarming vermin that
    immediately cloud around the attacker. This swarm deals 6d6 points of damage,
    and the attacker must succeed at a DC 36 Fortitude save or become nauseated for
    1d4 rounds. This does not require an action on Oaur-Ooung's behalf. The save DC
    is Constitution-based.
  Swarm Mastery (Ex): Oaur-Ooung is immune to swarm damage and cannot be distracted
    by swarm attacks.
desc_long: |-
  Immense Oaur-Ooung is a horrifically prolific source of soldiers for the qlippoth's war against mortals. It is from this qlippoth lord that a significant number of the Abyss's qlippoth hordes emerge. If through some chance event Oaur-Ooung were permanently slain, the production of qlippoth by the Abyss would not cease entirely, but it would diminish by a noticeable amount-at least, until the Abyss churned out some sort of equally vile and fecund replacement for the slain qlippoth lord. 

  Oaur-Ooung's Abyssal sanctum is a poisoned ocean with no shoreline. Here and there in its inky depths, submerged mountaintops reach in vain for the churning sea's surface, and leviathans swim through the vastness. Oaur-Ooung is the largest among them, but she keeps no lair as her own, content to drift through the eternal ocean spawning qlippoth large and small. Some are drowned, some she consumes, but enough escape her clutches and the ocean's depths to make their way elsewhere into the Abyss, often via churning vortices to other realms. 

  Sometimes, the creatures born from OaurOoung's blisterwombs are particularly powerful; it's rumored that at least one of the Abyss's demon lords began its existence as a qlippoth lord emerging from Oaur-Ooung. Those few who have recently seen Oaur-Ooung (and survived) claim that a blisterwomb of unprecedented size boils on her flank, suggesting that she is about to spawn something of immense power. What this new addition to the Abyss might be and what form it might take is unknown, but it surely bodes ill for mortal life on countless worlds. 

  Oaur-Ooung's body is 120 feet long, but her central tentacular stalk can unfurl to a length of miles for brief moments to lash out at creatures that have the distinct misfortune of having attracted her attention.

---

# Qlippoth Lord, Qaur-Ooung
The sides of this tentacled monstrosity—part jellyfish, part mushroom forest—swell with opaque, pulsing blisters.
**Source** Bestiary 6 pg. 236
**XP** 819,200
CE Colossal outsider (aquatic, chaotic, evil, extraplanar, qlippoth)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +35
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 24)

##### Defense

**AC** 40, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+4 deflection, +8 Dex, +26 natural, –8 size)
**hp** 481 (26d10+338); _[[universal monster rules/Regeneration|regeneration]]_ 15 (lawful)
**Fort** +32, **Ref** +27, **Will** +18
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, reactive swarms; **DR** 15/cold iron and lawful; **Immune** cold, death effects, mind-affecting effects, poison; **Resist** cid 30, electricity 30, fire 30; **SR** 34

##### Offense
**Speed** 20 ft., fly 60 ft. (good), swim 80 ft.
**Melee** slam +35 (6d6+17/19–20 plus poison), 6 tentacles +30 (2d8+8/19–20 plus _[[universal monster rules/Grab|grab]]_ and poison)
**Space** 60 ft., **Reach** 60 ft. (plus prodigious reach)
**Special Attacks** blisterwomb, _[[universal monster rules/Constrict|constrict]]_ (2d8+17 plus poison), create spawn, horrific appearance (DC 29)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +29)
Constant—_cloak of chaos_ (DC 24), _detect good_, _detect law_, fly, _freedom of movement_, _true seeing_ 
At will—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Cloudkill|cloudkill]]_ (DC 21), _[[spells/Control Water|control water]]_, _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport 
3/day—_[[spells/Control Plants|control plants]]_ (DC 24), quickened _[[spells/Heal|heal]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (DC 24), _[[spells/Plundered Power|plundered power]]_ (DC 23), _[[spells/Vortex|vortex]]_ (DC 23) 
1/day—_[[spells/Tsunami|tsunami]]_ (DC 25), _[[universal monster rules/Summon|summon]]_ qlippoth 
 Oaur-Ooung can use the mythic version of this ability within her sanctum.

##### Statistics
**Str** 44, **Dex** 27, **Con** 36, **Int** 21, **Wis** 23, **Cha** 22
**Base Atk** +26; **CMB** +51 (+53 bull rush); **CMD** 73 (75 vs. bull rush, can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam, tentacle), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_heal_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +44, Knowledge (arcana, geography, nature, planes, religion) +34, Perception +35, Sense Motive +35, Spellcraft +31, Stealth +21, Swim +54
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Compression|compression]]_, massive, swarm mastery

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Blisterwomb (Su)** Once per day as a standard action, Oaur-Ooung can cause one of the immense, pulsating blisters on her body to erupt. This creates a 30-foot cone of freezing fluid that deals 20d6 points of cold damage and knocks creatures standing in the area _[[conditions/Prone|prone]]_. With a successful DC 36 Reflex save, a creature takes half the damage and avoids being knocked _prone_. At the same time, a number of fully-grown qlippoth equal to a CR 20 encounter emerge from the blister— typically, this consists of four catabolignes (see page 225), but Oaur-Ooung can create any qlippoth she wishes with this ability. The save DC is Constitution-based.

**Create Spawn (Su)** Once per round as a swift action as she slays a living non-outsider with her slam attack, Oaur-Ooung can transform that slain creature into a qlippoth. The qlippoth she creates must be of a CR no greater than the slain creature’s CR – 2, but otherwise the nature of the new qlippoth is chosen by Oaur-Ooung. Once created, the new qlippoth is free-willed and retains no memories of its previous life. A slain creature subjected to this _[[spells/Transformation|transformation]]_ can resist the change with a successful DC 29 Will save. If the save fails, the slain creature cannot be restored to life until the qlippoth it spawned is slain, and even then, only via _[[spells/Miracle|miracle]]_, _[[spells/True Resurrection|true resurrection]]_, or _[[spells/Wish|wish]]_. The save DC is Charisma-based.

**Horrific Appearance (Su)** A creature that succumbs to OaurOoung’s horrific appearance is overwhelmed by the scope and size of the immense qlippoth lord, and falls _prone_ in a stupor. In addition to falling _prone_, the victim is _[[conditions/Dazed|dazed]]_ for 1d6 rounds. Each round the victim remains _dazed_, it takes 1d4 points of Constitution damage. If a creature is killed by this damage, its body splits open and a new qlippoth (of a CR equal to no more than that of the target) emerges from the remains.

**Massive (Ex)** Oaur-Ooung is unhindered by uneven ground and other environmental features that qualify as difficult terrain, though settlements and forested areas are considered difficult terrain for her. A Huge or smaller creature can move through any square occupied by Oaur-Ooung, and vice versa. Unlike kaiju, which are similarly massive, Oaur-Ooung can make attacks of opportunity against foes of any size and can be flanked by foes of any size. She gains a bonus for being on higher ground only if her entire space is on higher ground than the target. A Huge or smaller creature can _[[universal monster rules/Climb|climb]]_ Oaur-Ooung, but this requires a successful DC 30 _Climb_ check.

**Poison (Su)** Slam, tentacle, or _constrict_—injury: save Fort DC 36; frequency 1/round for 6 rounds; effect 1d4 Con drain; cure 2 consecutive saves. A creature slain by this poison splits open to spawn a new qlippoth (of a type chosen by Oaur-Ooung and of a CR no greater than that of the victim). The save DC is Constitution-based.

**Prodigious Reach (Ex)** Once per round as an immediate action, Oaur-Ooung can unfurl her central tentacle to attack any creature she can see within 600 feet with her slam attack. This attack can be used to make an attack of opportunity. She cannot grapple a foe outside of her normal reach of 60 feet.

**Reactive Swarms (Ex)** Once per round when a creature strikes Oaur-Ooung with a melee weapon, her flesh splits and releases a nauseating spray of swarming vermin that immediately cloud around the attacker. This swarm deals 6d6 points of damage, and the attacker must succeed at a DC 36 Fortitude save or become _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds. This does not require an action on Oaur-Ooung’s behalf. The save DC is Constitution-based.
**Swarm Mastery (Ex)** Oaur-Ooung is immune to swarm damage and cannot be distracted by swarm attacks.

##### Description

Immense Oaur-Ooung is a horrifically prolific source of soldiers for the qlippoth’s war against mortals. It is from this qlippoth lord that a significant number of the Abyss’s qlippoth hordes emerge. If through some chance event Oaur-Ooung were permanently slain, the production of qlippoth by the Abyss would not cease entirely, but it would diminish by a noticeable amount—at least, until the Abyss churned out some sort of equally vile and fecund replacement for the slain qlippoth lord.

Oaur-Ooung’s Abyssal sanctum is a poisoned ocean with no shoreline. Here and there in its inky depths, submerged mountaintops reach in vain for the churning sea’s surface, and leviathans swim through the vastness. Oaur-Ooung is the largest among them, but she keeps no lair as her own, content to drift through the eternal ocean spawning qlippoth large and small. Some are drowned, some she consumes, but enough escape her clutches and the ocean’s depths to make their way elsewhere into the Abyss, often via churning vortices to other realms.

Sometimes, the creatures born from OaurOoung’s blisterwombs are particularly powerful; it’s rumored that at least one of the Abyss’s demon lords began its existence as a qlippoth lord emerging from Oaur-Ooung. Those few who have recently seen Oaur-Ooung (and survived) claim that a blisterwomb of unprecedented size boils on her flank, suggesting that she is about to spawn something of immense power. What this new addition to the Abyss might be and what form it might take is _[[monsters/Unknown|unknown]]_, but it surely bodes ill for mortal life on countless worlds.

Oaur-Ooung’s body is 120 feet long, but her central tentacular stalk can unfurl to a length of miles for brief moments to lash out at creatures that have the distinct misfortune of having attracted her attention.