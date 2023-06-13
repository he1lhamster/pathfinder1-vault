---
cssclass: [monsters]
title1: Duergar, Duergar High Priest
title2: Duergar High Priest
CR: 12
sources:
- name: Monster Codex
  page: 51
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Duergar
classes:
- cleric 13
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 0
senses:
  darkvision: 120
AC:
  AC: 31
  touch: 14
  flat_footed: 31
  components:
    armor: 9
    deflection: 4
    natural: 8
HP:
  HP: 101
  long: 13d8+39
saves:
  fort: 10
  ref: 4
  will: 13
  other: +2 vs. spells
immunities:
- paralysis
- phantasms
- poison
weaknesses:
- light sensitivity
speeds:
  base: 20
  other_semicolon: freedom of movement
attacks:
  melee:
  - - text: +1 heavy mace +12/+7 (1d8+2)
      entries:
      - - damage: 1d8+2
      attack: +1 heavy mace
      bonus:
      - 12
      - 7
  ranged:
  - - text: mwk light crossbow +10 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 10
  special:
  - channel negative energy 4/day (DC 17, 7d6)
spell_like_abilities:
  entries:
  - name: enlarge person
    source: default
    freq: 1/day
    other: self only
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  - name: ironskin
    source: default
    freq: 1/day
  - name: copycat
    source: domain
    freq: 8/day
    other: 13 rounds
  - name: dazing touch
    source: domain
    freq: 8/day
  - name: charming smile
    source: domain
    freq: At will
    other: 13 rounds/day
    DC: 16
  - name: master's illusion
    source: domain
    freq: At will
    other: 13 rounds/day
    DC: 21
  sources:
  - name: default
    CL: 13
    concentration: 14
  - name: domain
    CL: 13
    concentration: 18
spells:
  entries:
  - name: blasphemy
    source: Cleric
    level: 7
    DC: 22
  - is_domain_spell: true
    name: insanity
    source: Cleric
    level: 7
    DC: 22
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 21
  - name: harm
    source: Cleric
    level: 6
    DC: 21
  - is_domain_spell: true
    name: mislead
    source: Cleric
    level: 6
    DC: 21
  - name: break enchantment
    source: Cleric
    level: 5
    DC: 20
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: charm monster
    source: Cleric
    level: 5
    DC: 20
  - name: slay living
    source: Cleric
    level: 5
    DC: 20
  - name: wall of stone
    source: Cleric
    level: 5
    DC: 20
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: heroism
    source: Cleric
    level: 4
  - name: spell immunity
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: stone shape
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: suggestion
    source: Cleric
    level: 3
    DC: 18
  - name: wind wall
    source: Cleric
    level: 3
  - name: control vermin
    source: Cleric
    level: 2
    DC: 17
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 17
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 17
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 16
  - is_domain_spell: true
    name: charm person
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: shield of faith
    source: Cleric
    level: 1
    count: 2
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
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
    CL: 13
    concentration: 18
    slots:
      0: at-will
    domains:
    - charm
    - trickery
tactics:
  Before Combat: The high priest casts freedom of movement, ironskin, and shield of
    faith.
  During Combat: The high priest first provides magical support, then uses enlarge
    person and enters combat.
  Base Statistics: When not under the effects of freedom of movement, ironskin, and
    shield of faith, the high priest's statistics are AC 22, touch 11, flat-footed
    22; Speed no freedom of movement.
ability_scores:
  STR: 13
  DEX: 10
  CON: 14
  INT: 8
  WIS: 20
  CHA: 12
BAB: 9
CMB: 10
CMD: 21
CMD_other: 25 vs. bull rush or trip
feats:
- name: Combat Casting
- name: Gray Dwarf Magic (ironskin)
- superscripts:
  - ARG
  name: Giant Steps
- name: Innate Flexibility
- name: Tough as Iron
- name: Toughness
- name: Weapon Focus (heavy mace)
skills:
  Knowledge (religion): 8
  Perception: 18
  Spellcraft: 9
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- slow and steady
- stability
gear:
  combat:
  - scroll of cure critical wounds
  other:
  - +3 chainmail
  - +1 heavy mace
  - mwk light crossbow with 20 bolts
  - amulet of natural armor +2
  - headband of inspired wisdom +2
  - ring of protection +1
  - silver unholy symbol
  - spell component pouch
  - 321 gp
ecology:
  environment: any underground
desc_long: Because religious doctrine is so influential in duergar society, common
  duergar treat high priests like the voice of their god, trusting their wisdom in
  all things. A high priest is effectively the primary lawmaker for her clan.

---

# Duergar, Duergar High Priest

**Source** Monster Codex pg. 51
**XP** 19,200
_[[monsters/Duergar|Duergar]]_ _[[classes/Cleric|cleric]]_ 13

LE Medium humanoid (dwarf)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +18

##### Defense

**AC** 31, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+9 armor, +4 _[[spells/Deflection|deflection]]_, +8 natural)
**hp** 101 (13d8+39)
**Fort** +10, **Ref** +4, **Will** +13; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.; _[[spells/Freedom of Movement|freedom of movement]]_
**Melee** +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +12/+7 (1d8+2)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +10 (1d8/19–20)
**Special Attacks** channel negative energy 4/day (DC 17, 7d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +14)
1/day—_[[spells/Enlarge Person|enlarge person]]_ (self only), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Ironskin|ironskin]]_
**Domain _Spell-Like Abilities_** (CL 13th; concentration +18)
8/day—copycat (13 rounds), dazing touch
At will—charming smile (13 rounds/day, DC 16), master’s illusion (13 rounds/day, DC 21)
**_Cleric_ Spells Prepared **(CL 13th; concentration +18)
7th—_[[spells/Blasphemy|blasphemy]]_ (DC 22), _[[spells/Insanity|insanity]]_ (DC 22)
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 21), _[[spells/Harm|harm]]_ (DC 21), _[[spells/Mislead|mislead]]_ (DC 21)
5th—_[[spells/Break Enchantment|break enchantment]]_ (DC 20), _[[spells/Breath Of Life|breath of life]]_, _[[spells/Charm Monster|charm monster]]_ (DC 20), _[[spells/Slay Living|slay living]]_ (DC 20), _[[spells/Wall Of Stone|wall of stone]]_ (DC 20)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Divine Power|divine power]]_, _freedom of movement_, _[[spells/Heroism|heroism]]_, _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Control Vermin|control vermin]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (2, DC 17), _invisibility_, _[[spells/Sound Burst|sound burst]]_ (DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 16), _[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Doom|doom]]_ (DC 16), _[[spells/Shield Of Faith|shield of faith]]_ (2)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_
**D** domain spell; **Domains** Charm, Trickery

### Tactics

**Before Combat** The high priest casts _freedom of movement_, _ironskin_, and _shield of faith_.
 **During Combat** The high priest first provides magical support, then uses _enlarge person_ and enters combat.
 **Base Statistics** When not under the effects of _freedom of movement_, _ironskin_, and _shield of faith_, the high priest’s statistics are **AC **22, touch 11, _flat-footed_ 22; **Speed **no _freedom of movement_.

##### Statistics
**Str** 13, **Dex** 10, **Con** 14, **Int** 8, **Wis** 20, **Cha** 12
**Base Atk** +9; **CMB** +10; **CMD** 21 (25 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Gray Dwarf Magic|Gray Dwarf Magic]]_ (_ironskin_), _[[feats/Giant Steps|Giant Steps]]_, _[[feats/Innate Flexibility|Innate Flexibility]]_, _[[feats/Tough As Iron|Tough as Iron]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_heavy mace_)
**Skills** Knowledge (religion) +8, Perception +18, Spellcraft +9
**Languages** Common, Dwarven, Undercommon
**SQ** _[[spells/Slow|slow]]_ and steady, stability
**Combat Gear** scroll of _cure critical wounds_; **Other Gear** +3 _[[items/Armor/Chainmail|chainmail]]_, +1 _heavy mace_, mwk _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 321 gp

##### Ecology

**Environment** any underground

##### Description

Because religious doctrine is so influential in _duergar_ society, common _duergar_ treat high priests like the voice of their god, trusting their wisdom in all things. A high priest is effectively the primary lawmaker for her clan.