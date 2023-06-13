---
cssclass: [monsters]
title1: Divine Loremaster
title2: Divine Loremaster
CR: 8
sources:
- name: NPC Codex
  page: 224
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Halfling
classes:
- cleric of Abadar 7
- loremaster 2
alignment: LN
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 2
AC:
  AC: 20
  touch: 14
  flat_footed: 18
  components:
    armor: 6
    deflection: 1
    dex: 2
    size: 1
HP:
  HP: 42
  long: 7d8+2d6
saves:
  fort: 9
  ref: 8
  will: 12
  other: +2 vs. fear
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk heavy mace +6/+1 (1d6-2)
      entries:
      - - damage: 1d6-2
      attack: mwk heavy mace
      bonus:
      - 6
      - 1
  special:
  - channel positive energy 5/day (DC 15, 4d6)
spell_like_abilities:
  entries:
  - name: resistant touch
    source: default
    freq: 6/day
  - name: touch of law
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 9
    concentration: 12
spells:
  entries:
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: spell resistance
    source: Cleric
    level: 5
  - name: discern lies
    source: Cleric
    level: 4
    DC: 17
  - name: divination
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: order's wrath
    source: Cleric
    level: 4
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: locate object
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against chaos
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: remove disease
    source: Cleric
    level: 3
  - name: augury
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - name: lesser restoration
    source: Cleric
    level: 2
  - name: status
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: shield other
    source: Cleric
    level: 2
  - name: zone of truth
    source: Cleric
    level: 2
    DC: 15
  - name: bane
    source: Cleric
    level: 1
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - name: comprehend languages
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: sanctuary
    source: Cleric
    level: 1
    DC: 14
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
    CL: 9
    concentration: 12
    slots:
      0: at-will
    domains:
    - law
    - protection
tactics:
  Before Combat: The loremaster casts magic vestment.
  During Combat: The loremaster casts spell resistance and stays out of combat, instead
    supporting her allies with healing spells and information about the foes they
    face.
  Base Statistics: Without magic vestment, the loremaster's statistics are AC 18,
    touch 14, flat-footed 16.
ability_scores:
  STR: 6
  DEX: 14
  CON: 10
  INT: 17
  WIS: 16
  CHA: 15
BAB: 6
CMB: 3
CMD: 16
feats:
- name: Brew Potion
- name: Combat Casting
- name: Empower Spell
- name: Scribe Scroll
- name: Skill Focus (Knowledge [religion])
skills:
  Acrobatics: 3
    when jumping: -1
  Bluff: 7
  Climb: -1
  Diplomacy: 14
  Heal: 11
  Intimidate: 7
  Knowledge (arcana): 4
  Knowledge (engineering): 4
  Knowledge (geography): 4
  Knowledge (nature): 4
  Knowledge (dungeoneering): 6
  Knowledge (history): 9
  Knowledge (local): 9
  Knowledge (nobility): 9
  Knowledge (planes): 14
  Knowledge (religion): 19
  Perception: 14
  Sense Motive: 11
languages:
- Common
- Halfling
special_qualities:
- aura
- lore +1
- secrets (instant mastery)
gear:
  combat:
  - potions of cure light wounds (5)
  - potion of lesser restoration
  - potions of remove disease (2)
  - scrolls of consecrate (2)
  - scrolls of delay poison (2)
  - scrolls of resist energy (2)
  - scrolls of spiritual weapon (2)
  other:
  - masterwork chain shirt
  - masterwork heavy mace
  - cloak of resistance +1
  - headband of vast intelligence +2
  - ring of protection +1
  - incense (worth 50 gp)
  - marked sticks (worth 25 gp)
  - pair of platinum rings (worth 50 gp)
  - 463 gp
desc_long: Divine loremasters support allies with divinations and healing rather than
  slinging combat spells or taking up arms in melee.

---

# Divine Loremaster

**Source** NPC Codex pg. 224
**XP** 4,800
Halfling _[[classes/Cleric|cleric]]_ of Abadar 7/loremaster 2

LN Small humanoid (halfling)
**Init** +2; **Senses** Perception +14

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +1 deflection, +2 Dex, +1 size)
**hp** 42 (7d8+2d6)
**Fort** +9, **Ref** +8, **Will** +12; +2 vs. _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Heavy mace|heavy mace]]_ +6/+1 (1d6–2)
**Special Attacks** channel positive energy 5/day (DC 15, 4d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
6/day—resistant touch, touch of law
**_Cleric_ Spells Prepared **(CL 9th; concentration +12)
5th—_[[spells/Breath Of Life|breath of life]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Discern Lies|discern lies]]_ (DC 17), _[[spells/Divination|divination]]_, order’s wrath
3rd—_[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Remove Disease|remove disease]]_
2nd—_[[spells/Augury|augury]]_, _[[spells/Hold Person|hold person]]_ (DC 15), lesser _[[spells/Restoration|restoration]]_, _[[spells/Status|status]]_, _[[spells/Shield Other|shield other]]_, _[[spells/Zone of Truth|zone of truth]]_ (DC 15)
1st—_[[spells/Bane|bane]]_, _[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 14), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 14)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light
**D **Domain spell; **Domains **Law, Protection

### Tactics

**Before Combat **The loremaster casts _magic vestment_.
**During Combat **The loremaster casts _spell resistance_ and stays out of combat, instead supporting her allies with healing spells and information about the foes they face.
**Base Statistics **Without _magic vestment_, the loremaster’s statistics are **AC **18, touch 14, _flat-footed_ 16.

##### Statistics
**Str** 6, **Dex** 14, **Con** 10, **Int** 17, **Wis** 16, **Cha** 15
**Base Atk** +6; **CMB** +3; **CMD** 16
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [religion])
**Skills** Acrobatics +3 (–1 when jumping), Bluff +7, _[[universal monster rules/Climb|Climb]]_ –1, Diplomacy +14, _[[spells/Heal|Heal]]_ +11, Intimidate +7, Knowledge (arcana, engineering, geography, nature) +4, Knowledge (dungeoneering) +6, Knowledge (history, local, nobility) +9, Knowledge (planes) +14, Knowledge (religion) +19, Perception +14, Sense Motive +11
**Languages** Common, Halfling
**SQ** aura, lore +1, secrets (instant mastery)
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (5), potion of lesser _restoration_, potions of _remove disease_ (2), scrolls of _[[spells/Consecrate|consecrate]]_ (2), scrolls of _[[spells/Delay Poison|delay poison]]_ (2), scrolls of _[[spells/Resist Energy|resist energy]]_ (2), scrolls of _[[spells/Spiritual Weapon|spiritual weapon]]_ (2); **Other Gear** masterwork _[[items/Armor/Chain shirt|chain shirt]]_, masterwork _heavy mace_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Incense|incense]]_ (worth 50 gp), marked sticks (worth 25 gp), pair of platinum rings (worth 50 gp), 463 gp

Divine loremasters support allies with divinations and healing rather than slinging combat spells or taking up arms in melee.