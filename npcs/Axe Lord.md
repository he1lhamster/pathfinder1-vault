---
cssclass: [monsters]
title1: Axe Lord
title2: Axe Lord
CR: 16
sources:
- name: NPC Codex
  page: 124
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Dwarf
classes:
- paladin of Torag 17
alignment: LG
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 3
auras:
- name: courage
  radius: 10
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
- name: righteousness
  radius: 10
AC:
  AC: 26
  touch: 11
  flat_footed: 26
  components:
    armor: 10
    deflection: 2
    dex: -1
    natural: 1
    shield: 4
HP:
  HP: 183
  long: 17d10+85
saves:
  fort: 16
  ref: 7
  will: 15
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
DR:
- amount: 5
  weakness: evil
immunities:
- charm
- compulsion
- disease
- fear
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: +3 shock dwarven waraxe +27/+22/+17/+12 (1d10+9/19-20/×3 plus 1d6 electricity)
      entries:
      - - damage: 1d10+9
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: electricity
      attack: +3 shock dwarven waraxe
      bonus:
      - 27
      - 22
      - 17
      - 12
  ranged:
  - - text: +1 throwing axe +17/+12/+7/+2 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: +1 throwing axe
      bonus:
      - 17
      - 12
      - 7
      - 2
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - channel positive energy (DC 20, 9d6)
  - smite evil 6/day (+2 attack and AC, +17 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 17
    concentration: 19
spells:
  entries:
  - name: holy sword
    source: Paladin
    level: 4
  - name: greater magic weapon
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
  - name: eagle's splendor
    source: Paladin
    level: 2
    count: 2
  - name: shield other
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
    count: 2
  - name: lesser restoration
    source: Paladin
    level: 1
  - name: protection from evil
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 14
    concentration: 16
tactics:
  Before Combat: The paladin casts delay poison on himself and greater magic weapon
    on his waraxe.
  During Combat: The paladin uses Improved Vital Strike and Cleave if he has a few
    targets close together.
  Base Statistics: Without delay poison and greater magic weapon, the paladin's statistics
    are Immune charm, compulsion, disease, fear; Melee +1 shock dwarven waraxe +25/+20/+15/+10
    (1d10+7/19-20/×3 plus 1d6 electricity).
ability_scores:
  STR: 22
  DEX: 8
  CON: 16
  INT: 10
  WIS: 14
  CHA: 14
BAB: 17
CMB: 23
CMD: 34
CMD_other: 38 vs. bull rush or trip
feats:
- name: Cleave
- name: Extra Lay on Hands
- name: Improved Critical (dwarven waraxe)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Toughness
- name: Vital Strike
- name: Weapon Focus (dwarven waraxe)
skills:
  Climb: 4
  Diplomacy: 7
  Heal: 7
  Intimidate: 10
  Knowledge (local): 2
  Knowledge (religion): 5
  Perception: 12
    to notice unusual stonework: 14
  Swim: 4
languages:
- Common
- Dwarven
special_qualities:
- aura
- code of conduct
- divine bond (weapon +5, 4/day)
- lay on hands (8d6, 12/day)
- mercies (dazed, deafened, nauseated, paralyzed, shaken)
gear:
  gear:
  - +3 banded mail
  - +2 heavy steel shield
  - +1 shock dwarven waraxe
  - +1 throwing axe
  - amulet of natural armor +1
  - belt of giant strength +4
  - boots of speed
  - cloak of resistance +1
  - headband of alluring charisma +2
  - ring of protection +2
  - silver holy symbol
  - platinum rings for shield other (2, worth 50 gp each)
  - 1,667 gp
desc_long: Axe lords guard dwarven citadels, hunting foul monsters from the deeps
  and threats from outside.

---

# Axe Lord

**Source** NPC Codex pg. 124
**XP** 76,800
Dwarf _[[classes/Paladin|paladin]]_ of Torag 17

LG Medium humanoid (dwarf)
**Init** +3; **Senses** Perception +12
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.), righteousness (10 ft.)

##### Defense

**AC** 26, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+10 armor, +2 _[[spells/Deflection|deflection]]_, –1 Dex, +1 natural, +4 _[[spells/Shield|shield]]_)
**hp** 183 (17d10+85)
**Fort** +16, **Ref** +7, **Will** +15; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **DR** 5/evil; **Immune** charm, compulsion, disease, _[[universal monster rules/Fear|fear]]_, poison

##### Offense
**Speed** 20 ft.
**Melee** +3 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Dwarven waraxe|dwarven waraxe]]_ +27/+22/+17/+12 (1d10+9/19–20/×3 plus 1d6 electricity)
**Ranged** +1 _[[items/Weapon/Throwing axe|throwing axe]]_ +17/+12/+7/+2 (1d6+7)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, channel positive energy (DC 20, 9d6), smite evil 6/day (+2 attack and AC, +17 damage)
**_Spell-Like Abilities_** (CL 17th; concentration +19)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 14th; concentration +16)
4th—_[[spells/Holy Sword|holy sword]]_
3rd—greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Prayer|prayer]]_
2nd—_[[spells/Delay Poison|delay poison]]_, _[[monsters/Eagle|eagle]]_’s splendor (2), _[[spells/Shield Other|shield other]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Divine Favor|divine favor]]_ (2), lesser _[[spells/Restoration|restoration]]_, _[[spells/Protection From Evil|protection from evil]]_

### Tactics

**Before Combat **The _paladin_ casts _delay poison_ on himself and greater _magic weapon_ on his waraxe.
**During Combat **The _paladin_ uses _[[feats/Improved Vital Strike|Improved Vital Strike]]_ and _[[feats/Cleave|Cleave]]_ if he has a few targets close together.
**Base Statistics **Without _delay poison_ and greater _magic weapon_, the _paladin_’s statistics are **Immune **charm, compulsion, disease, _fear_; **Melee** +1 _shock_ _dwarven waraxe_ +25/+20/+15/+10 (1d10+7/19–20/×3 plus 1d6 electricity).

##### Statistics
**Str** 22, **Dex** 8, **Con** 16, **Int** 10, **Wis** 14, **Cha** 14
**Base Atk** +17; **CMB** +23; **CMD** 34 (38 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _Cleave_, _[[feats/Extra Lay On Hands|Extra Lay on Hands]]_, _[[feats/Improved Critical|Improved Critical]]_ (_dwarven waraxe_), _[[feats/Improved Initiative|Improved Initiative]]_, _Improved Vital Strike_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dwarven waraxe_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +4, Diplomacy +7, _[[spells/Heal|Heal]]_ +7, Intimidate +10, Knowledge (local) +2, Knowledge (religion) +5, Perception +12 (+14 to notice unusual stonework), Swim +4
**Languages** Common, Dwarven
**SQ** aura, code of conduct, divine bond (weapon +5, 4/day), lay on hands (8d6, 12/day), mercies (_[[conditions/Dazed|dazed]]_, _[[conditions/Deafened|deafened]]_, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Paralyzed|paralyzed]]_, _[[conditions/Shaken|shaken]]_)
**Gear** +3 _[[items/Armor/Banded mail|banded mail]]_, +2 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _shock_ _dwarven waraxe_, +1 _throwing axe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +4|belt of giant strength +4]]_, _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, silver holy symbol, platinum rings for _shield other_ (2, worth 50 gp each), 1,667 gp

Axe lords _[[npcs/Guard|guard]]_ dwarven citadels, hunting foul monsters from the deeps and threats from outside.