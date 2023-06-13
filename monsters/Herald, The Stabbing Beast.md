---
cssclass: [monsters]
title1: Herald, The Stabbing Beast
desc_short: This towering, scorpion-tailed man stalks with a soundless grace and murderous
  intent.
title2: The Stabbing Beast
CR: 15
sources:
- name: Inner Sea Gods
  page: 300
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
- name: 'Pathfinder #59: The Price of Infamy'
  page: 90
  link: http://paizo.com/pathfinder/adventurePath/skullAndShackles/v5748btpy8moh
XP: 51200
alignment: NE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- herald
- shapechanger
initiative:
  bonus: 16
senses:
  darkvision: 60
  low-light vision: true
  see in darkness: true
  see invisibility: true
AC:
  AC: 31
  touch: 23
  flat_footed: 18
  components:
    dex: 12
    dodge: 1
    natural: 8
HP:
  HP: 212
  long: 17d10+119
saves:
  fort: 17
  ref: 17
  will: 14
  other: +4 vs. mind-affecting
defensive_abilities:
- all-around vision
DR:
- amount: 10
  weakness: good and magic
immunities:
- poison
resistances:
  acid: 30
  cold: 10
  electricity: 10
  fire: 10
SR: 26
speeds:
  base: 50
attacks:
  melee:
  - - text: +1 keen short swords +28/+28/+23/+18/+13 (1d6+4/17-20 plus bleed)
      entries:
      - - damage: 1d6+4
          crit_range: 17-20
        - effect: bleed
      attack: +1 keen short swords
      bonus:
      - 28
      - 28
      - 23
      - 18
      - 13
    - text: sting +24 (1d6+4 plus bleed and poison)
      entries:
      - - damage: 1d6+4
        - effect: bleed
        - effect: poison
      attack: sting
      bonus:
      - 24
  ranged:
  - - text: poison stream +29 touch (blindness 1d4+1 rounds)
      entries:
      - - effect: blindness 1d4+1 rounds
      attack: poison stream
      bonus:
      - 29
      touch: true
  special:
  - bleed (2d6)
  - poison
  - sudden strike
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - superscripts:
    - APG
    name: absorbing touch
    source: default
    freq: At will
  - superscripts:
    - APG
    name: alchemical allocation
    source: default
    freq: At will
  - name: charm person
    source: default
    freq: At will
    DC: 13
  - name: keen edge
    source: default
    freq: At will
  - name: poison
    source: default
    freq: At will
    DC: 16
  - name: true strike
    source: default
    freq: At will
  - name: false alibi
    source: default
    freq: 3/day
    DC: 15
  - name: greater teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: 3/day
  - name: modify memory
    source: default
    freq: 3/day
    DC: 16
  - name: suggestion
    source: default
    freq: 3/day
    DC: 15
  - name: summon
    source: default
    freq: 3/day
    level: 6
    summons:
    - name: fiendish deadfall scorpion [Bestiary 3 237]
      amount: 1
      chance: 100%
  sources:
  - name: default
    CL: 17
    concentration: 19
ability_scores:
  STR: 16
  DEX: 35
  CON: 24
  INT: 13
  WIS: 15
  CHA: 14
BAB: 17
CMB: 20
CMD: 43
feats:
- name: Combat Expertise
- name: Combat Reflexes
- is_bonus: true
  name: Deflect Arrows
- name: Dodge
- is_bonus: true
  name: Greater Feint
- is_bonus: true
  name: Improved Feint
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Mobility
- is_bonus: true
  name: Scorpion Style
- name: Spring Attack
- name: Two-Weapon Fighting
- is_bonus: true
  name: Weapon Finesse
skills:
  Appraise: 12
  Bluff: 22
  Climb: 11
  Craft (alchemy): 13
  Knowledge (arcana): 10
  Knowledge (nature): 10
  Knowledge (local): 13
  Knowledge (planes): 12
  Knowledge (religion): 9
  Perception: 26
  Sense Motive: 13
  Stealth: 32
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 4
languages:
- Abyssal
- Celestial
- Common
- Infernal
- Protean
- telepathy 100 ft.
special_qualities:
- change shape (Huge scorpion or scorpion-tailed human; shapechange)
- murderer's reward
ecology:
  environment: any land (Axis)
  organization: solitary
  treasure_type: standard
  treasure:
  - 2 +1 short swords
special_abilities:
  Change Shape (Su): 'In its scorpion form, replace or add the following statistics:
    Size Huge; Init +14; AC 31, touch 21, flat-footed 20 (+10 Dex, +1 dodge, +10 natural);
    Ref +16; Melee claws +28 (2d6+13 plus bleed and grab), sting +26 (2d6+11 plus
    bleed and poison); Space 15 ft.; Reach 15 ft.; Special Attacks constrict (2d6+12);
    Str 32, Dex 31; CMB +30 (+34 grapple); CMD 53 (65 vs. trip); Skills Climb +20,
    Stealth +24.'
  Murderer's Reward (Su): If the Stabbing Beast's attack reduces a target to fewer
    than 0 hit points, the herald immediately gains 2d6 temporary hit points (or 3d8,
    if the attack kills the target), but no more than the target's maximum hit points.
    The temporary hit points last for 1 hour.
  Poison (Ex): Sting-injury; save Fort DC 25; frequency 1/round for 6 rounds; effect
    1d6 Str; cure 2 consecutive saves.
  Poison Stream (Ex): As a ranged attack (or in place of a melee sting attack), the
    Stabbing Beast can fire a stream of poison up to 180 feet at an opponent's eyes.
    The target must succeed at a save against the Stabbing Beast's poison or be blinded
    for 1d4+1 rounds.
  Sudden Strike (Ex): During a surprise round, the herald may act as if it had a full
    round to act, rather than just one standard action.
desc_long: The Stabbing Beast is the herald of Norgorber, the god of greed, murder,
  secrets, and poison. It is an incredibly dangerous predator that uses its keen intellect
  and deadly poison to stalk and kill its prey. Its natural form is that of a huge
  scorpion, but it can also assume an armored humanoid shape suitable for stealth
  or interacting with Norgorber's followers. Though its main purpose for coming to
  Golarion is to kill, it has also been called to aid great thefts and bury terrible
  secrets.

---

# Herald, The Stabbing Beast
This towering, scorpion-tailed man stalks with a soundless _[[spells/Grace|grace]]_ and murderous intent.
**Source** Inner Sea Gods pg. 300, Pathfinder #59: The Price of Infamy pg. 90
**XP** 51,200

NE Medium outsider (evil, extraplanar, herald, shapechanger)
**Init** +16; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +26

##### Defense

**AC** 31, touch 23, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+12 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural)
**hp** 212 (17d10+119)
**Fort** +17, **Ref** +17, **Will** +14; +4 vs. mind–affecting
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_; **DR** 10/good and magic; **Immune** poison; **Resist** acid 30, cold 10, electricity 10, fire 10; **SR** 26

##### Offense
**Speed** 50 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Keen|keen]]_ short swords +28/+28/+23/+18/+13 (1d6+4/17–20 plus _[[universal monster rules/Bleed|bleed]]_), sting +24 (1d6+4 plus _bleed_ and poison)
**Ranged** poison stream +29 touch (blindness 1d4+1 rounds)
**Special Attacks** _bleed_ (2d6), poison, sudden strike
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +19)
Constant—_see invisibility_
At will—_[[spells/Absorbing Touch|absorbing touch]]_, _[[spells/Alchemical Allocation|alchemical allocation]]_, _[[spells/Charm Person|charm person]]_ (DC 13), _[[spells/Keen Edge|keen edge]]_, poison (DC 16), _[[spells/True Strike|true strike]]_
3/day—_[[spells/False Alibi|false alibi]]_ (DC 15), greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_, _[[spells/Modify Memory|modify memory]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 15), _[[universal monster rules/Summon|summon]]_ (level 6, 1 fiendish deadfall scorpion [Bestiary 3 237] 100%)

##### Statistics
**Str** 16, **Dex** 35, **Con** 24, **Int** 13, **Wis** 15, **Cha** 14
**Base Atk** +17; **CMB** +20; **CMD** 43
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _Dodge_, _[[feats/Greater Feint|Greater Feint]]_, _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Scorpion Style|Scorpion Style]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Appraise +12, Bluff +22, _[[universal monster rules/Climb|Climb]]_ +11, Craft (alchemy) +13, Knowledge (arcana, nature) +10, Knowledge (local) +13, Knowledge (planes) +12, Knowledge (religion) +9, Perception +26, Sense Motive +13, Stealth +32; **Racial Modifiers** +8 Bluff, +4 Perception
**Languages** Abyssal, Celestial, Common, Infernal, Protean; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Huge scorpion or scorpion-tailed human; _[[spells/Shapechange|shapechange]]_), murderer’s reward

##### Ecology

**Environment** any land (Axis)
**Organization** solitary
**Treasure** standard (2 +1 short swords)

### Special Abilities

**_Change Shape_ (Su)** In its scorpion form, replace or add the following statistics: **Size **Huge; **Init **+14; **AC **31, touch 21, _flat-footed_ 20 (+10 Dex, +1 _dodge_, +10 natural); **Ref **+16; **Melee** claws +28 (2d6+13 plus _bleed_ and _[[universal monster rules/Grab|grab]]_), sting +26 (2d6+11 plus _bleed_ and poison); **Space **15 ft.; **Reach **15 ft.; **Special Attacks **_[[universal monster rules/Constrict|constrict]]_ (2d6+12); **Str **32, **Dex **31; **CMB **+30 (+34 grapple); **CMD **53 (65 vs. _[[universal monster rules/Trip|trip]]_); **Skills **_Climb_ +20, Stealth +24.

**Murderer’s Reward (Su)** If the Stabbing Beast’s attack reduces a target to fewer than 0 hit points, the herald immediately gains 2d6 temporary hit points (or 3d8, if the attack kills the target), but no more than the target’s maximum hit points. The temporary hit points last for 1 hour.

**Poison (Ex)** Sting—injury; save Fort DC 25; frequency 1/round for 6 rounds; effect 1d6 Str; cure 2 consecutive saves.

**Poison Stream (Ex)** As a ranged attack (or in place of a melee sting attack), the Stabbing Beast can fire a stream of poison up to 180 feet at an opponent’s eyes. The target must succeed at a save against the Stabbing Beast’s poison or be _[[conditions/Blinded|blinded]]_ for 1d4+1 rounds.
**Sudden Strike (Ex)** During a surprise round, the herald may act as if it had a full round to act, rather than just one standard action.

##### Description

The Stabbing Beast is the herald of Norgorber, the god of greed, murder, secrets, and poison. It is an incredibly dangerous predator that uses its _keen_ intellect and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ poison to stalk and kill its prey. Its natural form is that of a huge scorpion, but it can also assume an armored humanoid shape suitable for stealth or interacting with Norgorber’s followers. Though its main purpose for coming to Golarion is to kill, it has also been _[[items/Weapon Magic Abilities/Called|called]]_ to aid great thefts and bury terrible secrets.