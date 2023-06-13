---
cssclass: [monsters]
title1: Goblin, Goblin Stickylord
title2: Goblin Stickylord
CR: 6
sources:
- name: Monster Codex
  page: 111
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Goblin
classes:
- alchemist 7 (Pathfinder RPG Advanced Player's Guide 26)
alignment: NE
size: Small
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 17
  flat_footed: 18
  components:
    armor: 5
    dex: 6
    natural: 2
    size: 1
HP:
  HP: 49
  long: 7d8+14
saves:
  fort: 7
  ref: 12
  will: 3
  other: +2 vs. fire, +4 vs. poison
resistances:
  fire: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: heavy mace +4 (1d6-2)
      entries:
      - - damage: 1d6-2
      attack: heavy mace
      bonus:
      - 4
  ranged:
  - - text: light crossbow +12 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 12
  special:
  - bomb 10/day (4d6+3 fire, DC 16)
spells:
  entries:
  - name: heroism
    source: Alchemist
    level: 3
  - superscripts:
    - UC
    name: resinous skin
    source: Alchemist
    level: 3
    DC: 16
  - superscripts:
    - APG
    name: alchemical allocation
    source: Alchemist
    level: 2
    count: 2
  - name: barkskin
    source: Alchemist
    level: 2
  - name: see invisibility
    source: Alchemist
    level: 2
  - name: disguise self
    source: Alchemist
    level: 1
  - name: expeditious retreat
    source: Alchemist
    level: 1
  - name: reduce person
    source: Alchemist
    level: 1
    DC: 14
  - name: shield
    source: Alchemist
    level: 1
  - superscripts:
    - UC
    name: targeted bomb admixture
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 7
tactics:
  During Combat: The goblin patiently quaffs his mutagen, casts buff spells on himself,
    and then proceeds to bomb his enemies.
ability_scores:
  STR: 6
  DEX: 22
  CON: 13
  INT: 16
  WIS: 10
  CHA: 8
BAB: 5
CMB: 2
CMD: 18
feats:
- name: Brew Potion
- superscripts:
  - ARG
  name: Fire Tamer
- superscripts:
  - ARG
  name: Flame Heart
- name: Point-Blank Shot
- name: Precise Shot
- name: Throw Anything
skills:
  Craft (alchemy): 13
  Disable Device: 16
  Heal: 4
  Intimidate: 6
    vs. goblins: 8
  Knowledge (arcana): 7
  Knowledge (nature): 7
  Perception: 10
  Ride: 10
  Sleight of Hand: 11
  Spellcraft: 11
  Stealth: 21
  Survival: 4
  Use Magic Device: 5
languages:
- Aklo
- Aquan
- Goblin
- Undercommon
special_qualities:
- alchemy (alchemy crafting +7, identify potions)
- discoveries (precise bombs [3 squares], tanglefoot bomb, wings)
- mutagen (+4/-2, +2 natural, 70 minutes)
- poison use
- swift alchemy
- swift poisoning
gear:
  combat:
  - potion of fly
  - potion of fox's cunning
  - potion of invisibility
  - wand of freedom of movement (2 charges)
  - tanglefoot bags (8)
  other:
  - +1 mithral chain shirt
  - heavy mace
  - light crossbow with 20 bolts
  - cloak of resistance +1
  - universal solvent (2)
  - 11 gp
ecology:
  environment: temperate forest and plains (usually coastal regions)
desc_long: |-
  Goblin stickylords are a decidedly bizarre breed of goblin alchemists. Unlike normal goblin alchemists, who focus on spreading around as much fire and flame as possible, stickylords have learned the value of locking enemies in place and then burning them.

   In order to make their gluey concoctions, goblin stickylords explore every aspect of adhesion, combining mundane materials like glue, pitch, and less pleasant substances with magic. These unique reagents are often harvested by lesser goblin minions-the better to keep the powerful stickylord from getting covered in bee stings or drowning in mud. (Sadly for these minions, stickylords need test subjects, so even faithful service is no guarantee that they won't be stuck to a stump in order for a stickylord to try out a new formula-or practice aiming.)

   On the battlefield, stickylords use their tanglefoot bomb discovery to stick enemies to the ground while the bomb's clinging fire does its job. Many command lesser alchemists or teams of pyromaniacs armed with fire arrows and alchemist's fire, who are ready to lob their projectiles once the stickylord can get the enemy to stop moving around.

   Despite their obsession, goblin stickylords are careful to always carry powerful solvents, as even the best of them wind up glued in place on occasion.

---

# Goblin, Goblin Stickylord

**Source** Monster Codex pg. 111
**XP** 2,400
_[[monsters/Goblin|Goblin]]_ _[[classes/Alchemist|alchemist]]_ 7 (Pathfinder RPG Advanced Player’s Guide 26)

NE Small humanoid (goblinoid)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 24, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 armor, +6 Dex, +2 natural, +1 size)
**hp** 49 (7d8+14)
**Fort** +7, **Ref** +12, **Will** +3; +2 vs. fire, +4 vs. poison
**Resist** fire 5

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Heavy mace|heavy mace]]_ +4 (1d6–2)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +12 (1d6/19–20)
**Special Attacks** bomb 10/day (4d6+3 fire, DC 16)
**_Alchemist_ Extracts Prepared **(CL 7th)
3rd—_[[spells/Heroism|heroism]]_, _[[spells/Resinous Skin|resinous skin]]_ (DC 16)
2nd—_[[spells/Alchemical Allocation|alchemical allocation]]_ (2), _[[spells/Barkskin|barkskin]]_, _[[spells/See Invisibility|see invisibility]]_
1st—_[[spells/Disguise Self|disguise self]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Reduce Person|reduce person]]_ (DC 14), _[[spells/Shield|shield]]_, _[[spells/Targeted Bomb Admixture|targeted bomb admixture]]_

### Tactics

**During Combat** The _goblin_ patiently quaffs his mutagen, casts buff spells on himself, and then proceeds to bomb his enemies.

##### Statistics
**Str** 6, **Dex** 22, **Con** 13, **Int** 16, **Wis** 10, **Cha** 8
**Base Atk** +5; **CMB** +2; **CMD** 18
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Fire Tamer|Fire Tamer]]_, _[[feats/Flame Heart|Flame Heart]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Craft (alchemy) +13, Disable Device +16, _[[spells/Heal|Heal]]_ +4, Intimidate +6 (+8 vs. goblins), Knowledge (arcana, nature) +7, Perception +10, Ride +10, Sleight of Hand +11, Spellcraft +11, Stealth +21, Survival +4, Use Magic Device +5
**Languages** Aklo, Aquan, _Goblin_, Undercommon
**SQ** alchemy (alchemy crafting +7, _[[spells/Identify|identify]]_ potions), discoveries (precise bombs [3 squares], tanglefoot bomb, wings), mutagen (+4/–2, +2 natural, 70 minutes), poison use, swift alchemy, swift _[[items/Armor Magic Abilities/Poisoning|poisoning]]_
**Combat Gear** potion of fly, potion of fox’s _[[items/Weapon Magic Abilities/Cunning|cunning]]_, potion of _[[spells/Invisibility|invisibility]]_, wand of _[[spells/Freedom of Movement|freedom of movement]]_ (2 charges), tanglefoot bags (8); **Other Gear** +1 mithral _[[items/Armor/Chain shirt|chain shirt]]_, _heavy mace_, _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Universal Solvent|universal solvent]]_ (2), 11 gp

##### Ecology

**Environment** temperate forest and plains (usually coastal regions)

##### Description

_Goblin_ stickylords are a decidedly bizarre breed of _goblin_ alchemists. Unlike normal _goblin_ alchemists, who focus on spreading around as much fire and flame as possible, stickylords have learned the value of locking enemies in place and then _[[items/Weapon Magic Abilities/Burning|burning]]_ them.

In order to make their gluey concoctions, _goblin_ stickylords explore every aspect of adhesion, combining mundane materials like glue, pitch, and less pleasant substances with magic. These unique reagents are often harvested by lesser _goblin_ minions—the better to keep the powerful stickylord from getting covered in bee stings or drowning in mud. (Sadly for these minions, stickylords need test subjects, so even faithful service is no guarantee that they won’t be stuck to a stump in order for a stickylord to try out a new formula—or practice aiming.)

On the battlefield, stickylords use their tanglefoot bomb discovery to stick enemies to the ground while the bomb’s clinging fire does its job. Many _[[spells/Command|command]]_ lesser alchemists or teams of pyromaniacs armed with fire arrows and _alchemist_’s fire, who are ready to lob their projectiles once the stickylord can get the enemy to stop moving around.

Despite their obsession, _goblin_ stickylords are careful to always carry powerful solvents, as even the best of them wind up glued in place on occasion.