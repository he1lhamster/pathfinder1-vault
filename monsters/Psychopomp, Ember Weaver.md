---
cssclass: [monsters]
title1: Psychopomp, Ember Weaver
desc_short: This slim, glowing figure is draped with voluminous gossamer shawls and
  veils that obscure its shape.
title2: Ember Weaver
CR: 8
sources:
- name: Monster Summoner's Handbook
  page: 25
  link: http://paizo.com/products/btpy9ela?Pathfinder-Player-Companion-Monster-Summoners-Handbook
XP: 4800
alignment: N
size: Medium
type: outsider
subtypes:
- psychopomp
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  spiritsense: 60
auras:
- name: eerie radiance
  radius: 300
  DC: 19
AC:
  AC: 22
  touch: 16
  flat_footed: 16
  components:
    dex: 5
    dodge: 1
    natural: 6
HP:
  HP: 104
  long: 11d8+55
saves:
  fort: 11
  ref: 8
  will: 12
DR:
- amount: 10
  weakness: adamantine
immunities:
- charm
- death effects
- disease
- fire
- poison
- spells with the light descriptor
resistances:
  cold: 10
  electricity: 10
SR: 19
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 touches +15 (4d6 fire)
      entries:
      - - damage: 4d6
          type: fire
      count: 2
      attack: touches
      bonus:
      - 15
  special:
  - rush of souls
spell_like_abilities:
  entries:
  - name: continual flame
    source: default
    freq: At will
  - name: dancing lights
    source: default
    freq: At will
    DC: 14
  - name: searing light
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 19
  - name: whispering wind
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: 1/day
  - name: freedom of movement
    source: default
    freq: 1/day
  - name: fly
    source: default
    freq: 1/day
  - name: locate creature
    source: default
    freq: 1/day
  - name: plane shift
    source: default
    freq: 1/day
  - name: slay living
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 19
  DEX: 21
  CON: 18
  INT: 18
  WIS: 21
  CHA: 18
BAB: 11
CMB: 15
CMD: 30
feats:
- name: Ability Focus (suggestion)
- name: Dodge
- name: Flyby Attack
- name: Mobility
- name: Toughness
skills:
  Acrobatics: 19
  Fly: 23
  Knowledge (geography): 18
  Knowledge (planes): 18
  Knowledge (religion): 18
  Perception: 19
  Sense Motive: 19
  Spellcraft: 18
  Survival: 19
languages:
- Abyssal
- Celestial
- Infernal
special_qualities:
- spirit touch
ecology:
  environment: any (Astral Plane)
  organization: solitary, pair, escort (1 ember weaver and 1 shoki), troupe (1 ember
    weaver plus 3-10 ahmuuths, catrinas, esoboks, or nosois), or procession (3-12
    ember weavers)
  treasure_type: standard
special_abilities:
  Eerie Radiance (Su): As a standard action, an ember weaver can wreath itself in
    an aura of cinders similar to dancing lights (CL 11th). Any living or dead creature
    within 300 feet with line of sight to the dancing embers must succeed at a DC
    19 Will save or else any protections or immunities it has against charm, fear,
    and mind-affecting effects are suppressed for as long as the ember weaver uses
    a free action to maintain the effect each round and for 1 round thereafter. Once
    a creature succeeds at this saving throw, it can't be affected by an eerie radiance
    for 24 hours. The light has no effect on psychopomps, creatures that can't see,
    and creatures the ember weaver chooses to exclude. This is a sight-based abjuration
    effect.
  Rush of Souls (Su): As a standard action every 1d4+1 rounds, an ember weaver can
    call forth a rush of souls to trample its foes. This ability deals 6d6 points
    of force damage to all creatures in a 60-foot cone. A successful DC 19 Reflex
    saving throw halves the damage. The save DC is Charisma-based.
desc_long: |-
  Ember weavers are beacons for dead souls seeking the afterlife, and escorts for other psychopomps. Most ember weavers patrol graveyards, ley lines, and other places where the dead enter into the river of souls, beckoning them to step toward eternity. Ember weavers also perform services in payment for knowledge about lost souls.

   Ember weavers lead ahmuuths and esoboks in hunts for spirits waylaid by undeath. They also accompany nosois and catrinas to recover confused or rebellious spirits.

---

# Psychopomp, Ember Weaver
This slim, glowing figure is draped with voluminous gossamer shawls and veils that obscure its shape.
**Source** Monster _[[classes/Summoner|Summoner]]_'s Handbook pg. 25
**XP** 4,800

N Medium outsider (psychopomp, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, spiritsense 60 ft.; Perception +19
**Aura** eerie _[[items/Weapon/Radiance|radiance]]_ (300 ft., DC 19)

##### Defense

**AC** 22, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 104 (11d8+55)
**Fort** +11, **Ref** +8, **Will** +12
**DR** 10/adamantine; **Immune** charm, death effects, disease, fire, poison, spells with the light descriptor; **Resist** cold 10, electricity 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 touches +15 (4d6 fire)
**Special Attacks** rush of souls
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
At will—_[[spells/Continual Flame|continual flame]]_, _[[spells/Dancing Lights|dancing lights]]_ (DC 14), _[[spells/Searing Light|searing light]]_, _[[spells/Suggestion|suggestion]]_ (DC 19), _[[spells/Whispering Wind|whispering wind]]_
1/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Freedom of Movement|freedom of movement]]_, fly, _[[spells/Locate Creature|locate creature]]_, _[[spells/Plane Shift|plane shift]]_, _[[spells/Slay Living|slay living]]_ (DC 19)

##### Statistics
**Str** 19, **Dex** 21, **Con** 18, **Int** 18, **Wis** 21, **Cha** 18
**Base Atk** +11; **CMB** +15; **CMD** 30
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_suggestion_), _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +19, Fly +23, Knowledge (geography) +18, Knowledge (planes) +18, Knowledge (religion) +18, Perception +19, Sense Motive +19, Spellcraft +18, Survival +19
**Languages** Abyssal, Celestial, Infernal
**SQ** spirit touch

##### Ecology

**Environment** any (Astral Plane)
**Organization** solitary, pair, escort (1 ember weaver and 1 shoki), troupe (1 ember weaver plus 3–10 ahmuuths, catrinas, esoboks, or nosois), or procession (3–12 ember weavers)
**Treasure** standard

### Special Abilities

**Eerie _Radiance_ (Su)** As a standard action, an ember weaver can wreath itself in an aura of cinders similar to _dancing lights_ (CL 11th). Any living or dead creature within 300 feet with line of sight to the _[[items/Weapon Magic Abilities/Dancing|dancing]]_ embers must succeed at a DC 19 Will save or else any protections or immunities it has against charm, _[[universal monster rules/Fear|fear]]_, and mind-affecting effects are suppressed for as long as the ember weaver uses a free action to maintain the effect each round and for 1 round thereafter. Once a creature succeeds at this saving throw, it can’t be affected by an eerie _radiance_ for 24 hours. The light has no effect on psychopomps, creatures that can’t see, and creatures the ember weaver chooses to exclude. This is a sight-based abjuration effect.

**Rush of Souls (Su)** As a standard action every 1d4+1 rounds, an ember weaver can call forth a rush of souls to _[[universal monster rules/Trample|trample]]_ its foes. This ability deals 6d6 points of force damage to all creatures in a 60-foot cone. A successful DC 19 Reflex saving throw halves the damage. The save DC is Charisma-based.

##### Description

Ember weavers are beacons for dead souls seeking the afterlife, and escorts for other psychopomps. Most ember weavers patrol graveyards, ley lines, and other places where the dead enter into the river of souls, beckoning them to step toward eternity. Ember weavers also perform services in payment for knowledge about lost souls.

Ember weavers lead ahmuuths and esoboks in hunts for spirits waylaid by undeath. They also accompany nosois and catrinas to recover _[[conditions/Confused|confused]]_ or rebellious spirits.