---
cssclass: [monsters]
title1: Qlippoth Lord, Yamasoth
desc_short: Writhing, hook-covered tentacles unfurl from this behemoth's body, at
  the center of which gapes a maw with a red eye in its throat.
title2: Yamasoth
CR: 24
sources:
- name: 'Pathfinder #64: Beyond the Doomsday Door'
  page: 66
  link: http://paizo.com/products/btpy8t35?Pathfinder-Adventure-Path-64-Beyond-the-Doomsday
    Door
XP: 1228800
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
- qlippoth
initiative:
  bonus: 11
senses:
  all-around vision: true
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: cloak of chaos
  DC: 24
AC:
  AC: 43
  touch: 18
  flat_footed: 35
  components:
    deflection: 4
    dex: 7
    dodge: 1
    natural: 25
    size: -4
HP:
  HP: 526
  long: 27d10+378
  regeneration: 15
  regeneration_weakness: lawful
saves:
  fort: 33
  ref: 28
  will: 18
DR:
- amount: 15
  weakness: cold iron and lawful
immunities:
- cold
- death effects
- mind-affecting effects
- poison
resistances:
  acid: 30
  electricity: 30
  fire: 30
SR: 35
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: maw +36 (2d10+13/19-20)
      entries:
      - - damage: 2d10+13
          crit_range: 19-20
      attack: maw
      bonus:
      - 36
    - text: 4 bites +36 (2d8+13/19-20)
      entries:
      - - damage: 2d8+13
          crit_range: 19-20
      count: 4
      attack: bites
      bonus:
      - 36
    - text: 6 tentacles +34 (2d6+6/19-20 plus grab)
      entries:
      - - damage: 2d6+6
          crit_range: 19-20
        - effect: grab
      count: 6
      attack: tentacles
      bonus:
      - 34
  special:
  - constrict (2d6+13)
  - gaze weapon
  - horrific appearance (DC 29)
  - polymorph plague
  - rend (4 bites, 2d8+19)
  - tentacle transformation
space: 20
reach: 20
reach_other: 30 ft. with tentacles
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 24
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: fly
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: statue
    source: default
    freq: At will
  - name: stone shape
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 21
  - name: quickened baleful polymorph
    source: default
    freq: 3/day
    DC: 21
  - name: flesh to stone
    source: default
    freq: 3/day
    DC: 22
  - name: phase door
    source: default
    freq: 3/day
  - name: polymorph any object
    source: default
    freq: 3/day
    DC: 24
  - name: wall of stone
    source: default
    freq: 3/day
  - name: earthquake
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any qlippoth
    - name: combination of qlippoth whose total combined CR is 20
    - name: lower
      chance: 100%
  sources:
  - name: default
    CL: 20
    concentration: 26
ability_scores:
  STR: 36
  DEX: 25
  CON: 38
  INT: 25
  WIS: 21
  CHA: 22
BAB: 27
CMB: 44
CMB_other: +48 grapple
CMD: 66
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Critical (tentacle)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (baleful polymorph)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 45
  Intimidate: 36
  Knowledge (arcana): 37
  Knowledge (planes): 37
  Knowledge (dungeoneering): 34
  Knowledge (history): 34
  Knowledge (nature): 34
  Knowledge (religion): 34
  Perception: 35
  Sense Motive: 35
  Spellcraft: 37
  Stealth: 25
  Use Magic Device: 36
  _racial_mods:
    Fly:
      _: 10
languages:
- Abyssal
- telepathy 300 ft.
special_qualities:
- qlippoth lord traits
ecology:
  environment: any (Sekatar-Seraktis)
  organization: solitary or group (Yamasoth plus 2d6 gongorinans and 2d6 various polymorphed
    minions)
  treasure_type: triple
special_abilities:
  Gaze Weapon (Su): As a free action at the start of his turn, Yamasoth can gape his
    central maw wide to expose the horrific red eye lodged in what should be his throat.
    This gaze weapon has a range of 30 feet, and polymorphs creatures affected by
    it into giant vermin, animals, or magical beasts (Fortitude DC 37 resists). Yamasoth
    chooses what creatures to transform victims into as they fail their saving throws.
    This effect otherwise functions as polymorph any object (CL 20th), and is a polymorph
    effect. Yamasoth can keep his maw open for up to 3 consecutive rounds, after which
    his throat-eye closes and this gaze weapon cannot be used again for 1 minute.
    The save DC is Constitution-based.
  Horrific Appearance (Su): Creatures that succumb to Yamasoth's horrific appearance
    are stunned. At the start of each round thereafter, a creature stunned in this
    way can make a choice- fight the overwhelming chaos and horror and attempt a new
    DC 29 Will save to end the stun effect and act normally on that round, or accept
    the chaos into its soul and automatically succeed at the save to recover from
    the stun effect. This latter option immediately shifts the creature's alignment
    one step closer to chaotic evil. This shift in alignment can be fixed via atonement,
    but counts as a voluntary alignment shift for the purposes of atonement's material
    component requirements. A creature that becomes chaotic evil as a result of this
    also becomes a willing minion and ally of Yamasoth.
  Maw (Ex): Yamasoth's central maw is a primary attack that threatens a critical hit
    on a roll of 19-20. A creature hit by Yamasoth's maw while his gaze weapon is
    active takes a -4 penalty on its next saving throw against the gaze attack.
  Polymorph Plague (Su): Any creature that has been affected by one of Yamasoth's
    polymorph effects becomes “contagious.” For 24 hours after the creature's initial
    transformation, any other creature that touches or is touched by the polymorphed
    creature must succeed at a Fortitude save (DC = 10 + 1/2 the polymorphed creature's
    HD + the polymorphed creature's Constitution modifier) to resist polymorphing
    into a creature identical to the current form of the polymorphed creature.
  Qlippoth Lord Traits: A qlippoth lord is a powerful and unique qlippoth that rules
    a significant portion of an Abyssal realm. Qlippoth lords possess the following
    traits. Immunity to cold, death effects, mind-affecting effects, and poison.Resistance
    to acid 30, electricity 30, and fire 30.Horrific Appearance (Su) This ability
    functions similarly to the typical qlippoth ability, save that qlippoth lords'
    horrific appearances often create physical effects and changes in their victims.
    Despite these physical effects, a qlippoth lord's horrific appearance remains
    a mind-affecting effect.Summon Qlippoth (Sp) Once per day, a qlippoth lord can
    summon any qlippoth or combination of qlippoth whose total combined CR is 20 or
    lower. This ability always works, and is equivalent to a 9th-level spell.Telepathy
    300 feet.A qlippoth lord's natural weapons, as well as any weapon it wields, are
    treated as chaotic, epic, and evil for the purpose of overcoming damage reduction.Qlippoth
    lords can grant spells to their worshipers. Granting spells does not require any
    specific action on the qlippoth lord's behalf. All qlippoth lords grant access
    to the domains of Chaos and Evil; in addition, they grant access to two other
    domains and a favored weapon that vary according to each qlippoth lord's themes
    and interests.
  Tentacle Transformation (Su): 'At the start of every oddnumbered round, three of
    Yamasoth's tentacle tips transform into one of three different types of appendages-a
    serpent's head, a clawed hand, or a metallic blade. The three tentacles all change
    into the same type of attack, and the change persists for 1 full round, after
    which the three tentacles revert to normal tentacles on every even-numbered round.
    While transformed, the limbs make the following types of attacks instead of tentacle
    attacks. Blade: talon +36 (3d6+13/19-20)Clawed Hand: claw +36 (2d6+13 plus bleed
    damage equal to the damage dealt by the claw)Serpent Head: bite +36 (1d8+13 plus
    poison: bite-injury; save Fort DC 37; frequency 1/round for 12 rounds; effect
    1d4 Dex drain and slowed for 1 round; cure 3 consecutive saves)'
desc_long: |-
  Yamasoth, known also as the Polymorph Plague, dwells in the endless cavern realm of Sekatar- Seraktis in the Abyss. Constantly at war with bickering balor lords and other powerful demons, Yamasoth has held his own as the lord of the Abyss's largest, most centralized region: the Kingdom of New Flesh. The “new flesh” in question consists of the qlippoth lord's subjects- men and women from countless worlds who may have been kings and queens at one time, but here are nothing more than base monsters, vermin, and beasts to serve at Yamasoth's whim. Some he feeds upon. Others he keeps for his harem. But the bulk of the denizens of the Kingdom of New Flesh are soldiers. In this army, other qlippoth serve as commanders and generals, particularly Yamasoth's favored minions, the gongorinans (see page 90).

  Unlike most qlippoth, Yamasoth does not necessarily prefer to kill but rather to transform. A human who sins and dies produces a soul that fuels the demonic horde, but a dumb beast or feral monster who dies is merely carrion. By transforming free-willed mortals into monsters, Yamasoth's Army of the New Flesh only becomes more capable of ending worlds. Yamasoth's centuries-long alliance with Runelord Alaznist may have eventually resulted in such an assault on Golarion, but the devastation of Earthfall ended those plans before Yamasoth's burgeoning realm could finalize its gestation-proof that even in the greatest of disasters, some good is wrought.

  Yamasoth's interest in transformations goes far beyond mere polymorphing. The qlippoth lord is also fascinated by the act of fleshwarping and reworking life into new forms of mutants. Rumors state that the nature of the experiments that take place deep in the Kingdom of New Flesh closely mimic those the daemons performed in the Abyss so long ago that resulted in the first demons. In fact, some dissident demonologists claim Yamasoth himself is a nascent demon lord, and is in fact that first, primal demon born of daemonic tampering with Abyssal quintessence and sinful souls.

---

# Qlippoth Lord, Yamasoth
Writhing, hook-covered tentacles unfurl from this behemoth’s body, at the center of which gapes a maw with a red eye in its throat.
**Source** Pathfinder #64: Beyond the Doomsday Door pg. 66
**XP** 1,228,800
CE Gargantuan outsider (chaotic, evil, extraplanar, qlippoth)
**Init** +11; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +35
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 24)

##### Defense

**AC** 43, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+4 deflection, +7 Dex, +1 _[[feats/Dodge|dodge]]_, +25 natural, –4 size)
**hp** 526 (27d10+378); _[[universal monster rules/Regeneration|regeneration]]_ 15 (lawful)
**Fort** +33, **Ref** +28, **Will** +18
**DR** 15/cold iron and lawful; **Immune** cold, death effects, mind-affecting effects, poison; **Resist** acid 30, electricity 30, fire 30; **SR** 35

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** maw +36 (2d10+13/19–20), 4 bites +36 (2d8+13/19–20), 6 tentacles +34 (2d6+6/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft. (30 ft. with tentacles)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+13), _[[universal monster rules/Gaze|gaze]]_ weapon, horrific appearance (DC 29), _[[spells/Polymorph|polymorph]]_ plague, _[[universal monster rules/Rend|rend]]_ (4 bites, 2d8+19), tentacle _[[spells/Transformation|transformation]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +26)
Constant—_cloak of chaos_ (DC 24), _detect good_, _detect law_, fly, _[[spells/Freedom of Movement|freedom of movement]]_, _true seeing_
At will—_[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Statue|statue]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 21)
3/day—quickened _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 21), _[[spells/Flesh to Stone|flesh to stone]]_ (DC 22), _[[spells/Phase Door|phase door]]_, _[[spells/Polymorph Any Object|polymorph any object]]_ (DC 24), _[[spells/Wall Of Stone|wall of stone]]_
1/day—_[[spells/Earthquake|earthquake]]_, _[[universal monster rules/Summon|summon]]_ (level 9, any qlippoth or combination of qlippoth whose total combined CR is 20 or lower 100%)

##### Statistics
**Str** 36, **Dex** 25, **Con** 38, **Int** 25, **Wis** 21, **Cha** 22
**Base Atk** +27; **CMB** +44 (+48 grapple); **CMD** 66 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (tentacle), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_baleful polymorph_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +45, Intimidate +36, Knowledge (arcana, planes) +37, Knowledge (dungeoneering, history, nature, religion) +34, Perception +35, Sense Motive +35, Spellcraft +37, Stealth +25, Use Magic Device +36; **Racial Modifiers** +10 Fly
**Languages** Abyssal; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** qlippoth lord traits

##### Ecology

**Environment** any (Sekatar-Seraktis)
**Organization** solitary or group (Yamasoth plus 2d6 gongorinans and 2d6 various polymorphed minions)
**Treasure** triple

### Special Abilities

**_Gaze_ Weapon (Su)** As a free action at the start of his turn, Yamasoth can gape his central maw wide to expose the horrific red eye lodged in what should be his throat. This _gaze_ weapon has a range of 30 feet, and polymorphs creatures affected by it into _[[spells/Giant Vermin|giant vermin]]_, animals, or magical beasts (Fortitude DC 37 resists). Yamasoth chooses what creatures to transform victims into as they fail their saving throws. This effect otherwise functions as _polymorph any object_ (CL 20th), and is a _polymorph_ effect. Yamasoth can keep his maw open for up to 3 consecutive rounds, after which his throat-eye closes and this _gaze_ weapon cannot be used again for 1 minute. The save DC is Constitution-based.

**Horrific Appearance (Su)** Creatures that succumb to Yamasoth’s horrific appearance are _[[conditions/Stunned|stunned]]_. At the start of each round thereafter, a creature _stunned_ in this way can make a choice— fight the overwhelming chaos and horror and attempt a new DC 29 Will save to end the stun effect and act normally on that round, or accept the chaos into its soul and automatically succeed at the save to recover from the stun effect. This latter option immediately shifts the creature’s alignment one step closer to chaotic evil. This shift in alignment can be fixed via _[[spells/Atonement|atonement]]_, but counts as a voluntary alignment shift for the purposes of _atonement_’s material component requirements. A creature that becomes chaotic evil as a result of this also becomes a willing minion and ally of Yamasoth.

**Maw (Ex)** Yamasoth’s central maw is a primary attack that threatens a critical hit on a roll of 19–20. A creature hit by Yamasoth’s maw while his _gaze_ weapon is active takes a –4 penalty on its next saving throw against the _gaze_ attack.

**_Polymorph_ Plague (Su) **Any creature that has been affected by one of Yamasoth’s _polymorph_ effects becomes “contagious.” For 24 hours after the creature’s initial _transformation_, any other creature that touches or is touched by the polymorphed creature must succeed at a Fortitude save (DC = 10 + 1/2 the polymorphed creature’s HD + the polymorphed creature’s Constitution modifier) to resist polymorphing into a creature identical to the current form of the polymorphed creature.

**Qlippoth Lord Traits** A qlippoth lord is a powerful and unique qlippoth that rules a significant portion of an Abyssal realm. Qlippoth lords possess the following traits.

* _[[universal monster rules/Immunity|Immunity]]_ to cold, death effects, mind-affecting effects, and poison.
* _[[universal monster rules/Resistance|Resistance]]_ to acid 30, electricity 30, and fire 30.
* Horrific Appearance (Su) This ability functions similarly to the typical qlippoth ability, save that qlippoth lords’ horrific appearances often create physical effects and changes in their victims. Despite these physical effects, a qlippoth lord’s horrific appearance remains a mind-affecting effect.
* _Summon_ Qlippoth (Sp) Once per day, a qlippoth lord can _summon_ any qlippoth or combination of qlippoth whose total combined CR is 20 or lower. This ability always works, and is equivalent to a 9th-level spell.
* _Telepathy_ 300 feet.
* A qlippoth lord’s natural weapons, as well as any weapon it wields, are treated as chaotic, epic, and evil for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.
* Qlippoth lords can grant spells to their worshipers. Granting spells does not require any specific action on the qlippoth lord’s behalf. All qlippoth lords grant access to the domains of Chaos and Evil; in addition, they grant access to two other domains and a favored weapon that vary according to each qlippoth lord’s themes and interests.

**Tentacle _Transformation_ (Su) **At the start of every oddnumbered round, three of Yamasoth’s tentacle tips transform into one of three different types of appendages—a serpent’s head, a clawed hand, or a metallic blade. The three tentacles all change into the same type of attack, and the change persists for 1 full round, after which the three tentacles revert to normal tentacles on every even-numbered round. While transformed, the limbs make the following types of attacks instead of tentacle attacks.

* Blade: talon +36 (3d6+13/19-20)
* Clawed Hand: claw +36 (2d6+13 plus _[[universal monster rules/Bleed|bleed]]_ damage equal to the damage dealt by the claw)
* Serpent Head: bite +36 (1d8+13 plus poison: bite—injury; save Fort DC 37; frequency 1/round for 12 rounds; effect 1d4 Dex drain and slowed for 1 round; cure 3 consecutive saves)

##### Description

Yamasoth, known also as the _Polymorph_ Plague, dwells in the endless cavern realm of Sekatar- Seraktis in the Abyss. Constantly at war with bickering balor lords and other powerful demons, Yamasoth has held his own as the lord of the Abyss’s largest, most centralized region: the Kingdom of New Flesh. The “new flesh” in question consists of the qlippoth lord’s subjects— men and women from countless worlds who may have been kings and queens at one time, but here are nothing more than base monsters, vermin, and beasts to serve at Yamasoth’s whim. Some he feeds upon. Others he keeps for his harem. But the bulk of the denizens of the Kingdom of New Flesh are soldiers. In this army, other qlippoth serve as commanders and generals, particularly Yamasoth’s favored minions, the gongorinans (see page 90).

Unlike most qlippoth, Yamasoth does not necessarily prefer to kill but rather to transform. A human who sins and dies produces a soul that fuels the demonic horde, but a dumb beast or feral monster who dies is merely carrion. By transforming free-willed mortals into monsters, Yamasoth’s Army of the New Flesh only becomes more capable of ending worlds. Yamasoth’s centuries-long alliance with Runelord Alaznist may have eventually resulted in such an assault on Golarion, but the devastation of Earthfall ended those plans before Yamasoth’s burgeoning realm could finalize its gestation—proof that even in the greatest of disasters, some good is wrought.

Yamasoth’s interest in transformations goes far beyond mere polymorphing. The qlippoth lord is also _[[conditions/Fascinated|fascinated]]_ by the act of fleshwarping and reworking life into new forms of mutants. Rumors state that the nature of the experiments that take place deep in the Kingdom of New Flesh closely _[[monsters/Mimic|mimic]]_ those the daemons performed in the Abyss so long ago that resulted in the first demons. In fact, some dissident demonologists claim Yamasoth himself is a nascent demon lord, and is in fact that first, primal demon born of daemonic tampering with Abyssal _[[spells/Quintessence|quintessence]]_ and sinful souls.