---
cssclass: [monsters]
title1: Wayang
desc_short: Spiralling patterns cover this shadowy humanoid's skin, and its black
  hair trails away in wisps.
title2: Wayang
CR: 1/2
sources:
- name: Bestiary 4
  page: 274
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 200
race: Male
classes:
- wayang illusionist 1
alignment: CN
size: Small
type: humanoid
subtypes:
- wayang
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 14
  touch: 14
  flat_footed: 11
  components:
    dex: 3
    size: 1
HP:
  HP: 8
  long: 1d6+2
saves:
  fort: 1
  ref: 3
  will: 1
  other: +2 vs. shadow spells
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +0 (1d3-1/19-20)
      entries:
      - - damage: 1d3-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 0
  ranged:
  - - text: blowgun +4 (1)
      entries:
      - - damage: '1'
      attack: blowgun
      bonus:
      - 4
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 11
  - name: pass without trace
    source: default
    freq: 1/day
  - name: ventriloquism
    source: default
    freq: 1/day
    DC: 12
  - name: blinding ray
    source: arcane school
    freq: 6/day
  sources:
  - name: default
    CL: 1
    concentration: 2
  - name: arcane school
    CL: 1
    concentration: 4
spells:
  entries:
  - name: hypnotism
    source: Illusionist
    level: 1
    DC: 14
  - name: silent image
    source: Illusionist
    level: 1
    DC: 14
  - superscripts:
    - APG
    name: vanish
    source: Illusionist
    level: 1
  - name: detect magic
    source: Illusionist
    level: 0
  - name: ghost sound
    source: Illusionist
    level: 0
    DC: 13
  - name: read magic
    source: Illusionist
    level: 0
  sources:
  - name: Illusionist
    type: prepared
    CL: 1
    concentration: 4
    slots:
      0: at-will
    opposition_schools:
    - necromancy
    - transmutation
ability_scores:
  STR: 8
  DEX: 16
  CON: 12
  INT: 17
  WIS: 8
  CHA: 13
BAB: 0
CMB: -2
CMD: 11
feats:
- name: Combat Casting
- name: Scribe Scroll
skills:
  Craft (alchemy): 7
  Knowledge (arcana): 7
  Perception: 2
  Spellcraft: 7
  Stealth: 10
  _racial_mods:
    Perception:
      _: 2
    Stealth:
      _: 2
languages:
- Abyssal
- Common
- Draconic
- Goblin
- Wayang
special_qualities:
- arcane bond (amulet)
- extended illusions +1 round
- light and dark
- shadow magic
ecology:
  environment: temperate forests
  organization: solitary, pair, tribe (3-24)
  treasure_type: NPC Gear
  treasure:
  - blowgun with 20 darts
  - dagger
  - other treasure
special_abilities:
  Light and Dark (Su): Once per day as an immediate action, a wayang can choose to
    be affected by positive and negative energy effects as if it were an undead creature,
    taking damage from positive energy and healing damage from negative energy. This
    ability lasts for 1 minute.
desc_long: Originating from the Shadow Plane, wayangs are pixie-like in stature with
  extremely gangly limbs and skin the color of deep shadow. They follow a philosophy
  known as “The Dissolution,” which teaches that in passing they again merge into
  shadow.

---

# Wayang
Spiralling patterns cover this shadowy humanoid’s skin, and its black hair trails away in wisps.
**Source** Bestiary 4 pg. 274
**XP** 200
Male _[[monsters/Wayang|wayang]]_ illusionist 1

CN Small humanoid (_wayang_)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 14, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+3 Dex, +1 size)
**hp** 8 (1d6+2)
**Fort** +1, **Ref** +3, **Will** +1; +2 vs. _[[items/Armor Magic Abilities/Shadow|shadow]]_ spells

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +0 (1d3–1/19–20)
**Ranged** _[[items/Weapon/Blowgun|blowgun]]_ +4 (1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +2)
1/day—_[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 12)
**Arcane School _Spell-Like Abilities_** (CL 1st; concentration +4)
6/day—_[[spells/Blinding Ray|blinding ray]]_
**Illusionist Spells Prepared **(CL 1st; concentration +4)
1st—_[[spells/Hypnotism|hypnotism]]_ (DC 14), _[[spells/Silent Image|silent image]]_ (DC 14), _[[spells/Vanish|vanish]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _ghost sound_ (DC 13), _[[spells/Read Magic|read magic]]_
**Opposition Schools** necromancy, transmutation

##### Statistics
**Str** 8, **Dex** 16, **Con** 12, **Int** 17, **Wis** 8, **Cha** 13
**Base Atk** +0; **CMB** –2; **CMD** 11
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Craft (alchemy) +7, Knowledge (arcana) +7, Perception +2, Spellcraft +7, Stealth +10; **Racial Modifiers** +2 Perception, +2 Stealth
**Languages** Abyssal, Common, Draconic, _[[monsters/Goblin|Goblin]]_, _Wayang_
**SQ** arcane bond (amulet), extended illusions +1 round, light and dark, _shadow_ magic

##### Ecology

**Environment** temperate forests
**Organization** solitary, pair, tribe (3–24)
**Treasure** NPC gear (_blowgun_ with 20 darts, _dagger_, other treasure)

### Special Abilities

**Light and Dark (Su)** Once per day as an immediate action, a _wayang_ can choose to be affected by positive and negative energy effects as if it were an undead creature, taking damage from positive energy and healing damage from negative energy. This ability lasts for 1 minute.

##### Description

Originating from the _Shadow_ Plane, wayangs are pixie-like in stature with extremely gangly limbs and skin the color of deep _shadow_. They follow a philosophy known as “The _[[spells/Dissolution|Dissolution]]_,” which teaches that in passing they again merge into _shadow_.