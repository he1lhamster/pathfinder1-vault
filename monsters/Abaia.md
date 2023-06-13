---
cssclass: [monsters]
title1: Abaia
desc_short: This multi-eyed eel's brightly colored markings shift in complex, ever-changing
  patterns.
title2: Abaia
CR: 10
sources:
- name: Bestiary 4
  page: 7
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 9600
alignment: N
size: Huge
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 3
senses:
  arcane sight: true
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 11
  flat_footed: 22
  components:
    dex: 3
    natural: 14
    size: -2
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 14
  ref: 12
  will: 8
SR: 21 (in water only)
speeds:
  base: 20
  swim: 80
attacks:
  melee:
  - - text: bite +21 (3d6+8/19-20 plus grab)
      entries:
      - - damage: 3d6+8
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 21
    - text: tail slap +15 (2d6+4 plus grab)
      entries:
      - - damage: 2d6+4
        - effect: grab
      attack: tail slap
      bonus:
      - 15
  special:
  - constrict (2d6+12)
  - endless coils
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: control water
    source: default
    freq: At will
  - superscripts:
    - APG
    name: hydraulic torrent
    source: default
    freq: At will
  - name: rainbow pattern
    source: default
    freq: At will
    DC: 17
  - name: control weather
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 17
ability_scores:
  STR: 26
  DEX: 16
  CON: 21
  INT: 17
  WIS: 14
  CHA: 17
BAB: 14
CMB: 24
CMB_other: +28 grapple
CMD: 37
CMD_other: can't be tripped
feats:
- name: Critical Focus
- name: Improved Critical (bite)
- name: Iron Will
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Knowledge (arcana): 17
  Knowledge (nature): 17
  Perception: 19
  Spellcraft: 17
  Stealth: 12
    in water: 24
  Swim: 16
  _racial_mods:
    Stealth:
      in water: 12
languages:
- Aquan
- Sylvan
- speak with animals
special_qualities:
- eldritch gizzard
- wave rider
ecology:
  environment: warm lakes
  organization: solitary
  treasure_type: standard
  treasure:
  - particularly staves and wands
special_abilities:
  Eldritch Gizzard (Su): An abaia can activate arcane spell trigger items as if it
    were a 14th-level sorcerer. It can store items in a special compartment within
    its stomach and activate them as if it were holding them. It can swallow or regurgitate
    an item as a standard action.
  Endless Coils (Ex): As a full-round action, an abaia can attempt a single combat
    maneuver check to grapple up to two Large or four Medium or smaller creatures
    within its reach. Any targets successfully grabbed take constrict damage. The
    abaia only needs to succeed at one grapple check to maintain a grapple against
    multiple opponents.
  Wave Rider (Su): An abaia moving onto land brings a sheath of water with it, allowing
    it to swim on land. Its swim speed drops by 10 feet at the start of its turn if
    it is out of the water, and the sheath dissipates entirely when the abaia's swim
    speed reaches 20 feet. An abaia wave riding on land retains its spell resistance
    but loses its bonus to Stealth.
desc_long: Originally from the primal world of the fey, an abaia protects lakes and
  their surroundings from exploitation, in particular by magic and overfishing. It
  favors waters with a mystical nature or supernatural properties. An abaia ignores
  creatures that take only what they need from the lake and otherwise show proper
  respect to the waters. Those that abuse an abaia's lake risk capsized boats, floods,
  torrential rains, and even direct attacks. After sinking a vessel, an abaia searches
  the wreckage for magical treasure.

---

# Abaia
This multi-eyed eel’s brightly colored markings shift in complex, ever-changing patterns.
**Source** Bestiary 4 pg. 7
**XP** 9,600

N Huge magical beast (aquatic)
**Init** +3; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+3 Dex, +14 natural, –2 size)
**hp** 147 (14d10+70)
**Fort** +14, **Ref** +12, **Will** +8
**SR** 21 (in water only)

##### Offense
**Speed** 20 ft., swim 80 ft.
**Melee** bite +21 (3d6+8/19–20 plus _[[universal monster rules/Grab|grab]]_), tail slap +15 (2d6+4 plus _grab_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+12), endless coils
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +17)
Constant—_arcane sight_, _[[spells/Speak with Animals|speak with animals]]_
At will—_[[spells/Control Water|control water]]_, _[[spells/Hydraulic Torrent|hydraulic torrent]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 17)
1/day—_[[spells/Control Weather|control weather]]_

##### Statistics
**Str** 26, **Dex** 16, **Con** 21, **Int** 17, **Wis** 14, **Cha** 17
**Base Atk** +14; **CMB** +24 (+28 grapple); **CMD** 37 (can’t be tripped)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Knowledge (arcana) +17, Knowledge (nature) +17, Perception +19, Spellcraft +17, Stealth +12 (+24 in water), Swim +16; **Racial Modifiers** +12 Stealth in water
**Languages** Aquan, Sylvan; _speak with animals_
**SQ** eldritch gizzard, wave rider

##### Ecology

**Environment** warm lakes
**Organization** solitary
**Treasure** standard (particularly staves and wands)

### Special Abilities

**Eldritch Gizzard (Su)** An _[[monsters/Abaia|abaia]]_ can activate arcane spell trigger items as if it were a 14th-level _[[classes/Sorcerer|sorcerer]]_. It can store items in a special compartment within its stomach and activate them as if it were holding them. It can swallow or regurgitate an item as a standard action.

**Endless Coils (Ex)** As a full-round action, an _abaia_ can attempt a single combat maneuver check to grapple up to two Large or four Medium or smaller creatures within its reach. Any targets successfully grabbed take _constrict_ damage. The _abaia_ only needs to succeed at one grapple check to maintain a grapple against multiple opponents.

**Wave Rider (Su)** An _abaia_ moving onto land brings a sheath of water with it, allowing it to swim on land. Its swim speed drops by 10 feet at the start of its turn if it is out of the water, and the sheath dissipates entirely when the _abaia_’s swim speed reaches 20 feet. An _abaia_ wave riding on land retains its _[[universal monster rules/Spell Resistance|spell resistance]]_ but loses its bonus to Stealth.

##### Description

Originally from the primal world of the fey, an _abaia_ protects lakes and their surroundings from exploitation, in particular by magic and overfishing. It favors waters with a mystical nature or supernatural properties. An _abaia_ ignores creatures that take only what they need from the lake and otherwise show proper respect to the waters. Those that abuse an _abaia_’s lake risk capsized boats, floods, torrential rains, and even direct attacks. After sinking a vessel, an _abaia_ searches the wreckage for magical treasure.