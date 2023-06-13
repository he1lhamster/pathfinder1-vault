---
cssclass: [monsters]
title1: Angel, Balisse
desc_short: This celestial being is obscured by darkness, but its wings glow brilliantly,
  silhouetting a stern individual with shining eyes.
title2: Balisse
CR: 8
sources:
- name: Bestiary 5
  page: 22
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Chronicle of the Righteous
  page: 59
  link: http://paizo.com/products/btpy8xe9?Pathfinder-Campaign-Setting-Chronicle-of-the-Righteous
XP: 4800
alignment: NG
size: Medium
type: outsider
subtypes:
- angel
- extraplanar
- good
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect evil: true
auras:
- name: protective aura
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    dex: 2
    dodge: 1
    natural: 8
    deflection vs. evil: 4
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 11
  ref: 7
  will: 10
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 10
  weakness: evil
immunities:
- acid
- cold
- petrification
resistances:
  electricity: 10
  fire: 10
SR: 19
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 flaming heavy mace +14/+9 (1d8+4 plus 1d6 fire)
      entries:
      - - damage: 1d8+4
        - damage: 1d6
          type: fire
      attack: +1 flaming heavy mace
      bonus:
      - 14
      - 9
  special:
  - brand of the impenitent
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: dispel evil
    source: default
    freq: At will
    DC: 19
  - name: dispel magic
    source: default
    freq: At will
  - name: holy smite
    source: default
    freq: At will
    DC: 18
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: plane shift
    source: default
    freq: At will
    other: self only
  - name: remove curse
    source: default
    freq: At will
  - name: remove disease
    source: default
    freq: At will
  - name: remove fear
    source: default
    freq: At will
  - name: cure serious wounds
    source: default
    freq: 3/day
  - name: hold person
    source: default
    freq: 3/day
    DC: 16
  - name: atonement
    source: default
    freq: 1/day
  - name: mark of justice
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 17
  DEX: 15
  CON: 18
  INT: 13
  WIS: 16
  CHA: 18
BAB: 10
CMB: 13
CMD: 26
feats:
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
skills:
  Acrobatics: 15
  Diplomacy: 17
  Fly: 19
  Knowledge (planes): 14
  Knowledge (religion): 14
  Perception: 16
  Sense Motive: 16
languages:
- Celestial
- Draconic
- Infernal
- truespeech
ecology:
  environment: any good-aligned planes
  organization: solitary
  treasure_type: double
  treasure:
  - +1 flaming heavy mace
  - other treasure
special_abilities:
  Brand of the Impenitent (Su): Three times per day, a balisse can brand a target
    within 30 feet (Will DC 19 negates) with a painless, glowing icon on its chest-usually
    the holy symbol of the deity or empyreal lord the balisse serves. This brand lasts
    for a number of days equal to the balisse's Hit Dice (10 days for most balisses).
    Anyone who attacks the branded target gains a +2 sacred bonus on weapon attack
    and damage rolls and a +2 sacred bonus on caster level checks to overcome the
    target's spell resistance. The save DC is Charisma-based.
desc_long: |-
  Balisses, sometimes called confessor angels, appear to good individuals on the horns of moral dilemmas or who are struggling with crises of faith. Though balisses may appear stern and unyielding, they prefer to guide individuals to their own moral decisions rather than ordering them to conform to a specific ideal of good, knowing that the goodness found on one's own is stronger than mere obedience. Balisses are formed from the souls of individuals who committed evil acts but were later redeemed and died while living an exemplary, moral life.

  Some balisses seek out mortals in need of their help, while others are given specific assignments by deities or empyreal lords. Balisses are used to dealing with stubbornness, and have an eternity's worth of patience. Though they brook no physical attacks, they can endure almost any other hostility for the sake of their mission.

  The average balisse is 7 feet tall and weighs 200 pounds.

---

# Angel, Balisse
This celestial being is obscured by _[[spells/Darkness|darkness]]_, but its wings glow brilliantly, silhouetting a stern individual with shining eyes.
**Source** Bestiary 5 pg. 22, _[[items/Wondrous Item/Chronicle of the Righteous|Chronicle of the Righteous]]_ pg. 59
**XP** 4,800

NG Medium outsider (angel, extraplanar, good)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_; Perception +16
**Aura** protective aura

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural; +4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 95 (10d10+40)
**Fort** +11, **Ref** +7, **Will** +10; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 10/evil; **Immune** acid, cold, petrification; **Resist** electricity 10, fire 10; **SR** 19

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Heavy mace|heavy mace]]_ +14/+9 (1d8+4 plus 1d6 fire)
**Special Attacks** _[[spells/Brand|brand]]_ of the impenitent
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_detect evil_
At will—aid, _[[spells/Dispel Evil|dispel evil]]_ (DC 19), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Holy Smite|holy smite]]_ (DC 18), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Plane Shift|plane shift]]_ (self only), _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_
3/day—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Hold Person|hold person]]_ (DC 16)
1/day—_[[spells/Atonement|atonement]]_, _[[spells/Mark of Justice|mark of justice]]_

##### Statistics
**Str** 17, **Dex** 15, **Con** 18, **Int** 13, **Wis** 16, **Cha** 18
**Base Atk** +10; **CMB** +13; **CMD** 26
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +15, Diplomacy +17, Fly +19, Knowledge (planes) +14, Knowledge (religion) +14, Perception +16, Sense Motive +16
**Languages** Celestial, Draconic, Infernal; truespeech

##### Ecology

**Environment** any good-aligned planes
**Organization** solitary
**Treasure** double (+1 _flaming_ _heavy mace_, other treasure)

### Special Abilities

**_Brand_ of the Impenitent (Su)** Three times per day, a balisse can _brand_ a target within 30 feet (Will DC 19 negates) with a painless, glowing icon on its chest—usually the holy symbol of the deity or empyreal lord the balisse serves. This _brand_ lasts for a number of days equal to the balisse’s Hit Dice (10 days for most balisses). Anyone who attacks the branded target gains a +2 _[[items/Weapon Magic Abilities/Sacred|sacred]]_ bonus on weapon attack and damage rolls and a +2 _sacred_ bonus on caster level checks to overcome the target’s _[[universal monster rules/Spell Resistance|spell resistance]]_. The save DC is Charisma-based.

##### Description

Balisses, sometimes _[[items/Weapon Magic Abilities/Called|called]]_ confessor angels, appear to good individuals on the horns of moral dilemmas or who are struggling with crises of faith. Though balisses may appear stern and unyielding, they prefer to guide individuals to their own moral decisions rather than ordering them to conform to a specific ideal of good, knowing that the goodness found on one’s own is stronger than mere obedience. Balisses are formed from the souls of individuals who committed evil acts but were later _[[items/Weapon Magic Abilities/Redeemed|redeemed]]_ and died while living an exemplary, moral life.

Some balisses seek out mortals in need of their help, while others are given specific assignments by deities or empyreal lords. Balisses are used to dealing with stubbornness, and have an eternity’s worth of patience. Though they brook no physical attacks, they can endure almost any other hostility for the sake of their mission.

The average balisse is 7 feet tall and weighs 200 pounds.