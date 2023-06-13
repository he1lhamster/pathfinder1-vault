---
cssclass: [monsters]
title1: Death Priest
title2: Death Priest
CR: 8
sources:
- name: NPC Codex
  page: 50
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Human
classes:
- cleric of Urgathoa 9
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
AC:
  AC: 20
  touch: 13
  flat_footed: 18
  components:
    armor: 7
    deflection: 1
    dex: 2
HP:
  HP: 89
  long: 9d8+27
saves:
  fort: 11
  ref: 6
  will: 11
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +5/+0 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 5
      - 0
  ranged:
  - - text: light crossbow +8 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 8
  special:
  - channel negative energy 4/day (DC 17, 5d6)
  - hand of the acolyte (7/day)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 7/day
    other: 4 rounds
  - name: dispelling touch
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - is_domain_spell: true
    name: slay living
    source: Cleric
    level: 5
    count: 2
    DC: 21
  - is_domain_spell: true
    name: death ward
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: poison
    source: Cleric
    level: 4
    DC: 20
  - name: spell immunity
    source: Cleric
    level: 4
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 19
  - name: contagion
    source: Cleric
    level: 3
    count: 2
    DC: 19
  - is_domain_spell: true
    name: dispel magic
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: darkness
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
    DC: 18
  - name: delay poison
    source: Cleric
    level: 2
    DC: 16
  - name: desecrate
    source: Cleric
    level: 2
  - name: resist energy
    source: Cleric
    level: 2
    DC: 16
  - name: bane
    source: Cleric
    level: 1
    DC: 15
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 17
    count: 2
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: protection from good
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 16
  - name: detect poison
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 9
    concentration: 13
    slots:
      0: at-will
    domains:
    - death
    - magic
tactics:
  Before Combat: The cleric casts bear's endurance, delay poison, and freedom of movement.
  During Combat: The cleric lets allies or undead minions handle the bulk of the fighting,
    using bestow curse, contagion, and slay living against individual foes or channeling
    negative energy against groups or to heal herself and her undead allies.
  Base Statistics: Without bear's endurance, the cleric's statistics are hp 71, Fort
    +9, Con 14.
ability_scores:
  STR: 8
  DEX: 15
  CON: 18
  INT: 10
  WIS: 19
  CHA: 12
BAB: 6
CMB: 5
CMD: 18
feats:
- name: Combat Casting
- name: Command Undead
- name: Greater Spell Focus (necromancy)
- name: Improved Channel
- name: Improved Initiative
- name: Spell Focus (necromancy)
skills:
  Craft (alchemy): 6
  Heal: 10
  Intimidate: 7
  Knowledge (religion): 12
  Perception: 10
languages:
- Common
special_qualities:
- aura
- death's embrace
gear:
  gear:
  - +1 chainmail
  - dagger
  - light crossbow with 20 bolts
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - pearl of power (1st)
  - ring of protection +1
  - bone unholy symbol
  - unholy water
  - onyx gems (worth 500 gp)
  - silver dust for desecrate (worth 25 gp)
  - 162 gp
desc_long: A death priest serves the goddess of plague and undeath, and seeks to infect,
  kill, and animate anyone who stands in her way. She might desire to one day become
  undead, but remains alive for now so she can carry out tasks in places that would
  never allow the undead.

---

# Death Priest

**Source** NPC Codex pg. 50
**XP** 4,800
Human _[[classes/Cleric|cleric]]_ of Urgathoa 9

NE Medium humanoid (human)
**Init** +6; **Senses** Perception +10

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex)
**hp** 89 (9d8+27)
**Fort** +11, **Ref** +6, **Will** +11

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +5/+0 (1d4–1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d8/19–20)
**Special Attacks** channel negative energy 4/day (DC 17, 5d6), hand of the _[[npcs/Acolyte|acolyte]]_ (7/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
7/day—bleeding touch (4 rounds)
1/day—_[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ touch
**_Cleric_ Spells Prepared **(CL 9th; concentration +13)
5th—slay livingD (2, DC 21)
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Freedom of Movement|freedom of movement]]_, poison (DC 20), _[[spells/Spell Immunity|spell immunity]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Contagion|contagion]]_ (2, DC 19), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Prayer|prayer]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Darkness|darkness]]_, death knellD (DC 18), _[[spells/Delay Poison|delay poison]]_ (DC 16), _[[spells/Desecrate|desecrate]]_, _[[spells/Resist Energy|resist energy]]_ (DC 16)
1st—_[[spells/Bane|bane]]_ (DC 15), cause fearD (DC 17, 2), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **Death, Magic

### Tactics

**Before Combat **The _cleric_ casts bear’s _endurance_, _delay poison_, and _freedom of movement_.
**During Combat **The _cleric_ lets allies or undead minions handle the bulk of the fighting, using _bestow curse_, _contagion_, and _[[spells/Slay Living|slay living]]_ against individual foes or _[[items/Armor Magic Abilities/Channeling|channeling]]_ negative energy against groups or to _[[spells/Heal|heal]]_ herself and her undead allies.
**Base Statistics **Without bear’s _endurance_, the _cleric_’s statistics are hp 71, Fort +9, Con 14.

##### Statistics
**Str** 8, **Dex** 15, **Con** 18, **Int** 10, **Wis** 19, **Cha** 12
**Base Atk** +6; **CMB** +5; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (necromancy), _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy)
**Skills** Craft (alchemy) +6, _Heal_ +10, Intimidate +7, Knowledge (religion) +12, Perception +10
**Languages** Common
**SQ** aura, death’s embrace
**Gear** +1 _[[items/Armor/Chainmail|chainmail]]_, _dagger_, _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, pearl of power (1st), _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, bone _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, _unholy_ water, onyx gems (worth 500 gp), silver dust for _desecrate_ (worth 25 gp), 162 gp

A _[[npcs/Death Priest|death priest]]_ serves the goddess of plague and undeath, and seeks to infect, kill, and animate anyone who stands in her way. She might desire to one day become undead, but remains alive for now so she can carry out tasks in places that would never allow the undead.