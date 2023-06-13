---
cssclass: [monsters]
title1: Dragon (Esoteric, Astral), Adult Astral Dragon
title2: Adult Astral Dragon
CR: 13
sources:
- name: Bestiary 5
  page: 88
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 25600
alignment: N
size: Huge
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 5
senses:
  dragon senses: true
  see invisibility: true
auras:
- name: mental static
  radius: 30
  DC: 21
- name: frightful presence
  radius: 180
  DC: 21
AC:
  AC: 28
  touch: 9
  flat_footed: 27
  components:
    dex: 1
    natural: 19
    size: -2
HP:
  HP: 184
  long: 16d12+80
saves:
  fort: 15
  ref: 11
  will: 17
  other: +4 vs. psychic spells
defensive_abilities:
- psychic resilience
DR:
- amount: 5
  weakness: magic
immunities:
- paralysis
- sleep
SR: 24
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +23 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: bite
      bonus:
      - 23
    - text: 2 claws +22 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 22
    - text: 2 wings +20 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 20
    - text: tail slap +20 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: tail slap
      bonus:
      - 20
  special:
  - breath weapon (100-ft. line, DC 23, 12d6 force)
  - crush
space: 15
reach: 10
reach_other: 15 ft. with bite
psychic_magic:
  entries:
  - name: analyze aura
    PE: 3
  - name: aversion
    PE: 2
    DC: 17
  - name: deja vu
    PE: 1
  - name: id insinuation I
    PE: 3
    DC: 18
  - name: telekinetic projectile
    PE: 0
  sources:
  - name: default
    CL: 16
    concentration: 21
  PE: 11
spells:
  entries:
  - name: ego whip I
    source: Psychic
    level: 3
  - name: haste
    source: Psychic
    level: 3
  - name: blur
    source: Psychic
    level: 2
  - name: hideous laughter
    source: Psychic
    level: 2
    DC: 17
  - name: locate object
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
    DC: 16
  - name: true strike
    source: Psychic
    level: 1
  - name: unwitting ally
    source: Psychic
    level: 1
    DC: 16
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
  - name: detect poison
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
  sources:
  - name: Psychic
    type: known
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 27
  DEX: 12
  CON: 20
  INT: 21
  WIS: 20
  CHA: 16
BAB: 16
CMB: 26
CMD: 37
CMD_other: 41 vs. trip
feats:
- name: Cleave
- name: Flyby Attack
- name: Improved Initiative
- name: Iron Will
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (bite)
skills:
  Appraise: 24
  Diplomacy: 22
  Fly: 12
  Intimidate: 22
  Knowledge (arcana): 24
  Knowledge (history): 24
  Knowledge (planes): 24
  Knowledge (religion): 24
  Perception: 24
  Sense Motive: 24
  Stealth: 12
languages:
- Aklo
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

# Dragon (Esoteric, Astral), Adult Astral Dragon

**Source** Bestiary 5 pg. 88
**XP** 25,600

N Huge dragon (extraplanar)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +24
**Aura** mental static (30 ft., DC 21), _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 21)

##### Defense

**AC** 28, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+1 Dex, +19 natural, –2 size)
**hp** 184 (16d12+80)
**Fort** +15, **Ref** +11, **Will** +17; +4 vs. _[[classes/Psychic|psychic]]_ spells
**Defensive Abilities** _[[universal monster rules/Psychic Resilience|psychic resilience]]_; **DR** 5/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 24

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +23 (2d8+12), 2 claws +22 (2d6+8), 2 wings +20 (1d8+4), tail slap +20 (2d6+12)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, DC 23, 12d6 force), crush
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 16th; concentration +21)
11 PE—_[[spells/Analyze Aura|analyze aura]]_ (3 PE), _[[spells/Aversion|aversion]]_ (2 PE, DC 17), _[[spells/Deja Vu|deja vu]]_ (1 PE), _[[spells/Id Insinuation I|id insinuation I]]_ (3 PE, DC 18), _[[spells/Telekinetic Projectile|telekinetic projectile]]_ (0 PE)
 **_Psychic_ Spells Known** (CL 7th; concentration +12)
 3rd (5/day)—_[[spells/Ego _[[items/Weapon/Whip|Whip]]_ I|ego _whip_ I]]_, _[[spells/Haste|haste]]_
 2nd (7/day)—_[[spells/Blur|blur]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _[[spells/Locate Object|locate object]]_
 1st (8/day)—_[[spells/Burst Of Insight|burst of insight]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Sundering Shards|sundering shards]]_ (DC 16), _[[spells/True Strike|true strike]]_, _[[spells/Unwitting Ally|unwitting ally]]_ (DC 16)
 0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close

##### Statistics
**Str** 27, **Dex** 12, **Con** 20, **Int** 21, **Wis** 20, **Cha** 16
**Base Atk** +16; **CMB** +26; **CMD** 37 (41 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Appraise +24, Diplomacy +22, Fly +12, Intimidate +22, Knowledge (arcana, history, planes, religion) +24, Perception +24, Sense Motive +24, Stealth +12
**Languages** Aklo, Celestial, Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_

Reserved and haughty, these dragons roam the Astral Plane, seeking to expand their knowledge of its esoteric secrets. They hunt to eat, and use _psychic magic_ to fight one another.