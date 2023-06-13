---
cssclass: [monsters]
title1: Drow, Drow Poisoner
title2: Drow Poisoner
CR: 11
sources:
- name: Monster Codex
  page: 38
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 12800
race: Drow
classes:
- alchemist 12 (Pathfinder RPG Advanced Player's Guide 26)
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 14
senses:
  all-around vision: true
  darkvision: 120
AC:
  AC: 23
  touch: 16
  flat_footed: 18
  components:
    armor: 6
    deflection: 1
    dex: 5
    natural: 1
HP:
  HP: 81
  long: 12d8+24
saves:
  fort: 10
  ref: 14
  will: 5
  other: +2 vs. enchantment
immunities:
- sleep
- poison
SR: 18
weaknesses:
- light blindness
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk rapier +10/+5 (1d6/18-20 plus poison)
      entries:
      - - damage: 1d6
          crit_range: 18-20
        - effect: poison
      attack: mwk rapier
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk hand crossbow +15 (1d4/19-20 plus poison)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: poison
      attack: mwk hand crossbow
      bonus:
      - 15
  - - text: bomb +14/+9 (6d6+5 fire)
      entries:
      - - damage: 6d6+5
          type: fire
      attack: bomb
      bonus:
      - 14
      - 9
  special:
  - bomb 19/day (6d6+5 fire and catch fire, DC 21, 10-ft. radius)
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: darkness
    source: default
    freq: 1/day
  - name: faerie fire
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 12
spells:
  entries:
  - name: cure critical wounds
    source: Alchemist
    level: 4
  - superscripts:
    - APG
    name: fluid form
    source: Alchemist
    level: 4
  - superscripts:
    - UM
    name: greater false life
    source: Alchemist
    level: 4
  - name: greater invisibility
    source: Alchemist
    level: 4
  - superscripts:
    - UM
    name: countless eyes
    source: Alchemist
    level: 3
  - name: displacement
    source: Alchemist
    level: 3
  - superscripts:
    - UM
    name: eruptive pustules
    source: Alchemist
    level: 3
    DC: 18
  - name: haste
    source: Alchemist
    level: 3
  - name: protection from energy
    source: Alchemist
    level: 3
  - superscripts:
    - APG
    name: alchemical allocation
    source: Alchemist
    level: 2
  - name: resist energy
    source: Alchemist
    level: 2
    count: 2
  - name: see invisibility
    source: Alchemist
    level: 2
  - superscripts:
    - UC
    name: touch injection
    source: Alchemist
    level: 2
  - superscripts:
    - APG
    name: vomit swarm
    source: Alchemist
    level: 2
  - superscripts:
    - UM
    name: anticipate peril
    source: Alchemist
    level: 1
    DC: 16
  - superscripts:
    - APG
    name: bomber's eye
    source: Alchemist
    level: 1
  - name: negate aroma
    source: Alchemist
    level: 1
  - superscripts:
    - UM
    name: polypurpose panacea
    source: Alchemist
    level: 1
    DC: 16
  - name: shield
    source: Alchemist
    level: 1
  - name: true strike
    source: Alchemist
    level: 1
    count: 2
  sources:
  - name: Alchemist
    type: prepared
    CL: 12
tactics:
  Before Combat: The poisoner drinks her Dexterity mutagen and her extracts of anticipate
    peril, countless eyes, and greater invisibility.
  Base Statistics: Without the Dexterity mutagen, anticipate peril, and countless
    eyes, the drow's statistics are Init +7; Senses no all-around vision; AC 21, touch
    14, flat-footed 18; Ref +12, Will +6; Ranged mwk hand crossbow +13 (1d4/19-20
    plus poison), or bomb +12/+7 (6d6+5 fire); Dex 17, Wis 12; CMD 23; Skills Disable
    Device +17, Fly +11, Heal +10, Perception +18, Stealth +14, Survival +10.
ability_scores:
  STR: 10
  DEX: 21
  CON: 12
  INT: 20
  WIS: 10
  CHA: 10
BAB: 9
CMB: 9
CMD: 25
feats:
- name: Brew Potion
- name: Extra Bombs
- name: Improved Initiative
- name: Point-Blank Shot
- name: Precise Shot
- name: Quick Draw
- name: Rapid Shot
- name: Throw Anything
skills:
  Craft (alchemy): 20
  Disable Device: 19
  Fly: 13
  Heal: 9
  Knowledge (arcana): 20
  Knowledge (nature): 14
  Perception: 17
  Spellcraft: 20
  Stealth: 16
  Survival: 9
  Use Magic Device: 15
languages:
- Elven
- Undercommon
special_qualities:
- alchemy (alchemy crafting +12, identify potions)
- discoveries (explosive bomb, fast bombs, poison bomb [12 rounds/level], smoke bomb,
  strafe bomb, wings)
- mutagen (+4/-2, +2 natural, 120 minutes)
- poison use
- swift alchemy
- swift poisoning
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of gaseous form
  - potion of ghostly disguise
  - potion of invisibility
  - deathblade
  - dragon bile
  - drow poison (4)
  - purple worm poison
  other:
  - +2 chain shirt
  - mwk hand crossbow with 20 bolts
  - mwk rapier
  - amulet of natural armor +1
  - belt of incredible dexterity +2
  - cloak of resistance +1
  - headband of vast intelligence +2
  - ring of protection +1
  - 170 gp
ecology:
  environment: underground
desc_long: This drow makes use of deadly venoms and alchemy.

---

# Drow, Drow Poisoner

**Source** Monster Codex pg. 38
**XP** 12,800
_[[monsters/Drow|Drow]]_ _[[classes/Alchemist|alchemist]]_ 12 (Pathfinder RPG Advanced Player's Guide 26)
CE Medium humanoid (elf)
**Init** +14; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +17

##### Defense

**AC** 23, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +5 Dex, +1 natural)
**hp** 81 (12d8+24)
**Fort** +10, **Ref** +14, **Will** +5; +2 vs. enchantment
**Immune** sleep, poison; **SR** 18
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +10/+5 (1d6/18–20 plus poison)
**Ranged** mwk _[[items/Weapon/Hand crossbow|hand crossbow]]_ +15 (1d4/19–20 plus poison) or bomb +14/+9 (6d6+5 fire)
**Special Attacks** bomb 19/day (6d6+5 fire and catch fire, DC 21, 10-ft. radius)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +12)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Darkness|darkness]]_, _[[spells/Faerie Fire|faerie fire]]_
**_Alchemist_ Extracts Prepared**(CL 12th)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Fluid Form|fluid form]]_, greater _[[spells/False Life, Greater|false life, greater]]_ _[[spells/Invisibility|invisibility]]_
3rd—_[[spells/Countless Eyes|countless eyes]]_, _[[spells/Displacement|displacement]]_, _[[spells/Eruptive Pustules|eruptive pustules]]_ (DC 18), _[[spells/Haste|haste]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Alchemical Allocation|alchemical allocation]]_, _[[spells/Resist Energy|resist energy]]_ (2), _[[spells/See Invisibility|see invisibility]]_, _[[spells/Touch Injection|touch injection]]_, _[[spells/Vomit Swarm|vomit swarm]]_
1st—_[[spells/Anticipate Peril|anticipate peril]]_ (DC 16), bomber’s eye, _[[spells/Negate Aroma|negate aroma]]_, _[[spells/Polypurpose Panacea|polypurpose panacea]]_ (DC 16), _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_ (2)

### Tactics

**Before Combat** The poisoner drinks her Dexterity mutagen and her extracts of _anticipate peril_, _countless eyes_, and greater _invisibility_.
 **Base Statistics** Without the Dexterity mutagen, _anticipate peril_, and _countless eyes_, the _drow_’s statistics are **Init** +7; **Senses** no _all-around vision_; **AC** 21, touch 14, _flat-footed_ 18; Ref +12, Will +6; **Ranged** mwk _hand crossbow_ +13 (1d4/19–20 plus poison), or bomb +12/+7 (6d6+5 fire); **Dex** 17, **Wis** 12; **CMD** 23; **Skills** Disable Device +17, Fly +11, _[[spells/Heal|Heal]]_ +10, Perception +18, Stealth +14, Survival +10.

##### Statistics
**Str** 10, **Dex** 21, **Con** 12, **Int** 20, **Wis** 10, **Cha** 10
**Base Atk** +9; **CMB** +9; **CMD** 25
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Extra Bombs|Extra Bombs]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Craft (alchemy) +20, Disable Device +19, Fly +13, _Heal_ +9, Knowledge (arcana) +20, Knowledge (nature) +14, Perception +17, Spellcraft +20, Stealth +16, Survival +9, Use Magic Device +15
**Languages** Elven, Undercommon
**SQ** alchemy (alchemy crafting +12, _[[spells/Identify|identify]]_ potions), discoveries (explosive bomb, fast bombs, poison bomb [12 rounds/level], _[[items/Mundane/Smoke Bomb|smoke bomb]]_, strafe bomb, wings), mutagen (+4/–2, +2 natural, 120 minutes), poison use, swift alchemy, swift _[[items/Armor Magic Abilities/Poisoning|poisoning]]_
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _[[spells/Gaseous Form|gaseous form]]_, potion of _[[spells/Ghostly Disguise|ghostly disguise]]_, potion of _invisibility_, _[[poisons/Deathblade|deathblade]]_, _[[poisons/Dragon bile|dragon bile]]_, _[[poisons/Drow poison|drow poison]]_ (4), _[[poisons/Purple Worm Poison|purple worm poison]]_; **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, mwk _hand crossbow_ with 20 bolts, mwk _rapier_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 170 gp

##### Ecology

**Environment** underground

##### Description

This _drow_ makes use of _[[items/Weapon Magic Abilities/Deadly|deadly]]_ venoms and alchemy.