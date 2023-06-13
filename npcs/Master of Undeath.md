---
cssclass: [monsters]
title1: Master of Undeath
title2: Master of Undeath
CR: 14
sources:
- name: NPC Codex
  page: 56
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Human
classes:
- cleric of Urgathoa 15
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 22
  touch: 12
  flat_footed: 21
  components:
    armor: 9
    deflection: 1
    dex: 1
    natural: 1
HP:
  HP: 146
  long: 15d8+75
saves:
  fort: 14
  ref: 7
  will: 17
speeds:
  base: 30
attacks:
  melee:
  - - text: +3 scythe +17/+12/+7 (2d4+6/19-20/×4)
      entries:
      - - damage: 2d4+6
          crit_range: 19-20
          crit_multiplier: 4
      attack: +3 scythe
      bonus:
      - 17
      - 12
      - 7
  special:
  - channel negative energy 4/day (DC 18, 8d6)
  - scythe of evil (7 rounds, 2/day)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 10/day
    other: 7 rounds
  - name: touch of evil
    source: default
    freq: 10/day
    other: 7 rounds
  sources:
  - name: default
    CL: 15
    concentration: 22
spells:
  entries:
  - name: fire storm
    source: Cleric
    level: 8
    DC: 26
  - is_domain_spell: true
    name: unholy aura
    source: Cleric
    level: 8
  - is_domain_spell: true
    name: blasphemy
    source: Cleric
    level: 7
    DC: 25
  - name: destruction
    source: Cleric
    level: 7
    DC: 24
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - name: antilife shell
    source: Cleric
    level: 6
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 24
  - is_domain_spell: true
    name: create undead
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: harm
    source: Cleric
    level: 6
    DC: 23
  - name: dispel good
    source: Cleric
    level: 5
  - name: greater command
    source: Cleric
    level: 5
    DC: 22
  - name: flame strike
    source: Cleric
    level: 5
    DC: 23
  - name: insect plague
    source: Cleric
    level: 5
  - name: righteous might
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: slay living
    source: Cleric
    level: 5
    DC: 22
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: giant vermin
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
  - name: poison
    source: Cleric
    level: 4
    DC: 21
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 22
  - is_domain_spell: true
    name: animate dead
    source: Cleric
    level: 3
  - name: contagion
    source: Cleric
    level: 3
    count: 2
    DC: 20
  - name: deeper darkness
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: wind wall
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
    DC: 19
  - name: desecrate
    source: Cleric
    level: 2
  - name: gentle repose
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 19
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 18
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 18
  - name: divine favor
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    count: 2
    DC: 18
  - name: entropic shield
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 17
  - name: light
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 15
    concentration: 22
    slots:
      0: at-will
    domains:
    - death
    - evil
tactics:
  Before Combat: The cleric casts bear's endurance, desecrate, freedom of movement,
    and greater magic weapon.
  During Combat: The cleric relies on offensive spells, or on channel energy if he
    has undead allies.
  Base Statistics: Without bear's endurance and greater magic weapon, the cleric's
    statistics are hp 116; Fort +12; Melee +1 scythe +15/+10/+5 (2d4+4/19-20/×4);
    Con 14.
ability_scores:
  STR: 15
  DEX: 12
  CON: 18
  INT: 10
  WIS: 24
  CHA: 8
BAB: 11
CMB: 13
CMD: 25
feats:
- name: Combat Casting
- name: Command Undead
- name: Critical Focus
- name: Extra Channel
- name: Improved Channel
- name: Improved Critical (scythe)
- name: Improved Initiative
- name: Spell Focus (evocation)
- name: Weapon Focus (scythe)
skills:
  Bluff: 5
  Intimidate: 5
  Knowledge (local): 6
  Knowledge (religion): 9
  Perception: 20
  Spellcraft: 11
languages:
- Common
special_qualities:
- aura
- death's embrace
gear:
  combat:
  - potion of invisibility
  other:
  - +3 mithral breastplate
  - +1 scythe
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - headband of inspired wisdom +4
  - ring of protection +1
  - unholy water
  - cold iron unholy symbol (worth 500 gp)
  - onyx gems (worth 1,000 gp)
  - silver dust for desecrate (worth 25 gp)
  - 2,482 gp
desc_long: These clerics turn innocents into undead monstrosities.

---

# Master of Undeath

**Source** NPC Codex pg. 56
**XP** 38,400
Human _[[classes/Cleric|cleric]]_ of Urgathoa 15

NE Medium humanoid (human)
**Init** +5; **Senses** Perception +20

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+9 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 natural)
**hp** 146 (15d8+75)
**Fort** +14, **Ref** +7, **Will** +17

##### Offense
**Speed** 30 ft.
**Melee** +3 _[[items/Weapon/Scythe|scythe]]_ +17/+12/+7 (2d4+6/19–20/×4)
**Special Attacks** channel negative energy 4/day (DC 18, 8d6), _scythe_ of evil (7 rounds, 2/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +22)
10/day—bleeding touch (7 rounds), _[[feats/Touch Of Evil|touch of evil]]_ (7 rounds)
**_Cleric_ Spells Prepared **(CL 15th; concentration +22)
8th—_[[spells/Fire Storm|fire storm]]_ (DC 26), _[[spells/Unholy Aura|unholy aura]]_
7th—blasphemyD (DC 25), _[[spells/Destruction|destruction]]_ (DC 24), _[[spells/Ethereal Jaunt|ethereal jaunt]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Blade Barrier|blade barrier]]_ (DC 24), _[[spells/Create Undead|create undead]]_, harmD (DC 23)
5th—_[[spells/Dispel Good|dispel good]]_, greater _[[spells/Command|command]]_ (DC 22), _[[spells/Flame Strike|flame strike]]_ (DC 23), _[[spells/Insect Plague|insect plague]]_, _[[spells/Righteous Might|righteous might]]_, slay livingD (DC 22)
4th—_[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Giant Vermin|giant vermin]]_, greater _[[spells/Magic Weapon|magic weapon]]_, poison (DC 21), _[[items/Weapon Magic Abilities/Unholy|unholy]]_ blightD (DC 22)
3rd—_[[spells/Animate Dead|animate dead]]_, _[[spells/Contagion|contagion]]_ (2, DC 20), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wind Wall|wind wall]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, death knellD (DC 19), _[[spells/Desecrate|desecrate]]_, _[[spells/Gentle Repose|gentle repose]]_, _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 18), cause fearD (DC 18), _[[spells/Divine Favor|divine favor]]_, _[[spells/Doom|doom]]_ (2, DC 18), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), light, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **Death, Evil

### Tactics

**Before Combat **The _cleric_ casts bear’s _endurance_, _desecrate_, _freedom of movement_, and greater _magic weapon_.
**During Combat **The _cleric_ relies on offensive spells, or on channel energy if he has undead allies.
**Base Statistics **Without bear’s _endurance_ and greater _magic weapon_, the _cleric_’s statistics are **hp **116; **Fort **+12; **Melee** +1 _scythe_ +15/+10/+5 (2d4+4/19–20/×4); **Con **14.

##### Statistics
**Str** 15, **Dex** 12, **Con** 18, **Int** 10, **Wis** 24, **Cha** 8
**Base Atk** +11; **CMB** +13; **CMD** 25
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Bluff +5, Intimidate +5, Knowledge (local) +6, Knowledge (religion) +9, Perception +20, Spellcraft +11
**Languages** Common
**SQ** aura, death’s embrace
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** +3 mithral _[[items/Armor/Breastplate|breastplate]]_, +1 _scythe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _unholy_ water, cold iron _unholy_ symbol (worth 500 gp), onyx gems (worth 1,000 gp), silver dust for _desecrate_ (worth 25 gp), 2,482 gp

These clerics turn innocents into undead monstrosities.