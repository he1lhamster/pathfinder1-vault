---
cssclass: [monsters]
title1: War Priest
title2: War Priest
CR: 1
sources:
- name: NPC Codex
  page: 44
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 400
race: Dwarf
classes:
- cleric of Gorum 2
alignment: CE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  other: +4 dodge vs. giants
  components:
    armor: 5
HP:
  HP: 21
  long: 2d8+9
saves:
  fort: 5
  ref: 0
  will: 6
  other: +2 vs. poison, spells, and spell-like abilities
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk greatsword with magic weapon +4 (2d6+4/19-20)
      entries:
      - - damage: 2d6+4
          crit_range: 19-20
      attack: mwk greatsword with magic weapon
      bonus:
      - 4
  ranged:
  - - text: light crossbow +1 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 1
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - channel negative energy 3/day (DC 11, 1d6)
  - destructive smite (+1, 6/day)
spell_like_abilities:
  entries:
  - name: touch of chaos
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 2
    concentration: 5
spells:
  entries:
  - name: bane
    source: Cleric
    level: 1
    DC: 14
  - name: magic stone
    source: Cleric
    level: 1
  - name: magic weapon
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 2
    concentration: 5
    slots:
      0: at-will
    domains:
    - chaos
    - destruction
tactics:
  Before Combat: The cleric casts magic weapon.
  During Combat: The cleric uses destructive smite as often as possible.
  Base Statistics: Without magic weapon, the cleric's statistics are Melee mwk greatsword
    +4 (2d6+3/19-20).
ability_scores:
  STR: 15
  DEX: 10
  CON: 15
  INT: 8
  WIS: 16
  CHA: 10
BAB: 1
CMB: 3
CMD: 13
CMD_other: 17 vs. bull rush or trip
feats:
- name: Toughness
skills:
  Knowledge (religion): 5
  Perception: 4
    to notice unusual stonework: 6
languages:
- Common
- Dwarven
special_qualities:
- aura
gear:
  combat:
  - potions of cure light wounds (2)
  other:
  - masterwork scale mail
  - light crossbow with 20 bolts
  - masterwork greatsword
  - wooden unholy symbol
  - 94 gp
desc_long: The dwarven war priest serves the god of strength, and uses her divine
  powers for the glory of war itself.

---

# War Priest

**Source** NPC Codex pg. 44
**XP** 400
Dwarf _[[classes/Cleric|cleric]]_ of Gorum 2
CE Medium humanoid (dwarf)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +4

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor) (+4 _[[feats/Dodge|dodge]]_ vs. giants)
**hp** 21 (2d8+9)
**Fort** +5, **Ref** +0, **Will** +6; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Greatsword|greatsword]]_ with _[[spells/Magic Weapon|magic weapon]]_ +4 (2d6+4/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +1 (1d8/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, channel negative energy 3/day (DC 11, 1d6), destructive smite (+1, 6/day)
**_Spell-Like Abilities_** (CL 2nd; concentration +5)
6/day—touch of chaos
**_Cleric_ Spells Prepared **(CL 2nd; concentration +5)
1st—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Magic Stone|magic stone]]_, _magic weapon_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domains **Chaos, _[[spells/Destruction|Destruction]]_

### Tactics

**Before Combat **The _cleric_ casts _magic weapon_.
**During Combat **The _cleric_ uses destructive smite as often as possible.
**Base Statistics **Without _magic weapon_, the _cleric_’s statistics are **Melee **mwk _greatsword_ +4 (2d6+3/19–20).

##### Statistics
**Str** 15, **Dex** 10, **Con** 15, **Int** 8, **Wis** 16, **Cha** 10
**Base Atk** +1; **CMB** +3; **CMD** 13 (17 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Toughness|Toughness]]_
**Skills** Knowledge (religion) +5, Perception +4 (+6 to notice unusual stonework)
**Languages** Common, Dwarven
**SQ** aura
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2); **Other Gear** masterwork _[[items/Armor/Scale mail|scale mail]]_, _light crossbow_ with 20 bolts, masterwork _greatsword_, wooden _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 94 gp

The dwarven _[[npcs/War Priest|war priest]]_ serves the god of strength, and uses her divine powers for the glory of war itself.