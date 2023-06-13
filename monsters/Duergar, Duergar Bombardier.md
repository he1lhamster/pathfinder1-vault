---
cssclass: [monsters]
title1: Duergar, Duergar Bombardier
title2: Duergar Bombardier
CR: 1
sources:
- name: Monster Codex
  page: 48
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 400
race: Duergar
classes:
- alchemist 2 (Pathfinder RPG Advanced Player's Guide 26)
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 4
senses:
  darkvision: 120
AC:
  AC: 22
  touch: 14
  flat_footed: 18
  components:
    armor: 2
    dex: 4
    natural: 6
HP:
  HP: 18
  long: 2d8+6
saves:
  fort: 5
  ref: 7
  will: 0
  other: +2 vs. spells
immunities:
- paralysis
- phantasms
- poison
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: light mace +2 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: light mace
      bonus:
      - 2
  ranged:
  - - text: bomb +6 (1d6+2 acid or fire)
      entries:
      - - damage: 1d6+2
          type: acid or fire
      attack: bomb
      bonus:
      - 6
  - - text: light crossbow +3 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 3
  special:
  - bomb 6/day (1d6+2 acid or fire, DC 13)
spell_like_abilities:
  entries:
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  - name: ironskin
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 2
    concentration: -1
spells:
  entries:
  - superscripts:
    - APG
    name: bomber's eye
    source: Alchemist
    level: 1
  - name: shield
    source: Alchemist
    level: 1
  - name: true strike
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 2
tactics:
  Before Combat: The bombardier quaffs a Dexterity mutagen and casts ironskin.
  During Combat: The bombardier spends most of the combat lobbing bombs or alchemist's
    fire at her foes, using invisibility and potions of longstrider to gain superior
    tactical positions or make a hasty retreat.
  Base Statistics: When she's not under the effect of her mutagen and ironskin, the
    bombardier's statistics are Init +2; AC 14, touch 12, flat-footed 12; Ref +5,
    Will +1; Ranged bomb +4 (1d6+2 fire) or light crossbow +3 (1d8/19-20); Dex 14,
    Wis 12; CMD 14 (18 vs. bull rush, 18 vs. trip); Skills Heal +6, Disable Device
    +7, Perception +6, Survival +6.
ability_scores:
  STR: 12
  DEX: 16
  CON: 15
  INT: 15
  WIS: 10
  CHA: 4
BAB: 1
CMB: 2
CMD: 16
CMD_other: 20 vs. bull rush or trip
feats:
- name: Brew Potion
- superscripts:
  - APG
  name: Extra Bombs
- name: Throw Anything
skills:
  Craft (alchemy): 7
  Disable Device: 8
  Heal: 4
  Knowledge (arcana): 7
  Perception: 6
  Survival: 4
languages:
- Aklo
- Common
- Draconic
- Dwarven
- Undercommon
special_qualities:
- alchemy (alchemy crafting +2, identify potions)
- discovery (acid bomb)
- ironskinned
- mutagen (+4/-2, +2 natural, 20 minutes)
- poison use
- slow and steady
- stability
gear:
  combat:
  - potions of cure light wounds (2)
  - potions of detect secret doors (2)
  - potions of expeditious retreat (2)
  - potions of negate aroma (2)
  - acid (6)
  - alchemist's fire (6)
  - smokesticks (6)
  - tanglefoot bags (6)
  - thunderstones (6)
  other:
  - leather armor
  - light crossbow with 10 bolts
  - light mace
  - dust of tracelessness
  - tindertwigs (6)
  - formula book
  - 2 gp
ecology:
  environment: any underground
desc_long: |-
  A duergar bombardier spends her days fiddling with reagents and bizarre ingredients that she either finds deep underground or purchases from scouts who have brought them back from the surface or distant caverns. Essential ingredients, especially plants, can be hard to find, and a bombardier must work for money or favors if she's to continue practicing her craft.

   Though the military and slavers are loath to employ these unpredictable duergar, bombardiers can be very effective when subtlety is not required. Though most bombardiers wouldn't hurt their own kind-the bonds of kin and law are too strong-they often inadvertently kill potential slaves instead of capturing them.

---

# Duergar, Duergar Bombardier

**Source** Monster Codex pg. 48
**XP** 400
_[[monsters/Duergar|Duergar]]_ _[[classes/Alchemist|alchemist]]_ 2 (Pathfinder RPG Advanced Player’s Guide 26)

LE Medium humanoid (dwarf)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +6

##### Defense

**AC** 22, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 armor, +4 Dex, +6 natural)
**hp** 18 (2d8+6)
**Fort** +5, **Ref** +7, **Will** +0; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Light mace|light mace]]_ +2 (1d6+1)
**Ranged** bomb +6 (1d6+2 acid or fire) or _[[items/Weapon/Light crossbow|light crossbow]]_ +3 (1d8/19–20)
**Special Attacks** bomb 6/day (1d6+2 acid or fire, DC 13)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration –1)
1/day—_[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Ironskin|ironskin]]_
**_Alchemist_ Extracts Prepared **(CL 2nd)
1st—bomber’s eye, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_

### Tactics

**Before Combat** The bombardier quaffs a Dexterity mutagen and casts _ironskin_.
 **During Combat** The bombardier spends most of the combat lobbing bombs or _alchemist_’s fire at her foes, using _invisibility_ and potions of _[[spells/Longstrider|longstrider]]_ to gain superior tactical positions or make a hasty retreat.
 **Base Statistics** When she’s not under the effect of her mutagen and _ironskin_, the bombardier’s statistics are **Init **+2; **AC **14, touch 12, _flat-footed_ 12; **Ref **+5, **Will **+1; **Ranged **bomb +4 (1d6+2 fire) or _light crossbow_ +3 (1d8/19–20); **Dex **14, **Wis **12; **CMD **14 (18 vs. bull rush, 18 vs. _[[universal monster rules/Trip|trip]]_); **Skills **_[[spells/Heal|Heal]]_ +6, Disable Device +7, Perception +6, Survival +6.

##### Statistics
**Str** 12, **Dex** 16, **Con** 15, **Int** 15, **Wis** 10, **Cha** 4
**Base Atk** +1; **CMB** +2; **CMD** 16 (20 vs. bull rush or _trip_)
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Extra Bombs|Extra Bombs]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Craft (alchemy) +7, Disable Device +8, _Heal_ +4, Knowledge (arcana) +7, Perception +6, Survival +4
**Languages** Aklo, Common, Draconic, Dwarven, Undercommon
**SQ** alchemy (alchemy crafting +2, _[[spells/Identify|identify]]_ potions), discovery (acid bomb), ironskinned, mutagen (+4/–2, +2 natural, 20 minutes), poison use, _[[spells/Slow|slow]]_ and steady, stability
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), potions of _[[spells/Detect Secret Doors|detect secret doors]]_ (2), potions of _[[spells/Expeditious Retreat|expeditious retreat]]_ (2), potions of _[[spells/Negate Aroma|negate aroma]]_ (2), acid (6), _alchemist_’s fire (6), smokesticks (6), tanglefoot bags (6), thunderstones (6); **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, _light crossbow_ with 10 bolts, _light mace_, _[[items/Wondrous Item/Dust of Tracelessness|dust of tracelessness]]_, tindertwigs (6), _[[items/Mundane/Formula book|formula book]]_, 2 gp

##### Ecology

**Environment** any underground

##### Description

A _duergar_ bombardier spends her days fiddling with reagents and bizarre ingredients that she either finds deep underground or purchases from scouts who have brought them back from the surface or distant caverns. Essential ingredients, especially plants, can be hard to find, and a bombardier must work for money or favors if she’s to continue practicing her craft.

Though the military and slavers are loath to employ these unpredictable _duergar_, bombardiers can be very effective when subtlety is not required. Though most bombardiers wouldn’t hurt their own kind—the bonds of kin and law are too strong—they often inadvertently kill potential slaves instead of capturing them.