---
cssclass: [monsters]
title1: Adlet
desc_short: This humanoid wolf's fur is snowy white and its eyes piercing blue; it
  grips an ornate spear in its fist.
title2: Adlet
CR: 10
sources:
- name: Bestiary 3
  page: 9
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 9600
alignment: CN
size: Medium
type: humanoid
subtypes:
- adlet
- cold
initiative:
  bonus: 12
senses:
  low-light vision: true
  scent: true
AC:
  AC: 24
  touch: 19
  flat_footed: 15
  components:
    dex: 8
    dodge: 1
    natural: 5
HP:
  HP: 127
  long: 15d8+60
saves:
  fort: 9
  ref: 17
  will: 8
immunities:
- cold
weaknesses:
- vulnerability to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 spear +17/+12/+7 (1d8+7/×3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 17
      - 12
      - 7
    - text: bite +10 (1d6+2 plus 1d6 cold)
      entries:
      - - damage: 1d6+2
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 10
  special:
  - frozen breath
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: ray of frost
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: 3/day
  - name: sleet storm
    source: default
    freq: 3/day
  - name: ice storm
    source: default
    freq: 1/day
  - name: wind walk
    source: default
    freq: 1/day
    other: self only
  sources:
  - name: default
    CL: 10
    concentration: 11
ability_scores:
  STR: 18
  DEX: 26
  CON: 18
  INT: 13
  WIS: 17
  CHA: 13
BAB: 11
CMB: 15
CMD: 35
feats:
- name: Diehard
- name: Dodge
- name: Endurance
- name: Improved Initiative
- name: Power Attack
- name: Run
- name: Self-Sufficient
- name: Weapon Focus (spear)
skills:
  Acrobatics: 13
    when jumping: 17
  Climb: 12
  Handle Animal: 9
  Heal: 5
  Perception: 13
  Stealth: 13
    in snow: 21
  Survival: 20
  Swim: 9
  _racial_mods:
    Stealth:
      in snow: 8
languages:
- Common
- Adlet
special_qualities:
- arctic stride
ecology:
  environment: cold plains, hills, or mountains
  organization: solitary, pair, or pack (3-18 plus 1 shaman)
  treasure_type: standard
  treasure:
  - +1 spear
  - other treasure
special_abilities:
  Arctic Stride (Ex): An adlet can move through any sort of difficult terrain at its
    normal speed while within arctic or snowy terrain. Magically altered terrain affects
    an adlet normally.
  Frozen Breath (Su): An adlet's breath is supernaturally cold, and deals an additional
    1d6 points of cold damage with its bite as a result. Once every 1d4 rounds as
    a swift action, it can exhale, filling a 10-foot-radius spread around it with
    frigid air that deals 2d6 points of cold damage and staggers those in the area
    with numbing cold for 1d6 rounds. A DC 21 Fortitude save negates the staggered
    effect but not the cold damage. The save DC is Constitution-based.
desc_long: |-
  Adlets are cunning hunters of the arctic wilds. Tall, sinewy, nimble, and very quick, they see themselves as the true heritors of untamed arctic lands, and are offended by any other humanoid species that attempts to settle in such regions. Although not normally evil, adlets are very aggressive and warlike. They also have no social taboo against cannibalism, and their practice of eating their dead rather than burying them only further builds misconceptions about their morality.

  Deeply religious, adlets worship the power and cruelty of nature, seeing divinity in the lash of the blizzard's wind, the ferocity of the polar bear, and the immensity of the towering iceberg. Many become oracles or druids, but all adlets know their place in the natural world. One in every dozen adlets is a shaman: an adlet with the advanced creature template and the ability to summon a greater ice elemental or 1d4+1 large ice elementals (see Bestiary 2 114) and commune with nature once per day each as spell-like abilities. An adlet is 6 feet tall and weighs 250 pounds.

---

# Adlet
This humanoid _[[monsters/Wolf|wolf]]_’s fur is snowy white and its eyes piercing blue; it grips an ornate _[[items/Weapon/Spear|spear]]_ in its fist.
**Source** Bestiary 3 pg. 9
**XP** 9,600

CN Medium humanoid (_[[monsters/Adlet|adlet]]_, cold)
**Init** +12; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +13

##### Defense

**AC** 24, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+8 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 127 each (15d8+60)
**Fort** +9, **Ref** +17, **Will** +8
**Immune** cold
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 40 ft.
**Melee** +1 _spear_ +17/+12/+7 (1d8+7/×3), bite +10 (1d6+2 plus 1d6 cold)
**Special Attacks** frozen breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +11)
Constant—_[[spells/Pass without Trace|pass without trace]]_
At will—_[[spells/Ray of Frost|ray of frost]]_
3/day—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Sleet Storm|sleet storm]]_
1/day—_[[spells/Ice Storm|ice storm]]_, _[[spells/Wind Walk|wind walk]]_ (self only)

##### Statistics
**Str** 18, **Dex** 26, **Con** 18, **Int** 13, **Wis** 17, **Cha** 13
**Base Atk** +11; **CMB** +15; **CMD** 35
**Feats** _[[feats/Diehard|Diehard]]_, _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, Run, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Acrobatics +13 (+17 when jumping), _[[universal monster rules/Climb|Climb]]_ +12, Handle Animal +9, _[[spells/Heal|Heal]]_ +5, Perception +13, Stealth +13 (+21 in snow), Survival +20, Swim +9; **Racial Modifiers** +8 Stealth in snow
**Languages** Common, _Adlet_
**SQ** arctic stride

##### Ecology

**Environment** cold plains, hills, or mountains
**Organization** solitary, pair, or pack (3–18 plus 1 _[[classes/Shaman|shaman]]_)
**Treasure** standard (+1 _spear_, other treasure)

### Special Abilities

**Arctic Stride (Ex)** An _adlet_ can move through any sort of difficult terrain at its normal speed while within arctic or snowy terrain. Magically altered terrain affects an _adlet_ normally.

**Frozen Breath (Su)** An _adlet_’s breath is supernaturally cold, and deals an additional 1d6 points of cold damage with its bite as a result. Once every 1d4 rounds as a swift action, it can exhale, filling a 10-foot-radius spread around it with frigid air that deals 2d6 points of cold damage and staggers those in the area with numbing cold for 1d6 rounds. A DC 21 Fortitude save negates the _[[conditions/Staggered|staggered]]_ effect but not the cold damage. The save DC is Constitution-based.

##### Description

Adlets are _[[items/Weapon Magic Abilities/Cunning|cunning]]_ hunters of the arctic wilds. Tall, sinewy, nimble, and very quick, they see themselves as the true heritors of untamed arctic lands, and are offended by any other humanoid species that attempts to settle in such regions. Although not normally evil, adlets are very aggressive and warlike. They also have no social taboo against cannibalism, and their practice of eating their dead rather than burying them only further builds misconceptions about their morality.

Deeply religious, adlets worship the power and _[[feats/Cruelty|cruelty]]_ of nature, seeing divinity in the lash of the blizzard’s wind, the _[[universal monster rules/Ferocity|ferocity]]_ of the polar bear, and the immensity of the towering iceberg. Many become oracles or druids, but all adlets know their place in the natural world. One in every dozen adlets is a _shaman_: an _adlet_ with the advanced creature template and the ability to _[[universal monster rules/Summon|summon]]_ a greater ice elemental or 1d4+1 large ice elementals (see Bestiary 2 114) and _[[spells/Commune with Nature|commune with nature]]_ once per day each as _spell-like abilities_. An _adlet_ is 6 feet tall and weighs 250 pounds.