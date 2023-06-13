---
cssclass: [monsters]
title1: Ghoul, Ghoul Creeper
title2: Ghoul Creeper
CR: 3
sources:
- name: Monster Codex
  page: 82
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Ghoul
classes:
- rogue 3
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    armor: 2
    dex: 4
    natural: 2
HP:
  HP: 37
  long: 5d8+15
saves:
  fort: 4
  ref: 7
  will: 7
defensive_abilities:
- channel resistance +2
- evasion
- trap sense +1
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +7 (1d6+3 plus disease and paralysis)
      entries:
      - - damage: 1d6+3
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 7
    - text: 2 claws +7 (1d6+3 plus paralysis)
      entries:
      - - damage: 1d6+3
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 7
  ranged:
  - - text: mwk light crossbow +8 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 8
  special:
  - disease (DC 14)
  - paralysis (1d4+1 rounds, DC 14, elves are immune to this effect)
  - sneak attack +2d6
ability_scores:
  STR: 17
  DEX: 19
  CON:
  INT: 13
  WIS: 16
  CHA: 16
BAB: 3
CMB: 6
CMD: 20
feats:
- name: Bag of Bones
- name: Power Attack
- name: Weapon Finesse
skills:
  Acrobatics: 12
  Bluff: 11
  Climb: 11
  Disable Device: 5
  Escape Artist: 17
  Intimidate: 11
  Perception: 11
  Sleight of Hand: 12
  Stealth: 12
languages:
- Common
- Undercommon
special_qualities:
- rogue talents (bleeding attack +2)
- trapfinding +1
gear:
  combat:
  - potion of greater magic fang
  - potion of inflict moderate wounds
  - tanglefoot bag
  other:
  - leather armor
  - mwk light crossbow with 20 arrows
  - 204 gp
ecology:
  environment: any land
desc_long: While all ghouls are quiet and deadly in the night, these ghouls specialize
  in striking from cover or exploiting tactical advantages. They set up ambushes or
  fight using group tactics to claim their prey.

---

# Ghoul, Ghoul Creeper

**Source** Monster Codex pg. 82
**XP** 800
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Rogue|rogue]]_ 3
CE Medium undead
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 armor, +4 Dex, +2 natural)
**hp** 37 (5d8+15)
**Fort** +4, **Ref** +7, **Will** +7
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2, evasion, trap sense +1; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** bite +7 (1d6+3 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +7 (1d6+3 plus _paralysis_)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d8/19–20)
**Special Attacks** disease (DC 14), _paralysis_ (1d4+1 rounds, DC 14, elves are immune to this effect), sneak attack +2d6

##### Statistics
**Str** 17, **Dex** 19, **Con** —, **Int** 13, **Wis** 16, **Cha** 16
**Base Atk** +3; **CMB** +6; **CMD** 20
**Feats** _[[feats/Bag Of Bones|Bag of Bones]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +12, Bluff +11, _[[universal monster rules/Climb|Climb]]_ +11, Disable Device +5, Escape Artist +17, Intimidate +11, Perception +11, Sleight of Hand +12, Stealth +12
**Languages** Common, Undercommon
**SQ** _rogue_ talents (bleeding attack +2), trapfinding +1
**Combat Gear** potion of greater _[[spells/Magic Fang|magic fang]]_, potion of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, mwk _light crossbow_ with 20 arrows, 204 gp

##### Ecology

**Environment** any land

##### Description

While all ghouls are quiet and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ in the night, these ghouls specialize in striking from cover or exploiting tactical advantages. They set up ambushes or fight using group tactics to claim their prey.