---
cssclass: [monsters]
title1: Heretic (Cultist)
title2: Heretic (Cultist)
CR: 2
sources:
- name: GameMastery Guide
  page: 278
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 600
race: Human
classes:
- cleric 3
alignment: NE
size: Medium
type: humanoid
initiative:
  bonus: 1
AC:
  AC: 18
  touch: 11
  flat_footed: 17
  components:
    armor: 6
    dex: 1
    shield: 1
HP:
  HP: 16
  long: 3d8+3
saves:
  fort: 4
  ref: 2
  will: 5
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk sickle +3 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk sickle
      bonus:
      - 3
  ranged:
  - - text: dart +3 (1d4)
      entries:
      - - damage: 1d4
      attack: dart
      bonus:
      - 3
  special:
  - channel negative energy 6/day (DC 14, 2d6)
spell_like_abilities:
  entries:
  - name: rebuke death
    source: default
    freq: 6/day
    other: 1d4+1
  - name: touch of evil
    source: default
    freq: 6/day
    other: 1 round
  sources:
  - name: default
    CL: 3
    concentration: 5
spells:
  entries:
  - is_domain_spell: true
    name: cure moderate wounds
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 14
  - name: hold person
    source: Cleric
    level: 2
    DC: 14
  - name: bane
    source: Cleric
    level: 1
    DC: 13
  - name: cause fear
    source: Cleric
    level: 1
    DC: 13
  - is_domain_spell: true
    name: cure light wounds
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 13
  - name: bleed
    source: Cleric
    level: 0
    DC: 12
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 3
    concentration: 5
    slots:
      0: at-will
    domains:
    - evil
    - healing
ability_scores:
  STR: 10
  DEX: 13
  CON: 12
  INT: 8
  WIS: 15
  CHA: 16
BAB: 2
CMB: 2
CMD: 13
feats:
- name: Alignment Channel
- name: Combat Casting
- name: Selective Channeling
skills:
  Knowledge (planes): 4
  Knowledge (religion): 4
  Linguistics: 4
  Perception: 3
  Sense Motive: 6
  Spellcraft: 3
languages:
- Abyssal
- Common
- Infernal
gear:
  combat:
  - bloodroot poison (1 dose)
  - vials of unholy water (2)
  other:
  - chainmail
  - light steel shield
  - darts (4)
  - masterwork sickle
  - silver unholy symbol
npc_boon: A cultist can hide the PCs or others they designate within a secret cult
  sanctuary for up to 3 days. They could also plant false evidence implicating an
  NPC as a cult member.
desc_long: |-
  Cultists are members of secret societies, meeting hooded and masked in dark masses and unspeakable, blasphemous rites. They gather the lay cult members and lead them in their maledictions, channeling for them the shadowed powers of the nether planes.

  Cultists can be found leading small cult cells or congregations of a half-dozen farmers, shipmates, bloodthirsty cannibals, or even misguided acolytes (CR 5). A pair of cultists might lead a larger cult of nine doomsayers or initiates (CR 8).

  Cultists might also serve as disciples of more powerful spellcasters. A pair of cultists can be acolytes of an evil medium (CR 6), three cultists might be apprenticed to a shaman (CR 7), four could follow a conjurist (CR 8), or up to a dozen cultists might follow a cult leader (CR 12).

---

# Heretic (Cultist)

**Source** GameMastery Guide pg. 278
**XP** 600
Human _[[classes/Cleric|cleric]]_ 3

NE Medium humanoid
**Init** +1; **Senses** Perception +3

##### Defense

**AC** 18, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 armor, +1 Dex, +1 _[[spells/Shield|shield]]_)
**hp** 16 (3d8+3)
**Fort** +4, **Ref** +2, **Will** +5

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Sickle|sickle]]_ +3 (1d6)
**Ranged** _[[items/Weapon/Dart|dart]]_ +3 (1d4)
**Special Attacks** channel negative energy 6/day (DC 14, 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +5)
6/day—_[[spells/Rebuke|rebuke]]_ death (1d4+1), _[[feats/Touch Of Evil|touch of evil]]_ (1 round)
**_Cleric_ Spells Prepared **(CL 3rd; concentration +5)
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Death Knell|death knell]]_ (DC 14), _[[spells/Hold Person|hold person]]_ (DC 14)
1st—_[[spells/Bane|bane]]_ (DC 13), _[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Doom|doom]]_ (DC 13)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 12), _[[spells/Guidance|guidance]]_, light, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains **Evil, Healing

##### Statistics
**Str** 10, **Dex** 13, **Con** 12, **Int** 8, **Wis** 15, **Cha** 16
**Base Atk** +2; **CMB** +2; **CMD** 13
**Feats** _[[feats/Alignment Channel|Alignment Channel]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Selective Channeling|Selective Channeling]]_
**Skills** Knowledge (planes) +4, Knowledge (religion) +4, Linguistics +4, Perception +3, Sense Motive +6, Spellcraft +3
**Languages** Abyssal, Common, Infernal
**Combat Gear** _[[poisons/Bloodroot|bloodroot]]_ poison (1 dose), vials of _[[items/Weapon Magic Abilities/Unholy|unholy]]_ water (2); **Other Gear** _[[items/Armor/Chainmail|chainmail]]_, _[[items/Shield/Light steel shield|light steel shield]]_, darts (4), masterwork _sickle_, silver _unholy_ symbol

**Boon **A _[[npcs/Cultist|cultist]]_ can hide the PCs or others they designate within a secret cult _[[spells/Sanctuary|sanctuary]]_ for up to 3 days. They could also plant false evidence implicating an NPC as a cult member.

Cultists are members of secret societies, meeting hooded and masked in dark masses and unspeakable, blasphemous rites. They gather the lay cult members and lead them in their maledictions, _[[items/Armor Magic Abilities/Channeling|channeling]]_ for them the shadowed powers of the nether planes.

Cultists can be found leading small cult cells or congregations of a half-dozen farmers, shipmates, _[[items/Armor Magic Abilities/Bloodthirsty|bloodthirsty]]_ cannibals, or even misguided acolytes (CR 5). A pair of cultists might lead a larger cult of nine doomsayers or initiates (CR 8).

Cultists might also serve as disciples of more powerful spellcasters. A pair of cultists can be acolytes of an evil _medium_ (CR 6), three cultists might be apprenticed to a _[[classes/Shaman|shaman]]_ (CR 7), four could follow a conjurist (CR 8), or up to a dozen cultists might follow a cult leader (CR 12).