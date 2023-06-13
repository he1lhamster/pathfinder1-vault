---
cssclass: [monsters]
title1: Bat, Skaveling
desc_short: 'This monstrously sized, undead bat has mottled, decayed flesh and eyes
  that smolder with an unholy green glow. '
title2: Skaveling
CR: 5
sources:
- name: Bestiary 2
  page: 42
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 1600
alignment: CE
size: Large
type: undead
initiative:
  bonus: 7
senses:
  blindsense: 120
AC:
  AC: 19
  touch: 13
  flat_footed: 15
  components:
    dex: 3
    natural: 6
    size: -1
HP:
  HP: 58
  long: 9d8+18
saves:
  fort: 5
  ref: 6
  will: 8
immunities:
- undead traits
speeds:
  base: 20
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +10 (2d8+7 plus disease and paralysis)
      entries:
      - - damage: 2d8+7
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 10
  special:
  - screech
  - paralysis (1d4+1 rounds, DC 16)
space: 10
reach: 5
ability_scores:
  STR: 21
  DEX: 17
  CON:
  INT: 8
  WIS: 15
  CHA: 14
BAB: 6
CMB: 12
CMD: 26
feats:
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Mobility
- name: Skill Focus (Stealth)
skills:
  Fly: 13
  Perception: 14
    when using blindsense: 18
  Stealth: 14
  _racial_mods:
    Perception:
      when using blindsense: 4
languages:
- Undercommon
ecology:
  environment: any underground
  organization: solitary or colony (2-8)
  treasure_type: incidental
special_abilities:
  Disease (Su): 'Ghoul Fever: Bite-injury; save Fort DC 16; onset 1 day; frequency
    1/day; effect 1d3 Con and 1d3 Dex damage; cure 2 consecutive saves. The save DC
    is Charisma-based. A humanoid who dies of ghoul fever rises as a ghoul at the
    next midnight (see ghouls).'
  Screech (Su): Once per day as a standard action, a skaveling can screech as a mobat,
    save that those who are affected are stunned for 1d3 rounds unless they make a
    DC 16 Fortitude save. The save DC is Charisma-based.
desc_long: Known in some circles as ghoul bats, skavelings are the hideous result
  of necromantic manipulation by urdefhans, who create them from mobats specially
  raised on diets of fungus and humanoid flesh. Upon reaching maturity, urdefhans
  ritually slay the bats using necrotic poisons, then raise the corpses to serve as
  mounts and guardians.

---

# Bat, Skaveling
This monstrously sized, undead bat has mottled, decayed flesh and eyes that smolder with an _[[items/Weapon Magic Abilities/Unholy|unholy]]_ green glow.

**Source** Bestiary 2 pg. 42
**XP** 1,600
CE Large undead
**Init** +7; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft.; Perception +14

##### Defense

**AC** 19, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 Dex, +6 natural, –1 size)
**hp** 58 (9d8+18)
**Fort** +5, **Ref** +6, **Will** +8
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 20 ft., fly 40 ft. (good)
**Melee** bite +10 (2d8+7 plus disease and _[[universal monster rules/Paralysis|paralysis]]_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[spells/Screech|screech]]_, _paralysis_ (1d4+1 rounds, DC 16)

##### Statistics
**Str** 21, **Dex** 17, **Con** —, **Int** 8, **Wis** 15, **Cha** 14
**Base Atk** +6; **CMB** +12; **CMD** 26
**Feats** Dodge, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Fly +13, Perception +14 (+18 when using _blindsense_), Stealth +14; **Racial Modifiers** +4 Perception when using _blindsense_
**Languages** Undercommon

##### Ecology

**Environment** any underground
**Organization** solitary or colony (2–8)
**Treasure** incidental

### Special Abilities

**Disease (Su)** _[[diseases/Ghoul Fever|Ghoul Fever]]_: Bite—injury; save Fort DC 16; onset 1 day; frequency 1/day; effect 1d3 Con and 1d3 Dex damage; cure 2 consecutive saves. The save DC is Charisma-based. A humanoid who dies of _ghoul fever_ rises as a _[[monsters/Ghoul|ghoul]]_ at the next midnight (see ghouls).
**_Screech_ (Su)** Once per day as a standard action, a skaveling can _screech_ as a mobat, save that those who are affected are _[[conditions/Stunned|stunned]]_ for 1d3 rounds unless they make a DC 16 Fortitude save. The save DC is Charisma-based.

##### Description

Known in some circles as _ghoul_ bats, skavelings are the hideous result of necromantic manipulation by urdefhans, who create them from mobats specially raised on diets of fungus and humanoid flesh. Upon reaching maturity, urdefhans ritually slay the bats using necrotic poisons, then raise the corpses to serve as mounts and guardians.