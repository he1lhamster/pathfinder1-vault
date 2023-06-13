---
cssclass: [monsters]
title1: Cetus
desc_short: This enormous scaled serpent has the head of a shark, powerful claws,
  and a maw wide enough to swallow a small ship.
title2: Cetus
CR: 13
sources:
- name: Bestiary 5
  page: 54
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 25600
alignment: CN
size: Colossal
type: dragon
subtypes:
- aquatic
- water
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
  tremorsense: 120
auras:
- name: mariner's misfortune
  radius: 30
AC:
  AC: 28
  touch: 16
  flat_footed: 22
  components:
    deflection: 8
    dex: 5
    dodge: 1
    natural: 12
    size: -8
HP:
  HP: 184
  long: 16d12+80
  regeneration: 10
  regeneration_weakness: petrification
saves:
  fort: 17
  ref: 15
  will: 14
  other: -4 vs. petrification
defensive_abilities:
- ocean's aegis
DR:
- amount: 5
  weakness: '-'
immunities:
- paralysis
- sleep
SR: 24
weaknesses:
- vulnerable to petrification
speeds:
  base: 20
  swim: 120
attacks:
  melee:
  - - text: bite +26 (6d6+27 plus grab)
      entries:
      - - damage: 6d6+27
        - effect: grab
      attack: bite
      bonus:
      - 26
  special:
  - constrict (6d6+27)
  - dispelling bite
  - fast swallow
  - impossible leap
  - rake (2 claws +26, 4d6+18)
  - swallow whole (8d6+24 damage, AC 17, 20 hp)
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: quickened control water
    source: default
    freq: At will
  - name: control winds
    source: default
    freq: At will
  - name: control weather
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 15
    concentration: 23
ability_scores:
  STR: 46
  DEX: 21
  CON: 20
  INT: 5
  WIS: 18
  CHA: 27
BAB: 16
CMB: 42
CMB_other: +46 grapple
CMD: 66
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Deflect Arrows
- name: Dodge
- name: Great Fortitude
- name: Greater Vital Strike
- name: Improved Vital Strike
- name: Mobility
- name: Quicken Spell-Like Ability (control water)
- name: Vital Strike
skills:
  Acrobatics: 15
  Intimidate: 16
  Perception: 23
  Stealth: 3
  Survival: 12
  Swim: 30
languages:
- Aquan
- Draconic
special_qualities:
- amphibious
ecology:
  environment: any oceans
  organization: solitary
  treasure_type: triple
special_abilities:
  Dispelling Bite (Su): The magically infused sea salt in a cetus's bite tears at
    some types of magic. Any time a cetus bites a creature under an effect or using
    a magic item that prevents that creature from being grappled-such as freedom of
    movement-or that holds the creature aloft-such as fly or air walk-each such effect
    is affected by a targeted dispel magic. The cetus treats its Hit Dice as its caster
    level for this effect.
  Impossible Leap (Su): A cetus can uncoil upward, revealing more length than it seems
    it could possibly possess while soaring to great heights. As a full-round action,
    it can leap out of the water toward a creature up to 1,200 feet in the air and
    make a bite attack against that creature before coiling down and returning to
    its original space. This leap provokes attacks of opportunity.
  Mariner's Misfortune (Su): Being near a cetus is bad luck for non-aquatic creatures.
    Any such creature in the cetus's aura must attempt a DC 26 Will save, rolling
    twice and taking the lower result. On a failed save, that creature must continue
    to roll twice and take the lower result on all ability checks, attacks rolls,
    savings throws, and skill checks for as long as it remains within the cetus's
    aura and for 1 minute thereafter. A creature that succeeds at its saving throw
    is immune to that cetus's mariner's misfortune for 24 hours. The save DC is Charisma-based.
  Ocean's Aegis (Su): The sea itself protects a cetus. A cetus gains a deflection
    bonus to AC equal to its Charisma bonus while any part of it is in water.
  Vulnerable to Petrification (Su): A cetus takes a -4 penalty on saving throws against
    petrification, and even on a successful save against petrification takes 1d4 points
    of Dexterity damage. If its Dexterity damage from petrification ever exceeds its
    Dexterity, a cetus becomes petrified. Being targeted with a petrification effect
    suppresses a cetus's regeneration for 1 minute, even if the creature succeeds
    at its save.
desc_long: |-
  Masters of the oceans, the enigmatic cetuses are mighty but slow-witted dragons who demand tribute of any who would dare enter their domain. A cetus's length and weight are immense, their dizzying coils proving almost impossible to count. Sailors have long told tales of these great creatures, noting that they are almost unstoppable unless they can be turned to stone and left to sink into the ocean depths.

  Cetuses prefer to fight their enemies on or under the water, but can leap unexpectedly high to attack foes who dare to take to the air.

---

# Cetus
This enormous scaled serpent has the head of a _[[monsters/Shark|shark]]_, powerful claws, and a maw wide enough to swallow a small ship.
**Source** Bestiary 5 pg. 54
**XP** 25,600

CN Colossal dragon (aquatic, water)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +23
**Aura** mariner’s misfortune (30 ft.)

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+8 deflection, +5 Dex, +1 _[[feats/Dodge|Dodge]]_, +12 natural, -8 size)
**hp** 184 (16d12+80); _[[universal monster rules/Regeneration|regeneration]]_ 10 (petrification)
**Fort** +17, **Ref** +15, **Will** +14; -4 vs. petrification
**Defensive Abilities** ocean’s _[[items/Shield/Aegis|aegis]]_; **DR** 5/—; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 24
**Weaknesses** vulnerable to petrification

##### Offense
**Speed** 20 ft., swim 120 ft.
**Melee** bite +26 (6d6+27 plus _[[universal monster rules/Grab|grab]]_)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (6d6+27), _[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ bite, _[[universal monster rules/Fast Swallow|fast swallow]]_, impossible leap, _[[universal monster rules/Rake|rake]]_ (2 claws +26, 4d6+18), _[[universal monster rules/Swallow Whole|swallow whole]]_ (8d6+24 damage, AC 17, 20 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15; concentration +23)
At will—quickened _[[spells/Control Water|control water]]_, _[[spells/Control Winds|control winds]]_
1/day—_[[spells/Control Weather|control weather]]_

##### Statistics
**Str** 46, **Dex** 21, **Con** 20, **Int** 5, **Wis** 18, **Cha** 27
**Base Atk** +16; **CMB** +42 (+46 grapple); **CMD** 66 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_control water_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +15, Intimidate +16, Perception +23, Stealth +3, Survival +12, Swim +30
**Languages** Aquan, Draconic
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** any oceans
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Dispelling_ Bite (Su)** The magically infused sea salt in a _[[monsters/Cetus|cetus]]_’s bite tears at some types of magic. Any time a _cetus_ bites a creature under an effect or using a magic item that prevents that creature from being _[[conditions/Grappled|grappled]]_—such as _[[spells/Freedom of Movement|freedom of movement]]_—or that holds the creature aloft—such as fly or _[[spells/Air Walk|air walk]]_—each such effect is affected by a targeted _[[spells/Dispel Magic|dispel magic]]_. The _cetus_ treats its Hit Dice as its caster level for this effect.

**Impossible Leap (Su)** A _cetus_ can uncoil upward, revealing more length than it seems it could possibly possess while soaring to great heights. As a full-round action, it can leap out of the water toward a creature up to 1,200 feet in the air and make a bite attack against that creature before coiling down and returning to its original space. This leap provokes attacks of opportunity.

**Mariner’s Misfortune (Su)** Being near a _cetus_ is bad luck for non-aquatic creatures. Any such creature in the _cetus_’s aura must attempt a DC 26 Will save, rolling twice and taking the lower result. On a failed save, that creature must continue to roll twice and take the lower result on all ability checks, attacks rolls, savings throws, and skill checks for as long as it remains within the _cetus_’s aura and for 1 minute thereafter. A creature that succeeds at its saving throw is immune to that _cetus_’s mariner’s misfortune for 24 hours. The save DC is Charisma-based.

**Ocean’s _Aegis_ (Su)** The sea itself protects a _cetus_. A _cetus_ gains a _deflection_ bonus to AC equal to its Charisma bonus while any part of it is in water.

**Vulnerable to Petrification (Su)** A _cetus_ takes a -4 penalty on saving throws against petrification, and even on a successful save against petrification takes 1d4 points of Dexterity damage. If its Dexterity damage from petrification ever exceeds its Dexterity, a _cetus_ becomes _[[conditions/Petrified|petrified]]_. Being targeted with a petrification effect suppresses a _cetus_’s _regeneration_ for 1 minute, even if the creature succeeds at its save.

##### Description

Masters of the oceans, the enigmatic cetuses are mighty but slow-witted dragons who _[[spells/Demand|demand]]_ tribute of any who would dare enter their domain. A _cetus_’s length and weight are immense, their dizzying coils proving almost impossible to count. Sailors have long told tales of these great creatures, noting that they are almost unstoppable unless they can be turned to stone and left to sink into the ocean depths.

Cetuses prefer to fight their enemies on or under the water, but can leap unexpectedly high to attack foes who dare to take to the air.