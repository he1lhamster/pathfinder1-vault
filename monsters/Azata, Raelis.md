---
cssclass: [monsters]
title1: Azata, Raelis
desc_short: This bronze-skinned humanoid is muscular yet lithe, garbed in colorful
  clothing emblazoned with glowing runes.
title2: Raelis
CR: 10
sources:
- name: Bestiary 5
  page: 39
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Pathfinder #66: The Dead Heart of Xin'
  page: 84
  link: http://paizo.com/products/btpy8tvr?Pathfinder-Adventure-Path-66-The-Dead-Heart-of-Xin
XP: 9600
alignment: CG
size: Large
type: outsider
subtypes:
- azata
- chaotic
- extraplanar
- good
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 23
  touch: 13
  flat_footed: 19
  components:
    dex: 4
    natural: 10
    size: -1
HP:
  HP: 115
  long: 11d10+55
saves:
  fort: 8
  ref: 11
  will: 9
DR:
- amount: 10
  weakness: cold iron and evil
immunities:
- electricity
- petrification
- rune mastery
resistances:
  cold: 10
  fire: 10
speeds:
  base: 50
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 slams +19 (2d8+7)
      entries:
      - - damage: 2d8+7
      count: 2
      attack: slams
      bonus:
      - 19
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: nondetection
    source: default
    freq: Constant
  - name: alter self
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: 3/day
  - name: modify memory
    source: default
    freq: 3/day
    DC: 17
  - name: greater teleport
    source: default
    freq: 1/day
    other: self plus 50 lbs. of objects only
  - name: plane shift
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 12
    concentration: 16
spells:
  entries:
  - name: seeming
    source: Sorcerer
    level: 5
  - name: sending
    source: Sorcerer
    level: 5
  - name: symbol of pain
    source: Sorcerer
    level: 5
    DC: 20
  - name: symbol of sleep
    source: Sorcerer
    level: 5
    DC: 20
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 18
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: scrying
    source: Sorcerer
    level: 4
    DC: 18
  - name: beast shape I
    source: Sorcerer
    level: 3
  - name: explosive runes
    source: Sorcerer
    level: 3
    DC: 18
  - name: glyph of warding
    source: Sorcerer
    level: 3
    DC: 18
  - name: haste
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 17
  - name: sepia snake sigil
    source: Sorcerer
    level: 3
    DC: 18
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 17
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 16
  - name: hypnotic pattern
    source: Sorcerer
    level: 2
    DC: 16
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: erase
    source: Sorcerer
    level: 1
  - name: feather fall
    source: Sorcerer
    level: 1
  - name: hypnotism
    source: Sorcerer
    level: 1
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 15
  - name: ventriloquism
    source: Sorcerer
    level: 1
    DC: 15
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 11
    concentration: 15
    slots:
      5: 4
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 24
  DEX: 19
  CON: 20
  INT: 18
  WIS: 15
  CHA: 19
BAB: 11
CMB: 19
CMB_other: +23 grapple
CMD: 33
CMD_other: 35 vs. grapple
feats:
- name: Greater Grapple
- name: Improved Grapple
- name: Improved Initiative
- name: Improved Unarmed Strike
- name: Power Attack
- name: Weapon Focus (slam)
skills:
  Acrobatics: 18
  Bluff: 18
  Disguise: 14
  Fly: 20
  Knowledge (geography): 18
  Knowledge (planes): 18
  Knowledge (history): 15
  Perception: 16
  Perform (oratory): 18
  Spellcraft: 18
  Stealth: 14
  _racial_mods:
    Disguise:
      _: 10
languages:
- Celestial
- Common
- Draconic
- Infernal
- truespeech
special_qualities:
- rune mastery
- word caller
ecology:
  environment: any (Elysium)
  organization: solitary, pair, or band (3-6)
  treasure_type: standard
special_abilities:
  Rune Mastery (Ex): Raelises add explosive runes, glyph of warding, sepia snake sigil,
    symbol of pain, and symbol of sleep to their list of spells known and increase
    these spells' DCs by 1. Additionally, raelises are immune to these spells.
  Spells: Raelises casts spells as 11th-level sorcerers.
  Word Caller (Su): Raelises sense the presence and basic topics of any books, scrolls,
    or other writings. As a standard action, they can read 100 pages of nonmagical
    writing, or read one scroll as if with read magic. These abilities' range is 50
    feet.
desc_long: Formed from the souls of authors, artists, and storytellers, raelises travel
  to the farthest corners of the planes searching for epic stories, poems, and simple
  tall tales.

---

# Azata, Raelis
This bronze-skinned humanoid is muscular yet lithe, garbed in colorful clothing emblazoned with glowing runes.
**Source** Bestiary 5 pg. 39, Pathfinder #66: The Dead Heart of Xin pg. 84
**XP** 9,600

CG Large outsider (azata, chaotic, extraplanar, good)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 Dex, +10 natural, -1 size)
**hp** 115 (11d10+55)
**Fort** +8, **Ref** +11, **Will** +9
**DR** 10/cold iron and evil; **Immune** electricity, petrification, rune mastery; **Resist** cold 10, fire 10

##### Offense
**Speed** 50 ft., fly 120 ft. (good)
**Melee** 2 slams +19 (2d8+7)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Nondetection|nondetection]]_
At will—_[[spells/Alter Self|alter self]]_
3/day—_[[spells/Dimension Door|dimension door]]_, _[[spells/Modify Memory|modify memory]]_ (DC 17)
1/day—greater teleport (self plus 50 lbs. of objects only), _[[spells/Plane Shift|plane shift]]_ (DC 21)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 11th; concentration +15)
5th (4/day)—_[[spells/Seeming|seeming]]_, _[[spells/Sending|sending]]_, _[[spells/Symbol of Pain|symbol of pain]]_ (DC 20), _[[spells/Symbol of Sleep|symbol of sleep]]_ (DC 20)
4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 18), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Scrying|scrying]]_ (DC 18)
3rd (7/day)—_[[spells/Beast Shape I|beast shape I]]_, _[[spells/Explosive Runes|explosive runes]]_ (DC 18), _[[spells/Glyph Of Warding|glyph of warding]]_ (DC 18), _[[spells/Haste|haste]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 17), _[[spells/Sepia Snake Sigil|sepia snake sigil]]_ (DC 18), _[[spells/Suggestion|suggestion]]_ (DC 17)
2nd (7/day)—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 16), _invisibility_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Erase|erase]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Hypnotism|hypnotism]]_, _[[spells/Silent Image|silent image]]_ (DC 15), _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 24, **Dex** 19, **Con** 20, **Int** 18, **Wis** 15, **Cha** 19
**Base Atk** +11; **CMB** +19 (+23 grapple); **CMD** 33 (35 vs. grapple)
**Feats** _[[feats/Greater Grapple|Greater Grapple]]_, _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Acrobatics +18, Bluff +18, Disguise +14, Fly +20, Knowledge (geography, planes) +18, Knowledge (history) +15, Perception +16, Perform (oratory) +18, Spellcraft +18, Stealth +14; **Racial Modifiers** +10 Disguise
**Languages** Celestial, Common, Draconic, Infernal; truespeech
**SQ** rune mastery, word caller

##### Ecology

**Environment** any (Elysium)
**Organization** solitary, pair, or band (3-6)
**Treasure** standard

### Special Abilities

**Rune Mastery (Ex)** Raelises add _explosive runes_, _glyph of warding_, _sepia snake sigil_, _symbol of pain_, and _symbol of sleep_ to their list of spells known and increase these spells’ DCs by 1. Additionally, raelises are immune to these spells.
**Spells** Raelises casts spells as 11th-level sorcerers.

**Word Caller (Su)** Raelises sense the presence and basic topics of any books, scrolls, or other writings. As a standard action, they can read 100 pages of nonmagical writing, or read one scroll as if with _read magic_. These abilities’ range is 50 feet.

##### Description

Formed from the souls of authors, artists, and storytellers, raelises travel to the farthest corners of the planes searching for epic stories, poems, and simple tall tales.