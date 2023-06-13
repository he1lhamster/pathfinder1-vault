---
cssclass: [monsters]
title1: Genie, Efreeti
desc_short: This muscular giant has crimson skin, smoldering eyes, and small black
  horns. Smoke rises in curls from its flesh.
title2: Efreeti
CR: 8
sources:
- name: Pathfinder RPG Bestiary
  page: 140
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 4800
alignment: LE
size: Large
type: outsider
subtypes:
- extraplanar
- fire
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect magic: true
AC:
  AC: 21
  touch: 13
  flat_footed: 17
  components:
    dex: 3
    dodge: 1
    natural: 8
    size: -1
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 7
  ref: 10
  will: 9
immunities:
- fire
speeds:
  base: 20
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 slams +15 (1d8+6 plus 1d6 fire)
      entries:
      - - damage: 1d8+6
        - damage: 1d6
          type: fire
      count: 2
      attack: slams
      bonus:
      - 15
  - - text: mwk falchion +16/+11 (2d6+9/18-20)
      entries:
      - - damage: 2d6+9
          crit_range: 18-20
      attack: mwk falchion
      bonus:
      - 16
      - 11
  special:
  - change size
  - heat
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: plane shift
    source: default
    freq: At Will
    paren_text: willing targets to elemental planes, Astral Plane, or Material Plane
      only
  - name: produce flame
    source: default
    freq: At Will
  - name: pyrotechnics
    source: default
    freq: At Will
    DC: 14
  - name: scorching ray
    source: default
    freq: At Will
  - name: invisibility
    source: default
    freq: 3/day
  - name: quickened scorching ray
    source: default
    freq: 3/day
  - name: wall of fire
    source: default
    freq: 3/day
    DC: 16
  - name: grant up to 3 wishes
    source: default
    freq: 1/day
    other: to nongenies only
  - name: gaseous form
    source: default
    freq: 1/day
  - name: permanent image
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 11
ability_scores:
  STR: 23
  DEX: 17
  CON: 18
  INT: 12
  WIS: 14
  CHA: 15
BAB: 10
CMB: 17
CMD: 31
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Deceitful
- name: Dodge
- is_bonus: true
  name: Improved Initiative
- name: Quicken Spell-Like Ability (scorching ray)
skills:
  Bluff: 19
  Craft (any one): 14
  Disguise: 10
  Fly: 13
  Intimidate: 15
  Perception: 15
  Sense Motive: 15
  Spellcraft: 14
  Stealth: 8
languages:
- Auran
- Aquan
- Common
- Ignan
- Terran
- telepathy 100 ft.
special_qualities:
- change shape (humanoid or giant, alter self or giant form I)
ecology:
  environment: any (Plane of Fire)
  organization: solitary, pair, company (3-6), or band (7-12)
  treasure_type: standard
  treasure:
  - mwk falchion
  - other gear
special_abilities:
  Change Size (Sp): Twice per day, an efreeti can magically change a creature's size.
    This works just like an enlarge person or reduce person spell (the efreeti chooses
    when using the ability), except that the ability can work on the efreeti. A DC
    13 Fortitude save negates the effect. The save DC is Charisma-based. This is the
    equivalent of a 2nd-level spell.
  Heat (Ex): An efreeti's body deals 1d6 points of fire damage whenever it hits in
    melee, or in each round it grapples.
desc_long: |-
  The efreet (singular efreeti) are genies from the Plane of Fire. An efreeti stands about 12 feet tall and weighs about 2,000 pounds.

  Efreet have few allies among geniekind. They certainly hate djinn, and attack them on sight. They hold an equally strong enmity for marids, and view the jann as frail and weak. Efreet often work closely with shaitans, yet even then alliances are temporary at best.

  A small percentage of efreet are noble. Noble efreet, often called maliks, have 13 Hit Dice and gain the following spell-like abilities: 3/day-fireball, heat metal; 1/day-greater invisibility, pyroclastic storm (as ice storm, with fire instead of cold damage). A noble efreeti's caster level for its spell-like abilities is 15th. Noble efreet are CR 10.

---

# Genie, Efreeti
This muscular giant has crimson skin, smoldering eyes, and small black horns. Smoke rises in curls from its flesh.
**Source** Pathfinder RPG Bestiary pg. 140
**XP** 4,800

LE Large outsider (extraplanar, fire)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +15

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 Dex, +1 dodge, +8 natural, –1 size)
**hp** 95 (10d10+40)
**Fort** +7, **Ref** +10, **Will** +9
**Immune** fire

##### Offense
**Speed** 20 ft., fly 40 ft. (perfect)
**Melee** 2 slams +15 (1d8+6 plus 1d6 fire) or mwk _[[items/Weapon/Falchion|falchion]]_ +16/+11 (2d6+9/18–20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** change size, _[[universal monster rules/Heat|heat]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th)
Constant—_detect magic_
At Will—_[[spells/Plane Shift|plane shift]]_ (willing targets to elemental planes, Astral Plane, or Material Plane only), _[[spells/Produce Flame|produce flame]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 14), _[[spells/Scorching Ray|scorching ray]]_
3/day—_[[spells/Invisibility|invisibility]]_, quickened _scorching ray_, _[[spells/Wall Of Fire|wall of fire]]_ (DC 16)
1/day—grant up to 3 wishes (to nongenies only), _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Permanent Image|permanent image]]_ (DC 18)

##### Statistics
**Str** 23, **Dex** 17, **Con** 18, **Int** 12, **Wis** 14, **Cha** 15
**Base Atk** +10; **CMB** +17; **CMD** 31
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_scorching ray_)
**Skills** Bluff +19, Craft (any one) +14, Disguise +10, Fly +13, Intimidate +15, Perception +15, Sense Motive +15, Spellcraft +14, Stealth +8
**Languages** Auran, Aquan, Common, Ignan, Terran; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (humanoid or giant, _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form I|giant form I]]_)

##### Ecology

**Environment** any (Plane of Fire)
**Organization** solitary, pair, company (3–6), or band (7–12)
**Treasure** standard (mwk _falchion_, other gear)

### Special Abilities

**Change Size (Sp)** Twice per day, an efreeti can magically change a creature’s size. This works just like an _[[spells/Enlarge Person|enlarge person]]_ or _[[spells/Reduce Person|reduce person]]_ spell (the efreeti chooses when using the ability), except that the ability can work on the efreeti. A DC 13 Fortitude save negates the effect. The save DC is Charisma-based. This is the equivalent of a 2nd-level spell.

**_Heat_ (Ex) **An efreeti’s body deals 1d6 points of fire damage whenever it hits in melee, or in each round it grapples.

##### Description

The efreet (singular efreeti) are genies from the Plane of Fire. An efreeti stands about 12 feet tall and weighs about 2,000 pounds.

Efreet have few allies among _[[spells/Geniekind|geniekind]]_. They certainly hate djinn, and attack them on sight. They hold an equally strong enmity for marids, and view the jann as frail and weak. Efreet often work closely with shaitans, yet even then alliances are temporary at best.

A small percentage of efreet are noble. Noble efreet, often _[[items/Weapon Magic Abilities/Called|called]]_ maliks, have 13 Hit Dice and gain the following _spell-like abilities_: 3/day—_[[spells/Fireball|fireball]]_, _[[spells/Heat Metal|heat metal]]_; 1/day—greater _invisibility_, pyroclastic storm (as _[[spells/Ice Storm|ice storm]]_, with fire instead of cold damage). A noble efreeti’s caster level for its _spell-like abilities_ is 15th. Noble efreet are CR 10.