---
cssclass: [monsters]
title1: Fire Diabolist
title2: Fire Diabolist
CR: 19
sources:
- name: NPC Codex
  page: 61
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Human
classes:
- cleric of Asmodeus 20
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
AC:
  AC: 37
  touch: 14
  flat_footed: 37
  components:
    armor: 11
    deflection: 4
    natural: 4
    shield: 8
HP:
  HP: 153
  long: 20d8+60
saves:
  fort: 18
  ref: 10
  will: 23
immunities:
- fire
speeds:
  base: 30
attacks:
  melee:
  - - text: rod of the viper +18/+13/+8 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: rod of the viper
      bonus:
      - 18
      - 13
      - 8
  ranged:
  - - text: +1 heavy crossbow +16 (1d10+1/19-20)
      entries:
      - - damage: 1d10+1
          crit_range: 19-20
      attack: +1 heavy crossbow
      bonus:
      - 16
  special:
  - channel negative energy 6/day (DC 23, 10d6)
  - hand of the acolyte (8/day)
spell_like_abilities:
  entries:
  - name: fire bolt
    source: default
    freq: 8/day
    other: 1d6+10 fire
  - name: dispelling touch
    source: default
    freq: 4/day
  sources:
  - name: default
    CL: 20
    concentration: 25
spells:
  entries:
  - is_domain_spell: true
    name: elemental swarm
    source: Cleric
    level: 9
    other: fire spell only
  - name: energy drain
    source: Cleric
    level: 9
    DC: 24
  - name: gate
    source: Cleric
    level: 9
  - name: implosion
    source: Cleric
    level: 9
    DC: 26
  - name: summon monster IX
    source: Cleric
    level: 9
  - name: antimagic field
    source: Cleric
    level: 8
  - name: fire storm
    source: Cleric
    level: 8
    DC: 25
  - is_domain_spell: true
    name: incendiary cloud
    source: Cleric
    level: 8
    DC: 24
  - name: summon monster VIII
    source: Cleric
    level: 8
  - name: unholy aura
    source: Cleric
    level: 8
  - name: blasphemy
    source: Cleric
    level: 7
    DC: 24
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - name: greater restoration
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: spell turning
    source: Cleric
    level: 7
  - name: summon monster VII
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: antimagic field
    source: Cleric
    level: 6
  - name: blade barrier
    source: Cleric
    level: 6
    count: 2
    DC: 23
  - name: heal
    source: Cleric
    level: 6
    count: 2
  - name: break enchantment
    source: Cleric
    level: 5
  - name: dispel good
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
  - name: greater command
    source: Cleric
    level: 5
    DC: 20
  - name: insect plague
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: spell resistance
    source: Cleric
    level: 5
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: dimensional anchor
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 19
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 21
  - is_domain_spell: true
    name: wall of fire
    source: Cleric
    level: 4
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - is_domain_spell: true
    name: fireball
    source: Cleric
    level: 3
    DC: 20
  - name: magic vestment
    source: Cleric
    level: 3
    count: 2
  - name: protection from energy
    source: Cleric
    level: 3
    count: 2
    DC: 18
  - name: align weapon
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - name: lesser restoration
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: produce flame
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
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
    count: 3
    DC: 16
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 16
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 20
    concentration: 25
    slots:
      0: at-will
    domains:
    - fire
    - magic
tactics:
  Before Combat: The cleric casts delay poison, freedom of movement, magic vestment
    (armor and shield), and spell turning.
  During Combat: The cleric first conjures devils to defend him.
  Base Statistics: Without magic vestment the cleric's statistics are AC 29, touch
    14, flat-footed 29.
ability_scores:
  STR: 13
  DEX: 10
  CON: 14
  INT: 13
  WIS: 21
  CHA: 16
BAB: 15
CMB: 16
CMD: 30
feats:
- name: Alignment Channel (evil)
- name: Augment Summoning
- name: Combat Casting
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Shield Focus
- name: Spell Focus (conjuration)
- name: Spell Focus (evocation)
- name: Spell Penetration
skills:
  Bluff: 13
  Diplomacy: 16
  Intimidate: 13
  Knowledge (arcana): 9
  Knowledge (religion): 14
  Perception: 20
  Sense Motive: 18
  Spellcraft: 14
languages:
- Common
- Infernal
special_qualities:
- aura
gear:
  combat:
  - potion of displacement
  - potion of fly
  - potion of haste
  other:
  - +1 mithral breastplate
  - +1 heavy steel shield
  - +1 heavy crossbow with 20 bolts
  - rod of the viper
  - amulet of natural armor +4
  - bag of holding (type II)
  - belt of physical might +2 (Con, Dex)
  - cloak of resistance +4
  - headband of inspired wisdom +4
  - ring of counterspells
  - ring of protection +4
  - silver unholy symbol
  - material components for gate (worth 10,000 gp)
  - 3,855 gp
desc_long: The fire diabolist serves the lord of Hell. He uses flame and infernal
  creatures to subjugate all to his will.

---

# Fire Diabolist

**Source** NPC Codex pg. 61
**XP** 204,800
Human _[[classes/Cleric|cleric]]_ of Asmodeus 20

LE Medium humanoid (human)
**Init** +4; **Senses** Perception +20

##### Defense

**AC** 37, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+11 armor, +4 _[[spells/Deflection|deflection]]_, +4 natural, +8 _[[spells/Shield|shield]]_)
**hp** 153 (20d8+60)
**Fort** +18, **Ref** +10, **Will** +23
**Immune** fire

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Rod/Rod of the Viper|rod of the viper]]_ +18/+13/+8 (1d8+3)
**Ranged** +1 _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +16 (1d10+1/19–20)
**Special Attacks** channel negative energy 6/day (DC 23, 10d6), hand of the _[[npcs/Acolyte|acolyte]]_ (8/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
8/day—fire bolt (1d6+10 fire)
4/day—_[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ touch
**_Cleric_ Spells Prepared **(CL 20th; concentration +25)
9th—elemental swarmD (fire spell only), _[[universal monster rules/Energy Drain|energy drain]]_ (DC 24), _[[spells/Gate|gate]]_, _[[spells/Implosion|implosion]]_ (DC 26), _[[spells/Summon Monster IX|summon monster IX]]_
8th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Fire Storm|fire storm]]_ (DC 25), incendiary cloudD (DC 24), _[[spells/Summon Monster VIII|summon monster VIII]]_, _[[spells/Unholy Aura|unholy aura]]_
7th—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, greater _[[spells/Restoration|restoration]]_, _[[spells/Spell Turning|spell turning]]_, _[[spells/Summon Monster VII|summon monster VII]]_
6th—_antimagic field_, _[[spells/Blade Barrier|blade barrier]]_ (2, DC 23), _[[spells/Heal|heal]]_ (2)
5th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dispel Good|dispel good]]_, _[[spells/Flame Strike|flame strike]]_ (DC 22), greater _[[spells/Command|command]]_ (DC 20), _[[spells/Insect Plague|insect plague]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dismissal|dismissal]]_ (DC 19), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 21), _[[spells/Wall Of Fire|wall of fire]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), fireballD (DC 20), _[[spells/Magic Vestment|magic vestment]]_ (2), _[[spells/Protection from Energy|protection from energy]]_ (2, DC 18)
2nd—_[[spells/Align Weapon|align weapon]]_, _[[spells/Delay Poison|delay poison]]_, _[[spells/Hold Person|hold person]]_ (DC 17), lesser _restoration_, _[[spells/Produce Flame|produce flame]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bless|bless]]_, _[[items/Weapon Magic Abilities/Burning|burning]]_ handsD (DC 18), _command_ (3, DC 16), _[[spells/Doom|doom]]_ (DC 16), _[[spells/Sanctuary|sanctuary]]_ (DC 16)
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_
**D **Domain spell; **Domains **Fire, Magic

### Tactics

**Before Combat **The _cleric_ casts _delay poison_, _freedom of movement_, _magic vestment_ (armor and _shield_), and _spell turning_.
**During Combat **The _cleric_ first conjures devils to defend him.
**Base Statistics **Without _magic vestment_ the _cleric_’s statistics are **AC **29, touch 14, _flat-footed_ 29.

##### Statistics
**Str** 13, **Dex** 10, **Con** 14, **Int** 13, **Wis** 21, **Cha** 16
**Base Atk** +15; **CMB** +16; **CMD** 30
**Feats** _[[feats/Alignment Channel|Alignment Channel]]_ (evil), _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Shield Focus|Shield Focus]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _Spell Focus_ (evocation), _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Bluff +13, Diplomacy +16, Intimidate +13, Knowledge (arcana) +9, Knowledge (religion) +14, Perception +20, Sense Motive +18, Spellcraft +14
**Languages** Common, Infernal
**SQ** aura
**Combat Gear** potion of _[[spells/Displacement|displacement]]_, potion of fly, potion of _[[spells/Haste|haste]]_; **Other Gear** +1 mithral _[[items/Armor/Breastplate|breastplate]]_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _heavy crossbow_ with 20 bolts, _rod of the viper_, _[[items/Wondrous Item/Amulet of Natural Armor +4|amulet of natural armor +4]]_, bag of holding (type II), _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Con, Dex), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Counterspells|ring of counterspells]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, material components for _gate_ (worth 10,000 gp), 3,855 gp

The _[[npcs/Fire Diabolist|fire diabolist]]_ serves the lord of Hell. He uses flame and infernal creatures to subjugate all to his will.