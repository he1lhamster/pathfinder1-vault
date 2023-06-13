---
cssclass: [monsters]
title1: Minotaur, Prophet of Baphomet
desc_short: This white-maned minotaur's gilt-edged robes project elegance and terror
  in equal measure. The cloud of heady incense about her form doesn't conceal the
  distinct scent of brimstone.
title2: Prophet of Baphomet
CR: 13
sources:
- name: Inner Sea Monster Codex
  page: 45
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 25600
race: Minotaur
classes:
- cleric of Baphomet 11 (Pathfinder RPG Bestiary 206)
alignment: CE
size: Large
type: monstrous humanoid
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 10
  flat_footed: 24
  components:
    armor: 8
    deflection: 1
    natural: 6
    size: -1
HP:
  HP: 127
  long: 11d8+6d10+45
  HD: 17
saves:
  fort: 14
  ref: 12
  will: 18
defensive_abilities:
- natural cunning
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 glaive +21/+16/+11 (2d8+10/19-20/×3)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 glaive
      bonus:
      - 21
      - 16
      - 11
    - text: gore +19 (1d6+9)
      entries:
      - - damage: 1d6+9
      attack: gore
      bonus:
      - 19
  ranged:
  - - text: mwk light crossbow +14 (2d6/19-20)
      entries:
      - - damage: 2d6
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 14
  special:
  - channel negative energy 3/day (DC 15, 6d6)
  - scythe of evil (5 rounds, 1/day)
  - might of the gods (+11, 11 rounds/day)
  - powerful charge (gore, 2d6+9)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: touch of evil
    source: default
    freq: 7/day
    other: 5 rounds
  - name: strength surge
    source: default
    freq: 7/day
    other: '+5'
  sources:
  - name: default
    CL: 11
    concentration: 15
spells:
  entries:
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 21
  - is_domain_spell: true
    name: stoneskin
    source: Cleric
    level: 6
  - name: flame strike
    source: Cleric
    level: 5
    DC: 20
  - is_domain_spell: true
    name: righteous might
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    DC: 19
  - name: air walk
    source: Cleric
    level: 4
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 19
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: spell immunity
    source: Cleric
    level: 4
  - name: cure serious wounds
    source: Cleric
    level: 3
  - name: deeper darkness
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: meld into stone
    source: Cleric
    level: 3
  - name: mind maze
    source: Cleric
    level: 3
    DC: 17
  - is_domain_spell: true
    name: bull's strength
    source: Cleric
    level: 2
  - name: resist energy
    source: Cleric
    level: 2
  - name: shatter
    source: Cleric
    level: 2
    DC: 17
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: status
    source: Cleric
    level: 2
  - name: wind wall
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 15
  - name: cause fear
    source: Cleric
    level: 1
    DC: 15
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 14
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 11
    concentration: 15
    slots:
      0: at-will
    domains:
    - evil
    - strength
ability_scores:
  STR: 23
  DEX: 10
  CON: 13
  INT: 9
  WIS: 18
  CHA: 10
BAB: 14
CMB: 21
CMB_other: +23 bull rush
CMD: 32
CMD_other: 34 vs. bull rush
feats:
- name: Combat Reflexes
- name: Improved Bull Rush
- name: Improved Critical (glaive)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Spell Focus (evocation)
- name: Toughness
- name: Weapon Focus (glaive)
skills:
  Intimidate: 11
  Knowledge (planes): 6
  Knowledge (religion): 6
  Linguistics: 4
  Perception: 12
  Spellcraft: 8
languages:
- Abyssal
- Common
- Giant
gear:
  combat:
  - potion of bear's endurance
  - potion of rage
  - scrolls of find traps (2)
  - scroll of invisibility purge
  - scroll of lesser planar ally
  - scroll of mass bull's strength
  - wand of cure serious wounds (12 charges)
  - wand of protection from law (22 charges)
  - wand of shield of faith (15 charges)
  - alchemist's fire (5)
  - unholy water (2)
  other:
  - +2 breastplate
  - +1 glaive
  - mwk light crossbow with 20 bolts
  - amulet of natural armor +1
  - cloak of resistance +2
  - headband of inspired wisdom +2
  - ring of protection +1
  - brass unholy symbol
  - spell component pouch
  - granite and diamond dust (500 gp)
ecology:
  environment: temperate ruins or underground
desc_long: Just as minotaurs believe they're direct descendants of Baphomet, minotaur
  prophets consider themselves his ideal mortal servitors. Prophets favor cunning
  gambits and manipulation over direct confrontation, and toy with captives and even
  their own cultists. Prophets also honor the Lord of the Labyrinth's more bestial
  interests; worshipers and enemies alike often fall victim to a prophet's monstrous
  appetite for flesh.

---

# Minotaur, Prophet of Baphomet
This white-maned _[[monsters/Minotaur|minotaur]]_’s gilt-edged robes project elegance and terror in equal measure. The cloud of heady _[[items/Mundane/Incense|incense]]_ about her form doesn’t conceal the distinct _[[universal monster rules/Scent|scent]]_ of brimstone.
**Source** Inner Sea Monster Codex pg. 45
**XP** 25,600
_Minotaur_ _[[classes/Cleric|cleric]]_ of Baphomet 11 (Pathfinder RPG Bestiary 206)
CE Large monstrous humanoid
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 24, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+8 armor, +1 deflection, +6 natural, –1 size)
**hp** 127 (17 HD; 11d8+6d10+45)
**Fort** +14, **Ref** +12, **Will** +18
**Defensive Abilities** natural _[[items/Weapon Magic Abilities/Cunning|cunning]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Glaive|glaive]]_ +21/+16/+11 (2d8+10/19–20/×3), gore +19 (1d6+9)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +14 (2d6/19–20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 3/day (DC 15, 6d6), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day), might of the gods (+11, 11 rounds/day), _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d6+9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
7/day—_[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
7/day—strength surge (+5)
**_Cleric_ Spells Prepared **(CL 11th; concentration +15)
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 21), _[[spells/Stoneskin|stoneskin]]_
5th—_[[spells/Flame Strike|flame strike]]_ (DC 20), _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 19)
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Chaos Hammer|chaos hammer]]_ (DC 19), _[[spells/Cure Critical Wounds|cure critical wounds]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Spell Immunity|spell immunity]]_
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Mind Maze|mind maze]]_ (DC 17)
2nd— bull’s strength, _[[spells/Resist Energy|resist energy]]_, _[[spells/Shatter|shatter]]_ (DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Status|status]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Bane|bane]]_ (DC 15), _[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Evil, Strength

##### Statistics
**Str** 23, **Dex** 10, **Con** 13, **Int** 9, **Wis** 18, **Cha** 10
**Base Atk** +14; **CMB** +21 (+23 bull rush); **CMD** 32 (34 vs. bull rush)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_glaive_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_glaive_)
**Skills** Intimidate +11, Knowledge (planes) +6, Knowledge (religion) +6, Linguistics +4, Perception +12, Spellcraft +8
**Languages** Abyssal, Common, Giant
**Combat Gear** potion of bear’s _[[feats/Endurance|endurance]]_, potion of _[[spells/Rage|rage]]_, scrolls of _[[spells/Find Traps|find traps]]_ (2), scroll of _[[spells/Invisibility Purge|invisibility purge]]_, scroll of lesser _[[spells/Planar Ally|planar ally]]_, scroll of mass bull’s strength, wand of _cure serious wounds_ (12 charges), wand of _[[spells/Protection From Law|protection from law]]_ (22 charges), wand of _shield of faith_ (15 charges), _[[classes/Alchemist|alchemist]]_’s fire (5), _[[items/Weapon Magic Abilities/Unholy|unholy]]_ water (2); **Other Gear** +2 _[[items/Armor/Breastplate|breastplate]]_, +1 _glaive_, mwk _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, brass _unholy_ symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, granite and diamond dust (500 gp)

##### Ecology

**Environment** temperate ruins or underground

##### Description

Just as minotaurs believe they’re direct descendants of Baphomet, _minotaur_ prophets consider themselves his ideal mortal servitors. Prophets favor _cunning_ gambits and manipulation over direct confrontation, and toy with captives and even their own cultists. Prophets also honor the Lord of the Labyrinth’s more bestial interests; worshipers and enemies alike often fall victim to a _[[feats/Prophet|prophet]]_’s monstrous appetite for flesh.