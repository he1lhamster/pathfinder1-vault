---
cssclass: [monsters]
title1: Street Magician
title2: Street Magician
CR: 1
sources:
- name: NPC Codex
  page: 178
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 400
race: Gnome
classes:
- enchanter 2
alignment: CN
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 13
  touch: 13
  flat_footed: 11
  components:
    dex: 1
    dodge: 1
    size: 1
HP:
  HP: 14
  long: 2d6+5
saves:
  fort: 2
  ref: 1
  will: 2
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +3 (1d3+1/19-20)
      entries:
      - - damage: 1d3+1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 3
  ranged:
  - - text: light crossbow +4 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  - name: dazing touch
    source: arcane school
    freq: 5/day
  sources:
  - name: default
    CL: 2
    concentration: 3
  - name: arcane school
    CL: 2
    concentration: 4
spells:
  entries:
  - name: charm person
    source: Enchanter
    level: 1
    DC: 13
  - name: color spray
    source: Enchanter
    level: 1
    DC: 14
  - name: grease
    source: Enchanter
    level: 1
  - name: sleep
    source: Enchanter
    level: 1
    DC: 13
  - name: dancing lights
    source: Enchanter
    level: 0
  - name: ghost sound
    source: Enchanter
    level: 0
    count: 2
    DC: 13
  - name: mage hand
    source: Enchanter
    level: 0
  sources:
  - name: Enchanter
    type: prepared
    CL: 2
    concentration: 4
    slots:
      0: at-will
    opposition_schools:
    - abjuration
    - necromancy
tactics:
  During Combat: The wizard casts color spray, then casts grease between himself and
    foes. If threatened, he drinks his potion of invisibility.
ability_scores:
  STR: 12
  DEX: 13
  CON: 14
  INT: 15
  WIS: 8
  CHA: 12
BAB: 1
CMB: 1
CMD: 13
feats:
- name: Dodge
- name: Scribe Scroll
skills:
  Bluff: 3
  Knowledge (arcana): 6
  Knowledge (geography): 6
  Knowledge (history): 6
  Knowledge (local): 7
  Perception: 2
  Spellcraft: 6
languages:
- Common
- Dwarven
- Gnome
- Halfling
special_qualities:
- arcane bond (amulet)
- enchanting smile
gear:
  combat:
  - potions of cure light wounds (2)
  - scrolls of disguise self (2)
  - scrolls of expeditious retreat (2)
  - scroll of invisibility
  - scrolls of obscuring mist (2)
  - alchemist's fire (2)
  - thunderstones (2)
  other:
  - dagger
  - light crossbow with 10 masterwork bolts
  - brooch of shielding (10 charges)
  - smokesticks (2)
  - spellbook
  - 67 gp
desc_long: The street magician uses his talents to make money.

---

# Street Magician

**Source** NPC Codex pg. 178
**XP** 400
Gnome enchanter 2

CN Small humanoid (gnome)
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +2

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+1 Dex, +1 dodge, +1 size)
**hp** 14 (2d6+5)
**Fort** +2, **Ref** +1, **Will** +2; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +3 (1d3+1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d6/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +3)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
 **Arcane School _Spell-Like Abilities_ **(CL 2nd; concentration +4)
 5/day—dazing touch
**Enchanter Spells Prepared **(CL 2nd; concentration +4)
1st—_[[spells/Charm Person|charm person]]_ (DC 13), _[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Grease|grease]]_, sleep (DC 13)
0 (at will)—_dancing lights_, _ghost sound_ (2, DC 13), _[[spells/Mage Hand|mage hand]]_
**Opposition Schools **abjuration, necromancy

### Tactics

**During Combat **The _[[classes/Wizard|wizard]]_ casts _color spray_, then casts _grease_ between himself and foes. If threatened, he drinks his potion of _[[spells/Invisibility|invisibility]]_.

##### Statistics
**Str** 12, **Dex** 13, **Con** 14, **Int** 15, **Wis** 8, **Cha** 12
**Base Atk** +1; **CMB** +1; **CMD** 13
**Feats** _Dodge_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Bluff +3, Knowledge (arcana, geography, history) +6, Knowledge (local) +7, Perception +2, Spellcraft +6
**Languages** Common, Dwarven, Gnome, Halfling
**SQ** arcane bond (amulet), enchanting smile
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), scrolls of _[[spells/Disguise Self|disguise self]]_ (2), scrolls of _[[spells/Expeditious Retreat|expeditious retreat]]_ (2), scroll of _invisibility_, scrolls of _[[spells/Obscuring Mist|obscuring mist]]_ (2), _[[classes/Alchemist|alchemist]]_’s fire (2), thunderstones (2); **Other Gear** _dagger_, _light crossbow_ with 10 masterwork bolts, _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_ (10 charges), smokesticks (2), _[[items/Mundane/Spellbook|spellbook]]_, 67 gp

The _[[npcs/Street Magician|street magician]]_ uses his talents to make money.