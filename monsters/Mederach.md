---
cssclass: [monsters]
title1: Mederach
desc_short: This towering spider has multifaceted, shining eyes, eight legs that are
  each tipped with silver, and massive mandibles.
title2: Mederach
CR: 9
sources:
- name: 'Pathfinder #105: The Inferno Gate'
  page: 88
  link: http://paizo.com/products/btpy9jb9?Pathfinder-Adventure-Path-105-The-Inferno-Gate
XP: 6400
alignment: CG
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- good
initiative:
  bonus: 0
senses:
  darkvision: 60
  detect evil: true
AC:
  AC: 23
  touch: 9
  flat_footed: 23
  components:
    natural: 14
    size: -1
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 12
  ref: 6
  will: 11
DR:
- amount: 10
  weakness: evil
SR: 20
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: bite +17 (1d8+5 plus poison)
      entries:
      - - damage: 1d8+5
        - effect: poison
      attack: bite
      bonus:
      - 17
    - text: 2 claws +16 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 16
  special:
  - poison
  - web (+11 ranged, DC 20, 12 hp)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: plane shift
    source: default
    freq: At will
    other: self only
  - name: calm emotions
    source: default
    freq: 3/day
    DC: 16
  - name: glitterdust
    source: default
    freq: 3/day
    DC: 16
  - name: break enchantment
    source: default
    freq: 1/day
    DC: 18
  - name: hold monster
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 21
  DEX: 10
  CON: 18
  INT: 13
  WIS: 16
  CHA: 19
BAB: 12
CMB: 18
CMD: 28
feats:
- name: Alertness
- name: Cleave
- name: Great Cleave
- name: Lightning Reflexes
- name: Power Attack
- name: Weapon Focus (bite)
skills:
  Acrobatics: 15
    when jumping: 19
  Climb: 28
  Diplomacy: 19
  Heal: 12
  Intimidate: 10
  Knowledge (planes): 10
  Perception: 22
  Sense Motive: 22
  Stealth: 5
languages:
- Celestial
- Common
- Infernal
special_qualities:
- change shape (Medium or Large animal only; beast shape II)
- peaceful intent
- silver claws
ecology:
  environment: any (Elysium)
  organization: solitary, pair, or team (3-6)
  treasure_type: standard
special_abilities:
  Peaceful Intent (Su): A mederach seeks peaceful and nonviolent solutions to confrontation
    unless facing mindless undead or evil arachnids. For all other creatures, the
    DC of saving throws attempted against a mederach's calm emotions and sanctuary
    spell-like abilities increases by 2 (this increase is not included in the DCs
    listed above). A mederach can use its claws to deal nonlethal damage without taking
    a penalty on its attack rolls.
  Poison (Ex): Bite-injury; save Fort DC 20; frequency 1/round for 6 rounds; effect
    daze; cure 1 save. The save DC is Constitution-based.
  Silver Claws (Ex): Because of the coating on them, a mederach's claws count as both
    silver and good for purposes of overcoming damage reduction.
desc_long: |-
  Natives of Elysium, mederachs are the kind and good counterparts to the bebiliths that lurk in the Abyss and prey upon demonic flesh. Mederachs once spent all of their time on their home plane, serving as healers and teachers to the azatas, angels, titans, and others creatures alongside which they lived; among themselves, mederachs delighted in discussing the nuances of the honest virtues they held in such high esteem, including kindness, charity, and mercy.

  As societies formed on the Material Plane, mederachs heard tales of mortals' changeable morality with interest and concern. Mortals, they came to believe, have souls that are inherently good, but that are also easily corrupted when exposed to prolonged suffering or extraplanar evil forces. During the Age of Darkness, mederachs heard of the various misfortunes and evils that had descended upon the lands of Golarion, including the falling of the Starstone, the collapse of major empires, and the rampages of the nascent demon lord Treerazer. Believing that these events would imperil the souls of all the world's mortals, mederachs began experimenting with plane-shifting; once they honed this ability, they began making regular forays to Golarion to aid good creatures in the fight against overwhelming evil. Now, in addition to embarking on these missions, mederachs also sometimes travel to the source of such evil plots-often the Abyss-and work on mortals' behalf there. However, no matter where their journeys take them, mederachs always keep in mind their belief that most evil can be redeemed, and so they seek to subdue their enemies and turn them toward good whenever possible instead of destroying them outright.

  Mederachs are typically 10 feet tall and weigh about 2,000 pounds.

---

# Mederach
This towering spider has multifaceted, shining eyes, eight legs that are each tipped with silver, and massive mandibles.
**Source** Pathfinder #105: The Inferno _[[spells/Gate|Gate]]_ pg. 88
**XP** 6,400

CG Large outsider (chaotic, extraplanar, good)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_; Perception +22

##### Defense

**AC** 23, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+14 natural, –1 size)
**hp** 114 (12d10+48)
**Fort** +12, **Ref** +6, **Will** +11
**DR** 10/evil; **SR** 20

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +17 (1d8+5 plus poison), 2 claws +16 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** poison, web (+11 ranged, DC 20, 12 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_detect evil_
At will—_[[spells/Plane Shift|plane shift]]_ (self only)
3/day—_[[spells/Calm Emotions|calm emotions]]_ (DC 16), _[[spells/Glitterdust|glitterdust]]_ (DC 16)
1/day—_[[spells/Break Enchantment|break enchantment]]_ (DC 18), _[[spells/Hold Monster|hold monster]]_ (DC 18)

##### Statistics
**Str** 21, **Dex** 10, **Con** 18, **Int** 13, **Wis** 16, **Cha** 19
**Base Atk** +12; **CMB** +18; **CMD** 28
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +15 (+19 when jumping), _Climb_ +28, Diplomacy +19, _[[spells/Heal|Heal]]_ +12, Intimidate +10, Knowledge (planes) +10, Perception +22, Sense Motive +22, Stealth +5
**Languages** Celestial, Common, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Medium or Large animal only; _[[spells/Beast Shape II|beast shape II]]_), _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_ intent, silver claws

##### Ecology

**Environment** any (Elysium)
**Organization** solitary, pair, or team (3–6)
**Treasure** standard

### Special Abilities

**_Peaceful_ Intent (Su)** A _[[monsters/Mederach|mederach]]_ seeks _peaceful_ and nonviolent solutions to confrontation unless facing mindless undead or evil arachnids. For all other creatures, the DC of saving throws attempted against a _mederach_’s _calm emotions_ and _[[spells/Sanctuary|sanctuary]]_ _spell-like abilities_ increases by 2 (this increase is not included in the DCs listed above). A _mederach_ can use its claws to deal nonlethal damage without taking a penalty on its attack rolls.

**Poison (Ex)** Bite—injury; save Fort DC 20; frequency 1/round for 6 rounds; effect _[[spells/Daze|daze]]_; cure 1 save. The save DC is Constitution-based.
**Silver Claws (Ex)** Because of the coating on them, a _mederach_’s claws count as both silver and good for purposes of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.

##### Description

Natives of Elysium, mederachs are the kind and good counterparts to the bebiliths that lurk in the Abyss and prey upon demonic flesh. Mederachs once spent all of their time on their home plane, serving as healers and teachers to the azatas, angels, titans, and others creatures alongside which they lived; among themselves, mederachs delighted in discussing the nuances of the honest virtues they held in such high esteem, including kindness, charity, and mercy.

As societies formed on the Material Plane, mederachs heard tales of mortals’ changeable morality with interest and concern. Mortals, they came to believe, have souls that are inherently good, but that are also easily corrupted when exposed to prolonged suffering or extraplanar evil forces. During the Age of _[[spells/Darkness|Darkness]]_, mederachs heard of the various misfortunes and evils that had descended upon the lands of Golarion, including the falling of the Starstone, the collapse of major empires, and the rampages of the nascent demon lord _[[monsters/Treerazer|Treerazer]]_. Believing that these events would imperil the souls of all the world’s mortals, mederachs began experimenting with plane-shifting; once they honed this ability, they began making regular forays to Golarion to aid good creatures in the fight against overwhelming evil. Now, in addition to embarking on these missions, mederachs also sometimes travel to the source of such evil plots—often the Abyss—and work on mortals’ behalf there. However, no matter where their journeys take them, mederachs always keep in mind their belief that most evil can be _[[items/Weapon Magic Abilities/Redeemed|redeemed]]_, and so they seek to subdue their enemies and turn them toward good whenever possible instead of destroying them outright.

Mederachs are typically 10 feet tall and weigh about 2,000 pounds.