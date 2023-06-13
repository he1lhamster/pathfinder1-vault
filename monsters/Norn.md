---
cssclass: [monsters]
title1: Norn
desc_short: This towering, stern woman wears her long blonde hair in braids. She carries
  a reel of golden thread and a pair of shears.
title2: Norn
CR: 18
sources:
- name: Bestiary 3
  page: 202
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 153600
alignment: LN
size: Large
type: fey
initiative:
  bonus: 16
senses:
  all-around vision: true
  blindsight: 120
  low-light vision: true
  greater arcane sight: true
  true seeing: true
AC:
  AC: 33
  touch: 21
  flat_footed: 31
  components:
    armor: 7
    dex: 2
    insight: 10
    natural: 5
    size: -1
HP:
  HP: 270
  long: 20d6+200
  regeneration: 10
  regeneration_weakness: cold iron
saves:
  fort: 18
  ref: 18
  will: 21
defensive_abilities:
- death ward
- fated
- foresight
- mind blank
- never surprised or flat-footed
DR:
- amount: 15
  weakness: cold iron
immunities:
- cold
resistances:
  acid: 30
  electricity: 30
  fire: 30
SR: 29
speeds:
  base: 40
  base_other: 30 ft. with armor
attacks:
  melee:
  - - text: shears +21/+21/+16 (1d8+12/15-20 plus energy drain)
      entries:
      - - damage: 1d8+12
          crit_range: 15-20
        - effect: energy drain
      attack: shears
      bonus:
      - 21
      - 21
      - 16
    - text: touch +11 (energy drain)
      entries:
      - - effect: energy drain
      attack: touch
      bonus:
      - 11
  special:
  - energy drain (2 levels, DC 30)
  - shift fate
  - snip thread
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: death ward
    source: default
    freq: Constant
  - name: foresight
    source: default
    freq: Constant
  - name: greater arcane sight
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 23
  - name: divination
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: geas/quest
    source: default
    freq: At will
  - name: vision
    source: default
    freq: At will
  - name: wind walk
    source: default
    freq: At will
    other: self only
  - name: maze
    source: default
    freq: 1/day
  - name: moment of prescience
    source: default
    freq: 1/day
  - name: quickened phantasmal killer
    source: default
    freq: 1/day
    DC: 24
  - name: power word kill
    source: default
    freq: 1/day
  - name: time stop
    source: default
    freq: 1/day
  - name: weird
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 18
    concentration: 28
ability_scores:
  STR: 25
  DEX: 14
  CON: 30
  INT: 21
  WIS: 24
  CHA: 31
BAB: 10
CMB: 18
CMD: 40
feats:
- name: Combat Expertise
- name: Combat Reflexes
- is_bonus: true
  name: Diehard
- name: Great Fortitude
- name: Improved Great Fortitude
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Lightning Reflexes
- name: Iron Will
- name: Lightning Reflexes
- name: Quicken Spell-Like Ability (phantasmal killer)
skills:
  Bluff: 23
  Craft (cloth): 18
  Heal: 11
  Intimidate: 30
  Knowledge (all): 18
  Perception: 30
  Perform (oratory): 18
  Sense Motive: 30
  Use Magic Device: 23
languages:
- Common
- Giant
- Sylvan
- tongues
special_qualities:
- change shape (humanoid; alter self or giant form II)
ecology:
  environment: cold mountains
  organization: solitary, pair, or trio
  treasure_type: double
  treasure:
  - +3 hide armor
  - shears
  - golden thread worth 500 gp
  - other treasure
special_abilities:
  Fated (Su): A norn adds her Charisma modifier as an insight bonus to AC and on initiative
    checks.
  Shears (Su): A norn's shears function as a +5 mithral keen speed scimitar, but only
    for a norn.
  Shift Fate (Su): As an immediate action, a norn can force any one target within
    120 feet to reroll a saving throw-this ability must be used immediately after
    the saving throw is rolled, and the target must abide by the result of this second
    roll.
  Snip Thread (Su): As a standard action up to three times per day but no more often
    than once every 1d4 rounds, a norn may produce a golden thread linked to a creature's
    fate and then attempt to snip it short with her shears. The target creature must
    be within 120 feet and in the norn's line of sight. The target immediately takes
    20d6 points of damage (Fortitude DC 30 for half). If the target dies from this
    damage, the norn has cut through the thread-in this case, the target may only
    be restored to life via miracle, wish, or divine intervention. This is a death
    effect. The Save DC is Charisma-based.
desc_long: |-
  Ancient beyond imagining, the norns are a race of powerful women who hold in their hands the physical manifestation of fate and destiny in the form of golden thread. They watch over all life, intervening with reluctance when called upon or with a vengeance when the strands of fate are twisted and abused by lesser beings. Worshiped as gods by some, the norns do little to discourage this veneration.

  A norn stands 14 feet tall and weighs 800 pounds.

---

# Norn
This towering, stern woman wears her long blonde hair in braids. She carries a reel of golden thread and a pair of shears.
**Source** Bestiary 3 pg. 202
**XP** 153,600

LN Large fey
**Init** +16; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, greater _[[spells/Arcane Sight|arcane sight]]_, _[[spells/True Seeing|true seeing]]_; Perception +30

##### Defense

**AC** 33, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+7 armor, +2 Dex, +10 insight, +5 natural, –1 size)
**hp** 270 (20d6+200); _[[universal monster rules/Regeneration|regeneration]]_ 10 (cold iron)
**Fort** +18, **Ref** +18, **Will** +21
**Defensive Abilities** _[[spells/Death Ward|death ward]]_, fated, _[[spells/Foresight|foresight]]_, _[[spells/Mind Blank|mind blank]]_, never surprised or _flat-footed_; **DR** 15/cold iron; **Immune** cold; **Resist** acid 30, electricity 30, fire 30; **SR** 29

##### Offense
**Speed** 40 ft. (30 ft. with armor)
**Melee** shears +21/+21/+16 (1d8+12/15–20 plus _[[universal monster rules/Energy Drain|energy drain]]_), touch +11 (_energy drain_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _energy drain_ (2 levels, DC 30), shift fate, snip thread
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +28)
Constant—_death ward_, _foresight_, greater _arcane sight_, _mind blank_, _[[spells/Tongues|tongues]]_, _true seeing_
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 23), _[[spells/Divination|divination]]_, greater _[[spells/Dispel Magic|dispel magic]]_, geas/quest, _[[spells/Vision|vision]]_, _[[spells/Wind Walk|wind walk]]_ (self only)
1/day—_[[spells/Maze|maze]]_, _[[spells/Moment of Prescience|moment of prescience]]_, quickened _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 24), _[[spells/Power Word Kill|power word kill]]_, _[[spells/Time Stop|time stop]]_, _[[spells/Weird|weird]]_ (DC 29)

##### Statistics
**Str** 25, **Dex** 14, **Con** 30, **Int** 21, **Wis** 24, **Cha** 31
**Base Atk** +10; **CMB** +18; **CMD** 40
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Great Fortitude|Improved Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_phantasmal killer_)
**Skills** Bluff +23, Craft (cloth) +18, _[[spells/Heal|Heal]]_ +11, Intimidate +30, Knowledge (all) +18, Perception +30, Perform (oratory) +18, Sense Motive +30, Use Magic Device +23
**Languages** Common, Giant, Sylvan; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (humanoid; _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form II|giant form II]]_)

##### Ecology

**Environment** cold mountains
**Organization** solitary, pair, or trio
**Treasure** double (+3 _[[items/Armor/Hide armor|hide armor]]_, shears, golden thread worth 500 gp, other treasure)

### Special Abilities

**Fated (Su)** A _[[monsters/Norn|norn]]_ adds her Charisma modifier as an insight bonus to AC and on initiative checks.
**Shears (Su)** A _norn_’s shears function as a +5 mithral _[[items/Weapon Magic Abilities/Keen|keen]]_ speed _[[items/Weapon/Scimitar|scimitar]]_, but only for a _norn_.
**Shift Fate (Su)** As an immediate action, a _norn_ can force any one target within 120 feet to reroll a saving throw—this ability must be used immediately after the saving throw is rolled, and the target must abide by the result of this second roll.
**Snip Thread (Su)** As a standard action up to three times per day but no more often than once every 1d4 rounds, a _norn_ may produce a golden thread linked to a creature’s fate and then attempt to snip it short with her shears. The target creature must be within 120 feet and in the _norn_’s line of sight. The target immediately takes 20d6 points of damage (Fortitude DC 30 for half). If the target dies from this damage, the _norn_ has cut through the thread—in this case, the target may only be restored to life via _[[spells/Miracle|miracle]]_, _[[spells/Wish|wish]]_, or divine intervention. This is a death effect. The Save DC is Charisma-based.

##### Description

Ancient beyond imagining, the norns are a race of powerful women who hold in their hands the physical manifestation of fate and destiny in the form of golden thread. They watch over all life, intervening with reluctance when _[[items/Weapon Magic Abilities/Called|called]]_ upon or with a _[[feats/Vengeance|vengeance]]_ when the strands of fate are twisted and abused by lesser beings. Worshiped as gods by some, the norns do little to discourage this veneration.

A _norn_ stands 14 feet tall and weighs 800 pounds.