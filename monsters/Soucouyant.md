---
cssclass: [monsters]
title1: Soucouyant
desc_short: This walking nightmare resembles a white-haired old woman who looks as
  though she has been skinned alive, her bloody muscles and sinews pulsing grotesquely.
title2: Soucouyant
CR: 8
sources:
- name: Isles of the Shackles
  page: 61
  link: http://paizo.com/products/btpy8qzx?Pathfinder-Campaign-Setting-Isles-of-the-Shackles
XP: 4800
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 10
senses:
  darkvision: 60
  detect good: true
  detect magic: true
AC:
  AC: 23
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    dodge: 1
    natural: 6
HP:
  HP: 102
  long: 12d10+36
saves:
  fort: 7
  ref: 14
  will: 11
DR:
- amount: 5
  weakness: cold iron and magic
immunities:
- fire
- charm
- disease
- fear
- sleep
SR: 19
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +16 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: bite
      bonus:
      - 16
    - text: 2 claws +17 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 17
  special:
  - blood drain (1d2 Constitution)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: chill touch
    source: default
    freq: At will
    DC: 15
  - name: deep slumber
    source: default
    freq: At will
    DC: 16
  - name: scorching ray
    source: default
    freq: At will
    DC: 16
  - name: spider climb
    source: default
    freq: At will
  sources:
  - name: default
    CL: 8
    concentration: 12
ability_scores:
  STR: 18
  DEX: 22
  CON: 17
  INT: 14
  WIS: 17
  CHA: 19
BAB: 12
CMB: 18
CMB_other: +22 grapple
CMD: 33
feats:
- name: Agile Maneuvers
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Weapon Focus (claw)
skills:
  Acrobatics: 18
  Bluff: 16
  Disguise: 16
  Intimidate: 19
  Perception: 18
  Stealth: 21
languages:
- Abyssal
- Common
- Infernal
special_qualities:
- fiery form
- mask evil
ecology:
  environment: any land
  organization: solitary
  treasure_type: standard
special_abilities:
  Detonate (Su): As a standard action, a soucouyant in her fiery form can choose to
    explode in a 30-foot-radius burst of fire that deals 8d6 points of damage (DC
    19 Reflex save for half damage) to all creatures in the area. Using this ability
    returns a soucouyant to her humanoid form.
  Fiery Form (Su): As a standard action, a soucouyant who has removed her skin can
    assume the form of a flying ball of fire similar to that created by a flaming
    sphere spell (CL 8th) for up to 8 rounds. Upon returning to humanoid form, a soucouyant
    must wait 1d4 rounds before she can assume fiery form again. A soucouyant who
    enters the same space as a creature stops moving for that round and deals 3d6
    points of fire damage to the creature unless it succeeds at a DC 18 Reflex save.
    A soucouyant in fiery form retains her usual AC, but is immune to nonmagical attacks
    and effects. A successful targeted dispel magic spell or dealing 20 points of
    cold damage to a soucouyant in fiery form forces her to return to her humanoid
    form. A soucouyant can assume fiery form a number of times per day equal to her
    Charisma modifier (6 for most soucouyants). The save DC is Charisma-based.
  Mask Evil (Su): During the day, a soucouyant has the appearance of an old woman,
    an illusion created by an effect like alter self; at night the illusion fades,
    revealing her monstrous nature. While she is ”wearing” her skin, a soucouyant's
    evil nature is masked as though by a constant undetectable alignment spell.
desc_long: |-
  Soucouyants are insidious monsters also known as blood crones. They prefer to live near small humanoid societies, assuming the appearance of a wizened old woman. It is only at night that she assumes her true form, when her wrinkled skin peels back and reveals the monstrosity that lurks within, which seeks the blood of those sleeping, unsuspecting neighbors who know her merely as the eccentric widow living at the edge of town. Soucouyants prefer to capture victims for their cruel experiments when possible, and drain such unfortunates of their blood over a course of days or even weeks to sate their sanguinary appetites.

  A typical soucouyant is 6 feet tall and weighs 120 pounds. The most powerful soucouyants take it upon themselves to further their spellcasting abilities, and usually possess levels as witches.

---

# Soucouyant
This walking _[[spells/Nightmare|nightmare]]_ resembles a white-haired old woman who looks as though she has been skinned alive, her bloody muscles and sinews pulsing grotesquely.
**Source** Isles of the Shackles pg. 61
**XP** 4,800

NE Medium monstrous humanoid
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +18

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 102 (12d10+36)
**Fort** +7, **Ref** +14, **Will** +11
**DR** 5/cold iron and magic; **Immune** fire, charm, disease, _[[universal monster rules/Fear|fear]]_, sleep; **SR** 19

##### Offense
**Speed** 30 ft.
**Melee** bite +16 (2d6+4), 2 claws +17 (1d6+4 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Constitution)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +12)
Constant—_detect good_, _detect magic_
At will—_[[spells/Chill Touch|chill touch]]_ (DC 15), _[[spells/Deep Slumber|deep slumber]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_ (DC 16), _[[spells/Spider Climb|spider climb]]_

##### Statistics
**Str** 18, **Dex** 22, **Con** 17, **Int** 14, **Wis** 17, **Cha** 19
**Base Atk** +12; **CMB** +18 (+22 grapple); **CMD** 33
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +18, Bluff +16, Disguise +16, Intimidate +19, Perception +18, Stealth +21
**Languages** Abyssal, Common, Infernal
**SQ** fiery form, _[[items/Mundane/Mask|mask]]_ evil

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** standard

### Special Abilities

**_[[spells/Detonate|Detonate]]_ (Su)** As a standard action, a _[[monsters/Soucouyant|soucouyant]]_ in her fiery form can choose to explode in a 30-foot-radius burst of fire that deals 8d6 points of damage (DC 19 Reflex save for half damage) to all creatures in the area. Using this ability returns a _soucouyant_ to her humanoid form.

**Fiery Form (Su)** As a standard action, a _soucouyant_ who has removed her skin can assume the form of a flying ball of fire similar to that created by a _[[spells/Flaming Sphere|flaming sphere]]_ spell (CL 8th) for up to 8 rounds. Upon returning to humanoid form, a _soucouyant_ must wait 1d4 rounds before she can assume fiery form again. A _soucouyant_ who enters the same space as a creature stops moving for that round and deals 3d6 points of fire damage to the creature unless it succeeds at a DC 18 Reflex save. A _soucouyant_ in fiery form retains her usual AC, but is immune to nonmagical attacks and effects. A successful targeted _[[spells/Dispel Magic|dispel magic]]_ spell or dealing 20 points of cold damage to a _soucouyant_ in fiery form forces her to return to her humanoid form. A _soucouyant_ can assume fiery form a number of times per day equal to her Charisma modifier (6 for most soucouyants). The save DC is Charisma-based.

**_Mask_ Evil (Su)** During the day, a _soucouyant_ has the appearance of an old woman, an illusion created by an effect like _[[spells/Alter Self|alter self]]_; at night the illusion fades, revealing her monstrous nature. While she is ”wearing” her skin, a _soucouyant_’s evil nature is masked as though by a constant _[[spells/Undetectable Alignment|undetectable alignment]]_ spell.

##### Description

Soucouyants are insidious monsters also known as blood crones. They prefer to live near small humanoid societies, assuming the appearance of a wizened old woman. It is only at night that she assumes her _[[spells/True Form|true form]]_, when her wrinkled skin peels back and reveals the monstrosity that lurks within, which seeks the blood of those sleeping, unsuspecting neighbors who know her merely as the eccentric widow living at the edge of town. Soucouyants prefer to capture victims for their _[[items/Weapon Magic Abilities/Cruel|cruel]]_ experiments when possible, and drain such unfortunates of their blood over a course of days or even weeks to sate their sanguinary appetites.

A typical _soucouyant_ is 6 feet tall and weighs 120 pounds. The most powerful soucouyants take it upon themselves to further their spellcasting abilities, and usually possess levels as witches.