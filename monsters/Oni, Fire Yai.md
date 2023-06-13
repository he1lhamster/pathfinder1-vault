---
cssclass: [monsters]
title1: Oni, Fire Yai
desc_short: This fanged, three-eyed giant rages in its finely crafted armor, its skin
  as red as a smoldering ember.
title2: Fire Yai
CR: 15
sources:
- name: Bestiary 3
  page: 206
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 51200
alignment: NE
size: Large
type: outsider
subtypes:
- fire
- giant
- native
- oni
- shapechanger
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 29
  touch: 10
  flat_footed: 28
  components:
    armor: 8
    dex: 1
    natural: 11
    size: -1
HP:
  HP: 229
  long: 17d10+136
  regeneration: 5
  regeneration_weakness: acid or cold
saves:
  fort: 18
  ref: 10
  will: 15
immunities:
- fire
SR: 26
weaknesses:
- vulnerability to cold
speeds:
  base: 40
  other_semicolon: 30 ft., fly 40 ft. (good) in armor
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 katana +27/+22/+17/+12 (2d6+16/18-20)
      entries:
      - - damage: 2d6+16
          crit_range: 18-20
      attack: +1 katana
      bonus:
      - 27
      - 22
      - 17
      - 12
  - - text: 2 slams +26 (1d10+10)
      entries:
      - - damage: 1d10+10
      count: 2
      attack: slams
      bonus:
      - 26
  ranged:
  - - text: fiery missile +19 touch (4d6 fire plus burn)
      entries:
      - - damage: 4d6
          type: fire
        - effect: burn
      attack: fiery missile
      bonus:
      - 19
      touch: true
  special:
  - burn (2d6, DC 26)
  - smoke form
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: scorching ray
    source: default
    freq: At will
  - name: charm monster
    source: default
    freq: 3/day
    DC: 16
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 15
  - name: fireball
    source: default
    freq: 3/day
    DC: 15
  - name: fire shield
    source: default
    freq: 3/day
    other: warm shield only
  - name: wall of fire
    source: default
    freq: 3/day
  - name: incendiary cloud
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 15
    concentration: 17
ability_scores:
  STR: 31
  DEX: 16
  CON: 26
  INT: 14
  WIS: 17
  CHA: 15
BAB: 17
CMB: 28
CMD: 41
feats:
- name: Cleave
- name: Combat Reflexes
- name: Great Cleave
- name: Improved Initiative
- name: Improved Overrun
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 22
  Craft (weapons): 12
  Craft (armor): 12
  Diplomacy: 11
  Disguise: 11
  Fly: 19
  Intimidate: 22
  Knowledge (arcana): 14
  Perception: 23
  Sense Motive: 23
  Spellcraft: 11
  Use Magic Device: 14
languages:
- Common
- Giant
special_qualities:
- change shape (Medium or Large humanoid; alter self or giant form I)
ecology:
  environment: temperate or warm hills or mountains
  organization: solitary, band (1 plus 4-8 fire giants), tribe (1 plus 20-30 fire
    giants), or dynasty (1 plus 2-20 other oni)
  treasure_type: standard
  treasure:
  - +1 banded mail
  - +1 katana
  - other treasure
special_abilities:
  Fiery Missile (Su): As a swift action, a fire yai can launch a bolt of fire from
    its third eye. This attack has a range of 180 feet with no range increment.
  Smoke Form (Sp): As a standard action, a fire yai can turn into a cloud of smoke.
    This functions like gaseous form, except the cloud has the properties of the smoke
    cloud from a pyrotechnics spell (Fort DC 26 negates the effects of the smoke cloud).
    The fire yai can end this ability as a standard action.
desc_long: |-
  Fire yai prefer to live in luxury-an orderly and well-built abode is essential. Even a lone fire yai prefers to build or inhabit a fortified stone dwelling in its territory, and surrounds itself with as many luxuries as it can acquire. Vain, greedy, and brutal, fire yai are the most impulsive of their kind-several tales tell of clever heroes taunting fire yai to act rashly. They rarely let challenges pass uncontested and react quickly to squelch any threat to their rule.

  While many fire yai seek out tribes of fire giants to infiltrate and rule, not all follow this compulsion. Capable of assuming the form of many types of humanoid, some fire yai seek to subtly invade and eventually rule entire nations of humanoids from within.

  A fire yai is 16 feet tall and weighs 7,000 pounds.

---

# Oni, Fire Yai
This fanged, three-eyed giant rages in its finely crafted armor, its skin as red as a smoldering ember.
**Source** Bestiary 3 pg. 206
**XP** 51,200

NE Large outsider (fire, giant, native, oni, shapechanger)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +23

##### Defense

**AC** 29, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+8 armor, +1 Dex, +11 natural, –1 size)
**hp** 229 (17d10+136); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or cold)
**Fort** +18, **Ref** +10, **Will** +15
**Immune** fire; **SR** 26
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., fly 60 ft. (good); 30 ft., fly 40 ft. (good) in armor
**Melee** +1 _[[items/Weapon/Katana|katana]]_ +27/+22/+17/+12 (2d6+16/18–20) or 2 slams +26 (1d10+10)
**Ranged** fiery missile +19 touch (4d6 fire plus _[[universal monster rules/Burn|burn]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _burn_ (2d6, DC 26), smoke form
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +17)
Constant—fly
At will—_[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Scorching Ray|scorching ray]]_
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 16), _[[spells/Deep Slumber|deep slumber]]_ (DC 15), _[[spells/Fireball|fireball]]_ (DC 15), _[[spells/Fire Shield|fire shield]]_ (warm _[[spells/Shield|shield]]_ only), _[[spells/Wall Of Fire|wall of fire]]_
1/day—_[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 20)

##### Statistics
**Str** 31, **Dex** 16, **Con** 26, **Int** 14, **Wis** 17, **Cha** 15
**Base Atk** +17; **CMB** +28; **CMD** 41
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +22, Craft (weapons) +12, Craft (armor) +12, Diplomacy +11, Disguise +11, Fly +19, Intimidate +22, Knowledge (arcana) +14, Perception +23, Sense Motive +23, Spellcraft +11, Use Magic Device +14
**Languages** Common, Giant
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Medium or Large humanoid; _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form I|giant form I]]_)

##### Ecology

**Environment** temperate or warm hills or mountains
**Organization** solitary, band (1 plus 4–8 fire giants), tribe (1 plus 20–30 fire giants), or dynasty (1 plus 2–20 other oni)
**Treasure** standard (+1 _[[items/Armor/Banded mail|banded mail]]_, +1 _katana_, other treasure)

### Special Abilities

**Fiery Missile (Su)** As a swift action, a fire yai can launch a bolt of fire from its _[[items/Wondrous Item/Third Eye|third eye]]_. This attack has a range of 180 feet with no range increment.
**Smoke Form (Sp)** As a standard action, a fire yai can turn into a cloud of smoke. This functions like _[[spells/Gaseous Form|gaseous form]]_, except the cloud has the properties of the smoke cloud from a _[[spells/Pyrotechnics|pyrotechnics]]_ spell (Fort DC 26 negates the effects of the smoke cloud). The fire yai can end this ability as a standard action.

##### Description

Fire yai prefer to live in luxury—an orderly and well-built abode is essential. Even a lone fire yai prefers to build or inhabit a fortified stone dwelling in its territory, and surrounds itself with as many luxuries as it can acquire. Vain, greedy, and brutal, fire yai are the most impulsive of their kind—several tales tell of clever heroes taunting fire yai to act rashly. They rarely let challenges pass uncontested and react quickly to squelch any threat to their rule.

While many fire yai seek out tribes of fire giants to infiltrate and rule, not all follow this compulsion. Capable of assuming the form of many types of humanoid, some fire yai seek to subtly invade and eventually rule entire nations of humanoids from within.

A fire yai is 16 feet tall and weighs 7,000 pounds.