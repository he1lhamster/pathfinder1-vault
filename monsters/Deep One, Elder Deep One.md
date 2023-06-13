---
cssclass: [monsters]
title1: Deep One, Elder Deep One
desc_short: The frame of this immense monstrosity is humanoid, but its ichthyic visage
  is that of a deep-sea predator.
title2: Elder Deep One
CR: 14
sources:
- name: Bestiary 5
  page: 69
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 38400
alignment: CE
size: Gargantuan
type: monstrous humanoid
subtypes:
- aquatic
- deep one
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: cloak of chaos
  DC: 22
- name: staggering presence
  radius: 180
  DC: 21
AC:
  AC: 29
  touch: 11
  flat_footed: 24
  components:
    deflection: 4
    dex: 1
    natural: 18
    size: -4
HP:
  HP: 202
  long: 15d8+135
  regeneration: 10
  regeneration_weakness: fire
saves:
  fort: 18
  ref: 16
  will: 19
defensive_abilities:
- mind reflection
DR:
- amount: 10
  weakness: magic and piercing
immunities:
- cold
- disease
resistances:
  acid: 10
  electricity: 10
SR: 25
speeds:
  base: 30
  swim: 60
attacks:
  melee:
  - - text: bite +24 (2d8+13/19-20)
      entries:
      - - damage: 2d8+13
          crit_range: 19-20
      attack: bite
      bonus:
      - 24
    - text: 2 claws +24 (2d6+13/19-20)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 24
  special:
  - Devastating Strike
  - staggering presence
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 22
  - name: freedom of movement
    source: default
    freq: Constant
  - name: dream
    source: default
    freq: At will
  - name: hold monster
    source: default
    freq: At will
    DC: 19
  - name: black tentacles
    source: default
    freq: 3/day
  - name: demand
    source: default
    freq: 3/day
    DC: 22
  - name: insanity
    source: default
    freq: 3/day
    DC: 21
  - name: nightmare
    source: default
    freq: 3/day
    DC: 19
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 23
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 22
  - name: binding
    source: default
    freq: 1/week
    DC: 22
  sources:
  - name: default
    CL: 14
    concentration: 18
ability_scores:
  STR: 36
  DEX: 12
  CON: 28
  INT: 19
  WIS: 23
  CHA: 19
BAB: 15
CMB: 32
CMB_other: +34 bull rush
CMD: 47
CMD_other: 49 vs. bull rush
feats:
- name: Awesome Blow
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Intimidate: 22
  Knowledge (arcana): 19
  Knowledge (religion): 19
  Perception: 24
  Sense Motive: 21
  Stealth: 7
  Swim: 39
  Use Magic Device: 19
languages:
- Aklo
- Common
special_qualities:
- amphibious
- deep dweller
- deific
- immortal
- item use
ecology:
  environment: any water
  organization: solitary or pair
  treasure_type: triple
special_abilities:
  Deep Dweller (Ex): Deep ones are immune to damage from water pressure; their bodies
    are capable of instantly adjusting to different water depths or even the surface
    with ease.
  Devastating Strike (Ex): An elder deep one ignores the first 10 points of hardness
    when it damages an object with its claws. A creature struck with a critical hit
    from an elder deep one's claw must succeed at a DC 30 Fortitude save or be stunned
    for 1 round. The save DC is Strength-based.
  Deific: An elder deep one can grant divine spells to its worshipers. Granting spells
    does not require any specific action on the elder deep one's behalf. Elder deep
    ones grant access to the domains of Chaos, Evil, Madness, and Water. Their symbols
    vary, but their favored weapon is the claw.
  Immortal (Ex): A deep one does not age. Barring death from violence, disease, or
    misadventure, a deep one can live forever. Deep ones are immune to effects that
    cause magical aging. A deep one does not age. Barring death from violence, disease,
    or misadventure, a deep one can live forever. Deep ones are immune to effects
    that cause magical aging.
  Item Use (Su): A deep one can activate spell-trigger items like staves and wands
    as if it were a spellcaster of the appropriate class.
  Mind Reflection (Ex): Any mind-affecting effect that fails to affect an elder deep
    one is reflected back on the source, affecting the original caster as if by spell
    turning, treating the elder deep one as the controller and source of the spell.
  Staggering Presence (Ex): This ability functions as frightful presence, except that
    a creature that fails its save is also staggered as long as it remains in the
    area of effect, and for an additional 1d6 rounds after leaving that area. This
    is a mind-affecting fear effect.
desc_long: A few deep ones never stop growing over the eons of their endless lives.
  Many elder deep ones claim the names of monsters or gods for their own-Mother Hydra
  and Father Dagon being two of the more legendary of their kind. Elder deep ones
  ascend to the status of near-gods in deep one society, towering over their kin and
  ruling their sunken cities. Just as they are worshiped, so do the elder deep ones
  worship the Great Old Ones and Outer Gods themselves.

---

# Deep One, Elder Deep One
The frame of this immense monstrosity is humanoid, but its ichthyic visage is that of a deep-sea predator.
**Source** Bestiary 5 pg. 69
**XP** 38,400
CE Gargantuan monstrous humanoid (aquatic, _[[monsters/Deep One|deep one]]_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 22), staggering presence (180 ft., DC 21)

##### Defense

**AC** 29, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 deflection, +1 Dex, +18 natural, -4 size)
**hp** 202 (15d8+135); _[[universal monster rules/Regeneration|regeneration]]_ 10 (fire)
**Fort** +18, **Ref** +16, **Will** +19
**Defensive Abilities** mind reflection; **DR** 10/magic and piercing; **Immune** cold, disease; **Resist** acid 10, electricity 10; **SR** 25

##### Offense
**Speed** 30 ft., swim 60 ft.
**Melee** bite +24 (2d8+13/19-20), 2 claws +24 (2d6+13/19-20)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[feats/Devastating Strike|Devastating Strike]]_, staggering presence
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +18)
Constant—_cloak of chaos_ (DC 22), _[[spells/Freedom of Movement|freedom of movement]]_
At will—_[[spells/Dream|dream]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19)
3/day—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Demand|demand]]_ (DC 22), _[[spells/Insanity|insanity]]_ (DC 21), _[[spells/Nightmare|nightmare]]_ (DC 19)
1/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 23), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 22)
1/week—_[[spells/Binding|binding]]_ (DC 22)

##### Statistics
**Str** 36, **Dex** 12, **Con** 28, **Int** 19, **Wis** 23, **Cha** 19
**Base Atk** +15; **CMB** +32 (+34 bull rush); **CMD** 47 (49 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Intimidate +22, Knowledge (arcana, religion) +19, Perception +24, Sense Motive +21, Stealth +7, Swim +39, Use Magic Device +19
**Languages** Aklo, Common
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, deep dweller, deific, immortal, item use

##### Ecology

**Environment** any water
**Organization** solitary or pair
**Treasure** triple

### Special Abilities

**Deep Dweller (Ex)** Deep ones are immune to damage from water pressure; their bodies are capable of instantly adjusting to different water depths or even the surface with ease.

**_Devastating Strike_ (Ex)** An elder _deep one_ ignores the first 10 points of hardness when it damages an object with its claws. A creature struck with a critical hit from an elder _deep one_’s claw must succeed at a DC 30 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1 round. The save DC is Strength-based.

**Deific** An elder _deep one_ can grant divine spells to its worshipers. Granting spells does not require any specific action on the elder _deep one_’s behalf. Elder deep ones grant access to the domains of Chaos, Evil, Madness, and Water. Their symbols vary, but their favored weapon is the claw.

**Immortal (Ex)** A _deep one_ does not age. Barring death from violence, disease, or misadventure, a _deep one_ can live forever. Deep ones are immune to effects that cause magical aging. A _deep one_ does not age. Barring death from violence, disease, or misadventure, a _deep one_ can live forever. Deep ones are immune to effects that cause magical aging.

**Item Use (Su)** A _deep one_ can activate spell-trigger items like staves and wands as if it were a spellcaster of the appropriate class.

**Mind Reflection (Ex)** Any mind-affecting effect that fails to affect an elder _deep one_ is reflected back on the source, affecting the original caster as if by _[[spells/Spell Turning|spell turning]]_, treating the elder _deep one_ as the controller and source of the spell.
**Staggering Presence (Ex)** This ability functions as _[[universal monster rules/Frightful Presence|frightful presence]]_, except that a creature that fails its save is also _[[conditions/Staggered|staggered]]_ as long as it remains in the area of effect, and for an additional 1d6 rounds after leaving that area. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect.

##### Description

A few deep ones never stop _[[items/Weapon Magic Abilities/Growing|growing]]_ over the eons of their endless lives. Many elder deep ones claim the names of monsters or gods for their own—Mother _[[monsters/Hydra|Hydra]]_ and Father Dagon being two of the more legendary of their kind. Elder deep ones ascend to the _[[spells/Status|status]]_ of near-gods in _deep one_ society, towering over their kin and ruling their sunken cities. Just as they are worshiped, so do the elder deep ones worship the Great Old Ones and Outer Gods themselves.