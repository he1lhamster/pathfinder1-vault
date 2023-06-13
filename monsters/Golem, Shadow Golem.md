---
cssclass: [monsters]
title1: Golem, Shadow Golem
desc_short: This towering humanoid figure seems to be made of solidified shadows.
  Two pale orbs glare from its otherwise blank visage.
title2: Shadow Golem
CR: 14
sources:
- name: 'Pathfinder #102: Breaking the Bones of Hell'
  page: 88
  link: http://paizo.com/products/btpy9i8d?Pathfinder-Adventure-Path-102-Breaking-the-Bones-of-Hell
XP: 38400
alignment: N
size: Large
type: construct
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  see in darkness: true
auras:
- name: shadow
  radius: 60
AC:
  AC: 29
  touch: 19
  flat_footed: 25
  components:
    deflection: 6
    dex: 4
    natural: 10
    size: -1
HP:
  HP: 151
  long: 22d10+30
saves:
  fort: 7
  ref: 11
  will: 7
defensive_abilities:
- immunity to magic
DR:
- amount: 15
  weakness: adamantine and slashing
immunities:
- cold
- construct traits
speeds:
  base: 50
attacks:
  melee:
  - - text: 2 claws +33 (3d10+12)
      entries:
      - - damage: 3d10+12
      count: 2
      attack: claws
      bonus:
      - 33
  special:
  - breath weapon
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 20
    concentration: 15
ability_scores:
  STR: 34
  DEX: 19
  CON:
  INT:
  WIS: 11
  CHA: 1
BAB: 22
CMB: 35
CMD: 55
skills:
  Stealth: 0
    in dim light: 16
  Perception: 0
  _racial_mods:
    Stealth:
      in dim light: 16
ecology:
  environment: any
  organization: solitary or gang (2-4)
  treasure_type: none
special_abilities:
  Breath Weapon (Su): As a free action once every 1d4+1 rounds, a shadow golem can
    exhale a 30-foot cone of shadows. All creatures caught in this area take 2d4 points
    of Strength damage and become staggered for 1 round. A successful DC 21 Fortitude
    save reduces the Strength damage to 2 points and negates the staggering effect.
    The save DC is Constitution-based.
  Immunity to Magic (Ex): A shadow golem is immune to any spell or spell-like ability
    that allows spell resistance. In addition, certain spells and effects function
    differently against the creature, as noted below. Any spell with the light or
    darkness descriptor cast directly on a shadow golem suppresses its shadow aura
    for 1 round per spell level (no save).A shadow conjuration or shadow evocation
    spell reactivates a shadow golem's shadow aura if it had been suppressed and grants
    the shadow golem fast healing 5 for 10 rounds. The greater versions of these spells
    grant fast healing 10 for 20 rounds.Both sunbeam and sunburst affect a shadow
    golem normally. Shadow golems are considered to be particularly susceptible to
    sunlight for the purpose of resolving damage inflicted by either of these spells.
    If a shadow golem fails its saving throw against one of these spells, its shadow
    aura is suppressed for 1d8 rounds.A searing light spell that strikes a shadow
    golem deals no damage, but does slow it (as per the slow spell) for 1 round (no
    save).
  Shadow Aura (Su): A shadow golem constantly exudes an aura of eerie shadowy illumination,
    causing the area surrounding it to a distance of 60 feet to function as if illuminated
    by dim light, regardless of the ambient lighting (or lack thereof). As long as
    a shadow golem is in dim light (such as that granted by its own aura), it gains
    a +6 deflection bonus to its AC and gains the benefit of a constant air walk effect.
    A character who attempts to cast a spell with the darkness or light descriptor
    while within a shadow golem's shadow aura must make a successful DC 25 caster
    level check, or the spell is countered as it is cast. At the start of any round
    in which the shadow golem's aura interacts with an in-place darkness or light
    spell effect, that effect is automatically dispelled if the effect is from a spell
    whose level is 4th level or lower. If the effect is from a 5th-level or higher-level
    spell, the golem's shadow aura attempts to dispel the effect as if via greater
    dispel magic (CL 20th). The golem's shadow aura can attempt to dispel any amount
    of spells in this way, and if it fails to do so during one round, it can attempt
    to do so again at the start of each following round.
desc_long: |-
  Among the most exotic of golems are the enigmatic shadow golems, animated constructs composed not of any mundane material but of pure shadowstuff harvested from the Shadow Plane. Tempered by magic, this strange substance holds a solid shape yet retains its eerie otherworldly features, allowing the shadow golem to walk on the air or to resist physical attacks that don't cut deeply-and even then, only the sharpest of adamantine edges can do significant harm to one of these creatures.

  Shadow golems are typically built in the form of hulking humanoids with skin and clothing as black as spilled ink. Despite their muscular forms, they can move with surprising speed, and weigh much less than one might expect a muscle-bound statue to weigh. While the creator of a shadow golem can fashion the construct into any shape, a strange element of the way the animating magic mixes with the raw shadowstuff results in an unusual side effect-the facial features of all shadow golems are indistinct, with the exception of two glowing eyes that are difficult to spot in the cloak of shadows that surrounds every shadow golem.

  The typical shadow golem stands 11 feet tall and weighs 400 pounds.

---

# Golem, Shadow Golem
This towering humanoid figure seems to be made of solidified shadows. Two pale orbs glare from its otherwise blank visage.
**Source** Pathfinder #102: _[[items/Weapon Magic Abilities/Breaking|Breaking]]_ the Bones of Hell pg. 88
**XP** 38,400

N Large construct
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +0
**Aura** _[[items/Armor Magic Abilities/Shadow|shadow]]_ (60 ft.)

##### Defense

**AC** 29, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+6 deflection, +4 Dex, +10 Natural, -1 Size)
**hp** 151 (22d10+30)
**Fort** +7, **Ref** +11, **Will** +7
**Defensive Abilities** _[[universal monster rules/Immunity|immunity]]_ to magic; **DR** 15/adamantine and slashing; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** 50 ft.
**Melee** 2 claws +33 (3d10+12)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +15)
Constant—_[[spells/Air Walk|air walk]]_

##### Statistics
**Str** 34, **Dex** 19, **Con** —, **Int** —, **Wis** 11, **Cha** 1
**Base Atk** +22; **CMB** +35; **CMD** 55
**Skills** Stealth +0 (+16 in dim light); **Racial Modifiers** +16 Stealth in dim light

##### Ecology

**Environment** any
**Organization** solitary or gang (2–4)
**Treasure** none

### Special Abilities

**_Breath Weapon_ (Su)** As a free action once every 1d4+1 rounds, a _shadow_ golem can exhale a 30-foot cone of shadows. All creatures caught in this area take 2d4 points of Strength damage and become _[[conditions/Staggered|staggered]]_ for 1 round. A successful DC 21 Fortitude save reduces the Strength damage to 2 points and negates the staggering effect. The save DC is Constitution-based.

**_Immunity_ to Magic (Ex)** A _shadow_ golem is immune to any spell or spell-like ability that allows _[[universal monster rules/Spell Resistance|spell resistance]]_. In addition, certain spells and effects function differently against the creature, as noted below.

* Any spell with the light or _[[spells/Darkness|darkness]]_ descriptor cast directly on a _shadow_ golem suppresses its _shadow_ aura for 1 round per spell level (no save).
* A _[[spells/Shadow Conjuration|shadow conjuration]]_ or _[[spells/Shadow Evocation|shadow evocation]]_ spell reactivates a _shadow_ golem’s _shadow_ aura if it had been suppressed and grants the _shadow_ golem _[[universal monster rules/Fast Healing|fast healing]]_ 5 for 10 rounds. The greater versions of these spells grant _fast healing_ 10 for 20 rounds.
* Both _[[spells/Sunbeam|sunbeam]]_ and _[[spells/Sunburst|sunburst]]_ affect a _shadow_ golem normally. _Shadow_ golems are considered to be particularly susceptible to sunlight for the purpose of resolving damage inflicted by either of these spells. If a _shadow_ golem fails its saving throw against one of these spells, its _shadow_ aura is suppressed for 1d8 rounds.
* A _[[spells/Searing Light|searing light]]_ spell that strikes a _shadow_ golem deals no damage, but does _[[spells/Slow|slow]]_ it (as per the _slow_ spell) for 1 round (no save).
**_Shadow_ Aura (Su)** A _shadow_ golem constantly exudes an aura of eerie shadowy illumination, causing the area surrounding it to a distance of 60 feet to function as if illuminated by dim light, regardless of the ambient lighting (or lack thereof). As long as a _shadow_ golem is in dim light (such as that granted by its own aura), it gains a +6 _deflection_ bonus to its AC and gains the benefit of a constant _air walk_ effect. A character who attempts to cast a spell with the _darkness_ or light descriptor while within a _shadow_ golem’s _shadow_ aura must make a successful DC 25 caster level check, or the spell is countered as it is cast. At the start of any round in which the _shadow_ golem’s aura interacts with an in-place _darkness_ or light spell effect, that effect is automatically dispelled if the effect is from a spell whose level is 4th level or lower. If the effect is from a 5th-level or higher-level spell, the golem’s _shadow_ aura attempts to dispel the effect as if via greater _[[spells/Dispel Magic|dispel magic]]_ (CL 20th). The golem’s _shadow_ aura can attempt to dispel any amount of spells in this way, and if it fails to do so during one round, it can attempt to do so again at the start of each following round.

##### Description

Among the most exotic of golems are the enigmatic _shadow_ golems, _[[items/Armor Magic Abilities/Animated|animated]]_ constructs composed not of any mundane material but of pure shadowstuff harvested from the _Shadow_ Plane. Tempered by magic, this strange substance holds a solid shape yet retains its eerie otherworldly features, allowing the _shadow_ golem to walk on the air or to resist physical attacks that don’t cut deeply—and even then, only the sharpest of adamantine edges can do significant _[[spells/Harm|harm]]_ to one of these creatures.

_Shadow_ golems are typically built in the form of hulking humanoids with skin and clothing as black as spilled _[[items/Mundane/Ink|ink]]_. Despite their muscular forms, they can move with surprising speed, and weigh much less than one might expect a muscle-bound _[[spells/Statue|statue]]_ to weigh. While the creator of a _shadow_ golem can fashion the construct into any shape, a strange element of the way the animating magic mixes with the raw shadowstuff results in an unusual side effect—the facial features of all _shadow_ golems are indistinct, with the exception of two glowing eyes that are difficult to spot in the _[[spells/Cloak Of Shadows|cloak of shadows]]_ that surrounds every _shadow_ golem.

The typical _shadow_ golem stands 11 feet tall and weighs 400 pounds.