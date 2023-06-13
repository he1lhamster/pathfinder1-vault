---
cssclass: [monsters]
title1: Zombie, Juju Zombie
desc_short: This wretched human figure has tight leathery skin, sunken eyes, and an
  emaciated frame, yet it moves with eerie alacrity.
title2: Juju Zombie
CR: 2
sources:
- name: Bestiary 2
  page: 291
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 600
race: Human
classes:
- juju zombie rogue 2
alignment: NE
size: Medium
type: undead
subtypes:
- augmented human
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 15
  flat_footed: 13
  components:
    dex: 4
    dodge: 1
    natural: 3
HP:
  HP: 15
  long: 2d8+3
saves:
  fort: 0
  ref: 7
  will: 1
defensive_abilities:
- channel resistance +4
- evasion
DR:
- amount: 5
  weakness: magic and slashing
immunities:
- cold
- electricity
- magic missile
- undead traits
resistances:
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk short sword +6 (1d6+4/19-20)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
      attack: mwk short sword
      bonus:
      - 6
  - - text: slam +5 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: slam
      bonus:
      - 5
  special:
  - sneak attack +1d6
ability_scores:
  STR: 18
  DEX: 19
  CON:
  INT: 8
  WIS: 13
  CHA: 10
BAB: 1
CMB: 5
CMD: 19
feats:
- name: Dodge
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Toughness
- name: Weapon Finesse
skills:
  Acrobatics: 8
  Climb: 16
  Disable Device: 8
  Intimidate: 5
  Perception: 6
  Sleight of Hand: 9
  Stealth: 8
  Survival: 3
  Swim: 8
  Use Magic Device: 5
  _racial_mods:
    Climb:
      _: 8
languages:
- Common
special_qualities:
- rogue talents (combat trick)
- trapfinding +1
ecology:
  environment: any land
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - masterwork short sword
  - other treasure
desc_long: A juju zombie is an animated corpse of a creature, created to serve as
  an undead minion, that retains the skills and abilities it possessed in life.

---

# Zombie, Juju Zombie
This wretched human figure has tight leathery skin, sunken eyes, and an emaciated frame, yet it moves with eerie alacrity.
**Source** Bestiary 2 pg. 291
**XP** 600
Human juju zombie _[[classes/Rogue|rogue]]_ 2

NE Medium undead (augmented human)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +6

##### Defense

**AC** 18, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 15 (2d8+3)
**Fort** +0, **Ref** +7, **Will** +1
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, evasion; **DR** 5/magic and slashing; **Immune** cold, electricity, _[[spells/Magic Missile|magic missile]]_, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Short sword|short sword]]_ +6 (1d6+4/19–20) or slam +5 (1d6+6)
**Special Attacks** sneak attack +1d6

##### Statistics
**Str** 18, **Dex** 19, **Con** —, **Int** 8, **Wis** 13, **Cha** 10
**Base Atk** +1; **CMB** +5; **CMD** 19
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +8, _[[universal monster rules/Climb|Climb]]_ +16, Disable Device +8, Intimidate +5, Perception +6, Sleight of Hand +9, Stealth +8, Survival +3, Swim +8, Use Magic Device +5; **Racial Modifiers** +8 _Climb_
**Languages** Common
**SQ** _rogue_ talents (combat trick), trapfinding +1

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** NPC gear (masterwork _short sword_, other treasure)

##### Description

A juju zombie is an _[[items/Armor Magic Abilities/Animated|animated]]_ corpse of a creature, created to serve as an undead minion, that retains the skills and abilities it possessed in life.