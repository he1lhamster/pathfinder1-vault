---
cssclass: [monsters]
title1: Troglodyte, Troglodyte Tyrant
title2: Troglodyte Tyrant
CR: 10
sources:
- name: Monster Codex
  page: 219
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 9600
race: Enlightened
classes:
- troglodyte cleric 7
- fighter 2 (see page 212)
alignment: CE
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 2
senses:
  darkvision: 90
auras:
- name: stench
  radius: 30
  DC: 21
  duration: 10 rounds
AC:
  AC: 24
  touch: 10
  flat_footed: 24
  components:
    armor: 8
    natural: 6
HP:
  HP: 135
  long: 9d8+2d10+84
  HD: 11
saves:
  fort: 17
  ref: 6
  will: 10
  will_other: +1 vs. fear
defensive_abilities:
- bravery +1
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 battleaxe +15/+10 (1d8+6/×3)
      entries:
      - - damage: 1d8+6
          crit_multiplier: 3
      attack: +1 battleaxe
      bonus:
      - 15
      - 10
    - text: bite +8 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: bite
      bonus:
      - 8
    - text: claw +8 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: claw
      bonus:
      - 8
  - - text: bite +13 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 13
  ranged:
  - - text: javelin +10/+5 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: javelin
      bonus:
      - 10
      - 5
  special:
  - channel negative energy 5/day (DC 15, 4d6)
  - fury of the Abyss (+3, 8/day)
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 8/day
    other: '+3'
  sources:
  - name: default
    CL: 7
    concentration: 12
spells:
  entries:
  - name: divine power
    source: Cleric
    level: 4
  - name: mark of the reptile god
    source: Cleric
    level: 4
    DC: 19
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - name: prayer
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: rage
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - name: amplify stench
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: bull's strength
    source: Cleric
    level: 2
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 3
  - name: entropic shield
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: protection from good
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
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 7
    concentration: 12
    slots:
      0: at-will
    domains:
    - evil (demon subdomain)
    - strength
tactics:
  Before Combat: The tyrant casts amplify stench on herself and bull's strength on
    a trusted ally. She then uses her wand of bear's endurance.
  During Combat: When combat begins, the tyrant casts rage on her allies-though she
    doesn't concentrate on it. She then casts divine power on herself if the enemies
    haven't reached her yet. She casts mark of the reptile god and bestow curse on
    strong enemies, then fights in melee.
  Base Statistics: Without amplify stench and bear's endurance, the tyrant's statistics
    are Aura stench (30 ft., DC 19, 10 rounds); hp 113; Fort +15; Con 18.
ability_scores:
  STR: 20
  DEX: 15
  CON: 22
  INT: 14
  WIS: 20
  CHA: 14
BAB: 8
CMB: 13
CMD: 25
feats:
- name: Ability Focus (stench)
- name: Combat Casting
- name: Lightning Reflexes
- name: Power Attack
- name: Quick Draw
- name: Selective Channeling
- name: Toughness
- name: Weapon Focus (battleaxe)
skills:
  Intimidate: 13
  Knowledge (planes): 11
  Knowledge (religion): 13
  Perception: 13
  Sense Motive: 16
  Spellcraft: 11
  Stealth: 0
    in rocky areas: 4
languages:
- Abyssal
- Draconic
- Undercommon
gear:
  combat:
  - potions of cure moderate wounds (2)
  - wand of bear's endurance (6 charges)
  other:
  - mwk half-plate
  - +1 battleaxe
  - javelins (6)
  - belt of giant strength +2
  - headband of inspired wisdom +2
  - gold crown set with jet and bloodstones (worth 500 gp)
  - 44 gp
ecology:
  environment: any underground
desc_long: Troglodyte tyrants come from the enlightened troglodytes who live far deeper
  underground than common troglodytes. Stronger, more intelligent, and longer-lived
  than their degenerate kin, they find it easy to assert dominance over tribes of
  normal troglodytes. Warlike in the extreme, tyrants are seasoned veterans of numerous
  military campaigns and they are expert tacticians, willing to sacrifice large numbers
  of troglodyte warriors to probe an enemy's strengths and weaknesses.

---

# Troglodyte, Troglodyte Tyrant

**Source** Monster Codex pg. 219
**XP** 9,600
Enlightened _[[monsters/Troglodyte|troglodyte]]_ _[[classes/Cleric|cleric]]_ 7/fighter 2 (see page 212)
CE Medium humanoid (reptilian)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft.; Perception +13
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 21, 10 rounds)

##### Defense

**AC** 24, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+8 armor, +6 natural)
**hp** 135 (11 HD; 9d8+2d10+84)
**Fort** +17, **Ref** +6, **Will** +10 (+1 vs. _[[universal monster rules/Fear|fear]]_)
**Defensive Abilities** bravery +1

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Battleaxe|battleaxe]]_ +15/+10 (1d8+6/×3), bite +8 (1d4+2), claw +8 (1d4+2) or bite +13 (1d4+5), 2 claws +13 (1d4+5)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +10/+5 (1d6+5)
**Special Attacks** channel negative energy 5/day (DC 15, 4d6), fury of the Abyss (+3, 8/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
8/day—strength surge (+3)
**_Cleric_ Spells Prepared **(CL 7th; concentration +12)
4th—_[[spells/Divine Power|divine power]]_, _[[spells/Mark Of The Reptile God|mark of the reptile god]]_ (DC 19), _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Prayer|prayer]]_, _[[spells/Rage|rage]]_, _[[spells/Searing Light|searing light]]_
2nd—_[[spells/Amplify Stench|amplify stench]]_, bull’s strength, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_ (3), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, stabilize
**D** domain spell; **Domains** Evil (Demon subdomain), Strength

### Tactics

**Before Combat** The tyrant casts _amplify stench_ on herself and bull’s strength on a trusted ally. She then uses her wand of bear’s _[[feats/Endurance|endurance]]_.
 **During Combat** When combat begins, the tyrant casts _rage_ on her allies—though she doesn’t concentrate on it. She then casts _divine power_ on herself if the enemies haven’t reached her yet. She casts _mark of the reptile god_ and _bestow curse_ on strong enemies, then fights in melee.
 **Base Statistics** Without _amplify stench_ and bear’s _endurance_, the tyrant’s statistics are **Aura **_stench_ (30 ft., DC 19, 10 rounds); **hp **113; **Fort **+15; **Con **18.

##### Statistics
**Str** 20, **Dex** 15, **Con** 22, **Int** 14, **Wis** 20, **Cha** 14
**Base Atk** +8; **CMB** +13; **CMD** 25
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_stench_), _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_battleaxe_)
**Skills** Intimidate +13, Knowledge (planes) +11, Knowledge (religion) +13, Perception +13, Sense Motive +16, Spellcraft +11, Stealth +0 (+4 in rocky areas)
**Languages** Abyssal, Draconic, Undercommon
**Combat Gear** potions of _cure moderate wounds_ (2), wand of bear’s _endurance_ (6 charges); **Other Gear** mwk _[[items/Armor/Half-plate|half-plate]]_, +1 _battleaxe_, javelins (6), _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, gold crown set with _[[universal monster rules/Jet|jet]]_ and bloodstones (worth 500 gp), 44 gp

##### Ecology

**Environment** any underground

##### Description

_Troglodyte_ tyrants come from the enlightened troglodytes who live far deeper underground than common troglodytes. Stronger, more intelligent, and longer-lived than their degenerate kin, they find it easy to assert dominance over tribes of normal troglodytes. Warlike in the extreme, tyrants are seasoned veterans of numerous military campaigns and they are expert tacticians, willing to _[[spells/Sacrifice|sacrifice]]_ large numbers of _troglodyte_ warriors to probe an enemy’s strengths and weaknesses.