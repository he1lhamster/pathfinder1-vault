---
cssclass: [monsters]
title1: Vampire, Enlightened Vampire
title2: Enlightened Vampire
CR: 12
sources:
- name: Monster Codex
  page: 242
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Human
classes:
- vampire monk (hungry ghost monk) 11 (Pathfinder RPG Advanced Player's Guide 110)
alignment: LE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 34
  touch: 25
  flat_footed: 28
  components:
    armor: 2
    deflection: 1
    dex: 5
    dodge: 1
    monk: 4
    wis: 4
    natural: 7
HP:
  HP: 108
  long: 11d8+55
  fast_healing: 5
saves:
  fort: 10
  ref: 14
  will: 11
  other: +2 vs. enchantments
defensive_abilities:
- channel resistance +4
- improved evasion
DR:
- amount: 10
  weakness: magic and silver
immunities:
- disease
- poison
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- vampire weaknesses
speeds:
  base: 60
attacks:
  melee:
  - - text: unarmed strike +15/+10 (2d8+6/19-20 plus energy drain)
      entries:
      - - damage: 2d8+6
          crit_range: 19-20
        - effect: energy drain
      attack: unarmed strike
      bonus:
      - 15
      - 10
  - - text: flurry of blows +15/+15/+10/+10/+5 (2d8+6/19-20 plus energy drain)
      entries:
      - - damage: 2d8+6
          crit_range: 19-20
        - effect: energy drain
      attack: flurry of blows
      bonus:
      - 15
      - 15
      - 10
      - 10
      - 5
  - - text: slam +14 (1d4+6 plus energy drain)
      entries:
      - - damage: 1d4+6
        - effect: energy drain
      attack: slam
      bonus:
      - 14
  special:
  - blood drain
  - children of the night
  - create spawn
  - dominate (DC 18)
  - energy drain (2 levels, DC 18)
  - flurry of blows
  - life from a stone
  - life funnel
  - steal ki
tactics:
  During Combat: The enlightened vampire uses flurry of blows and ki strike to gain
    extra attacks, and uses steal ki and life funnel to replenish his ki and hit points.
    He uses Punishing Kick to knock his most dangerous opponent prone, then grapples
    it and drains its blood.
ability_scores:
  STR: 22
  DEX: 20
  CON:
  INT: 14
  WIS: 18
  CHA: 16
BAB: 8
CMB: 17
CMB_other: +21 grapple
CMD: 39
CMD_other: 41 vs. grapple
feats:
- is_bonus: true
  name: Alertness
- name: Combat Expertise
- is_bonus: true
  name: Dodge
- name: Gorgon's Fist
- name: Greater Grapple
- name: Improved Critical (unarmed strike)
- name: Improved Grapple
- is_bonus: true
  name: Improved Initiative
- name: Improved Unarmed Strike
- superscripts:
  - UM
  name: Ki Stand
- is_bonus: true
  name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- superscripts:
  - APG
  name: Punishing Kick
- name: Scorpion Style
- name: Step Up
- is_bonus: true
  name: Toughness
- name: Weapon Focus (unarmed strike)
skills:
  Acrobatics: 19
    when jumping: 42
  Climb: 20
  Intimidate: 17
  Knowledge (history): 16
  Perception: 30
  Sense Motive: 30
  Stealth: 27
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Celestial
- Common
- Elven
special_qualities:
- change shape (dire bat or wolf, beast shape II)
- fast movement
- gaseous form
- high jump
- ki pool (9 points, cold iron/lawful/magic)
- life funnel
- maneuver training
- shadowless
- slow fall 50 ft.
- spider climb
gear:
  combat:
  - potion of displacement
  - potion of haste
  other:
  - amulet of natural armor +1
  - belt of physical might +2 (Str, Dex)
  - bracers of armor +1
  - headband of alluring charisma +2
  - ring of protection +1
  - 500 gp
ecology:
  environment: any
desc_long: An enlightened vampire spends his nights in meditation. He tries to live
  an ascetic's life, in search of purity and wholeness, even if his very nature requires
  him to harm others on a regular basis. Because of this, he lives in a state of suffering,
  seeking to atone for his nature while exploring the mysteries of enlightenment.
  This outlook on unlife doesn't stop him from killing his enemies. Whenever someone
  harms his spawn or one of his herd, an enlightened vampire responds with deliberate
  and decisive action.

---

# Vampire, Enlightened Vampire

**Source** Monster Codex pg. 242
**XP** 19,200
Human _[[monsters/Vampire|vampire]]_ _[[classes/Monk|monk]]_ (hungry _[[monsters/Ghost|ghost]]_ _monk_) 11 (Pathfinder RPG Advanced Player’s Guide 110)

LE Medium undead (augmented humanoid, human)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +30

##### Defense

**AC** 34, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+2 armor, +1 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +4 _monk_, +4 Wis, +7 natural)
**hp** 108 (11d8+55); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +10, **Ref** +14, **Will** +11; +2 vs. enchantments
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, improved evasion; **DR** 10/magic and silver; **Immune** disease, poison, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _vampire_ weaknesses

##### Offense
**Speed** 60 ft.
**Melee** unarmed strike +15/+10 (2d8+6/19–20 plus _[[universal monster rules/Energy Drain|energy drain]]_) or flurry of blows +15/+15/+10/+10/+5 (2d8+6/19–20 plus _energy drain_) or slam +14 (1d4+6 plus _energy drain_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_, children of the night, create spawn, dominate (DC 18), _energy drain_ (2 levels, DC 18), flurry of blows, life from a stone, life funnel, steal ki

### Tactics

**During Combat **The enlightened _vampire_ uses flurry of blows and ki strike to gain extra attacks, and uses steal ki and life funnel to replenish his ki and hit points. He uses _[[feats/Punishing Kick|Punishing Kick]]_ to _[[spells/Knock|knock]]_ his most dangerous opponent _[[conditions/Prone|prone]]_, then grapples it and drains its blood.

##### Statistics
**Str** 22, **Dex** 20, **Con** —, **Int** 14, **Wis** 18, **Cha** 16
**Base Atk** +8; **CMB** +17 (+21 grapple); **CMD** 39 (41 vs. grapple)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[monsters/Gorgon|Gorgon]]_’s Fist, _[[feats/Greater Grapple|Greater Grapple]]_, _[[feats/Improved Critical|Improved Critical]]_ (unarmed strike), _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Ki Stand|Ki Stand]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _Punishing Kick_, _[[feats/Scorpion Style|Scorpion Style]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (unarmed strike)
**Skills** Acrobatics +19 (+42 when jumping), _[[universal monster rules/Climb|Climb]]_ +20, Intimidate +17, Knowledge (history) +16, Perception +30, Sense Motive +30, Stealth +27; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Celestial, Common, Elven
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (dire bat or _[[monsters/Wolf|wolf]]_, _[[spells/Beast Shape II|beast shape II]]_), fast movement, _[[spells/Gaseous Form|gaseous form]]_, high _[[spells/Jump|jump]]_, ki pool (9 points, cold iron/lawful/magic), life funnel, maneuver _[[items/Weapon Magic Abilities/Training|training]]_, shadowless, _[[spells/Slow|slow]]_ fall 50 ft., _[[spells/Spider Climb|spider climb]]_
**Combat Gear** potion of _[[spells/Displacement|displacement]]_, potion of _[[spells/Haste|haste]]_; **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Dex), _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 500 gp

##### Ecology

**Environment** any

##### Description

An enlightened _vampire_ spends his nights in meditation. He tries to live an ascetic’s life, in search of purity and wholeness, even if his very nature requires him to _[[spells/Harm|harm]]_ others on a regular basis. Because of this, he lives in a state of suffering, seeking to atone for his nature while exploring the mysteries of enlightenment. This outlook on unlife doesn’t stop him from killing his enemies. Whenever someone harms his spawn or one of his herd, an enlightened _vampire_ responds with deliberate and decisive action.