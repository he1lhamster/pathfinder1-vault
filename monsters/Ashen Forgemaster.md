---
cssclass: [monsters]
title1: Ashen Forgemaster
desc_short: This hulking, serpentine creature resembles an oversized salamander devoid
  of color. Its flesh is pockmarked with coal-like scales and metallic piercings,
  and it carries a fearsome spear.
title2: Ashen Forgemaster
CR: 17
sources:
- name: 'Pathfinder #138: Rise of New Thassilon'
  page: 84
  link: https://paizo.com/products/btq01w1w
XP: 102400
alignment: CE
size: Large
type: undead
subtypes:
- extraplanar
- fire
initiative:
  bonus: 9
senses:
  darkvision: 60
  smoke vision: true
auras:
- name: fire aura
  radius: 5
AC:
  AC: 32
  touch: 14
  flat_footed: 27
  components:
    dex: 5
    natural: 18
    size: -1
HP:
  HP: 290
  long: 20d8+200
  regeneration: 15
  regeneration_weakness: cold
saves:
  fort: 16
  ref: 11
  will: 13
defensive_abilities:
- ashen cloud
- channel resistance +4
- rejuvenation
DR:
- amount: 15
  weakness: good
immunities:
- fire
- undead traits
SR: 28
weaknesses:
- vulnerability to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: +2 impervious transformative spear +28/+23/+18 (2d6+17/×3 plus 2d6 fire)
      entries:
      - - damage: 2d6+17
          crit_multiplier: 3
        - damage: 2d6
          type: fire
      attack: +2 impervious transformative spear
      bonus:
      - 28
      - 23
      - 18
    - text: tail slap +20 (3d6+5 plus 2d6 fire and grab)
      entries:
      - - damage: 3d6+5
        - damage: 2d6
          type: fire
        - effect: grab
      attack: tail slap
      bonus:
      - 20
  special:
  - constrict (3d6+15 plus 2d6 fire)
  - heat (2d6 fire)
  - lava trail
space: 10
reach: 10
reach_other: 20 ft. with tail
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: At will
  - name: mending
    source: default
    freq: At will
  - name: produce flame
    source: default
    freq: At will
  - name: quickened detonate
    source: default
    freq: 3/day
    DC: 24
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: make whole
    source: default
    freq: 3/day
  - name: blade barrier
    source: default
    freq: 1/day
    DC: 26
  - name: flame strike
    source: default
    freq: 1/day
    DC: 25
  - name: wall of iron
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 30
ability_scores:
  STR: 30
  DEX: 21
  CON:
  INT: 23
  WIS: 8
  CHA: 31
BAB: 15
CMB: 26
CMB_other: +30 grapple
CMD: 41
feats:
- name: Cleave
- name: Combat Reflexes
- name: Craft Magic Arms and ArmorB
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (detonate)
- name: Skill Focus (Perception)
- name: Vital Strike
- name: Weapon Focus (spear)
skills:
  Bluff: 20
  Craft (armorsmithing): 34
  Craft (blacksmithing): 34
  Craft (weaponsmithing): 34
  Intimidate: 23
  Knowledge (engineering): 26
  Knowledge (planes): 26
  Perception: 28
  Spellcraft: 29
  _racial_mods:
    Craft (armorsmithing):
      _: 8
    Craft (blacksmithing):
      _: 8
    Craft (weaponsmithing):
      _: 8
languages:
- Common
- Ignan
special_qualities:
- prison forge
ecology:
  environment: any land
  organization: solitary, pair, or cluster (3-5)
  treasure_type: double
  treasure:
  - +2 impervious transformative spear
  - other nonflammable treasure
special_abilities:
  Ashen Cloud (Ex): When an ashen forgemaster is struck in combat, some of its scales
    crumble off to create a noxious cloud of ash, smoke, and rotting flesh that lingers
    for 1 round in all adjacent squares. Any creature that starts its turn in this
    cloud is sickened for 1 round (Fortitude DC 30 negates). The cloud obscures all
    sight beyond 5 feet, providing total concealment. A creature within 5 feet has
    concealment. The save DC is Constitution-based.
  Fire Aura (Su): An ashen forgemaster is surrounded by an aura of intense heat. All
    creatures within 5 feet take 1d6 points of fire damage at the beginning of the
    forgemaster's turn.
  Lava Trail (Su): At the start of the forgemaster's turn, any square it occupies
    melts or catches fire from the intense heat of its body. These squares become
    difficult terrain for all creatures other than the ashen forgemaster. Each creature
    that enters or begins its turn within the affected squares takes 10d6 points of
    fire damage. The squares cool and return to normal after 1 round.
  Prison Forge (Su): An ashen forgemaster is bound to a monolithic forge and cannot
    stray more than 500 feet from it. A forgemaster that moves more than 500 feet
    from its prison forge is staggered until it returns. A forgemaster that remains
    more than 500 feet from its forge for 24 hours takes 2d6 points of Charisma damage,
    and an additional 2d6 points of Charisma damage every day it remains out of range
    of its forge. When the total Charisma damage equals or exceeds the forgemaster's
    Charisma score, it is destroyed and rejuvenated in its prison forge once again
    (see below).
  Rejuvenation (Su): One day after an ashen forgemaster is destroyed, its forge begins
    to rebuild the undead creature's body. This process takes 2d6 days-if the body
    is destroyed before that time passes, the forge merely starts the process anew.
    After this time passes, the forgemaster awakens fully healed. It does not have
    any of the gear left behind on its old body, but it can forge a new weapon or
    simply select one from the many weapons it has previously made.
  Smoke Vision (Ex): An ashen forgemaster can see perfectly in smoky conditions (such
    as those created by pyrotechnics or its own ashen cloud ability).
desc_long: |-
  Ashen forgemasters are massive, undead salamanders tasked with eternally toiling at a forge, crafting armor and weapons. They begin their lives as living salamanders but are bound to a forge, continuing their work eternally, long into their undeath. Centuries spent in seclusion erodes their personality, and they eventually grow into paranoid, violent, and sadistic creatures. Forgemasters surround themselves with the weapons and armor they have crafted over the years, the designs and shapes of which grow more bizarre as the forgemaster's delusions grow.

   An ashen forgemaster stands between 9 and 12 feet tall and weighs about 5,000 pounds.

---

# Ashen Forgemaster
This hulking, serpentine creature resembles an oversized _[[monsters/Salamander|salamander]]_ devoid of color. Its flesh is pockmarked with coal-like scales and metallic piercings, and it carries a fearsome _[[items/Weapon/Spear|spear]]_.
**Source** Pathfinder #138: Rise of New Thassilon pg. 84
**XP** 102,400
CE Large undead (extraplanar, fire)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., smoke _[[spells/Vision|vision]]_; Perception +28
**Aura** fire aura (5 ft.)

##### Defense

**AC** 32, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+5 Dex, +18 natural, –1 size)
**hp** 290 (20d8+200); _[[universal monster rules/Regeneration|regeneration]]_ 15 (cold)
**Fort** +16, **Ref** +11, **Will** +13
**Defensive Abilities** ashen cloud, _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, rejuvenation; **DR** 15/good; **Immune** fire, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 28
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft.
**Melee** +2 _[[items/Weapon Magic Abilities/Impervious|impervious]]_ _[[items/Weapon Magic Abilities/Transformative|transformative]]_ _spear_ +28/+23/+18 (2d6+17/×3 plus 2d6 fire), tail slap +20 (3d6+5 plus 2d6 fire and _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with tail)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (3d6+15 plus 2d6 fire), _[[universal monster rules/Heat|heat]]_ (2d6 fire), lava trail
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +30)
At will—_[[spells/Fire Shield|fire shield]]_, _[[spells/Mending|mending]]_, _[[spells/Produce Flame|produce flame]]_ 
3/day—quickened _[[spells/Detonate|detonate]]_ (DC 24), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Make Whole|make whole]]_ 
1/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 26), _[[spells/Flame Strike|flame strike]]_ (DC 25), _[[spells/Wall of Iron|wall of iron]]_

##### Statistics
**Str** 30, **Dex** 21, **Con** —, **Int** 23, **Wis** 8, **Cha** 31
**Base Atk** +15; **CMB** +26 (+30 grapple); **CMD** 41
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, Craft Magic Arms and ArmorB, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_detonate_), _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Bluff +20, Craft (armorsmithing) +34, Craft (blacksmithing) +34, Craft (weaponsmithing) +34, Intimidate +23, Knowledge (engineering, planes) +26, Perception +28, Spellcraft +29; **Racial Modifiers** +8 Craft (armorsmithing, blacksmithing, and weaponsmithing)
**Languages** Common, Ignan
**SQ** prison forge

##### Ecology

**Environment** any land
**Organization** solitary, pair, or cluster (3–5)
**Treasure** double (+2 _impervious_ _transformative_ _spear_, other nonflammable treasure)

### Special Abilities

**Ashen Cloud (Ex)** When an _[[monsters/Ashen Forgemaster|ashen forgemaster]]_ is struck in combat, some of its scales crumble off to create a noxious cloud of ash, smoke, and rotting flesh that lingers for 1 round in all adjacent squares. Any creature that starts its turn in this cloud is _[[conditions/Sickened|sickened]]_ for 1 round (Fortitude DC 30 negates). The cloud obscures all sight beyond 5 feet, providing total concealment. A creature within 5 feet has concealment. The save DC is Constitution-based.

**Fire Aura (Su)** An _ashen forgemaster_ is surrounded by an aura of intense _heat_. All creatures within 5 feet take 1d6 points of fire damage at the beginning of the forgemaster’s turn.

**Lava Trail (Su)** At the start of the forgemaster’s turn, any square it occupies melts or catches fire from the intense _heat_ of its body. These squares become difficult terrain for all creatures other than the _ashen forgemaster_. Each creature that enters or begins its turn within the affected squares takes 10d6 points of fire damage. The squares cool and return to normal after 1 round.

**Prison Forge (Su)** An _ashen forgemaster_ is bound to a monolithic forge and cannot stray more than 500 feet from it. A forgemaster that moves more than 500 feet from its prison forge is _[[conditions/Staggered|staggered]]_ until it returns. A forgemaster that remains more than 500 feet from its forge for 24 hours takes 2d6 points of Charisma damage, and an additional 2d6 points of Charisma damage every day it remains out of range of its forge. When the total Charisma damage equals or exceeds the forgemaster’s Charisma score, it is destroyed and rejuvenated in its prison forge once again (see below).

**Rejuvenation (Su)** One day after an _ashen forgemaster_ is destroyed, its forge begins to rebuild the undead creature’s body. This process takes 2d6 days—if the body is destroyed before that time passes, the forge merely starts the process anew. After this time passes, the forgemaster awakens fully healed. It does not have any of the gear left behind on its old body, but it can forge a new weapon or simply select one from the many weapons it has previously made.
**Smoke _Vision_ (Ex)** An _ashen forgemaster_ can see perfectly in smoky conditions (such as those created by _[[spells/Pyrotechnics|pyrotechnics]]_ or its own ashen cloud ability).

##### Description

Ashen forgemasters are massive, undead salamanders tasked with eternally toiling at a forge, crafting armor and weapons. They begin their lives as living salamanders but are bound to a forge, continuing their work eternally, long into their undeath. Centuries spent in seclusion erodes their personality, and they eventually grow into paranoid, violent, and sadistic creatures. Forgemasters surround themselves with the weapons and armor they have crafted over the years, the designs and shapes of which grow more bizarre as the forgemaster’s delusions grow.

An _ashen forgemaster_ stands between 9 and 12 feet tall and weighs about 5,000 pounds.