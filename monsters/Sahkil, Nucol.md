---
cssclass: [monsters]
title1: Sahkil, Nucol
desc_short: This monstrous wild boar is infested with wriggling worms and accompanied
  by a buzzing cloud of flies.
title2: Nucol
CR: 4
sources:
- name: Book of the Damned
  page: 253
  link: http://paizo.com/products/btpy9tok
XP: 1200
alignment: NE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- sahkil
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect magic: true
  low-light vision: true
AC:
  AC: 17
  touch: 13
  flat_footed: 14
  components:
    dex: 3
    natural: 4
HP:
  HP: 42
  long: 5d10+15
saves:
  fort: 7
  ref: 7
  will: 2
DR:
- amount: 5
  weakness: good
immunities:
- death effects
- disease
- fear
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 15
speeds:
  base: 40
attacks:
  melee:
  - - text: gore +10 (2d6+7 plus nervous consumption)
      entries:
      - - damage: 2d6+7
        - effect: nervous consumption
      attack: gore
      bonus:
      - 10
  special:
  - cough
  - look of fear (DC 15)
  - spirit touch
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: open/close
    source: default
    freq: At will
  - name: grease
    source: default
    freq: 3/day
    DC: 14
  - name: sense fear
    source: default
    freq: 3/day
  - name: remove disease
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 7
ability_scores:
  STR: 21
  DEX: 16
  CON: 17
  INT: 9
  WIS: 12
  CHA: 16
BAB: 5
CMB: 10
CMB_other: +12 bull rush
CMD: 23
CMD_other: 25 vs. bull rush
feats:
- name: Improved Bull Rush
- name: Improved Initiative
- name: Power Attack
skills:
  Bluff: 11
  Intimidate: 11
  Perception: 9
  Sense Motive: 9
  Stealth: 11
languages:
- Abyssal
- Celestial
- Infernal
- telepathy 100 ft.
special_qualities:
- easy to call
- emotional focus
- skip between
ecology:
  environment: any (Ethereal Plane)
  organization: solitary, pair, or sounder (3-12)
  treasure_type: incidental
special_abilities:
  Cough (Su): 'As a standard action, a nucol can bellow out a contagious cough. This
    cough can take one of two forms: a ranged touch attack consisting of a wad of
    infectious phlegm with a range of 30 feet, or a spray of snot and spit that can
    affect creatures in a 15-foot cone. Creatures subject to the cone effect can avoid
    the effects of the cough with a successful DC 15 Reflex save. All creatures affected
    by either form of the cough must succeed at a DC 15 Fortitude save or contract
    nervous consumption. The save DCs are Charisma-based.'
  Look of Fear (Su): A creature affected by a nucol's gaze is shaken for 1d2 rounds.
  Nervous Consumption (Su): Injury or contact-gore or cough; save Fort DC 15; onset
    immediate; frequency 1/day; effect 1 point of Wisdom damage. As long as a creature
    suffering from this illness suffers any Wisdom damage from any source, it takes
    a -1 penalty to its Armor Class and on ability checks and skill checks. This is
    a disease effect. The save DC is Constitution-based.
desc_long: |-
  Nucols are sahkils that delight in spreading the fear of parasites and other unseen things that can pollute the body and cause sickness. They spread a disease that weakens their victims' will and amplifies feelings of doubt and inadequacy. Nucols often use their remove disease spell-like ability to bargain with their victims, agreeing to cure them in return for a favor. The sahkil legitimately heals the victim of its affliction, but the price for doing so often outweighs the value of the curative.

   A nucol is over 4 feet long and weighs 90 pounds.

---

# Sahkil, Nucol
This monstrous wild _[[monsters/Boar|boar]]_ is infested with wriggling worms and accompanied by a buzzing cloud of flies.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 253
**XP** 1,200

NE Medium outsider (evil, extraplanar, sahkil)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +4 natural)
**hp** 42 (5d10+15)
**Fort** +7, **Ref** +7, **Will** +2
**DR** 5/good; **Immune** death effects, disease, _[[universal monster rules/Fear|fear]]_, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 15

##### Offense
**Speed** 40 ft.
**Melee** gore +10 (2d6+7 plus nervous _[[feats/Consumption|consumption]]_)
**Special Attacks** cough, look of _fear_ (DC 15), spirit touch
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +7)
Constant—_detect magic_
 At will—open/close
 3/day—_[[spells/Grease|grease]]_ (DC 14), _[[spells/Sense Fear|sense fear]]_
 1/day—_[[spells/Remove Disease|remove disease]]_

##### Statistics
**Str** 21, **Dex** 16, **Con** 17, **Int** 9, **Wis** 12, **Cha** 16
**Base Atk** +5; **CMB** +10 (+12 bull rush); **CMD** 23 (25 vs. bull rush)
**Feats** _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +11, Intimidate +11, Perception +9, Sense Motive +9, Stealth +11
**Languages** Abyssal, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** easy to call, emotional focus, skip between

##### Ecology

**Environment** any (Ethereal Plane)
**Organization** solitary, pair, or sounder (3-12)
**Treasure** incidental

### Special Abilities

**Cough (Su)** As a standard action, a nucol can bellow out a contagious cough. This cough can take one of two forms: a ranged touch attack consisting of a wad of infectious phlegm with a range of 30 feet, or a spray of snot and spit that can affect creatures in a 15-foot cone. Creatures subject to the cone effect can avoid the effects of the cough with a successful DC 15 Reflex save. All creatures affected by either form of the cough must succeed at a DC 15 Fortitude save or contract nervous _consumption_. The save DCs are Charisma-based.

**Look of _Fear_ (Su)** A creature affected by a nucol’s _[[universal monster rules/Gaze|gaze]]_ is _[[conditions/Shaken|shaken]]_ for 1d2 rounds.

**Nervous _Consumption_ (Su)** Injury or contact—gore or cough; save Fort DC 15; onset immediate; frequency 1/day; effect 1 point of Wisdom damage. As long as a creature suffering from this illness suffers any Wisdom damage from any source, it takes a –1 penalty to its Armor Class and on ability checks and skill checks. This is a disease effect. The save DC is Constitution-based.

##### Description

Nucols are sahkils that delight in spreading the _fear_ of parasites and other _[[items/Weapon Magic Abilities/Unseen|unseen]]_ things that can pollute the body and cause sickness. They spread a disease that weakens their victims’ will and amplifies feelings of doubt and inadequacy. Nucols often use their _remove disease_ spell-like ability to bargain with their victims, agreeing to cure them in return for a favor. The sahkil legitimately heals the victim of its affliction, but the price for doing so often outweighs the value of the curative.

A nucol is over 4 feet long and weighs 90 pounds.