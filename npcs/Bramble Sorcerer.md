---
cssclass: [monsters]
title1: Bramble Sorcerer
title2: Bramble Sorcerer
CR: 4
sources:
- name: NPC Codex
  page: 162
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1200
race: Half-elf
classes:
- sorcerer 5
alignment: LE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 18
  touch: 13
  flat_footed: 15
  components:
    armor: 4
    dex: 2
    dodge: 1
    natural: 1
HP:
  HP: 30
  long: 5d6+10
saves:
  fort: 3
  ref: 6
  will: 4
  other: +2 vs. enchantments
resistances:
  acid: 5
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk light mace +3 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk light mace
      bonus:
      - 3
  - - text: 2 claws +2 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 2
  ranged:
  - - text: mwk light crossbow +5 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 5
  special:
  - claws (2, 1d4, treated as magic, 7 rounds/day)
spells:
  entries:
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 15
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 15
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
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 14
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 5
    concentration: 9
    slots:
      2: 5
      1: 7
      0: at-will
    bloodline: draconic (green)
tactics:
  Before Combat: The sorcerer casts mage armor and resist energy (fire).
  During Combat: The sorcerer casts mirror image, then entangles opponents with his
    wand of entangle (using the Use Magic Device skill). He uses one of his scrolls
    of levitate to avoid melee combat, and casts cause fear to remove opponents threatening
    him.
  Base Statistics: Without mage armor and resist energy, the sorcerer's statistics
    are AC 14, touch 13, flat-footed 11; Resist acid 5.
ability_scores:
  STR: 10
  DEX: 14
  CON: 12
  INT: 13
  WIS: 8
  CHA: 18
BAB: 2
CMB: 2
CMD: 15
feats:
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Lightning Reflexes
- name: Skill Focus (Use Magic Device)
skills:
  Intimidate: 10
  Knowledge (arcana): 7
  Perception: 7
  Spellcraft: 7
  Use Magic Device: 13
languages:
- Common
- Draconic
- Elven
special_qualities:
- bloodline arcana (acid spells deal +1 damage per die)
- elf blood
gear:
  combat:
  - potion of cure moderate wounds
  - potion of invisibility
  - scrolls of levitate (2)
  - scroll of ray of exhaustion
  - scroll of silent image
  - wand of entangle (20 charges)
  - smokestick
  other:
  - masterwork light crossbow with 10 bolts
  - masterwork light mace
  - cloak of resistance +1
  - 190 gp
desc_long: The bramble sorcerer serves the interests of green dragons, walking where
  his masters cannot and speaking on their behalf to other forest dwellers.

---

# Bramble Sorcerer

**Source** NPC Codex pg. 162
**XP** 1,200
Half-elf _[[classes/Sorcerer|sorcerer]]_ 5

LE Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 30 (5d6+10)
**Fort** +3, **Ref** +6, **Will** +4; +2 vs. enchantments
**Resist** acid 5, fire 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Light mace|light mace]]_ +3 (1d6) or 2 claws +2 (1d4)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +5 (1d8/19–20)
**Special Attacks** claws (2, 1d4, treated as magic, 7 rounds/day)
**_Sorcerer_ Spells Known **(CL 5th; concentration +9)
2nd (5/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Resist Energy|resist energy]]_
1st (7/day)—_[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **draconic (green)

### Tactics

**Before Combat **The _sorcerer_ casts _mage armor_ and _resist energy_ (fire).
**During Combat **The _sorcerer_ casts _mirror image_, then entangles opponents with his wand of _[[spells/Entangle|entangle]]_ (using the Use Magic Device skill). He uses one of his scrolls of _[[spells/Levitate|levitate]]_ to avoid melee combat, and casts _cause fear_ to remove opponents threatening him.
**Base Statistics **Without _mage armor_ and _resist energy_, the _sorcerer_’s statistics are **AC **14, touch 13, _flat-footed_ 11; Resist acid 5.

##### Statistics
**Str** 10, **Dex** 14, **Con** 12, **Int** 13, **Wis** 8, **Cha** 18
**Base Atk** +2; **CMB** +2; **CMD** 15
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Use Magic Device)
**Skills** Intimidate +10, Knowledge (arcana) +7, Perception +7, Spellcraft +7, Use Magic Device +13
**Languages** Common, Draconic, Elven
**SQ** bloodline arcana (acid spells deal +1 damage per die), elf blood
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Invisibility|invisibility]]_, scrolls of _levitate_ (2), scroll of _[[spells/Ray of Exhaustion|ray of exhaustion]]_, scroll of _[[spells/Silent Image|silent image]]_, wand of _entangle_ (20 charges), _[[items/Mundane/Smokestick|smokestick]]_; **Other Gear** masterwork _light crossbow_ with 10 bolts, masterwork _light mace_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 190 gp

The _[[npcs/Bramble Sorcerer|bramble sorcerer]]_ serves the interests of green dragons, walking where his masters cannot and speaking on their behalf to other forest dwellers.