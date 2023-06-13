---
cssclass: [monsters]
title1: Black Ice
title2: Black Ice
CR: 16
sources:
- name: NPC Codex
  page: 238
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Gnome
classes:
- illusionist 10
- shadowdancer 7
alignment: NE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 23
  touch: 17
  flat_footed: 20
  components:
    armor: 4
    deflection: 3
    dex: 2
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 147
  long: 10d6+7d8+78
saves:
  fort: 12
  ref: 15
  will: 15
  other: +2 vs. illusions
defensive_abilities:
- defensive roll
- defensive training (+4 dodge bonus to AC vs. giants)
- evasion
- greater invisibility
- improved uncanny dodge
- slippery mind
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 100
speeds:
  base: 30
attacks:
  melee:
  - - text: staff of frost +10/+5 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: staff of frost
      bonus:
      - 10
      - 5
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  - name: invisibility field
    source: arcane school
    freq: At will
    other: 10 rounds/day
  - name: blinding ray
    source: arcane school
    freq: 8/day
  - name: shadow illusion
    source: shadowdancer
    freq: 3/day
    DC: 13
  - name: shadow call
    source: shadowdancer
    freq: 2/day
    DC: 16
  sources:
  - name: default
    CL: 17
    concentration: 19
  - name: arcane school
    CL: 10
    concentration: 15
  - name: shadowdancer
    CL: 7
    concentration: 9
spells:
  entries:
  - name: feeblemind
    source: Illusionist
    level: 5
    DC: 20
  - name: nightmare
    source: Illusionist
    level: 5
    DC: 23
  - name: shadow evocation
    source: Illusionist
    level: 5
    DC: 23
  - name: teleport
    source: Illusionist
    level: 5
  - name: charm monster
    source: Illusionist
    level: 4
    DC: 19
  - name: greater invisibility
    source: Illusionist
    level: 4
  - name: phantasmal killer
    source: Illusionist
    level: 4
    DC: 22
  - name: solid fog
    source: Illusionist
    level: 4
  - name: stoneskin
    source: Illusionist
    level: 4
  - name: blink
    source: Illusionist
    level: 3
  - name: displacement
    source: Illusionist
    level: 3
  - name: fly
    source: Illusionist
    level: 3
  - name: major image
    source: Illusionist
    level: 3
    DC: 21
  - name: slow
    source: Illusionist
    level: 3
    DC: 18
  - name: acid arrow
    source: Illusionist
    level: 2
  - name: darkness
    source: Illusionist
    level: 2
  - name: hypnotic pattern
    source: Illusionist
    level: 2
    DC: 20
  - name: invisibility
    source: Illusionist
    level: 2
    count: 2
  - name: resist energy
    source: Illusionist
    level: 2
  - name: charm person
    source: Illusionist
    level: 1
    DC: 16
  - name: color spray
    source: Illusionist
    level: 1
    DC: 19
  - name: feather fall
    source: Illusionist
    level: 1
  - name: mage armor
    source: Illusionist
    level: 1
  - name: magic missile
    source: Illusionist
    level: 1
    count: 2
  - name: shield
    source: Illusionist
    level: 1
  - name: daze
    source: Illusionist
    level: 0
    DC: 15
  - name: ghost sound
    source: Illusionist
    level: 0
    DC: 18
  - name: mage hand
    source: Illusionist
    level: 0
  - name: ray of frost
    source: Illusionist
    level: 0
  sources:
  - name: Illusionist
    type: prepared
    CL: 10
    concentration: 15
    slots:
      0: at-will
    opposition_schools:
    - divination
    - necromancy
tactics:
  Before Combat: The shadowdancer casts mage armor and stoneskin.
  During Combat: The shadowdancer casts greater invisibility and shield, then harries
    his foes with phantasmal killer, hypnotic pattern, and spells from his staff of
    frost.
  Base Statistics: Without mage armor and stoneskin, the shadowdancer's statistics
    are AC 19, touch 17, flat-footed 16; DR none.
ability_scores:
  STR: 6
  DEX: 14
  CON: 16
  INT: 20
  WIS: 10
  CHA: 14
BAB: 10
CMB: 7
CMD: 23
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Fleet (2)
- name: Greater Spell Focus (illusion)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Scribe Scroll
- name: Spell Focus (illusion)
- name: Toughness
skills:
  Acrobatics: 20
  Bluff: 20
  Craft (alchemy): 7
  Diplomacy: 20
  Fly: 17
  Knowledge (arcana): 23
  Knowledge (dungeoneering): 13
  Knowledge (geography): 13
  Knowledge (planes): 23
  Perception: 20
  Perform (dance): 8
  Spellcraft: 23
  Stealth: 24
  Swim: 2
languages:
- Aklo
- Common
- Draconic
- Gnome
- Sylvan
special_qualities:
- arcane bond (staff of frost)
- extended illusions (+5 rounds)
- hide in plain sight
- rogue talents (combat trick, fast stealth)
- shadow jump (80 feet/day)
- summon shadow
gear:
  combat:
  - restorative ointment (5 applications)
  - staff of frost (10 charges)
  other:
  - amulet of natural armor +2
  - cloak of resistance +4
  - headband of vast intelligence +2
  - ring of protection +3
  - diamond dust (worth 500 gp)
  - 3,800 gp
desc_long: These evasive spellcasters make frustrating enemies.

---

# Black Ice

**Source** NPC Codex pg. 238
**XP** 76,800
Gnome illusionist 10/shadowdancer 7

NE Small humanoid (gnome)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 armor, +3 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural, +1 size)
**hp** 147 (10d6+7d8+78)
**Fort** +12, **Ref** +15, **Will** +15; +2 vs. illusions
**Defensive Abilities** defensive roll, defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), evasion, greater _[[spells/Invisibility|invisibility]]_, improved uncanny _dodge_, slippery mind; **DR** 10/adamantine (100 points)

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Staff/Staff of Frost|staff of frost]]_ +10/+5 (1d4–2)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +19)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**Arcane School _Spell-Like Abilities_ **(CL 10th; concentration +15)
At will—_invisibility_ field (10 rounds/day)
8/day—_[[spells/Blinding Ray|blinding ray]]_
**Shadowdancer _Spell-Like Abilities_ **(CL 7th; concentration +9)
3/day—_[[items/Armor Magic Abilities/Shadow|shadow]]_ illusion (DC 13)
2/day—_shadow_ call (DC 16)
**Illusionist Spells Prepared **(CL 10th; concentration +15)
5th—_[[spells/Feeblemind|feeblemind]]_ (DC 20), _[[spells/Nightmare|nightmare]]_ (DC 23), _[[spells/Shadow Evocation|shadow evocation]]_ (DC 23), teleport
4th—_[[spells/Charm Monster|charm monster]]_ (DC 19), greater _invisibility_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 22), _[[spells/Solid Fog|solid fog]]_, _[[spells/Stoneskin|stoneskin]]_
3rd—_[[spells/Blink|blink]]_, _[[spells/Displacement|displacement]]_, fly, _[[spells/Major Image|major image]]_ (DC 21), _[[spells/Slow|slow]]_ (DC 18)
2nd—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Darkness|darkness]]_, _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 20), _invisibility_ (2), _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Color Spray|color spray]]_ (DC 19), _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_ (2), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 15), _ghost sound_ (DC 18), _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_
**Opposition Schools **_[[spells/Divination|divination]]_, necromancy

### Tactics

**Before Combat **The shadowdancer casts _mage armor_ and _stoneskin_.
**During Combat **The shadowdancer casts greater _invisibility_ and _shield_, then harries his foes with _phantasmal killer_, _hypnotic pattern_, and spells from his _staff of frost_.
**Base Statistics **Without _mage armor_ and _stoneskin_, the shadowdancer’s statistics are **AC **19, touch 17, _flat-footed_ 16; **DR **none.

##### Statistics
**Str** 6, **Dex** 14, **Con** 16, **Int** 20, **Wis** 10, **Cha** 14
**Base Atk** +10; **CMB** +7; **CMD** 23
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Fleet|Fleet]]_ (2), _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (illusion), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (illusion), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +20, Bluff +20, Craft (alchemy) +7, Diplomacy +20, Fly +17, Knowledge (arcana) +23, Knowledge (dungeoneering, geography) +13, Knowledge (planes) +23, Perception +20, Perform (dance) +8, Spellcraft +23, Stealth +24, Swim +2
**Languages** Aklo, Common, Draconic, Gnome, Sylvan
**SQ** arcane bond (_staff of frost_), extended illusions (+5 rounds), hide in plain sight, _[[classes/Rogue|rogue]]_ talents (combat trick, fast stealth), _shadow_ _[[spells/Jump|jump]]_ (80 feet/day), _[[universal monster rules/Summon|summon]]_ _shadow_
**Combat Gear** _[[items/Wondrous Item/Restorative Ointment|restorative ointment]]_ (5 applications), _staff of frost_ (10 charges); **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, diamond dust (worth 500 gp), 3,800 gp

These evasive spellcasters make frustrating enemies.