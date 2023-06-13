---
cssclass: [monsters]
title1: Boggard, Boggard Brute
title2: Boggard Brute
CR: 3
sources:
- name: Monster Codex
  page: 10
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Boggard
classes:
- fighter 1
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    armor: 2
    dex: 1
    natural: 3
HP:
  HP: 34
  long: 3d8+1d10+16
  HD: 4
saves:
  fort: 8
  ref: 2
  will: 2
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: mwk morningstar +9 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: mwk morningstar
      bonus:
      - 9
    - text: tongue +2 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 2
      touch: true
  ranged:
  - - text: mwk javelin +5 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: mwk javelin
      bonus:
      - 5
  special:
  - terrifying croak (DC 13)
tactics:
  During Combat: The boggard brute throws his javelins before rushing into combat.
ability_scores:
  STR: 19
  DEX: 13
  CON: 16
  INT: 6
  WIS: 13
  CHA: 10
BAB: 3
CMB: 7
CMD: 18
feats:
- name: Intimidating Prowess
- name: Toughness
- name: Weapon Focus (morningstar)
skills:
  Acrobatics: 4
    when jumping: 20
  Intimidate: 9
  Perception: 5
  Stealth: 0
    in swamps: 8
  Swim: 12
languages:
- Boggard
special_qualities:
- hold breath
- swamp stride
gear:
  combat:
  - potions of barkskin (2)
  other:
  - leather armor
  - mwk javelins (2)
  - mwk morningstar
  - 132 gp
ecology:
  environment: temperate marshes
desc_long: Boggard brutes may be armed with primitive-looking weapons, yet their terrifying
  strength makes them as deadly as any knight in armor.

---

# Boggard, Boggard Brute

**Source** Monster Codex pg. 10
**XP** 800
_[[monsters/Boggard|Boggard]]_ _[[classes/Fighter|fighter]]_ 1
CE Medium humanoid (_boggard_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 armor, +1 Dex, +3 natural)
**hp** 34 (4 HD; 3d8+1d10+16)
**Fort** +8, **Ref** +2, **Will** +2

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** mwk _[[items/Weapon/Morningstar|morningstar]]_ +9 (1d8+6), tongue +2 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** mwk _[[items/Weapon/Javelin|javelin]]_ +5 (1d6+4)
**Special Attacks** terrifying croak (DC 13)

### Tactics

**During Combat **The _boggard_ brute throws his javelins before rushing into combat.

##### Statistics
**Str** 19, **Dex** 13, **Con** 16, **Int** 6, **Wis** 13, **Cha** 10
**Base Atk** +3; **CMB** +7; **CMD** 18
**Feats** _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_morningstar_)
**Skills** Acrobatics +4 (+20 when jumping), Intimidate +9, Perception +5, Stealth +0 (+8 in swamps), Swim +12
**Languages** _Boggard_
**SQ** _[[universal monster rules/Hold Breath|hold breath]]_, swamp stride
**Combat Gear** potions of _[[spells/Barkskin|barkskin]]_ (2); **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, mwk javelins (2), mwk _morningstar_, 132 gp

##### Ecology

**Environment** temperate marshes

##### Description

_Boggard_ brutes may be armed with primitive-looking weapons, yet their terrifying strength makes them as _[[items/Weapon Magic Abilities/Deadly|deadly]]_ as any _[[npcs/Knight|knight]]_ in armor.