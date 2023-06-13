---
cssclass: [monsters]
title1: Kokogiak
desc_short: 'This hulking mountain of fur and fangs looks like a whitefurred bear
  of immense proportions with ten legs, each ending in massive, jet-black claws. Its
  head, with slavering jaws and a tongue dripping silvery foam, sits at the end of
  a long yet thickly muscled neck. Its dead black eyes are small but infinite pits
  of malice. '
title2: Kokogiak
CR: 12
sources:
- name: 'Pathfinder #69: Maiden, Mother, Crone'
  page: 86
  link: http://paizo.com/products/btpy8xbz?Pathfinder-Adventure-Path-69-Maiden-Mother-Crone
XP: 19200
alignment: NE
size: Huge
type: magical beast
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 9
  flat_footed: 24
  components:
    dex: 1
    natural: 16
    size: -2
HP:
  HP: 172
  long: 15d10+90
saves:
  fort: 15
  ref: 10
  will: 9
immunities:
- cold
- illusions
speeds:
  base: 40
  burrow: 20
  climb: 20
  swim: 20
attacks:
  melee:
  - - text: bite +23 (2d6+10 plus pull)
      entries:
      - - damage: 2d6+10
        - effect: pull
      attack: bite
      bonus:
      - 23
    - text: 6 claws +24 (2d6+10/19-20)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
      count: 6
      attack: claws
      bonus:
      - 24
  special:
  - blizzard breath
  - forlorn gaze
  - pull (bite, 10 ft.)
space: 15
reach: 10
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
    DC: 14
  - name: major image
    source: default
    freq: 3/day
    DC: 16
  - name: solid fog
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 15
    concentration: 18
ability_scores:
  STR: 31
  DEX: 13
  CON: 22
  INT: 13
  WIS: 14
  CHA: 16
BAB: 15
CMB: 27
CMD: 38
CMD_other: 54 vs. trip
feats:
- name: Critical Focus
- name: Improved Critical (claws)
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
- name: Weapon Focus (claws)
skills:
  Bluff: 18
  Climb: 22
  Perception: 18
  Stealth: 11
    in ice or snow: 19
  Swim: 22
  _racial_mods:
    Stealth:
      in ice or snow: 8
languages:
- Aquan
- Common
special_qualities:
- ice walker
- penetrating sight
- sound imitation
ecology:
  environment: cold coastlines, hills, or plains
  organization: solitary or pair
  treasure_type: none
special_abilities:
  Blizzard Breath (Su): A kokogiak's breath weapon is a polar gale so bitterly cold
    that it saps vigor from those it touches. Once every 1d4 rounds as a standard
    action, a kokogiak can expel a 60-foot cone of blistering arctic winds, dealing
    8d6 points of cold damage to all creatures struck. A successful DC 23 Reflex save
    halves this damage. Any creature damaged by this attack must then succeed at a
    DC 23 Fortitude save or become fatigued (or exhausted if it was already fatigued).
    The save DCs are Constitution-based.
  Forlorn Gaze (Su): As a standard action, a kokogiak can lock its black eyes on a
    target within 60 feet to fascinate the creature. A successful DC 20 Will save
    negates this effect. Creatures that fail the save are fascinated and they see
    they kokogiak as a lost loved one, trusted friend in danger, or ally in desperate
    need. Once a creature is fascinated, the kokogiak can compel the creature to move
    toward it. Once adjacent, the creature is flat-footed against the kokogiak's attacks,
    but the creature receives a new saving throw at the beginning of its turn to break
    the fascination. This is a mind-affecting effect and the save DC is Charisma-based.
  Ice Walker (Ex): A kokogiak takes no penalty to speed or on Acrobatics, Climb, or
    Stealth checks in snowy or icy terrain or weather conditions. It can walk across
    snow crusts or thin ice without breaking through. In addition, a kokogiak can
    choose to not leave tracks when moving in this type of terrain.
  Penetrating Sight (Ex): A kokogiak's sight is not affected by its own fog cloud
    or solid fog spell-like abilities. In addition, a kokogiak does not take any penalties
    on Perception checks while its snowing.
  Sound Imitation (Ex): A kokogiak can mimic any voice or sound it has heard by making
    a successful Bluff check against a listener's Sense Motive check.
desc_long: The kokogiak (called qupqugiaq by some tribes) is a deadly predator of
  the far northern wastes. At first glance, it appears to be a simple ravening beast
  or an enormous, unnaturally deformed polar bear, yet its raw power and cunning are
  legendary in the tales of northern nomads. Its name in some places is synonymous
  with cabin fever or deep-winter hallucinations that drive folk to desperation and
  madness, rushing out into the frozen wild in pursuit of some long-lost lover only
  to become lost themselves, victims of the kokogiak's dreadful might. Kokogiaks have
  an elongated neck, and are nearly 20 feet long from tail to nose. Over a dozen feet
  high at the shoulder, kokogiaks weigh between 6 and 8 tons.

---

# Kokogiak
This hulking mountain of fur and fangs looks like a whitefurred
bear of immense proportions with ten legs, each ending
in massive, jet-black claws. Its head, with slavering jaws and
a tongue dripping silvery foam, sits at the end of a long yet
thickly muscled neck. Its dead black eyes are small but infinite
pits of malice.

**Source** Pathfinder #69: Maiden, Mother, Crone pg. 86
**XP** 19,200

NE Huge magical beast
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +18

##### Defense

**AC** 25, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+1 Dex, +16 natural, –2 size)
**hp** 172 (15d10+90)
**Fort** +15, **Ref** +10, **Will** +9
**Immune** cold, illusions

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., swim 20 ft.
**Melee** bite +23 (2d6+10 plus _[[universal monster rules/Pull|pull]]_), 6 claws +24 (2d6+10/19–20)
**Space** 15 ft., **Reach** 10 ft. (20 ft. with bite)
**Special Attacks** blizzard breath, forlorn _[[universal monster rules/Gaze|gaze]]_, _pull_ (bite, 10 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
3/day—_[[spells/Major Image|major image]]_ (DC 16), _[[spells/Solid Fog|solid fog]]_

##### Statistics
**Str** 31, **Dex** 13, **Con** 22, **Int** 13, **Wis** 14, **Cha** 16
**Base Atk** +15; **CMB** +27; **CMD** 38 (54 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), Improved Vital
Strike, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, Vital
Strike, _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** Bluff +18, _Climb_ +22, Perception +18, Stealth +11 (+19 in ice
or snow), Swim +22; **Racial Modifiers** +8 Stealth in ice or snow
**Languages** Aquan, Common
**SQ** ice walker, penetrating sight, sound imitation

##### Ecology

**Environment** cold coastlines, hills, or plains
**Organization** solitary or pair
**Treasure** none

### Special Abilities

**Blizzard Breath (Su)** A _[[monsters/Kokogiak|kokogiak]]_’s _[[universal monster rules/Breath Weapon|breath weapon]]_ is a polar
gale so bitterly cold that it saps _[[spells/Vigor|vigor]]_ from those it touches.
Once every 1d4 rounds as a standard action, a _kokogiak_ can
expel a 60-foot cone of blistering arctic winds, dealing 8d6
points of cold damage to all creatures struck. A successful DC
 23 Reflex save halves this damage. Any creature damaged
by this attack must then succeed at a DC 23 Fortitude save or
become _[[conditions/Fatigued|fatigued]]_ (or _[[conditions/Exhausted|exhausted]]_ if it was already _fatigued_).
The save DCs are Constitution-based.

**Forlorn _Gaze_ (Su)** As a standard action, a _kokogiak_ can lock
its black eyes on a target within 60 feet to fascinate the
creature. A successful DC 20 Will save negates this effect.
Creatures that fail the save are _[[conditions/Fascinated|fascinated]]_ and they see
they _kokogiak_ as a lost loved one, trusted friend in danger,
or ally in desperate need. Once a creature is _fascinated_,
the _kokogiak_ can compel the creature to move toward it.
Once adjacent, the creature is _flat-footed_ against the
_kokogiak_’s attacks, but the creature receives a
new saving throw at the beginning of its
turn to break the fascination. This
is a mind-affecting effect
and the save DC is
Charisma-based.

**Ice Walker (Ex)** A
_kokogiak_ takes
no penalty
to speed
or on
Acrobatics,
_Climb_, or
Stealth checks in snowy
or icy terrain or weather
conditions. It can walk
across snow crusts or thin ice without _[[items/Weapon Magic Abilities/Breaking|breaking]]_ through. In
addition, a _kokogiak_ can choose to not leave tracks when
moving in this type of terrain.

**Penetrating Sight (Ex)** A _kokogiak_’s sight is not affected
by its own _fog cloud_ or _solid fog_ _spell-like abilities_. In
addition, a _kokogiak_ does not take any penalties on
Perception checks while its snowing.
**Sound Imitation (Ex)** A _kokogiak_ can _[[monsters/Mimic|mimic]]_ any voice or sound
it has heard by making a successful Bluff check against a
listener’s Sense Motive check.

##### Description

The _kokogiak_ (_[[items/Weapon Magic Abilities/Called|called]]_ qupqugiaq by some tribes) is a
_[[items/Weapon Magic Abilities/Deadly|deadly]]_ predator of the far northern wastes. At first glance,
it appears to be a simple ravening beast or an enormous,
unnaturally deformed polar bear, yet its raw power and
_[[items/Weapon Magic Abilities/Cunning|cunning]]_ are legendary in the tales of northern nomads.
Its name in some places is synonymous with cabin fever or
deep-winter hallucinations that drive folk to desperation
and madness, rushing out into the frozen wild in pursuit
of some long-lost lover only to become lost themselves,
victims of the _kokogiak_’s dreadful might. Kokogiaks have
an elongated neck, and are nearly 20 feet long from tail
to nose. Over a dozen feet high at the shoulder, kokogiaks
weigh between 6 and 8 tons.