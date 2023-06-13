---
cssclass: [monsters]
title1: Chon Chon, Chon Chon Swarm
title2: Chon Chon Swarm
CR: 3
sources:
- name: 'Pathfinder #53: Tide of Honor'
  page: 82
  link: http://paizo.com/pathfinder/v5748btpy8mh0
XP: 800
alignment: CN
size: Tiny
type: aberration
subtypes:
- swarm
initiative:
  bonus: 6
senses:
  darkvision: 60
auras:
- name: jabber
  radius: 15
  DC: 11
AC:
  AC: 16
  touch: 16
  flat_footed: 14
  components:
    dex: 2
    insight: 2
    size: 2
HP:
  HP: 27
  long: 6d8
saves:
  fort: 2
  ref: 6
  will: 6
speeds:
  base: 10
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: swarm +6 (2d6)
      entries:
      - - damage: 2d6
      attack: swarm
      bonus:
      - 6
  ranged:
  - - text: acid spit +8 (2d4 acid)
      entries:
      - - damage: 2d4
          type: acid
      attack: acid spit
      bonus:
      - 8
  special:
  - babble
  - distraction (DC 13)
space: 10
reach: 0
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 7
    concentration: 8
ability_scores:
  STR: 10
  DEX: 15
  CON: 10
  INT: 7
  WIS: 12
  CHA: 13
BAB: 4
CMB: 4
CMD: 14
feats:
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
skills:
  Fly: 19
  Perception: 8
    to listen: 14
  _racial_mods:
    Perception:
      to listen: 4
languages:
- Common (cannot speak)
ecology:
  environment: temperate or tropical forests or ruins
  organization: solitary
  treasure_type: none
special_abilities:
  Acid Spit (Ex): A chon chon can spit a disgusting blob of acid at a single foe,
    making a ranged attack with a range of 30 feet and no range increment. A successful
    attack deals 2d4 points of acid damage and forces the target to make a DC 13 Fortitude
    saving throw to avoid becoming nauseated for 1 round. The save DC is Constitution-based.
  Jabber (Su): |-
    A chon chon swarm mutters even more loudly than a solitary chon chon. Any creature attempting to cast a spell within 30 feet of a chon chon must make a successful DC 11 concentration check or lose the spell. This is a sonic, mindaffecting effect. The concentration DC is Charisma-based.

    Chon chons appear to be human heads with ears so grotesquely enlarged that they can serve as f leshy wings. Their jealous hatred of all beings with full bodies easily counters their comical appearance, however. Accursed creatures drawn to places of dark magic and arcane disasters, chon chons possess the desires of the most obsessed magic users, but their dementia and twisted forms prevent them from ever obtaining the power they seek. Although these crazed beings loathe all things, they do find a vicious kind of solace among their own kind, not out of any sort of commiseration, but rather by wallowing in the pain of their own kind. Such hateful swarms gather to bear witness to each others' misery, inadvertently increasing the deadly efficacy of the entire group.

    A single chon chon is no larger than a human head and weighs 10 pounds at most. The creature's ears give it a total wingspan of 3 feet, making it appear much larger and more menacing.
desc_long: ''

---

# Chon Chon, Chon Chon Swarm

**Source** Pathfinder #53: Tide of Honor pg. 82
**XP** 800

CN Tiny aberration (swarm)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +8
**Aura** jabber (15 ft., DC 11)

##### Defense

**AC** 16, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 Dex, +2 insight, +2 size)
**hp** 27 (6d8)
**Fort** +2, **Ref** +6, **Will** +6

##### Offense
**Speed** 10 ft., fly 60 ft. (good)
**Melee** swarm +6 (2d6)
**Ranged** acid spit +8 (2d4 acid)
**Space** 10 ft., **Reach** 0 ft.
**Special Attacks** _[[spells/Babble|babble]]_, _[[universal monster rules/Distraction|distraction]]_ (DC 13)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +8)
Constant—_[[spells/Detect Magic|detect magic]]_

##### Statistics
**Str** 10, **Dex** 15, **Con** 10, **Int** 7, **Wis** 12, **Cha** 13
**Base Atk** +4; **CMB** +4; **CMD** 14
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Fly +19, Perception +10 (+14 to listen); **Racial Modifiers** Perception (+4 to listen)
**Languages** Common (cannot speak)

##### Ecology

**Environment** temperate or tropical forests or ruins
**Organization** solitary
**Treasure** none

### Special Abilities

**Acid Spit (Ex) **A _[[monsters/Chon Chon|chon chon]]_ can spit a disgusting blob of acid at a single foe, making a ranged attack with a range of 30 feet and no range increment. A successful attack deals 2d4 points of acid damage and forces the target to make a DC 13 Fortitude saving throw to avoid becoming _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Constitution-based.

**Jabber (Su) **A _chon chon_ swarm mutters even more loudly than a solitary _chon chon_. Any creature attempting to cast a spell within 30 feet of a _chon chon_ must make a successful DC 11 concentration check or lose the spell. This is a sonic, mindaffecting effect. The concentration DC is Charisma-based.

Chon chons appear to be human heads with ears so grotesquely enlarged that they can serve as f leshy wings. Their jealous hatred of all beings with full bodies easily counters their comical appearance, however. _[[feats/Accursed|Accursed]]_ creatures drawn to places of dark magic and arcane disasters, chon chons possess the desires of the most obsessed magic users, but their dementia and twisted forms prevent them from ever obtaining the power they seek. Although these crazed beings loathe all things, they do find a _[[items/Weapon Magic Abilities/Vicious|vicious]]_ kind of solace among their own kind, not out of any sort of commiseration, but rather by wallowing in the pain of their own kind. Such hateful swarms gather to bear _[[spells/Witness|witness]]_ to each others’ misery, inadvertently increasing the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ efficacy of the entire group.

A single _chon chon_ is no larger than a human head and weighs 10 pounds at most. The creature’s ears give it a total wingspan of 3 feet, making it appear much larger and more _[[items/Weapon Magic Abilities/Menacing|menacing]]_.