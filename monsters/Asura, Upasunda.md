---
cssclass: [monsters]
title1: Asura, Upasunda
desc_short: This six-armed woman has three fanged faces on her head. She wears colorful
  robes, and her hands wield several exotic weapons.
title2: Upasunda
CR: 9
sources:
- name: Bestiary 3
  page: 26
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 6400
alignment: LE
size: Medium
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 7
senses:
  all-around vision: true
  darkvision: 60
auras:
- name: elusive
  radius: 50
AC:
  AC: 24
  touch: 21
  flat_footed: 16
  components:
    dex: 7
    dodge: 1
    insight: 3
    natural: 3
HP:
  HP: 114
  long: 12d10+48
  regeneration: 5
  regeneration_weakness: good weapons, good spells
saves:
  fort: 12
  ref: 11
  will: 15
defensive_abilities:
- improved evasion
DR:
- amount: 10
  weakness: good
immunities:
- curse effects
- disease
- flanking
- poison
resistances:
  acid: 10
  electricity: 10
SR: 20
speeds:
  base: 50
attacks:
  melee:
  - - text: mwk longsword +19/+14/+9 (1d8+6/19-20)
      entries:
      - - damage: 1d8+6
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 19
      - 14
      - 9
    - text: mwk spear +19 (1d8+9/×3)
      entries:
      - - damage: 1d8+9
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 19
    - text: mwk kukri +19 (1d4+6/18-20)
      entries:
      - - damage: 1d4+6
          crit_range: 18-20
      attack: mwk kukri
      bonus:
      - 19
    - text: 2 slams +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: slams
      bonus:
      - 13
  - - text: 6 slams +18 (1d4+6)
      entries:
      - - damage: 1d4+6
      count: 6
      attack: slams
      bonus:
      - 18
  special:
  - infused weapons
  - multiweapon mastery
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: feather fall
    source: default
    freq: At will
  - name: see invisibility
    source: default
    freq: At will
  - name: spider climb
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: levitate
    source: default
    freq: 3/day
  - name: rainbow pattern
    source: default
    freq: 3/day
    DC: 18
  - name: haste
    source: default
    freq: 1/day
  - name: hold monster
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: adhukaits
      amount: 2
      chance: 45%
    - name: upasunda
      amount: 1
      chance: 20%
  sources:
  - name: default
    CL: 9
    concentration: 13
ability_scores:
  STR: 22
  DEX: 24
  CON: 19
  INT: 15
  WIS: 24
  CHA: 19
BAB: 12
CMB: 18
CMB_other: +20 grapple
CMD: 39
CMD_other: 41 vs. grapple
feats:
- name: Cleave
- is_bonus: true
  name: Combat Reflexes
- is_bonus: true
  name: Deflect Arrows
- name: Dodge
- name: Great Cleave
- is_bonus: true
  name: Improved Grapple
- name: Mobility
- name: Power Attack
- name: Spring Attack
skills:
  Acrobatics: 19
    when jumping: 27
  Bluff: 16
  Diplomacy: 13
  Escape Artist: 25
  Intimidate: 16
  Knowledge (arcana): 8
  Knowledge (planes): 14
  Perception: 23
  Perform (dance): 16
  Sense Motive: 19
  Stealth: 19
  _racial_mods:
    Acrobatics:
      when jumping: 8
    Escape Artist:
      _: 6
    Perception:
      _: 4
languages:
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or squad (3-6)
  treasure_type: standard
  treasure:
  - weapons listed above plus other treasure
special_abilities:
  Infused Weapons (Su): In addition to being evil and lawful, weapons an upasunda
    wields are considered to be magic for the purposes of overcoming damage reduction.
  Multiweapon Mastery (Ex): An upasunda takes no penalties when fighting with multiple
    weapons.
desc_long: |-
  Upasundas, also called beatific ones, are asuras who devote themselves to martial meditations and physical perfection. Upasundas seek monklike poise and skill, and through it, the ability to deal flawless destruction wherever they go. Their nickname suggests purity, and indeed, each beatific one is an expression of asura purity through devotion to the ideal of annihilation. It is believed that the first upasundas were created from the jealous followers of a man who achieved divinity through his own force of will. Those of his followers who felt abandoned when this new deity ascended to the Great Beyond sought other ways to achieve immortality, and fell pray to one of the asura ranas, who granted them their desire by transforming them into beatific ones.

  Upasundas never surrender to foes in combat and rarely flee from battle. They hope to increase in skill and wisdom or to die in battle. On either path lies evolution toward a greater understanding of destruction in its countless forms.

  An upasunda is 7 feet tall and weighs 240 pounds.

---

# Asura, Upasunda
This six-armed woman has three fanged faces on her head. She wears colorful robes, and her hands wield several exotic weapons.
**Source** Bestiary 3 pg. 26
**XP** 6,400

LE Medium outsider (asura, evil, extraplanar, lawful)
**Init** +7; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +23
**Aura** elusive (50 ft.)

##### Defense

**AC** 24, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +3 insight, +3 natural)
**hp** 114 (12d10+48); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells)
**Fort** +12, **Ref** +11, **Will** +15
**Defensive Abilities** improved evasion; **DR** 10/good; **Immune** curse effects, disease, flanking, poison; **Resist** acid 10, electricity 10; **SR** 20

##### Offense
**Speed** 50 ft.
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +19/+14/+9 (1d8+6/19–20), mwk _[[items/Weapon/Spear|spear]]_ +19 (1d8+9/×3), mwk _[[items/Weapon/Kukri|kukri]]_ +19 (1d4+6/18–20), 2 slams +13 (1d4+3) or 6 slams +18 (1d4+6)
**Special Attacks** infused weapons, _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
At will—_[[spells/Disguise Self|disguise self]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Feather Fall|feather fall]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Spider Climb|spider climb]]_
3/day—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Levitate|levitate]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 18)
1/day—_[[spells/Haste|haste]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 4, 2 adhukaits 45% or 1 upasunda 20%)

##### Statistics
**Str** 22, **Dex** 24, **Con** 19, **Int** 15, **Wis** 24, **Cha** 19
**Base Atk** +12; **CMB** +18 (+20 grapple); **CMD** 39 (41 vs. grapple)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _Dodge_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Acrobatics +19 (+27 when jumping), Bluff +16, Diplomacy +13, Escape Artist +25, Intimidate +16, Knowledge (arcana) +8, Knowledge (planes) +14, Perception +23, Perform (dance) +16, Sense Motive +19, Stealth +19; **Racial Modifiers** +8 Acrobatics when jumping, +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or squad (3–6)
**Treasure** standard (weapons listed above plus other treasure)

### Special Abilities

**Infused Weapons (Su)** In addition to being evil and lawful, weapons an upasunda wields are considered to be magic for the purposes of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.

**_Multiweapon Mastery_ (Ex)** An upasunda takes no penalties when fighting with multiple weapons.

##### Description

Upasundas, also _[[items/Weapon Magic Abilities/Called|called]]_ beatific ones, are asuras who devote themselves to martial meditations and physical perfection. Upasundas seek monklike poise and skill, and through it, the ability to deal flawless _[[spells/Destruction|destruction]]_ wherever they go. Their nickname suggests purity, and indeed, each _[[monsters/Beatific One|beatific one]]_ is an expression of asura purity through devotion to the ideal of annihilation. It is believed that the first upasundas were created from the jealous followers of a man who achieved divinity through his own force of will. Those of his followers who felt abandoned when this new deity ascended to the Great Beyond sought other ways to achieve immortality, and fell pray to one of the asura ranas, who granted them their desire by transforming them into beatific ones.

Upasundas never surrender to foes in combat and rarely flee from battle. They hope to increase in skill and wisdom or to die in battle. On either path lies evolution toward a greater understanding of _destruction_ in its countless forms.

An upasunda is 7 feet tall and weighs 240 pounds.