---
cssclass: [monsters]
title1: Fire Cleric
title2: Fire Cleric
CR: 10
sources:
- name: NPC Codex
  page: 52
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Human
classes:
- cleric of Asmodeus 11
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 3
AC:
  AC: 20
  touch: 9
  flat_footed: 20
  components:
    armor: 7
    dex: -1
    natural: 1
    shield: 3
HP:
  HP: 75
  long: 11d8+22
saves:
  fort: 9
  ref: 5
  will: 13
resistances:
  electricity: 20
  fire: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk heavy mace +10/+5 (1d8+1)
      entries:
      - - damage: 1d8+1
      attack: mwk heavy mace
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk light crossbow +8 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 8
  special:
  - channel negative energy 7/day (DC 19, 6d6)
  - staff of order (5 rounds, 1/day)
spell_like_abilities:
  entries:
  - name: fire bolt
    source: default
    freq: 8/day
    other: 1d6+5 fire
  - name: touch of law
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 23
  - is_domain_spell: true
    name: fire seeds
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: fire shield
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    count: 2
    DC: 22
  - name: spell resistance
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: cure serious wounds
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 19
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: wall of fire
    source: Cleric
    level: 4
  - name: cure serious wounds
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: fireball
    source: Cleric
    level: 3
    DC: 20
  - name: glyph of warding
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - name: water walk
    source: Cleric
    level: 3
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - is_domain_spell: true
    name: produce flame
    source: Cleric
    level: 2
  - name: resist energy
    source: Cleric
    level: 2
    count: 2
    DC: 17
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - name: bless
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: burning hands
    source: Cleric
    level: 1
    DC: 18
  - name: command
    source: Cleric
    level: 1
    count: 2
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: endure elements
    source: Cleric
    level: 1
  - name: magic weapon
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 11
    concentration: 16
    slots:
      0: at-will
    domains:
    - fire
    - law
tactics:
  Before Combat: The cleric casts freedom of movement and resist energy (electricity).
  During Combat: The cleric casts fire shield (warm shield), uses his wand of shield
    of faith, then attacks with fire spells, switching to blade barrier, channeled
    energy, and flame strike against fire-resistant opponents.
ability_scores:
  STR: 13
  DEX: 8
  CON: 12
  INT: 10
  WIS: 21
  CHA: 14
BAB: 8
CMB: 9
CMD: 18
feats:
- name: Extra Channel
- name: Greater Spell Focus (evocation)
- name: Improved Channel
- name: Improved Initiative
- name: Lightning Reflexes
- name: Selective Channeling
- name: Spell Focus (evocation)
skills:
  Intimidate: 7
  Knowledge (nobility): 6
  Knowledge (religion): 6
  Knowledge (planes): 7
  Linguistics: 5
  Perception: 11
  Sense Motive: 13
  Spellcraft: 8
languages:
- Common
- Ignan
- Infernal
special_qualities:
- aura
gear:
  combat:
  - necklace of fireballs (type III)
  - potion of delay poison
  - wand of shield of faith (7 charges)
  other:
  - +1 breastplate
  - +1 heavy steel shield
  - masterwork heavy mace
  - masterwork light crossbow with 20 bolts
  - amulet of natural armor +1
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - silver unholy symbol
  - 1,453 gp
desc_long: The fire cleric serves infernal or elemental powers and uses his magic
  to purge weakness from the world.

---

# Fire Cleric

**Source** NPC Codex pg. 52
**XP** 9,600
Human _[[classes/Cleric|cleric]]_ of Asmodeus 11

LE Medium humanoid (human)
**Init** +3; **Senses** Perception +11

##### Defense

**AC** 20, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 armor, –1 Dex, +1 natural, +3 _[[spells/Shield|shield]]_)
**hp** 75 (11d8+22)
**Fort** +9, **Ref** +5, **Will** +13
**Resist** electricity 20, fire 10

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Heavy mace|heavy mace]]_ +10/+5 (1d8+1)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d8/19–20)
**Special Attacks** channel negative energy 7/day (DC 19, 6d6), staff of order (5 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
8/day—fire bolt (1d6+5 fire), touch of law
**_Cleric_ Spells Prepared **(CL 11th; concentration +16)
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Fire Seeds|fire seeds]]_
5th—_[[spells/Fire Shield|fire shield]]_, _[[spells/Flame Strike|flame strike]]_ (2, DC 22), _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dismissal|dismissal]]_ (DC 19), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd—_cure serious wounds_, fireballD (DC 20), _[[spells/Glyph Of Warding|glyph of warding]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Searing Light|searing light]]_, _[[spells/Water Walk|water walk]]_
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Produce Flame|produce flame]]_, _[[spells/Resist Energy|resist energy]]_ (2, DC 17), _[[spells/Silence|silence]]_ (DC 17)
1st—_[[spells/Bless|bless]]_, _[[items/Weapon Magic Abilities/Burning|burning]]_ handsD (DC 18), _[[spells/Command|command]]_ (2, DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Magic Weapon|magic weapon]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **Fire, Law

### Tactics

**Before Combat **The _cleric_ casts _freedom of movement_ and _resist energy_ (electricity).
**During Combat **The _cleric_ casts _fire shield_ (warm _shield_), uses his wand of _[[spells/Shield Of Faith|shield of faith]]_, then attacks with fire spells, switching to _blade barrier_, channeled energy, and _flame strike_ against fire-resistant opponents.

##### Statistics
**Str** 13, **Dex** 8, **Con** 12, **Int** 10, **Wis** 21, **Cha** 14
**Base Atk** +8; **CMB** +9; **CMD** 18
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Intimidate +7, Knowledge (nobility, religion) +6, Knowledge (planes) +7, Linguistics +5, Perception +11, Sense Motive +13, Spellcraft +8
**Languages** Common, Ignan, Infernal
**SQ** aura
**Combat Gear** necklace of fireballs (type III), potion of _[[spells/Delay Poison|delay poison]]_, wand of _shield of faith_ (7 charges); **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, masterwork _heavy mace_, masterwork _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 1,453 gp

The _[[npcs/Fire Cleric|fire cleric]]_ serves infernal or elemental powers and uses his magic to purge weakness from the world.