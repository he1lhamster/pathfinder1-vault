---
cssclass: [monsters]
title1: Animal Lord, Cat Lord
desc_short: This dark-skinned woman's languid movements are grace personified, her
  sparkling eyes those of a cat.
title2: Cat Lord
CR: 11
sources:
- name: Bestiary 3
  page: 14
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 12800
race: Human
classes:
- animal lord ranger 10
alignment: NG
size: Medium
type: outsider
subtypes:
- native
- shapechanger
initiative:
  bonus: 7
senses:
  low-light vision: true
  scent: true
AC:
  AC: 25
  touch: 18
  flat_footed: 18
  components:
    armor: 3
    deflection: 1
    dex: 6
    dodge: 1
    natural: 4
HP:
  HP: 139
  long: 10d10+80
saves:
  fort: 13
  ref: 14
  will: 7
defensive_abilities:
- evasion
DR:
- amount: 10
  weakness: silver
speeds:
  base: 30
  other_semicolon: leap
  climb: 20
attacks:
  melee:
  - - text: bite +15 (1d6+5 plus grab)
      entries:
      - - damage: 1d6+5
        - effect: grab
      attack: bite
      bonus:
      - 15
    - text: 2 claws +15 (1d3+5)
      entries:
      - - damage: 1d3+5
      count: 2
      attack: claws
      bonus:
      - 15
  ranged:
  - - text: +1 seeking composite longbow +18/+13 (1d8+6/×3)
      entries:
      - - damage: 1d8+6
          crit_multiplier: 3
      attack: +1 seeking composite longbow
      bonus:
      - 18
      - 13
  special:
  - favored enemy (evil outsiders +6, giants +2, undead +2)
  - pounce
  - rake (2 claws +15, 1d3+5)
spell_like_abilities:
  entries:
  - name: charm animal
    source: default
    freq: At will
    other: cats only
    DC: 13
  sources:
  - name: default
    CL: 10
    concentration: 12
spells:
  entries:
  - name: greater magic fang
    source: Ranger
    level: 3
  - name: cat's grace
    source: Ranger
    level: 2
  - name: hold animal
    source: Ranger
    level: 2
    DC: 16
  - name: charm animal
    source: Ranger
    level: 1
    DC: 15
  - name: longstrider
    source: Ranger
    level: 1
  - name: pass without trace
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 7
    concentration: 11
ability_scores:
  STR: 20
  DEX: 24
  CON: 22
  INT: 12
  WIS: 18
  CHA: 14
BAB: 10
CMB: 17
CMB_other: +21 grapple
CMD: 34
feats:
- name: Agile Maneuvers
- name: Deadly Aim
- name: Dodge
- name: Endurance
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Shot on the Run
- name: Toughness
- name: Vital Strike
skills:
  Acrobatics: 17
    when jumping: 22
  Climb: 26
  Handle Animal: 15
  Knowledge (nature): 14
  Perception: 17
  Sense Motive: 14
  Stealth: 20
    in undergrowth: 24
  Survival: 17
  _racial_mods:
    Acrobatics:
      when jumping: 5
    Stealth:
      in undergrowth: 4
languages:
- Common
- Sylvan
- speak with animals (cats only)
special_qualities:
- change shape (leopard; shapechange)
- favored terrain (jungle +4, plains +2)
- hunter's bond (leopard)
- swift tracker
- track +5
- wild empathy +12
- woodland stride
ecology:
  environment: warm jungles
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - +1 leather armor
  - +1 seeking composite longbow [+5 Str] with 20 arrows
  - amulet of natural armor +1
  - ring of protection +1
  - other treasure
desc_long: |-
  When the gods of nature or powerful spirits desire a champion to defend the animal world, they invest a token of their power in a chosen vessel-be it animal or humanoid. Traditionally, only one animal lord for a specific animal species is active on a world at any one time, although sometimes, when an extant animal lord strays from its charge or otherwise fails, the force that created it might create a replacement to send against the fallen animal lord to challenge it in a combat to the death, with the victor claiming the right to rule or a chance at redemption.

  An animal lord does not dwell among humanity-the wild is its domain. How an animal lord interacts with a humanoid society largely depends on how that society treats the animals of that lord's affinity. Societies that honor and respect those animals, even if they use the animals as a food source, earn the animal lord's (sometimes grudging) respect, but those who abuse or otherwise harm animals of that lord's species find a powerful and ardent enemy in the lord.

  The cat lord above uses a leopard as the base animal-this particular cat lord represents a newly created animal lord. The longer an animal lord exists, the higher its level should be.

---

# Animal Lord, Cat Lord
This dark-skinned woman’s languid movements are _[[spells/Grace|grace]]_ personified, her sparkling eyes those of a cat.
**Source** Bestiary 3 pg. 14
**XP** 12,800
Human animal lord _[[classes/Ranger|ranger]]_ 10

NG Medium outsider (native, shapechanger)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +17

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +6 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 139 (10d10+80)
**Fort** +13, **Ref** +14, **Will** +7
**Defensive Abilities** evasion; **DR** 10/silver

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.; leap
**Melee** bite +15 (1d6+5 plus _[[universal monster rules/Grab|grab]]_), 2 claws +15 (1d3+5)
**Ranged** +1 seeking _[[items/Weapon/Composite longbow|composite longbow]]_ +18/+13 (1d8+6/×3)
**Special Attacks** favored enemy (evil outsiders +6, giants +2, undead +2), _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +15, 1d3+5)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
At will—_[[spells/Charm Animal|charm animal]]_ (cats only, DC 13)
**_Ranger_ Spells Prepared **(CL 7th; concentration +11)
3rd—greater _[[spells/Magic Fang|magic fang]]_
2nd—cat’s _grace_, _[[spells/Hold Animal|hold animal]]_ (DC 16)
1st—_charm animal_ (DC 15), _[[spells/Longstrider|longstrider]]_, _[[spells/Pass without Trace|pass without trace]]_

##### Statistics
**Str** 20, **Dex** 24, **Con** 22, **Int** 12, **Wis** 18, **Cha** 14
**Base Atk** +10; **CMB** +17 (+21 grapple); **CMD** 34
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +17 (+22 when jumping), _Climb_ +26, Handle Animal +15, Knowledge (nature) +14, Perception +17, Sense Motive +14, Stealth +20 (+24 in undergrowth), Survival +17; **Racial Modifiers** +5 Acrobatics when jumping, +4 Stealth in undergrowth
**Languages** Common, Sylvan; _[[spells/Speak with Animals|speak with animals]]_ (cats only)
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (leopard; _[[spells/Shapechange|shapechange]]_), favored terrain (jungle +4, plains +2), _[[classes/Hunter|hunter]]_’s bond (leopard), swift tracker, track +5, wild _[[feats/Empathy|empathy]]_ +12, woodland stride

##### Ecology

**Environment** warm jungles
**Organization** solitary
**Treasure** NPC gear (+1 _[[items/Armor/Leather armor|leather armor]]_, +1 seeking _composite longbow_ [+5 Str] with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, other treasure)

##### Description

When the gods of nature or powerful spirits desire a _[[items/Armor Magic Abilities/Champion|champion]]_ to defend the animal world, they invest a token of their power in a chosen vessel—be it animal or humanoid. Traditionally, only one animal lord for a specific animal species is active on a world at any one time, although sometimes, when an extant animal lord strays from its charge or otherwise fails, the force that created it might create a replacement to send against the _[[monsters/Fallen|fallen]]_ animal lord to challenge it in a combat to the death, with the victor claiming the right to rule or a chance at _[[feats/Redemption|redemption]]_.

An animal lord does not dwell among humanity—the wild is its domain. How an animal lord interacts with a humanoid society largely depends on how that society treats the animals of that lord’s affinity. Societies that honor and respect those animals, even if they use the animals as a food source, earn the animal lord’s (sometimes grudging) respect, but those who abuse or otherwise _[[spells/Harm|harm]]_ animals of that lord’s species find a powerful and ardent enemy in the lord.

The cat lord above uses a leopard as the base animal—this particular cat lord represents a newly created animal lord. The longer an animal lord exists, the higher its level should be.