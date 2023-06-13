---
cssclass: [monsters]
title1: Careful Initiate
title2: Careful Initiate
CR: 1/2
sources:
- name: NPC Codex
  page: 96
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 200
race: Human
classes:
- monk 1
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 3
AC:
  AC: 16
  touch: 16
  flat_footed: 12
  components:
    dex: 3
    dodge: 1
    wis: 2
HP:
  HP: 9
  long: 1d8+1
saves:
  fort: 2
  ref: 5
  will: 4
speeds:
  base: 30
attacks:
  melee:
  - - text: unarmed strike +3 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: unarmed strike
      bonus:
      - 3
  - - text: kama +3 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: kama
      bonus:
      - 3
  - - text: unarmed strike flurry of blows +2/+2 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: unarmed strike flurry of blows
      bonus:
      - 2
      - 2
  ranged:
  - - text: light crossbow +3 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 3
  - - text: shuriken +3 (1d2+1)
      entries:
      - - damage: 1d2+1
      attack: shuriken
      bonus:
      - 3
  - - text: shuriken flurry of blows +2/+2 (1d2+1)
      entries:
      - - damage: 1d2+1
      attack: shuriken flurry of blows
      bonus:
      - 2
      - 2
  special:
  - flurry of blows
  - stunning fist (1/day, DC 12)
tactics:
  Before Combat: The monk uses Stealth to catch enemies off-guard, starting any surprise
    round with Stunning Fist.
  During Combat: The monk never fights multiple opponents if she can help it, and
    prefers to use her shuriken with a flurry of blows before entering melee.
ability_scores:
  STR: 12
  DEX: 16
  CON: 10
  INT: 13
  WIS: 15
  CHA: 8
BAB: 0
CMB: 1
CMD: 17
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Unarmed Strike
- name: Stunning Fist
- name: Weapon Finesse
skills:
  Acrobatics: 7
  Knowledge (history): 5
  Knowledge (religion): 5
  Perception: 6
  Sense Motive: 6
  Stealth: 7
languages:
- Common
- Dwarven
gear:
  combat:
  - potions of cure light wounds (2)
  - potions of mage armor (2)
  - potions of magic weapon (2)
  other:
  - kama
  - light crossbow with 10 bolts
  - shuriken (20)
  - 50 gp
desc_long: Neophyte monks are often eager to prove their mettle in battle, but just
  as often their strict training means they tend to act tentatively when deprived
  of their master's guidance.

---

# Careful Initiate

**Source** NPC Codex pg. 96
**XP** 200
Human _[[classes/Monk|monk]]_ 1

LN Medium humanoid (human)
**Init** +3; **Senses** Perception +6

##### Defense

**AC** 16, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +2 Wis)
**hp** 9 (1d8+1)
**Fort** +2, **Ref** +5, **Will** +4

##### Offense
**Speed** 30 ft.
**Melee** unarmed strike +3 (1d6+1) or _[[items/Weapon/Kama|kama]]_ +3 (1d6+1) or unarmed strike flurry of blows +2/+2 (1d6+1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +3 (1d8/19–20) or shuriken +3 (1d2+1) or shuriken flurry of blows +2/+2 (1d2+1)
**Special Attacks** flurry of blows, _[[feats/Stunning Fist|stunning fist]]_ (1/day, DC 12)

### Tactics

**Before Combat** The _monk_ uses Stealth to catch enemies off-guard, starting any surprise round with _Stunning Fist_.
**During Combat** The _monk_ never fights multiple opponents if she can help it, and prefers to use her shuriken with a flurry of blows before entering melee.

##### Statistics
**Str** 12, **Dex** 16, **Con** 10, **Int** 13, **Wis** 15, **Cha** 8
**Base Atk** +0; **CMB** +1; **CMD** 17
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _Stunning Fist_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +7, Knowledge (history, religion) +5, Perception +6, Sense Motive +6, Stealth +7
**Languages** Common, Dwarven
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), potions of _[[spells/Mage Armor|mage armor]]_ (2), potions of _[[spells/Magic Weapon|magic weapon]]_ (2); **Other Gear** _kama_, _light crossbow_ with 10 bolts, shuriken (20), 50 gp

Neophyte monks are often eager to prove their mettle in battle, but just as often their strict _[[items/Weapon Magic Abilities/Training|training]]_ means they tend to act tentatively when deprived of their master’s _[[spells/Guidance|guidance]]_.