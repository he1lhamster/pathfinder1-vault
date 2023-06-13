---
cssclass: [monsters]
title1: Merlucent
desc_short: A mane of long, writhing tentacles crowns this translucent, humanoid figure.
  A crystalline skeleton supports its faintly glowing flesh.
title2: Merlucent
CR: 3
sources:
- name: 'Pathfinder #104: Wrath of Thrune'
  page: 90
  link: http://paizo.com/products/btpy9jb7?Pathfinder-Adventure-Path-104-Wrath-of-Thrune
XP: 800
alignment: CN
size: Medium
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 16
  touch: 13
  flat_footed: 13
  components:
    dex: 3
    natural: 3
HP:
  HP: 26
  long: 4d8+8
saves:
  fort: 3
  ref: 4
  will: 6
resistances:
  cold: 5
speeds:
  base: 15
  swim: 40
attacks:
  melee:
  - - text: 3 tentacles +6 (1d4+1 plus poison)
      entries:
      - - damage: 1d4+1
        - effect: poison
      count: 3
      attack: tentacles
      bonus:
      - 6
  special:
  - arcane echo
  - poison
  - pull (tentacle, 5 ft.)
  - vitrify
space: 5
reach: 5
reach_other: 15 ft. with tentacle
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: delay poison
    source: default
    freq: 3/day
  - name: light
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 4
    concentration: 4
ability_scores:
  STR: 12
  DEX: 16
  CON: 15
  INT: 11
  WIS: 14
  CHA: 11
BAB: 3
CMB: 4
CMD: 17
feats:
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Climb: 6
  Handle Animal: 4
  Perception: 7
  Stealth: 10
  Survival: 11
  Swim: 14
  _racial_mods:
    Survival:
      _: 4
languages:
- Aklo
- telepathy 30 ft.
special_qualities:
- jellyfish empathy
- transparent flesh
ecology:
  environment: any ocean
  organization: solitary, hunting group (3-6), or clan (9-14)
  treasure_type: incidental
special_abilities:
  Arcane Echo (Su): Merlucents naturally filter arcane energies from the world around
    them, and can produce large displays of magical power. Three times per day as
    a standard action, a merlucent can replicate the effects of a single arcane spell
    cast within 20 feet of it, directing the spell's effect and choosing a target
    as if it were the caster. This echo uses the merlucent's caster level rather than
    that of the original spellcaster, and a merlucent can't echo any effect with a
    spell level greater than half the merlucent's own Hit Dice (generally limiting
    it to second-level spells). A merlucent can't echo the spells, spell-like abilities,
    or arcane echo effects created by other merlucents.
  Jellyfish Empathy (Ex): This ability functions as a druid's wild empathy ability,
    save that it works only on jellyfish. A merlucent gains a racial bonus on this
    check equal to its Hit Dice (normally +4). Jellyfish are normally mindless, but
    this empathic communication imparts upon them a modicum of implanted intelligence,
    allowing merlucents to train jellyfish and use them as guardians (though it does
    not grant them skills or feats).
  Poison (Ex): Tentacle-injury; save Fort DC 14; frequency 1/round for 4 rounds; effect
    1d3 Dex; cure 1 save. The save DC is Constitution-based.
  Transparent Flesh (Ex): A merlucent's transparent flesh becomes hazy and indistinct
    in water, granting it concealment while the creature is submerged.
  Vitrify (Su): |-
    A merlucent can produce a polyp and implant it in the ear of a willing or helpless creature over the course of 1 minute, during which the merlucent is flat-footed. The polyp begins slowly consuming its host's brain, transforming the creature's flesh into a transparent jelly and replacing its bone with delicate crystal. A creature that takes any amount of Intelligence damage from a merlucent polyp can breathe while underwater, but loses the ability to breathe air. If a humanoid creature takes ability damage in excess of its Intelligence score, it transforms into a new merlucent, losing all abilities or class levels it previously possessed. The polyp can be destroyed by any effect that removes disease, but the inability to breathe air persists until a creature's Intelligence damage is healed.

     Vitrify: Implantation; save Fort 12; onset 12 hours; frequency 1/day; effect 1d4 Int damage; cure 2 consecutive saves. The save DC is Charisma-based.
desc_long: |-
  Merlucents are strange creatures formed from the fusion of human and jellyfish. As a species, they are simple-minded ascetics. Individual clans claim small stretches of coastline where they hunt fish and shellfish, and scratch strange glyphs into coral, coaxing it to grow in unnatural though beautiful formations. Naturally sensitive to arcane energy, they settle in locations rife with ambient magic, such as along ley lines or near schools of magic built on islands or coasts. Local communities generally consider merlucents to be pests for stripping fishing grounds bare, but the aberrations also keep more aggressive aquatic threats away. This small blessing turns bane every 2 to 5 years when merlucents enter their mating phase and become extremely aggressive.

  To reproduce, each merlucent spawns dozens of antsized polyps, each of which must mature inside the skull of a humanoid host. Depending on the host, it can take anywhere from days to weeks for the tiny parasite to take over its host's mind and convert the bony, flesh-covered body into its own adult form. To support their children, merlucents conduct fanatical crusades, kidnapping surface dwellers to act as incubators. Relying on its members' stealth and paralytic poison, a single clan may snatch dozens of unwary sailors or coastal residents in a single season.

  Merlucents range from 4 to 5 feet in height and weigh around 180 pounds, though smaller or larger specimens may be spawned depending on the size of the host.

---

# Merlucent
A mane of long, writhing tentacles crowns this translucent, humanoid figure. A crystalline skeleton supports its faintly glowing flesh.
**Source** Pathfinder #104: Wrath of Thrune pg. 90
**XP** 800

CN Medium aberration (aquatic)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +7

##### Defense

**AC** 16, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +3 natural)
**hp** 26 (4d8+8)
**Fort** +3, **Ref** +4, **Will** +6
**Resist** cold 5

##### Offense
**Speed** 15 ft., swim 40 ft.
**Melee** 3 tentacles +6 (1d4+1 plus poison)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tentacle)
**Special Attacks** arcane _[[spells/Echo|echo]]_, poison, _[[universal monster rules/Pull|pull]]_ (tentacle, 5 ft.), vitrify
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +4)
Constant—_[[spells/Detect Magic|detect magic]]_
3/day—_[[spells/Delay Poison|delay poison]]_, light

##### Statistics
**Str** 12, **Dex** 16, **Con** 15, **Int** 11, **Wis** 14, **Cha** 11
**Base Atk** +3; **CMB** +4; **CMD** 17
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +6, Handle Animal +4, Perception +7, Stealth +10, Survival +11, Swim +14; **Racial Modifiers** +4 Survival
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 30 ft.
**SQ** jellyfish _[[feats/Empathy|empathy]]_, transparent flesh

##### Ecology

**Environment** any ocean
**Organization** solitary, hunting group (3–6), or clan (9–14)
**Treasure** incidental

### Special Abilities

**Arcane _Echo_ (Su)** Merlucents naturally _[[items/Mundane/Filter|filter]]_ arcane energies from the world around them, and can produce large displays of magical power. Three times per day as a standard action, a _[[monsters/Merlucent|merlucent]]_ can replicate the effects of a single arcane spell cast within 20 feet of it, directing the spell’s effect and choosing a target as if it were the caster. This _echo_ uses the _merlucent_’s caster level rather than that of the original spellcaster, and a _merlucent_ can’t _echo_ any effect with a spell level greater than half the _merlucent_’s own Hit Dice (generally limiting it to second-level spells). A _merlucent_ can’t _echo_ the spells, _spell-like abilities_, or arcane _echo_ effects created by other merlucents.

**Jellyfish _Empathy_ (Ex)** This ability functions as a _[[classes/Druid|druid]]_’s wild _empathy_ ability, save that it works only on jellyfish. A _merlucent_ gains a racial bonus on this check equal to its Hit Dice (normally +4). Jellyfish are normally mindless, but this empathic communication imparts upon them a modicum of implanted intelligence, allowing merlucents to train jellyfish and use them as guardians (though it does not grant them skills or feats).

**Poison (Ex)** Tentacle—injury; save Fort DC 14; frequency 1/round for 4 rounds; effect 1d3 Dex; cure 1 save. The save DC is Constitution-based.

**Transparent Flesh (Ex)** A _merlucent_’s transparent flesh becomes hazy and indistinct in water, granting it concealment while the creature is submerged.

**Vitrify (Su)** A _merlucent_ can produce a polyp and implant it in the ear of a willing or _[[conditions/Helpless|helpless]]_ creature over the course of 1 minute, during which the _merlucent_ is _flat-footed_. The polyp begins slowly consuming its host’s brain, transforming the creature’s flesh into a transparent jelly and replacing its bone with delicate crystal. A creature that takes any amount of Intelligence damage from a _merlucent_ polyp can breathe while _[[items/Weapon Magic Abilities/Underwater|underwater]]_, but loses the ability to breathe air. If a humanoid creature takes ability damage in excess of its Intelligence score, it transforms into a new _merlucent_, losing all abilities or class levels it previously possessed. The polyp can be destroyed by any effect that removes disease, but the inability to breathe air persists until a creature’s Intelligence damage is healed.

Vitrify: Implantation; save Fort 12; onset 12 hours; frequency 1/day; effect 1d4 Int damage; cure 2 consecutive saves. The save DC is Charisma-based.

##### Description

Merlucents are strange creatures formed from the fusion of human and jellyfish. As a species, they are simple-minded ascetics. Individual clans claim small stretches of coastline where they hunt fish and shellfish, and scratch strange glyphs into coral, coaxing it to grow in unnatural though beautiful formations. Naturally sensitive to arcane energy, they settle in locations rife with ambient magic, such as along ley lines or near schools of magic built on islands or coasts. Local communities generally consider merlucents to be pests for stripping fishing grounds bare, but the aberrations also keep more aggressive aquatic threats away. This small blessing turns _[[spells/Bane|bane]]_ every 2 to 5 years when merlucents enter their mating phase and become extremely aggressive.

To reproduce, each _merlucent_ spawns dozens of antsized polyps, each of which must mature inside the skull of a humanoid host. Depending on the host, it can take anywhere from days to weeks for the tiny parasite to take over its host’s mind and convert the bony, flesh-covered body into its own adult form. To support their children, merlucents conduct fanatical crusades, kidnapping surface dwellers to act as incubators. Relying on its members’ stealth and paralytic poison, a single clan may _[[feats/Snatch|snatch]]_ dozens of unwary sailors or coastal residents in a single season.

Merlucents range from 4 to 5 feet in height and weigh around 180 pounds, though smaller or larger specimens may be spawned depending on the size of the host.