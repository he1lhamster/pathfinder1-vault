---
cssclass: [monsters]
title1: Mage Hunter
title2: Mage Hunter
CR: 18
sources:
- name: NPC Codex
  page: 142
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Human
classes:
- ranger 19
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 11
senses:
  darkvision: 60
AC:
  AC: 34
  touch: 19
  flat_footed: 28
  components:
    armor: 10
    deflection: 3
    dex: 5
    dodge: 1
    natural: 5
HP:
  HP: 195
  long: 19d10+86
saves:
  fort: 19
  ref: 24
  will: 14
defensive_abilities:
- improved evasion
- nondetection
immunities:
- electricity (120 points)
- fire (120 points)
- poison
resistances:
  cold: 30
  electricity: 30
  fire: 30
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 greataxe +21/+16/+11/+6 (1d12+2/×3)
      entries:
      - - damage: 1d12+2
          crit_multiplier: 3
      attack: +1 greataxe
      bonus:
      - 21
      - 16
      - 11
      - 6
  ranged:
  - - text: +1 frost longbow +27/+22/+17/+12 (1d8+1/19-20/×3 plus 1d6 cold)
      entries:
      - - damage: 1d8+1
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: cold
      attack: +1 frost longbow
      bonus:
      - 27
      - 22
      - 17
      - 12
  special:
  - favored enemy (elves +6, gnomes +2, humans +4, magical beasts +2)
spells:
  entries:
  - name: freedom of movement
    source: Ranger
    level: 4
  - name: nondetection
    source: Ranger
    level: 4
  - name: darkvision
    source: Ranger
    level: 3
  - name: neutralize poison
    source: Ranger
    level: 3
  - name: repel vermin
    source: Ranger
    level: 3
  - name: barkskin
    source: Ranger
    level: 2
  - name: bear's endurance
    source: Ranger
    level: 2
  - name: protection from energy
    source: Ranger
    level: 2
    count: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
    count: 3
  sources:
  - name: Ranger
    type: prepared
    CL: 16
    concentration: 18
tactics:
  Before Combat: The ranger casts barkskin, bear's endurance, darkvision, delay poison,
    freedom of movement, longstrider, nondetection, protection from energy (electricity,
    fire), and resist energy (cold, electricity, fire).
  During Combat: The ranger slays spellcasters with bane arrows. He rings his chime
    of interruption to hamper spellcasting.
  Base Statistics: Without barkskin, bear's endurance, darkvision, longstrider, nondetection,
    protection from energy, and resist energy, the ranger's statistics are Senses
    normal; hp 157; Fort +17; Defensive Abilities improved evasion; Immune none; Resist
    none; Speed 30 ft.; Con 14; Skills Acrobatics +22.
ability_scores:
  STR: 12
  DEX: 24
  CON: 18
  INT: 10
  WIS: 14
  CHA: 8
BAB: 19
CMB: 20
CMD: 41
feats:
- name: Critical Focus
- name: Deadly Aim
- name: Dodge
- name: Endurance
- name: Improved Critical (longbow)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Precise Shot
- name: Iron Will
- name: Lightning Reflexes
- name: Manyshot
- name: Point-Blank Shot
- name: Precise Shot
- name: Quick Draw
- name: Rapid Shot
- name: Staggering Critical
- name: Stunning Critical
skills:
  Acrobatics: 22
    when jumping: 26
  Climb: 14
  Handle Animal: 7
  Heal: 10
  Knowledge (arcana): 10
  Knowledge (local): 10
  Knowledge (dungeoneering): 8
  Knowledge (geography): 8
  Knowledge (history): 5
  Knowledge (nature): 7
  Linguistics: 1
  Perception: 24
  Ride: 14
  Spellcraft: 13
  Stealth: 29
  Survival: 15
  Swim: 9
languages:
- Common
- Draconic
special_qualities:
- camouflage
- favored terrain (forest +4, plains +2, underground +2, urban +6)
- hide in plain sight
- hunter's bond (companions)
- improved quarry
- swift tracker
- track +9
- wild empathy +18
- woodland stride
gear:
  combat:
  - +1 elf-bane arrows (5)
  - +1 flaming arrows (5)
  - +1 gnome-bane arrows (5)
  - +1 human-bane arrows (10)
  - +1 shock arrows (5)
  - chime of interruption
  - potions of invisibility (2)
  - wand of cure serious wounds (20 charges)
  other:
  - +4 mithral breastplate
  - +1 frost longbow with 20 arrows
  - +1 greataxe
  - bag of holding (type I)
  - belt of incredible dexterity +4
  - cloak of resistance +4
  - ring of protection +3
  - diamond dust for nondetection (worth 50 gp)
  - 2,574 gp
desc_long: A mage hunter thrills at killing sorcerers and wizards. Knowing how to
  circumvent their hated spells, he casts nondetection every day to deter pursuit
  and scrying.

---

# Mage Hunter

**Source** NPC Codex pg. 142
**XP** 153,600
Human _[[classes/Ranger|ranger]]_ 19
CE Medium humanoid (human)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +24

##### Defense

**AC** 34, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+10 armor, +3 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 195 (19d10+86)
**Fort** +19, **Ref** +24, **Will** +14
**Defensive Abilities** improved evasion, _[[spells/Nondetection|nondetection]]_; **Immune** electricity (120 points), fire (120 points), poison; **Resist** cold 30, electricity 30, fire 30

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Greataxe|greataxe]]_ +21/+16/+11/+6 (1d12+2/×3)
**Ranged** +1 frost _[[items/Weapon/Longbow|longbow]]_ +27/+22/+17/+12 (1d8+1/19–20/×3 plus 1d6 cold)
**Special Attacks** favored enemy (elves +6, gnomes +2, humans +4, magical beasts +2)
**_Ranger_ Spells Prepared **(CL 16th; concentration +18)
4th—_[[spells/Freedom of Movement|freedom of movement]]_, _nondetection_
3rd—_darkvision_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Repel Vermin|repel vermin]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Protection from Energy|protection from energy]]_ (2)
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_ (3)

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, bear’s _endurance_, _darkvision_, _delay poison_, _freedom of movement_, _longstrider_, _nondetection_, _protection from energy_ (electricity, fire), and _resist energy_ (cold, electricity, fire).
**During Combat **The _ranger_ slays spellcasters with _[[spells/Bane|bane]]_ arrows. He rings his _[[items/Wondrous Item/Chime of Interruption|chime of interruption]]_ to hamper spellcasting.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _darkvision_, _longstrider_, _nondetection_, _protection from energy_, and _resist energy_, the _ranger_’s statistics are **Senses **normal; **hp **157; **Fort **+17; **Defensive Abilities **improved evasion; **Immune **none; **Resist **none; **Speed **30 ft.; **Con **14; **Skills **Acrobatics +22.

##### Statistics
**Str** 12, **Dex** 24, **Con** 18, **Int** 10, **Wis** 14, **Cha** 8
**Base Atk** +19; **CMB** +20; **CMD** 41
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _Endurance_, _[[feats/Improved Critical|Improved Critical]]_ (_longbow_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** Acrobatics +22 (+26 when jumping), _[[universal monster rules/Climb|Climb]]_ +14, Handle Animal +7, _[[spells/Heal|Heal]]_ +10, Knowledge (arcana, local) +10, Knowledge (dungeoneering, geography) +8, Knowledge (history) +5, Knowledge (nature) +7, Linguistics +1, Perception +24, Ride +14, Spellcraft +13, Stealth +29, Survival +15, Swim +9
**Languages** Common, Draconic
**SQ** camouflage, favored terrain (forest +4, plains +2, underground +2, urban +6), hide in plain sight, _[[classes/Hunter|hunter]]_’s bond (companions), improved quarry, swift tracker, track +9, wild _[[feats/Empathy|empathy]]_ +18, woodland stride
**Combat Gear** +1 elf-bane arrows (5), +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ arrows (5), +1 gnome-bane arrows (5), +1 human-bane arrows (10), +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ arrows (5), _chime of interruption_, potions of _[[spells/Invisibility|invisibility]]_ (2), wand of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (20 charges); **Other Gear** +4 mithral _[[items/Armor/Breastplate|breastplate]]_, +1 frost _longbow_ with 20 arrows, +1 _greataxe_, bag of holding (type I), _[[items/Wondrous Item/Belt of Incredible Dexterity +4|belt of incredible dexterity +4]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, diamond dust for _nondetection_ (worth 50 gp), 2,574 gp

A _[[npcs/Mage Hunter|mage hunter]]_ thrills at killing sorcerers and wizards. Knowing how to circumvent their hated spells, he casts _nondetection_ every day to deter pursuit and _[[spells/Scrying|scrying]]_.