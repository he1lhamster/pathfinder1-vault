---
cssclass: [monsters]
title1: Sacred Sorcerer
title2: Sacred Sorcerer
CR: 8
sources:
- name: NPC Codex
  page: 166
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Human
classes:
- sorcerer 9
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 19
  touch: 14
  flat_footed: 16
  components:
    armor: 4
    deflection: 1
    dex: 2
    dodge: 1
    natural: 1
HP:
  HP: 75
  long: 9d6+41
saves:
  fort: 5
  ref: 8
  will: 9
resistances:
  acid: 10
  cold: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk morningstar +4 (1d8-1)
      entries:
      - - damage: 1d8-1
      attack: mwk morningstar
      bonus:
      - 4
  ranged:
  - - text: javelin +6 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: javelin
      bonus:
      - 6
  - - text: ray +7 (by spell)
      entries:
      - - effect: by spell
      attack: ray
      bonus:
      - 7
spell_like_abilities:
  entries:
  - name: heavenly fire
    source: default
    freq: 7/day
    other: 1d4+4 divine energy
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - name: remove curse
    source: Sorcerer
    level: 4
  - name: summon monster IV
    source: Sorcerer
    level: 4
  - name: wall of fire
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 17
  - name: magic circle against evil
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 17
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: shatter
    source: Sorcerer
    level: 2
  - name: bless
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 15
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: daze
    source: Sorcerer
    level: 0
    DC: 14
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 9
    concentration: 13
    slots:
      4: 5
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: celestial
tactics:
  Before Combat: The sorcerer casts false life and mage armor.
  During Combat: The sorcerer casts summon monster IV to summon a celestial giant
    wasp, then shoots ray spells at her foes.
  Base Statistics: Without false life and mage armor, the sorcerer's statistics are
    AC 15, touch 14, flat-footed 12; hp 61.
ability_scores:
  STR: 8
  DEX: 14
  CON: 12
  INT: 10
  WIS: 14
  CHA: 18
BAB: 4
CMB: 3
CMD: 17
feats:
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Lightning Reflexes
- name: Mobility
- name: Point-Blank Shot
- name: Toughness
- name: Weapon Focus (ray)
skills:
  Diplomacy: 5
  Handle Animal: 5
  Heal: 6
  Knowledge (arcana): 10
  Knowledge (religion): 1
  Linguistics: 1
  Perception: 9
  Spellcraft: 10
  Survival: 3
languages:
- Celestial
- Common
special_qualities:
- bloodline arcana (summoned creatures gain DR 4/evil)
- wings of heaven (9 minutes/day)
gear:
  combat:
  - potion of cure serious wounds
  - scroll of confusion
  - wand of bull's strength (25 charges)
  - holy water (2)
  other:
  - javelins (4)
  - masterwork morningstar
  - amulet of natural armor +1
  - cloak of resistance +1
  - ring of protection +1
  - 988 gp
desc_long: The sacred sorcerer is an agent of the gods, less constrained than a priest
  and armed with magic rarely used by other servants of the divine.

---

# Sacred Sorcerer

**Source** NPC Codex pg. 166
**XP** 4,800
Human _[[classes/Sorcerer|sorcerer]]_ 9

N Medium humanoid (human)
**Init** +2; **Senses** Perception +9

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 75 (9d6+41)
**Fort** +5, **Ref** +8, **Will** +9
**Resist** acid 10, cold 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Morningstar|morningstar]]_ +4 (1d8–1)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +6 (1d6–1) or ray +7 (by spell)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
7/day—heavenly fire (1d4+4 divine energy)
**_Sorcerer_ Spells Known **(CL 9th; concentration +13)
4th (5/day)—_[[spells/Remove Curse|remove curse]]_, _[[spells/Summon Monster IV|summon monster IV]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 17), _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 17)
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/False Life|false life]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Shatter|shatter]]_
1st (7/day)—_[[spells/Bless|bless]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15), _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **celestial

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _mage armor_.
**During Combat **The _sorcerer_ casts _summon monster IV_ to _[[universal monster rules/Summon|summon]]_ a celestial giant wasp, then shoots ray spells at her foes.
**Base Statistics **Without _false life_ and _mage armor_, the _sorcerer_’s statistics are **AC **15, touch 14, _flat-footed_ 12; **hp **61.

##### Statistics
**Str** 8, **Dex** 14, **Con** 12, **Int** 10, **Wis** 14, **Cha** 18
**Base Atk** +4; **CMB** +3; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (ray)
**Skills** Diplomacy +5, Handle Animal +5, _[[spells/Heal|Heal]]_ +6, Knowledge (arcana) +10, Knowledge (religion) +1, Linguistics +1, Perception +9, Spellcraft +10, Survival +3
**Languages** Celestial, Common
**SQ** bloodline arcana (summoned creatures gain DR 4/evil), wings of heaven (9 minutes/day)
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _[[spells/Confusion|confusion]]_, wand of bull’s strength (25 charges), _[[items/Mundane/Holy water|holy water]]_ (2); **Other Gear** javelins (4), masterwork _morningstar_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 988 gp

The _[[npcs/Sacred Sorcerer|sacred sorcerer]]_ is an agent of the gods, less constrained than a priest and armed with magic rarely used by other servants of the divine.