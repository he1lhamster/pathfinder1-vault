---
cssclass: [monsters]
title1: Undead Bane
title2: Undead Bane
CR: 16
sources:
- name: NPC Codex
  page: 202
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Human
classes:
- ranger 9
- sorcerer 1
- arcane archer 7
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 9
AC:
  AC: 26
  touch: 17
  flat_footed: 21
  components:
    armor: 6
    deflection: 1
    dex: 4
    dodge: 1
    insight: 1
    natural: 3
HP:
  HP: 138
  long: 9d10+1d6+7d10+43
saves:
  fort: 16
  ref: 17
  will: 11
defensive_abilities:
- evasion
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 short sword +17/+12/+7/+2 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: +1 short sword
      bonus:
      - 17
      - 12
      - 7
      - 2
  ranged:
  - - text: +2 flaming shock shortbow +24/+19/+14/+9 (1d6+2/×3 plus 1d6 electricity
        and 1d6 fire)
      entries:
      - - damage: 1d6+2
          crit_multiplier: 3
        - damage: 1d6
          type: electricity
        - damage: 1d6
          type: fire
      attack: +2 flaming shock shortbow
      bonus:
      - 24
      - 19
      - 14
      - 9
  special:
  - enhance arrows (distance, elemental, elemental burst, magic)
  - favored enemy (humans +2, undead +4)
  - imbue arrow
  - phase arrow (1/day)
  - seeker arrow (2/day)
spell_like_abilities:
  entries:
  - name: touch of destiny
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 6
    concentration: 8
spells:
  entries:
  - name: barkskin
    source: Ranger
    level: 2
  - name: snare
    source: Ranger
    level: 2
  - name: alarm
    source: Ranger
    level: 1
  - name: entangle
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  - name: slow
    source: Sorcerer
    level: 3
    DC: 15
  - name: false life
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 13
  - name: detect undead
    source: Sorcerer
    level: 1
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 13
  - name: true strike
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Ranger
    type: prepared
    CL: 6
    concentration: 8
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 8
    failure_chance: 20%
    slots:
      3: 3
      2: 6
      1: 7
      0: at-will
    bloodline: destined
tactics:
  Before Combat: The arcane archer casts barkskin and uses her wand of shield. She
    prepares frost burst arrows using her enhance arrows ability.
  During Combat: Preferring to stay out of the reach and sight of powerful enemies,
    the arcane archer casts fly and greater invisibility on herself, takes flight,
    and pelts her enemies with arrows from relative safety.
  Base Statistics: Without barkskin, the arcane archer's statistics are AC 24, touch
    17, flat-footed 19
ability_scores:
  STR: 10
  DEX: 20
  CON: 14
  INT: 8
  WIS: 14
  CHA: 14
BAB: 16
CMB: 16
CMD: 34
feats:
- name: Deadly Aim
- name: Dodge
- name: Endurance
- name: Eschew Materials
- name: Great Fortitude
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Vital Strike
- name: Manyshot
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Vital Strike
- name: Weapon Focus (shortbow)
skills:
  Climb: 12
  Heal: 15
  Intimidate: 12
  Knowledge (religion): 9
  Perception: 22
  Stealth: 17
  Survival: 15
  Swim: 12
languages:
- Common
special_qualities:
- bloodline arcana (gains a luck bonus on saves when casting personal-range spells)
- evasion
- favored terrain (forest +2, underground +4)
- hunter's bond (companions)
- swift tracker
- track +4
- wild empathy +11
- woodland stride
gear:
  combat:
  - +1 ghost touch arrows (10)
  - +1 undead-bane arrows (10)
  - potion of cure moderate wounds
  - potion of cure serious wounds
  - potion of lesser restoration
  - potion of remove disease
  - scrolls of greater invisibility (2)
  - scrolls of invisibility (2)
  - wand of fly (10 charges)
  - wand of shield (20 charges)
  - holy water (10)
  other:
  - +2 chain shirt
  - +2 flaming shock shortbow with 20 arrows
  - +1 short sword
  - amulet of natural armor +1
  - belt of physical might +2 (Dex, Con)
  - cloak of resistance +2
  - dusky rose prism ioun stone
  - efficient quiver
  - ring of feather fall
  - ring of protection +1
  - 238 gp
desc_long: Though these archers primarily hunt undead, they are dangerous foes for
  any creatures.

---

# Undead Bane

**Source** NPC Codex pg. 202
**XP** 76,800
Human _[[classes/Ranger|ranger]]_ 9/sorcerer 1/arcane archer 7

N Medium humanoid (human)
**Init** +9; **Senses** Perception +22

##### Defense

**AC** 26, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +1 insight, +3 natural)
**hp** 138 (9d10+1d6+7d10+43)
**Fort** +16, **Ref** +17, **Will** +11
**Defensive Abilities** evasion

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Short sword|short sword]]_ +17/+12/+7/+2 (1d6+1/19–20)
**Ranged** +2 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Shortbow|shortbow]]_ +24/+19/+14/+9 (1d6+2/×3 plus 1d6 electricity and 1d6 fire)
**Special Attacks** enhance arrows (distance, elemental, elemental burst, magic), favored enemy (humans +2, undead +4), imbue arrow, _[[items/Ammunition/Phase Arrow|phase arrow]]_ (1/day), seeker arrow (2/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
5/day—touch of destiny
**_Ranger_ Spells Prepared** (CL 6th; concentration +8)
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Snare|snare]]_
1st—_[[spells/Alarm|alarm]]_, _[[spells/Entangle|entangle]]_, _[[spells/Resist Energy|resist energy]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known**(CL 6th; concentration +8; arcane spell failure 20%)
3rd (3/day)—_[[spells/Slow|slow]]_ (DC 15)
2nd (6/day)—_[[spells/False Life|false life]]_, _[[spells/Mirror Image|mirror image]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (DC 13), _[[spells/Detect Undead|detect undead]]_, _[[spells/Silent Image|silent image]]_ (DC 13), _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Disrupt Undead|disrupt undead]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **destined

### Tactics

**Before Combat **The arcane archer casts _barkskin_ and uses her wand of _[[spells/Shield|shield]]_. She prepares frost burst arrows using her enhance arrows ability.
**During Combat **Preferring to stay out of the reach and sight of powerful enemies, the arcane archer casts fly and greater _[[spells/Invisibility|invisibility]]_ on herself, takes _[[universal monster rules/Flight|flight]]_, and pelts her enemies with arrows from relative safety.
**Base Statistics **Without _barkskin_, the arcane archer’s statistics are **AC **24, touch 17, _flat-footed_ 19

##### Statistics
**Str** 10, **Dex** 20, **Con** 14, **Int** 8, **Wis** 14, **Cha** 14
**Base Atk** +16; **CMB** +16; **CMD** 34
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_shortbow_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, _[[spells/Heal|Heal]]_ +15, Intimidate +12, Knowledge (religion) +9, Perception +22, Stealth +17, Survival +15, Swim +12
**Languages** Common
**SQ** bloodline arcana (gains a luck bonus on saves when casting personal-range spells), evasion, favored terrain (forest +2, underground +4), _[[classes/Hunter|hunter]]_’s bond (companions), swift tracker, track +4, wild _[[feats/Empathy|empathy]]_ +11, woodland stride
**Combat Gear** +1 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ arrows (10), +1 undead-bane arrows (10), potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of lesser _[[spells/Restoration|restoration]]_, potion of _[[spells/Remove Disease|remove disease]]_, scrolls of greater _invisibility_ (2), scrolls of _invisibility_ (2), wand of fly (10 charges), wand of _shield_ (20 charges), _[[items/Mundane/Holy water|holy water]]_ (10); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 _flaming_ _shock_ _shortbow_ with 20 arrows, +1 _short sword_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Dex, Con), _[[items/Wondrous Item/Cloak of _Resistance_ +2|cloak of _resistance_ +2]]_, dusky rose prism ioun stone, _[[items/Wondrous Item/Efficient Quiver|efficient quiver]]_, ring of _[[spells/Feather Fall|feather fall]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 238 gp

Though these archers primarily hunt undead, they are dangerous foes for any creatures.