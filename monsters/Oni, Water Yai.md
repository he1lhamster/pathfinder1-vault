---
cssclass: [monsters]
title1: Oni, Water Yai
desc_short: This towering woman has blue skin, small fangs, and a third eye glaring
  from her forehead. Her robes are soaking wet.
title2: Water Yai
CR: 18
sources:
- name: Bestiary 3
  page: 212
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 153600
alignment: CE
size: Huge
type: outsider
subtypes:
- aquatic
- giant
- native
- oni
- shapechanger
- water
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 32
  touch: 11
  flat_footed: 29
  components:
    armor: 6
    dex: 3
    natural: 15
    size: -2
HP:
  HP: 297
  long: 22d10+176
  regeneration: 10
  regeneration_weakness: fire or good spells
saves:
  fort: 21
  ref: 10
  will: 18
defensive_abilities:
- freedom of movement
immunities:
- acid
SR: 29
speeds:
  base: 50
  fly: 60
  fly_maneuverability: good
  swim: 60
attacks:
  melee:
  - - text: mwk spear +35/+30/+25/+20 (3d6+21/19-20/×3)
      entries:
      - - damage: 3d6+21
          crit_range: 19-20
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 35
      - 30
      - 25
      - 20
  - - text: 2 slams +34 (2d6+14)
      entries:
      - - damage: 2d6+14
      count: 2
      attack: slams
      bonus:
      - 34
  ranged:
  - - text: acidic missile +23 touch (4d6 acid plus nausea)
      entries:
      - - damage: 4d6
          type: acid
        - effect: nausea
      attack: acidic missile
      bonus:
      - 23
      touch: true
space: 15
reach: 15
reach_other: 20 ft. with spear
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: water walk
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: liquid form
    source: default
    freq: At will
  - name: water breathing
    source: default
    freq: At will
  - name: charm monster
    source: default
    freq: 3/day
    DC: 20
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 21
  - name: control water
    source: default
    freq: 3/day
  - name: polar ray
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 39
  DEX: 17
  CON: 27
  INT: 16
  WIS: 20
  CHA: 22
BAB: 22
CMB: 38
CMB_other: +40 bull rush, disarm
CMD: 51
CMD_other: 53 vs. bull rush, disarm
feats:
- name: Awesome Blow
- name: Blind-Fight
- name: Cleave
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (spear)
- name: Improved Disarm
- name: Improved Initiative
- name: Power Attack
skills:
  Acrobatics: 21
    when jumping: 29
  Bluff: 30
  Disguise: 30
  Fly: 24
  Intimidate: 30
  Knowledge (arcana): 24
  Perception: 26
  Perform (sing): 24
  Sense Motive: 26
  Spellcraft: 21
  Swim: 43
languages:
- Common
- Giant
special_qualities:
- amphibious
- change shape (Medium, Large, or Huge humanoid; alter self or giant form II)
ecology:
  environment: any water
  organization: solitary
  treasure_type: standard
  treasure:
  - masterwork spear
  - other treasure
special_abilities:
  Acidic Missile (Su): As a swift action, a water yai can launch a bolt of acid from
    its third eye. Any creature struck by this bolt must also make a DC 29 Fortitude
    save to avoid becoming nauseated for 1 round by the overwhelming stench of the
    acid. This attack has a range of 180 feet with no range increment. The save DC
    is Constitution-based.
  Flowing Robes (Su): A water yai wears a special silk kimono infused with magical
    water. This kimono grants a +6 armor bonus. These robes function as armor only
    for water yai.
  Liquid Form (Sp): As a standard action, a water yai can turn into a mobile pool
    of water. This functions like gaseous form, except that the yai cannot fly in
    this form. It retains its own base speed, and its swim speed doubles to 120 feet.
    The water yai can end this ability as a standard action.
desc_long: The water yai clad themselves in the flesh of storm giants, yet these yai
  are more at home dwelling beneath the waves than they are above them. Unlike most
  oni, water yai have no real longing to rule or infiltrate societies-yet they still
  enjoy posing as humanoids. They often assume the forms of enormous merfolk in the
  water, but prefer to adopt the shapes of storm giants when on land. The water yai
  then pursues its favorite decadence-the acclimation of material wealth and luxuries.
  Water yai tend to be easily distracted by beautiful treasures, and despite their
  evil natures are prone to acts of unexpected frivolity.

---

# Oni, Water Yai
This towering woman has blue skin, small fangs, and a _[[items/Wondrous Item/Third Eye|third eye]]_ glaring from her forehead. Her robes are soaking wet.
**Source** Bestiary 3 pg. 212
**XP** 153,600
CE Huge outsider (aquatic, giant, native, oni, shapechanger, water)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +26

##### Defense

**AC** 32, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+6 armor, +3 Dex, +15 natural, –2 size)
**hp** 297 (22d10+176); _[[universal monster rules/Regeneration|regeneration]]_ 10 (fire or good spells)
**Fort** +21, **Ref** +10, **Will** +18
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **Immune** acid; **SR** 29

##### Offense
**Speed** 50 ft., fly 60 ft. (good), swim 60 ft.
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +35/+30/+25/+20 (3d6+21/19–20/×3) or 2 slams +34 (2d6+14)
**Ranged** acidic missile +23 touch (4d6 acid plus nausea)
**Space** 15 ft., **Reach** 15 ft. (20 ft. with _spear_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—fly, _freedom of movement_, _[[spells/Water Walk|water walk]]_
At will—_[[spells/Invisibility|invisibility]]_ (self only), liquid form, _[[universal monster rules/Water Breathing|water breathing]]_
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 20), _[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Control Water|control water]]_, _[[spells/Polar Ray|polar ray]]_

##### Statistics
**Str** 39, **Dex** 17, **Con** 27, **Int** 16, **Wis** 20, **Cha** 22
**Base Atk** +22; **CMB** +38 (+40 bull rush, disarm); **CMD** 51 (53 vs. bull rush, disarm)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_spear_), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +21 (+29 when jumping), Bluff +30, Disguise +30, Fly +24, Intimidate +30, Knowledge (arcana) +24, Perception +26, Perform (sing) +24, Sense Motive +26, Spellcraft +21, Swim +43
**Languages** Common, Giant
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Change Shape|change shape]]_ (Medium, Large, or Huge humanoid; _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form II|giant form II]]_)

##### Ecology

**Environment** any water
**Organization** solitary
**Treasure** standard (masterwork _spear_, other treasure)

### Special Abilities

**Acidic Missile (Su)** As a swift action, a water yai can launch a bolt of acid from its _third eye_. Any creature struck by this bolt must also make a DC 29 Fortitude save to avoid becoming _[[conditions/Nauseated|nauseated]]_ for 1 round by the overwhelming _[[universal monster rules/Stench|stench]]_ of the acid. This attack has a range of 180 feet with no range increment. The save DC is Constitution-based.

**Flowing Robes (Su)** A water yai wears a special _[[items/Mundane/Silk kimono|silk kimono]]_ infused with magical water. This kimono grants a +6 armor bonus. These robes function as armor only for water yai.

**Liquid Form (Sp)** As a standard action, a water yai can turn into a mobile pool of water. This functions like _[[spells/Gaseous Form|gaseous form]]_, except that the yai cannot fly in this form. It retains its own base speed, and its swim speed doubles to 120 feet. The water yai can end this ability as a standard action.

##### Description

The water yai clad themselves in the flesh of storm giants, yet these yai are more at home dwelling beneath the waves than they are above them. Unlike most _[[monsters/Oni, Water Yai|oni, water yai]]_ have no real longing to rule or infiltrate societies—yet they still enjoy posing as humanoids. They often assume the forms of enormous _[[monsters/Merfolk|merfolk]]_ in the water, but prefer to adopt the shapes of storm giants when on land. The water yai then pursues its favorite decadence—the acclimation of material wealth and luxuries. Water yai tend to be easily distracted by beautiful treasures, and despite their evil natures are _[[conditions/Prone|prone]]_ to acts of unexpected frivolity.