---
cssclass: [monsters]
title1: Scholar Priest
title2: Scholar Priest
CR: 2
sources:
- name: NPC Codex
  page: 45
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 600
race: Human
classes:
- cleric of Nethys 3
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: -1
AC:
  AC: 15
  touch: 9
  flat_footed: 15
  components:
    armor: 6
    dex: -1
HP:
  HP: 23
  long: 3d8+6
saves:
  fort: 4
  ref: 0
  will: 6
speeds:
  base: 20
attacks:
  melee:
  - - text: quarterstaff +3 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: quarterstaff
      bonus:
      - 3
  ranged:
  - - text: light crossbow +1 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 1
  special:
  - channel negative energy 7/day (DC 13, 2d6)
  - hand of the acolyte (6/day)
spell_like_abilities:
  entries:
  - name: blast rune
    source: default
    freq: 6/day
    paren_text: 1d6+1 energy damage, 3 rounds
  sources:
  - name: default
    CL: 3
    concentration: 6
spells:
  entries:
  - name: hold person
    source: Cleric
    level: 2
    DC: 16
  - is_domain_spell: true
    name: magic mouth
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    count: 2
    DC: 15
  - is_domain_spell: true
    name: erase
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 3
    concentration: 6
    slots:
      0: at-will
    domains:
    - magic
    - rune
tactics:
  During Combat: The cleric uses his scroll of darkness, then follows with ranged
    spells.
ability_scores:
  STR: 12
  DEX: 8
  CON: 13
  INT: 10
  WIS: 16
  CHA: 15
BAB: 2
CMB: 3
CMD: 12
feats:
- name: Extra Channel
- name: Scribe Scroll
- name: Selective Channeling
- name: Spell Focus (enchantment)
skills:
  Knowledge (arcana): 7
  Perception: 3
  Sense Motive: 9
  Spellcraft: 7
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of invisibility
  - scroll of comprehend languages
  - scroll of cure moderate wounds
  - scroll of darkness
  - scroll of find traps
  - alchemist's fire (2)
  - everburning torch
  - smokesticks (2)
  other:
  - masterwork breastplate
  - light crossbow with 20 bolts
  - quarterstaff
  - silver unholy symbol
  - 537 gp
desc_long: The scholar priest is a devotee of magical knowledge, securing it from
  the unworthy at all costs.

---

# Scholar Priest

**Source** NPC Codex pg. 45
**XP** 600
Human _[[classes/Cleric|cleric]]_ of Nethys 3

CN Medium humanoid (human)
**Init** –1; **Senses** Perception +3

##### Defense

**AC** 15, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+6 armor, –1 Dex)
**hp** 23 (3d8+6)
**Fort** +4, **Ref** +0, **Will** +6

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +3 (1d6+1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +1 (1d8/19–20)
**Special Attacks** channel negative energy 7/day (DC 13, 2d6), hand of the _[[npcs/Acolyte|acolyte]]_ (6/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +6)
6/day—blast rune (1d6+1 energy damage, 3 rounds)
**_Cleric_ Spells Prepared **(CL 3rd; concentration +6)
2nd—_[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Magic Mouth|magic mouth]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Command|command]]_ (2, DC 15), _[[spells/Erase|erase]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D **Domain spell; **Domains **Magic, Rune

### Tactics

**During Combat **The _cleric_ uses his scroll of _[[spells/Darkness|darkness]]_, then follows with ranged spells.

##### Statistics
**Str** 12, **Dex** 8, **Con** 13, **Int** 10, **Wis** 16, **Cha** 15
**Base Atk** +2; **CMB** +3; **CMD** 12
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Knowledge (arcana) +7, Perception +6, Sense Motive +9, Spellcraft +7
**Languages** Common
**SQ** aura
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Comprehend Languages|comprehend languages]]_, scroll of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _darkness_, scroll of _[[spells/Find Traps|find traps]]_, _[[classes/Alchemist|alchemist]]_’s fire (2), _[[items/Mundane/Everburning torch|everburning torch]]_, smokesticks (2); **Other Gear** masterwork _[[items/Armor/Breastplate|breastplate]]_, _light crossbow_ with 20 bolts, _quarterstaff_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 537 gp

The _[[npcs/Scholar Priest|scholar priest]]_ is a devotee of magical knowledge, securing it from the unworthy at all costs.