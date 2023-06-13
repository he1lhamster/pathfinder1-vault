---
cssclass: [monsters]
title1: Troggle, Troggle Raider
desc_short: This troggle wears filthy studded leather armor and a dog collar, and
  carries a powerful bow on its back.
title2: Troggle Raider
CR: 6
sources:
- name: Monster Codex
  page: 160
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Troggle
classes:
- ranger 2
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 21
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    dex: 3
    natural: 5
    size: -1
HP:
  HP: 54
  long: 5d8+2d10+21
  HD: 7
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 10
  ref: 7
  will: 3
speeds:
  base: 45
attacks:
  melee:
  - - text: bite +11 (1d6+7 plus trip)
      entries:
      - - damage: 1d6+7
        - effect: trip
      attack: bite
      bonus:
      - 11
    - text: 2 claws +12 (1d4+7)
      entries:
      - - damage: 1d4+7
      count: 2
      attack: claws
      bonus:
      - 12
  ranged:
  - - text: composite shortbow +7 (1d8+7/×3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: composite shortbow
      bonus:
      - 7
  special:
  - combat style (natural weapon)
  - favored enemy (humans +2)
space: 10
reach: 10
ability_scores:
  STR: 24
  DEX: 17
  CON: 16
  INT: 7
  WIS: 10
  CHA: 3
BAB: 5
CMB: 13
CMD: 26
CMD_other: 30 vs. trip
feats:
- name: Combat Reflexes
- name: Fleet
- name: Iron Will
- name: Night Stalker
- is_bonus: true
  name: Skill Focus (Stealth)
- name: Weapon Focus (claws)
skills:
  Climb: 12
  Perception: 8
  Stealth: 10
    in dim light or darkness: 14
  Survival: 6
languages:
- Giant
special_qualities:
- ogre blood
- track +1
- wild empathy -2
gear:
  gear:
  - +1 studded leather
  - composite shortbow with 20 arrows
  - amulet of mighty fists +1
  - 49 gp
ecology:
  environment: cold hills and mountains
desc_long: Some troggles exhibit natural skill for hunting and tracking, and their
  ogre masters take advantage of these talents to create fast, deadly pets that excel
  at finding and killing humans for the stewpot.

---

# Troggle, Troggle Raider
This _[[monsters/Troggle|troggle]]_ wears filthy _[[items/Armor/Studded leather armor|studded leather armor]]_ and a _[[monsters/Dog|dog]]_ collar, and carries a powerful bow on its back.
**Source** Monster Codex pg. 160
**XP** 2,400
_Troggle_ _[[classes/Ranger|ranger]]_ 2
CE Large humanoid (giant)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 21, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +3 Dex, +5 natural, –1 size)
**hp** 54 (7 HD; 5d8+2d10+21); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +10, **Ref** +7, **Will** +3

##### Offense
**Speed** 45 ft.
**Melee** bite +11 (1d6+7 plus _[[universal monster rules/Trip|trip]]_), 2 claws +12 (1d4+7)
**Ranged** _[[items/Weapon/Composite shortbow|composite shortbow]]_ +7 (1d8+7/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** combat style (natural weapon), favored enemy (humans +2)

##### Statistics
**Str** 24, **Dex** 17, **Con** 16, **Int** 7, **Wis** 10, **Cha** 3
**Base Atk** +5; **CMB** +13; **CMD** 26 (30 vs. _trip_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Fleet|Fleet]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Night Stalker|Night Stalker]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Perception +8, Stealth +10 (+14 in dim light or _[[spells/Darkness|darkness]]_), Survival +6
**Languages** Giant
**SQ** _[[monsters/Ogre|ogre]]_ blood, track +1, wild _[[feats/Empathy|empathy]]_ –2
**Gear** +1 studded leather, _composite shortbow_ with 20 arrows, _[[items/Wondrous Item/Amulet of Mighty Fists +1|amulet of mighty fists +1]]_, 49 gp

##### Ecology

**Environment** cold hills and mountains

##### Description

Some troggles exhibit natural skill for hunting and tracking, and their _ogre_ masters take advantage of these talents to create fast, _[[items/Weapon Magic Abilities/Deadly|deadly]]_ pets that excel at finding and killing humans for the stewpot.