---
cssclass: [monsters]
title1: Pard
desc_short: This brightly-colored feline blur resembles a cheetah with longer fur
  and lynx-like ears, and seems to scorch the air as it moves.
title2: Pard
CR: 3
sources:
- name: Bestiary 4
  page: 211
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 800
alignment: CN
size: Medium
type: magical beast
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 20
  touch: 18
  flat_footed: 12
  components:
    dex: 7
    dodge: 1
    natural: 2
HP:
  HP: 26
  long: 4d10+4
saves:
  fort: 5
  ref: 11
  will: 2
  other: +4 vs. poison
defensive_abilities:
- evasion
- improved uncanny dodge
- uncanny dodge
DR:
- amount: 5
  weakness: magic
resistances:
  electricity: 10
  fire: 10
speeds:
  base: 120
attacks:
  melee:
  - - text: bite +12 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: bite
      bonus:
      - 12
    - text: 2 claws +7 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 2
      attack: claws
      bonus:
      - 7
  special:
  - phasing attack
ability_scores:
  STR: 15
  DEX: 24
  CON: 12
  INT: 4
  WIS: 13
  CHA: 11
BAB: 4
CMB: 6
CMD: 24
CMD_other: 28 vs. trip
feats:
- name: Dodge
- is_bonus: true
  name: Mobility
- is_bonus: true
  name: Spring Attack
- name: Weapon Finesse
- is_bonus: true
  name: Wind Stance
skills:
  Acrobatics: 15
    when jumping: 27
  Perception: 6
  Stealth: 15
  _racial_mods:
    Acrobatics:
      _: 4
      when jumping: 16
    Stealth:
      _: 4
languages:
- telepathy (empathy) 60 ft.
ecology:
  environment: temperate or warm forests or plains
  organization: solitary, pair, or den (1-2 adults and 1-4 cubs)
  treasure_type: incidental
special_abilities:
  Empathy (Su): Pards can transmit complex emotions and basic ideas to other pards.
    When interacting with other kinds of creatures, they can only convey simple emotions
    such as anger, fear, and curiosity.
  Phasing Attack (Su): As a full-round action, a pard can shift itself partially out
    of phase, damaging any creature it moves through. This works like the overrun
    combat maneuver, but the pard must move at least 30 feet and it gains a +4 bonus
    on the check. If it succeeds, the target takes 2d6 points of fire damage. If it
    exceeds a creature's CMD by 5 or more, it stuns the creature for 1 round instead
    of knocking it prone. The target can make an attack of opportunity, but at a -4
    penalty. If the target forgoes an attack of opportunity provoked by this maneuver,
    it can try to avoid the pard by attempting a DC 19 Reflex save; if successful,
    it takes only half damage. The pard can only deal phasing attack damage to each
    target once per round, no matter how many times its movement takes it over a target
    creature. When using this ability, the pard can move through up to 5 feet of any
    solid object, barrier, or difficult terrain as if it were a normal open square.
    The pard cannot end its movement inside a creature or solid barrier. This ability
    counts as trample for the purposes of effects that enhance or protect against
    trample. The save DC is Dexterity-based.
desc_long: |-
  Pards are alien catlike creatures known for their unnatural swiftness. They have sleek, short-furred bodies and long legs built for speed. Their color and markings vary widely, even among members of the same family, ranging through every color imaginable, with some bearing stripes, others spots, and a few solid-colored coats. Adult pards are 6 feet long and weigh 100 pounds.

  Pards are carnivores and usually hunt small game and larger birds (such as swans), though many have developed a fondness for the flesh of gnomes and quicklings. Smarter than common beasts, pards are semi-intelligent, mate for life, and have a complex social structure. Pards also possess a form of telepathy they use to communicate amongst themselves, and can use this on a limited basis to confront intruders or create mutually beneficial alliances.

---

# Pard
This brightly-colored feline _[[spells/Blur|blur]]_ resembles a cheetah with longer fur and lynx-like ears, and seems to scorch the air as it moves.
**Source** Bestiary 4 pg. 211
**XP** 800

CN Medium magical beast
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +6

##### Defense

**AC** 20, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 26 (4d10+4)
**Fort** +5, **Ref** +11, **Will** +2; +4 vs. poison
**Defensive Abilities** evasion, improved uncanny _dodge_, uncanny _dodge_; **DR** 5/magic; **Resist** electricity 10, fire 10

##### Offense
**Speed** 120 ft.
**Melee** bite +12 (1d6+2), 2 claws +7 (1d4+1)
**Special Attacks** phasing attack

##### Statistics
**Str** 15, **Dex** 24, **Con** 12, **Int** 4, **Wis** 13, **Cha** 11
**Base Atk** +4; **CMB** +6; **CMD** 24 (28 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +15 (+27 when jumping), Perception +6, Stealth +15; **Racial Modifiers** +4 Acrobatics (+16 when jumping), +4 Stealth
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ (_[[feats/Empathy|empathy]]_) 60 ft.

##### Ecology

**Environment** temperate or warm forests or plains
**Organization** solitary, pair, or den (1–2 adults and 1–4 cubs)
**Treasure** incidental

### Special Abilities

**_Empathy_ (Su)** Pards can transmit complex emotions and basic ideas to other pards. When interacting with other kinds of creatures, they can only convey simple emotions such as anger, _[[universal monster rules/Fear|fear]]_, and curiosity.

**Phasing Attack (Su)** As a full-round action, a _[[monsters/Pard|pard]]_ can shift itself partially out of phase, damaging any creature it moves through. This works like the overrun combat maneuver, but the _pard_ must move at least 30 feet and it gains a +4 bonus on the check. If it succeeds, the target takes 2d6 points of fire damage. If it exceeds a creature’s CMD by 5 or more, it stuns the creature for 1 round instead of knocking it _[[conditions/Prone|prone]]_. The target can make an attack of opportunity, but at a –4 penalty. If the target forgoes an attack of opportunity provoked by this maneuver, it can try to avoid the _pard_ by attempting a DC 19 Reflex save; if successful, it takes only half damage. The _pard_ can only deal phasing attack damage to each target once per round, no matter how many times its movement takes it over a target creature. When using this ability, the _pard_ can move through up to 5 feet of any solid object, barrier, or difficult terrain as if it were a normal open square. The _pard_ cannot end its movement inside a creature or solid barrier. This ability counts as _[[universal monster rules/Trample|trample]]_ for the purposes of effects that enhance or protect against _trample_. The save DC is Dexterity-based.

##### Description

Pards are alien catlike creatures known for their unnatural swiftness. They have sleek, short-furred bodies and long legs built for speed. Their color and markings vary widely, even among members of the same family, ranging through every color imaginable, with some bearing stripes, others spots, and a few solid-colored coats. Adult pards are 6 feet long and weigh 100 pounds.

Pards are carnivores and usually hunt small game and larger birds (such as swans), though many have developed a fondness for the flesh of gnomes and quicklings. Smarter than common beasts, pards are semi-intelligent, mate for life, and have a complex social structure. Pards also possess a form of _telepathy_ they use to communicate amongst themselves, and can use this on a limited basis to confront intruders or create mutually beneficial alliances.