---
cssclass: [monsters]
title1: Sangoi
desc_short: Dressed in tattered finery and an animal for a cloak, this small,gaunt
  humanoid has unnaturally long fingers and nails.
title2: Sangoi
CR: 7
sources:
- name: Bestiary 5
  page: 219
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Pathfinder #69: Maiden, Mother, Crone'
  page: 88
  link: http://paizo.com/products/btpy8xbz?Pathfinder-Adventure-Path-69-Maiden-Mother-Crone
XP: 3200
alignment: NE
size: Small
type: fey
initiative:
  bonus: 10
senses:
  hear heartbeat: true
  low-light vision: true
AC:
  AC: 21
  touch: 18
  flat_footed: 14
  components:
    dex: 6
    dodge: 1
    natural,+1 size: 3
HP:
  HP: 82
  long: 11d6+44
saves:
  fort: 7
  ref: 13
  will: 8
DR:
- amount: 5
  weakness: cold iron
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +12 (1d4+1 plus 1d4 bleed)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: bleed
      attack: bite
      bonus:
      - 12
    - text: 2 claws +12 (1d3+1plus 1d4 bleed)
      entries:
      - - damage: 1d3+1
          type: plus 1d4 bleed
      count: 2
      attack: claws
      bonus:
      - 12
  ranged:
  - - text: dagger +12 (1d3+1/19-20)
      entries:
      - - damage: 1d3+1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 12
  special:
  - bleed (1d4)
  - blood rage
  - curse of misery,horrific critical
  - sneak attack +2d6
spell_like_abilities:
  entries:
  - name: hide from animals
    source: default
    freq: Constant
    other: self only
  - name: hide from undead
    source: default
    freq: Constant
    other: self only
  - name: tongues
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 16
  - name: animal trance
    source: default
    freq: 3/day
    DC: 16
  - name: invisibility
    source: default
    freq: 3/day
    other: self only
  - name: snare
    source: default
    freq: 3/day
    DC: 17
  - name: control weather
    source: default
    freq: 1/day
  - name: dominate animal
    source: default
    freq: 1/day
    DC: 17
  - name: speak with dead
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 13
  DEX: 23
  CON: 18
  INT: 14
  WIS: 12
  CHA: 19
BAB: 5
CMB: 5
CMD: 22
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: PowerAttack
- name: Spring Attack
- name: Weapon Finesse
skills:
  Acrobatics: 20
  Bluff: 18
  Craft (traps): 10
  Diplomacy: 10
  Disguise: 18
  Escape Artist: 11
  Intimidate: 15
  Knowledge (local): 10
  Knowledge (nature): 10
  Perception: 15
  Sleight of Hand: 11
  Stealth: 24
languages:
- Aklo
- Common
- Sylvan
- tongues
special_qualities:
- change shape (Medium or Small landanimal or humanoid, polymorph)
- sidewaysglance
- sunlight transparency
ecology:
  environment: any cold or temperate land
  organization: solitary or pair
  treasure_type: standard
  treasure:
  - dagger
special_abilities:
  Curse of Misery (Su): |-
    As a full-roundaction, a sangoican deliver itscurse to an adjacenthumanoid as a melee touch attack. If the target fails itssave, the sangoi gains the benefit of aid (with a caster levelequal to the target's Hit Dice). A sangoi gains a +2 moralebonus on attack rolls, weapon damage rolls, saving throws,and opposed skill checks against any creature affectedby its curse. A creature that successfully saves can't beaffected by the same sangoi's curse for 24 hours. The saveDC is Charisma-based.
    Curse of Misery: Touch-contact; save Will DC 19; frequency1 day; effect permanent crushing despair.
  Hear Heartbeat (Ex): A sangoi can hear the beating hearts ofliving creatures nearby,
    granting it blindsense 30 feet andblindsight 5 feet. It can locate all creatures
    taking bleeddamage within 30 feet as if it had blindsight. This abilitydoes not
    reveal the location of creatures without hearts.
  Horrific Critical (Ex): When a sangoi enters a blood rage, itsclaws and teeth elongate
    and sharpen, threatening a criticalhit on a roll of 18-20. If a sangoi reduces
    a humanoid to-1 or fewer hit points with a critical hit from its claws orteeth,
    it can tear out the target's heart and consume it asa free action (Fortitude DC
    19 negates), killing the creatureinstantly. The sangoi gains 1d8 temporary hit
    points and a+2 enhancement bonus to Strength for 1 hour. When it killsa creature
    in this way, any humanoid within30 feet who witnesses this attack mustsucceed
    at a DC 19 Will save or becomeshaken and sickened for 1d4 rounds (thisis a mind-affecting
    fear effect). The saveDCs are Charisma-based.
  Sideways Glance (Su): Sangois fade fromview when in a creature's peripheralvision.
    They gain concealment againstcreatures they flank. They can attempta Bluff check
    to feint as a swiftaction, but only against a foe thatcan clearly see them.
  Sunlight Transparency (Ex): Sunlight causes sangois topartially fade from view.
    Theirbodies become translucent (20%miss chance), and they become fatigued andtake
    a -10 penalty on Disguise checks aslong as they remain in direct sunlight.
desc_long: |-
  Sometimes mistaken for vampires,sangois are evil nocturnal feythat haunt towns and graveyards,feeding on blood and hunting by thesounds of victims' hearts. They preferhumanoid blood but settle for animalblood when hungry.

  Sangoi stand 4 feet tall and weigh35 to 40 pounds.

---

# Sangoi
Dressed in tattered finery and an animal for a cloak, this small,

gaunt humanoid has unnaturally long fingers and nails.
**Source** Bestiary 5 pg. 219, Pathfinder #69: Maiden, Mother, Crone pg. 88
**XP** 3,200

NE Small fey
**Init** +10; **Senses** hear heartbeat, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 21, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+6 Dex, +1 dodge, +3 natural,

+1 size)
**hp** 82 (11d6+44)
**Fort** +7, **Ref** +13, **Will** +8
**DR** 5/cold iron

##### Offense
**Speed** 30 ft.
**Melee** bite +12 (1d4+1 plus 1d4 _[[universal monster rules/Bleed|bleed]]_), 2 claws +12 (1d3+1

plus 1d4 _bleed_)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +12 (1d3+1/19–20)
**Special Attacks** _bleed_ (1d4), _[[universal monster rules/Blood Rage|blood rage]]_, curse of misery,

horrific critical, sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
Constant—_[[spells/Hide from Animals|hide from animals]]_ (self only), _[[spells/Hide from Undead|hide from undead]]_ (self only), _[[spells/Tongues|tongues]]_

At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16)

3/day—_[[spells/Animal Trance|animal trance]]_ (DC 16), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Snare|snare]]_ (DC 17)

1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Dominate Animal|dominate animal]]_ (DC 17), _[[spells/Speak with Dead|speak with dead]]_ (DC 17)

##### Statistics
**Str** 13, **Dex** 23, **Con** 18, **Int** 14, **Wis** 12, **Cha** 19
**Base Atk** +5; **CMB** +5; **CMD** 22
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, Power

Attack, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +20, Bluff +18, Craft (traps) +10,

Diplomacy +10, Disguise +18, Escape Artist +11,

Intimidate +15, Knowledge (local, nature) +10,

Perception +15, Sleight of Hand +11, Stealth +24
**Languages** Aklo, Common, Sylvan; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[classes/Medium|Medium]]_ or Small land

animal or humanoid, _[[spells/Polymorph|polymorph]]_), sideways

glance, sunlight transparency

##### Ecology

**Environment** any cold or temperate land
**Organization** solitary or pair
**Treasure** standard (_dagger_)

### Special Abilities

**Curse of Misery (Su)**

As a full-round

action, a _[[monsters/Sangoi|sangoi]]_

can deliver its

curse to an adjacent

humanoid as a melee touch attack. If the target fails its

save, the _sangoi_ gains the benefit of aid (with a caster level

equal to the target’s Hit Dice). A _sangoi_ gains a +2 morale

bonus on attack rolls, weapon damage rolls, saving throws,

and opposed skill checks against any creature affected

by its curse. A creature that successfully saves can’t be

affected by the same _sangoi_’s curse for 24 hours. The save

DC is Charisma-based.

Curse of Misery: Touch—contact; save Will DC 19; frequency

1 day; effect permanent _[[spells/Crushing Despair|crushing despair]]_.

**Hear Heartbeat (Ex)** A _sangoi_ can hear the beating hearts of

living creatures nearby, granting it _[[universal monster rules/Blindsense|blindsense]]_ 30 feet and

_[[universal monster rules/Blindsight|blindsight]]_ 5 feet. It can locate all creatures taking _bleed_

damage within 30 feet as if it had _blindsight_. This ability

does not reveal the location of creatures without hearts.

**Horrific Critical (Ex)** When a _sangoi_ enters a _blood rage_, its

claws and teeth elongate and sharpen, threatening a critical

hit on a roll of 18–20. If a _sangoi_ reduces a humanoid to

–1 or fewer hit points with a critical hit from its claws or

teeth, it can tear out the target’s heart and consume it as

a free action (Fortitude DC 19 negates), killing the creature

instantly. The _sangoi_ gains 1d8 temporary hit points and a

+2 enhancement bonus to Strength for 1 hour. When it kills

a creature in this way, any humanoid within

30 feet who witnesses this attack must

succeed at a DC 19 Will save or become

_[[conditions/Shaken|shaken]]_ and _[[conditions/Sickened|sickened]]_ for 1d4 rounds (this

is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect). The save

DCs are Charisma-based.
**Sideways Glance (Su)** Sangois fade from

view when in a creature’s peripheral

_[[spells/Vision|vision]]_. They gain concealment against

creatures they flank. They can attempt

a Bluff check to feint as a swift

action, but only against a foe that

can clearly see them.
**Sunlight Transparency (Ex)**

Sunlight causes sangois to

partially fade from view. Their

bodies become translucent (20%

miss chance), and they become _[[conditions/Fatigued|fatigued]]_ and

take a –10 penalty on Disguise checks as

long as they remain in direct sunlight.

##### Description

Sometimes mistaken for vampires,

sangois are evil nocturnal fey

that haunt towns and graveyards,

feeding on blood and hunting by the

sounds of victims’ hearts. They prefer

humanoid blood but settle for animal

blood when hungry.

_Sangoi_ stand 4 feet tall and weigh

35 to 40 pounds.