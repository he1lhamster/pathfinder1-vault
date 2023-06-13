---
cssclass: [monsters]
title1: Archon, Gate Archon
desc_short: This masked humanoid being has wings and armor of rune-carved gray stone,
  and its eyes glow blue.
title2: Gate Archon
CR: 17
sources:
- name: Bestiary 5
  page: 35
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 102400
alignment: LG
size: Medium
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 3
senses:
  darkvision: 60
  true seeing: true
auras:
- name: aura of menace
  radius: 30
  DC: 23
  duration: 10 rounds
AC:
  AC: 33
  touch: 14
  flat_footed: 29
  components:
    armor: 9
    dex: 3
    dodge: 1
    natural: 10
    deflection vs. evil: 2
HP:
  HP: 263
  long: 17d10+170
  regeneration: 10
  regeneration_weakness: evil weapons and effects
saves:
  fort: 20
  ref: 8
  will: 16
  other: +4 vs. poison
DR:
- amount: 10
  weakness: evil
immunities:
- electricity
- fear
- petrification
SR: 28
speeds:
  base: 20
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 conductive greatsword +30/+25/+20/+15 (2d6+18/17-20)
      entries:
      - - damage: 2d6+18
          crit_range: 17-20
      attack: +3 conductive greatsword
      bonus:
      - 30
      - 25
      - 20
      - 15
    - text: 2 wings +22 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: wings
      bonus:
      - 22
spell_like_abilities:
  entries:
  - name: nondetection
    source: default
    freq: Constant
  - name: statue
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 18
  - name: detect evil
    source: default
    freq: At will
  - name: dimensional anchor
    source: default
    freq: At will
  - name: dismissal
    source: default
    freq: At will
    DC: 19
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: calcific touch
    source: default
    freq: 3/day
    DC: 19
  - name: glyph of warding
    source: default
    freq: 3/day
    DC: 18
  - name: plane shift
    source: default
    freq: 3/day
    DC: 20
  - name: gate
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 22
spells:
  entries:
  - name: mass heal
    source: Cleric
    level: 9
    DC: 24
  - name: dimensional lock
    source: Cleric
    level: 8
  - name: greater spell immunity
    source: Cleric
    level: 8
  - name: greater scrying
    source: Cleric
    level: 7
    DC: 22
  - name: holy word
    source: Cleric
    level: 7
    count: 2
    DC: 22
  - name: antilife shell
    source: Cleric
    level: 6
  - name: banishment
    source: Cleric
    level: 6
    count: 2
    DC: 22
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 21
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: break enchantment
    source: Cleric
    level: 5
    count: 2
  - name: breath of life
    source: Cleric
    level: 5
  - name: dispel evil
    source: Cleric
    level: 5
    DC: 20
  - name: righteous might
    source: Cleric
    level: 5
  - name: wall of stone
    source: Cleric
    level: 5
  - name: blessing of fervor
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
  - name: neutralize poison
    source: Cleric
    level: 4
  - name: daylight
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
    count: 2
  - name: searing light
    source: Cleric
    level: 3
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 17
  - name: consecrate
    source: Cleric
    level: 2
  - name: eagle's splendor
    source: Cleric
    level: 2
  - name: owl's wisdom
    source: Cleric
    level: 2
  - name: remove paralysis
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - name: divine favor
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: protection from evil
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 17
    concentration: 23
ability_scores:
  STR: 30
  DEX: 17
  CON: 31
  INT: 18
  WIS: 22
  CHA: 21
BAB: 17
CMB: 27
CMD: 41
feats:
- name: Combat Expertise
- name: Dodge
- name: Improved Critical (greatsword)
- name: Lunge
- name: Mobility
- name: Power Attack
- name: Shield of Swings
- name: Spring Attack
- name: Whirlwind Attack
skills:
  Acrobatics: 17
    when jumping: 13
  Fly: 24
  Intimidate: 25
  Knowledge (planes): 24
  Perception: 26
  Sense Motive: 26
  Spellcraft: 24
  Stealth: 20
  Survival: 26
  Use Magic Device: 25
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- graven wings
- stoneblade
ecology:
  environment: any (Heaven)
  organization: solitary or pair
  treasure_type: standard
  treasure:
  - mithral full plate
  - +3 conductive greatsword
  - other treasure
special_abilities:
  Graven Wings (Ex, Sp): A gate archon can inscribe a glyph of warding onto its wings;
    this glyph can be triggered only when the archon is using its statue form.
  Stoneblade (Ex, Su): A gate archon can create a +3 conductive greatsword as a full-round
    action. A stoneblade crumbles to dust if the archon dies or crafts a new sword.
desc_long: Gate archons stand in silent vigils over interplanar portals.

---

# Archon, Gate Archon
This masked humanoid being has wings and armor of rune-carved _[[monsters/Gray|gray]]_ stone, and its eyes glow blue.
**Source** Bestiary 5 pg. 35
**XP** 102,400

LG Medium outsider (archon, extraplanar, good, lawful)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +26
**Aura** aura of menace (30 ft., DC 23, 10 rounds)

##### Defense

**AC** 33, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+9 armor, +3 Dex, +1 _[[feats/Dodge|Dodge]]_, +10 natural; +2 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 263 (17d10+170); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil weapons and effects)
**Fort** +20, **Ref** +8, **Will** +16; +4 vs. poison
**DR** 10/evil; **Immune** electricity, _[[universal monster rules/Fear|fear]]_, petrification; **SR** 28

##### Offense
**Speed** 20 ft., fly 90 ft. (good)
**Melee** +3 _[[items/Weapon Magic Abilities/Conductive|conductive]]_ _[[items/Weapon/Greatsword|greatsword]]_ +30/+25/+20/+15 (2d6+18/17-20), 2 wings +22 (1d4+5)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +22)
Constant—_[[spells/Nondetection|nondetection]]_, _[[spells/Statue|statue]]_, _true seeing_
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Detect Evil|detect evil]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dismissal|dismissal]]_ (DC 19), greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Calcific Touch|calcific touch]]_ (DC 19), _[[spells/Glyph Of Warding|glyph of warding]]_ (DC 18), _[[spells/Plane Shift|plane shift]]_ (DC 20)
1/day—_[[spells/Gate|gate]]_
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 17th; concentration +23)
9th—mass _[[spells/Heal|heal]]_ (DC 24)
8th—_[[spells/Dimensional Lock|dimensional lock]]_, greater _[[spells/Spell Immunity|spell immunity]]_
7th— greater _[[spells/Scrying|scrying]]_ (DC 22), _[[spells/Holy Word|holy word]]_ (2, DC 22)
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Banishment|banishment]]_ (2, DC 22), _[[spells/Blade Barrier|blade barrier]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _heal_
5th—_[[spells/Break Enchantment|break enchantment]]_ (2), _[[spells/Breath Of Life|breath of life]]_, _[[spells/Dispel Evil|dispel evil]]_ (DC 20), _[[spells/Righteous Might|righteous might]]_, _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Blessing Of Fervor|blessing of fervor]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Neutralize Poison|neutralize poison]]_
3rd—_[[spells/Daylight|daylight]]_, _dispel magic_, _[[spells/Prayer|prayer]]_ (2), _[[spells/Searing Light|searing light]]_
2nd—_[[spells/Calm Emotions|calm emotions]]_ (DC 17), _[[spells/Consecrate|consecrate]]_, _[[monsters/Eagle|eagle]]_’s splendor, owl’s wisdom, _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Silence|silence]]_ (DC 17)
1st—_[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Shield Of Faith|shield of faith]]_
0—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, stabilize

##### Statistics
**Str** 30, **Dex** 17, **Con** 31, **Int** 18, **Wis** 22, **Cha** 21
**Base Atk** +17; **CMB** +27; **CMD** 41
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_greatsword_), _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Shield of Swings|Shield of Swings]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +17 (+13 when jumping), Fly +24, Intimidate +25, Knowledge (planes) +24, Perception +26, Sense Motive +26, Spellcraft +24, Stealth +20, Survival +26, Use Magic Device +25
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** graven wings, stoneblade

##### Ecology

**Environment** any (Heaven)
**Organization** solitary or pair
**Treasure** standard (mithral _[[items/Armor/Full plate|full plate]]_, +3 _conductive_ _greatsword_, other treasure)

### Special Abilities

**Graven Wings (Ex, Sp)** A _gate_ archon can inscribe a _glyph of warding_ onto its wings; this glyph can be triggered only when the archon is using its _statue_ form.
**Stoneblade (Ex, Su)** A _gate_ archon can create a +3 _conductive_ _greatsword_ as a full-round action. A stoneblade crumbles to dust if the archon dies or crafts a new sword.

##### Description

_Gate_ archons stand in silent vigils over interplanar portals.