---
cssclass: [monsters]
title1: Agathion, Draconal
desc_short: 'This noble creature seems to be part serpent, part humanoid, and part
  dragon, with great wings and a crown of horns. '
title2: Draconal
CR: 20
sources:
- name: Bestiary 2
  page: 18
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: NG
size: Large
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: 6
senses:
  blindsense: 60
  darkvision: 120
  low-light vision: true
auras:
- name: protective aura
  radius: 20
AC:
  AC: 36
  touch: 18
  flat_footed: 33
  other: +4 deflection vs. evil
  components:
    dex: 2
    dodge: 1
    insight: 6
    natural: 18
    size: -1
HP:
  HP: 324
  long: 24d10+192
  regeneration: 10
  regeneration_weakness: evil weapons and spells
saves:
  fort: 22
  ref: 16
  will: 17
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 15
  weakness: evil and silver
immunities:
- one energy type (see Celestial Focus)
- electricity
- petrification
resistances:
  cold: 10
  sonic: 10
SR: 31
speeds:
  base: 40
  fly: 120
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +36 (2d6+13 plus 1d6 energy)
      entries:
      - - damage: 2d6+13
        - damage: 1d6
          type: energy
      attack: bite
      bonus:
      - 36
    - text: 2 claws +31 (1d8+6 plus 1d6 energy)
      entries:
      - - damage: 1d8+6
        - damage: 1d6
          type: energy
      count: 2
      attack: claws
      bonus:
      - 31
  special:
  - breath weapon (120-ft. line, 20d6 energy damage, Reflex DC 30 half, usable once
    every 1d4 rounds)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: Constant
  - name: beast shape II
    source: default
    freq: At will
  - name: command
    source: default
    freq: At will
    DC: 17
  - name: detect thoughts
    source: default
    freq: At will
  - name: elemental body III
    source: default
    freq: At will
    other: air or water elementals only
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: gust of wind
    source: default
    freq: At will
  - name: hold monster
    source: default
    freq: At will
    DC: 20
  - name: identify
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: lightning bolt
    source: default
    freq: At will
    DC: 19
  - name: mage hand
    source: default
    freq: At will
  - name: message
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: 7/day
  - name: cure serious wounds
    source: default
    freq: 7/day
  - name: neutralize poison
    source: default
    freq: 7/day
  - name: remove disease
    source: default
    freq: 7/day
  - name: control water
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 3/day
  - name: control winds
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    DC: 23
  sources:
  - name: default
    CL: 24
    concentration: 30
spells:
  entries:
  - name: implosion
    source: Cleric
    level: 9
    DC: 26
  - is_domain_spell: true
    name: storm of vengeance
    source: Cleric
    level: 9
    DC: 26
  - is_domain_spell: true
    name: demand
    source: Cleric
    level: 8
  - name: earthquake
    source: Cleric
    level: 8
  - name: quickened holy smite
    source: Cleric
    level: 8
    DC: 21
  - name: empowered breath of life
    source: Cleric
    level: 7
  - name: empowered flame strike
    source: Cleric
    level: 7
    DC: 22
  - name: holy word
    source: Cleric
    level: 7
    DC: 24
  - name: quickened invisibility purge
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: repulsion
    source: Cleric
    level: 7
    DC: 24
  - name: animate objects
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: blade barrier
    source: Cleric
    level: 6
    DC: 23
  - name: find the path
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: heroes' feast
    source: Cleric
    level: 6
  - name: quickened remove paralysis
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: dispel evil
    source: Cleric
    level: 5
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
  - name: greater command
    source: Cleric
    level: 5
    DC: 22
  - name: spell resistance
    source: Cleric
    level: 5
  - name: true seeing
    source: Cleric
    level: 5
  - name: cure critical wounds
    source: Cleric
    level: 4
    count: 3
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: holy smite
    source: Cleric
    level: 4
    DC: 21
  - name: repel vermin
    source: Cleric
    level: 4
    DC: 21
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 20
  - name: daylight
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: helping hand
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: good only
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 19
  - name: enthrall
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 19
  - name: lesser restoration
    source: Cleric
    level: 2
    count: 2
  - name: shield other
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: detect undead
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: divine favor
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 18
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: purify food and drink
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
    domains:
    - good
    - nobility
ability_scores:
  STR: 36
  DEX: 15
  CON: 27
  INT: 24
  WIS: 24
  CHA: 23
BAB: 24
CMB: 38
CMD: 57
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Greater Spell Penetration
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Power Attack
- name: Quicken Spell
- name: Skill Focus (Perception)
- name: Spell Penetration
skills:
  Acrobatics: 25
  Bluff: 29
  Diplomacy: 26
  Escape Artist: 22
  Heal: 27
  Intimidate: 29
  Knowledge (arcana): 30
  Knowledge (nature): 27
  Knowledge (planes): 34
  Knowledge (religion): 31
  Perception: 48
  Sense Motive: 34
  Spellcraft: 27
  Stealth: 21
  Use Magic Device: 26
  _racial_mods:
    Perception:
      _: 4
languages:
- Celestial
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- celestial focus
- divine insight
- lay on hands (10d6, 16/day, as a 20th-level paladin)
ecology:
  environment: any air (Nirvana)
  organization: solitary, pair, or flight (3-6)
  treasure_type: double
special_abilities:
  Celestial Focus (Ex): A draconal's color indicates aspects of its power and attunement
    to the powers of the good planes. These determine the draconal's breath weapon,
    the additional energy damage of its claw and bite attacks, additional resistances
    and immunities, and its additional domain choices (see Spells, below).
  Divine Insight (Su): A draconal adds its Charisma bonus as an insight bonus to Armor
    Class.
  Protective Aura (Su): Against attacks made or effects created by evil creatures,
    this ability provides a +4 deflection bonus to AC and a +4 resistance bonus on
    saving throws to anyone within 20 feet of the draconal. Otherwise, it functions
    as a magic circle against evil effect and a lesser globe of invulnerability, both
    with a radius of 20 feet (caster level equals draconal's HD). (The defensive benefits
    from the circle are not included in a draconal's stat block.)
  Spells: 'Draconals cast spells as 17th-level clerics. Like clerics, they have access
    to two domains, selecting from the following list: Air, Good, Nobility, Weather,
    and two additional domain options based on their color (see facing page). The
    majority of draconals choose Good and Nobility as their domains (as represented
    by this stat block). Draconals have a domain spell slot at each spell level but
    do not gain the granted powers of their chosen domains, nor do they gain access
    to other cleric abilities.'
desc_long: |-
  Draconals are mighty agathion lords, few in number and greatly removed from mortal affairs. They watch over powerful magic and are direct agents of the gods and the needs of the good planes. Patient and ageless, they plan for the long term, which often frustrates mortal creatures who seek to gain their assistance with a threat in the here and now. A draconal would rather support or enhance a group of heroes than tackle a problem directly, maintaining its focus on planar matters. 

  Draconals are attuned to nature and believe in cycles of life and death. Though they are good, they understand that the presence of evil gives good creatures something to strive against, preventing stagnation and complacency. This means their outlook sometimes appears almost neutral, though they hate suffering and needless death.

---

# Agathion, Draconal
This noble creature seems to be part serpent, part humanoid, and part dragon, with great wings and a crown of horns.

**Source** Bestiary 2 pg. 18
**XP** 307,200

NG Large outsider (agathion, extraplanar, good)
**Init** +6; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +48
**Aura** protective aura (20 ft.)

##### Defense

**AC** 36, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+2 Dex, +1 dodge, +6 insight, +18 natural, –1 size) (+4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 324 (24d10+192); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil weapons and spells)
**Fort** +22, **Ref** +16, **Will** +17; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 15/evil and silver; **Immune** one energy type (see Celestial Focus), electricity, petrification; **Resist** cold 10, sonic 10; **SR** 31

##### Offense
**Speed** 40 ft., fly 120 ft. (average)
**Melee** bite +36 (2d6+13 plus 1d6 energy), 2 claws +31 (1d8+6 plus 1d6 energy)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, 20d6 energy damage, Reflex DC 30 half, usable once every 1d4 rounds)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +30)
Constant—_[[spells/Speak with Animals|speak with animals]]_ 
At will—_[[spells/Beast Shape II|beast shape II]]_, _[[spells/Command|command]]_ (DC 17), _[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Elemental Body III|elemental body III]]_ (air or water elementals only), greater teleport (self plus 50 lbs. of objects only), _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Identify|identify]]_, light, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 19), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_ 
7/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Disease|remove disease]]_ 
3/day—_[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Control Winds|control winds]]_, _[[spells/Heal|heal]]_, _[[spells/Plane Shift|plane shift]]_ (DC 23)
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 17th; concentration +23)
9th—_[[spells/Implosion|implosion]]_ (DC 26), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 26)
8th—_[[spells/Demand|demand]]_, _[[spells/Earthquake|earthquake]]_, quickened _[[spells/Holy Smite|holy smite]]_ (DC 21)
7th—empowered _[[spells/Breath Of Life|breath of life]]_, empowered _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Holy Word|holy word]]_ (DC 24), quickened _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Repulsion|repulsion]]_ (DC 24)
6th—_[[spells/Animate Objects|animate objects]]_, _[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Find the Path|find the path]]_, _heal_, heroes’ feast, quickened _[[spells/Remove Paralysis|remove paralysis]]_
5th—_breath of life_, _[[spells/Dispel Evil|dispel evil]]_, _flame strike_ (DC 22), greater _command_ (DC 22), _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (3), _[[spells/Freedom of Movement|freedom of movement]]_, _holy smite_ (DC 21), _[[spells/Repel Vermin|repel vermin]]_ (DC 21)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Daylight|daylight]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Helping Hand|helping hand]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (good only), _[[spells/Calm Emotions|calm emotions]]_ (DC 19), _[[spells/Enthrall|enthrall]]_, _[[spells/Hold Person|hold person]]_ (DC 19), lesser _[[spells/Restoration|restoration]]_ (2), _[[spells/Shield Other|shield other]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Detect Undead|detect undead]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18), _[[spells/Shield Of Faith|shield of faith]]_
0—_[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D** domain spell; **Domains** Good, Nobility

##### Statistics
**Str** 36, **Dex** 15, **Con** 27, **Int** 24, **Wis** 24, **Cha** 23
**Base Atk** +24; **CMB** +38; **CMD** 57 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Acrobatics +25, Bluff +29, Diplomacy +26, Escape Artist +22, _Heal_ +27, Intimidate +29, Knowledge (arcana) +30, Knowledge (nature) +27, Knowledge (planes) +34, Knowledge (religion) +31, Perception +48, Sense Motive +34, Spellcraft +27, Stealth +21, Use Magic Device +26; **Racial Modifiers** +4 Perception
**Languages** Celestial, Draconic, Infernal; _speak with animals_, truespeech
**SQ** celestial focus, divine insight, lay on hands (10d6, 16/day, as a 20th-level _[[classes/Paladin|paladin]]_)

##### Ecology

**Environment** any air (Nirvana)
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–6)
**Treasure** double

### Special Abilities

**Celestial Focus (Ex) **A draconal’s color indicates aspects of its power and attunement to the powers of the good planes. These determine the draconal’s _breath weapon_, the additional energy damage of its claw and bite attacks, additional resistances and immunities, and its additional domain choices (see Spells, below).

**Divine Insight (Su)** A draconal adds its Charisma bonus as an insight bonus to Armor Class.

**Protective Aura (Su)** Against attacks made or effects created by evil creatures, this ability provides a +4 _deflection_ bonus to AC and a +4 _resistance_ bonus on saving throws to anyone within 20 feet of the draconal. Otherwise, it functions as a _[[spells/Magic Circle against Evil|magic circle against evil]]_ effect and a lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, both with a radius of 20 feet (caster level equals draconal’s HD). (The defensive benefits from the circle are not included in a draconal’s stat block.)
**Spells **Draconals cast spells as 17th-level clerics. Like clerics, they have access to two domains, selecting from the following list: Air, Good, Nobility, Weather, and two additional domain options based on their color (see facing page). The majority of draconals choose Good and Nobility as their domains (as represented by this stat block). Draconals have a domain spell slot at each spell level but do not gain the granted powers of their chosen domains, nor do they gain access to other _cleric_ abilities.

##### Description

Draconals are mighty agathion lords, few in number and greatly removed from mortal affairs. They watch over powerful magic and are direct agents of the gods and the needs of the good planes. Patient and ageless, they plan for the long term, which often frustrates mortal creatures who seek to gain their assistance with a threat in the here and now. A draconal would rather support or enhance a group of heroes than tackle a problem directly, maintaining its focus on _[[items/Weapon Magic Abilities/Planar|planar]]_ matters.

Draconals are attuned to nature and believe in cycles of life and death. Though they are good, they understand that the presence of evil gives good creatures something to strive against, preventing stagnation and complacency. This means their outlook sometimes appears almost neutral, though they hate suffering and needless death.