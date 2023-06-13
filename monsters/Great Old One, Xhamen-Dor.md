---
cssclass: [monsters]
title1: Great Old One, Xhamen-Dor
desc_short: A hideous tangle of hairlike fungal filaments writhes with nauseating
  purpose. Bones lie tangled in the wriggling mass, arrayed around a central draconic
  skull.
title2: Xhamen-Dor
CR: 26
sources:
- name: 'Pathfinder #113: What Grows Within'
  page: 86
  link: http://paizo.com/products/btpy9qcl?Pathfinder-Adventure-Path-113-What-Grows-Within
XP: 2457600
alignment: NE
size: Gargantuan
type: plant
subtypes:
- aquatic
- evil
- Great Old One
initiative:
  bonus: 24
senses:
  blindsight: 60
  low-light vision: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 31
AC:
  AC: 44
  touch: 26
  flat_footed: 34
  components:
    dex: 10
    insight: 10
    natural: 18
    size: -4
HP:
  HP: 602
  long: 28d8+476
  fast_healing: 20
saves:
  fort: 33
  ref: 21
  will: 20
defensive_abilities:
- all-around vision
- amorphous
- immortality
- insanity (DC 31)
DR:
- amount: 15
  weakness: epic and slashing
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- energy drain
- mind-affecting effects
- paralysis
- petrification
- plant traits
- poison
resistances:
  acid: 30
  fire: 30
SR: 37
speeds:
  base: 40
  other_semicolon: air walk
  climb: 40
  swim: 60
attacks:
  melee:
  - - text: 4 tentacles +35 (3d6+18/19-20 plus grab)
      entries:
      - - damage: 3d6+18
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 35
    - text: bite +35 (4d8+18/19-20 plus dread decay)
      entries:
      - - damage: 4d8+18
          crit_range: 19-20
        - effect: dread decay
      attack: bite
      bonus:
      - 35
  special:
  - constrict (3d6+13)
  - entangling shroud
  - infected dreams
  - mythic power (10/day, surge +1d12)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: greater magic fang
    source: default
    freq: Constant
  - is_mythic_spell: true
    name: animate dead
    source: default
    freq: At will
  - name: control undead
    source: default
    freq: At will
    DC: 24
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 22
  - is_mythic_spell: true
    name: wall of thorns
    source: default
    freq: At will
  - name: control plants
    source: default
    freq: 3/day
    DC: 25
  - name: create greater undead
    source: default
    freq: 3/day
  - name: create undead
    source: default
    freq: 3/day
  - name: demand
    source: default
    freq: 3/day
    DC: 25
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 22
  - name: quickened wither limb
    source: default
    freq: 3/day
    DC: 23
  - name: cursed earth
    source: default
    freq: 1/day
  - name: microcosm
    source: default
    freq: 1/day
    DC: 26
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 26
    concentration: 33
ability_scores:
  STR: 36
  DEX: 30
  CON: 45
  INT: 19
  WIS: 28
  CHA: 25
BAB: 21
CMB: 38
CMD: 68
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Critical (tentacle)
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Quicken Spell-Like Ability (wither limb)
- name: Staggering Critical
- name: Vital Strike
skills:
  Climb: 21
  Knowledge (arcana): 18
  Knowledge (geography): 18
  Knowledge (nature): 32
  Knowledge (religion): 32
  Perception: 40
  Spellcraft: 32
  Swim: 52
languages:
- Aklo
- telepathy 100 ft.
special_qualities:
- amphibious
- compression
- contagious lore
- no breath
- powerful tentacles
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Contagious Lore (Su): Any creature that learns Xhamen-Dor's name and comprehends
    the Great Old One's nature as an insidious parasite (this typically requires a
    creature to be exposed to information in a book or to be taught the information,
    but also automatically affects any creature who succeeds at a Knowledge check
    to learn more about the Great Old One) is at risk of being targeted by Xhamen-Dor's
    infectious dreams. Every year, there is a flat 1% chance that such a creature
    can be targeted by the Great Old One's infected dream ability. If 5 years pass
    without being targeted, the victim “forgets” about Xhamen-Dor until taught of
    the Great Old One again. A miracle or wish can spell also cause someone to forget
    in this way.
  Dread Decay (Su): A creature damaged by Xhamen- Dor's bite becomes afflicted by
    a fast-acting infection that swiftly rots flesh and bone into a foul-smelling
    gangrenous slop. The bitten creature must succeed at a DC 41 Fortitude saving
    throw or take 2d6 points of Strength drain and 2d6 points of Constitution drain.
    On a successful save, the victim takes only 2 points of Strength drain and 2 points
    of Constitution drain. A creature whose Strength score is reduced to 0 by this
    effect falls comatose and immediately experiences infected dreams (see below).
    A creature whose Constitution score is reduced to 0 by this effect is immediately
    absorbed into Xhamen-Dor's body, along with its memories, mind, and soul. Such
    a creature cannot be restored to life except via wish or miracle. Even then a
    creature brought back to life in this manner experiences infected dreams (see
    page 87). This is a disease effect. The save DC is Constitution-based.
  Entangling Shroud (Su): Xhamen-Dor is surrounded by a writhing storm of fungal filaments
    that fills an area equal to his reach. While these filaments are almost microscopic
    in width, they are quite strong and capable of swatting aside ranged weapon attacks,
    granting Xhamen-Dor a 50% miss chance against all such attacks. In addition, any
    creature that ends its turn within Xhamen-Dor's reach must succeed at a DC 37
    Reflex saving throw or become entangled as long as it remains in that area. An
    entangled creature can try to break free as a move action; the DC of the Strength
    or Escape Artist check is equal to that of the Reflex save to avoid becoming entangled
    in the first place. The save DC is Strength-based.
  Great Old One Traits: Rules for Xhamen-Dor's Great Old One traits like immortality,
    insanity, its mythic abilities, otherworldly insight, and the base rules for unspeakable
    presence can be found on page 306 of Pathfinder RPG Bestiary 4.
  Immortality (Ex): 'If Xhamen-Dor is slain, its body collapses into a reeking pile
    of fungus, hair, and bones. The core of its being compresses down to a tiny blot
    of incorporeal fungal matter that is immediately expelled from the core of its
    mass and hurled out into the depths of space. All creatures within 120 feet of
    Xhamen-Dor when this occurs must succeed at a DC 31 Fortitude saving throw or
    take 2d6 points of Charisma drain as portions of their sanity and souls are pulled
    along with the blot. Xhamen-Dor's remains animate as a unique undead creature
    known as a seeded 24 hours after this event (see page 90 for statistics), but
    this is merely an echo of the Great Old One. Xhamen-Dor is reborn again when one
    of two events occur: the blot fired into space impacts a planet, or one of its
    surviving seeded returns to Carcosa and resurrects as the Great Old One. If the
    former, it can be centuries or even eons before Xhamen-Dor awakens again, but
    if the latter, the Great Old One can return within a matter of months or less.
    The save DC is Charisma-based.'
  Infected Dreams (Su): |-
    Any knowledgeable creature that has succumbed to the yearly 1% chance of Xhamen-Dor's contagious lore ability (see page 86) or whose Strength score has been drained to 0 by dread decay (see page 86) can be targeted by the Great Old One's nightmare spell-like ability, regardless of the distance between the creature and Xhamen-Dor. In order to use infected dreams against a target, Xhamen-Dor must successfully affect that target with its nightmare spell-like ability. If the victim fails its saving throw against the nightmare, it becomes infected with the following virulent fungal blight.

    Seeded Infestation-save Fort DC 41; onset immediate; frequency 1/day; effect 1d4 Con drain; cure none. This infestation can be cured only by magic. A creature whose Constitution score is reduced to 0 by this infestation dies and rises in 1d4 rounds as a seeded creature (see page 90). This is an infestation effect. The save DC is Constitution-based.
  Powerful Tentacles (Su): Xhamen-Dor's tentacles are treated as primary natural attacks.
  Unspeakable Presence (Su): Failing a DC 31 Will saving throw against Xhamen-Dor's
    unspeakable presence causes a victim to become nauseated for 1d4 rounds, and then
    sickened for an additional 2d4 rounds. The save DC is Charisma-based.
desc_long: |-
  Spawned countless eons ago within the deepest tainted reservoirs hidden in the foul sewers of Carcosa, the fungal infestation known as Xhamen-Dor, the Inmost Blot, has traveled from world to world for ages untold, infesting reality and returning time and time again to its place of creation to expand the alien city's scope. Full details on this destructive agency of parasitism can be found on pages 62-67.

  Xhamen-Dor is an elephantine mass of fungus and hairlike tendrils capable of assuming any basic form, although its preferred shapes are that of a serpentine creature, a spiderweb-like tangle, or a shuddering carpet of filth.

---

# Great Old One, Xhamen-Dor
A hideous tangle of hairlike fungal filaments writhes with nauseating purpose. Bones lie tangled in the wriggling mass, arrayed around a central draconic skull.
**Source** Pathfinder #113: _[[spells/What Grows Within|What Grows Within]]_ pg. 86
**XP** 2,457,600

NE Gargantuan plant (aquatic, evil, Great Old One)
**Init** +24; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +40
**Aura** unspeakable presence (300 ft., DC 31)

##### Defense

**AC** 44, touch 26, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+10 Dex, +10 insight, +18 natural, –4 size)
**hp** 602 (28d8+476); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +33, **Ref** +21, **Will** +20
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Amorphous|amorphous]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 31); **DR** 15/epic and slashing; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, _[[universal monster rules/Plant Traits|plant traits]]_, poison; **Resist** acid 30, fire 30; **SR** 37

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft., swim 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 4 tentacles +35 (3d6+18/19–20 plus _[[universal monster rules/Grab|grab]]_), bite +35 (4d8+18/19–20 plus dread decay)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (3d6+13), entangling shroud, infected dreams, mythic power (10/day, surge +1d12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 26th; concentration +33)
Constant—_air walk_, greater _[[spells/Magic Fang|magic fang]]_
At will—_[[spells/Animate Dead|animate dead]]_, _[[spells/Control Undead|control undead]]_ (DC 24), _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Nightmare|nightmare]]_ (DC 22), _[[spells/Wall Of Thorns|wall of thorns]]_
3/day—_[[spells/Control Plants|control plants]]_ (DC 25), _[[spells/Create Greater Undead|create greater undead]]_, _[[spells/Create Undead|create undead]]_, _[[spells/Demand|demand]]_ (DC 25), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 22), quickened _[[spells/Wither Limb|wither limb]]_ (DC 23)
1/day—_[[spells/Cursed Earth|cursed earth]]_, _[[spells/Microcosm|microcosm]]_ (DC 26), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 25)

##### Statistics
**Str** 36, **Dex** 30, **Con** 45, **Int** 19, **Wis** 28, **Cha** 25
**Base Atk** +21; **CMB** +38; **CMD** 68
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (tentacle), _Improved Critical_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_, _wither limb_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _Climb_ +21, Knowledge (arcana) +18, Knowledge (geography) +18, Knowledge (nature) +32, Knowledge (religion) +32, Perception +40, Spellcraft +32, Swim +52
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Compression|compression]]_, contagious lore, _[[universal monster rules/No Breath|no breath]]_, powerful tentacles

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Contagious Lore (Su)** Any creature that learns Xhamen-Dor’s name and comprehends the Great Old One’s nature as an insidious parasite (this typically requires a creature to be exposed to information in a book or to be taught the information, but also automatically affects any creature who succeeds at a Knowledge check to learn more about the Great Old One) is at risk of being targeted by Xhamen-Dor’s infectious dreams. Every year, there is a flat 1% chance that such a creature can be targeted by the Great Old One’s infected _dream_ ability. If 5 years pass without being targeted, the victim “forgets” about Xhamen-Dor until taught of the Great Old One again. A _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ can spell also cause someone to forget in this way.

**Dread Decay (Su)** A creature damaged by Xhamen- Dor’s bite becomes afflicted by a fast-acting infection that swiftly rots flesh and bone into a foul-smelling gangrenous slop. The bitten creature must succeed at a DC 41 Fortitude saving throw or take 2d6 points of Strength drain and 2d6 points of Constitution drain. On a successful save, the victim takes only 2 points of Strength drain and 2 points of Constitution drain. A creature whose Strength score is reduced to 0 by this effect falls comatose and immediately experiences infected dreams (see below). A creature whose Constitution score is reduced to 0 by this effect is immediately absorbed into Xhamen-Dor’s body, along with its memories, mind, and soul. Such a creature cannot be restored to life except via _wish_ or _miracle_. Even then a creature brought back to life in this manner experiences infected dreams (see page 87). This is a disease effect. The save DC is Constitution-based.

**Entangling Shroud (Su)** Xhamen-Dor is surrounded by a writhing storm of fungal filaments that fills an area equal to his reach. While these filaments are almost microscopic in width, they are quite strong and capable of swatting aside ranged weapon attacks, granting Xhamen-Dor a 50% miss chance against all such attacks. In addition, any creature that ends its turn within Xhamen-Dor’s reach must succeed at a DC 37 Reflex saving throw or become _[[conditions/Entangled|entangled]]_ as long as it remains in that area. An _entangled_ creature can try to break free as a move action; the DC of the Strength or Escape Artist check is equal to that of the Reflex save to avoid becoming _entangled_ in the first place. The save DC is Strength-based.

**Great Old One Traits** Rules for Xhamen-Dor’s Great Old One traits like immortality, _insanity_, its mythic abilities, otherworldly insight, and the base rules for unspeakable presence can be found on page 306 of Pathfinder RPG Bestiary 4.

**Immortality (Ex)** If Xhamen-Dor is slain, its body collapses into a reeking pile of fungus, hair, and bones. The core of its being compresses down to a tiny _[[spells/Blot|blot]]_ of _[[universal monster rules/Incorporeal|incorporeal]]_ fungal matter that is immediately expelled from the core of its mass and hurled out into the depths of space. All creatures within 120 feet of Xhamen-Dor when this occurs must succeed at a DC 31 Fortitude saving throw or take 2d6 points of Charisma drain as portions of their sanity and souls are pulled along with the _blot_. Xhamen-Dor’s remains animate as a unique undead creature known as a seeded 24 hours after this event (see page 90 for statistics), but this is merely an _[[spells/Echo|echo]]_ of the Great Old One. Xhamen-Dor is reborn again when one of two events occur: the _blot_ fired into space impacts a planet, or one of its surviving seeded returns to Carcosa and resurrects as the Great Old One. If the former, it can be centuries or even eons before Xhamen-Dor awakens again, but if the latter, the Great Old One can return within a matter of months or less. The save DC is Charisma-based.

**Infected Dreams (Su)** Any knowledgeable creature that has succumbed to the yearly 1% chance of Xhamen-Dor’s contagious lore ability (see page 86) or whose Strength score has been drained to 0 by dread decay (see page 86) can be targeted by the Great Old One’s _nightmare_ spell-like ability, regardless of the distance between the creature and Xhamen-Dor. In order to use infected dreams against a target, Xhamen-Dor must successfully affect that target with its _nightmare_ spell-like ability. If the victim fails its saving throw against the _nightmare_, it becomes infected with the following _[[items/Weapon Magic Abilities/Virulent|virulent]]_ fungal _[[spells/Blight|blight]]_.

Seeded Infestation—save Fort DC 41; onset immediate; frequency 1/day; effect 1d4 Con drain; cure none. This infestation can be cured only by magic. A creature whose Constitution score is reduced to 0 by this infestation dies and rises in 1d4 rounds as a seeded creature (see page 90). This is an infestation effect. The save DC is Constitution-based.

**Powerful Tentacles (Su)** Xhamen-Dor’s tentacles are treated as primary _[[universal monster rules/Natural Attacks|natural attacks]]_.

**Unspeakable Presence (Su)** Failing a DC 31 Will saving throw against Xhamen-Dor’s unspeakable presence causes a victim to become _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds, and then _[[conditions/Sickened|sickened]]_ for an additional 2d4 rounds. The save DC is Charisma-based.

##### Description

Spawned countless eons ago within the deepest tainted reservoirs hidden in the foul sewers of Carcosa, the _[[spells/Fungal Infestation|fungal infestation]]_ known as Xhamen-Dor, the Inmost _Blot_, has traveled from world to world for ages untold, infesting reality and returning time and time again to its place of creation to expand the alien city’s scope. Full details on this destructive agency of parasitism can be found on pages 62–67.

Xhamen-Dor is an elephantine mass of fungus and hairlike tendrils capable of assuming any basic form, although its preferred shapes are that of a serpentine creature, a spiderweb-like tangle, or a shuddering carpet of filth.