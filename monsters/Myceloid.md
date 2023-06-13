---
cssclass: [monsters]
title1: Myceloid
desc_short: This shambling fungus creature bears a strong resemblance to a rotund
  human, but with a mushroom cap for a head.
title2: Myceloid
CR: 4
sources:
- name: Bestiary 3
  page: 196
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1200
alignment: NE
size: Medium
type: plant
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 16
  touch: 10
  flat_footed: 16
  components:
    natural: 6
HP:
  HP: 37
  long: 5d8+15
saves:
  fort: 7
  ref: 1
  will: 4
DR:
- amount: 5
  weakness: slashing
immunities:
- plant traits
resistances:
  cold: 10
  fire: 10
  sonic: 10
weaknesses:
- vulnerable to electricity
speeds:
  base: 20
attacks:
  melee:
  - - text: 2 claws +6 (1d6+3 plus disease)
      entries:
      - - damage: 1d6+3
        - effect: disease
      count: 2
      attack: claws
      bonus:
      - 6
  special:
  - spore cloud
spell_like_abilities:
  entries:
  - name: spore domination
    source: default
    freq: 1/day
    DC: 14
  sources:
  - name: default
    CL: 6
    concentration: 6
ability_scores:
  STR: 17
  DEX: 11
  CON: 16
  INT: 9
  WIS: 12
  CHA: 10
BAB: 3
CMB: 6
CMD: 16
feats:
- name: Improved Initiative
- name: Iron Will
- name: Skill Focus (Stealth)
skills:
  Perception: 6
  Sense Motive: 5
  Stealth: 9
  Survival: 5
  _racial_mods:
    Sense Motive:
      _: 4
    Survival:
      _: 4
languages:
- Undercommon
- telepathy 60 ft. (myceloids and purple pox sufferers only)
ecology:
  environment: any underground
  organization: solitary, pair, band (3-24), or colony (25-250)
  treasure_type: standard
special_abilities:
  Disease (Su): 'Purple Pox: inhaled or injury; save Fort DC 15; onset 1 minute; frequency
    1/day; effect 1d2 Wis and 1d2 Con damage; cure 2 consecutive saves. A creature
    that dies of the purple pox becomes bloated over the course of 24 hours, after
    which its body bursts open, releasing a fully grown myceloid. Additionally, as
    long as a creature takes at least 7 points of Wisdom damage from the purple pox,
    it must make a DC 15 Will save each day to avoid becoming affected by a lesser
    geas (no HD limit) that compels the sickly character to seek out the nearest myceloid
    colony in order to offer itself up for spore domination. The save DCs are Constitution-based.'
  Spore Cloud (Ex): Once per day as a standard action, a myceloid can expel a 10-foot-radius
    burst of spores centered on itself. This cloud persists for 1d3 rounds. Any creature
    caught in this cloud or that moves through it is exposed to the myceloid's purple
    pox disease-a creature need save only once against any one spore cloud, however,
    before becoming permanently immune to that particular spore cloud's effects. The
    spore cloud does not hamper vision.
  Spore Domination (Sp): This spell-like ability functions as charm monster, but functions
    only against creatures currently infected with purple pox.
desc_long: |-
  The walking fungi known as myceloids feed off of decaying organic matter like many other fungi, yet unlike typical mushrooms or molds, they take particular pleasure in feeding from the rotting bodies of humanoids. Myceloids claim to be able to taste things like “innocence,” “despair,” and “hope” in the ripeness of rancid meat, although whether this is true or simply part of the myceloids' twisted sense of humor is unclear.

  Most myceloids have deep purple caps studded with white lumps, and paler purple necks and bodies of tough, leathery fungus. Their spores grow tenaciously in living flesh, causing a rapid spread of painful purple lesions that, in advanced stages of the sickness, sprout tiny purple mushrooms; plucking these mushrooms is painful to the victim and causes bleeding. This condition, known as purple pox, is the method by which myceloids both season their meat and procreate.

  Myceloids prefer to capture victims alive for later infection and control. To a myceloid, a living creature has three uses-first as a slave, second as a host from which to birth new myceloids, and finally as a banquet to feast upon once the first two destinies have played out.

---

# Myceloid
This shambling fungus creature bears a strong resemblance to a rotund human, but with a mushroom cap for a head.
**Source** Bestiary 3 pg. 196
**XP** 1,200

NE Medium plant
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +6

##### Defense

**AC** 16, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 natural)
**hp** 37 (5d8+15)
**Fort** +7, **Ref** +1, **Will** +4
**DR** 5/slashing; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 10, fire 10, sonic 10
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 20 ft.
**Melee** 2 claws +6 (1d6+3 plus disease)
**Special Attacks** spore cloud
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +6)
1/day—spore domination (DC 14)

##### Statistics
**Str** 17, **Dex** 11, **Con** 16, **Int** 9, **Wis** 12, **Cha** 10
**Base Atk** +3; **CMB** +6; **CMD** 16
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Perception +6, Sense Motive +5, Stealth +9, Survival +5; **Racial Modifiers** +4 Sense Motive, +4 Survival
**Languages** Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 60 ft. (myceloids and purple pox sufferers only)

##### Ecology

**Environment** any underground
**Organization** solitary, pair, band (3–24), or colony (25–250)
**Treasure** standard

### Special Abilities

**Disease (Su) **Purple Pox: inhaled or injury; save Fort DC 15; onset 1 minute; frequency 1/day; effect 1d2 Wis and 1d2 Con damage; cure 2 consecutive saves. A creature that dies of the purple pox becomes bloated over the course of 24 hours, after which its body bursts open, releasing a fully grown _[[monsters/Myceloid|myceloid]]_. Additionally, as long as a creature takes at least 7 points of Wisdom damage from the purple pox, it must make a DC 15 Will save each day to avoid becoming affected by a lesser geas (no HD limit) that compels the sickly character to seek out the nearest _myceloid_ colony in order to offer itself up for spore domination. The save DCs are Constitution-based.
**Spore Cloud (Ex) **Once per day as a standard action, a _myceloid_ can expel a 10-foot-radius burst of spores centered on itself. This cloud persists for 1d3 rounds. Any creature caught in this cloud or that moves through it is exposed to the _myceloid_’s purple pox disease—a creature need save only once against any one spore cloud, however, before becoming permanently immune to that particular spore cloud’s effects. The spore cloud does not hamper _[[spells/Vision|vision]]_.
**Spore Domination (Sp)** This spell-like ability functions as _[[spells/Charm Monster|charm monster]]_, but functions only against creatures currently infected with purple pox.

##### Description

The walking fungi known as myceloids feed off of decaying organic matter like many other fungi, yet unlike typical mushrooms or molds, they take particular pleasure in feeding from the rotting bodies of humanoids. Myceloids claim to be able to taste things like “_[[spells/Innocence|innocence]]_,” “despair,” and “hope” in the ripeness of rancid meat, although whether this is true or simply part of the myceloids’ twisted sense of humor is unclear.

Most myceloids have deep purple caps studded with white lumps, and paler purple necks and bodies of tough, leathery fungus. Their spores grow tenaciously in living flesh, causing a rapid spread of painful purple lesions that, in advanced stages of the sickness, sprout tiny purple mushrooms; plucking these mushrooms is painful to the victim and causes bleeding. This condition, known as purple pox, is the method by which myceloids both season their meat and procreate.

Myceloids prefer to capture victims alive for later infection and control. To a _myceloid_, a living creature has three uses—first as a _[[items/Mundane/Slave|slave]]_, second as a host from which to birth new myceloids, and finally as a banquet to feast upon once the first two destinies have played out.