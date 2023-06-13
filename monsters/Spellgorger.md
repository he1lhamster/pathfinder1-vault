﻿---
cssclass: [monsters]
title1: Spellgorger
desc_short: This ten-foot-diameter floating globe of shuddering violet sludge has
  a tangle of dripping tendrils and is encircled by strange arcane energies.
title2: Spellgorger
CR: 12
sources:
- name: 'Pathfinder #107: Scourge of the Godclaw'
  page: 88
  link: http://paizo.com/products/btpy9n0j?Pathfinder-Adventure-Path-107-Scourge-of-the-Godclaw
XP: 19200
alignment: N
size: Large
type: ooze
initiative:
  bonus: 8
senses:
  scent magic: true
auras:
- name: discordant field
  radius: 30
  DC: 25
  duration: 10 rounds
AC:
  AC: 26
  touch: 26
  flat_footed: 17
  components:
    deflection: 8
    dex: 8
    dodge: 1
    size: -1
HP:
  HP: 161
  long: 14d8+98
saves:
  fort: 13
  ref: 12
  will: 9
defensive_abilities:
- deflective shield
- spell healing
immunities:
- fire
- force
- ooze traits
speeds:
  base: 10
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 slams +17 (2d6+5 plus 2d6 fire and 2d6 force)
      entries:
      - - damage: 2d6+5
        - damage: 2d6
          type: fire
        - damage: 2d6
          type: force
      count: 2
      attack: slams
      bonus:
      - 17
  ranged:
  - - text: firebolt +17 touch (2d6 fire plus 2d6 force)
      entries:
      - - damage: 2d6
          type: fire
        - damage: 2d6
          type: force
      attack: firebolt
      bonus:
      - 17
      touch: true
  special:
  - engulf (DC 24)
  - firebolts
  - parasitic spellcasting
space: 10
reach: 10
ability_scores:
  STR: 20
  DEX: 27
  CON: 24
  INT: 19
  WIS: 16
  CHA: 26
BAB: 10
CMB: 16
CMD: 35
feats:
- name: Ability Focus (engulf)
- name: Combat Casting
- name: Dodge
- name: Great Fortitude
- name: Iron Will
- name: Mobility
- name: Weapon Finesse
skills:
  Acrobatics: 22
  Fly: 31
  Knowledge (arcana): 18
  Perception: 17
  Spellcraft: 18
  Use Magic Device: 22
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal
special_qualities:
- prehensile tendrils
ecology:
  environment: any underground
  organization: solitary, pair, or gluttony (3-6)
  treasure_type: standard
special_abilities:
  Deflective Shield (Su): A spellgorger is surrounded by a magical shield of energy
    that grants it a deflection bonus to its Armor Class equal to its Charisma modifier
    (+8 for most spellgorgers).
  Discordant Field (Su): Whenever a spellgorger moves more than 5 feet in a round,
    it becomes surrounded by a disruptive field of magically energized motes that
    interfere with the spellcasting of any creature within 30 feet. Any attempt to
    cast a spell within this area while the discordant field is active requires a
    successful concentration check (DC = 15 + double the level of the spell being
    cast). If this check fails, the spell is lost and the spellcaster must make a
    successful DC 24 Fortitude save to avoid being staggered for 1 round by magical
    feedback generated by the field (this is a mind-affecting effect). Spellgorgers
    are immune to the effects of this ability. The save DC is Constitution-based.
  Engulf (Ex): When a spellgorger engulfs a creature, the ooze can choose to maintain
    a bubble of air around the engulfed creature's head so that it need not fear suffocation.
    An engulfed creature gains the pinned condition as normal, but does not take any
    additional damage from being engulfed.
  Firebolts (Su): As a standard action, a spellgorger can expel up to four bolts of
    burning magical force. It can direct these firebolts at any target within 60 feet
    (no range increment) but cannot target a single creature with more than one firebolt.
    A creature struck by a firebolt takes 2d6 points of fire damage and 2d6 points
    of force damage.
  Immune to Force Effects (Ex): A spellgorger is immune to force damage, and can pass
    through force effects (such as those created by a forcecage and a wall of force)
    as if they did not exist. When it attacks a target, it ignores any armor bonuses
    granted to that foe from force effects (such as those created by bracers of armor,
    mage armor, and shield).
  Parasitic Spellcasting (Su): If a spellgorger has engulfed a creature capable of
    casting spells, it can cast any one of the creature's known spells that has a
    casting time of one full-round action or less (using the spell's casting time
    as normal); when it does so, it is treated as the spell's caster. The spellgorger
    must supply any components for casting the spell in question-if the spell requires
    the use of focus or material components, the spellgorger can use any components
    carried by the engulfed spellcaster as if it had those components. A spell cast
    in this way is considered expended by the engulfed spellcaster, and all spell
    effects resolve at the engulfed spellcaster's caster level (but are not further
    enhanced by feats or abilities the engulfed spellcaster may have).
  Prehensile Tendrils (Ex): A spellgorger's tendrils are capable of fine manipulation,
    such as that required for somatic components when casting spells or handling material
    components. It cannot use these tendrils to effectively wield weapons, but can
    use them to activate relatively small handheld magical items like wands (though
    not larger items like staves).
  Scent Magic (Ex): A spellgorger has the scent ability, but can smell only creatures
    with active spell effects or magic items that exude magical auras.
  Spell Healing (Su): Whenever a spellgorger uses its parasitic spellcasting ability,
    it regains a number of hit points equal to double the level of the spell it cast.
    If the spellgorger is at maximum hit points, it gains temporary hit points equal
    to this amount instead. These temporary hit points do not stack. A spellgorger
    gains no sustenance (or healing) from casting 0-level spells in this manner.
desc_long: |-
  Spellgorgers are among the more terrifying threats that face an adventuring spellcaster-shapeless entities that feed on magic. Rarely encountered in large numbers, spellgorgers are most common in remote reaches of the Darklands, where they often prey upon the numerous spellcasting races that dwell below, such as the drow, duergar, derro, and svirfneblin. A spellgorger prefers the “taste” of arcane magic, but can feed on divine and psychic magic as well.

  A spellgorger resembles a floating sphere of violet sludge that exudes a slithery forest of fine tendrils and sparks of magical energy. A typical specimen is 10 feet in diameter and weighs 1,000 pounds, but spellgorgers' supernatural ability to fly and swift reflexes belie their massive bulk and weight.

---

# Spellgorger
This ten-foot-diameter floating globe of shuddering violet sludge has a tangle of dripping tendrils and is encircled by strange arcane energies.
**Source** Pathfinder #107: Scourge of the Godclaw pg. 88
**XP** 19,200

N Large ooze
**Init** +8; **Senses** _[[universal monster rules/Scent|scent]]_ magic; Perception +17
**Aura** discordant field (30 ft., DC 25, 10 rounds)

##### Defense

**AC** 26, touch 26, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+8 deflection, +8 Dex, +1 _[[feats/Dodge|dodge]]_, –1 size)
**hp** 161 (14d8+98)
**Fort** +13, **Ref** +12, **Will** +9
**Defensive Abilities** deflective _[[spells/Shield|shield]]_, spell healing; **Immune** fire, force, ooze traits

##### Offense
**Speed** 10 ft., fly 30 ft. (perfect)
**Melee** 2 slams +17 (2d6+5 plus 2d6 fire and 2d6 force)
**Ranged** firebolt +17 touch (2d6 fire plus 2d6 force)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Engulf|engulf]]_ (DC 24), firebolts, parasitic spellcasting

##### Statistics
**Str** 20, **Dex** 27, **Con** 24, **Int** 19, **Wis** 16, **Cha** 26
**Base Atk** +10; **CMB** +16; **CMD** 35
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_engulf_), _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +22, Fly +31, Knowledge (arcana) +18, Perception +17, Spellcraft +18, Use Magic Device +22
**Languages** Abyssal, Celestial, Common, Draconic, Infernal
**SQ** _[[items/Weapon Magic Abilities/Prehensile|prehensile]]_ tendrils

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or gluttony (3–6)
**Treasure** standard

### Special Abilities

**Deflective _Shield_ (Su)** A _[[monsters/Spellgorger|spellgorger]]_ is surrounded by a magical _shield_ of energy that grants it a _deflection_ bonus to its Armor Class equal to its Charisma modifier (+8 for most spellgorgers).

**Discordant Field (Su)** Whenever a _spellgorger_ moves more than 5 feet in a round, it becomes surrounded by a _[[feats/Disruptive|disruptive]]_ field of magically energized motes that interfere with the spellcasting of any creature within 30 feet. Any attempt to cast a spell within this area while the discordant field is active requires a successful concentration check (DC = 15 + double the level of the spell being cast). If this check fails, the spell is lost and the spellcaster must make a successful DC 24 Fortitude save to avoid being _[[conditions/Staggered|staggered]]_ for 1 round by magical feedback generated by the field (this is a mind-affecting effect). Spellgorgers are immune to the effects of this ability. The save DC is Constitution-based.

**_Engulf_ (Ex)** When a _spellgorger_ engulfs a creature, the ooze can choose to maintain a bubble of air around the engulfed creature’s head so that it need not _[[universal monster rules/Fear|fear]]_ _[[spells/Suffocation|suffocation]]_. An engulfed creature gains the _[[conditions/Pinned|pinned]]_ condition as normal, but does not take any additional damage from being engulfed.

**Firebolts (Su)** As a standard action, a _spellgorger_ can expel up to four bolts of _[[items/Weapon Magic Abilities/Burning|burning]]_ magical force. It can direct these firebolts at any target within 60 feet (no range increment) but cannot target a single creature with more than one firebolt. A creature struck by a firebolt takes 2d6 points of fire damage and 2d6 points of force damage.

**Immune to Force Effects (Ex)** A _spellgorger_ is immune to force damage, and can pass through force effects (such as those created by a _[[spells/Forcecage|forcecage]]_ and a _[[spells/Wall Of Force|wall of force]]_) as if they did not exist. When it attacks a target, it ignores any armor bonuses granted to that foe from force effects (such as those created by bracers of armor, _[[spells/Mage Armor|mage armor]]_, and _shield_).

**Parasitic Spellcasting (Su)** If a _spellgorger_ has engulfed a creature capable of casting spells, it can cast any one of the creature’s known spells that has a casting time of one full-round action or less (using the spell’s casting time as normal); when it does so, it is treated as the spell’s caster. The _spellgorger_ must supply any components for casting the spell in question—if the spell requires the use of focus or material components, the _spellgorger_ can use any components carried by the engulfed spellcaster as if it had those components. A spell cast in this way is considered expended by the engulfed spellcaster, and all spell effects resolve at the engulfed spellcaster’s caster level (but are not further enhanced by feats or abilities the engulfed spellcaster may have).

**_Prehensile_ Tendrils (Ex)** A _spellgorger_’s tendrils are capable of fine manipulation, such as that required for somatic components when casting spells or handling material components. It cannot use these tendrils to effectively wield weapons, but can use them to activate relatively small handheld magical items like wands (though not larger items like staves).
**_Scent_ Magic (Ex)** A _spellgorger_ has the _scent_ ability, but can smell only creatures with active spell effects or magic items that exude magical auras.
**Spell Healing (Su)** Whenever a _spellgorger_ uses its parasitic spellcasting ability, it regains a number of hit points equal to double the level of the spell it cast. If the _spellgorger_ is at maximum hit points, it gains temporary hit points equal to this amount instead. These temporary hit points do not stack. A _spellgorger_ gains no sustenance (or healing) from casting 0-level spells in this manner.

##### Description

Spellgorgers are among the more terrifying threats that face an adventuring spellcaster—shapeless entities that feed on magic. Rarely encountered in large numbers, spellgorgers are most common in remote reaches of the Darklands, where they often prey upon the numerous spellcasting races that dwell below, such as the _[[monsters/Drow|drow]]_, _[[monsters/Duergar|duergar]]_, _[[monsters/Derro|derro]]_, and _[[monsters/Svirfneblin|svirfneblin]]_. A _spellgorger_ prefers the “taste” of arcane magic, but can feed on divine and _[[universal monster rules/Psychic Magic|psychic magic]]_ as well.

A _spellgorger_ resembles a floating sphere of violet sludge that exudes a slithery forest of fine tendrils and sparks of magical energy. A typical specimen is 10 feet in diameter and weighs 1,000 pounds, but spellgorgers’ supernatural ability to fly and swift reflexes belie their massive bulk and weight.