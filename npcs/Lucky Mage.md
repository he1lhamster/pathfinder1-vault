---
cssclass: [monsters]
title1: Lucky Mage
title2: Lucky Mage
CR: 10
sources:
- name: NPC Codex
  page: 168
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Halfling
classes:
- sorcerer 11
alignment: N
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 3
AC:
  AC: 21
  touch: 16
  flat_footed: 17
  components:
    armor: 4
    deflection: 1
    dex: 3
    dodge: 1
    natural: 1
    size: 1
HP:
  HP: 63
  long: 11d6+22
saves:
  fort: 9
  ref: 11
  will: 10
  other: +2 vs. fear
defensive_abilities:
- fated +3
immunities:
- fire (120 points)
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk longspear +5 (1d6-2/×3)
      entries:
      - - damage: 1d6-2
          crit_multiplier: 3
      attack: mwk longspear
      bonus:
      - 5
  ranged:
  - - text: mwk light crossbow +10 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 10
  special:
  - it was meant to be (1/day)
spell_like_abilities:
  entries:
  - name: touch of destiny
    source: default
    freq: 8/day
    other: '+5'
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - name: break enchantment
    source: Sorcerer
    level: 5
  - name: interposing hand
    source: Sorcerer
    level: 5
  - name: teleport
    source: Sorcerer
    level: 5
  - name: bestow curse
    source: Sorcerer
    level: 4
    DC: 19
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: freedom of movement
    source: Sorcerer
    level: 4
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 18
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 18
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 18
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 17
  - name: blur
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: spider climb
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 16
  - name: floating disk
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
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
  - name: prestidigitation
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
    CL: 11
    concentration: 16
    slots:
      5: 5
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: destined
tactics:
  Before Combat: The sorcerer casts freedom of movement, mage armor, and protection
    from energy (fire).
  During Combat: The sorcerer uses interposing hand or hold person to keep opponents
    from reaching her while she uses ranged attack spells such as fireball and ray
    of exhaustion.
  Base Statistics: Without mage armor and protection from energy, the sorcerer's statistics
    are AC 17, touch 16, flat-footed 13; Immune none.
ability_scores:
  STR: 6
  DEX: 16
  CON: 12
  INT: 13
  WIS: 10
  CHA: 21
BAB: 5
CMB: 2
CMD: 23
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Defensive Combat Training
- name: Dodge
- name: Eschew Materials
- name: Great Fortitude
- name: Lightning Reflexes
- name: Mobility
skills:
  Acrobatics: 5
    when jumping: 1
  Bluff: 13
  Climb: 0
  Fly: 9
  Knowledge (arcana): 9
  Knowledge (history): 9
  Perception: 13
  Spellcraft: 10
languages:
- Common
- Gnome
- Halfling
special_qualities:
- bloodline arcana (gains a luck bonus to saves when casting personal-range spells)
gear:
  combat:
  - potion of cure moderate wounds
  - potion of cure serious wounds
  - potion of eagle's splendor
  - potion of fly
  - potion of invisibility
  - wand of shield (44 charges)
  other:
  - masterwork light crossbow with 10 bolts
  - masterwork longspear
  - amulet of natural armor +1
  - cloak of resistance +2
  - headband of alluring charisma +2
  - ring of protection +1
  - 649 gp
desc_long: The lucky mage uses her magic, innate talents and good fortune to survive
  incredible odds with barely a scratch. Rather than depend on this strange fortune,
  however, the lucky mage constantly strives to understand and harness her unique
  abilities.

---

# Lucky Mage

**Source** NPC Codex pg. 168
**XP** 9,600
Halfling _[[classes/Sorcerer|sorcerer]]_ 11

N Small humanoid (halfling)
**Init** +3; **Senses** Perception +13

##### Defense

**AC** 21, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +1 deflection, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural, +1 size)
**hp** 63 (11d6+22)
**Fort** +9, **Ref** +11, **Will** +10; +2 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** fated +3; **Immune** fire (120 points)

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Longspear|longspear]]_ +5 (1d6–2/×3)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +10 (1d6/19–20)
**Special Attacks** it was meant to be (1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
8/day—touch of destiny (+5)
**_Sorcerer_ Spells Known **(CL 11th; concentration +16)
5th (5/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Interposing Hand|interposing hand]]_, teleport
4th (7/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Invisibility|invisibility]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18)
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, blindness/deafness (DC 17), _[[spells/Blur|blur]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Spider Climb|spider climb]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Floating Disk|floating disk]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline** destined

### Tactics

**Before Combat **The _sorcerer_ casts _freedom of movement_, _mage armor_, and _protection from energy_ (fire).
**During Combat **The _sorcerer_ uses _interposing hand_ or _hold person_ to keep opponents from reaching her while she uses ranged attack spells such as _fireball_ and _ray of exhaustion_.
**Base Statistics **Without _mage armor_ and _protection from energy_, the _sorcerer_’s statistics are **AC **17, touch 16, _flat-footed_ 13; **Immune **none.

##### Statistics
**Str** 6, **Dex** 16, **Con** 12, **Int** 13, **Wis** 10, **Cha** 21
**Base Atk** +5; **CMB** +2; **CMD** 23
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_
**Skills** Acrobatics +5 (+1 when jumping), Bluff +13, _[[universal monster rules/Climb|Climb]]_ +0, Fly +9, Knowledge (arcana, history) +9, Perception +13, Spellcraft +10
**Languages** Common, Gnome, Halfling
**SQ** bloodline arcana (gains a luck bonus to saves when casting personal-range spells)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _[[monsters/Eagle|eagle]]_’s splendor, potion of fly, potion of _invisibility_, wand of _[[spells/Shield|shield]]_ (44 charges); **Other Gear** masterwork _light crossbow_ with 10 bolts, masterwork _longspear_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 649 gp

The _[[npcs/Lucky Mage|lucky mage]]_ uses her magic, innate talents and good fortune to survive incredible odds with barely a scratch. Rather than depend on this strange fortune, however, the _lucky mage_ constantly strives to understand and harness her unique abilities.