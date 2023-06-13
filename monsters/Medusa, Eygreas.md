---
cssclass: [monsters]
title1: Medusa, Eygreas
desc_short: This monstrous, snaked-haired creature has the upper body of a bronze-skinned
  woman and the lower body of an enormous serpent.
title2: Eygreas
CR: 13
sources:
- name: Mythical Monsters Revisited
  page: 44
  link: http://paizo.com/products/btpy8pfw?Pathfinder-Campaign-Setting-Mythical-Monsters-Revisited
XP: 25600
race: Female
classes:
- brazen medusa ranger 5
alignment: LE
size: Large
type: monstrous humanoid
initiative:
  bonus: 8
senses:
  all-around vision: true
  darkvision: 60
AC:
  AC: 29
  touch: 14
  flat_footed: 24
  components:
    armor: 6
    dex: 4
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 141
  long: 8d10+5d10+70
  HD: 13
saves:
  fort: 11
  ref: 16
  will: 8
DR:
- amount: 5
  weakness: adamantine and magic
immunities:
- poison
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +16 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: claws
      bonus:
      - 16
    - text: snake bite +16 (1d6+2 plus poison)
      entries:
      - - damage: 1d6+2
        - effect: poison
      attack: snake bite
      bonus:
      - 16
    - text: tail slap +11 (1d8+1 plus grab)
      entries:
      - - damage: 1d8+1
        - effect: grab
      attack: tail slap
      bonus:
      - 11
  - - text: mwk scimitar +15/+10/+5 (1d8+2/18-20)
      entries:
      - - damage: 1d8+2
          crit_range: 18-20
      attack: mwk scimitar
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: +2 seeking composite longbow +18/+13/+8 (2d6+4/x3)
      entries:
      - - damage: 2d6+4
          crit_multiplier: 3
      attack: +2 seeking composite longbow
      bonus:
      - 18
      - 13
      - 8
  special:
  - constrict (1d8+1)
  - favored enemy (humans +2, monstrous humanoids +4)
  - petrifying gaze
space: 10
reach: 10
spells:
  entries:
  - name: entangle
    source: Ranger
    level: 1
    DC: 12
  - name: pass without trace
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 2
    concentration: 3
ability_scores:
  STR: 15
  DEX: 19
  CON: 20
  INT: 10
  WIS: 13
  CHA: 17
BAB: 13
CMB: 16
CMB_other: +20 grapple
CMD: 31
feats:
- name: Dodge
- name: Endurance
- name: Far Shot
- name: Improved Initiative
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Weapon Finesse
skills:
  Bluff: 16
  Intimidate: 16
  Perception: 21
  Stealth: 15
  Survival: 17
  _racial_mods:
    Perception:
      _: 4
languages:
- Common
- Draconic
special_qualities:
- favored terrain (jungle +2)
- hunter's bond (constrictor snake)
- track +2
- wild empathy +8
gear:
  gear:
  - +2 chain shirt
  - +2 seeking composite longbow (+2 Str) with 40 arrows
  - masterwork scimitar
  - amulet of natural armor +1
  - bracers of armor +1
special_abilities:
  Petrifying Gaze (Su): Turn to stone permanently, 30 feet, Fortitude DC 19 negates.
    The save DC is Charisma-based.
  Poison (Ex): Snake bite-injury; save Fort DC 19; frequency 1/ round for 6 rounds;
    effect 1d3 Str; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  At a young age, Eygreas learned from her mother-a strong-willed medusa by the name of Litiasha-that she was the daughter of a powerful boggard priestking. When the tribe of boggards ambushed Litiasha several years after Eygreas's birth, demanding that the medusa release her brazen daughter to them to be sacrif iced on an altar to Gogunta, Litiasha barely had time to petrify more than half of the boggard warriors before she was overwhelmed and abducted by them, and sacrif iced in her daughter's place. Eygreas barely escaped the onslaught; the traumatic event spurred within her a burning hatred for the froglike denizens of the swamp, and so she honed her skill with her bow and devoted her life to hunting the tribe that had killed her kin. After stealthily slaughtering all of the boggards with her arrows and gaze-and thus removing her only driving motivation-she fell into a realm of madness and bitter isolation.

  Now, the brazen medusa stalks the Thassilonian ruins that dot the southern Mushfens, seeking some sort of artifact or piece of history that will once again give meaning to her life, all the while butchering any she comes across with little regard to their motives or means. Though her memory is mostly shattered, her skill at hunting remains sharp, and she seeks solace from the chaos of her mind by stalking her prey and feasting on their corpses. Still, though she does not remember why, the sight of the toady people of the swamp enrages her to no end, and the only thing that will stop Eygreas from pursuing her current target is the opportunity to hunt a boggard instead.

---

# Medusa, Eygreas
This monstrous, snaked-haired creature has the upper body of a bronze-skinned woman and the lower body of an enormous serpent.
**Source** Mythical Monsters Revisited pg. 44
**XP** 25,600
Female brazen _[[monsters/Medusa|medusa]]_ _[[classes/Ranger|ranger]]_ 5

LE Large monstrous humanoid
**Init** +8; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +21

##### Defense

**AC** 29, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+6 armor, +4 Dex, +1 dodge, +9 natural, –1 size)
**hp** 141 (13 HD; 8d10+5d10+70)
**Fort** +11, **Ref** +16, **Will** +8
**DR** 5/adamantine and magic; **Immune** poison

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +16 (1d6+2), snake bite +16 (1d6+2 plus poison), tail slap +11 (1d8+1 plus _[[universal monster rules/Grab|grab]]_) or mwk _[[items/Weapon/Scimitar|scimitar]]_ +15/+10/+5 (1d8+2/18–20)
**Ranged** +2 seeking _[[items/Weapon/Composite longbow|composite longbow]]_ +18/+13/+8 (2d6+4/x3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+1), favored enemy (humans +2, monstrous humanoids +4), petrifying _[[universal monster rules/Gaze|gaze]]_
**_Ranger_ Spells Prepared **(CL 2nd; concentration +3)
1st—_[[spells/Entangle|entangle]]_ (DC 12), _[[spells/Pass without Trace|pass without trace]]_

##### Statistics
**Str** 15, **Dex** 19, **Con** 20, **Int** 10, **Wis** 13, **Cha** 17
**Base Atk** +13; **CMB** +16 (+20 grapple); **CMD** 31
**Feats** _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Far Shot|Far Shot]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +16, Intimidate +16, Perception +21, Stealth +15, Survival +17; **Racial Modifiers** +4 Perception
**Languages** Common, Draconic
**SQ** favored terrain (jungle +2), _[[classes/Hunter|hunter]]_’s bond (constrictor snake), track +2, wild _[[feats/Empathy|empathy]]_ +8
**Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 seeking _composite longbow_ (+2 Str) with 40 arrows, masterwork _scimitar_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_

### Special Abilities

**Petrifying _Gaze_ (Su) **Turn to stone permanently, 30 feet, Fortitude DC 19 negates. The save DC is Charisma-based.

**Poison (Ex) **Snake bite—injury; save Fort DC 19; frequency 1/ round for 6 rounds; effect 1d3 Str; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

At a young age, Eygreas learned from her mother—a strong-willed _medusa_ by the name of Litiasha—that she was the daughter of a powerful _[[monsters/Boggard|boggard]]_ priestking. When the tribe of boggards ambushed Litiasha several years after Eygreas’s birth, demanding that the _medusa_ release her brazen daughter to them to be sacrif iced on an altar to Gogunta, Litiasha barely had time to petrify more than half of the _boggard_ warriors before she was overwhelmed and abducted by them, and sacrif iced in her daughter’s place. Eygreas barely escaped the _[[feats/Onslaught|onslaught]]_; the traumatic event spurred within her a _[[items/Weapon Magic Abilities/Burning|burning]]_ hatred for the froglike denizens of the swamp, and so she honed her skill with her bow and devoted her life to hunting the tribe that had killed her kin. After stealthily slaughtering all of the boggards with her arrows and _gaze_—and thus removing her only driving motivation—she fell into a realm of madness and _[[items/Armor Magic Abilities/Bitter|bitter]]_ isolation.

Now, the brazen _medusa_ stalks the Thassilonian ruins that dot the southern Mushfens, seeking some sort of artifact or piece of history that will once again give meaning to her life, all the while butchering any she comes across with little regard to their motives or means. Though her memory is mostly shattered, her skill at hunting remains sharp, and she seeks solace from the chaos of her mind by _[[items/Weapon Magic Abilities/Stalking|stalking]]_ her prey and feasting on their corpses. Still, though she does not remember why, the sight of the toady people of the swamp enrages her to no end, and the only thing that will stop Eygreas from pursuing her current target is the opportunity to hunt a _boggard_ instead.