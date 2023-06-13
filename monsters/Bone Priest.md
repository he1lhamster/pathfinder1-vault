---
cssclass: [monsters]
title1: Bone Priest
desc_short: This skeletal creature wears rotting robes, and carries a sword in its
  talon-like hands. An evil blue light dances in its empty eye sockets.
title2: Bone Priest
CR: 4
sources:
- name: The Emerald Spire Superdungeon
  page: 152
  link: http://paizo.com/products/btpy8yqx?Pathfinder-Module-The-Emerald-Spire-Superdungeon
XP: 1200
alignment: LE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 16
  touch: 12
  flat_footed: 14
  components:
    dex: 2
    natural: 4
HP:
  HP: 37
  long: 5d8+15
saves:
  fort: 4
  ref: 3
  will: 7
defensive_abilities:
- channel resistance +2
DR:
- amount: 5
  weakness: bludgeoning and magic
immunities:
- cold
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk bastard sword +7 (1d10+3/19-20)
      entries:
      - - damage: 1d10+3
          crit_range: 19-20
      attack: mwk bastard sword
      bonus:
      - 7
  - - text: slam +5 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: slam
      bonus:
      - 5
  special:
  - death drink
  - unnerving gaze
spells:
  entries:
  - name: hold person
    source: '?'
    level: 2
    DC: 15
  - name: spiritual weapon
    source: '?'
    level: 2
  - is_domain_spell: true
    name: touch of idiocy
    source: '?'
    level: 2
    DC: 15
  - name: cause fear
    source: '?'
    level: 1
    DC: 14
  - name: command
    source: '?'
    level: 1
    DC: 14
  - is_domain_spell: true
    name: lesser confusion
    source: '?'
    level: 1
    DC: 14
  - name: protection from good
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: guidance
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: prepared
    CL: 3
    concentration: 6
    domains:
    - madness
ability_scores:
  STR: 14
  DEX: 15
  CON:
  INT: 11
  WIS: 16
  CHA: 17
BAB: 3
CMB: 5
CMD: 17
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Weapon Focus (bastard sword)
skills:
  Intimidate: 11
  Knowledge (religion): 8
  Perception: 11
  Stealth: 10
languages:
- Common
- Undercommon
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
  treasure:
  - mwk bastard sword
  - other treasure
special_abilities:
  Death Drink (Su): When a bone priest reduces a creature to 0 hit points or fewer
    with a melee attack or coup de grace, it can use death knell against that creature
    as a free action. It doesn't need to be touching the creature to use this ability.
  Spells: A bone priest casts spells as 3rd-level cleric. It also gains domain spells
    from the Madness domain, but none of the other domain abilities or cleric abilities.
  Unnerving Gaze (Su): A bone priest can make a gaze attack that strikes fear into
    the hearts of all creatures within a 30-foot radius that can see the bone priest.
    These creatures must succeed at a DC 15 Will saving throw or be shaken for 1d4
    rounds. This is a mind-affecting fear effect. The save DC is Charisma-based.
desc_long: |-
  Bone priests are undead servants of evil gods, condemned to continue serving for decades or centuries after death. In life, bone priests were acolytes or underpriests who failed at some difficult test or fell in battle against powerful enemies of the faith. Their dark gods have rewarded their fanaticism by giving another chance to demonstrate their worthiness.

  Bone priests retain the spellcasting ability and some of the domain spells they possessed in life. A typical bone priest casts spells as a 3rd-level cleric and has the bonus spells of one of the domains it had originally-usually Darkness, Death, Destruction, Evil, or Madness (the bone priest presented here possesses the Madness domain).

  While bone priests occasionally arise with no outside intervention other than the will of their gods, they are normally created through a profane ritual that culminates in the casting of a create undead spell by a caster of at least 11th level.

---

# Bone Priest
This skeletal creature wears rotting robes, and carries a sword in its talon-like hands. An evil blue light dances in its empty eye sockets.
**Source** The Emerald Spire Superdungeon pg. 152
**XP** 1,200

LE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 Dex, +4 natural)
**hp** 37 (5d8+15)
**Fort** +4, **Ref** +3, **Will** +7
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **DR** 5/bludgeoning and magic; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Bastard sword|bastard sword]]_ +7 (1d10+3/19–20) or slam +5 (1d4+3)
**Special Attacks** death drink, unnerving _[[universal monster rules/Gaze|gaze]]_
**Spells Prepared **(CL 3rd; concentration +6)
2nd—_[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_ (DC 15)
1st—_[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Command|command]]_ (DC 14), lesser _[[spells/Confusion|confusion]]_ (DC 14), _[[spells/Protection From Good|protection from good]]_
0—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D **domain spell; **Domain **Madness

##### Statistics
**Str** 14, **Dex** 15, **Con** —, **Int** 11, **Wis** 16, **Cha** 17
**Base Atk** +3; **CMB** +5; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_bastard sword_)
**Skills** Intimidate +11, Knowledge (religion) +8, Perception +11, Stealth +10
**Languages** Common, Undercommon

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard (mwk _bastard sword_, other treasure)

### Special Abilities

**Death Drink (Su)** When a _[[monsters/Bone Priest|bone priest]]_ reduces a creature to 0 hit points or fewer with a melee attack or coup de _[[spells/Grace|grace]]_, it can use _[[spells/Death Knell|death knell]]_ against that creature as a free action. It doesn’t need to be touching the creature to use this ability.
**Spells **A _bone priest_ casts spells as 3rd-level _[[classes/Cleric|cleric]]_. It also gains domain spells from the Madness domain, but none of the other domain abilities or _cleric_ abilities.

**Unnerving _Gaze_ (Su)** A _bone priest_ can make a _gaze_ attack that strikes _[[universal monster rules/Fear|fear]]_ into the hearts of all creatures within a 30-foot radius that can see the _bone priest_. These creatures must succeed at a DC 15 Will saving throw or be _[[conditions/Shaken|shaken]]_ for 1d4 rounds. This is a mind-affecting _fear_ effect. The save DC is Charisma-based.

##### Description

Bone priests are undead servants of evil gods, condemned to continue serving for decades or centuries after death. In life, bone priests were acolytes or underpriests who failed at some difficult test or fell in battle against powerful enemies of the faith. Their dark gods have rewarded their fanaticism by giving another chance to demonstrate their worthiness.

Bone priests retain the spellcasting ability and some of the domain spells they possessed in life. A typical _bone priest_ casts spells as a 3rd-level _cleric_ and has the bonus spells of one of the domains it had originally—usually _[[spells/Darkness|Darkness]]_, Death, _[[spells/Destruction|Destruction]]_, Evil, or Madness (the _bone priest_ presented here possesses the Madness domain).

While bone priests occasionally arise with no outside intervention other than the will of their gods, they are normally created through a profane ritual that culminates in the casting of a _[[spells/Create Undead|create undead]]_ spell by a caster of at least 11th level.