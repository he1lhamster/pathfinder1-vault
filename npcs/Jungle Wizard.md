---
cssclass: [monsters]
title1: Jungle Wizard
title2: Jungle Wizard
CR: 4
sources:
- name: NPC Codex
  page: 180
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1200
race: Elf
classes:
- transmuter 5
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 18
  touch: 13
  flat_footed: 15
  components:
    armor: 4
    dex: 3
    natural: 1
HP:
  HP: 28
  long: 5d6+8
saves:
  fort: 2
  ref: 6
  will: 5
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk longsword +3 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 3
  ranged:
  - - text: shortbow +5 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 5
spell_like_abilities:
  entries:
  - name: telekinetic fist
    source: default
    freq: 7/day
    other: 1d4+2 bludgeoning
  sources:
  - name: default
    CL: 5
    concentration: 9
spells:
  entries:
  - name: beast shape I
    source: Transmuter
    level: 3
  - name: empowered burning hands
    source: Transmuter
    level: 3
    DC: 16
  - name: displacement
    source: Transmuter
    level: 3
  - name: invisibility
    source: Transmuter
    level: 2
  - name: spider climb
    source: Transmuter
    level: 2
  - name: summon swarm
    source: Transmuter
    level: 2
  - name: web
    source: Transmuter
    level: 2
    DC: 16
  - name: burning hands
    source: Transmuter
    level: 1
    DC: 16
  - name: feather fall
    source: Transmuter
    level: 1
  - name: grease
    source: Transmuter
    level: 1
  - name: mage armor
    source: Transmuter
    level: 1
  - name: obscuring mist
    source: Transmuter
    level: 1
  - name: dancing lights
    source: Transmuter
    level: 0
  - name: ghost sound
    source: Transmuter
    level: 0
    DC: 14
  - name: mage hand
    source: Transmuter
    level: 0
  - name: touch of fatigue
    source: Transmuter
    level: 0
    DC: 14
  sources:
  - name: Transmuter
    type: prepared
    CL: 5
    concentration: 9
    slots:
      0: at-will
    opposition_schools:
    - divination
    - enchantment
tactics:
  Before Combat: The wizard casts mage armor. When she prepares spells, she uses physical
    enhancement to increase her Constitution. She studies the combat area for the
    best places to use spells like grease and web, then hides in ambush.
  During Combat: The wizard casts web on her opponents or in their path (especially
    if there is a pit or ravine present). She casts summon swarm into the web. If
    trapped opponents are escaping from the web, she casts empowered burning hands
    on them.
  Base Statistics: Without mage armor, the wizard's statistics are AC 14, touch 13,
    flat-footed 11.
ability_scores:
  STR: 10
  DEX: 16
  CON: 13
  INT: 18
  WIS: 12
  CHA: 8
BAB: 2
CMB: 2
CMD: 15
feats:
- name: Empower Spell
- name: Improved Initiative
- name: Lightning Reflexes
- name: Scribe Scroll
- name: Spell Focus (evocation)
skills:
  Acrobatics: 7
  Climb: 3
  Fly: 7
  Knowledge (arcana): 12
  Knowledge (geography): 10
  Knowledge (history): 9
  Knowledge (nature): 11
  Perception: 7
  Spellcraft: 12
    to identify magic item properties: 14
  Survival: 4
  Swim: 1
languages:
- Common
- Draconic
- Elven
- Gnoll
- Goblin
- Orc
special_qualities:
- arcane bond (monkey)
- elven magic
- physical enhancement +2
- weapon familiarity
gear:
  combat:
  - potion of cure moderate wounds
  - potions of pass without trace (2)
  - scroll of cat's grace
  - scroll of pyrotechnics
  - scroll of stinking cloud
  - scroll of web
  other:
  - masterwork longsword
  - shortbow with 20 arrows
  - amulet of natural armor +1
  - spellbook
  - 104 gp
desc_long: Jungle wizards live in harmony with nature. They're frequently mistaken
  for druids, and often use such misunderstandings to their advantage. Many jungle
  wizards use natural materials for their magical gear, such as large leaves or hides
  for spellbooks and scrolls, unworked tree branches for wands, or grasses that can
  be knotted into the shapes of rings.

---

# Jungle Wizard

**Source** NPC Codex pg. 180
**XP** 1,200
Elf transmuter 5

NE Medium humanoid (elf)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +3 Dex, +1 natural)
**hp** 28 (5d6+8)
**Fort** +2, **Ref** +6, **Will** +5; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +3 (1d8/19–20)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +5 (1d6/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +9)
7/day—telekinetic fist (1d4+2 bludgeoning)
**Transmuter Spells Prepared **(CL 5th; concentration +9)
3rd—_[[spells/Beast Shape I|beast shape I]]_, empowered _[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Displacement|displacement]]_
2nd—_[[spells/Invisibility|invisibility]]_, _[[spells/Spider Climb|spider climb]]_, _[[spells/Summon Swarm|summon swarm]]_, web (DC 16)
1st—_burning hands_ (DC 16), _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 14)
**Opposition Schools **_[[spells/Divination|divination]]_, enchantment

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_. When she prepares spells, she uses physical enhancement to increase her Constitution. She studies the combat area for the best places to use spells like _grease_ and web, then hides in ambush.
**During Combat **The _wizard_ casts web on her opponents or in their path (especially if there is a pit or ravine present). She casts _summon swarm_ into the web. If trapped opponents are escaping from the web, she casts empowered _burning hands_ on them.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **14, touch 13, _flat-footed_ 11.

##### Statistics
**Str** 10, **Dex** 16, **Con** 13, **Int** 18, **Wis** 12, **Cha** 8
**Base Atk** +2; **CMB** +2; **CMD** 15
**Feats** _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Acrobatics +7, _[[universal monster rules/Climb|Climb]]_ +3, Fly +7, Knowledge (arcana) +12, Knowledge (geography) +10, Knowledge (history) +9, Knowledge (nature) +11, Perception +7, Spellcraft +12 (+14 to _[[spells/Identify|identify]]_ magic item properties), Survival +4, Swim +1
**Languages** Common, Draconic, Elven, _[[monsters/Gnoll|Gnoll]]_, _[[monsters/Goblin|Goblin]]_, _[[monsters/Orc|Orc]]_
**SQ** arcane bond (monkey), elven magic, physical enhancement +2, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potions of _[[spells/Pass without Trace|pass without trace]]_ (2), scroll of cat’s _[[spells/Grace|grace]]_, scroll of _[[spells/Pyrotechnics|pyrotechnics]]_, scroll of _[[spells/Stinking Cloud|stinking cloud]]_, scroll of web; **Other Gear** masterwork _longsword_, _shortbow_ with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 104 gp

Jungle wizards live in harmony with nature. They’re frequently mistaken for druids, and often use such misunderstandings to their advantage. Many jungle wizards use natural materials for their magical gear, such as large leaves or hides for spellbooks and scrolls, unworked tree branches for wands, or grasses that can be knotted into the shapes of rings.