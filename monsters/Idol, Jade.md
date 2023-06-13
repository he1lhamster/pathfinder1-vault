---
cssclass: [monsters]
title1: Idol, Jade
desc_short: Masterfully carved, this elegant jade figurine stands no more than a hand's
  breadth tall, yet its delicate limbs and incredible details bear all the features
  of a seductive maiden cast in miniature.
title2: Jade
CR: 4
sources:
- name: 'Pathfinder #27: What Lies in Dust'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8b8h
XP: 1200
alignment: N
size: Diminutive
type: construct
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: tainted air
  radius: 30
AC:
  AC: 20
  touch: 17
  flat_footed: 16
  components:
    armor: 2
    dex: 3
    size: 4
HP:
  HP: 22
  long: 4d10
saves:
  fort: 1
  ref: 6
  will: 2
DR:
- amount: 5
  weakness: bludgeoning and magic
immunities:
- cold
- construct traits
- electricity
- fire
speeds:
  base: 10
attacks:
  melee:
  - - text: 2 slams +5 (1d2-3)
      entries:
      - - damage: 1d2-3
      count: 2
      attack: slams
      bonus:
      - 5
  ranged:
  - - text: sliver +10 (1d2-3)
      entries:
      - - damage: 1d2-3
      attack: sliver
      bonus:
      - 10
  special:
  - jade breath
  - venom affinity
space: 1
reach: 0
spell_like_abilities:
  entries:
  - name: delay poison
    source: default
    freq: At will
  - name: detect poison
    source: default
    freq: At will
  - name: pass without trace
    source: default
    freq: 3/day
  - name: summon monster I
    source: default
    freq: 3/day
    other: viper only
  - name: neutralize poison
    source: default
    freq: 1/day
  - name: poison
    source: default
    freq: 1/day
    DC: 16
  - name: true strike
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
ability_scores:
  STR: 4
  DEX: 17
  CON:
  INT: 11
  WIS: 13
  CHA: 14
BAB: 4
CMB: 3
CMD: 10
feats:
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Perception: 5
  Stealth: 19
  _racial_mods:
    Stealth:
      amid jade objects: 4
languages:
- understands creator's language (cannot speak)
special_qualities:
- inanimate
- share abilities
ecology:
  environment: any
  organization: solitary
  treasure_type: incidental
special_abilities:
  Jade Breath (Su): |-
    As a standard action once every 1d4 rounds, a jade idol can exhale a breath of gas that unerringly snakes its way through the air to envelop a single target within 50 feet. If the target is reduced to 0 Dexterity, it is instantly turned to jade-colored stone. Inanimate corpses targeted by this attack are instantly turned to stone, but benefit from the perpetual effects of gentle repose while petrified. The spell stone to flesh reverses this effect.

    Poison-inhaled; save DC 14; frequency 1/ round for 6 rounds; effect 1d4 Dexterity damage; cure 2 consecutive saves. The save DC is Charisma-based.
  Tainted Air (Su): All creatures within 30 feet of a jade idol take a -2 penalty
    on saving throws against poison. The effect lasts as long as a creature remains
    within the jade idol's aura.
  Venom Affinity (Su): Any poisonous animal or vermin that comes within 10 feet of
    a jade idol or a creature bearing the idol must make a DC 14 Will save or be charmed
    as per the spell charm animal. Beasts affected by this effect remain charmed for
    10 minutes, obeying either the idol's will or its bearer's. Any creature that
    makes its save cannot be affected by the same jade idol's venom affinity for the
    next 24 hours. The save DC is Charisma-based.
desc_long: From the moldering depths of the Sodden Lands to far away Tian Xia, jade
  idols stand watch over sacred temples, royal tombs, the monuments of powerful ancients,
  and the hidden lairs of plotting assassins and cruel wizards. Crafted primarily
  to serve as unassuming killers, jade idols possess unnatural patience, waiting for
  weeks, months, or even years for the opportune time when they might be delivered
  into their victims' hands and forgotten before striking. Jade idols are also particularly
  valued for their ability to transform living flesh into a stone similar in appearance
  to jade, but far more brittle and ultimately worthless (a DC 14 Appraise or Knowledge
  [nature] check reveals the difference). Regardless of the stone's value, the tombs
  of many forgotten dynasties bear small legions of jade idols, left by their departed
  masters to keep the residents preserved in lifeless jade for all time.

---

# Idol, Jade
Masterfully carved, this elegant jade figurine stands no more than a hand’s breadth tall, yet its delicate limbs and incredible details bear all the features of a seductive maiden cast in miniature.
**Source** Pathfinder #27: What Lies in Dust pg. 82
**XP** 1,200

N Diminutive construct
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5
**Aura** tainted air (30 ft.)

##### Defense

**AC** 20, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 armor, +3 Dex, +4 size)
**hp** 22 (4d10)
**Fort** +1, **Ref** +6, **Will** +2
**DR** 5/bludgeoning and magic; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_, electricity, fire

##### Offense
**Speed** 10 ft.
**Melee** 2 slams +5 (1d2-3)
**Ranged** sliver +10 (1d2-3)
**Space** 1 ft., **Reach** 0 ft.
**Special Attacks** jade breath, venom affinity
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th)
At will — _[[spells/Delay Poison|delay poison]]_, _[[spells/Detect Poison|detect poison]]_*
3/day — _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Summon Monster I|summon monster I]]_ (viper only)
1/day — _[[spells/Neutralize Poison|neutralize poison]]_, poison (DC 16), _[[spells/True Strike|true strike]]_

##### Statistics
**Str** 4, **Dex** 17, **Con** —, **Int** 11, **Wis** 13, **Cha** 14
**Base Atk** +4; **CMB** +3; **CMD** 10
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Perception +5, Stealth +19; **Racial Modifiers** +4 Stealth amid jade objects
**Languages** understands creator's language (cannot speak)
**SQ** inanimate, share abilities

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Jade Breath (Su)** As a standard action once every 1d4 rounds, a jade idol can exhale a breath of gas that unerringly snakes its way through the air to envelop a single target within 50 feet. If the target is reduced to 0 Dexterity, it is instantly turned to jade-colored stone. Inanimate corpses targeted by this attack are instantly turned to stone, but benefit from the perpetual effects of _[[spells/Gentle Repose|gentle repose]]_ while _[[conditions/Petrified|petrified]]_. The spell _[[spells/Stone to Flesh|stone to flesh]]_ reverses this effect.

Poison—inhaled; save DC 14; frequency 1/ round for 6 rounds; effect 1d4 Dexterity damage; cure 2 consecutive saves. The save DC is Charisma-based.

**Tainted Air (Su)** All creatures within 30 feet of a jade idol take a –2 penalty on saving throws against poison. The effect lasts as long as a creature remains within the jade idol’s aura.

**Venom Affinity (Su)** Any poisonous animal or vermin that comes within 10 feet of a jade idol or a creature bearing the idol must make a DC 14 Will save or be charmed as per the spell _[[spells/Charm Animal|charm animal]]_. Beasts affected by this effect remain charmed for 10 minutes, obeying either the idol’s will or its bearer’s. Any creature that makes its save cannot be affected by the same jade idol’s venom affinity for the next 24 hours. The save DC is Charisma-based.

##### Description

From the moldering depths of the Sodden Lands to far away Tian Xia, jade idols stand watch over _[[items/Weapon Magic Abilities/Sacred|sacred]]_ temples, royal tombs, the monuments of powerful ancients, and the hidden lairs of plotting assassins and _[[items/Weapon Magic Abilities/Cruel|cruel]]_ wizards. Crafted primarily to serve as unassuming killers, jade idols possess unnatural patience, waiting for weeks, months, or even years for the opportune time when they might be delivered into their victims’ hands and forgotten before striking. Jade idols are also particularly valued for their ability to transform living flesh into a stone similar in appearance to jade, but far more brittle and ultimately worthless (a DC 14 Appraise or Knowledge [nature] check reveals the difference). Regardless of the stone’s value, the tombs of many forgotten dynasties bear small legions of jade idols, left by their departed masters to keep the residents preserved in lifeless jade for all time.