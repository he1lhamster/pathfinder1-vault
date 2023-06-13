---
cssclass: [monsters]
title1: Demon, Andrazku
desc_short: 'This burly, primitive-looking creature has an ape-like upper body, demonic
  horns, cloven hooves, and skin the color of a snow-buried corpse. '
title2: Andrazku
CR: 5
sources:
- name: 'Pathfinder #69: Maiden, Mother, Crone'
  page: 84
  link: http://paizo.com/products/btpy8xbz?Pathfinder-Adventure-Path-69-Maiden-Mother-Crone
XP: 1600
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- cold
- demon
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  scent: true
AC:
  AC: 18
  touch: 11
  flat_footed: 17
  components:
    dex: 1
    natural: 7
HP:
  HP: 57
  long: 6d10+24
saves:
  fort: 9
  ref: 6
  will: 2
DR:
- amount: 5
  weakness: cold iron or good
immunities:
- cold
- electricity
- poison
resistances:
  acid: 10
  fire: 10
SR: 16
weaknesses:
- vulnerable to fire
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: 2 slams +10 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: slams
      bonus:
      - 10
    - text: bite +10 (1d6+4 plus bleed and 1d6 cold)
      entries:
      - - damage: 1d6+4
        - effect: bleed
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 10
  special:
  - bleed 1d4
  - breath weapon (10-ft. cone, 3d6 cold, Reflex half DC 17, usable every 1d4 rounds)
  - mutilating gouge
  - powerful charge (slam, 2d6+6)
spell_like_abilities:
  entries:
  - name: cause fear
    source: default
    freq: 3/day
    DC: 13
  - name: locate creature
    source: default
    freq: 3/day
  - name: teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: righteous might
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: andrazku
      amount: 1
      chance: 25%
  sources:
  - name: default
    CL: 6
    concentration: 8
ability_scores:
  STR: 21
  DEX: 13
  CON: 18
  INT: 10
  WIS: 11
  CHA: 14
BAB: 6
CMB: 11
CMD: 22
feats:
- name: Improved Initiative
- name: Power Attack
- name: Skill Focus (Perception)
skills:
  Bluff: 11
  Climb: 12
  Intimidate: 8
  Perception: 12
  Sense Motive: 9
  Survival: 6
  Swim: 10
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Giant
- telepathy 100 ft.
special_qualities:
- icewalking
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or gang (3-8)
  treasure_type: standard
special_abilities:
  Icewalking (Ex): This ability works like the spider climb spell, but the surfaces
    the demon climbs must be icy. The demon can move across icy surfaces without penalty
    and does not need to attempt Acrobatics checks to run or charge on ice.
  Mutilating Gouge (Ex): If the andrazku hits with both slams in the same round, its
    target must succeed at a DC 17 Fortitude save or take 1 point of Charisma damage.
    The DC is Constitution-based.
desc_long: |-
  Andrazkus are thugs who use their strength to lord over weaker creatures. Their hatred is cold and seething, prone to suddenly snapping in an avalanche of ice and crushing blows. Birthed from the protomatter of the Abyss with natural gifts for tracking and subduing prey, they are sometimes used as trackers and jailors by more powerful demons who need to find lost prisoners and slaves. 

  From the waist up these demons are built much like strong, hairy humans or dwarves, but with exaggerated proportions resembling those of a gorilla. Their thick necks sport bristling manes that merge with the hair on their backs, and their flat faces bear two ramlike horns and cold eyes filled with hate. Their breath is a freezing fog, and their teeth are small but numerous, like a shark's. An andrazku's legs seem small in comparison to its torso, bend backward like a satyr's, and end in large cloven hooves. Their skin is the dead blue of a frozen corpse or a frost giant. Their top-heavy builds mean they have difficulty standing upright and normally assume a hunched posture; many prefer to walk and run on all fours, like apes. An andrazku is 7 feet tall at the shoulder and weighs 450 pounds.

---

# Demon, Andrazku
This burly, primitive-looking creature has an ape-like upper
body, demonic horns, cloven hooves, and skin the color of a
snow-buried corpse.

**Source** Pathfinder #69: Maiden, Mother, Crone pg. 84
**XP** 1,600
CE Medium outsider (chaotic, cold, demon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +12

##### Defense

**AC** 18, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+1 Dex, +7 natural)
**hp** 57 (6d10+24)
**Fort** +9, **Ref** +6, **Will** +2
**DR** 5/cold iron or good; **Immune** cold, electricity, poison; **Resist** acid 10, fire 10; **SR** 16
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 slams +10 (1d6+4), bite +10 (1d6+4 plus _[[universal monster rules/Bleed|bleed]]_ and
 1d6 cold)
**Special Attacks** _bleed_ 1d4, _[[universal monster rules/Breath Weapon|breath weapon]]_ (10-ft. cone, 3d6 cold,
Reflex half DC 17, usable every 1d4 rounds), mutilating gouge,
_[[universal monster rules/Powerful Charge|powerful charge]]_ (slam, 2d6+6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
3/day—_[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Locate Creature|locate creature]]_, teleport (self plus
 50 lbs. of objects only)
1/day—_[[spells/Righteous Might|righteous might]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1 andrazku 25%)

##### Statistics
**Str** 21, **Dex** 13, **Con** 18, **Int** 10, **Wis** 11, **Cha** 14
**Base Atk** +6; **CMB** +11; **CMD** 22
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +11, _Climb_ +12, Intimidate +8, Perception +20, Sense
Motive +9, Survival +6, Swim +10; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Giant; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** icewalking

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or gang (3–8)
**Treasure** standard

### Special Abilities

**Icewalking (Ex)** This ability works like the _[[spells/Spider Climb|spider climb]]_
spell, but the surfaces the demon climbs must be icy.
The demon can move across icy surfaces without penalty
and does not need to attempt Acrobatics checks to run or
charge on ice.

**Mutilating Gouge (Ex)** If the andrazku hits with both slams
in the same round, its target must succeed at a DC 17
Fortitude save or take 1 point of Charisma damage. The DC
is Constitution-based.

##### Description

Andrazkus are thugs who use their strength to lord over
weaker creatures. Their hatred is cold and seething, _[[conditions/Prone|prone]]_
to suddenly snapping in an avalanche of ice and crushing
blows. Birthed from the protomatter of the Abyss with
natural gifts for tracking and subduing prey, they are
sometimes used as trackers and jailors by more powerful
demons who need to find lost prisoners and slaves.

From the waist up these demons are built much like
strong, hairy humans or dwarves, but with exaggerated
proportions resembling those of a gorilla. Their thick
necks sport bristling manes that merge with the hair on
their backs, and their flat faces bear two ramlike horns
and cold eyes filled with hate. Their breath is a freezing
fog, and their teeth are small but numerous, like a
_[[monsters/Shark|shark]]_’s. An andrazku’s legs seem small in comparison
to its torso, bend backward like a _[[monsters/Satyr|satyr]]_’s, and end in large
cloven hooves. Their skin is the dead blue of a frozen
corpse or a frost giant. Their top-heavy builds mean they
have difficulty standing upright and normally assume
a hunched posture; many prefer to walk and run on all
fours, like apes. An andrazku is 7 feet tall at the shoulder
and weighs 450 pounds.