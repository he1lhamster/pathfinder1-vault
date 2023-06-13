---
cssclass: [monsters]
title1: Drow, Drow Priest
title2: Drow Priest
CR: 5
sources:
- name: Monster Codex
  page: 36
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Drow
classes:
- noble cleric 5
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 5
senses:
  darkvision: 120
AC:
  AC: 24
  touch: 13
  flat_footed: 23
  components:
    armor: 9
    deflection: 2
    dex: 1
    shield: 2
HP:
  HP: 31
  long: 5d8+5
saves:
  fort: 5
  ref: 2
  will: 8
  other: +2 vs. enchantment
immunities:
- sleep
SR: 16
weaknesses:
- light blindness
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk flail +4 (1d8)
      entries:
      - - damage: 1d8
      attack: mwk flail
      bonus:
      - 4
  special:
  - channel negative energy 7/day (DC 14, 3d6)
  - hand of the acolyte (7/day)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - name: faerie fire
    source: default
    freq: At will
  - name: feather fall
    source: default
    freq: At will
  - name: levitate
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: 1/day
  - name: divine favor
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 15
  - name: touch of evil
    source: domain
    freq: 7/day
    other: 2 rounds
  sources:
  - name: default
    CL: 5
  - name: domain
    CL: 5
    concentration: 9
spells:
  entries:
  - superscripts:
    - UC
    name: chain of perdition
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: dispel magic
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: evil only
  - superscripts:
    - UM
    name: dread bolt
    source: Cleric
    level: 2
    DC: 16
  - name: hold person
    source: Cleric
    level: 2
    DC: 16
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    DC: 15
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 14
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 9
    slots:
      0: at-will
    domains:
    - evil
    - magic
tactics:
  Before Combat: The priest casts shield of faith on herself. She prefers to let her
    minions do the fighting, and has them stand between her and any approaching foes.
  During Combat: The priest channels negative energy at groups of foes and uses single-target
    spells against her most dangerous opponent (typically starting with hold person
    so her allies can surround the hapless target).
  Base Statistics: Without shield of faith, the drow's statistics are AC 22, touch
    11, flat-footed 21.
ability_scores:
  STR: 10
  DEX: 12
  CON: 12
  INT: 14
  WIS: 18
  CHA: 15
BAB: 3
CMB: 3
CMD: 14
feats:
- name: Combat Casting
- name: Extra Channel
- name: Improved Initiative
skills:
  Bluff: 3
  Diplomacy: 6
  Intimidate: 7
  Knowledge (arcana): 6
  Knowledge (history): 6
  Knowledge (nobility): 6
  Knowledge (religion): 10
  Perception: 11
  Sense Motive: 12
languages:
- Abyssal
- Common
- Elven
- Undercommon
special_qualities:
- poison use
gear:
  combat:
  - potion of invisibility
  - potion of owl's wisdom
  - scroll of cure moderate wounds
  - scroll of cure serious wounds
  - scroll of magic weapon
  other:
  - mwk full plate
  - heavy steel shield
  - mwk flail
  - spell component pouch
  - 167 gp
ecology:
  environment: underground
desc_long: Having manipulated and assassinated her way into the middle ranks of her
  church, the drow priest uses her powers to eliminate rivals as she continues her
  climb. The drow religious orders are just as cutthroat as every other aspect of
  drow society. Their priests see the ability to out-scheme one's foes as a sign of
  the unholy favor of their demonic patrons.

---

# Drow, Drow Priest

**Source** Monster Codex pg. 36
**XP** 1,600
_[[monsters/Drow|Drow]]_ noble _[[classes/Cleric|cleric]]_ 5
CE Medium humanoid (elf)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +11

##### Defense

**AC** 24, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+9 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +2 _[[spells/Shield|shield]]_)
**hp** 31 (5d8+5)
**Fort** +5, **Ref** +2, **Will** +8; +2 vs. enchantment
**Immune** sleep; **SR** 16
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk flail +4 (1d8)
**Special Attacks** channel negative energy 7/day (DC 14, 3d6), hand of the _[[npcs/Acolyte|acolyte]]_ (7/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th)
Constant—_[[spells/Detect Magic|detect magic]]_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Levitate|levitate]]_
1/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Suggestion|suggestion]]_ (DC 15)
**Domain _Spell-Like Abilities_** (CL 5th; concentration +9)
7/day—_[[feats/Touch Of Evil|touch of evil]]_ (2 rounds)
**_Cleric_ Spells Prepared **(CL 5th; concentration +9)
3rd—_[[spells/Chain of Perdition|chain of perdition]]_, _dispel magic_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (evil only), _[[spells/Dread Bolt|dread bolt]]_ (DC 16), _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Murderous Command|murderous command]]_ (DC 15), _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _detect magic_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Evil, Magic

### Tactics

**Before Combat** The priest casts _shield of faith_ on herself. She prefers to let her minions do the fighting, and has them stand between her and any approaching foes.
 **During Combat** The priest channels negative energy at groups of foes and uses single-target spells against her most dangerous opponent (typically starting with _hold person_ so her allies can surround the hapless target).
 **Base Statistics** Without _shield of faith_, the _drow_’s statistics are **AC** 22, touch 11, _flat-footed_ 21.

##### Statistics
**Str** 10, **Dex** 12, **Con** 12, **Int** 14, **Wis** 18, **Cha** 15
**Base Atk** +3; **CMB** +3; **CMD** 14
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Bluff +3, Diplomacy +6, Intimidate +7, Knowledge (arcana) +6, Knowledge (history) +6, Knowledge (nobility) +6, Knowledge (religion) +10, Perception +11, Sense Motive +12
**Languages** Abyssal, Common, Elven, Undercommon
**SQ** poison use
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, potion of owl’s wisdom, scroll of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _[[spells/Magic Weapon|magic weapon]]_; **Other Gear** mwk _[[items/Armor/Full plate|full plate]]_, _[[items/Shield/Heavy steel shield|heavy steel shield]]_, mwk flail, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 167 gp

##### Ecology

**Environment** underground

##### Description

Having manipulated and assassinated her way into the middle ranks of her church, the _drow_ priest uses her powers to eliminate rivals as she continues her _[[universal monster rules/Climb|climb]]_. The _drow_ religious orders are just as cutthroat as every other aspect of _drow_ society. Their priests see the ability to out-scheme one’s foes as a sign of the _[[items/Weapon Magic Abilities/Unholy|unholy]]_ favor of their demonic patrons.