---
cssclass: [monsters]
title1: Spiroskek
desc_short: The rear limbs of this elk-sized insectoid loop into a large, chitinous
  sphere, and it nimbly propels itself forward with balance and grace.
title2: Spiroskek
CR: 6
sources:
- name: Down the Blighted Path
  page: 59
  link: http://paizo.com/products/btpy9j6u?Pathfinder-Module-Down-the-Blighted-Path
XP: 2400
alignment: CN
size: Medium
type: magical beast
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  tremorsense: 60
AC:
  AC: 19
  touch: 15
  flat_footed: 14
  components:
    dex: 4
    dodge: 1
    natural: 4
HP:
  HP: 68
  long: 8d10+24
saves:
  fort: 9
  ref: 10
  will: 5
defensive_abilities:
- wheel barbs
immunities:
- disease
- poison
speeds:
  base: 40
  climb: 10
attacks:
  melee:
  - - text: bite +13 (1d6+4 plus bleed)
      entries:
      - - damage: 1d6+4
        - effect: bleed
      attack: bite
      bonus:
      - 13
    - text: claws +12 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: claws
      bonus:
      - 12
  special:
  - freewheeling charge
  - bleed (1d6)
spell_like_abilities:
  entries:
  - name: glitterdust
    source: default
    freq: 3/day
    DC: 15
  - name: silent image
    source: default
    freq: 3/day
    DC: 14
  sources:
  - name: default
    CL: 8
    concentration: 11
ability_scores:
  STR: 18
  DEX: 19
  CON: 16
  INT: 5
  WIS: 16
  CHA: 17
BAB: 8
CMB: 12
CMD: 27
feats:
- name: Dodge
- name: Mobility
- name: Nimble Moves
- name: Weapon Focus (bite)
skills:
  Climb: 17
  Perception: 12
  Stealth: 9
  Survival: 5
    when tracking: 13
  _racial_mods:
    Perception:
      _: 4
    Survival:
      when tracking: 8
languages:
- Aklo (can't speak)
ecology:
  environment: any underground
  organization: solitary, pair, or nest (3-6)
  treasure_type: incidental
special_abilities:
  Freewheeling Charge (Ex): A spiroskek can prime its wheel-limb for a swift and powerful
    charge attack, allowing it to move triple its normal speed on a charge, double
    move, or run action. While using a freewheeling charge, a spiroskek may run or
    charge over difficult terrain (though each square of difficult terrain still counts
    as 2 squares of movement). If the spiroskek successfully hits during this charge,
    it can immediately attempt either a bull rush or an overrun combat maneuver with
    a +4 circumstance bonus on the check without provoking an attack of opportunity.
    The effort needed for a freewheeling charge leaves the spiroskek staggered until
    the end of its next turn.
  Wheel Barbs (Ex): The spiroskek's wheel-limb is covered in tiny, flexible barbs.
    These grant the spiroskek a +4 bonus to CMD against bull rush, dragAPG, repositionAPG,
    and trip maneuvers, and to Acrobatics checks to avoid falling on slippery terrain.
desc_long: |-
  Wise Darklands-dwellers learn to listen for the faint, eerie “skek-kek-kek” noise that a prowling spiroskek's wheel-limb makes. These insectile carnivores of Nar-Voth stalk a variety of intelligent prey, and generations of devouring derros, duergar, and fey has imparted the creatures with a measure of illusory magic. They are clever ambush predators, capable of phenomenal bursts of speed. Once their prey has been wounded, a pack follows like vultures, waiting for their anticoagulant saliva to bleed a creature dry before moving in to feast. Many spiroskeks target slaver parties, taking advantage of the meat that arrives bound or hobbled; duergar especially hate the beasts.

  Spiroskeks are clever, but have little culture. They communicate in a language of mandible clicks and bodily gestures, which they use to give warnings and exchange tales of successful hunts. Normally loyal to their nests, spiroskeks consider most other creatures-even others of their kind-either enemies or prey.

  Spiroskeks are 5 to 6 feet tall and weigh approximately 170 pounds.

---

# Spiroskek
The rear limbs of this elk-sized insectoid loop into a large, chitinous sphere, and it nimbly propels itself forward with balance and _[[spells/Grace|grace]]_.
**Source** Down the Blighted Path pg. 59
**XP** 2,400

CN Medium magical beast
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +12

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 68 (8d10+24)
**Fort** +9, **Ref** +10, **Will** +5
**Defensive Abilities** wheel barbs; **Immune** disease, poison

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 10 ft.
**Melee** bite +13 (1d6+4 plus _[[universal monster rules/Bleed|bleed]]_), claws +12 (1d4+4)
**Special Attacks** freewheeling charge, _bleed_ (1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
3/day—_[[spells/Glitterdust|glitterdust]]_ (DC 15), _[[spells/Silent Image|silent image]]_ (DC 14)

##### Statistics
**Str** 18, **Dex** 19, **Con** 16, **Int** 5, **Wis** 16, **Cha** 17
**Base Atk** +8; **CMB** +12; **CMD** 27
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** _Climb_ +17, Perception +12, Stealth +9, Survival +5 (+13 when tracking); **Racial Modifiers** +4 Perception, +8 Survival when tracking
**Languages** Aklo (can’t speak)

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or nest (3–6)
**Treasure** incidental

### Special Abilities

**Freewheeling Charge (Ex)** A _[[monsters/Spiroskek|spiroskek]]_ can prime its wheel-limb for a swift and _[[universal monster rules/Powerful Charge|powerful charge]]_ attack, allowing it to move triple its normal speed on a charge, double move, or run action. While using a freewheeling charge, a _spiroskek_ may run or charge over difficult terrain (though each square of difficult terrain still counts as 2 squares of movement). If the _spiroskek_ successfully hits during this charge, it can immediately attempt either a bull rush or an overrun combat maneuver with a +4 circumstance bonus on the check without provoking an attack of opportunity. The effort needed for a freewheeling charge leaves the _spiroskek_ _[[conditions/Staggered|staggered]]_ until the end of its next turn.

**Wheel Barbs (Ex)** The _spiroskek_’s wheel-limb is covered in tiny, flexible barbs. These grant the _spiroskek_ a +4 bonus to CMD against bull rush, drag, reposition, and _[[universal monster rules/Trip|trip]]_ maneuvers, and to Acrobatics checks to avoid falling on slippery terrain.

##### Description

Wise Darklands-dwellers learn to listen for the faint, eerie “skek-kek-kek” noise that a prowling _spiroskek_’s wheel-limb makes. These insectile carnivores of Nar-Voth stalk a variety of intelligent prey, and generations of devouring derros, _[[monsters/Duergar|duergar]]_, and fey has imparted the creatures with a measure of illusory magic. They are clever ambush predators, capable of phenomenal bursts of speed. Once their prey has been wounded, a pack follows like vultures, waiting for their anticoagulant saliva to _bleed_ a creature dry before moving in to feast. Many spiroskeks target slaver parties, taking advantage of the meat that arrives bound or hobbled; _duergar_ especially hate the beasts.

Spiroskeks are clever, but have little culture. They communicate in a language of mandible clicks and bodily gestures, which they use to give warnings and exchange tales of successful hunts. Normally loyal to their nests, spiroskeks consider most other creatures—even others of their kind—either enemies or prey.

Spiroskeks are 5 to 6 feet tall and weigh approximately 170 pounds.