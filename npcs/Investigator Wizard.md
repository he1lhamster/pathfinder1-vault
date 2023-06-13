---
cssclass: [monsters]
title1: Investigator Wizard
title2: Investigator Wizard
CR: 3
sources:
- name: NPC Codex
  page: 179
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 800
race: Human
classes:
- diviner 4
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 8
AC:
  AC: 18
  touch: 14
  flat_footed: 15
  components:
    armor: 4
    deflection: 1
    dex: 2
    dodge: 1
HP:
  HP: 22
  long: 4d6+6
saves:
  fort: 2
  ref: 3
  will: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: club +1 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: club
      bonus:
      - 1
  ranged:
  - - text: light crossbow +4 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
spell_like_abilities:
  entries:
  - name: diviner's fortune
    source: default
    freq: 7/day
    other: '+2'
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: cat's grace
    source: Diviner
    level: 2
  - name: detect thoughts
    source: Diviner
    level: 2
    DC: 16
  - name: web
    source: Diviner
    level: 2
    count: 2
    DC: 16
  - name: comprehend languages
    source: Diviner
    level: 1
  - name: feather fall
    source: Diviner
    level: 1
  - name: mage armor
    source: Diviner
    level: 1
  - name: magic missile
    source: Diviner
    level: 1
    count: 2
  - name: dancing lights
    source: Diviner
    level: 0
  - name: detect magic
    source: Diviner
    level: 0
  - name: detect poison
    source: Diviner
    level: 0
  - name: message
    source: Diviner
    level: 0
  sources:
  - name: Diviner
    type: prepared
    CL: 4
    concentration: 8
    slots:
      0: at-will
    opposition_schools:
    - illusion
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor.
  During Combat: If surprised, the wizard uses forewarned to cast cat's grace in the
    surprise round. He uses web, color spray, or sleep against targets he intends
    to capture.
  Base Statistics: Without mage armor, the wizard's statistics are AC 14, touch 14,
    flat-footed 11.
ability_scores:
  STR: 8
  DEX: 14
  CON: 13
  INT: 18
  WIS: 12
  CHA: 10
BAB: 2
CMB: 1
CMD: 15
feats:
- name: Combat Casting
- name: Dodge
- name: Improved Initiative
- name: Scribe Scroll
skills:
  Diplomacy: 4
  Intimidate: 4
  Knowledge (arcana): 10
  Knowledge (local): 10
  Knowledge (geography): 8
  Knowledge (history): 8
  Knowledge (nobility): 8
  Knowledge (religion): 8
  Perception: 5
  Sense Motive: 5
  Spellcraft: 11
languages:
- Common
- Draconic
- Dwarven
- Elven
- Orc
special_qualities:
- arcane bond (ring of protection +1)
- forewarned
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of detect thoughts
  - scroll of knock
  - scroll of locate object
  - scrolls of sleep (2)
  - wand of color spray (20 charges)
  other:
  - club
  - light crossbow with 20 bolts
  - ring of protection +1
  - manacles
  - spellbook
  - 125 gp
desc_long: The investigator mage works with city guards to investigate crimes.

---

# Investigator Wizard

**Source** NPC Codex pg. 179
**XP** 800
Human diviner 4

LN Medium humanoid (human)
**Init** +8; **Senses** Perception +5

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 22 (4d6+6)
**Fort** +2, **Ref** +3, **Will** +5

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Club|club]]_ +1 (1d6–1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d8/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
7/day—diviner's fortune (+2)
**Diviner Spells Prepared **(CL 4th; concentration +8)
2nd—cat’s _[[spells/Grace|grace]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), web (2, DC 16)
1st—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_ (2)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Message|message]]_
**Opposition Schools **illusion, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_.
**During Combat **If surprised, the _wizard_ uses forewarned to cast cat’s _grace_ in the surprise round. He uses web, _[[spells/Color Spray|color spray]]_, or sleep against targets he intends to capture.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **14, touch 14, _flat-footed_ 11.

##### Statistics
**Str** 8, **Dex** 14, **Con** 13, **Int** 18, **Wis** 12, **Cha** 10
**Base Atk** +2; **CMB** +1; **CMD** 15
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Diplomacy +4, Intimidate +4, Knowledge (arcana, local) +10, Knowledge (geography, history, nobility, religion) +8, Perception +5, Sense Motive +5, Spellcraft +11
**Languages** Common, Draconic, Dwarven, Elven, _[[monsters/Orc|Orc]]_
**SQ** arcane bond (_[[items/Ring/Ring of Protection +1|ring of protection +1]]_), forewarned
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _detect thoughts_, scroll of _[[spells/Knock|knock]]_, scroll of _[[spells/Locate Object|locate object]]_, scrolls of sleep (2), wand of _color spray_ (20 charges); **Other Gear** _club_, _light crossbow_ with 20 bolts, _ring of protection +1_, manacles, _[[items/Mundane/Spellbook|spellbook]]_, 125 gp

The _[[classes/Investigator|investigator]]_ mage works with city guards to investigate crimes.