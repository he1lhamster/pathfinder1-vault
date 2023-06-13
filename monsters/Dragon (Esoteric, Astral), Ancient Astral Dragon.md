---
cssclass: [monsters]
title1: Dragon (Esoteric, Astral), Ancient Astral Dragon
title2: Ancient Astral Dragon
CR: 18
sources:
- name: Bestiary 5
  page: 89
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 153600
alignment: N
size: Gargantuan
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
  see invisibility: true
auras:
- name: mental static
  radius: 30
  DC: 27
- name: frightful presence
  radius: 300
  DC: 27
AC:
  AC: 37
  touch: 6
  flat_footed: 37
  components:
    natural: 31
    size: -4
HP:
  HP: 348
  long: 24d12+192
saves:
  fort: 21
  ref: 14
  will: 23
  other: +4 vs. psychic spells
defensive_abilities:
- psychic interference
- psychic resilience
DR:
- amount: 15
  weakness: magic
immunities:
- paralysis
- sleep
SR: 30
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +33 (4d6+18)
      entries:
      - - damage: 4d6+18
      attack: bite
      bonus:
      - 33
    - text: 2 claws +32 (2d8+12)
      entries:
      - - damage: 2d8+12
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 30
    - text: tail slap +30 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 30
  special:
  - breath weapon (120-ft. line, DC 29, 20d6 damage)
  - crush
  - staggering breath
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
psychic_magic:
  entries:
  - name: analyze aura
    PE: 3
  - name: aversion
    PE: 2
    DC: 19
  - name: deja vu
    PE: 1
  - name: possession
    PE: 5
    DC: 22
  - name: telekinetic projectile
    PE: 0
  - name: thoughtsense
    PE: 4
  sources:
  - name: default
    CL: 15
    concentration: 22
  PE: 19
spells:
  entries:
  - name: insanity
    source: Psychic
    level: 7
    DC: 24
  - name: repulsion
    source: Psychic
    level: 7
    DC: 24
  - name: blade barrier
    source: Psychic
    level: 6
    DC: 23
  - name: disintegrate
    source: Psychic
    level: 6
    DC: 23
  - name: create mindscape
    source: Psychic
    level: 6
  - name: dismissal
    source: Psychic
    level: 5
    DC: 22
  - name: remote viewing
    source: Psychic
    level: 5
  - name: wall of force
    source: Psychic
    level: 5
  - name: waves of fatigue
    source: Psychic
    level: 5
    DC: 22
  - name: greater false life
    source: Psychic
    level: 4
  - name: lesser globe of invulnerability
    source: Psychic
    level: 4
  - name: spell immunity
    source: Psychic
    level: 4
  - name: telekinetic charge
    source: Psychic
    level: 4
  - name: displacement
    source: Psychic
    level: 3
  - name: ego whip I
    source: Psychic
    level: 3
    DC: 20
  - name: haste
    source: Psychic
    level: 3
  - name: major image
    source: Psychic
    level: 3
    DC: 20
  - name: hideous laughter
    source: Psychic
    level: 2
    DC: 19
  - name: hypercognition,locate object
    source: Psychic
    level: 2
  - name: mirror image
    source: Psychic
    level: 2
  - name: touch of idiocy
    source: Psychic
    level: 2
  - name: burst of insight
    source: Psychic
    level: 1
  - name: feather fall
    source: Psychic
    level: 1
  - name: sundering shards
    source: Psychic
    level: 1
    DC: 18
  - name: true strike
    source: Psychic
    level: 1
  - name: unwitting ally
    source: Psychic
    level: 1
    DC: 18
  - name: dancing lights
    source: Psychic
    level: 0
  - name: daze
    source: Psychic
    level: 0
    DC: 17
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect psychic significance
    source: Psychic
    level: 0
  - name: know direction
    source: Psychic
    level: 0
  - name: mage hand
    source: Psychic
    level: 0
  - name: message
    source: Psychic
    level: 0
  - name: open/close
    source: Psychic
    level: 0
  - name: virtue
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 35
  DEX: 10
  CON: 24
  INT: 25
  WIS: 24
  CHA: 20
BAB: 24
CMB: 40
CMD: 50
CMD_other: 54 vs. trip
feats:
- name: Cleave
- name: Flyby Attack
- name: Great Cleave
- name: Improved Initiative
- name: Iron Will
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Snatch
- name: Toughness
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Appraise: 34
  Bluff: 32
  Diplomacy: 32
  Fly: 13
  Intimidate: 32
  Knowledge (arcana): 34
  Knowledge (history): 34
  Knowledge (nobility): 34
  Knowledge (planes): 34
  Knowledge (religion): 34
  Perception: 34
  Sense Motive: 34
  Stealth: 15
languages:
- Aklo
- Auran
- Celestial
- Common
- Draconic
- Infernal
special_qualities:
- change shape
desc_long: Reserved and haughty, these dragons roam the Astral Plane, seeking to expand
  their knowledge of its esoteric secrets. They hunt to eat, and use psychic magic
  to fight one another.

---

# Dragon (Esoteric, Astral), Ancient Astral Dragon

**Source** Bestiary 5 pg. 89
**XP** 153,600

N Gargantuan dragon (extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +34
**Aura** mental static (30 ft., DC 27), _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 27)

##### Defense

**AC** 37, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+31 natural, –4 size)
**hp** 348 (24d12+192)
**Fort** +21, **Ref** +14, **Will** +23; +4 vs. _[[classes/Psychic|psychic]]_ spells
**Defensive Abilities** _psychic_ interference, _[[universal monster rules/Psychic Resilience|psychic resilience]]_; **DR** 15/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 30

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy)
**Melee** bite +33 (4d6+18), 2 claws +32 (2d8+12), 2 wings +30 (2d6+6), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, DC 29, 20d6 damage), crush, staggering breath, tail sweep
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 15th; concentration +22)
19 PE-analyze aura (3 PE), _[[spells/Aversion|aversion]]_ (2 PE, DC 19), _[[spells/Deja Vu|deja vu]]_ (1 PE), _[[spells/Possession|possession]]_ (5 PE, DC 22), _[[spells/Telekinetic Projectile|telekinetic projectile]]_ (0 PE), _[[universal monster rules/Thoughtsense|thoughtsense]]_ (4 PE)
 **_Psychic_ Spells Known** (CL 15th; concentration +22)
7th (5/day)-insanity (DC 24), _[[spells/Repulsion|repulsion]]_ (DC 24)
6th (7/day)-blade barrier (DC 23), _[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Create Mindscape|create mindscape]]_
5th (7/day)-dismissal (DC 22), _[[spells/Remote Viewing|remote viewing]]_, _[[spells/Wall Of Force|wall of force]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_ (DC 22)
4th (7/day)-greater _[[spells/False Life|false life]]_, lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Telekinetic Charge|telekinetic charge]]_
3rd (8/day)-displacement, _[[spells/Ego _[[items/Weapon/Whip|Whip]]_ I|ego _whip_ I]]_ (DC 20), _[[spells/Haste|haste]]_, _[[spells/Major Image|major image]]_ (DC 20)
2nd (8/day)-hideous laughter (DC 19), _[[spells/Hypercognition|hypercognition]]_,_[[spells/Locate Object|locate object]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (8/day)-burst of insight, _[[spells/Feather Fall|feather fall]]_, _[[spells/Sundering Shards|sundering shards]]_ (DC 18), _[[spells/True Strike|true strike]]_, _[[spells/Unwitting Ally|unwitting ally]]_ (DC 18)
0 (at will)-dancing lights, _[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect _Psychic_ Significance|detect _psychic_ significance]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 35, **Dex** 10, **Con** 24, **Int** 25, **Wis** 24, **Cha** 20
**Base Atk** +24; **CMB** +40; **CMD** 50 (54 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Appraise +34, Bluff +32, Diplomacy +32, Fly +13, Intimidate +32, Knowledge (arcana, history, nobility, planes, religion) +34, Perception +34, Sense Motive +34, Stealth +15
**Languages** Aklo, Auran, Celestial, Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_

Reserved and haughty, these dragons roam the Astral Plane, seeking to expand their knowledge of its esoteric secrets. They hunt to eat, and use _psychic magic_ to fight one another.