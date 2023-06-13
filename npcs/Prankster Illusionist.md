---
cssclass: [monsters]
title1: Prankster Illusionist
title2: Prankster Illusionist
CR: 9
sources:
- name: NPC Codex
  page: 185
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 6400
race: Gnome
classes:
- illusionist 10
alignment: CN
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 20
  touch: 15
  flat_footed: 17
  components:
    armor: 4
    deflection: 1
    dex: 2
    dodge: 1
    natural: 1
    size: 1
HP:
  HP: 73
  long: 10d6+36
saves:
  fort: 7
  ref: 6
  will: 10
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk dagger +5 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 5
  ranged:
  - - text: mwk dagger +9 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 9
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
    freq: 7/day
  sources:
  - name: default
    CL: 10
    concentration: 11
  - name: arcane school
    CL: 10
    concentration: 14
spells:
  entries:
  - name: cloudkill
    source: Illusionist
    level: 5
    DC: 19
  - name: persistent image
    source: Illusionist
    level: 5
    DC: 21
  - name: teleport
    source: Illusionist
    level: 5
  - name: greater invisibility
    source: Illusionist
    level: 4
  - name: phantasmal killer
    source: Illusionist
    level: 4
    DC: 20
  - name: empowered scorching ray
    source: Illusionist
    level: 4
  - name: solid fog
    source: Illusionist
    level: 4
  - name: stone shape
    source: Illusionist
    level: 4
  - name: dispel magic
    source: Illusionist
    level: 3
  - name: displacement
    source: Illusionist
    level: 3
  - name: fly
    source: Illusionist
    level: 3
  - name: haste
    source: Illusionist
    level: 3
    DC: 17
  - name: major image
    source: Illusionist
    level: 3
    DC: 19
  - name: detect thoughts
    source: Illusionist
    level: 2
    DC: 16
  - name: glitterdust
    source: Illusionist
    level: 2
    DC: 16
  - name: hypnotic pattern
    source: Illusionist
    level: 2
    DC: 18
  - name: magic mouth
    source: Illusionist
    level: 2
  - name: mirror image
    source: Illusionist
    level: 2
  - name: scorching ray
    source: Illusionist
    level: 2
  - name: color spray
    source: Illusionist
    level: 1
    count: 2
    DC: 17
  - name: feather fall
    source: Illusionist
    level: 1
  - name: grease
    source: Illusionist
    level: 1
  - name: magic missile
    source: Illusionist
    level: 1
  - name: silent image
    source: Illusionist
    level: 1
    DC: 17
  - name: dancing lights
    source: Illusionist
    level: 0
  - name: detect magic
    source: Illusionist
    level: 0
  - name: ghost sound
    source: Illusionist
    level: 0
    DC: 16
  - name: mage hand
    source: Illusionist
    level: 0
  sources:
  - name: Illusionist
    type: prepared
    CL: 10
    concentration: 14
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor from her wand.
  During Combat: The wizard prefers to prank others rather than cause deliberate harm.
    She casts greater invisibility, then harasses and annoys her targets with glitterdust,
    grease, major image, persistent image, and solid fog. If attacked with lethal
    force, she retaliates with cloudkill, empowered scorching ray, and magic missile.
  Base Statistics: Without mage armor, the wizard's statistics are AC 16, touch 15,
    flat-footed 13.
ability_scores:
  STR: 6
  DEX: 14
  CON: 16
  INT: 18
  WIS: 14
  CHA: 12
BAB: 5
CMB: 2
CMD: 16
feats:
- name: Combat Casting
- name: Craft Wand
- name: Craft Wondrous Item
- name: Dodge
- name: Empower Spell
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (illusion)
skills:
  Acrobatics: 7
    when jumping: 3
  Appraise: 12
  Craft (sculptures): 14
  Fly: 12
  Knowledge (arcana): 17
  Knowledge (geography): 10
  Knowledge (local): 10
  Knowledge (nature): 10
  Perception: 9
  Perform (oratory): 6
  Spellcraft: 17
  Stealth: 11
languages:
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Sylvan
special_qualities:
- arcane bond (raven)
- extended illusions (+5 rounds)
gear:
  combat:
  - potion of cure moderate wounds
  - potion of cure serious wounds
  - scroll of displacement
  - scroll of empowered scorching ray
  - scroll of teleport
  - wand of burning hands (CL 5th, 20 charges)
  - wand of invisibility (20 charges)
  - wand of mage armor (20 charges)
  other:
  - masterwork dagger
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - cloak of resistance +1
  - headband of vast intelligence +2
  - ring of protection +1
  - spellbook
  - jade dust for magic mouth (worth 50 gp)
  - 998 gp
desc_long: These irreverent illusionists are the bane of humorless adventurers. Their
  tricks are sometimes mistaken for enemy attacks, and even in dangerous situations,
  their own amusement comes first.

---

# Prankster Illusionist

**Source** NPC Codex pg. 185
**XP** 6,400
Gnome illusionist 10

CN Small humanoid (gnome)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +1 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural, +1 size)
**hp** 73 (10d6+36)
**Fort** +7, **Ref** +6, **Will** +10; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +5 (1d3–2/19–20)
**Ranged** mwk _dagger_ +9 (1d3–2/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +11)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**Arcane School _Spell-Like Abilities_** (CL 10th; concentration +14)
At will—_[[spells/Invisibility|invisibility]]_ field (10 rounds/day)
7/day—_[[spells/Blinding Ray|blinding ray]]_
**Illusionist Spells Prepared **(CL 10th; concentration +14)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 19), _[[spells/Persistent Image|persistent image]]_ (DC 21), teleport
4th—greater _invisibility_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 20), empowered _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Solid Fog|solid fog]]_, _[[spells/Stone Shape|stone shape]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, fly, _[[spells/Haste|haste]]_ (DC 17), _[[spells/Major Image|major image]]_ (DC 19)
2nd—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Glitterdust|glitterdust]]_ (DC 16), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 18), _[[spells/Magic Mouth|magic mouth]]_, _[[spells/Mirror Image|mirror image]]_, _scorching ray_
1st—_[[spells/Color Spray|color spray]]_ (2, DC 17), _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Silent Image|silent image]]_ (DC 17)
0 (at will)—_dancing lights_, _[[spells/Detect Magic|detect magic]]_, _ghost sound_ (DC 16), _[[spells/Mage Hand|mage hand]]_
**Opposition Schools **enchantment, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _[[spells/Mage Armor|mage armor]]_ from her wand.
**During Combat **The _wizard_ prefers to prank others rather than cause deliberate _[[spells/Harm|harm]]_. She casts greater _invisibility_, then harasses and annoys her targets with _glitterdust_, _grease_, _major image_, _persistent image_, and _solid fog_. If attacked with lethal force, she retaliates with _cloudkill_, empowered _scorching ray_, and _magic missile_.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **16, touch 15, _flat-footed_ 13.

##### Statistics
**Str** 6, **Dex** 14, **Con** 16, **Int** 18, **Wis** 14, **Cha** 12
**Base Atk** +5; **CMB** +2; **CMD** 16
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (illusion)
**Skills** Acrobatics +7 (+3 when jumping), Appraise +12, Craft (sculptures) +14, Fly +12, Knowledge (arcana) +17, Knowledge (geography, local, nature) +10, Perception +9, Perform (oratory) +6, Spellcraft +17, Stealth +11
**Languages** Common, Draconic, Dwarven, Elven, Gnome, Sylvan
**SQ** arcane bond (raven), extended illusions (+5 rounds)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _displacement_, scroll of empowered _scorching ray_, scroll of teleport, wand of _[[spells/Burning Hands|burning hands]]_ (CL 5th, 20 charges), wand of _invisibility_ (20 charges), wand of _mage armor_ (20 charges); **Other Gear** masterwork _dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, jade dust for _magic mouth_ (worth 50 gp), 998 gp

These irreverent illusionists are the _[[spells/Bane|bane]]_ of humorless adventurers. Their tricks are sometimes mistaken for enemy attacks, and even in dangerous situations, their own amusement comes first.