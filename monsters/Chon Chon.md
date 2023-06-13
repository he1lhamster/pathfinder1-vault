---
cssclass: [monsters]
title1: Chon Chon
desc_short: This flying head has incredibly large ears that constantly flap to keep
  the creature aloft. It babbles to itself as it flies, as if to remind itself of
  secrets only it knows.
title2: Chon Chon
CR: 1/2
sources:
- name: 'Pathfinder #53: Tide of Honor'
  page: 82
  link: http://paizo.com/pathfinder/v5748btpy8mh0
XP: 200
alignment: CN
size: Tiny
type: aberration
initiative:
  bonus: 2
senses:
  darkvision: 60
auras:
- name: jabber
  radius: 15
  DC: 11
AC:
  AC: 14
  touch: 14
  flat_footed: 12
  components:
    dex: 2
    size: 2
HP:
  HP: 9
  long: 2d8
saves:
  fort: 0
  ref: 4
  will: 4
speeds:
  base: 10
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +1 (1d3-2)
      entries:
      - - damage: 1d3-2
      attack: bite
      bonus:
      - 1
  ranged:
  - - text: acid spit +5 (1d4 acid)
      entries:
      - - damage: 1d4
          type: acid
      attack: acid spit
      bonus:
      - 5
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 3
    concentration: 4
ability_scores:
  STR: 6
  DEX: 15
  CON: 10
  INT: 7
  WIS: 12
  CHA: 13
BAB: 1
CMB: 1
CMD: 9
feats:
- name: Lightning Reflexes
skills:
  Fly: 15
  Perception: 6
    to listen: 10
  _racial_mods:
    Perception:
      to listen: 4
languages:
- Common
ecology:
  environment: temperate or tropical forests or ruins
  organization: solitary, pair, flight (3-12)
  treasure_type: none
special_abilities:
  Acid Spit (Ex): A chon chon can spit a disgusting blob of acid at a single foe,
    making a ranged attack with a range of 30 feet and no range increment. A successful
    attack deals 1d4 points of acid damage and forces the target to make a DC 11 Fortitude
    saving throw to avoid becoming nauseated for 1 round. The save DC is Constitution-based.
  Jabber (Su): A chon chon endlessly mutters half-remembered spells and meaningless
    arcane formulae to itself. This jabbering creates a kind of magical static that
    interferes with spells being cast nearby. Any creature attempting to cast a spell
    within 15 feet of a chon chon must make a successful DC 11 concentration check
    or lose the spell. This is a sonic, mind-affecting effect. The concentration DC
    is Charisma-based.
desc_long: |-
  Chon chons appear to be human heads with ears so grotesquely enlarged that they can serve as f leshy wings. Their jealous hatred of all beings with full bodies easily counters their comical appearance, however. Accursed creatures drawn to places of dark magic and arcane disasters, chon chons possess the desires of the most obsessed magic users, but their dementia and twisted forms prevent them from ever obtaining the power they seek. Although these crazed beings loathe all things, they do find a vicious kind of solace among their own kind, not out of any sort of commiseration, but rather by wallowing in the pain of their own kind. Such hateful swarms gather to bear witness to each others' misery, inadvertently increasing the deadly efficacy of the entire group.

  A single chon chon is no larger than a human head and weighs 10 pounds at most. The creature's ears give it a total wingspan of 3 feet, making it appear much larger and more menacing.

---

# Chon Chon
This flying head has incredibly large ears that constantly flap to keep the creature aloft. It babbles to itself as it flies, as if to remind itself of secrets only it knows.
**Source** Pathfinder #53: Tide of Honor pg. 82
**XP** 200

CN Tiny aberration
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +6
**Aura** jabber (15 ft., DC 11)

##### Defense

**AC** 14, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 size)
**hp** 9 (2d8)
**Fort** +0, **Ref** +4, **Will** +4

##### Offense
**Speed** 10 ft., fly 60 ft. (good)
**Melee** bite +1 (1d3-2)
**Ranged** acid spit +5 (1d4 acid)
**Space** 2-1/2 ft., **Reach** 0 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
Constant-detect magic

##### Statistics
**Str** 6, **Dex** 15, **Con** 10, **Int** 7, **Wis** 12, **Cha** 13
**Base Atk** +1; **CMB** +1; **CMD** 9
**Feats** _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Fly +15, Perception +6 (+10 to listen); **Racial Modifiers** Perception (+4 to listen)
**Languages** Common

##### Ecology

**Environment** temperate or tropical forests or ruins
**Organization** solitary, pair, _[[universal monster rules/Flight|flight]]_ (3-12)
**Treasure** none

### Special Abilities

**Acid Spit (Ex) **A _[[monsters/Chon Chon|chon chon]]_ can spit a disgusting blob of acid at a single foe, making a ranged attack with a range of 30 feet and no range increment. A successful attack deals 1d4 points of acid damage and forces the target to make a DC 11 Fortitude saving throw to avoid becoming _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Constitution-based.

**Jabber (Su) **A _chon chon_ endlessly mutters half-remembered spells and meaningless arcane formulae to itself. This jabbering creates a kind of magical static that interferes with spells being cast nearby. Any creature attempting to cast a spell within 15 feet of a _chon chon_ must make a successful DC 11 concentration check or lose the spell. This is a sonic, mind-affecting effect. The concentration DC is Charisma-based.

##### Description

Chon chons appear to be human heads with ears so grotesquely enlarged that they can serve as f leshy wings. Their jealous hatred of all beings with full bodies easily counters their comical appearance, however. _[[feats/Accursed|Accursed]]_ creatures drawn to places of dark magic and arcane disasters, chon chons possess the desires of the most obsessed magic users, but their dementia and twisted forms prevent them from ever obtaining the power they seek. Although these crazed beings loathe all things, they do find a _[[items/Weapon Magic Abilities/Vicious|vicious]]_ kind of solace among their own kind, not out of any sort of commiseration, but rather by wallowing in the pain of their own kind. Such hateful swarms gather to bear _[[spells/Witness|witness]]_ to each others’ misery, inadvertently increasing the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ efficacy of the entire group.

A single _chon chon_ is no larger than a human head and weighs 10 pounds at most. The creature’s ears give it a total wingspan of 3 feet, making it appear much larger and more _[[items/Weapon Magic Abilities/Menacing|menacing]]_.