---
cssclass: [monsters]
title1: Asura, Vayuphak
desc_short: This blue-skinned humanoid has two pairs of ebony wings protruding from
  its waist. Talon-like nails grace its hands.
title2: Vayuphak
CR: 5
sources:
- name: Occult Bestiary
  page: 8
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 1600
alignment: LE
size: Medium
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 3
senses:
  darkvision: 60
auras:
- name: elusive
  radius: 30
- name: mental static
  radius: 30
  DC: 18
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    dex: 3
    dodge: 1
    natural: 4
HP:
  HP: 52
  long: 8d10+8
  fast_healing: 5
saves:
  fort: 3
  ref: 11
  will: 9
  other: +2 vs. enchantments
defensive_abilities:
- enveloping winds
- DR 5/cold iron or good
immunities:
- curse effects
- disease
- poison
resistances:
  acid: 10
  electricity: 10
SR: 16
speeds:
  base: 30
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: mwk spear +12/+7 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 12
      - 7
    - text: 2 wings +6 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 2
      attack: wings
      bonus:
      - 6
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: vayuphak
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 5
    concentration: 9
psychic_magic:
  entries:
  - name: dispel magic
    PE: 3
  - superscripts:
    - OA
    name: id insinuation I
    PE: 2
    DC: 16
  - superscripts:
    - OA
    name: object reading
    PE: 1
  - name: scorching ray
    PE: 2
  sources:
  - name: default
    CL: 5
    concentration: 9
  PE: 7
ability_scores:
  STR: 16
  DEX: 16
  CON: 13
  INT: 15
  WIS: 16
  CHA: 19
BAB: 8
CMB: 11
CMD: 25
feats:
- name: Dodge
- name: Flyby Attack
- name: Lightning Reflexes
- name: Mobility
skills:
  Acrobatics: 13
  Bluff: 15
  Diplomacy: 10
  Escape Artist: 15
  Fly: 15
  Intimidate: 12
  Knowledge (planes): 10
  Perception: 18
  Perform (dance): 13
  Spellcraft: 9
  Stealth: 10
  _racial_mods:
    Escape Artist:
      _: 6
    Perception:
      _: 4
languages:
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or band (3-12)
  treasure_type: standard
  treasure:
  - mwk spear
  - other treasure
special_abilities:
  Enveloping Winds (Su): As an immediate action, a vayuphak can surround itself with
    a whirling torrent of air to protect it from ranged attacks. All ranged attacks
    made with physical weapons have a 20% miss chance against the vayuphak, except
    for attacks from massive weapons such as a giant's thrown rock or a ballista.
    This ability has no effect on ray attacks.
desc_long: |-
  Vayuphaks, or “golden ones,” are asuras who serve as guardians and stewards of desecrated holy places. Whenever asuras descend to pollute a sanctified place, vayuphaks remain behind, defending the once-sacred site from those who might reclaim it. Many make twisted mockeries out of their conquests, forming tainted kingdoms and faithless monasteries that ape the edifices of the virtuous who once occupied the area, compounding the pain of loss with outrage at their vicious parodies. Otherwise, vayuphaks spend much of their vigil in silent meditation, honing their thoughts and minds into deadly weapons. They are fearsome when roused to battle, though they prefer insinuating themselves into opponents' minds over direct, physical confrontation.

  Legends claim vayuphaks were created from a divine servant who was tasked with guarding a treasure that signified the deity's favor. After countless followers of the god slaughtered each other while attempting to obtain the prize, the enraged deity cursed the artifact so that all who looked upon it would be driven mad. The unwitting divine servant was the first victim, and wracked with madness, he claimed the treasure for himself and fled. The first vayuphaks sprung from his fevered dreams and selfloathing, and it is whispered these asuras still stand guard over both the dreaming servant and the cursed relic.

  Vayuphaks stand 7 feet tall and weigh 120 pounds, though rumors tell of powerful vayuphaks growing to giant sizes.

---

# Asura, Vayuphak
This blue-skinned humanoid has two pairs of ebony wings protruding from its waist. Talon-like nails _[[spells/Grace|grace]]_ its hands.
**Source** Occult Bestiary pg. 8
**XP** 1,600

LE Medium outsider (asura, evil, extraplanar, lawful)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +18
**Aura** elusive (30 ft.), mental static (30 ft., DC 18)

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 52 (8d10+8); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +3, **Ref** +11, **Will** +9; +2 vs. enchantments
**Defensive Abilities** enveloping winds, DR 5/cold iron or good; **Immune** curse effects, disease, poison; **Resist** acid 10, electricity 10; **SR** 16

##### Offense
**Speed** 30 ft., fly 40 ft. (good)
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +12/+7 (1d8+4/×3), 2 wings +6 (1d4+1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +9)
At will—greater teleport (self plus 50 lbs. of objects only)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 1 vayuphak 35%)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 5th; concentration +9)
7 PE—_[[spells/Dispel Magic|dispel magic]]_ (3 PE), _[[spells/Id Insinuation I|id insinuation I]]_ (2 PE, DC 16), _[[spells/Object Reading|object reading]]_ (1 PE), _[[spells/Scorching Ray|scorching ray]]_ (2 PE)

##### Statistics
**Str** 16, **Dex** 16, **Con** 13, **Int** 15, **Wis** 16, **Cha** 19
**Base Atk** +8; **CMB** +11; **CMD** 25
**Feats** _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_
**Skills** Acrobatics +13, Bluff +15, Diplomacy +10, Escape Artist +15, Fly +15, Intimidate +12, Knowledge (planes) +10, Perception +18, Perform (dance) +13, Spellcraft +9, Stealth +10; **Racial Modifiers** +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or band (3–12)
**Treasure** standard (mwk _spear_, other treasure)

### Special Abilities

**Enveloping Winds (Su)** As an immediate action, a vayuphak can surround itself with a whirling torrent of air to protect it from ranged attacks. All ranged attacks made with physical weapons have a 20% miss chance against the vayuphak, except for attacks from massive weapons such as a giant’s thrown rock or a ballista. This ability has no effect on ray attacks.

##### Description

Vayuphaks, or “golden ones,” are asuras who serve as guardians and stewards of desecrated holy places. Whenever asuras descend to pollute a sanctified place, vayuphaks remain behind, _[[items/Weapon Magic Abilities/Defending|defending]]_ the once-sacred site from those who might reclaim it. Many make twisted mockeries out of their conquests, forming tainted kingdoms and faithless monasteries that ape the edifices of the virtuous who once occupied the area, compounding the pain of loss with outrage at their _[[items/Weapon Magic Abilities/Vicious|vicious]]_ parodies. Otherwise, vayuphaks spend much of their vigil in silent meditation, honing their thoughts and minds into _[[items/Weapon Magic Abilities/Deadly|deadly]]_ weapons. They are fearsome when roused to battle, though they prefer insinuating themselves into opponents’ minds over direct, physical confrontation.

Legends claim vayuphaks were created from a divine servant who was tasked with _[[items/Armor Magic Abilities/Guarding|guarding]]_ a treasure that signified the deity’s favor. After countless followers of the god slaughtered each other while attempting to obtain the prize, the enraged deity cursed the artifact so that all who looked upon it would be driven mad. The unwitting divine servant was the first victim, and wracked with madness, he claimed the treasure for himself and fled. The first vayuphaks sprung from his _[[curses/Fevered dreams|fevered dreams]]_ and selfloathing, and it is whispered these asuras still stand _[[npcs/Guard|guard]]_ over both the dreaming servant and the cursed relic.

Vayuphaks stand 7 feet tall and weigh 120 pounds, though rumors tell of powerful vayuphaks _[[items/Weapon Magic Abilities/Growing|growing]]_ to giant sizes.