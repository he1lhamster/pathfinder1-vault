---
cssclass: [monsters]
title1: Serpentfolk, Serpentfolk Illusionist
title2: Serpentfolk Illusionist
CR: 8
sources:
- name: Monster Codex
  page: 204
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Advanced
classes:
- serpentfolk illusionist 4
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 21
  touch: 17
  flat_footed: 15
  components:
    deflection: 1
    dex: 6
    natural: 4
HP:
  HP: 99
  long: 5d10+4d6+58
  HD: 9
saves:
  fort: 7
  ref: 11
  will: 9
immunities:
- mind-affecting effects
- paralysis
- poison
SR: 19
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +8/+3 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 8
      - 3
    - text: bite +2 (1d6 plus poison)
      entries:
      - - damage: 1d6
        - effect: poison
      attack: bite
      bonus:
      - 2
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
    DC: 15
    other: humanoid form only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 15
  - name: blur
    source: default
    freq: 1/day
  - name: dominate person
    source: default
    freq: 1/day
    DC: 19
  - name: major image
    source: default
    freq: 1/day
    DC: 17
  - name: mirror image
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 17
  - name: blinding ray
    source: arcane school
    freq: 9/day
  sources:
  - name: default
    CL: 4
    concentration: 8
  - name: arcane school
    CL: 4
    concentration: 10
spells:
  entries:
  - name: blindness/deafness
    source: Illusionist
    level: 2
    DC: 18
  - name: detect thoughts
    source: Illusionist
    level: 2
    DC: 18
  - superscripts:
    - UC
    name: illusion of calm
    source: Illusionist
    level: 2
    DC: 19
  - name: invisibility
    source: Illusionist
    level: 2
  - superscripts:
    - UM
    name: pernicious poison
    source: Illusionist
    level: 2
  - name: color spray
    source: Illusionist
    level: 1
    count: 2
    DC: 18
  - name: hypnotism
    source: Illusionist
    level: 1
    DC: 18
  - name: shield
    source: Illusionist
    level: 1
  - name: silent image
    source: Illusionist
    level: 1
    DC: 18
  - superscripts:
    - APG
    name: vanish
    source: Illusionist
    level: 1
  - name: dancing lights
    source: Illusionist
    level: 0
  - name: detect magic
    source: Illusionist
    level: 0
  - name: mage hand
    source: Illusionist
    level: 0
  - name: read magic
    source: Illusionist
    level: 0
  sources:
  - name: Illusionist
    type: prepared
    CL: 4
    concentration: 10
    slots:
      0: at-will
    opposition_schools:
    - conjuration
    - evocation
tactics:
  During Combat: A serpentfolk illusionist seeks to deceive opponents with spells
    until it can debilitate them with blindness/deafness, color spray, or a venomous
    bite enhanced with pernicious poison. Otherwise, it attacks with its wand or uses
    suggestion and dominate person to turn enemies into allies.
ability_scores:
  STR: 10
  DEX: 22
  CON: 21
  INT: 22
  WIS: 13
  CHA: 18
BAB: 7
CMB: 7
CMD: 24
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (enchantment)
- name: Spell Focus (illusion)
- name: Toughness
skills:
  Acrobatics: 11
  Bluff: 10
  Diplomacy: 10
  Disguise: 10
  Escape Artist: 19
  Intimidate: 12
  Knowledge (arcana): 18
  Knowledge (dungeoneering): 10
  Knowledge (nobility): 10
  Knowledge (religion): 10
  Knowledge (history): 12
  Knowledge (planes): 12
  Perception: 13
  Sense Motive: 7
  Spellcraft: 18
  Use Magic Device: 15
  _racial_mods:
    Escape Artist:
      _: 8
    Use Magic Device:
      _: 4
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Elven
- Undercommon
- telepathy 100 ft.
special_qualities:
- arcane bond (viper)
- extended illusions (+2 rounds)
gear:
  combat:
  - potions of cure moderate wounds (2)
  - scrolls of blur (2)
  - scrolls of daze monster (2)
  - scrolls of hideous laughter (2)
  - scroll of hold person
  - scrolls of invisibility (2)
  - scrolls of mirror image (2)
  - scrolls of touch of idiocy (2)
  - wand of mage armor (20 charges)
  - wand of magic missile (20 charges)
  other:
  - mwk dagger
  - amulet of natural armor +1
  - ring of protection +1
  - spellbook
  - 273 gp
ecology:
  environment: any land (usually jungles or underground)
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 2 saves. The save DC is Constitution-based.
desc_long: A serpentfolk illusionist has greatly enhanced its racial gifts for deception
  with decades of intensive arcane study. On the surface world, it is often the leader
  of a group of serpentfolk or a cult of lesser reptilian humanoids.

---

# Serpentfolk, Serpentfolk Illusionist

**Source** Monster Codex pg. 204
**XP** 4,800
Advanced _[[monsters/Serpentfolk|serpentfolk]]_ illusionist 4

NE Medium monstrous humanoid
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +13

##### Defense

**AC** 21, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 _[[spells/Deflection|deflection]]_, +6 Dex, +4 natural)
**hp** 99 (9 HD; 5d10+4d6+58)
**Fort** +7, **Ref** +11, **Will** +9
**Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison; **SR** 19

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +8/+3 (1d4/19–20), bite +2 (1d6 plus poison)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
At will—_[[spells/Disguise Self|disguise self]]_ (DC 15, humanoid form only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
1/day—_[[spells/Blur|blur]]_, _[[spells/Dominate Person|dominate person]]_ (DC 19), _[[spells/Major Image|major image]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 17)
**Arcane School _Spell-Like Abilities_** (CL 4th; concentration +10)
9/day—_[[spells/Blinding Ray|blinding ray]]_
**Illusionist Spells Prepared **(CL 4th; concentration +10)
2nd—blindness/deafness (DC 18), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Illusion of Calm|illusion of calm]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Pernicious Poison|pernicious poison]]_
1st—_[[spells/Color Spray|color spray]]_ (2, DC 18), _[[spells/Hypnotism|hypnotism]]_ (DC 18), _[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_ (DC 18), _[[spells/Vanish|vanish]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools** conjuration, evocation

### Tactics

**During Combat** A _serpentfolk_ illusionist seeks to deceive opponents with spells until it can debilitate them with blindness/deafness, _color spray_, or a _[[spells/Venomous Bite|venomous bite]]_ enhanced with _pernicious poison_. Otherwise, it attacks with its wand or uses _suggestion_ and _dominate person_ to turn enemies into allies.

##### Statistics
**Str** 10, **Dex** 22, **Con** 21, **Int** 22, **Wis** 13, **Cha** 18
**Base Atk** +7; **CMB** +7; **CMD** 24
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _Spell Focus_ (illusion), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +11, Bluff +10, Diplomacy +10, Disguise +10, Escape Artist +19, Intimidate +12, Knowledge (arcana) +18, Knowledge (dungeoneering, nobility, religion) +10, Knowledge (history, planes) +12, Perception +13, Sense Motive +7, Spellcraft +18, Use Magic Device +15; **Racial Modifiers** +8 Escape Artist, +4 Use Magic Device
**Languages** Abyssal, Aklo, Common, Draconic, Elven, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** arcane bond (viper), extended illusions (+2 rounds)
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), scrolls of _blur_ (2), scrolls of _[[spells/Daze Monster|daze monster]]_ (2), scrolls of _[[spells/Hideous Laughter|hideous laughter]]_ (2), scroll of _[[spells/Hold Person|hold person]]_, scrolls of _invisibility_ (2), scrolls of _mirror image_ (2), scrolls of _[[spells/Touch of Idiocy|touch of idiocy]]_ (2), wand of _[[spells/Mage Armor|mage armor]]_ (20 charges), wand of _[[spells/Magic Missile|magic missile]]_ (20 charges); **Other Gear** mwk _dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 273 gp

##### Ecology

**Environment** any land (usually jungles or underground)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Str; cure 2 saves. The save DC is Constitution-based.

##### Description

A _serpentfolk_ illusionist has greatly enhanced its racial gifts for deception with decades of intensive arcane study. On the surface world, it is often the leader of a group of _serpentfolk_ or a cult of lesser reptilian humanoids.