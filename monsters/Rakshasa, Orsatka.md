---
cssclass: [monsters]
title1: Rakshasa, Orsatka
desc_short: This hulking bear-headed fiend has a mouth full of fangs and clawed, six-fingered
  hands with too many knuckles.
title2: Orsatka
CR: 13
sources:
- name: Book of the Damned
  page: 252
  link: http://paizo.com/products/btpy9tok
XP: 25600
alignment: LE
size: Medium
type: outsider
subtypes:
- native
- rakshasa
- shapechanger
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 28
  touch: 16
  flat_footed: 22
  components:
    dex: 6
    natural: 12
HP:
  HP: 189
  long: 14d10+112
saves:
  fort: 17
  ref: 15
  will: 11
DR:
- amount: 15
  weakness: good and piercing
SR: 28
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: bite +23 (4d6+9/19-20 plus stagger)
      entries:
      - - damage: 4d6+9
          crit_range: 19-20
        - effect: stagger
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (2d4+9 plus stagger)
      entries:
      - - damage: 2d4+9
        - effect: stagger
      count: 2
      attack: claws
      bonus:
      - 23
  special:
  - detect thoughts (DC 23)
  - wicked reach
space: 5
reach: 5
reach_other: 10 ft. with trip
spell_like_abilities:
  entries:
  - name: magic missile
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: 3/day
  - name: magic circle against good 1/day-true form
    source: default
    freq: 3/day
    DC: 18
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 28
  DEX: 22
  CON: 26
  INT: 15
  WIS: 21
  CHA: 19
BAB: 14
CMB: 23
CMB_other: +27 trip
CMD: 39
CMD_other: 41 vs. trip
feats:
- name: Alertness
- name: Combat Expertise
- name: Greater Trip
- name: Improved Critical (bite)
- name: Improved Trip
- name: Iron Will
- name: Power Attack
skills:
  Bluff: 25
  Climb: 34
  Disguise: 29
  Intimidate: 21
  Knowledge (local): 12
  Knowledge (planes): 12
  Perception: 26
  Sense Motive: 26
  Stealth: 23
  _racial_mods:
    Bluff:
      _: 4
    Disguise:
      _: 8
languages:
- Common
- Infernal
- Undercommon
special_qualities:
- change shape (any humanoid, alter self)
ecology:
  environment: any
  organization: solitary or guard (1 plus 1 other rakshasa)
  treasure_type: double
special_abilities:
  Stagger (Su): A creature damaged by an orsatka's bite or claw must succeed at a
    DC 21 Will save or be staggered for 1 round by the overwhelming pain. This is
    a mind-affecting pain effect. The save DC is Charisma-based.
  Wicked Reach (Ex): 'An orsatka's joints are strange and unnatural even by the standards
    of rakshasas. An orsatka can stretch its limbs for the purpose of trip combat
    maneuvers: it is considered to have a reach of 10 feet when attempting to trip,
    and can perform such a maneuver as an attack of opportunity.'
desc_long: |-
  Often called “fiend killers” by those acquainted with their bruising ways, orsatkas are among the least subtle of rakshasas. Orsatkas arise from those who committed acts of senseless brutality on a massive scale. They are cruelty and brute force incarnate; instead of having incredible spellcasting power, orsatkas have the capability to inflict devastating damage. Rakshasas' typical affinity for magic manifests in orsatkas as an uncanny way of sniffing out their enemies, regardless of the abjurations and illusions those foes might use to protect themselves. When not disguised, orsatkas resemble huge, muscle-bound humans with bearlike heads, which sometimes boast thick, red-tinted fur.

   Orsatkas are about 7 feet tall and weigh around 400 pounds.

---

# Rakshasa, Orsatka
This hulking bear-headed fiend has a mouth full of fangs and clawed, six-fingered hands with too many knuckles.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 252
**XP** 25,600

LE Medium outsider (native, _[[monsters/Rakshasa|rakshasa]]_, shapechanger)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +26

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+6 Dex, +12 natural)
**hp** 189 (14d10+112)
**Fort** +17, **Ref** +15, **Will** +11
**DR** 15/good and piercing; **SR** 28

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +23 (4d6+9/19-20 plus stagger), 2 claws +23 (2d4+9 plus stagger)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _[[universal monster rules/Trip|trip]]_)
**Special Attacks** _[[spells/Detect Thoughts|detect thoughts]]_ (DC 23), wicked reach
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
At will—_[[spells/Magic Missile|magic missile]]_
 3/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Good|magic circle against good]]_ 1/day—_[[spells/True Form|true form]]_ (DC 18)

##### Statistics
**Str** 28, **Dex** 22, **Con** 26, **Int** 15, **Wis** 21, **Cha** 19
**Base Atk** +14; **CMB** +23 (+27 _trip_); **CMD** 39 (41 vs. _trip_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +25, _Climb_ +34, Disguise +29, Intimidate +21, Knowledge (local, planes) +12, Perception +26, Sense Motive +26, Stealth +23; **Racial Modifiers** +4 Bluff, +8 Disguise
**Languages** Common, Infernal, Undercommon
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid, _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any
**Organization** solitary or _[[npcs/Guard|guard]]_ (1 plus 1 other _rakshasa_)
**Treasure** double

### Special Abilities
**Stagger (Su)** A creature damaged by an orsatka’s bite or claw must succeed at a DC 21 Will save or be _[[conditions/Staggered|staggered]]_ for 1 round by the overwhelming pain. This is a mind-affecting pain effect. The save DC is Charisma-based.

**Wicked Reach (Ex)** An orsatka’s joints are strange and unnatural even by the standards of rakshasas. An orsatka can stretch its limbs for the purpose of _trip_ combat maneuvers: it is considered to have a reach of 10 feet when attempting to _trip_, and can perform such a maneuver as an attack of opportunity.

##### Description

Often _[[items/Weapon Magic Abilities/Called|called]]_ “fiend killers” by those acquainted with their bruising ways, orsatkas are among the least subtle of rakshasas. Orsatkas arise from those who committed acts of senseless brutality on a massive scale. They are _[[feats/Cruelty|cruelty]]_ and brute force incarnate; instead of having incredible spellcasting power, orsatkas have the capability to inflict devastating damage. Rakshasas’ typical affinity for magic manifests in orsatkas as an uncanny way of sniffing out their enemies, regardless of the abjurations and illusions those foes might use to protect themselves. When not disguised, orsatkas resemble huge, muscle-bound humans with bearlike heads, which sometimes boast thick, red-tinted fur.

Orsatkas are about 7 feet tall and weigh around 400 pounds.