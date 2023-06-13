---
cssclass: [monsters]
title1: Lich, Psychic Lich
desc_short: This gaunt, ghoulish figure's skin is inscribed with faintly glowing runes.
  Short-lived afterimages trail behind it.
title2: Psychic Lich
CR: 12
sources:
- name: Occult Bestiary
  page: 33
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 19200
race: Human
classes:
- psychic lich psychic 11 (Pathfinder RPG Occult Adventures 60)
alignment: LE
size: Medium
type: undead
subtypes:
- augmented humanoid
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 15
  flat_footed: 19
  components:
    deflection: 1
    dex: 1
    natural: 5
    wis: 3
HP:
  HP: 96
  long: 11d6+55
saves:
  fort: 8
  ref: 8
  will: 12
defensive_abilities:
- channel resistance +4
- psychic feast
- rejuvenation
DR:
- amount: 15
  weakness: bludgeoning and magic
immunities:
- cold
- electricity
- undead traits
weaknesses:
- mind-affecting effects
speeds:
  base: 30
attacks:
  melee:
  - - text: touch +4 (1d8+5 plus bewildering touch)
      entries:
      - - damage: 1d8+5
        - effect: bewildering touch
      attack: touch
      bonus:
      - 4
  - - text: sickle +4 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: sickle
      bonus:
      - 4
    - text: touch -1 (1d8+5 plus bewildering touch)
      entries:
      - - damage: 1d8+5
        - effect: bewildering touch
      attack: touch
      bonus:
      - -1
  special:
  - bewildering touch (DC 18)
  - phrenic amplifications (defensive prognostication, ongoing defense, overpowering
    mind, space-rending spell)
  - phrenic pool (8 points)
  - physical push (+3, 3/day)
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: 1/day
    DC: 17
  - name: telepathic bond
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 11
    concentration: 17
spells:
  entries:
  - superscripts:
    - UM
    name: echolocation
    source: Psychic
    level: 5
  - name: mind fog
    source: Psychic
    level: 5
    DC: 21
  - superscripts:
    - OA
    name: synapse overload
    source: Psychic
    level: 5
    DC: 21
  - superscripts:
    - UM
    name: aura of doom
    source: Psychic
    level: 4
    DC: 20
  - name: freedom of movement
    source: Psychic
    level: 4
  - superscripts:
    - OA
    name: id insinuation III
    source: Psychic
    level: 4
    DC: 20
  - superscripts:
    - OA
    name: mental barrier III
    source: Psychic
    level: 4
  - name: dispel magic
    source: Psychic
    level: 3
  - name: fly
    source: Psychic
    level: 3
  - name: haste
    source: Psychic
    level: 3
  - superscripts:
    - OA
    name: mind thrust III
    source: Psychic
    level: 3
    DC: 19
  - superscripts:
    - OA
    name: synaptic pulse
    source: Psychic
    level: 3
    DC: 19
  - name: bear's endurance
    source: Psychic
    level: 2
  - name: blur
    source: Psychic
    level: 2
  - name: calm emotions
    source: Psychic
    level: 2
    DC: 18
  - name: false life
    source: Psychic
    level: 2
  - superscripts:
    - OA
    name: mental block
    source: Psychic
    level: 2
  - name: resist energy
    source: Psychic
    level: 2
  - superscripts:
    - UM
    name: ear-piercing scream
    source: Psychic
    level: 1
    DC: 17
  - name: expeditious retreat
    source: Psychic
    level: 1
  - name: mage armor
    source: Psychic
    level: 1
  - name: magic missile
    source: Psychic
    level: 1
  - superscripts:
    - OA
    name: mindlink
    source: Psychic
    level: 1
  - name: shield
    source: Psychic
    level: 1
  - name: arcane mark
    source: Psychic
    level: 0
  - name: dancing lights
    source: Psychic
    level: 0
  - name: detect magic
    source: Psychic
    level: 0
  - superscripts:
    - OA
    name: detect psychic significance
    source: Psychic
    level: 0
  - name: ghost sound
    source: Psychic
    level: 0
    DC: 16
  - name: mage hand
    source: Psychic
    level: 0
  - name: message
    source: Psychic
    level: 0
  - name: prestidigitation
    source: Psychic
    level: 0
    DC: 16
  - name: read magic
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 11
    concentration: 17
    slots:
      5: 4
      4: 6
      3: 7
      2: 7
      1: 7
      0: at-will
    psychic_discipline: self-perfection
ability_scores:
  STR: 8
  DEX: 12
  CON:
  INT: 22
  WIS: 16
  CHA: 16
BAB: 5
CMB: 4
CMD: 22
feats:
- name: Craft Wondrous Item
- name: Defensive Combat Training
- name: Improved Initiative
- superscripts:
  - OA
  name: Intuitive Spell
- name: Lightning Reflexes
- is_bonus: true
  name: Psychic Combatant
- is_bonus: true
  name: Psychic Defender
- name: Quicken Spell
- name: Toughness
skills:
  Bluff: 17
  Disguise: 12
  Intimidate: 15
  Knowledge (arcana): 20
  Knowledge (history): 20
  Linguistics: 20
  Perception: 11
  Perform (oratory): 10
  Sense Motive: 25
  Spellcraft: 20
  Stealth: 23
  _racial_mods:
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Abyssal
- Aklo
- Azlanti
- Celestial
- Common
- Draconic
- Dwarven
- Elven
- Giant
- Gnome
- Halfling
- Infernal
- Osiriani
- Skald
- Sylvan
- Undercommon
- Varisian
- Vudrani
special_qualities:
- bodily purge (6d8)
- detect thoughts
- telepathic bond
ecology:
  environment: any
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - sickle
  - cloak of resistance +2
  - headband of vast intelligence +2 [Stealth]
  - ring of counterspells [dispel magic]
  - ring of protection +1
  - robe of blending
  - scroll of invisibility
  - other treasure
desc_long: While some liches prefer to spend undeath's eternity in seclusion, a psychic
  lich sustains its life force by embracing its personal accomplishments to create
  a powerful astral echo of itself. Even more megalomaniacal than most liches, psychic
  liches resemble ordinary liches for the most part, but their every moment is attended
  by ghostly images of past cruelties, a constantly rotating illusory display of the
  evil deeds that brought them their power. Most psychic liches are humans, or come
  from other races renowned for their psychic abilities.

---

# Lich, Psychic Lich
This gaunt, ghoulish figure’s skin is inscribed with faintly glowing runes. Short-lived afterimages trail behind it.
**Source** Occult Bestiary pg. 33
**XP** 19,200
Human _[[classes/Psychic|psychic]]_ _[[monsters/Lich|lich]]_ _psychic_ 11 (Pathfinder RPG Occult Adventures 60)

LE Medium undead (augmented humanoid)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+1 _[[spells/Deflection|deflection]]_, +1 Dex, +5 natural, +3 Wis)
**hp** 96 (11d6+55)
**Fort** +8, **Ref** +8, **Will** +12
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _psychic_ feast, rejuvenation; **DR** 15/bludgeoning and magic; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** mind-affecting effects

##### Offense
**Speed** 30 ft.
**Melee** touch +4 (1d8+5 plus _[[items/Weapon Magic Abilities/Bewildering|bewildering]]_ touch) or _[[items/Weapon/Sickle|sickle]]_ +4 (1d6–1), touch –1 (1d8+5 plus _bewildering_ touch)
**Special Attacks** _bewildering_ touch (DC 18), phrenic amplifications (defensive _[[spells/Prognostication|prognostication]]_, ongoing defense, overpowering mind, space-rending spell), phrenic pool (8 points), physical push (+3, 3/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +17)
1/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Telepathic Bond|telepathic bond]]_
**_Psychic_ Spells Known **(CL 11th; concentration +17)
5th (4/day)— _[[spells/Echolocation|echolocation]]_, _[[spells/Mind Fog|mind fog]]_ (DC 21), _[[spells/Synapse Overload|synapse overload]]_ (DC 21)
4th (6/day)—_[[spells/Aura of Doom|aura of doom]]_ (DC 20), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Id Insinuation III|id insinuation III]]_ (DC 20), _[[spells/Mental Barrier III|mental barrier III]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Haste|haste]]_, _[[spells/Mind Thrust III|mind thrust III]]_ (DC 19), _[[spells/Synaptic Pulse|synaptic pulse]]_ (DC 19)
2nd (7/day)— bear’s _[[feats/Endurance|endurance]]_, _[[spells/Blur|blur]]_, _[[spells/Calm Emotions|calm emotions]]_ (DC 18), _[[spells/False Life|false life]]_, _[[spells/Mental Block|mental block]]_, _[[spells/Resist Energy|resist energy]]_
1st (7/day)—_[[spells/Ear-Piercing Scream|ear-piercing scream]]_ (DC 17), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Mindlink|mindlink]]_, _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect _Psychic_ Significance|detect _psychic_ significance]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 16), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_ (DC 16), _[[spells/Read Magic|read magic]]_
**_Psychic_ Discipline** self-perfection

##### Statistics
**Str** 8, **Dex** 12, **Con** —, **Int** 22, **Wis** 16, **Cha** 16
**Base Atk** +5; **CMB** +4; **CMD** 22
**Feats** _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intuitive Spell|Intuitive Spell]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Psychic Combatant|Psychic Combatant]]_, _[[feats/Psychic Defender|Psychic Defender]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +17, Disguise +12, Intimidate +15, Knowledge (arcana) +20, Knowledge (history) +20, Linguistics +20, Perception +11, Perform (oratory) +10, Sense Motive +25, Spellcraft +20, Stealth +23; **Racial Modifiers** +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Abyssal, Aklo, Azlanti, Celestial, Common, Draconic, Dwarven, Elven, Giant, Gnome, Halfling, Infernal, Osiriani, _[[classes/Skald|Skald]]_, Sylvan, Undercommon, Varisian, Vudrani
**SQ** bodily purge (6d8), _detect thoughts_, _telepathic bond_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** NPC gear (_sickle_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_ [Stealth], _[[items/Ring/Ring of Counterspells|ring of counterspells]]_ [dispel magic], _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Wondrous Item/Robe of Blending|robe of blending]]_, scroll of _[[spells/Invisibility|invisibility]]_, other treasure)

##### Description

While some liches prefer to spend undeath’s eternity in seclusion, a _psychic_ _lich_ sustains its life force by embracing its personal accomplishments to create a powerful astral _[[spells/Echo|echo]]_ of itself. Even more megalomaniacal than most liches, _psychic_ liches resemble ordinary liches for the most part, but their every moment is attended by ghostly images of past cruelties, a constantly rotating illusory display of the evil deeds that brought them their power. Most _psychic_ liches are humans, or come from other races renowned for their _psychic_ abilities.