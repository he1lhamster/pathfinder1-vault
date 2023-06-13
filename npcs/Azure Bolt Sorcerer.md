---
cssclass: [monsters]
title1: Azure Bolt Sorcerer
title2: Azure Bolt Sorcerer
CR: 12
sources:
- name: NPC Codex
  page: 170
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- sorcerer 13
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
senses:
  see invisibility: true
AC:
  AC: 22
  touch: 15
  flat_footed: 19
  components:
    armor: 4
    deflection: 2
    dex: 2
    dodge: 1
    natural: 3
HP:
  HP: 141
  long: 13d6+93
saves:
  fort: 10
  ref: 10
  will: 9
resistances:
  electricity: 10
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +7 (1d6+1 plus 1d6 electricity)
      entries:
      - - damage: 1d6+1
        - damage: 1d6
          type: electricity
      count: 2
      attack: claws
      bonus:
      - 7
  - - text: mwk morningstar +8/+3 (1d8+1)
      entries:
      - - damage: 1d8+1
      attack: mwk morningstar
      bonus:
      - 8
      - 3
  ranged:
  - - text: mwk javelin +9 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: mwk javelin
      bonus:
      - 9
  special:
  - claws (2, 1d4+1 plus 1d6 electricity, treated as magic weapons, 8 rounds/day)
  - breath weapon (60-foot line, 13d6 electricity, DC 21, 1/day)
spells:
  entries:
  - name: acid fog
    source: Sorcerer
    level: 6
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 23
  - name: form of the dragon I
    source: Sorcerer
    level: 6
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 22
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 20
  - name: overland flight
    source: Sorcerer
    level: 5
  - name: spell resistance
    source: Sorcerer
    level: 5
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 19
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
    DC: 19
  - name: ice storm
    source: Sorcerer
    level: 4
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 20
  - name: fly
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 20
  - name: slow
    source: Sorcerer
    level: 3
    DC: 18
  - name: bear's endurance
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: gust of wind
    source: Sorcerer
    level: 2
    DC: 19
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: grease
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 16
  - name: shield
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 15
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 17
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 13
    concentration: 18
    slots:
      6: 4
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: draconic (blue)
tactics:
  Before Combat: The sorcerer casts bear's endurance, false life, fly, mage armor,
    and see invisibility.
  During Combat: The sorcerer prefers to fight with her electricity spells, such as
    chain lightning and lightning bolt, and saves her breath weapon until her foes
    are lined up so she can catch as many as possible in its effect. She uses spells
    such as black tentacles, grease, and ice storm to hinder her opponents. If forced
    into melee combat, the sorcerer casts haste and form of the dragon I.
  Base Statistics: Without bear's endurance, false life, fly, and mage armor, the
    sorcerer's statistics are AC 18, touch 15, flat-footed 15; hp 126; Fort +8; Speed
    30 ft.
ability_scores:
  STR: 12
  DEX: 14
  CON: 18
  INT: 10
  WIS: 8
  CHA: 21
BAB: 6
CMB: 7
CMD: 22
feats:
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Maximize Spell
- name: Mobility
- name: Quick Draw
- name: Spell Focus (evocation)
- name: Toughness
skills:
  Bluff: 12
  Fly: 10
  Intimidate: 20
  Knowledge (arcana): 7
  Linguistics: 1
  Perception: 11
  Spellcraft: 7
languages:
- Common
- Draconic
special_qualities:
- bloodline arcana (electricity spells deal +1 damage per die)
gear:
  combat:
  - potions of cure serious wounds (2)
  - wand of vampiric touch (10 charges)
  other:
  - masterwork javelins (2)
  - masterwork morningstar
  - amulet of natural armor +1
  - bag of holding (type I)
  - cloak of resistance +2
  - headband of alluring charisma +2
  - ring of protection +2
  - 1,839 gp
desc_long: An azure bolt sorcererbelieves she is smarter than she actually is, and
  spins wild schemes to make herself feel important.

---

# Azure Bolt Sorcerer

**Source** NPC Codex pg. 170
**XP** 19,200
Human _[[classes/Sorcerer|sorcerer]]_ 13

LE Medium humanoid (human)
**Init** +6; **Senses** _[[spells/See Invisibility|see invisibility]]_; Perception +11

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 141 (13d6+93)
**Fort** +10, **Ref** +10, **Will** +9
**Resist** electricity 10

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 claws +7 (1d6+1 plus 1d6 electricity) or mwk _[[items/Weapon/Morningstar|morningstar]]_ +8/+3 (1d8+1)
**Ranged** mwk _[[items/Weapon/Javelin|javelin]]_ +9 (1d6+1)
**Special Attacks** claws (2, 1d4+1 plus 1d6 electricity, treated as magic weapons, 8 rounds/day), _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-foot line, 13d6 electricity, DC 21, 1/day)
**_Sorcerer_ Spells Known **(CL 13th; concentration +18)
6th (4/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Form of the Dragon I|form of the dragon I]]_
5th (7/day)—_[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 20), _[[spells/Overland Flight|overland flight]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, _[[universal monster rules/Fear|fear]]_ (DC 19), _[[spells/Ice Storm|ice storm]]_
3rd (7/day)—_[[spells/Fireball|fireball]]_ (DC 20), fly, _[[spells/Haste|haste]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20), _[[spells/Slow|slow]]_ (DC 18)
2nd (7/day)—bear’s _[[feats/Endurance|endurance]]_, _[[spells/False Life|false life]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 19), _[[spells/Resist Energy|resist energy]]_, _[[spells/Scorching Ray|scorching ray]]_, _see invisibility_
1st (8/day)—_[[spells/Grease|grease]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 17), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline** draconic (blue)

### Tactics

**Before Combat **The _sorcerer_ casts bear’s _endurance_, _false life_, fly, _mage armor_, and _see invisibility_.
**During Combat **The _sorcerer_ prefers to fight with her electricity spells, such as _chain lightning_ and _lightning bolt_, and saves her _breath weapon_ until her foes are lined up so she can catch as many as possible in its effect. She uses spells such as _black tentacles_, _grease_, and _ice storm_ to _[[feats/Hinder|hinder]]_ her opponents. If forced into melee combat, the _sorcerer_ casts _haste_ and _form of the dragon I_.
**Base Statistics **Without bear’s _endurance_, _false life_, fly, and _mage armor_, the _sorcerer_’s statistics are **AC **18, touch 15, _flat-footed_ 15; **hp **126; **Fort **+8; **Speed **30 ft.

##### Statistics
**Str** 12, **Dex** 14, **Con** 18, **Int** 10, **Wis** 8, **Cha** 21
**Base Atk** +6; **CMB** +7; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_
**Skills** Bluff +12, Fly +10, Intimidate +20, Knowledge (arcana) +7, Linguistics +1, Perception +11, Spellcraft +7
**Languages** Common, Draconic
**SQ** bloodline arcana (electricity spells deal +1 damage per die)
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), wand of _[[spells/Vampiric Touch|vampiric touch]]_ (10 charges); **Other Gear** masterwork javelins (2), masterwork _morningstar_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, bag of holding (type I), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 1,839 gp

An azure bolt sorcererbelieves she is smarter than she actually is, and spins wild schemes to make herself feel important.