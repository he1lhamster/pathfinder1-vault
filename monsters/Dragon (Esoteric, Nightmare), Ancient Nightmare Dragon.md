---
cssclass: [monsters]
title1: Dragon (Esoteric, Nightmare), Ancient Nightmare Dragon
title2: Ancient Nightmare Dragon
CR: 15
sources:
- name: Bestiary 5
  page: 95
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 51200
alignment: NE
size: Huge
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  dreamsight: true
  low-light vision: true
  see in darkness: true
auras:
- name: terrifying presence
  radius: 300
  DC: 26
AC:
  AC: 36
  touch: 7
  flat_footed: 36
  components:
    dex: -1
    natural: 29
    size: -2
HP:
  HP: 325
  long: 21d12+189
saves:
  fort: 21
  ref: 11
  will: 20
DR:
- amount: 5
  weakness: magic
immunities:
- mind-affecting effects
- paralysis
- sleep
SR: 26
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +33 (2d8+19/19-20)
      entries:
      - - damage: 2d8+19
          crit_range: 19-20
      attack: bite
      bonus:
      - 33
    - text: 2 claws +32 (2d6+13/19-20)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: wings
      bonus:
      - 30
    - text: tail slap +30 (2d6+19)
      entries:
      - - damage: 2d6+19
      attack: tail slap
      bonus:
      - 30
  special:
  - breath weapon (50-ft. cone, DC 29, 20d6 acid)
  - crush
  - nightmare talons
space: 15
reach: 10
reach_other: 15 ft. with bite
psychic_magic:
  entries:
  - name: dimension door
    PE: 4
  - name: ghost sound
    PE: 0
  - name: nightmare
    PE: 5
    DC: 20
  - name: true strike
    PE: 1
  sources:
  - name: default
    CL: 21
    concentration: 27
  PE: 16
spells:
  entries:
  - name: dream travel
    source: Psychic
    level: 6
  - name: greater dispel magic
    source: Psychic
    level: 6
  - name: dream scan
    source: Psychic
    level: 5
  - name: ego whip III
    source: Psychic
    level: 5
  - name: erase impressions
    source: Psychic
    level: 5
  - name: agonize
    source: Psychic
    level: 4
    DC: 19
  - name: crushing despair
    source: Psychic
    level: 4
    DC: 19
  - name: phantasmal killer
    source: Psychic
    level: 4
    DC: 19
  - name: stoneskin
    source: Psychic
    level: 4
  - name: deep slumber
    source: Psychic
    level: 3
    DC: 18
  - name: major image
    source: Psychic
    level: 3
    DC: 18
  - name: vision of Hell
    source: Psychic
    level: 3
  - name: wall of nausea
    source: Psychic
    level: 3
  - name: haunting mists
    source: Psychic
    level: 2
  - name: mind thrust II
    source: Psychic
    level: 2
  - name: mirror image
    source: Psychic
    level: 2
  - name: scare
    source: Psychic
    level: 2
    DC: 17
  - name: touch of idiocy
    source: Psychic
    level: 2
  - name: command
    source: Psychic
    level: 1
    DC: 16
  - name: compel hostility
    source: Psychic
    level: 1
  - name: detect thoughts
    source: Psychic
    level: 1
    DC: 16
  - name: ill omen
    source: Psychic
    level: 1
  - name: unwitting ally
    source: Psychic
    level: 1
    DC: 16
  - name: bleed
    source: Psychic
    level: 0
    DC: 15
  - name: dancing lights
    source: Psychic
    level: 0
  - name: daze
    source: Psychic
    level: 0
    DC: 15
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect psychic significance
    source: Psychic
    level: 0
  - name: lullaby
    source: Psychic
    level: 0
    DC: 15
  - name: resistance
    source: Psychic
    level: 0
  - name: telekinetic projectile
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 13
    concentration: 18
    slots:
      6: 4
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 37
  DEX: 9
  CON: 28
  INT: 20
  WIS: 22
  CHA: 23
BAB: 21
CMB: 36
CMD: 45
CMD_other: 49 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Snatch
- name: Stealthy
- name: Weapon Focus (bite)
skills:
  Bluff: 30
  Diplomacy: 30
  Escape Artist: 1
  Fly: 15
  Intimidate: 30
  Knowledge (arcana): 29
  Knowledge (planes): 29
  Knowledge (religion): 29
  Perception: 30
  Sense Motive: 30
  Stealth: 25
  Survival: 30
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Infernal
special_qualities:
- change shape
desc_long: These hunters of the Dimension of Dreams seek to wreak nightmares on sleepers
  and make existing bad dreams even more terrifying. Nightmare dragons often work
  with night hags in their grim collection of sleeping souls.

---

# Dragon (Esoteric, Nightmare), Ancient Nightmare Dragon

**Source** Bestiary 5 pg. 95
**XP** 51,200

NE Huge dragon (extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., dreamsight, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +30
**Aura** terrifying presence (300 ft., DC 26)

##### Defense

**AC** 36, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 36 (–1 Dex, +29 natural, –2 size)
**hp** 325 (21d12+189)
**Fort** +21, **Ref** +11, **Will** +20
**DR** 5/magic; **Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 26

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +33 (2d8+19/19–20), 2 claws +32 (2d6+13/19–20), 2 wings +30 (1d8+6), tail slap +30 (2d6+19)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 29, 20d6 acid), crush, _[[spells/Nightmare|nightmare]]_ talons
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 21st; concentration +27)
16 PE—_[[spells/Dimension Door|dimension door]]_ (4 PE), _[[spells/Ghost Sound|ghost sound]]_ (0 PE), _nightmare_ (5 PE, DC 20), _[[spells/True Strike|true strike]]_ (1 PE)
 **_[[classes/Psychic|Psychic]]_ Spells Known **(CL 13th; concentration +18)
 6th (4/day)—_[[spells/Dream Travel|dream travel]]_, greater _[[spells/Dispel Magic|dispel magic]]_
 5th (7/day)—_[[spells/Dream Scan|dream scan]]_, _[[spells/Ego _[[items/Weapon/Whip|Whip]]_ III|ego _whip_ III]]_, _[[spells/Erase Impressions|erase impressions]]_
 4th (7/day)—_[[spells/Agonize|agonize]]_ (DC 19), _[[spells/Crushing Despair|crushing despair]]_ (DC 19), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 19), _[[spells/Stoneskin|stoneskin]]_
 3rd (7/day)—_[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Vision of Hell|vision of Hell]]_, _[[spells/Wall Of Nausea|wall of nausea]]_
 2nd (7/day)—_[[spells/Haunting Mists|haunting mists]]_, _[[spells/Mind Thrust II|mind thrust II]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scare|scare]]_ (DC 17), _[[spells/Touch of Idiocy|touch of idiocy]]_
 1st (8/day)—_[[spells/Command|command]]_ (DC 16), _[[spells/Compel Hostility|compel hostility]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Ill Omen|ill omen]]_, _[[spells/Unwitting Ally|unwitting ally]]_ (DC 16)
 0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect _Psychic_ Significance|detect _psychic_ significance]]_, _[[spells/Lullaby|lullaby]]_ (DC 15), _[[universal monster rules/Resistance|resistance]]_, _[[spells/Telekinetic Projectile|telekinetic projectile]]_

##### Statistics
**Str** 37, **Dex** 9, **Con** 28, **Int** 20, **Wis** 22, **Cha** 23
**Base Atk** +21; **CMB** +36; **CMD** 45 (49 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Snatch|Snatch]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +30, Diplomacy +30, Escape Artist +1, Fly +15, Intimidate +30, Knowledge (arcana, planes, religion) +29, Perception +30, Sense Motive +30, Stealth +25, Survival +30
**Languages** Abyssal, Aklo, Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_

These hunters of the Dimension of Dreams seek to wreak nightmares on sleepers and make existing bad dreams even more terrifying. _Nightmare_ dragons often work with night hags in their grim collection of sleeping souls.