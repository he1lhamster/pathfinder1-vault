---
cssclass: [monsters]
title1: Diabolical Charmer
title2: Diabolical Charmer
CR: 14
sources:
- name: NPC Codex
  page: 172
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Human
classes:
- sorcerer 15
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
AC:
  AC: 21
  touch: 15
  flat_footed: 18
  other: +2 deflection vs. good
  components:
    armor: 4
    deflection: 2
    dex: 2
    dodge: 1
    natural: 2
HP:
  HP: 85
  long: 15d6+30
saves:
  fort: 7
  ref: 11
  will: 15
  other: +4 vs. poison
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
resistances:
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk quarterstaff +7/+2 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: mwk quarterstaff
      bonus:
      - 7
      - 2
spell_like_abilities:
  entries:
  - name: corrupting touch
    source: default
    freq: 9/day
    other: 7 rounds
  - name: hellfire
    source: default
    freq: 1/day
    other: 15d6 fire
    DC: 23
  sources:
  - name: default
    CL: 15
    concentration: 21
spells:
  entries:
  - name: delayed blast fireball
    source: Sorcerer
    level: 7
    DC: 24
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: summon monster VII
    source: Sorcerer
    level: 7
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 22
  - name: globe of invulnerability
    source: Sorcerer
    level: 6
  - name: mass suggestion
    source: Sorcerer
    level: 6
    DC: 22
  - name: planar binding
    source: Sorcerer
    level: 6
    other: devils/fiendish creatures only
    DC: 22
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 22
  - name: dismissal
    source: Sorcerer
    level: 5
    DC: 21
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 21
  - name: polymorph
    source: Sorcerer
    level: 5
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 22
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: wall of fire
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 20
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 19
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 19
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: darkness
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 18
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 18
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 19
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: protection from good
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 16
  - name: daze
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 16
  sources:
  - name: Sorcerer
    type: known
    CL: 15
    concentration: 21
    slots:
      7: 4
      6: 7
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
    bloodline: infernal
tactics:
  Before Combat: The sorcerer casts false life and stoneskin, and uses her wand of
    mage armor.
  During Combat: The sorcerer uses hellfire on the first round of combat, then uses
    controlling spells like dominate person, or damaging attacks such as black tentacles
    or cone of cold.
  Base Statistics: Without false life, mage armor, and stoneskin, the sorcerer's statistics
    are AC 17, touch 15, flat-footed 14; hp 70; DR none.
ability_scores:
  STR: 8
  DEX: 14
  CON: 10
  INT: 12
  WIS: 14
  CHA: 23
BAB: 7
CMB: 6
CMD: 21
feats:
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Extend Spell
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Persuasive
- name: Quicken Spell
- name: Spell Focus (evocation)
- name: Spell Penetration
skills:
  Bluff: 19
  Diplomacy: 23
  Fly: 10
  Intimidate: 23
  Knowledge (arcana): 9
  Knowledge (planes): 6
  Perception: 12
  Spellcraft: 9
languages:
- Common
- Infernal
special_qualities:
- bloodline arcana (+2 DC for charm spells)
- infernal resistances
- on dark wings
gear:
  combat:
  - potions of cure serious wounds (2)
  - scrolls of invisibility (2)
  - scroll of nondetection
  - wand of mage armor (20 charges)
  other:
  - masterwork quarterstaff
  - amulet of natural armor +2
  - cloak of resistance +2
  - headband of alluring charisma +4
  - ring of counterspells
  - ring of protection +2
  - diamond dust (worth 500 gp)
  - 1,675 gp
desc_long: The diabolical charmer uses magic and honeyed words to convince mortals
  and fiends to do her bidding.

---

# Diabolical Charmer

**Source** NPC Codex pg. 172
**XP** 38,400
Human _[[classes/Sorcerer|sorcerer]]_ 15

LE Medium humanoid (human)
**Init** +6; **Senses** Perception +12

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural) (+2 _deflection_ vs. good)
**hp** 85 (15d6+30)
**Fort** +7, **Ref** +11, **Will** +15; +4 vs. poison
**DR** 10/adamantine (150 points); **Resist** fire 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +7/+2 (1d6–1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
9/day—corrupting touch (7 rounds)
1/day—hellfire (15d6 fire, DC 23)
**_Sorcerer_ Spells Known **(CL 15th; concentration +21)
7th (4/day)—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 24), greater teleport, _[[spells/Summon Monster VII|summon monster VII]]_
6th (7/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 22), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 22), _[[spells/Planar Binding|planar binding]]_ (devils/fiendish creatures only, DC 22)
5th (7/day)—_[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Polymorph|polymorph]]_, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Charm Monster|charm monster]]_ (DC 22), _[[spells/Dimension Door|dimension door]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 20), _[[spells/Hold Person|hold person]]_ (DC 19), _suggestion_ (DC 19), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Darkness|darkness]]_, _[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_, web (DC 18)
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 18), _[[spells/Charm Person|charm person]]_ (DC 19), _[[spells/Magic Missile|magic missile]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 16)
**Bloodline **infernal

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _stoneskin_, and uses her wand of _[[spells/Mage Armor|mage armor]]_.
**During Combat **The _sorcerer_ uses hellfire on the first round of combat, then uses controlling spells like _dominate person_, or damaging attacks such as _black tentacles_ or _cone of cold_.
**Base Statistics **Without _false life_, _mage armor_, and _stoneskin_, the _sorcerer_’s statistics are **AC **17, touch 15, _flat-footed_ 14; **hp **70; **DR **none.

##### Statistics
**Str** 8, **Dex** 14, **Con** 10, **Int** 12, **Wis** 14, **Cha** 23
**Base Atk** +7; **CMB** +6; **CMD** 21
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Bluff +19, Diplomacy +23, Fly +10, Intimidate +23, Knowledge (arcana) +9, Knowledge (planes) +6, Perception +12, Spellcraft +9
**Languages** Common, Infernal
**SQ** bloodline arcana (+2 DC for charm spells), infernal resistances, on dark wings
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scrolls of _invisibility_ (2), scroll of _[[spells/Nondetection|nondetection]]_, wand of _mage armor_ (20 charges); **Other Gear** masterwork _quarterstaff_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Counterspells|ring of counterspells]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, diamond dust (worth 500 gp), 1,675 gp

The _[[npcs/Diabolical Charmer|diabolical charmer]]_ uses magic and honeyed words to convince mortals and fiends to do her bidding.