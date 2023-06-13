---
cssclass: [monsters]
title1: Troggle
desc_short: This leathery creature has a lanky, ogre-like shape, but walks on all
  fours. Its claws, teeth, tail, and gait give it a degenerate , bestial appearance.
title2: Troggle
CR: 4
sources:
- name: Monster Codex
  page: 160
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1200
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 15
  touch: 10
  flat_footed: 14
  components:
    dex: 1
    natural: 5
    size: -1
HP:
  HP: 32
  long: 5d8+10
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 6
  ref: 2
  will: 3
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +7 (1d6+5 plus trip)
      entries:
      - - damage: 1d6+5
        - effect: trip
      attack: bite
      bonus:
      - 7
    - text: 2 claws +7 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 7
space: 10
reach: 10
ability_scores:
  STR: 20
  DEX: 13
  CON: 14
  INT: 5
  WIS: 10
  CHA: 5
BAB: 3
CMB: 9
CMD: 20
CMD_other: 24 vs. trip
feats:
- name: Combat Reflexes
- name: Iron Will
- name: Night Stalker
- is_bonus: true
  name: Skill Focus (Stealth)
skills:
  Climb: 9
  Perception: 6
  Stealth: 1
    in dim light or darkness: 5
  _racial_mods:
    Stealth:
      in dim light or darkness: 4
languages:
- Giant
special_qualities:
- ogre blood
ecology:
  environment: cold hills and mountains
  organization: solitary, pair, or gang (3-4)
  treasure_type: half
special_abilities:
  Ogre Blood (Ex): Troggles count as ogres for the purpose of any effects related
    to race.
desc_long: These dim-witted creatures are a mongrel cross between a troll and an ogre,
  combining the worst features of each. They usually act like animals and move on
  all fours, but can rear up on their hind legs to attack with their sharp claws and
  vicious bites. Some ogres keep them as pets, treating them as exceptionally stupid
  but hilarious kinfolk. Trolls usually kill troggles on sight, and have been known
  to band together to wipe out entire ogre clans that possess troggles.

---

# Troggle
This leathery creature has a lanky, ogre-like shape, but walks on all fours. Its claws, teeth, tail, and gait give it a degenerate , bestial appearance.
**Source** Monster Codex pg. 160
**XP** 1,200
CE Large humanoid (giant)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +6

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 Dex, +5 natural, –1 size)
**hp** 32 (5d8+10); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +6, **Ref** +2, **Will** +3

##### Offense
**Speed** 40 ft.
**Melee** bite +7 (1d6+5 plus _[[universal monster rules/Trip|trip]]_), 2 claws +7 (1d4+5)
**Space** 10 ft., **Reach** 10 ft.

##### Statistics
**Str** 20, **Dex** 13, **Con** 14, **Int** 5, **Wis** 10, **Cha** 5
**Base Atk** +3; **CMB** +9; **CMD** 20 (24 vs. _trip_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Night Stalker|Night Stalker]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** _[[universal monster rules/Climb|Climb]]_ +9, Perception +6, Stealth +1 (+5 in dim light or _[[spells/Darkness|darkness]]_); **Racial Modifiers** +4 Stealth in dim light or _darkness_
**Languages** Giant
**SQ** _[[monsters/Ogre|ogre]]_ blood

##### Ecology

**Environment** cold hills and mountains
**Organization** solitary, pair, or gang (3–4)
**Treasure** half

### Special Abilities

**_Ogre_ Blood (Ex)** Troggles count as ogres for the purpose of any effects related to race.

##### Description

These dim-witted creatures are a mongrel cross between a _[[monsters/Troll|troll]]_ and an _ogre_, combining the worst features of each. They usually act like animals and move on all fours, but can rear up on their hind legs to attack with their sharp claws and _[[items/Weapon Magic Abilities/Vicious|vicious]]_ bites. Some ogres keep them as pets, treating them as exceptionally stupid but hilarious kinfolk. Trolls usually kill troggles on sight, and have been known to band together to wipe out entire _ogre_ clans that possess troggles.