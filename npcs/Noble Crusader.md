---
cssclass: [monsters]
title1: Noble Crusader
title2: Noble Crusader
CR: 4
sources:
- name: NPC Codex
  page: 46
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1200
race: Human
classes:
- cleric of Iomedae 5
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: -1
AC:
  AC: 18
  touch: 9
  flat_footed: 18
  components:
    armor: 7
    dex: -1
    shield: 2
HP:
  HP: 41
  long: 5d8+15
saves:
  fort: 7
  ref: 1
  will: 7
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk longsword +8 (1d8+3/19-20)
      entries:
      - - damage: 1d8+3
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 8
  special:
  - channel positive energy 6/day (DC 13, 3d6)
spell_like_abilities:
  entries:
  - name: touch of law
    source: default
    freq: 5/day
  - name: battle rage
    source: default
    freq: 5/day
    other: +2 damage
  sources:
  - name: default
    CL: 5
    concentration: 7
spells:
  entries:
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: law only
  - name: enthrall
    source: Cleric
    level: 2
    DC: 14
  - name: resist energy
    source: Cleric
    level: 2
    DC: 14
  - name: sound burst
    source: Cleric
    level: 2
    DC: 14
  - name: command
    source: Cleric
    level: 1
    DC: 13
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: magic weapon
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: summon monster I
    source: Cleric
    level: 1
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 7
    slots:
      0: at-will
    domains:
    - law
    - war
tactics:
  Before Combat: The cleric casts magic vestment.
  During Combat: The cleric attacks with her longsword, and casts magic weapon or
    align weapon as needed. When fighting undead, she channels positive energy. Otherwise,
    she uses ranged magical attacks only as a last resort.
  Base Statistics: Without magic vestment, the cleric's statistics are AC 18, touch
    9, flat-footed 18.
ability_scores:
  STR: 17
  DEX: 8
  CON: 14
  INT: 10
  WIS: 14
  CHA: 12
BAB: 3
CMB: 6
CMD: 15
feats:
- name: Combat Casting
- name: Heavy Armor Proficiency
- name: Improved Shield Bash
- name: Weapon Focus (longsword)
skills:
  Diplomacy: 9
  Heal: 6
  Knowledge (nobility): 6
  Knowledge (religion): 5
  Perception: 6
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of bull's strength
  - thunderstone
  other:
  - masterwork splint mail
  - +1 light steel shield
  - masterwork longsword
  - cloak of resistance +1
  - silver holy symbol
  - 271 gp
desc_long: The noble crusader battles the forces of chaos, usually at the behest of
  a local monarch.

---

# Noble Crusader

**Source** NPC Codex pg. 46
**XP** 1,200
Human _[[classes/Cleric|cleric]]_ of Iomedae 5

LN Medium humanoid (human)
**Init** –1; **Senses** Perception +6

##### Defense

**AC** 18, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 armor, –1 Dex, +2 _[[spells/Shield|shield]]_)
**hp** 41 (5d8+15)
**Fort** +7, **Ref** +1, **Will** +7

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +8 (1d8+3/19–20)
**Special Attacks** channel positive energy 6/day (DC 13, 3d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +7)
5/day—touch of law
5/day—battle _[[spells/Rage|rage]]_ (+2 damage)
**_Cleric_ Spells Prepared **(CL 5th; concentration +7)
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Searing Light|searing light]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (law only), _[[spells/Enthrall|enthrall]]_ (DC 14), _[[spells/Resist Energy|resist energy]]_ (DC 14), _[[spells/Sound Burst|sound burst]]_ (DC 14)
1st—_[[spells/Command|command]]_ (DC 13), _[[spells/Divine Favor|divine favor]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Shield Of Faith|shield of faith]]_, _[[spells/Summon Monster I|summon monster I]]_
0 (at will)—_[[spells/Guidance|guidance]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domains **Law, War

### Tactics

**Before Combat **The _cleric_ casts _magic vestment_.
**During Combat **The _cleric_ attacks with her _longsword_, and casts _magic weapon_ or _align weapon_ as needed. When fighting undead, she channels positive energy. Otherwise, she uses ranged magical attacks only as a last resort.
**Base Statistics **Without _magic vestment_, the _cleric_’s statistics are **AC **18, touch 9, _flat-footed_ 18.

##### Statistics
**Str** 17, **Dex** 8, **Con** 14, **Int** 10, **Wis** 14, **Cha** 12
**Base Atk** +3; **CMB** +6; **CMD** 15
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved _Shield_ Bash|Improved _Shield_ Bash]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_)
**Skills** Diplomacy +9, _[[spells/Heal|Heal]]_ +6, Knowledge (nobility) +6, Knowledge (religion) +5, Perception +6
**Languages** Common
**SQ** aura
**Combat Gear** potion of bull’s strength, _[[items/Mundane/Thunderstone|thunderstone]]_; **Other Gear** masterwork _[[items/Armor/Splint mail|splint mail]]_, +1 _[[items/Shield/Light steel shield|light steel shield]]_, masterwork _longsword_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, silver holy symbol, 271 gp

The _[[npcs/Noble Crusader|noble crusader]]_ battles the forces of chaos, usually at the behest of a local monarch.