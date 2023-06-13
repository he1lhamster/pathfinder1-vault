---
cssclass: [monsters]
title1: Serpentfolk, Serpentfolk Spy
title2: Serpentfolk Spy
CR: 5
sources:
- name: Monster Codex
  page: 202
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Advanced
classes:
- serpentfolk rogue 1
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 19
  touch: 16
  flat_footed: 13
  components:
    dex: 6
    natural: 3
HP:
  HP: 56
  long: 5d10+1d8+25
  HD: 6
saves:
  fort: 7
  ref: 12
  will: 5
immunities:
- mind-affecting effects
- paralysis
- poison
SR: 16
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 short sword +12 (1d6+2/19-20)
      entries:
      - - damage: 1d6+2
          crit_range: 19-20
      attack: +1 short sword
      bonus:
      - 12
    - text: bite +6 (1d6 plus poison)
      entries:
      - - damage: 1d6
        - effect: poison
      attack: bite
      bonus:
      - 6
  - - text: mwk dagger +12 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 12
    - text: bite +6 (1d6 plus poison)
      entries:
      - - damage: 1d6
        - effect: poison
      attack: bite
      bonus:
      - 6
  ranged:
  - - text: mwk hand crossbow +12 (1d4/19-20 plus black adder venom)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: black adder venom
      attack: mwk hand crossbow
      bonus:
      - 12
  special:
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
    DC: 16
    other: humanoid form only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  - name: blur
    source: default
    freq: 1/day
  - name: mirror image
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 4
    concentration: 9
tactics:
  During Combat: A serpentfolk spy lures and harries prey with telepathic taunts and
    ventriloquism before striking from ambush with poisoned weapons and venomous bites.
    It conceals its true numbers and position with blur, disguise self, or mirror
    image.
ability_scores:
  STR: 12
  DEX: 23
  CON: 19
  INT: 18
  WIS: 13
  CHA: 20
BAB: 5
CMB: 6
CMD: 22
feats:
- name: Great Fortitude
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Acrobatics: 15
  Bluff: 13
  Diplomacy: 13
  Disable Device: 11
  Disguise: 15
  Escape Artist: 22
  Intimidate: 13
  Knowledge (arcana): 9
  Knowledge (local): 8
  Perception: 10
  Sense Motive: 10
  Sleight of Hand: 10
  Spellcraft: 9
  Stealth: 10
  Use Magic Device: 20
  _racial_mods:
    Escape Artist:
      _: 8
    Use Magic Device:
      _: 4
languages:
- Aklo
- Common
- Draconic
- Undercommon
- telepathy 100 ft.
special_qualities:
- trapfinding +1
gear:
  combat:
  - black adder venom (3 doses)
  other:
  - +1 short sword
  - mwk dagger
  - mwk hand crossbow with 10 bolts
  - thieves' tools
  - 77 gp
ecology:
  environment: any land (usually jungles or underground)
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 16; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: A serpentfolk spy monitors activity in surface settlements, noting authority
  figures, defenses, and those who could be bribed or coerced into serving the serpentfolk
  empire. While most serpentfolk spies describe their professions in terms of analyzing
  weaknesses and preparing for the eventual large-scale assault on the surface world,
  the truth is that many spies (and their masters) have immediate goals in mind. Spies
  often stake out powerful priests and arcanists, posing as fellow scholars or simple
  servitors, in order to gain access to knowledge and arcane lore not readily available
  in their subterranean caverns. Given their long life spans and reptilian patience,
  these individuals may infiltrate an organization and stay implanted there for years,
  waiting for a choice artifact or tome to present itself. Once it does, the spy absconds
  with the relic and retreats back to the serpentfolk city of its paymasters-killing
  any warmbloods who stand in its way.

---

# Serpentfolk, Serpentfolk Spy

**Source** Monster Codex pg. 202
**XP** 1,600
Advanced _[[monsters/Serpentfolk|serpentfolk]]_ _[[classes/Rogue|rogue]]_ 1

NE Medium monstrous humanoid
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +10

##### Defense

**AC** 19, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+6 Dex, +3 natural)
**hp** 56 (6 HD; 5d10+1d8+25)
**Fort** +7, **Ref** +12, **Will** +5
**Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison; **SR** 16

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Short sword|short sword]]_ +12 (1d6+2/19–20), bite +6 (1d6 plus poison) or mwk _[[items/Weapon/Dagger|dagger]]_ +12 (1d4+1/19–20), bite +6 (1d6 plus poison)
**Ranged** mwk _[[items/Weapon/Hand crossbow|hand crossbow]]_ +12 (1d4/19–20 plus _[[poisons/Black Adder Venom|black adder venom]]_)
**Special Attacks** sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +9)
At will—_[[spells/Disguise Self|disguise self]]_ (DC 16, humanoid form only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
1/day—_[[spells/Blur|blur]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)

### Tactics

**During Combat** A _serpentfolk_ spy lures and harries prey with telepathic taunts and _ventriloquism_ before striking from ambush with poisoned weapons and venomous bites. It conceals its true numbers and position with _blur_, _disguise self_, or _mirror image_.

##### Statistics
**Str** 12, **Dex** 23, **Con** 19, **Int** 18, **Wis** 13, **Cha** 20
**Base Atk** +5; **CMB** +6; **CMD** 22
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +15, Bluff +13, Diplomacy +13, Disable Device +11, Disguise +15, Escape Artist +22, Intimidate +13, Knowledge (arcana) +9, Knowledge (local) +8, Perception +10, Sense Motive +10, Sleight of Hand +10, Spellcraft +9, Stealth +10, Use Magic Device +20; **Racial Modifiers** +8 Escape Artist, +4 Use Magic Device
**Languages** Aklo, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** trapfinding +1
**Combat Gear** _black adder venom_ (3 doses); **Other Gear** +1 _short sword_, mwk _dagger_, mwk _hand crossbow_ with 10 bolts, thieves’ tools, 77 gp

##### Ecology

**Environment** any land (usually jungles or underground)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 16; frequency 1/round for 6 rounds; effect 1d2 Str; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

A _serpentfolk_ spy monitors activity in surface settlements, noting authority figures, defenses, and those who could be bribed or coerced into serving the _serpentfolk_ empire. While most _serpentfolk_ spies describe their professions in terms of analyzing weaknesses and preparing for the eventual large-scale assault on the surface world, the truth is that many spies (and their masters) have immediate goals in mind. Spies often stake out powerful priests and arcanists, posing as fellow scholars or simple servitors, in order to gain access to knowledge and arcane lore not readily available in their subterranean caverns. Given their long life spans and reptilian patience, these individuals may infiltrate an organization and stay implanted there for years, waiting for a choice artifact or tome to present itself. Once it does, the spy absconds with the relic and retreats back to the _serpentfolk_ city of its paymasters—killing any warmbloods who stand in its way.