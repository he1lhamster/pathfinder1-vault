---
cssclass: [monsters]
title1: Dragon (Esoteric, Occult), Ancient Occult Dragon
title2: Ancient Occult Dragon
CR: 15
sources:
- name: Bestiary 5
  page: 97
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 51200
alignment: NG
size: Huge
type: dragon
initiative:
  bonus: 0
senses:
  appraising sight: true
  aura sight: true
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 25
- name: protective aura
  radius: 20
AC:
  AC: 38
  touch: 8
  flat_footed: 38
  components:
    natural: 30
    size: -2
HP:
  HP: 270
  long: 20d12+140
saves:
  fort: 19
  ref: 12
  will: 20
DR:
- amount: 15
  weakness: magic
immunities:
- paralysis
- sleep
SR: 26
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +29 (2d8+16/19-20)
      entries:
      - - damage: 2d8+16
          crit_range: 19-20
      attack: bite
      bonus:
      - 29
    - text: 2 claws +29 (2d6+11/19-20)
      entries:
      - - damage: 2d6+11
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 29
    - text: 2 wings +27 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 27
    - text: tail slap +27 (2d6+16)
      entries:
      - - damage: 2d6+16
      attack: tail slap
      bonus:
      - 27
  special:
  - breath weapon (50-ft. cone, DC 27, 12d6 cold or fire)
space: 15
reach: 10
reach_other: 15 ft. with bite
psychic_magic:
  entries:
  - name: augury
    PE: 2
  - name: blood biography
    PE: 3
  - name: cognitive block
    PE: 3
  - name: debilitating portent
    PE: 4
  - name: divination
    PE: 4
  - name: forbid action
    PE: 1
    DC: 19
  - name: invisibility
    PE: 2
  - name: mending
    PE: 0
  - name: speak with dead
    PE: 3
  sources:
  - name: default
    CL: 20
    concentration: 27
  PE: 17
spells:
  entries:
  - name: greater teleport
    source: Psychic
    level: 7
  - name: limited wish
    source: Psychic
    level: 7
  - name: blade barrier
    source: Psychic
    level: 6
    DC: 23
  - name: permanent image
    source: Psychic
    level: 6
    DC: 23
  - name: repress memory
    source: Psychic
    level: 6
  - name: dismissal
    source: Psychic
    level: 5
    DC: 22
  - name: mind fog
    source: Psychic
    level: 5
    DC: 22
  - name: psychic crush I
    source: Psychic
    level: 5
  - name: synapse overload
    source: Psychic
    level: 5
  - name: confusion
    source: Psychic
    level: 4
    DC: 21
  - name: dimension door
    source: Psychic
    level: 4
  - name: dream
    source: Psychic
    level: 4
  - name: spell immunity
    source: Psychic
    level: 4
  - name: clairaudience/clairvoyance
    source: Psychic
    level: 3
  - name: gaseous form
    source: Psychic
    level: 3
  - name: mental barrier II
    source: Psychic
    level: 3
  - name: speak with dead
    source: Psychic
    level: 3
    DC: 20
  - name: hideous laughter
    source: Psychic
    level: 2
    DC: 19
  - name: hold person
    source: Psychic
    level: 2
    DC: 19
  - name: protection from arrows
    source: Psychic
    level: 2
  - name: suggestion
    source: Psychic
    level: 2
    DC: 19
  - name: zone of truth
    source: Psychic
    level: 2
    DC: 19
  - name: burst of adrenaline
    source: Psychic
    level: 1
  - name: charm person
    source: Psychic
    level: 1
    DC: 18
  - name: burst of insight
    source: Psychic
    level: 1
  - name: interrogation
    source: Psychic
    level: 1
    DC: 18
  - name: mage armor
    source: Psychic
    level: 1
  - name: detect poison
    source: Psychic
    level: 0
  - name: ghost sound
    source: Psychic
    level: 0
    DC: 17
  - name: grave words
    source: Psychic
    level: 0
  - name: mage hand
    source: Psychic
    level: 0
  - name: message
    source: Psychic
    level: 0
  - name: read magic
    source: Psychic
    level: 0
  - name: resistance
    source: Psychic
    level: 0
  - name: telekinetic projectile
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
  STR: 32
  DEX: 10
  CON: 25
  INT: 24
  WIS: 22
  CHA: 21
BAB: 20
CMB: 33
CMD: 43
CMD_other: 47 vs. trip
feats:
- name: Deceitful
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Perception)
- name: Snatch
skills:
  Appraise: 30
  Bluff: 32
  Diplomacy: 28
  Disguise: 29
  Fly: 15
  Intimidate: 28
  Knowledge (arcana): 30
  Knowledge (geography): 30
  Knowledge (history): 30
  Knowledge (planes): 30
  Knowledge (religion): 30
  Perception: 35
  Sense Motive: 29
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Infernal
- Sylvan
special_qualities:
- change shape
- item mastery
desc_long: Occult dragons infiltrate large urban centers in humanoid form to search
  for esoteric secrets and psychically charged artifacts to add to their hoards.

---

# Dragon (Esoteric, Occult), Ancient Occult Dragon

**Source** Bestiary 5 pg. 97
**XP** 51,200

NG Huge dragon
**Init** +0; **Senses** appraising sight, _[[spells/Aura Sight|aura sight]]_, _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +35
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 25), protective aura (20 ft.)

##### Defense

**AC** 38, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+30 natural, –2 size)
**hp** 270 (20d12+140)
**Fort** +19, **Ref** +12, **Will** +20
**DR** 15/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 26

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +29 (2d8+16/19–20), 2 claws +29 (2d6+11/19–20), 2 wings +27 (1d8+5), tail slap +27 (2d6+16)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 27, 12d6 cold or fire)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 20th; concentration +27)
17 PE—_[[spells/Augury|augury]]_ (2 PE), _[[spells/Blood Biography|blood biography]]_ (3 PE), _[[spells/Cognitive Block|cognitive block]]_ (3 PE), _[[spells/Debilitating Portent|debilitating portent]]_ (4 PE), _[[spells/Divination|divination]]_ (4 PE), _[[spells/Forbid Action|forbid action]]_ (1 PE, DC 19), _[[spells/Invisibility|invisibility]]_ (2 PE), _[[spells/Mending|mending]]_ (0 PE), _[[spells/Speak with Dead|speak with dead]]_ (3 PE)
 **_[[classes/Psychic|Psychic]]_ Spells Known** (CL 15th; concentration +22) 
7th (5/day)—greater teleport, _[[spells/Limited Wish|limited wish]]_
 6th (7/day)—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Permanent Image|permanent image]]_ (DC 23), _[[spells/Repress Memory|repress memory]]_
 5th (7/day)—_[[spells/Dismissal|dismissal]]_ (DC 22), _[[spells/Mind Fog|mind fog]]_ (DC 22), _[[spells/Psychic Crush I|psychic crush I]]_, _[[spells/Synapse Overload|synapse overload]]_
 4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, _[[spells/Spell Immunity|spell immunity]]_
 3rd (8/day)—clairaudience/clairvoyance, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Mental Barrier II|mental barrier II]]_, _speak with dead_ (DC 20)
 2nd (8/day)—_[[spells/Hideous Laughter|hideous laughter]]_ (DC 19), _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Suggestion|suggestion]]_ (DC 19), _[[spells/Zone of Truth|zone of truth]]_ (DC 19)
 1st (8/day)—_[[spells/Burst Of Adrenaline|burst of adrenaline]]_, _[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Burst Of Insight|burst of insight]]_, _[[spells/Interrogation|interrogation]]_ (DC 18), _[[spells/Mage Armor|mage armor]]_
 0 (at will)—_[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 17), _[[spells/Grave Words|grave words]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Telekinetic Projectile|telekinetic projectile]]_, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 32, **Dex** 10, **Con** 25, **Int** 24, **Wis** 22, **Cha** 21
**Base Atk** +20; **CMB** +33; **CMD** 43 (47 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Deceitful|Deceitful]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Snatch|Snatch]]_
**Skills** Appraise +30, Bluff +32, Diplomacy +28, Disguise +29, Fly +15, Intimidate +28, Knowledge (arcana, geography, history, planes, religion) +30, Perception +35, Sense Motive +29
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Infernal, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_, item mastery

Occult dragons infiltrate large urban centers in humanoid form to search for esoteric secrets and psychically charged artifacts to add to their hoards.