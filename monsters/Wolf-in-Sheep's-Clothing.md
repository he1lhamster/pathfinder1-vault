---
cssclass: [monsters]
title1: Wolf-in-Sheep's-Clothing
desc_short: A small forest animal sits motionless atop a worn stump-and then the stump's
  face peels open into a maw of sharp teeth.
title2: Wolf-in-Sheep's-Clothing
CR: 8
sources:
- name: Bestiary 3
  page: 285
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: Misfit Monsters Redeemed
  page: 63
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8gnj
XP: 4800
alignment: N
size: Medium
type: aberration
initiative:
  bonus: 4
senses:
  all-around vision: true
  darkvision: 60
AC:
  AC: 21
  touch: 10
  flat_footed: 21
  components:
    natural: 11
HP:
  HP: 97
  long: 13d8+39
saves:
  fort: 9
  ref: 6
  will: 10
speeds:
  base: 5
  burrow: 5
  climb: 5
attacks:
  melee:
  - - text: bite +12 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 12
    - text: 8 tentacles +11 (1d4+1 plus grab and pull)
      entries:
      - - damage: 1d4+1
        - effect: grab
        - effect: pull
      count: 8
      attack: tentacles
      bonus:
      - 11
  special:
  - constrict (tentacle 1d4+3)
  - implant
  - pull (tentacle, 5 ft.)
space: 5
reach: 5
reach_other: 15 ft. with tentacle
ability_scores:
  STR: 17
  DEX: 10
  CON: 17
  INT: 6
  WIS: 14
  CHA: 7
BAB: 9
CMB: 12
CMB_other: +18 grapple
CMD: 22
CMD_other: can't be tripped
feats:
- name: Great Fortitude
- is_bonus: true
  name: Greater Grapple
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Multiattack
- name: Skill Focus (Perception)
- name: Weapon Focus (tentacle)
skills:
  Climb: 15
  Disguise: -1
    as tree stump: 11
  Knowledge (nature): 4
  Perception: 14
  Sense Motive: 8
  Stealth: 9
  _racial_mods:
    Disguise:
      as tree stump: 12
special_qualities:
- corpse lure
ecology:
  environment: any forest
  organization: solitary
  treasure_type: incidental
special_abilities:
  Corpse Lure (Ex): By setting a corpse atop its stump and riddling the body with
    small, extruded filaments, a wolf-in-sheep's-clothing can crudely maneuver the
    corpse, manipulating it like a puppet. The corpse cannot leave the stump or perform
    complex actions, but is instead used to lure larger prey within range of the wolf-in-sheep's-clothing's
    tentacles. The largest corpse a wolf-in-sheep's-clothing can manipulate in this
    fashion is two size categories smaller than itself (thus Tiny creatures for a
    Medium wolf-in-sheep's-clothing). When a wolf-in-sheep's-clothing uses a corpse
    like this, it gains a +8 bonus on Disguise checks beyond its normal racial bonus.
  Implant (Ex): |-
    A wolf-in-sheep's-clothing can infest a creature with its eggs in one of two ways. A creature that eats a carcass used by the monster as a corpse lure automatically becomes implanted. Alternatively, up to once per day, a wolf-in-sheep's-clothing can implant an egg into a helpless or pinned creature as part of a grapple action. The target can resist being implanted with a DC 19 Fortitude save, but if it fails, the seed gestates and becomes a self-aware creature that slowly steals nourishment from its host before finally exploding free of its host's gut. The parasite can be cut free of the host's belly with a DC 25 Heal check, which takes 1 hour and deals 3d6 slashing damage regardless of success or failure. Remove disease (or any similar effect) also kills an implanted egg.

    Wolf-in-Sheep's-Clothing Egg: Infestation-ingestion; save Fort 19; onset 1 day; frequency 1/day; effect 1d4 Str damage until host reaches 0, then 3d6 damage as parasite bursts free; cure 3 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  A wolf-in-sheep's-clothing appears at first to be little more than a tree stump sitting in a clearing, perhaps with a small animal sitting atop it. Only when a predator comes close does it become clear that the small animal is in fact long dead, given false life by tendrils springing up through its form, but by then it's too late, as the wolf-in-sheep's-clothing drags the would-be hunter into its waiting maw.

  Though intelligent, these monsters see little need for the company of others. Their method of reproduction is as hideous as their tactic of using corpses as lures, for they implant their parasitic eggs in living hosts, giving their spawn a fresh meal to eat upon hatching.

  A wolf-in-sheep's-clothing is usually about 4 to 5 feet across and weighs 200 pounds.

---

# Wolf-in-Sheep's-Clothing
A small forest animal sits motionless atop a worn stump—and then the stump’s face peels open into a maw of sharp teeth.
**Source** Bestiary 3 pg. 285, Misfit Monsters _[[items/Weapon Magic Abilities/Redeemed|Redeemed]]_ pg. 63
**XP** 4,800

N Medium aberration
**Init** +4; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+11 natural)
**hp** 97 (13d8+39)
**Fort** +9, **Ref** +6, **Will** +10

##### Offense
**Speed** 5 ft., _[[universal monster rules/Burrow|burrow]]_ 5 ft., _[[universal monster rules/Climb|climb]]_ 5 ft.
**Melee** bite +12 (1d6+3), 8 tentacles +11 (1d4+1 plus _[[universal monster rules/Grab|grab]]_ and _[[universal monster rules/Pull|pull]]_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tentacle)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (tentacle 1d4+3), implant, _pull_ (tentacle, 5 ft.)

##### Statistics
**Str** 17, **Dex** 10, **Con** 17, **Int** 6, **Wis** 14, **Cha** 7
**Base Atk** +9; **CMB** +12 (+18 grapple); **CMD** 22 (can’t be tripped)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Grapple|Greater Grapple]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (tentacle)
**Skills** _Climb_ +15, Disguise –1 (+11 as tree stump), Knowledge (nature) +4, Perception +14, Sense Motive +8, Stealth +9; **Racial Modifiers** +12 Disguise as tree stump
**SQ** corpse lure

##### Ecology

**Environment** any forest
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Corpse Lure (Ex)** By setting a corpse atop its stump and riddling the body with small, extruded filaments, a wolf-in-sheep’s-clothing can crudely maneuver the corpse, manipulating it like a puppet. The corpse cannot leave the stump or perform complex actions, but is instead used to lure larger prey within range of the wolf-in-sheep’s-clothing’s tentacles. The largest corpse a wolf-in-sheep’s-clothing can manipulate in this fashion is two size categories smaller than itself (thus Tiny creatures for a _Medium_ wolf-in-sheep’s-clothing). When a wolf-in-sheep’s-clothing uses a corpse like this, it gains a +8 bonus on Disguise checks beyond its normal racial bonus.

**Implant (Ex)** A wolf-in-sheep’s-clothing can infest a creature with its eggs in one of two ways. A creature that eats a carcass used by the monster as a corpse lure automatically becomes implanted. Alternatively, up to once per day, a wolf-in-sheep’s-clothing can implant an egg into a _[[conditions/Helpless|helpless]]_ or _[[conditions/Pinned|pinned]]_ creature as part of a grapple action. The target can resist being implanted with a DC 19 Fortitude save, but if it fails, the seed gestates and becomes a self-aware creature that slowly steals nourishment from its host before finally exploding free of its host’s gut. The parasite can be cut free of the host’s belly with a DC 25 _[[spells/Heal|Heal]]_ check, which takes 1 hour and deals 3d6 slashing damage regardless of success or failure. _[[spells/Remove Disease|Remove disease]]_ (or any similar effect) also kills an implanted egg.

Wolf-in-Sheep’s-Clothing Egg: Infestation—ingestion; save Fort 19; onset 1 day; frequency 1/day; effect 1d4 Str damage until host reaches 0, then 3d6 damage as parasite bursts free; cure 3 consecutive saves. The save DC is Constitution-based.

##### Description

A wolf-in-sheep’s-clothing appears at first to be little more than a tree stump sitting in a clearing, perhaps with a small animal sitting atop it. Only when a predator comes close does it become clear that the small animal is in fact long dead, given _[[spells/False Life|false life]]_ by tendrils springing up through its form, but by then it’s too late, as the wolf-in-sheep’s-clothing drags the would-be _[[classes/Hunter|hunter]]_ into its waiting maw.

Though intelligent, these monsters see little need for the company of others. Their method of reproduction is as hideous as their tactic of using corpses as lures, for they implant their parasitic eggs in living hosts, giving their spawn a fresh meal to eat upon hatching.

A wolf-in-sheep’s-clothing is usually about 4 to 5 feet across and weighs 200 pounds.