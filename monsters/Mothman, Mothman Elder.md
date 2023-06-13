---
cssclass: [monsters]
title1: Mothman, Mothman Elder
desc_short: Two colorful membranous wings rise behind this large insectlike humanoid,
  forming and reforming into complex patterns.
title2: Mothman Elder
CR: 12
sources:
- name: Mystery Monsters Revisited
  page: 33
  link: http://paizo.com/products/btpy8v2z?Pathfinder-Campaign-Setting-Mystery-Monsters-Revisited
XP: 19200
alignment: CN
size: Large
type: monstrous humanoid
initiative:
  bonus: 9
senses:
  darkvision: 60
  see invisibility: true
auras:
- name: warp elements
  radius: 120
  DC: 22
AC:
  AC: 26
  touch: 14
  flat_footed: 21
  components:
    dex: 5
    natural: 12
    size: -1
HP:
  HP: 142
  long: 15d10+60
saves:
  fort: 9
  ref: 14
  will: 16
defensive_abilities:
- blur
DR:
- amount: 10
  weakness: magic
resistances:
  cold: 20
  fire: 20
SR: 23
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +20 (2d6+3/19-20)
      entries:
      - - damage: 2d6+3
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 20
  ranged:
  - - text: obliteration ray +19 touch (8d6 energy)
      entries:
      - - damage: 8d6
          type: energy
      attack: obliteration ray
      bonus:
      - 19
      touch: true
  special:
  - mind-warping gaze (DC 22)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: control weather
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: cloudkill
    source: default
    freq: 3/day
    DC: 20
  - name: hold monster
    source: default
    freq: 3/day
    DC: 20
  - name: phantasmal killer
    source: default
    freq: 3/day
    DC: 19
  - name: scrying
    source: default
    freq: 3/day
    DC: 19
  - name: earthquake
    source: default
    freq: 1/day
    DC: 23
  - name: incendiary cloud
    source: default
    freq: 1/day
    DC: 23
  sources:
  - name: default
    CL: 15
    concentration: 20
ability_scores:
  STR: 17
  DEX: 20
  CON: 18
  INT: 17
  WIS: 21
  CHA: 20
BAB: 15
CMB: 21
CMD: 34
feats:
- name: Agile Maneuvers
- name: Blind-Fight
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Weapon Finesse
- name: Weapon Focus (claw)
skills:
  Fly: 25
  Knowledge (arcana): 21
  Knowledge (dungeoneering): 21
  Perception: 23
  Sense Motive: 20
  Spellcraft: 18
  Stealth: 19
languages:
- Common
- Sylvan
- Undercommon (can't speak)
- telepathy 100 ft.
special_abilities:
  Mind-Warping Gaze (Su): See page 194 of Pathfinder RPG Bestiary 2.
  Obliteration Ray (Su): As a swift action, a mothman elder can fire a ray of devastating
    energy as a ranged touch attack that deals 8d6 points of damage (or 8d8 points
    of damage against an object, automatically bypassing hardness). This attack deals
    either acid, cold, electricity, or fire damage, as chosen by the mothman elder
    at the start of its turn. This attack has a range of 180 feet with no range increment.
  Warp Elements (Su): A mothman elder's presence distorts the perceptions of those
    around it, to the point that they believe it is either suddenly swelteringly hot
    or numbingly cold. Any creature that starts its turn within 120 feet of a mothman
    elder must succeed at a DC 22 Will save or immediately succumb to the effects
    of extreme heat (Pathfinder RPG Core Rulebook 444) or extreme cold (Core Rulebook
    442). A mothman elder can switch between emitting a hot or cold aura as a move
    action. This effect lasts as long as the target remains within the area of effect
    and for 1d6 minutes afterward. A target may attempt a new Will save every minute
    to prematurely end the effect. This is a mind-affecting effect-the heat and cold
    are not real, and thus energy resistance and spells like endure elements have
    no effect. The save DC is Charisma-based.
desc_long: |-
  Mothmen that are captured or fail to accomplish their goals answer to greater beings. Called elders by their kin, these cataclysmic creatures are taskmasters in charge of disciplining renegade mothmen and disposing of damning evidence that might bring knowledge of the mothmen to public light. This means hunting down and destroying individuals that reveal themselves to too many or fail in fulfilling destiny.

  A mothman elder is 8 feet tall and weighs 150 pounds.

---

# Mothman, Mothman Elder
Two colorful membranous wings rise behind this large insectlike humanoid, forming and reforming into complex patterns.
**Source** Mystery Monsters Revisited pg. 33
**XP** 19,200

CN Large monstrous humanoid
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +23
**Aura** warp elements (120 ft., DC 22)

##### Defense

**AC** 26, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+5 Dex, +12 natural, –1 size)
**hp** 142 (15d10+60)
**Fort** +9, **Ref** +14, **Will** +16
**Defensive Abilities** _[[spells/Blur|blur]]_; **DR** 10/magic; **Resist** cold 20, fire 20; **SR** 23

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 claws +20 (2d6+3/19–20)
**Ranged** obliteration ray +19 touch (8d6 energy)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** mind-warping _[[universal monster rules/Gaze|gaze]]_ (DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
Constant—_blur_, _see invisibility_
At will—_[[spells/Control Weather|control weather]]_, greater _[[spells/Dispel Magic|dispel magic]]_
3/day—_[[spells/Cloudkill|cloudkill]]_ (DC 20), _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 19), _[[spells/Scrying|scrying]]_ (DC 19)
1/day—_[[spells/Earthquake|earthquake]]_ (DC 23), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 23)

##### Statistics
**Str** 17, **Dex** 20, **Con** 18, **Int** 17, **Wis** 21, **Cha** 20
**Base Atk** +15; **CMB** +21; **CMD** 34
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Fly +25, Knowledge (arcana) +21, Knowledge (dungeoneering) +21, Perception +23, Sense Motive +20, Spellcraft +18, Stealth +19
**Languages** Common, Sylvan, Undercommon (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

### Special Abilities

**Mind-Warping _Gaze_ (Su)** See page 194 of Pathfinder RPG Bestiary 2.

**Obliteration Ray (Su)** As a swift action, a _[[monsters/Mothman|mothman]]_ elder can fire a ray of devastating energy as a ranged touch attack that deals 8d6 points of damage (or 8d8 points of damage against an object, automatically bypassing hardness). This attack deals either acid, cold, electricity, or fire damage, as chosen by the _mothman_ elder at the start of its turn. This attack has a range of 180 feet with no range increment.

**Warp Elements (Su)** A _mothman_ elder’s presence distorts the perceptions of those around it, to the point that they believe it is either suddenly swelteringly hot or numbingly cold. Any creature that starts its turn within 120 feet of a _mothman_ elder must succeed at a DC 22 Will save or immediately succumb to the effects of extreme _[[universal monster rules/Heat|heat]]_ (Pathfinder RPG Core Rulebook 444) or extreme cold (Core Rulebook 442). A _mothman_ elder can switch between emitting a hot or cold aura as a move action. This effect lasts as long as the target remains within the area of effect and for 1d6 minutes afterward. A target may attempt a new Will save every minute to prematurely end the effect. This is a mind-affecting effect—the _heat_ and cold are not real, and thus _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ and spells like _[[spells/Endure Elements|endure elements]]_ have no effect. The save DC is Charisma-based.

##### Description

Mothmen that are captured or fail to accomplish their goals answer to greater beings. _[[items/Weapon Magic Abilities/Called|Called]]_ elders by their kin, these cataclysmic creatures are taskmasters in charge of disciplining renegade mothmen and disposing of damning evidence that might bring knowledge of the mothmen to public light. This means hunting down and destroying individuals that reveal themselves to too many or fail in fulfilling destiny.

A _mothman_ elder is 8 feet tall and weighs 150 pounds.