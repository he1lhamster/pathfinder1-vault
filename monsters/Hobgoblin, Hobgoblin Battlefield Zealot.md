---
cssclass: [monsters]
title1: Hobgoblin, Hobgoblin Battlefield Zealot
title2: Hobgoblin Battlefield Zealot
CR: 2
sources:
- name: Monster Codex
  page: 118
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 600
race: Hobgoblin
classes:
- cleric 2
- fighter 1
alignment: LE
size: Medium
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 16
  touch: 12
  flat_footed: 14
  components:
    armor: 3
    dex: 2
    shield: 1
HP:
  HP: 25
  long: 2d8+1d10+6
  HD: 3
saves:
  fort: 7
  ref: 2
  will: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: bastard sword +4 (1d10+2/19-20)
      entries:
      - - damage: 1d10+2
          crit_range: 19-20
      attack: bastard sword
      bonus:
      - 4
  ranged:
  - - text: light crossbow +4 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
  special:
  - channel negative energy 3/day (DC 13, 1d6)
spell_like_abilities:
  entries:
  - name: battle rage
    source: default
    freq: 5/day
    other: '+1'
  - name: strength surge
    source: default
    freq: 5/day
    other: '+1'
  sources:
  - name: default
    CL: 2
    concentration: 4
spells:
  entries:
  - name: cure light wounds
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: magic weapon
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 13
  - name: shield of faith
    source: Cleric
    level: 1
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 2
    concentration: 4
    slots:
      0: at-will
    domains:
    - strength
    - war
ability_scores:
  STR: 14
  DEX: 14
  CON: 15
  INT: 8
  WIS: 15
  CHA: 10
BAB: 2
CMB: 4
CMD: 16
feats:
- name: Combat Casting
- name: Improved Channel
- name: Power Attack
skills:
  Craft (alchemy): 3
  Heal: 10
  Spellcraft: 3
  Stealth: 5
  Perception: 2
languages:
- Common
- Goblin
gear:
  combat:
  - potion of cure moderate wounds
  - scrolls of cause fear (3)
  - wand of cure light wounds (35 charges)
  - alchemist's fire (4)
  - tanglefoot bags (2)
  other:
  - mwk studded leather
  - buckler
  - bastard sword
  - light crossbow with 20 bolts
  - healer's kit
  - silver unholy symbol
  - spell component pouch
  - 228 gp
ecology:
  environment: temperate hills
desc_long: Zealots generally use their magic to aid their allies and provide healing,
  knowing that keeping their tougher allies in good health makes for a stronger army.

---

# Hobgoblin, Hobgoblin Battlefield Zealot

**Source** Monster Codex pg. 118
**XP** 600
_[[monsters/Hobgoblin|Hobgoblin]]_ _[[classes/Cleric|cleric]]_ 2/fighter 1

LE Medium humanoid (goblinoid)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 armor, +2 Dex, +1 _[[spells/Shield|shield]]_)
**hp** 25 (3 HD; 2d8+1d10+6)
**Fort** +7, **Ref** +2, **Will** +5

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Bastard sword|bastard sword]]_ +4 (1d10+2/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d8/19–20)
**Special Attacks** channel negative energy 3/day (DC 13, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +4)
5/day—battle _[[spells/Rage|rage]]_ (+1), strength surge (+1)
**_Cleric_ Spells Prepared **(CL 2nd; concentration +4)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 13), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Guidance|guidance]]_, light, stabilize, _[[spells/Virtue|virtue]]_
**D** domain spell; **Domains** Strength, War

##### Statistics
**Str** 14, **Dex** 14, **Con** 15, **Int** 8, **Wis** 15, **Cha** 10
**Base Atk** +2; **CMB** +4; **CMD** 16
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Craft (alchemy) +3, _[[spells/Heal|Heal]]_ +10, Spellcraft +3, Stealth +5
**Languages** Common, _[[monsters/Goblin|Goblin]]_
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scrolls of _[[spells/Cause Fear|cause fear]]_ (3), wand of _cure light wounds_ (35 charges), _[[classes/Alchemist|alchemist]]_’s fire (4), tanglefoot bags (2); **Other Gear** mwk studded leather, _[[items/Armor/Buckler|buckler]]_, _bastard sword_, _light crossbow_ with 20 bolts, _[[npcs/Healer|healer]]_’s kit, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 228 gp

##### Ecology

**Environment** temperate hills

##### Description

Zealots generally use their magic to aid their allies and provide healing, knowing that keeping their tougher allies in good health makes for a stronger army.