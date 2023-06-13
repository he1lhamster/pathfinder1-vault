---
cssclass: [monsters]
title1: Battle Mage
title2: Battle Mage
CR: 2
sources:
- name: NPC Codex
  page: 179
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 600
race: Elf
classes:
- wizard 3
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 16
  touch: 12
  flat_footed: 14
  components:
    armor: 4
    dex: 2
HP:
  HP: 19
  long: 3d6+6
saves:
  fort: 2
  ref: 3
  will: 3
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk rapier +3 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: mwk rapier
      bonus:
      - 3
  ranged:
  - - text: mwk longbow +4 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: mwk longbow
      bonus:
      - 4
  special:
  - hand of the apprentice (6/day)
spells:
  entries:
  - name: mirror image
    source: Wizard
    level: 2
  - name: scorching ray
    source: Wizard
    level: 2
  - name: magic missile
    source: Wizard
    level: 1
  - name: shield
    source: Wizard
    level: 1
  - name: shocking grasp
    source: Wizard
    level: 1
  - name: daze
    source: Wizard
    level: 0
    DC: 13
  - name: detect magic
    source: Wizard
    level: 0
  - name: light
    source: Wizard
    level: 0
  - name: resistance
    source: Wizard
    level: 0
  sources:
  - name: Wizard
    type: prepared
    CL: 3
    concentration: 6
    slots:
      0: at-will
tactics:
  Before Combat: The wizard uses her wand to cast mage armor.
  During Combat: The wizard attacks with scorching ray, her longbow, and hand of the
    apprentice. If forced into melee, she casts mirror image and obscuring mist.
  Base Statistics: Without mage armor, the wizard's statistics are AC 12, touch 12,
    flat-footed 10.
ability_scores:
  STR: 12
  DEX: 15
  CON: 12
  INT: 17
  WIS: 10
  CHA: 8
BAB: 1
CMB: 2
CMD: 14
feats:
- name: Combat Casting
- name: Point-Blank Shot
- name: Scribe Scroll
skills:
  Acrobatics: 4
  Climb: 2
  Knowledge (arcana): 9
  Knowledge (history): 7
  Perception: 5
  Spellcraft: 9
    to identify magic item properties: 11
  Stealth: 4
languages:
- Common
- Draconic
- Elven
- Orc
- Sylvan
special_qualities:
- arcane bond (rapier)
- elven magic
- weapon familiarity
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of glitterdust
  - scroll of invisibility
  - scroll of magic weapon
  - scrolls of mirror image (2)
  - scroll of obscuring mist
  - scroll of protection from evil
  - scroll of scorching ray
  - wand of mage armor (20 charges)
  other:
  - masterwork longbow with 20 arrows
  - masterwork rapier
  - spellbook
  - 113 gp
desc_long: These mercenary wizards are able to fill many roles, and demand a high
  fee for their versatility.

---

# Battle Mage

**Source** NPC Codex pg. 179
**XP** 600
Elf _[[classes/Wizard|wizard]]_ 3

NE Medium humanoid (elf)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +2 Dex)
**hp** 19 (3d6+6)
**Fort** +2, **Ref** +3, **Will** +3; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +3 (1d6/18–20)
**Ranged** mwk _[[items/Weapon/Longbow|longbow]]_ +4 (1d8+1/×3)
**Special Attacks** hand of the apprentice (6/day)
**_Wizard_ Spells Prepared **(CL 3rd; concentration +6)
2nd—_[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_
1st—_[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, light, _[[universal monster rules/Resistance|resistance]]_

### Tactics

**Before Combat **The _wizard_ uses her wand to cast _[[spells/Mage Armor|mage armor]]_.
**During Combat **The _wizard_ attacks with _scorching ray_, her _longbow_, and hand of the apprentice. If forced into melee, she casts _mirror image_ and _[[spells/Obscuring Mist|obscuring mist]]_.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **12, touch 12, _flat-footed_ 10.

##### Statistics
**Str** 12, **Dex** 15, **Con** 12, **Int** 17, **Wis** 10, **Cha** 8
**Base Atk** +1; **CMB** +2; **CMD** 14
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Acrobatics +4, _[[universal monster rules/Climb|Climb]]_ +2, Knowledge (arcana) +9, Knowledge (history) +7, Perception +5, Spellcraft +9 (+11 to _[[spells/Identify|identify]]_ magic item properties), Stealth +4
**Languages** Common, Draconic, Elven, _[[monsters/Orc|Orc]]_, Sylvan
**SQ** arcane bond (_rapier_), elven magic, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _[[spells/Glitterdust|glitterdust]]_, scroll of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Magic Weapon|magic weapon]]_, scrolls of _mirror image_ (2), scroll of _obscuring mist_, scroll of _[[spells/Protection From Evil|protection from evil]]_, scroll of _scorching ray_, wand of _mage armor_ (20 charges); **Other Gear** masterwork _longbow_ with 20 arrows, masterwork _rapier_, _[[items/Mundane/Spellbook|spellbook]]_, 113 gp

These mercenary wizards are able to fill many roles, and _[[spells/Demand|demand]]_ a high fee for their versatility.