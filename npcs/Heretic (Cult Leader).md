---
cssclass: [monsters]
title1: Heretic (Cult Leader)
title2: Heretic (Cult Leader)
CR: 11
sources:
- name: GameMastery Guide
  page: 279
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 12800
race: Human
classes:
- cleric 10
- rogue 2
alignment: NE
size: Medium
type: humanoid
initiative:
  bonus: 2
AC:
  AC: 24
  touch: 14
  flat_footed: 22
  components:
    armor: 6
    deflection: 2
    dex: 2
    shield: 4
HP:
  HP: 83
  long: 12d8+29
saves:
  fort: 10
  ref: 9
  will: 13
defensive_abilities:
- evasion
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 human bane morningstar +10/+5 (1d8+2)
      entries:
      - - damage: 1d8+2
      attack: +1 human bane morningstar
      bonus:
      - 10
      - 5
  ranged:
  - - text: dagger +10 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 10
  special:
  - channel negative energy 5/day (DC 15, 5d6)
  - scythe of evil (5 rounds, 1/day)
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: rebuke death
    source: default
    freq: 8/day
    other: 1d4+5
  - name: touch of evil
    source: default
    freq: 8/day
    other: 5 rounds
  sources:
  - name: default
    CL: 10
    concentration: 15
spells:
  entries:
  - is_domain_spell: true
    name: breath of life
    source: Cleric
    level: 5
  - name: mass cure light wounds
    source: Cleric
    level: 5
  - name: righteous might
    source: Cleric
    level: 5
  - name: summon monster V
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 19
  - name: divine power
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: cure serious wounds
    source: Cleric
    level: 3
    count: 2
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: cure moderate wounds
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 17
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: undetectable alignment
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - is_domain_spell: true
    name: cure light wounds
    source: Cleric
    level: 1
  - name: deathwatch
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: purify food & drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 10
    concentration: 15
    slots:
      0: at-will
    domains:
    - evil
    - healing
ability_scores:
  STR: 12
  DEX: 14
  CON: 14
  INT: 8
  WIS: 21
  CHA: 10
BAB: 8
CMB: 9
CMD: 23
feats:
- name: Channel Smite
- name: Combat Casting
- name: Command Undead
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Extra Channel
- name: Forge Ring
- name: Vital Strike
skills:
  Bluff: 5
  Diplomacy: 5
  Heal: 10
  Knowledge (history): 3
  Knowledge (local): 3
  Knowledge (planes): 10
  Knowledge (religion): 10
  Linguistics: 5
  Perception: 10
  Profession (any one): 10
  Sense Motive: 10
  Spellcraft: 10
languages:
- Abyssal
- Common
- Infernal
- Terran
special_qualities:
- aura
- healer's blessing
- rogue talent (combat trick)
- trapfinding
gear:
  combat:
  - scroll of invisibility purge
  - alchemist's fire (2)
  other:
  - +2 chain shirt
  - +2 heavy wooden shield
  - +1 human bane morningstar
  - cold iron dagger
  - cloak of resistance +1
  - elemental gem (earth)
  - headband of inspired wisdom +2
  - ring of counterspells (dispel magic)
  - ring of protection +2
  - robe of bones
  - silver unholy symbol
npc_boon: A cult leader can bind a planar ally for the PCs, send a pair of cultists
  to assist with a task, or trade a good-aligned magical item she has taken for an
  evil one she could use.
desc_long: ''

---

# Heretic (Cult Leader)

**Source** GameMastery Guide pg. 279
**XP** 12,800
Human _[[classes/Cleric|cleric]]_ 10/rogue 2

NE Medium humanoid
**Init** +2; **Senses** Perception +10

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+6 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +4 _[[spells/Shield|shield]]_)
**hp** 83 (12d8+29)
**Fort** +10, **Ref** +9, **Will** +13
**Defensive Abilities** evasion

##### Offense
**Speed** 30 ft.
**Melee** +1 human _[[spells/Bane|bane]]_ _[[items/Weapon/Morningstar|morningstar]]_ +10/+5 (1d8+2)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +10 (1d4+1/19–20)
**Special Attacks** channel negative energy 5/day (DC 15, 5d6), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day), sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +15)
8/day—_[[spells/Rebuke|rebuke]]_ death (1d4+5), _[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
**_Cleric_ Spells Prepared **(CL 10th; concentration +15)
5th—_[[spells/Breath Of Life|breath of life]]_, mass _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Righteous Might|righteous might]]_, _[[spells/Summon Monster V|summon monster V]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dismissal|dismissal]]_ (DC 19), _[[spells/Divine Power|divine power]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Prayer|prayer]]_
2nd—aid, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Silence|silence]]_ (DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Undetectable Alignment|undetectable alignment]]_
1st—_[[spells/Command|command]]_ (DC 16), _cure light wounds_, _[[spells/Deathwatch|deathwatch]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, light, purify food &_[[items/Mundane/Amp|amp]]_; drink
**D **domain spell; **Domains **Evil, Healing

##### Statistics
**Str** 12, **Dex** 14, **Con** 14, **Int** 8, **Wis** 21, **Cha** 10
**Base Atk** +8; **CMB** +9; **CMD** 23
**Feats** _[[feats/Channel Smite|Channel Smite]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +5, Diplomacy +5, _[[spells/Heal|Heal]]_ +10, Knowledge (history) +3, Knowledge (local) +3, Knowledge (planes) +10, Knowledge (religion) +10, Linguistics +5, Perception +10, Profession (any one) +10, Sense Motive +10, Spellcraft +10
**Languages** Abyssal, Common, Infernal, Terran
**SQ** aura, _[[npcs/Healer|healer]]_’s blessing, _[[classes/Rogue|rogue]]_ talent (combat trick), trapfinding
**Combat Gear** scroll of _[[spells/Invisibility Purge|invisibility purge]]_, _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 human _bane_ _morningstar_, cold iron _dagger_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Elemental Gem|elemental gem]]_ (earth), _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Counterspells|ring of counterspells]]_ (_dispel magic_), _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Wondrous Item/Robe of Bones|robe of bones]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol

**Boon** A cult leader can bind a _[[spells/Planar Ally|planar ally]]_ for the PCs, send a pair of cultists to assist with a task, or trade a good-aligned magical item she has taken for an evil one she could use.