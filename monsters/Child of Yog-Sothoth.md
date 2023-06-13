---
cssclass: [monsters]
title1: Child of Yog-Sothoth
desc_short: This creature could almost pass for human from the neck up, but below
  that its scaly skin, tail, and animal-like legs, as well as the tentacles that droop
  from its belly, reveal its aberrant nature.
title2: Child of Yog-Sothoth
CR: 7
sources:
- name: 'Pathfinder #113: What Grows Within'
  page: 82
  link: http://paizo.com/products/btpy9qcl?Pathfinder-Adventure-Path-113-What-Grows-Within
XP: 3200
race: Male
classes:
- human child of Yog-Sothoth wizard 7
alignment: CE
size: Medium
type: aberration
subtypes:
- augmented humanoid
initiative:
  bonus: 5
senses:
  all-around vision: true
  low-light vision: true
AC:
  AC: 14
  touch: 11
  flat_footed: 13
  components:
    dex: 1
    natural: 3
HP:
  HP: 76
  long: 7d6+49
saves:
  fort: 7
  ref: 3
  will: 7
  other: +4 vs. mind-affecting effects
immunities:
- disease
- poison
resistances:
  cold: 10
  fire: 10
SR: 18
weaknesses:
- loathed
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 dagger +6 (1d4+3/19-20)
      entries:
      - - damage: 1d4+3
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 6
    - text: tail +5 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: tail
      bonus:
      - 5
  special:
  - blood drain (1d2 Con)
  - hand of the apprentice (8/day)
  - stench (DC 18, 7 rounds/day)
spell_like_abilities:
  entries:
  - name: comprehend languages
    source: default
    freq: 3/day
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 17
  - name: hypnotism
    source: default
    freq: 3/day
    DC: 16
  - name: invisibility
    source: default
    freq: 1/day
  - name: contact entity I
    source: default
    freq: 1/week
  - name: contact entity II
    source: default
    freq: 1/week
  sources:
  - name: default
    CL: 7
    concentration: 12
spells:
  entries:
  - name: black tentacles
    source: Wizard
    level: 4
  - name: dimension door
    source: Wizard
    level: 4
  - name: dispel magic
    source: Wizard
    level: 3
  - name: suggestion
    source: Wizard
    level: 3
    DC: 18
  - name: vampiric touch
    source: Wizard
    level: 3
  - name: acid arrow
    source: Wizard
    level: 2
  - name: mirror image
    source: Wizard
    level: 2
  - name: summon monster II
    source: Wizard
    level: 2
  - name: summon swarm
    source: Wizard
    level: 2
  - name: charm person
    source: Wizard
    level: 1
    count: 2
    DC: 16
  - name: grease
    source: Wizard
    level: 1
    DC: 16
  - name: mage armor
    source: Wizard
    level: 1
  - name: ray of enfeeblement
    source: Wizard
    level: 1
    count: 2
    DC: 16
  - name: arcane mark
    source: Wizard
    level: 0
  - name: detect magic
    source: Wizard
    level: 0
  - name: mage hand
    source: Wizard
    level: 0
  - name: open/close
    source: Wizard
    level: 0
    DC: 15
  sources:
  - name: Wizard
    type: prepared
    CL: 7
    concentration: 12
    slots:
      0: at-will
ability_scores:
  STR: 14
  DEX: 13
  CON: 20
  INT: 20
  WIS: 10
  CHA: 6
BAB: 3
CMB: 5
CMD: 20
feats:
- name: Combat Casting
- name: Deceitful
- name: Defensive Combat Training
- name: Extend Spell
- name: Improved Initiative
- name: Iron Will
- name: Scribe Scroll
- is_bonus: true
  name: Toughness
skills:
  Bluff: 7
  Disguise: 7
    when disguised as human: 15
  Intimidate: 5
  Knowledge (nature): 15
  Knowledge (planes): 15
  Knowledge (religion): 15
  Perception: 7
  Spellcraft: 19
  _racial_mods:
    Disguise:
      when disguised as human: 8
    Knowledge (arcana):
      _: 4
    Spellcraft:
      _: 4
languages:
- Aklo
- Common
- Elder Thing
- Mi-go
special_qualities:
- arcane bond (+1 dagger)
- conceal features
- magic savant
ecology:
  environment: any
  organization: solitary or family (1 child of Yog-Sothoth and 1 spawn of Yog-Sothoth)
  treasure_type: NPC Gear
  treasure:
  - +1 dagger
  - spell component pouch
  - spellbook
  - other treasure
desc_long: Creatures born of mortal flesh infused with the essence of the outer god
  Yog-Sothoth, these deviant children are often tasked with preparing the world for
  further incursions from other dimensions or agents of the Elder Mythos. Traditionally,
  the process of creating a child of Yog-Sothoth involves a blasphemous ritual that
  uses a mortal creature (typically a human) as an incubator. For the purpose of this
  ritual, gender is irrelevant. Giving birth to a child of Yog-Sothoth is always fatal.
  In most cases, the ritual results in the birth of twins-one a child of Yog-Sothoth,
  which can pass for a time as a member of the race of the creature in which it incubated,
  and one that cannot. Those twins that inherit a monstrous appearance take more after
  the Outer God itself in form, and are known as the spawn of Yog-Sothoth (Pathfinder
  RPG Bestiary 4 251).

---

# Child of Yog-Sothoth
This creature could almost _[[feats/Pass For Human|pass for human]]_ from the neck up, but below that its scaly skin, tail, and animal-like legs, as well as the tentacles that droop from its belly, reveal its aberrant nature.
**Source** Pathfinder #113: _[[spells/What Grows Within|What Grows Within]]_ pg. 82
**XP** 3,200
Male human _[[monsters/Child of Yog-Sothoth|child of Yog-Sothoth]]_ _[[classes/Wizard|wizard]]_ 7
CE Medium aberration (augmented humanoid)
**Init** +5; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, Perception +7

##### Defense

**AC** 14, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+1 Dex, +3 natural)
**hp** 76 (7d6+49)
**Fort** +7, **Ref** +3, **Will** +7; +4 vs. mind-affecting effects
**Immune** disease, poison; **Resist** cold 10, fire 10; **SR** 18
**Weaknesses** loathed

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +6 (1d4+3/19–20), tail +5 (1d6+1)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Con), hand of the apprentice (8/day), _[[universal monster rules/Stench|stench]]_ (DC 18, 7 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
3/day—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Hypnotism|hypnotism]]_ (DC 16)
1/day—_[[spells/Invisibility|invisibility]]_
1/week—_[[spells/Contact Entity I|contact entity I]]_, _[[spells/Contact Entity II|contact entity II]]_
**_Wizard_ Spells Prepared **(CL 7th; concentration +12)
4th—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Dimension Door|dimension door]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Vampiric Touch|vampiric touch]]_
2nd—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Summon Monster II|summon monster II]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Charm Person|charm person]]_ (2, DC 16), _[[spells/Grease|grease]]_ (DC 16), _[[spells/Mage Armor|mage armor]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (2, DC 16)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, open/close (DC 15)

##### Statistics
**Str** 14, **Dex** 13, **Con** 20, **Int** 20, **Wis** 10, **Cha** 6
**Base Atk** +3; **CMB** +5; **CMD** 20
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +7, Disguise +7 (+15 when disguised as human), Intimidate +5, Knowledge (nature) +15, Knowledge (planes) +15, Knowledge (religion) +15, Perception +7, Spellcraft +19; **Racial Modifiers** +8 Disguise (when disguised as human), +4 Knowledge (arcana), +4 Spellcraft
**Languages** Aklo, Common, _[[monsters/Elder Thing|Elder Thing]]_, _[[monsters/Mi-go|Mi-go]]_
**SQ** arcane bond (+1 _dagger_), conceal features, magic savant

##### Ecology

**Environment** any
**Organization** solitary or family (1 _child of Yog-Sothoth_ and 1 _[[monsters/Spawn of Yog-Sothoth|spawn of Yog-Sothoth]]_)
**Treasure** NPC gear (+1 _dagger_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Spellbook|spellbook]]_, other treasure)

##### Description

Creatures born of mortal flesh infused with the essence of the outer god Yog-Sothoth, these deviant children are often tasked with preparing the world for further incursions from other dimensions or agents of the Elder Mythos. Traditionally, the process of creating a _child of Yog-Sothoth_ involves a blasphemous ritual that uses a mortal creature (typically a human) as an incubator. For the purpose of this ritual, gender is irrelevant. Giving birth to a _child of Yog-Sothoth_ is always fatal. In most cases, the ritual results in the birth of twins—one a _child of Yog-Sothoth_, which can pass for a time as a member of the race of the creature in which it incubated, and one that cannot. Those twins that inherit a monstrous appearance take more after the Outer God itself in form, and are known as the _spawn of Yog-Sothoth_ (Pathfinder RPG Bestiary 4 251).