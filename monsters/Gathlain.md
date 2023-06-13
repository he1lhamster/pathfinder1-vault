---
cssclass: [monsters]
title1: Gathlain
desc_short: Wings composed of wood and vines grow out of the body of this lithesome
  fey.
title2: Gathlain
CR: 1/2
sources:
- name: Bestiary 4
  page: 122
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 200
race: Gathlain
classes:
- sorcerer 1
alignment: CN
size: Small
type: fey
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 17
  touch: 15
  flat_footed: 13
  components:
    dex: 3
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 7
  long: 1d6+1
saves:
  fort: 0
  ref: 3
  will: 1
speeds:
  base: 30
  fly: 40
  fly_maneuverability: poor
attacks:
  melee:
  - - text: spear +2 (1d6+1/×3)
      entries:
      - - damage: 1d6+1
          crit_multiplier: 3
      attack: spear
      bonus:
      - 2
spell_like_abilities:
  entries:
  - name: entangle
    source: default
    freq: 1/day
  - superscripts:
    - APG
    name: feather step
    source: default
    freq: 1/day
  - name: laughing touch
    source: bloodline
    freq: 6/day
  sources:
  - name: default
    CL: 1
    concentration: 4
  - name: bloodline
    CL: 1
    concentration: 4
spells:
  entries:
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 14
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 15
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: ray of frost
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 4
      0: at-will
    bloodline: fey
ability_scores:
  STR: 12
  DEX: 16
  CON: 11
  INT: 10
  WIS: 8
  CHA: 17
BAB: 0
CMB: 0
CMD: 14
feats:
- name: Dodge
- name: Eschew Materials
skills:
  Fly: 1
  Knowledge (arcana): 4
  Spellcraft: 4
  Perception: -1
languages:
- Common
- Sylvan
special_qualities:
- bloodline arcana (+2 DC for compulsion spells)
ecology:
  environment: temperate forests or jungles
  organization: solitary, flight (2-6), or grove (2-12)
  treasure_type: NPC Gear
  treasure:
  - spear
  - other treasure
desc_long: |-
  According to some fey ballads, gathlains were one of the first peoples awakened in the primal world of fey. They were created from the seeds of an enormous magical tree, with the tree's mistletoe grown into their flesh forming their strange wings.

  Mischievous and capricious, these creatures have discordant temperaments. They act purely to entertain themselves and sate their immense curiosity about the world around them. That very curiosity has caused many to migrate to the Material Plane and adventure there. These gathlains seek out and attempt to mingle with gnomes. However, gnomes often find gathlains too undisciplined, random, and foolish for their tastes.

---

# Gathlain
Wings composed of wood and vines grow out of the body of this lithesome fey.
**Source** Bestiary 4 pg. 122
**XP** 200
_[[monsters/Gathlain|Gathlain]]_ _[[classes/Sorcerer|sorcerer]]_ 1

CN Small fey
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception –1

##### Defense

**AC** 17, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +1 dodge, +2 natural, +1 size)
**hp** 7 (1d6+1)
**Fort** +0, **Ref** +3, **Will** +1

##### Offense
**Speed** 30 ft., fly 40 ft. (poor)
**Melee** _[[items/Weapon/Spear|spear]]_ +2 (1d6+1/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +4)
1/day—_[[spells/Entangle|entangle]]_, _[[spells/Feather Step|feather step]]_
**Bloodline _Spell-Like Abilities_** (CL 1st; concentration +4)
6/day—laughing touch
**_Sorcerer_ Spells Known **(CL 1st; concentration +4)
1st (4/day)—_[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Ray of Frost|ray of frost]]_
**Bloodline** fey

##### Statistics
**Str** 12, **Dex** 16, **Con** 11, **Int** 10, **Wis** 8, **Cha** 17
**Base Atk** +0; **CMB** +0; **CMD** 14
**Feats** _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_
**Skills** Fly +1, Knowledge (arcana) +4, Spellcraft +4
**Languages** Common, Sylvan
**SQ** bloodline arcana (+2 DC for compulsion spells)

##### Ecology

**Environment** temperate forests or jungles
**Organization** solitary, _[[universal monster rules/Flight|flight]]_ (2–6), or grove (2–12)
**Treasure** NPC gear (_spear_, other treasure)

##### Description

According to some fey ballads, gathlains were one of the first peoples awakened in the primal world of fey. They were created from the seeds of an enormous magical tree, with the tree’s _[[items/Mundane/Mistletoe|mistletoe]]_ grown into their flesh forming their strange wings.

Mischievous and capricious, these creatures have discordant temperaments. They act purely to entertain themselves and sate their immense curiosity about the world around them. That very curiosity has caused many to migrate to the Material Plane and adventure there. These gathlains seek out and attempt to mingle with gnomes. However, gnomes often find gathlains too undisciplined, random, and foolish for their tastes.