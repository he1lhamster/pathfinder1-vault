---
cssclass: [monsters]
title1: Khala
desc_short: This dragon has broad, ragged wings. Its serpentine body ends inthree
  long, f lailing necks with hissing, triangular heads.
title2: Khala
CR: 17
sources:
- name: Bestiary 5
  page: 151
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Irrisen - Land of Eternal Winter
  page: 59
  link: http://paizo.com/products/btpy8w7f?Pathfinder-Campaign-Setting-Irrisen-Land-of-Eternal-Winter
XP: 102400
alignment: CE
size: Large
type: dragon
subtypes:
- cold
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 31
  touch: 15
  flat_footed: 25
  components:
    dex: 6
    natural: 16
    size: -1
HP:
  HP: 261
  long: 18d12+144
saves:
  fort: 19
  ref: 17
  will: 16
immunities:
- cold
- disease
- paralysis
- sleep
resistances:
  acid: 10
  electricity: 10
weaknesses:
- vulnerable to fire
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: 3 bites +27 (2d10+10/19-20 plus disease)
      entries:
      - - damage: 2d10+10
          crit_range: 19-20
        - effect: disease
      count: 3
      attack: bites
      bonus:
      - 27
    - text: tail +25(2d8+10 plus grab)
      entries:
      - - damage: 2d8+10
        - effect: grab
      attack: tail
      bonus:
      - 25
  special:
  - breath weapon (60-ft. line, 16d6 cold damage,Reflex DC 27 half, usable every 1d4
    rounds)
  - constrict(2d8+10)
  - rend (2 bites, 2d10+15)
  - tenacious grapple
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: 3/day
    other: chill shield only
  - name: empowered ice storm
    source: default
    freq: 3/day
  - name: incendiary cloud
    source: default
    freq: 3/day
    DC: 25
    other: deals cold damage
  - name: suggestion
    source: default
    freq: 3/day
    DC: 20
  - name: control weather
    source: default
    freq: 1/day
  - name: polar ray
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 23
ability_scores:
  STR: 30
  DEX: 22
  CON: 27
  INT: 22
  WIS: 21
  CHA: 25
BAB: 18
CMB: 29
CMB_other: +33 grapple
CMD: 45
CMD_other: can't betripped
feats:
- name: Alertness
- name: Critical Focus
- name: Empower Spell-LikeAbility (ice storm)
- name: Flyby Attack
- name: Improved Critical(bite)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Staggering Critical
- name: Stunning Critical
skills:
  Appraise: 27
  Bluff: 28
  Diplomacy: 28
  Fly: 29
  Intimidate: 28
  Knowledge (geography): 27
  Knowledge (local): 27
  Knowledge (nature): 27
  Perception: 30
  Sense Motive: 30
  Stealth: 23
  Survival: 26
languages:
- Abyssal
- Aquan
- Common
- Draconic
- Giant
- Goblin
ecology:
  environment: any cold
  organization: solitary
  treasure_type: double
special_abilities:
  Breath Weapon (Su): A khala can fire a jet of frigid liquidfrom one of its three
    mouths, dealing 16d6 pointsof cold damage (Reflex DC 27 half). Even if theysucceed
    at the Reflex save, creatures caught in the linemust succeed at a DC 27 Fortitude
    save or be encased in ice.A trapped creature must succeed at a DC 25 Strength
    check orDC 26 Escape Artist check as a full-round action to break free.
  Disease (Ex): 'Chillbane Fever: Bite-injury; save Fortitude DC 27;onset 1 day; frequency
    1/day; effect 1d4 Con damage,sickened, and fatigued; cure 2 consecutive saves.'
  Tenacious Grapple (Ex): A khala does not gain the grappledcondition if it grabs
    a foe with its tail, and it can maintain agrapple with its tail as a swift action.
desc_long: It is rumored that khalas were a breed of rare amphibiousdragon, warped
  through evil and wintry magic fromproud creatures into voracious and wicked things
  thatdelight in the suffering of others. The creature ambulateslike a snake, slithering
  along the ground or through theboughs of trees with its wings drawn close to its
  body, butit prefers f light whenever possible. All khalas are female,and scholars
  debate how the creatures procreate. It isbelieved that the males of the species,
  known in legend asthe zmeys, were wiped out in a war with the khalas.

---

# Khala
This dragon has broad, ragged wings. Its serpentine body ends in

three long, f lailing necks with hissing, triangular heads.
**Source** Bestiary 5 pg. 151, Irrisen - Land of Eternal Winter pg. 59
**XP** 102,400
CE Large dragon (cold)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +30

##### Defense

**AC** 31, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+6 Dex, +16 natural, –1 size)
**hp** 261 (18d12+144)
**Fort** +19, **Ref** +17, **Will** +16
**Immune** cold, disease, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **Resist** acid 10,

electricity 10
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** 3 bites +27 (2d10+10/19–20 plus disease), tail +25

(2d8+10 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. line, 16d6 cold damage,

Reflex DC 27 half, usable every 1d4 rounds), _[[universal monster rules/Constrict|constrict]]_

(2d8+10), _[[universal monster rules/Rend|rend]]_ (2 bites, 2d10+15), tenacious grapple
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
3/day—_[[spells/Fire Shield|fire shield]]_ (chill _[[spells/Shield|shield]]_ only), empowered _[[spells/Ice Storm|ice storm]]_, _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 25, deals cold damage), _[[spells/Suggestion|suggestion]]_ (DC 20)
1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Polar Ray|polar ray]]_

##### Statistics
**Str** 30, **Dex** 22, **Con** 27, **Int** 22, **Wis** 21, **Cha** 25
**Base Atk** +18; **CMB** +29 (+33 grapple); **CMD** 45 (can’t be

tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Critical Focus|Critical Focus]]_, Empower Spell-Like

Ability (_ice storm_), _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_

(bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** Appraise +27, Bluff +28, Diplomacy +28, Fly +29,

Intimidate +28, Knowledge (geography) +27,

Knowledge (local) +27, Knowledge (nature) +27,

Perception +30, Sense Motive +30, Stealth +23,

Survival +26
**Languages** Abyssal, Aquan, Common, Draconic, Giant, _[[monsters/Goblin|Goblin]]_

##### Ecology

**Environment** any cold
**Organization** solitary
**Treasure** double

### Special Abilities

**_Breath Weapon_ (Su)** A _[[monsters/Khala|khala]]_ can fire a _[[universal monster rules/Jet|jet]]_ of frigid liquid

from one of its three mouths, dealing 16d6 points

of cold damage (Reflex DC 27 half). Even if they

succeed at the Reflex save, creatures caught in the line

must succeed at a DC 27 Fortitude save or be encased in ice.

A trapped creature must succeed at a DC 25 Strength check or

DC 26 Escape Artist check as a full-round action to break free.

**Disease (Ex)** _[[diseases/Chillbane Fever|Chillbane Fever]]_: Bite—injury; save Fortitude DC 27;

onset 1 day; frequency 1/day; effect 1d4 Con damage,

_[[conditions/Sickened|sickened]]_, and _[[conditions/Fatigued|fatigued]]_; cure 2 consecutive saves.

**Tenacious Grapple (Ex)** A _khala_ does not gain the _[[conditions/Grappled|grappled]]_

condition if it grabs a foe with its tail, and it can maintain a

grapple with its tail as a swift action.

##### Description

It is rumored that khalas were a breed of rare _[[universal monster rules/Amphibious|amphibious]]_

dragon, warped through evil and wintry magic from

proud creatures into voracious and wicked things that

delight in the suffering of others. The creature ambulates

like a snake, _[[items/Weapon Magic Abilities/Slithering|slithering]]_ along the ground or through the

boughs of trees with its wings drawn close to its body, but

it prefers f light whenever possible. All khalas are female,

and scholars debate how the creatures procreate. It is

believed that the males of the species, known in legend as

the zmeys, were wiped out in a war with the khalas.