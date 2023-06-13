---
cssclass: [monsters]
title1: Div, Bushyasta
desc_short: This gaunt figure has ashy yellow skin and a strange, feathered mask covering
  most of her face, save for her wide, fang-filled mouth.
title2: Bushyasta
CR: 6
sources:
- name: Book of the Damned
  page: 248
  link: http://paizo.com/products/btpy9tok
XP: 2400
alignment: NE
size: Medium
type: outsider
subtypes:
- div
- evil
- extraplanar
initiative:
  bonus: 9
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  see in darkness: true
AC:
  AC: 19
  touch: 15
  flat_footed: 14
  components:
    dex: 5
    natural: 4
HP:
  HP: 68
  long: 8d10+24
saves:
  fort: 9
  ref: 7
  will: 9
defensive_abilities:
- faded
DR:
- amount: 5
  weakness: cold iron or good
immunities:
- fire
- poison
resistances:
  acid: 10
  electricity: 10
SR: 17
weaknesses:
- light sensitivity
speeds:
  base: 30
  climb: 20
attacks:
  melee:
  - - text: bite +13 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+3 plus 1d6 nonlethal)
      entries:
      - - damage: 1d6+3
        - damage: 1d6
          type: nonlethal
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - staggering touch
  - withering effort
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: spider climb
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: touch of fatigue
    source: default
    freq: At will
    DC: 14
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 17
  - name: gust of wind
    source: default
    freq: 3/day
    DC: 16
  - name: slow
    source: default
    freq: 1/day
    DC: 17
  - name: suggestion
    source: default
    freq: 1/day
    DC: 17
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: aghashes
      amount: 2
      chance: 50%
  sources:
  - name: default
    CL: 6
    concentration: 10
ability_scores:
  STR: 16
  DEX: 21
  CON: 16
  INT: 18
  WIS: 17
  CHA: 19
BAB: 8
CMB: 11
CMD: 26
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Vital Strike
- name: Weapon Finesse
skills:
  Bluff: 15
  Climb: 19
  Knowledge (arcana): 15
  Knowledge (planes): 15
  Knowledge (religion): 15
  Knowledge (local): 12
  Perception: 14
  Sense Motive: 14
  Spellcraft: 15
  Stealth: 16
  Use Magic Device: 15
languages:
- Abyssal
- Celestial
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abbadon)
  organization: solitary, pair, or gathering (3-8)
  treasure_type: standard
special_abilities:
  Faded (Su): In bright light, a bushyasta appears translucent. The div gains partial
    concealment (20% miss chance) but still takes penalties due to its light sensitivity.
  Staggering Touch (Su): A bushyasta's claws inflict wracking pains. In addition to
    their normal lethal damage, her claws deal 1d6 points of nonlethal damage. A creature
    that takes nonlethal damage from this attack must succeed at a DC 18 Fortitude
    save or be staggered for 1 round. This duration stacks with multiple hits and
    multiple failed saving throws. The save DC is Charisma-based.
  Withering Effort (Su): Once per day as a standard action, a bushyasta can create
    a surge of negative energy that weakens nearby creatures. Creatures within 30
    feet of a bushyasta must succeed at a DC 18 Fortitude save or become fatigued.
    If a creature in this area that was already fatigued fails this saving throw,
    it becomes exhausted instead. The fatigued (or exhausted) condition persists as
    long as the creature is active, but it can remove the fatigued (or exhausted)
    condition if it does nothing but rest for 10 minutes. The save DC is Charisma-based.
desc_long: |-
  Preying upon the fruitful and industrious, bushyastas are agents of sloth and laziness. They promote shiftless behavior and try to lull people to sleep so that they can't achieve their goals. Keeping mortals from productive toil is a bushyasta's driving purpose.

   Bushyastas often haunt construction sites, especially those of places of civil or religious importance, and particularly savor disrupting creations that would be a focus of pride and glory for a community.

   All divs have some manner of esoteric flaw in their behavior; bushyastas' is hate for and avoidance of perfumed odors. These fiends loathe anyone wearing perfume or carrying aromatic flowers. Bushyastas' abhorrence of fragrant scents led to a custom of perfuming the dead in order to keep these divs away from funeral services.

---

# Div, Bushyasta
This gaunt figure has ashy yellow skin and a strange, feathered _[[items/Mundane/Mask|mask]]_ covering most of her face, save for her wide, fang-filled mouth.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 248
**XP** 2,400

NE Medium outsider (div, evil, extraplanar)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +14

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +4 natural)
**hp** 68 (8d10+24)
**Fort** +9, **Ref** +7, **Will** +9
**Defensive Abilities** faded; **DR** 5/cold iron or good; **Immune** fire, poison; **Resist** acid 10, electricity 10; **SR** 17
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +13 (1d8+3), 2 claws +13 (1d6+3 plus 1d6 nonlethal)
**Special Attacks** staggering touch, withering effort
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +10)
Constant—_detect good_, _detect magic_, _[[spells/Spider Climb|spider climb]]_
 At will—_[[spells/Dimension Door|dimension door]]_ (self plus 50 lbs. of objects only), _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 14)
 3/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 17), _[[spells/Gust Of Wind|gust of wind]]_ (DC 16)
 1/day—_[[spells/Slow|slow]]_ (DC 17), _[[spells/Suggestion|suggestion]]_ (DC 17), _[[universal monster rules/Summon|summon]]_ (level 4, 2 aghashes 50%)

##### Statistics
**Str** 16, **Dex** 21, **Con** 16, **Int** 18, **Wis** 17, **Cha** 19
**Base Atk** +8; **CMB** +11; **CMD** 26
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +15, _Climb_ +19, Knowledge (arcana, planes, religion) +15, Knowledge (local) +12, Perception +14, Sense Motive +14, Spellcraft +15, Stealth +16, Use Magic Device +15 
**Languages** Abyssal, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abbadon)
**Organization** solitary, pair, or gathering (3-8)
**Treasure** standard

### Special Abilities

**Faded (Su)** In bright light, a bushyasta appears translucent. The div gains partial concealment (20% miss chance) but still takes penalties due to its _light sensitivity_.
**Staggering Touch (Su)** A bushyasta’s claws inflict wracking pains. In addition to their normal lethal damage, her claws deal 1d6 points of nonlethal damage. A creature that takes nonlethal damage from this attack must succeed at a DC 18 Fortitude save or be _[[conditions/Staggered|staggered]]_ for 1 round. This duration stacks with multiple hits and multiple failed saving throws. The save DC is Charisma-based.

**Withering Effort (Su)** Once per day as a standard action, a bushyasta can create a surge of negative energy that weakens nearby creatures. Creatures within 30 feet of a bushyasta must succeed at a DC 18 Fortitude save or become _[[conditions/Fatigued|fatigued]]_. If a creature in this area that was already _fatigued_ fails this saving throw, it becomes _[[conditions/Exhausted|exhausted]]_ instead. The _fatigued_ (or _exhausted_) condition persists as long as the creature is active, but it can remove the _fatigued_ (or _exhausted_) condition if it does nothing but rest for 10 minutes. The save DC is Charisma-based.

##### Description

Preying upon the fruitful and industrious, bushyastas are agents of sloth and laziness. They promote shiftless behavior and try to lull people to sleep so that they can’t achieve their goals. Keeping mortals from productive toil is a bushyasta’s driving purpose.

Bushyastas often haunt construction sites, especially those of places of civil or religious importance, and particularly savor disrupting creations that would be a focus of pride and glory for a community.

All divs have some manner of esoteric flaw in their behavior; bushyastas’ is hate for and avoidance of perfumed odors. These fiends loathe anyone wearing perfume or carrying aromatic flowers. Bushyastas’ abhorrence of fragrant scents led to a custom of perfuming the dead in order to keep these divs away from funeral services.