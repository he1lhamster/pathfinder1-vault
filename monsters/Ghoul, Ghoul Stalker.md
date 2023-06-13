---
cssclass: [monsters]
title1: Ghoul, Ghoul Stalker
title2: Ghoul Stalker
CR: 6
sources:
- name: Monster Codex
  page: 82
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Ghoul
classes:
- rogue 6
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 15
  flat_footed: 13
  components:
    armor: 1
    dex: 5
    natural: 2
HP:
  HP: 74
  long: 8d8+38
saves:
  fort: 5
  ref: 10
  will: 8
defensive_abilities:
- channel resistance +2
- evasion
- trap sense +2
- uncanny dodge
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +8 (1d6+3 plus disease and paralysis)
      entries:
      - - damage: 1d6+3
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 8
    - text: 2 claws +8 (1d6+3 plus paralysis)
      entries:
      - - damage: 1d6+3
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 8
  ranged:
  - - text: +1 composite shortbow +10/+10 (1d6+4/×3)
      entries:
      - - damage: 1d6+4
          crit_multiplier: 3
      attack: +1 composite shortbow
      bonus:
      - 10
      - 10
  - - text: +1 composite shortbow +12 (1d6+4/×3)
      entries:
      - - damage: 1d6+4
          crit_multiplier: 3
      attack: +1 composite shortbow
      bonus:
      - 12
  special:
  - disease (DC 14)
  - paralysis (1d4+1 rounds, DC 14, elves are immune to this effect)
  - sneak attack +3d6
ability_scores:
  STR: 17
  DEX: 20
  CON:
  INT: 13
  WIS: 16
  CHA: 16
BAB: 5
CMB: 8
CMD: 23
feats:
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Toughness
- name: Weapon Focus (composite shortbow)
skills:
  Acrobatics: 16
  Bluff: 10
  Climb: 14
  Disable Device: 8
  Escape Artist: 16
  Intimidate: 10
  Knowledge (dungeoneering): 12
  Perception: 14
  Sense Motive: 14
  Stealth: 16
languages:
- Common
special_qualities:
- rogue talents (finesse rogue, ledge walker, weapon training)
- trapfinding +3
gear:
  combat:
  - +1 frost arrows (4)
  - +1 human-bane arrows (3)
  - potion of inflict light wounds
  other:
  - +1 composite shortbow with 20 arrows
  - bracers of armor +1
  - 62 gp
ecology:
  environment: any land
desc_long: While all ghouls are quiet and deadly in the night, these ghouls specialize
  in striking from cover or exploiting tactical advantages. They set up ambushes or
  fight using group tactics to claim their prey.

---

# Ghoul, Ghoul Stalker

**Source** Monster Codex pg. 82
**XP** 2,400
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Rogue|rogue]]_ 6
CE Medium undead
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14

##### Defense

**AC** 18, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+1 armor, +5 Dex, +2 natural)
**hp** 74 (8d8+38)
**Fort** +5, **Ref** +10, **Will** +8
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2, evasion, trap sense +2, uncanny _[[feats/Dodge|dodge]]_; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** bite +8 (1d6+3 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +8 (1d6+3 plus _paralysis_)
**Ranged** +1 _[[items/Weapon/Composite shortbow|composite shortbow]]_ +10/+10 (1d6+4/×3) or +1 _composite shortbow_ +12 (1d6+4/×3)
**Special Attacks** disease (DC 14), _paralysis_ (1d4+1 rounds, DC 14, elves are immune to this effect), sneak attack +3d6

##### Statistics
**Str** 17, **Dex** 20, **Con** —, **Int** 13, **Wis** 16, **Cha** 16
**Base Atk** +5; **CMB** +8; **CMD** 23
**Feats** _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite shortbow_)
**Skills** Acrobatics +16, Bluff +10, _[[universal monster rules/Climb|Climb]]_ +14, Disable Device +8, Escape Artist +16, Intimidate +10, Knowledge (dungeoneering) +12, Perception +14, Sense Motive +14, Stealth +16
**Languages** Common
**SQ** _rogue_ talents (finesse _rogue_, _[[feats/Ledge Walker|ledge walker]]_, weapon _[[items/Weapon Magic Abilities/Training|training]]_), trapfinding +3
**Combat Gear** +1 frost arrows (4), +1 human-bane arrows (3), potion of _[[spells/Inflict Light Wounds|inflict light wounds]]_; **Other Gear** +1 _composite shortbow_ with 20 arrows, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, 62 gp

##### Ecology

**Environment** any land

##### Description

While all ghouls are quiet and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ in the night, these ghouls specialize in striking from cover or exploiting tactical advantages. They set up ambushes or fight using group tactics to claim their prey.