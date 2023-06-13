---
cssclass: [monsters]
title1: Scyld Hranni, Storm Giant Matriarch
desc_short: This purple-haired giant has dark bronze skin and piercing eyes; she wields
  an electrified trident and a coral-encrusted shield.
title2: Scyld Hranni, Storm Giant Matriarch
CR: 20
sources:
- name: Giants Revisited
  page: 56
  link: http://paizo.com/products/btpy8rv4?Pathfinder-Campaign-Setting-Giants-Revisited
XP: 307200
race: Female
classes:
- storm giant cleric of Aegirran 13
alignment: CG
size: Huge
type: humanoid
subtypes:
- giant
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 37
  touch: 12
  flat_footed: 33
  components:
    armor: 8
    dex: 4
    natural: 12
    shield: 5
    size: -2
HP:
  HP: 380
  long: 19d8+13d8+237
  HD: 32
saves:
  fort: 26
  ref: 14
  will: 24
defensive_abilities:
- rock catching
immunities:
- electricity
speeds:
  base: 60
  swim: 40
  swim_other: 45 ft., swim 40 ft. in armor
attacks:
  melee:
  - - text: +3 shocking burst trident +40/+35/+30/+25 (3d6+18/19-20)
      entries:
      - - damage: 3d6+18
          crit_range: 19-20
      attack: +3 shocking burst trident
      bonus:
      - 40
      - 35
      - 30
      - 25
  - - text: 2 slams +36 (2d6+15)
      entries:
      - - damage: 2d6+15
      count: 2
      attack: slams
      bonus:
      - 36
  ranged:
  - - text: +1 seeking composite longbow +26/+21/+16/+11 (3d6+16/×3)
      entries:
      - - damage: 3d6+16
          crit_multiplier: 3
      attack: +1 seeking composite longbow
      bonus:
      - 26
      - 21
      - 16
      - 11
  special:
  - channel positive energy 6/day (DC 19, 7d6)
  - gale aura
  - surge
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: control weather
    source: default
    freq: 2/day
  - name: levitate
    source: default
    freq: 2/day
  - name: call lightning
    source: default
    freq: 1/day
    DC: 16
  - name: chain lightning
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 15
    concentration: 18
spells:
  entries:
  - is_domain_spell: true
    name: elemental body IV
    source: Cleric
    level: 7
    other: water only
  - name: holy word
    source: Cleric
    level: 7
    DC: 27
  - name: waves of ecstasy
    source: Cleric
    level: 7
    DC: 27
  - name: antilife shell
    source: Cleric
    level: 6
  - name: banishment
    source: Cleric
    level: 6
    DC: 26
  - name: cold ice strike
    source: Cleric
    level: 6
    DC: 26
  - name: heal
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: sirocco
    source: Cleric
    level: 6
    DC: 26
  - is_domain_spell: true
    name: call lightning storm
    source: Cleric
    level: 5
    DC: 25
  - name: cleanse
    source: Cleric
    level: 5
  - name: greater forbid action
    source: Cleric
    level: 5
    DC: 25
  - name: holy ice
    source: Cleric
    level: 5
    DC: 25
  - name: righteous might
    source: Cleric
    level: 5
  - name: true seeing
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: aura of doom
    source: Cleric
    level: 4
    DC: 24
  - name: blessing of fervor
    source: Cleric
    level: 4
    DC: 24
  - is_domain_spell: true
    name: control water
    source: Cleric
    level: 4
  - name: death ward
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 24
  - name: divination
    source: Cleric
    level: 4
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 23
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 23
  - name: create food and water
    source: Cleric
    level: 3
  - name: daylight
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: water walk
    source: Cleric
    level: 3
  - name: augury
    source: Cleric
    level: 2
  - name: compassionate ally
    source: Cleric
    level: 2
    DC: 22
  - name: grace
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 22
  - name: silence
    source: Cleric
    level: 2
    DC: 22
  - is_domain_spell: true
    name: slipstream
    source: Cleric
    level: 2
    DC: 22
  - name: sound burst
    source: Cleric
    level: 2
    DC: 22
  - name: zone of truth
    source: Cleric
    level: 2
    DC: 22
  - name: command
    source: Cleric
    level: 1
    DC: 21
  - name: divine favor
    source: Cleric
    level: 1
  - name: murderous command
    source: Cleric
    level: 1
    DC: 21
  - is_domain_spell: true
    name: obscuring mist
    source: Cleric
    level: 1
  - name: protection from evil
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 21
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
  - name: purify food and drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 13
    concentration: 23
    slots:
      0: at-will
    domains:
    - water (oceans subdomain)
    - weather (storms subdomain)
ability_scores:
  STR: 40
  DEX: 18
  CON: 25
  INT: 16
  WIS: 30
  CHA: 17
BAB: 23
CMB: 40
CMD: 54
feats:
- name: Bashing Finish
- name: Channel Smite
- name: Combat Casting
- name: Critical Focus
- name: Deafening Critical
- name: Improved Critical (trident)
- name: Improved Shield Bash
- name: Missile Shield
- name: Point- Blank Shot
- name: Power Attack
- name: Rapid Shot
- name: Shield Master
- name: Shield Slam
- name: Staggering Critical
- name: Two-Weapon Fighting
- name: Weapon Focus (trident)
skills:
  Acrobatics: 22
    when jumping: 26
  Climb: 36
  Diplomacy: 26
  Intimidate: 26
  Knowledge (history): 16
  Knowledge (religion): 16
  Perception: 33
  Sense Motive: 33
  Spellcraft: 16
  Swim: 31
languages:
- Auran
- Common
- Draconic
- Giant
special_qualities:
- militant
- water breathing
gear:
  combat:
  - potion of cure serious wounds
  - potion of haste
  - scroll of commune
  - scroll of invisibility purge
  other:
  - +2 mithral moderate fortification chainmail
  - +3 spiked bashing heavy wooden shield
  - +1 seeking composite longbow with 40 arrows
  - +3 shocking burst trident
  - belt of giant strength +2
  - boots of striding and springing
  - headband of inspired wisdom +4
  - minor cloak of displacement
  - wooden holy symbol of Aegirran
desc_long: Scyld Hranni is a revered storm giant warrior, her family originally hailing
  from a small islet just west of the island of Thuryan in Cheliax. The Hranni family
  gave up their holdings not long after Cheliax bound their fate to the devils of
  Hell, and since their disbanding, Scyld has searched for purpose amid the vast waters
  of the Arcadian Ocean, traveling along the coast of southern Avistan and northern
  Garund. Other storm giants regard her violet hair as a sign of being blessed by
  the gods, a notion she encourages through her devoted worship of Aegirran. Clad
  in sleek mithral armor and a barnacle-encrusted shield of driftwood and jagged coral,
  Scyld trains the myriad sea creatures of the Arcadian Ocean to help her in her search
  for purpose and her ambitions of eliminating evil throughout the region.

---

# Scyld Hranni, Storm Giant Matriarch
This purple-haired giant has dark bronze skin and piercing eyes; she wields an electrified _[[items/Weapon/Trident|trident]]_ and a coral-encrusted _[[spells/Shield|shield]]_.
**Source** Giants Revisited pg. 56
**XP** 307,200
Female storm giant _[[classes/Cleric|cleric]]_ of Aegirran 13

CG Huge humanoid (giant)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +33

##### Defense

**AC** 37, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+8 armor, +4 Dex, +12 natural, +5 _shield_, –2 size)
**hp** 380 (32 HD; 19d8+13d8+237)
**Fort** +26, **Ref** +14, **Will** +24
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** electricity

##### Offense
**Speed** 60 ft., swim 40 ft. (45 ft., swim 40 ft. in armor)
**Melee** +3 _[[items/Weapon Magic Abilities/Shocking Burst|shocking burst]]_ _trident_ +40/+35/+30/+25 (3d6+18/19–20) or 2 slams +36 (2d6+15)
**Ranged** +1 seeking _[[items/Weapon/Composite longbow|composite longbow]]_ +26/+21/+16/+11 (3d6+16/×3)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** channel positive energy 6/day (DC 19, 7d6), gale aura*, surge*
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
Constant—_[[spells/Freedom of Movement|freedom of movement]]_
2/day—_[[spells/Control Weather|control weather]]_, _[[spells/Levitate|levitate]]_
1/day—_[[spells/Call Lightning|call lightning]]_ (DC 16), _[[spells/Chain Lightning|chain lightning]]_ (DC 19)
**_Cleric_ Spells Prepared **(CL 13th; concentration +23)
7th—_[[spells/Elemental Body IV|elemental body IV]]_  (water only), _[[spells/Holy Word|holy word]]_ (DC 27), _[[spells/Waves of Ecstasy|waves of ecstasy]]_ (DC 27)
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Banishment|banishment]]_ (DC 26), _[[spells/Cold Ice Strike|cold ice strike]]_** (DC 26), _[[spells/Heal|heal]]_, _[[spells/Sirocco|sirocco]]_* (DC 26)
5th—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 25), _[[spells/Cleanse|cleanse]]_, greater _[[spells/Forbid Action|forbid action]]_** (DC 25), _[[spells/Holy Ice|holy ice]]_** (DC 25), _[[spells/Righteous Might|righteous might]]_, _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Aura of Doom|aura of doom]]_** (DC 24), _[[spells/Blessing Of Fervor|blessing of fervor]]_* (DC 24), _[[spells/Control Water|control water]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Dismissal|dismissal]]_ (DC 24), _[[spells/Divination|divination]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 23), blindness/deafness (DC 23), _[[spells/Create Food and Water|create food and water]]_, _[[spells/Daylight|daylight]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Water Walk|water walk]]_
2nd—_[[spells/Augury|augury]]_, _[[spells/Compassionate Ally|compassionate ally]]_** (DC 22), _[[spells/Grace|grace]]_*, _[[spells/Hold Person|hold person]]_ (DC 22), _[[spells/Silence|silence]]_ (DC 22), _[[spells/Slipstream|slipstream]]_ (DC 22), _[[spells/Sound Burst|sound burst]]_ (DC 22), _[[spells/Zone of Truth|zone of truth]]_ (DC 22)
1st—_[[spells/Command|command]]_ (DC 21), _[[spells/Divine Favor|divine favor]]_, _[[spells/Murderous Command|murderous command]]_** (DC 21), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 21), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_
**D** Domain spell; **Domains **Water (Oceans subdomain*), Weather (Storms subdomain*)

##### Statistics
**Str** 40, **Dex** 18, **Con** 25, **Int** 16, **Wis** 30, **Cha** 17
**Base Atk** +23; **CMB** +40; **CMD** 54
**Feats** _[[feats/Bashing Finish|Bashing Finish]]_*, _[[feats/Channel Smite|Channel Smite]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deafening Critical|Deafening Critical]]_, _[[feats/Improved Critical|Improved Critical]]_ (_trident_), _[[feats/Improved _Shield_ Bash|Improved _Shield_ Bash]]_, _[[feats/Missile Shield|Missile Shield]]_*, Point- Blank Shot, _[[feats/Power Attack|Power Attack]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Shield Master|Shield Master]]_, _[[feats/Shield Slam|Shield Slam]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_trident_)
**Skills** Acrobatics +22 (+26 when jumping), _[[universal monster rules/Climb|Climb]]_ +36, Diplomacy +26, Intimidate +26, Knowledge (history) +16, Knowledge (religion) +16, Perception +33, Sense Motive +33, Spellcraft +16, Swim +31
**Languages** Auran, Common, Draconic, Giant
**SQ** militant, _[[universal monster rules/Water Breathing|water breathing]]_
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _[[spells/Haste|haste]]_, scroll of _[[spells/Commune|commune]]_, scroll of _[[spells/Invisibility Purge|invisibility purge]]_; **Other Gear** +2 mithral moderate _[[universal monster rules/Fortification|fortification]]_ _[[items/Armor/Chainmail|chainmail]]_, +3 spiked _[[items/Armor Magic Abilities/Bashing|bashing]]_ _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 seeking _composite longbow_ with 40 arrows, +3 _shocking burst_ _trident_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, minor cloak of _[[spells/Displacement|displacement]]_, wooden holy symbol of Aegirran 
* See the Advanced Player’s Guide. 
** See Ultimate Magic.

##### Description

Scyld Hranni is a revered storm giant warrior, her family originally hailing from a small islet just west of the island of Thuryan in Cheliax. The Hranni family gave up their holdings not long after Cheliax bound their fate to the devils of Hell, and since their disbanding, Scyld has searched for purpose amid the vast waters of the Arcadian Ocean, traveling along the coast of southern Avistan and northern Garund. Other storm giants regard her violet hair as a sign of being _[[feats/Blessed|blessed]]_ by the gods, a notion she encourages through her devoted worship of Aegirran. Clad in sleek mithral armor and a barnacle-encrusted _shield_ of driftwood and jagged coral, Scyld trains the myriad sea creatures of the Arcadian Ocean to help her in her search for purpose and her ambitions of eliminating evil throughout the region.