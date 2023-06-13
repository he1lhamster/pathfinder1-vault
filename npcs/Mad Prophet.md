---
cssclass: [monsters]
title1: Mad Prophet
title2: Mad Prophet
CR: 12
sources:
- name: NPC Codex
  page: 233
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Gnome
classes:
- cleric of the Old Cults 9
- Pathfinder chronicler 4
alignment: CE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 5
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 5
    dex: 1
    natural: 2
    size: 1
HP:
  HP: 97
  long: 9d8+4d8+35
saves:
  fort: 11
  ref: 7
  will: 13
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- live to tell the tale (2/day)
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 heavy mace +9/+4 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: +1 heavy mace
      bonus:
      - 9
      - 4
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - aura of madness (DC 18, 9 rounds/day)
  - bardic performance 7 rounds/day (countersong, distraction, epic tales, fascinate,
    inspire courage +1)
  - channel negative energy 8/day (DC 17, 5d6)
spell_like_abilities:
  entries:
  - name: lore keeper
    source: default
    freq: At will
  - name: remote viewing
    source: default
    freq: At will
    other: 9 rounds/day
  - name: vision of madness
    source: default
    freq: 7/day
  - name: dancing lights
    source: gnome
    freq: 1/day
  - name: ghost sound
    source: gnome
    freq: 1/day
  - name: prestidigitation
    source: gnome
    freq: 1/day
  - name: speak with animals
    source: gnome
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 13
  - name: gnome
    CL: 13
    concentration: 16
spells:
  entries:
  - name: slay living
    source: Cleric
    level: 5
    DC: 20
  - is_domain_spell: true
    name: true seeing
    source: Cleric
    level: 5
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 18
  - is_domain_spell: true
    name: confusion
    source: Cleric
    level: 4
    DC: 18
  - name: summon monster IV
    source: Cleric
    level: 4
  - name: tongues
    source: Cleric
    level: 4
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 18
  - name: invisibility purge
    source: Cleric
    level: 3
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
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 16
  - name: resist energy
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: touch of idiocy
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    DC: 16
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: entropic shield
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: lesser confusion
    source: Cleric
    level: 1
    DC: 15
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: detect poison
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 9
    concentration: 13
    slots:
      0: at-will
    domains:
    - knowledge
    - madness
tactics:
  During Combat: The Pathfinder chronicler drinks his potion of fly. While flying
    above his enemies, he activates his aura of madness, casts chaos hammer, and swoops
    down to cast slay living on spellcasters.
ability_scores:
  STR: 6
  DEX: 12
  CON: 12
  INT: 14
  WIS: 19
  CHA: 16
BAB: 9
CMB: 6
CMD: 17
feats:
- name: Combat Casting
- name: Command Undead
- name: Extra Channel
- name: Great Fortitude
- name: Improved Initiative
- name: Spell Focus (necromancy)
- name: Toughness
skills:
  Bluff: 11
  Diplomacy: 11
  Heal: 12
  Intimidate: 11
  Knowledge (arcana): 12
  Knowledge (dungeoneering): 12
  Knowledge (history): 12
  Knowledge (planes): 17
  Knowledge (religion): 17
  Linguistics: 8
  Perception: 17
  Perform (oratory): 11
  Profession (scribe): 14
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Gnome
- Sylvan
special_qualities:
- aura
- bardic knowledge +2
- deep pockets (400 gp)
- improved aid
- master scribe
- pathfinding
gear:
  combat:
  - potion of cure serious wounds
  - potion of fly
  - scroll of flame strike
  - scroll of summon monster V
  - scroll of summon monster VI
  other:
  - +2 studded leather
  - +1 heavy mace
  - amulet of natural armor +2
  - brooch of shielding
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - 363 gp
desc_long: These Pathfinders know some paths are twisted and mad.

---

# Mad Prophet

**Source** NPC Codex pg. 233
**XP** 19,200
Gnome _[[classes/Cleric|cleric]]_ of the Old Cults 9/Pathfinder chronicler 4
CE Small humanoid (gnome)
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 armor, +1 Dex, +2 natural, +1 size)
**hp** 97 (9d8+4d8+35)
**Fort** +11, **Ref** +7, **Will** +13; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 dodge bonus to AC vs. giants), live to tell the tale (2/day)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +9/+4 (1d6–1)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, aura of madness (DC 18, 9 rounds/day), bardic performance 7 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, epic tales, fascinate, inspire courage +1), channel negative energy 8/day (DC 17, 5d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
At will—lore keeper, _[[spells/Remote Viewing|remote viewing]]_ (9 rounds/day)
7/day—_[[spells/Vision|vision]]_ of madness
**Gnome _Spell-Like Abilities_** (CL 13th; concentration +16)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Cleric_ Spells Prepared **(CL 9th; concentration +13)
5th—_[[spells/Slay Living|slay living]]_ (DC 20), _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 18), _[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Summon Monster IV|summon monster IV]]_, _[[spells/Tongues|tongues]]_
3rd—blindness/deafness (DC 18), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Prayer|prayer]]_, _[[spells/Rage|rage]]_, _[[spells/Searing Light|searing light]]_
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Hold Person|hold person]]_ (2, DC 16), _[[spells/Resist Energy|resist energy]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Doom|doom]]_ (DC 16), _[[spells/Entropic Shield|entropic shield]]_, lesser _confusion_ (DC 15), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domains **Knowledge, Madness

### Tactics

**During Combat **The _[[npcs/Pathfinder Chronicler|Pathfinder chronicler]]_ drinks his potion of fly. While flying above his enemies, he activates his aura of madness, casts _chaos hammer_, and swoops down to cast _slay living_ on spellcasters.

##### Statistics
**Str** 6, **Dex** 12, **Con** 12, **Int** 14, **Wis** 19, **Cha** 16
**Base Atk** +9; **CMB** +6; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Toughness|Toughness]]_
**Skills** Bluff +11, Diplomacy +11, _[[spells/Heal|Heal]]_ +12, Intimidate +11, Knowledge (arcana, dungeoneering, history) +12, Knowledge (planes, religion) +17, Linguistics +8, Perception +17, Perform (oratory) +11, Profession (scribe) +14
**Languages** Abyssal, Aklo, Common, Draconic, Gnome, Sylvan
**SQ** aura, bardic knowledge +2, deep pockets (400 gp), improved aid, master scribe, pathfinding
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of fly, scroll of _[[spells/Flame Strike|flame strike]]_, scroll of _[[spells/Summon Monster V|summon monster V]]_, scroll of _[[spells/Summon Monster VI|summon monster VI]]_; **Other Gear** +2 studded leather, +1 _heavy mace_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, 363 gp

These Pathfinders know some paths are twisted and mad.