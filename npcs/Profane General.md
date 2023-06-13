---
cssclass: [monsters]
title1: Profane General
title2: Profane General
CR: 12
sources:
- name: NPC Codex
  page: 54
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- cleric of Gorum 13
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 0
AC:
  AC: 22
  touch: 10
  flat_footed: 22
  components:
    armor: 11
    natural: 1
HP:
  HP: 121
  long: 13d8+59
saves:
  fort: 13
  ref: 5
  will: 12
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 flaming greatsword +16/+11 (2d6+8/17-20 plus 1d6 fire)
      entries:
      - - damage: 2d6+8
          crit_range: 17-20
        - damage: 1d6
          type: fire
      attack: +1 flaming greatsword
      bonus:
      - 16
      - 11
  - - text: mwk dagger +15/+10 (1d4+7/19-20)
      entries:
      - - damage: 1d4+7
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 15
      - 10
  ranged:
  - - text: mwk heavy crossbow +10 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 10
  special:
  - channel negative energy 4/day (DC 15, 7d6)
  - might of the gods (+13, 13 rounds/day)
  - weapon master (13 rounds/day)
spell_like_abilities:
  entries:
  - name: battle rage
    source: default
    freq: 6/day
    other: +6 damage
  - name: strength surge
    source: default
    freq: 6/day
    other: '+6'
  sources:
  - name: default
    CL: 13
    concentration: 16
spells:
  entries:
  - is_domain_spell: true
    name: power word blind
    source: Cleric
    level: 7
  - name: word of chaos
    source: Cleric
    level: 7
  - name: heal
    source: Cleric
    level: 6
  - name: mass bull's strength
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: stoneskin
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 18
  - is_domain_spell: true
    name: righteous might
    source: Cleric
    level: 5
  - name: spell resistance
    source: Cleric
    level: 5
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 17
  - name: dismissal
    source: Cleric
    level: 4
    DC: 17
  - is_domain_spell: true
    name: divine power
    source: Cleric
    level: 4
  - name: restoration
    source: Cleric
    level: 4
  - name: spell immunity
    source: Cleric
    level: 4
  - name: cure serious wounds
    source: Cleric
    level: 3
    count: 2
  - name: invisibility purge
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: wind wall
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - name: resist energy
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 14
  - name: bless
    source: Cleric
    level: 1
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 2
  - is_domain_spell: true
    name: enlarge person
    source: Cleric
    level: 1
    DC: 14
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 13
    concentration: 16
    slots:
      0: at-will
    domains:
    - strength
    - war
tactics:
  Before Combat: The cleric casts bear's endurance and stoneskin.
  During Combat: The cleric targets weak-looking opponents first, using spells to
    blind and damage multiple enemies before attacking with her greatsword.
  Base Statistics: Without bear's endurance and stoneskin, the cleric's statistics
    are hp 95, Fort +11; DR none; Con 14.
ability_scores:
  STR: 20
  DEX: 10
  CON: 18
  INT: 12
  WIS: 17
  CHA: 8
BAB: 9
CMB: 14
CMD: 24
feats:
- name: Cleave
- name: Combat Casting
- name: Extra Channel
- name: Heavy Armor Proficiency
- name: Improved Critical (greatsword)
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (greatsword)
skills:
  Diplomacy: 7
  Heal: 11
  Intimidate: 4
  Knowledge (engineering): 6
  Knowledge (nobility): 6
  Knowledge (planes): 6
  Knowledge (history): 9
  Knowledge (religion): 9
  Knowledge (local): 3
  Perception: 16
  Ride: -1
  Spellcraft: 9
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of haste
  other:
  - +2 full plate
  - +1 flaming greatsword
  - masterwork dagger (2)
  - masterwork heavy crossbow
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - iron unholy symbol
  - granite and diamond dust for stoneskin (worth 250 gp)
  - 276 gp
desc_long: The profane general, a powerful cleric of war who leads by example, cleaves
  through enemies to inspire her allies and followers to greater glory and victory.

---

# Profane General

**Source** NPC Codex pg. 54
**XP** 19,200
Human _[[classes/Cleric|cleric]]_ of Gorum 13

CN Medium humanoid (human)
**Init** +0; **Senses** Perception +16

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+11 armor, +1 natural)
**hp** 121 (13d8+59)
**Fort** +13, **Ref** +5, **Will** +12
**DR** 10/adamantine (150 points)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Greatsword|greatsword]]_ +16/+11 (2d6+8/17–20 plus 1d6 fire) or mwk _[[items/Weapon/Dagger|dagger]]_ +15/+10 (1d4+7/19–20)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +10 (1d10/19–20)
**Special Attacks** channel negative energy 4/day (DC 15, 7d6), might of the gods (+13, 13 rounds/day), weapon master (13 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +16)
6/day—battle _[[spells/Rage|rage]]_ (+6 damage), strength surge (+6)
**_Cleric_ Spells Prepared **(CL 13th; concentration +16)
7th—_[[spells/Power Word Blind|power word blind]]_, _[[spells/Word Of Chaos|word of chaos]]_
6th—_[[spells/Heal, Mass|heal, mass]]_ bull’s strength, _[[spells/Stoneskin|stoneskin]]_
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Flame Strike|flame strike]]_ (DC 18), _[[spells/Righteous Might|righteous might]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 17), _[[spells/Dismissal|dismissal]]_ (DC 17), _[[spells/Divine Power|divine power]]_, _[[spells/Restoration|restoration]]_, _[[spells/Spell Immunity|spell immunity]]_
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Prayer|prayer]]_, _[[spells/Wind Wall|wind wall]]_
2nd—aid, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Delay Poison|delay poison]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Resist Energy|resist energy]]_ (DC 15), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_ (2), enlarge personD (DC 14), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light
**D **Domain spell; **Domains **Strength, War

### Tactics

**Before Combat **The _cleric_ casts bear’s _endurance_ and _stoneskin_.
**During Combat **The _cleric_ targets weak-looking opponents first, using spells to blind and damage multiple enemies before attacking with her _greatsword_.
**Base Statistics **Without bear’s _endurance_ and _stoneskin_, the _cleric_’s statistics are **hp **95, **Fort **+11; **DR **none; **Con **14.

##### Statistics
**Str** 20, **Dex** 10, **Con** 18, **Int** 12, **Wis** 17, **Cha** 8
**Base Atk** +9; **CMB** +14; **CMD** 24
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greatsword_), _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greatsword_)
**Skills** Diplomacy +7, _[[spells/Heal|Heal]]_ +11, Intimidate +4, Knowledge (engineering, nobility, planes) +6, Knowledge (history, religion) +9, Knowledge (local) +3, Perception +16, Ride –1, Spellcraft +9
**Languages** Common
**SQ** aura
**Combat Gear** potion of _[[spells/Haste|haste]]_; **Other Gear** +2 _[[items/Armor/Full plate|full plate]]_, +1 _flaming_ _greatsword_, masterwork _dagger_ (2), masterwork _heavy crossbow_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, iron _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, granite and diamond dust for _stoneskin_ (worth 250 gp), 276 gp

The _[[npcs/Profane General|profane general]]_, a powerful _cleric_ of war who leads by example, cleaves through enemies to inspire her allies and followers to greater glory and victory.