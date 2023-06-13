---
cssclass: [monsters]
title1: Charau-ka, Devotee of the Ravener King
desc_short: Clad in bloodstains, ivory fetishes, and animal hides, this apelike priest's
  regalia speaks to the horrible powers it serves.
title2: Devotee of the Ravener King
CR: 7
sources:
- name: Inner Sea Monster Codex
  page: 14
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 3200
race: Charau-ka
classes:
- 'cleric of Angazhan 5 (Pathfinder Campaign Setting: The Inner Sea World Guide 308)'
alignment: CE
size: Small
type: humanoid
subtypes:
- charau-ka
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 22
  touch: 14
  flat_footed: 20
  components:
    armor: 5
    deflection: 1
    dex: 2
    natural: 3
    size: 1
HP:
  HP: 65
  long: 3d8+5d8+29
  HD: 8
saves:
  fort: 8
  ref: 6
  will: 8
speeds:
  base: 20
  climb: 30
attacks:
  melee:
  - - text: +1 spear +8 (1d6+2/×3)
      entries:
      - - damage: 1d6+2
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 8
    - text: bite +2 (1d3+1)
      entries:
      - - damage: 1d3+1
      attack: bite
      bonus:
      - 2
  ranged:
  - - text: rock +9 (1d4+1, 19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: rock
      bonus:
      - 9
  special:
  - channel negative energy 6/day (DC 15, 3d6)
  - shrieking frenzy
  - thrown-weapon mastery
spell_like_abilities:
  entries:
  - name: touch of chaos
    source: default
    freq: 6/day
  - name: touch of evil
    source: default
    freq: 6/day
    other: 2 rounds
  sources:
  - name: default
    CL: 5
    concentration: 8
spells:
  entries:
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 16
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 16
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
  - name: desecrate
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 15
  - name: bane
    source: Cleric
    level: 1
    DC: 14
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 2
  - name: magic stone
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 8
    slots:
      0: at-will
    domains:
    - chaos
    - evil
ability_scores:
  STR: 13
  DEX: 15
  CON: 16
  INT: 8
  WIS: 16
  CHA: 16
BAB: 5
CMB: 5
CMD: 18
feats:
- name: Combat Casting
- name: Improved Natural Armor
- name: Point-Blank Shot
- name: Selective Channeling
- is_bonus: true
  name: Throw Anything
skills:
  Climb: 11
  Knowledge (religion): 4
  Perception: 4
  Spellcraft: 6
  Stealth: 8
  _racial_mods:
    Stealth:
      _: 4
languages:
- Abyssal
- Polyglot
gear:
  combat:
  - scroll of cure moderate wounds
  - scrolls of invisibility (2)
  other:
  - +1 hide armor
  - +1 spear
  - ring of protection +1
  - ivory holy symbol worth 30 gp
  - mwk manacles
ecology:
  environment: warm forests
desc_long: |-
  The clergy of Angazhan-if such a word applies to the jostling, bickering agents of the demon lord of beasts-perform numerous malicious rites and rituals throughout Usaro, continually working through the steady river of slaves that flows into the city. Devotees navigate the sticky, blood-slick temple stairs to march sacrifices to the waiting altars, or else break off to mingle with their charau-ka flock, distributing blessings and beatings on their demon lord's behalf. Those who earn the Gorilla King's favor become cherished advisors, attending to the living god personally, but the fickle temperament of their sovereign means few devotees hold his good will for long.

   Angazhan's clerics are expert saboteurs and provocateurs. When traveling with other charau-ka, they throw foes into disarray before their charau-ka followers above let loose volleys of death.

   Ostracized devotees of the Ravener King wander the jungles and spread the gifts of the Angazhan to re-establish their worth. They may encourage growth in the wilderness, blight the croplands around Mwangi villages, and carefully husband wild monsters, forcing the wild world into bloody competition with human settlements. Such wild hermits exchange a cleric of Angazhan's normal spells for ones to help them contain, augment, and direct the natural world, using stone shape and glyph of warding to fashion animal traps, sanctuary to move unharmed among wild beasts, and bear's endurance and bull's strength to augment their vile creations before launching them into combat.

   Every devotee of the Ravener King journeys through the Mwangi Expanse at least once every few months in search of victims transformed into trees by tobongos (Pathfinder Campaign Setting: Heart of the Jungle 61). Using rituals revealed by the Gorilla King, devotees bathe these new plants with ape blood, transforming them into corrupted fetishes capable of draining the life force from others. Angazhan is said to occasionally look upon the realm and reward the most productive creators of these chaotic totems of decay with his fiendish blessing. The charau-ka's already fiercely territorial nature rises to unbridled levels when tribes compete to gain their god's favor.

---

# Charau-ka, Devotee of the Ravener King
Clad in bloodstains, ivory fetishes, and animal hides, this apelike priest’s regalia speaks to the horrible powers it serves.
**Source** Inner Sea Monster Codex pg. 14
**XP** 3,200
_[[monsters/Charau-ka|Charau-ka]]_ _[[classes/Cleric|cleric]]_ of Angazhan 5 (Pathfinder Campaign Setting: The Inner Sea World Guide 308)
CE Small humanoid (_charau-ka_)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +4

##### Defense

**AC** 22, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 armor, +1 deflection, +2 Dex, +3 natural, +1 size)
**hp** 65 (8 HD; 3d8+5d8+29)
**Fort** +8, **Ref** +6, **Will** +8

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +8 (1d6+2/×3), bite +2 (1d3+1)
**Ranged** rock +9 (1d4+1, 19–20)
**Special Attacks** channel negative energy 6/day (DC 15, 3d6), shrieking frenzy, thrown-weapon mastery
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
6/day—touch of chaos
6/day—_[[feats/Touch Of Evil|touch of evil]]_ (2 rounds)
**_Cleric_ Spells Prepared **(CL 5th; concentration +8)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), blindness/deafness (DC 16), _[[spells/Magic Circle against Good|magic circle against good]]_
2nd—aid, _[[spells/Align Weapon|align weapon]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Silence|silence]]_ (DC 15)
1st—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Magic Stone|magic stone]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Purify Food and Drink|purify food and drink]]_
**D** domain spell; **Domains** Chaos, Evil

##### Statistics
**Str** 13, **Dex** 15, **Con** 16, **Int** 8, **Wis** 16, **Cha** 16
**Base Atk** +5; **CMB** +5; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** _Climb_ +11, Knowledge (religion) +4, Perception +4, Spellcraft +6, Stealth +8; **Racial Modifiers** +4 Stealth
**Languages** Abyssal, Polyglot
**Combat Gear** scroll of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scrolls of _[[spells/Invisibility|invisibility]]_ (2); **Other Gear** +1 _[[items/Armor/Hide armor|hide armor]]_, +1 _spear_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, ivory holy symbol worth 30 gp, mwk manacles

##### Ecology

**Environment** warm forests

##### Description

The clergy of Angazhan—if such a word applies to the jostling, bickering agents of the demon lord of beasts—perform numerous malicious rites and rituals throughout Usaro, continually working through the steady river of slaves that flows into the city. Devotees navigate the _[[items/Weapon Magic Abilities/Sticky|sticky]]_, blood-slick temple stairs to march sacrifices to the waiting altars, or else break off to mingle with their _charau-ka_ flock, distributing blessings and beatings on their demon lord’s behalf. Those who earn the Gorilla _[[npcs/King|King]]_’s favor become cherished advisors, attending to the living god personally, but the fickle temperament of their sovereign means few devotees hold his good will for long.

Angazhan’s clerics are expert saboteurs and provocateurs. When traveling with other _charau-ka_, they throw foes into disarray before their _charau-ka_ followers above let loose volleys of death.

Ostracized devotees of the Ravener _King_ wander the jungles and spread the gifts of the Angazhan to re-establish their worth. They may encourage growth in the wilderness, _[[spells/Blight|blight]]_ the croplands around Mwangi villages, and carefully husband wild monsters, forcing the wild world into bloody competition with human settlements. Such wild hermits exchange a _cleric_ of Angazhan’s normal spells for ones to help them contain, augment, and direct the natural world, using _[[spells/Stone Shape|stone shape]]_ and _[[spells/Glyph Of Warding|glyph of warding]]_ to fashion animal traps, _[[spells/Sanctuary|sanctuary]]_ to move unharmed among wild beasts, and bear’s _[[feats/Endurance|endurance]]_ and bull’s strength to augment their vile creations before launching them into combat.

Every devotee of the Ravener _King_ journeys through the Mwangi Expanse at least once every few months in search of victims transformed into trees by tobongos (Pathfinder Campaign Setting: Heart of the Jungle 61). Using rituals revealed by the Gorilla _King_, devotees bathe these new plants with ape blood, transforming them into corrupted fetishes capable of draining the life force from others. Angazhan is said to occasionally look upon the realm and reward the most productive creators of these chaotic totems of decay with his fiendish blessing. The _charau-ka_’s already fiercely territorial nature rises to unbridled levels when tribes compete to gain their god’s favor.