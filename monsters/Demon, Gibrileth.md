---
cssclass: [monsters]
title1: Demon, Gibrileth
desc_short: 'This flying, bulbous, tumor-riddled mass has numerous arms, no legs,
  and a leering, three-eyed face. '
title2: Gibrileth
CR: 11
sources:
- name: The Worldwound
  page: 46
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 12800
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
  scent: true
AC:
  AC: 25
  touch: 13
  flat_footed: 21
  components:
    dex: 4
    natural: 12
    size: -1
HP:
  HP: 137
  long: 11d10+77
saves:
  fort: 14
  ref: 9
  will: 10
defensive_abilities:
- amorphous
DR:
- amount: 10
  weakness: good
immunities:
- acid
- disease
- electricity
- poison
resistances:
  cold: 10
  fire: 10
SR: 22
speeds:
  base: 10
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 scorpion whip +18/+13/+8 (1d6+8/18-20 plus disease)
      entries:
      - - damage: 1d6+8
          crit_range: 18-20
        - effect: disease
      attack: +1 scorpion whip
      bonus:
      - 18
      - 13
      - 8
    - text: bite +12 (1d8+3 plus disease)
      entries:
      - - damage: 1d8+3
        - effect: disease
      attack: bite
      bonus:
      - 12
  ranged:
  - - text: tumor +14 (2d6 acid plus disease)
      entries:
      - - damage: 2d6
          type: acid
        - effect: disease
      attack: tumor
      bonus:
      - 14
  special:
  - disease (see page 29)
  - whip specialist
space: 10
reach: 10
reach_other: 20 ft. with whip
spell_like_abilities:
  entries:
  - name: contagion
    source: default
    freq: At will
    DC: 17
  - name: grease
    source: default
    freq: At will
    DC: 14
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: unholy blight
    source: default
    freq: At will
    DC: 17
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 16
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: gibrileth
      amount: 1
      chance: 35%
  - name: waves of fatigue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
    concentration: 16
ability_scores:
  STR: 24
  DEX: 19
  CON: 24
  INT: 13
  WIS: 16
  CHA: 17
BAB: 11
CMB: 19
CMB_other: +23 trip
CMD: 35
CMD_other: 37 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Greater Trip
- name: Improved Initiative
- name: Improved Trip
- name: Lightning Reflexes
skills:
  Fly: 20
  Knowledge (dungeoneering): 15
  Knowledge (planes): 15
  Perception: 25
  Sense Motive: 17
  Stealth: 14
  Survival: 17
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- tumors
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or infection (3-8)
  treasure_type: standard
  treasure:
  - +1 scorpion whip
  - other treasure
special_abilities:
  Disease: Any weapon a gibrileth wields becomes a vector for spreading the demonplague.
    A creature bitten by a gibrileth or damaged by a weapon it wields is exposed to
    this virulent disease. A successful DC 22 Fortitude save is needed to resist this
    creature's particular strain of demonplague-full details on this widespread sickness
    appear on page 29. The save DC is Constitution-based.
  Tumors (Su): As a swift action, a gibrileth can rip a grapefruitsized tumor from
    its body with one of its many arms and throw it as a splash weapon with a range
    increment of 20 feet. A direct hit deals 2d6 points of acid damage, and deals
    1d4 points of acid splash damage to all creatures within 5 feet of the target.
    A creature can avoid the splash damage with a successful DC 22 Reflex save. The
    save DC is Constitution-based.
  Whip Specialist (Ex): A gibrileth does not provoke attacks of opportunity when using
    a whip.
desc_long: |-
  Gibrileths are known as filth demons because their appearance is so vile that even other demons find them appalling-including some hezrous. A gibrileth's body is composed almost entirely of quivering, globular, acidic tumors, save for its batlike wings and the nest of spindly, atrophied arms growing from the top of its body. It can walk with a clumsy gait, using its long arms, but it prefers to be on the wing. These creatures enjoy spreading nausea and sickness, either via their spell-like abilities or through violence-in fact, they are one of the primary sources of demonplague throughout the Worldwound. Gibrileths particularly relish the taste of partially liquefied, diseased flesh, and many keep infected victims in pens like cattle for periodic snacking, allowing their sickness to season them properly before feeding. Gibrileths rise from the souls of mortals who deliberately encourage the spread of disease or sickness, many of whom died of disease themselves. 

  A gibrileth is approximately 10 feet in diameter, with a wingspan of 16 feet. These foul, bloated demons typically weigh about 2,400 pounds.

---

# Demon, Gibrileth
This flying, bulbous, tumor-riddled mass has numerous arms,
no legs, and a leering, three-eyed face.

**Source** The Worldwound pg. 46
**XP** 12,800
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +25

##### Defense

**AC** 25, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 Dex, +12 natural, –1 size)
**hp** 137 (11d10+77)
**Fort** +14, **Ref** +9, **Will** +10
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **DR** 10/good; **Immune** acid,
disease, electricity, poison; **Resist** cold 10, fire 10; **SR** 22

##### Offense
**Speed** 10 ft., fly 40 ft. (good)
**Melee** +1 _[[items/Weapon/Scorpion whip|scorpion whip]]_ +18/+13/+8 (1d6+8/18–20 plus
disease), bite +12 (1d8+3 plus disease)
**Ranged** tumor +14 (2d6 acid plus disease)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _[[items/Weapon/Whip|whip]]_)
**Special Attacks** disease (see page 29), _whip_ specialist
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +16)
At will—_[[spells/Contagion|contagion]]_ (DC 17), _[[spells/Grease|grease]]_ (DC 14), greater teleport
 (self plus 50 lbs. of objects only), _[[spells/Unholy Blight|unholy blight]]_ (DC 17)
3/day—_[[spells/Stinking Cloud|stinking cloud]]_ (DC 16)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4,
 1 gibrileth 35%),
_[[spells/Waves of Fatigue|waves of fatigue]]_

##### Statistics
**Str** 24, **Dex** 19, **Con** 24, **Int** 13, **Wis** 16, **Cha** 17
**Base Atk** +11; **CMB** +19
(+23 _[[universal monster rules/Trip|trip]]_); **CMD** 35
(37 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, Greater
_Trip_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, Lightning
Reflexes
**Skills** Fly +20, Knowledge
(dungeoneering) +15,
Knowledge (planes) +15,
Perception +25, Sense
Motive +17, Stealth +14, Survival +17; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic;
_[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** tumors

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or infection (3–8)
**Treasure** standard (+1 _scorpion whip_, other treasure)

### Special Abilities

**Disease **Any weapon a gibrileth wields becomes a vector for
spreading the _[[diseases/Demonplague|demonplague]]_. A creature bitten by a gibrileth
or damaged by a weapon it wields is exposed to this _[[items/Weapon Magic Abilities/Virulent|virulent]]_
disease. A successful DC 22 Fortitude save is needed to resist
this creature’s particular strain of _demonplague_—full details
on this widespread sickness appear on page 29. The save DC
is Constitution-based.

**Tumors (Su)** As a swift action, a gibrileth can rip a grapefruitsized
tumor from its body with one of its many arms and
throw it as a splash weapon with a range increment of
 20 feet. A direct hit deals 2d6 points of acid damage, and
deals 1d4 points of _[[spells/Acid Splash|acid splash]]_ damage to all creatures
within 5 feet of the target. A creature can avoid the splash
damage with a successful DC 22 Reflex save. The save DC is
Constitution-based.

**_Whip_ Specialist (Ex)** A gibrileth does not provoke attacks of
opportunity when using a _whip_.

##### Description

Gibrileths are known as filth demons because their
appearance is so vile that even other demons find them
appalling—including some hezrous. A gibrileth’s body is
composed almost entirely of quivering,
globular, acidic tumors, save for its batlike
wings and the nest of spindly, atrophied
arms _[[items/Weapon Magic Abilities/Growing|growing]]_ from the top of its body. It
can walk with a clumsy gait, using its long
arms, but it prefers to be on the wing.
These creatures enjoy spreading
nausea and sickness, either
via their _spell-like abilities_ or
through violence—in fact, they
are one of the primary sources
of _demonplague_ throughout
the Worldwound. Gibrileths
particularly relish the taste
of partially liquefied,
diseased flesh, and many
keep infected victims
in pens like cattle for
periodic snacking, allowing
their sickness to season them
properly before feeding. Gibrileths
rise from the souls of mortals who
deliberately encourage the spread of
disease or sickness, many of whom died
of disease themselves.

A gibrileth is approximately 10 feet in
diameter, with a wingspan of 16 feet. These
foul, bloated demons typically weigh about
 2,400 pounds.