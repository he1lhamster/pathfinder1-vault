---
cssclass: [monsters]
title1: Dweomercat
title2: Dweomercat
CR: 7
sources:
- name: 'Pathfinder #36: Sound of a Thousand Screams'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7x
XP: 3200
alignment: CN
size: Medium
type: magical beast
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 23
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    dodge: 1
    natural: 6
HP:
  HP: 85
  long: 10d10+30
saves:
  fort: 10
  ref: 13
  will: 6
DR:
- amount: 5
  weakness: magic
SR: 19
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 claws +16 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: claws
      bonus:
      - 16
    - text: bite +16 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: bite
      bonus:
      - 16
  special:
  - dweomer leap
  - pounce
  - rake (2 claws +11, 1d4+2)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: lesser globe of invulnerability
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: 3/day
    other: self only
  - name: antimagic field
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 10
ability_scores:
  STR: 15
  DEX: 23
  CON: 16
  INT: 13
  WIS: 16
  CHA: 16
BAB: 10
CMB: 12
CMD: 29
CMD_other: 33 vs. trip
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Spring Attack
- name: Weapon Finesse
skills:
  Climb: 6
  Knowledge (arcana): 11
  Perception: 16
  Stealth: 19
  _racial_mods:
    Climb:
      _: 4
languages:
- Common
- Sylvan
special_qualities:
- spell link
ecology:
  environment: any forest (First World)
  organization: solitary, hunt (2-3), ambush (1-3 dweomercats and 2-12 dweomercat
    cubs)
  treasure_type: standard
special_abilities:
  Dweomer Leap (Su): When a dweomercat is targeted by a spell or within the area of
    effect of a spell, it can, as a swift action, choose to teleport to a square adjacent
    to the spell's caster, effectively appearing mid-leap and aimed toward the caster.
    This ability takes effect regardless of whether or not the spell overcomes the
    dweomercat's spell resistance. If it chooses, the dweomercat can immediately make
    a full attack against the spell's caster as though pouncing. Using this ability
    does not provoke an attack of opportunity. If there is no safe space adjacent
    to the caster-or if the dweomercat chooses-the dweomercat can forgo using this
    ability.
  Spell Link (Su): |-
    When a dweomercat is targeted by a spell or within the area of effect of a spell, it can, as a swift action, forgo its dweomer leap ability to gain an effect related to the school of the spell targeting it. This effect activates before the dweomercat is affected by the spell targeting it and regardless of whether or not the spell overcomes its spell resistance. Each power lasts for 1 minute per level of the spell targeting the dweomercat, until the dweomercat uses this ability again, or until the dweomercat chooses to dismiss the effect as a free action, whichever duration is shortest. This ability does not prevent the spell affecting the dweomercat from taking effect; it only provides an additional benefit.

    Abjuration: Gains acid, cold, fire, electricity, or sonic resistance equal to 2 per spell level.
    Conjuration: Gains a deflection bonus to AC equal to +1 for every 5 levels of the spell.
    Divination: Gains the effects of detect chaos, evil, good, or law.
    Enchantment: Grants the effects of the spell heroism.
    Evocation: Inflicts an amount of damage equal to the spell's level upon the spell's caster.
    Illusion: Grants the effects of invisibility. This effect ends as per the spell.
    Necromancy: Gains the effects of false life, as if cast by the opposing spell's caster.
    Transmutation: Gains an enhancement bonus on its natural weapons equal to +1 for every 5 levels of the spell.

    Powerful and regal, dweomercats stalk the First World, preying upon lesser creatures, but more voraciously hunting new and ever stranger sources of magic. Beings as much composed of sculpted arcane eddies as of flesh and blood, these capricious felines flourish along the intangible ley lines of their home realm, drinking in its weird powers as a plant thrives on light. Yet even more potent than their thirst for magic and the euphoria they draw from being in proximity to the reshaping of reality is dweomercats' racial curiosity, which leads them endlessly across the First World-and often beyond.

    The average adult dweomercat is about 4 feet tall and 7 feet long, weighing over 250 pounds, while their cubs are approximately 1 foot tall and weigh no more than 15 pounds.
desc_long: ''

---

# Dweomercat

**Source** Pathfinder #36: Sound of a Thousand Screams pg. 82
**XP** 3,200

CN Medium magical beast
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +16

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 85 (10d10+30)
**Fort** +10, **Ref** +13, **Will** +6
**DR** 5/magic; **SR** 19

##### Offense
**Speed** 40 ft.
**Melee** 2 claws +16 (1d4+2), bite +16 (1d6+2)
**Special Attacks** dweomer leap, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +11, 1d4+2)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
Constant - _[[spells/Detect Magic|detect magic]]_
At will - lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, _[[spells/Dispel Magic|dispel magic]]_
3/day - _[[spells/Dimension Door|dimension door]]_ (self only), _[[spells/Antimagic Field|antimagic field]]_

##### Statistics
**Str** 15, **Dex** 23, **Con** 16, **Int** 13, **Wis** 16, **Cha** 16
**Base Atk** +10; **CMB** +12; **CMD** 29 (33 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +6, Knowledge (arcana) +11, Perception +16, Stealth +19; **Racial Modifiers** +4 _Climb_
**Languages** Common, Sylvan
**SQ** spell link

##### Ecology

**Environment** any forest (First World)
**Organization** solitary, hunt (2-3), ambush (1-3 dweomercats and 2-12 _[[monsters/Dweomercat|dweomercat]]_ cubs)
**Treasure** standard

### Special Abilities

**Dweomer Leap (Su)** When a _dweomercat_ is targeted by a spell or within the area of effect of a spell, it can, as a swift action, choose to teleport to a square adjacent to the spell’s caster, effectively appearing mid-leap and aimed toward the caster. This ability takes effect regardless of whether or not the spell overcomes the _dweomercat_’s _[[universal monster rules/Spell Resistance|spell resistance]]_. If it chooses, the _dweomercat_ can immediately make a full attack against the spell’s caster as though pouncing. Using this ability does not provoke an attack of opportunity. If there is no safe space adjacent to the caster—or if the _dweomercat_ chooses—the _dweomercat_ can forgo using this ability.
**Spell Link (Su)** When a _dweomercat_ is targeted by a spell or within the area of effect of a spell, it can, as a swift action, forgo its dweomer leap ability to gain an effect related to the school of the spell targeting it. This effect activates before the _dweomercat_ is affected by the spell targeting it and regardless of whether or not the spell overcomes its _spell resistance_. Each power lasts for 1 minute per level of the spell targeting the _dweomercat_, until the _dweomercat_ uses this ability again, or until the _dweomercat_ chooses to dismiss the effect as a free action, whichever duration is shortest. This ability does not prevent the spell affecting the _dweomercat_ from taking effect; it only provides an additional benefit.

Abjuration: Gains acid, cold, fire, electricity, or sonic _[[universal monster rules/Resistance|resistance]]_ equal to 2 per spell level.
Conjuration: Gains a _[[spells/Deflection|deflection]]_ bonus to AC equal to +1 for every 5 levels of the spell.
_[[spells/Divination|Divination]]_: Gains the effects of _[[spells/Detect Chaos|detect chaos]]_, evil, good, or law.
Enchantment: Grants the effects of the spell _[[spells/Heroism|heroism]]_.
Evocation: Inflicts an amount of damage equal to the spell’s level upon the spell’s caster.
Illusion: Grants the effects of _[[spells/Invisibility|invisibility]]_. This effect ends as per the spell.
Necromancy: Gains the effects of _[[spells/False Life|false life]]_, as if cast by the opposing spell’s caster.
Transmutation: Gains an enhancement bonus on its natural weapons equal to +1 for every 5 levels of the spell.

Powerful and regal, dweomercats stalk the First World, preying upon lesser creatures, but more voraciously hunting new and ever stranger sources of magic. Beings as much composed of sculpted arcane eddies as of flesh and blood, these capricious felines flourish along the intangible ley lines of their home realm, drinking in its _[[spells/Weird|weird]]_ powers as a plant thrives on light. Yet even more _[[items/Weapon Magic Abilities/Potent|potent]]_ than their thirst for magic and the euphoria they draw from being in proximity to the reshaping of reality is dweomercats’ racial curiosity, which leads them endlessly across the First World—and often beyond.

The average adult _dweomercat_ is about 4 feet tall and 7 feet long, weighing over 250 pounds, while their cubs are approximately 1 foot tall and weigh no more than 15 pounds.