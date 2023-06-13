---
cssclass: [monsters]
title1: Dragon (Primal, Brine), Ancient Brine Dragon
title2: Ancient Brine Dragon
CR: 16
sources:
- name: Bestiary 2
  page: 95
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 76800
alignment: LN
size: Huge
type: dragon
subtypes:
- extraplanar
- water
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 26
AC:
  AC: 37
  touch: 7
  flat_footed: 37
  components:
    dex: -1
    natural: 30
    size: -2
HP:
  HP: 275
  long: 22d12+132
saves:
  fort: 19
  ref: 14
  will: 18
DR:
- amount: 15
  weakness: magic
immunities:
- acid
- paralysis
- sleep
SR: 27
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
  swim: 60
attacks:
  melee:
  - - text: bite +34 (2d8+21 plus 1d2 Str)
      entries:
      - - damage: 2d8+21
        - damage: 1d2
          type: Str
      attack: bite
      bonus:
      - 34
    - text: 2 claws +34 (2d6+14)
      entries:
      - - damage: 2d6+14
      count: 2
      attack: claws
      bonus:
      - 34
    - text: tail slap +29 (2d6+21)
      entries:
      - - damage: 2d6+21
      attack: tail slap
      bonus:
      - 29
    - text: 2 wings +29 (1d8+7)
      entries:
      - - damage: 1d8+7
      count: 2
      attack: wings
      bonus:
      - 29
  special:
  - breath weapon (100-ft. line, 20d6 acid, DC 27)
  - capsize
  - crush
  - desiccating bite
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: control water
    source: default
    freq: At will
  - name: obscuring mist
    source: default
    freq: At will
  - name: speak with animals
    source: default
    freq: At will
    other: fish only
  - name: water breathing
    source: default
    freq: At will
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 23
  sources:
  - name: default
    CL: 22
    concentration: 27
spells:
  entries:
  - name: control weather
    source: '?'
    level: 7
  - name: mass fly
    source: '?'
    level: 7
  - name: fluid form
    source: '?'
    level: 6
  - name: true seeing
    source: '?'
    level: 6
  - name: transformation
    source: '?'
    level: 6
  - name: break enchantment
    source: '?'
    level: 5
  - name: dismissal
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: wall of force
    source: '?'
    level: 5
  - name: ball lightning
    source: '?'
    level: 4
    DC: 19
  - name: ice storm
    source: '?'
    level: 4
  - name: greater invisibility
    source: '?'
    level: 4
  - name: solid fog
    source: '?'
    level: 4
  - name: aqueous orb
    source: '?'
    level: 3
    DC: 18
  - name: deep slumber
    source: '?'
    level: 3
    DC: 18
  - name: dispel magic
    source: '?'
    level: 3
  - name: sleet storm
    source: '?'
    level: 3
    DC: 18
  - name: alter self
    source: '?'
    level: 2
  - name: detect thoughts
    source: '?'
    level: 2
    DC: 17
  - name: invisibility
    source: '?'
    level: 2
  - name: make whole
    source: '?'
    level: 2
  - name: slipstream
    source: '?'
    level: 2
  - name: color spray
    source: '?'
    level: 1
    DC: 16
  - name: feather fall
    source: '?'
    level: 1
  - name: flare burst
    source: '?'
    level: 1
    DC: 16
  - name: ray of enfeeblement
    source: '?'
    level: 1
  - name: touch of the sea
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 15
    concentration: 20
    slots:
      7: 4
      6: 6
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 38
  DEX: 9
  CON: 23
  INT: 23
  WIS: 20
  CHA: 21
BAB: 22
CMB: 38
CMD: 47
CMD_other: 51 vs. trip
feats:
- name: Awesome Blow
- name: Greater Vital Strike
- name: Hover
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Skill Focus (Swim)
- name: Vital Strike
- name: Wingover
skills:
  Bluff: 30
  Diplomacy: 30
  Fly: 16
  Heal: 30
  Knowledge (arcana): 31
  Knowledge (geography): 31
  Knowledge (nature): 31
  Perception: 30
  Sense Motive: 30
  Survival: 30
  Swim: 53
  Use Magic Device: 30
languages:
- Aquan
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Halfling
special_qualities:
- water breathing
ecology:
  environment: any aquatic (Plane of Water)
  organization: solitary
  treasure_type: triple
desc_long: Although not inherently evil, brine dragons have little patience for kindness
  and philanthropy. As they age, they grow more and more opinionated and obsessed
  with power-by adult age, a brine dragon counts itself a failure if it doesn't rule
  over a collection of “lesser beings” such as humans, merfolk, locathah, or even
  sahuagin.

---

# Dragon (Primal, Brine), Ancient Brine Dragon

**Source** Bestiary 2 pg. 95
**XP** 76,800

LN Huge dragon (extraplanar, water)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +30
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 26)

##### Defense

**AC** 37, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–1 Dex, +30 natural, –2 size)
**hp** 275 (22d12+132)
**Fort** +19, **Ref** +14, **Will** +18
**DR** 15/magic; **Immune** acid, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 27

##### Offense
**Speed** 60 ft., fly 200 ft. (poor), swim 60 ft.
**Melee** bite +34 (2d8+21 plus 1d2 Str), 2 claws +34 (2d6+14), tail slap +29 (2d6+21), 2 wings +29 (1d8+7)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, 20d6 acid, DC 27), _[[universal monster rules/Capsize|capsize]]_, crush, desiccating bite
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 22nd; concentration +27)
At will—_[[spells/Control Water|control water]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_ (fish only), _[[universal monster rules/Water Breathing|water breathing]]_
3/day—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 23)
**Spells Known **(CL 15th; concentration +20)
7th (4/day)—_[[spells/Control Weather|control weather]]_, mass fly
6th (6/day)—_[[spells/Fluid Form|fluid form]]_, _[[spells/True Seeing|true seeing]]_, _[[spells/Transformation|transformation]]_
5th (7/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dismissal|dismissal]]_, teleport, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Ball Lightning|ball lightning]]_ (DC 19), _[[spells/Ice Storm|ice storm]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Solid Fog|solid fog]]_
3rd (7/day)—_[[spells/Aqueous Orb|aqueous orb]]_ (DC 18), _[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Sleet Storm|sleet storm]]_ (DC 18)
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _invisibility_, _[[spells/Make Whole|make whole]]_, _[[spells/Slipstream|slipstream]]_
1st (8/day)—_[[spells/Color Spray|color spray]]_ (DC 16), _[[spells/Feather Fall|feather fall]]_, _[[spells/Flare Burst|flare burst]]_ (DC 16), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_, _[[spells/Touch of the Sea|touch of the sea]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 38, **Dex** 9, **Con** 23, **Int** 23, **Wis** 20, **Cha** 21
**Base Atk** +22; **CMB** +38; **CMD** 47 (51 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Swim), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +30, Diplomacy +30, Fly +16, _[[spells/Heal|Heal]]_ +30, Knowledge (arcana, geography, nature) +31, Perception +30, Sense Motive +30, Survival +30, Swim +53, Use Magic Device +30
**Languages** Aquan, Common, Draconic, Dwarven, Elven, Gnome, Halfling
**SQ** _water breathing_

##### Ecology

**Environment** any aquatic (Plane of Water)
**Organization** solitary
**Treasure** triple

Although not inherently evil, brine dragons have little patience for kindness and philanthropy. As they age, they grow more and more opinionated and obsessed with power—by adult age, a brine dragon counts itself a failure if it doesn't rule over a collection of “lesser beings” such as humans, _[[monsters/Merfolk|merfolk]]_, _[[monsters/Locathah|locathah]]_, or even _[[monsters/Sahuagin|sahuagin]]_.