---
cssclass: [monsters]
title1: Dragon (Imperial, Sovereign), Ancient Sovereign Dragon
title2: Ancient Sovereign Dragon
CR: 20
sources:
- name: Bestiary 3
  page: 101
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 307200
alignment: N
size: Gargantuan
type: dragon
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 30
AC:
  AC: 39
  touch: 5
  flat_footed: 39
  components:
    dex: -1
    natural: 34
    size: -4
HP:
  HP: 377
  long: 26d12+208
saves:
  fort: 23
  ref: 16
  will: 24
DR:
- amount: 15
  weakness: magic
immunities:
- paralysis
- sleep
SR: 31
speeds:
  base: 50
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +37 (4d6+21/19-20)
      entries:
      - - damage: 4d6+21
          crit_range: 19-20
      attack: bite
      bonus:
      - 37
    - text: 2 claws +37 (2d8+14/19-20)
      entries:
      - - damage: 2d8+14
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 37
    - text: gore +36 (2d8+21)
      entries:
      - - damage: 2d8+21
      attack: gore
      bonus:
      - 36
    - text: tail slap +34 (2d8+21)
      entries:
      - - damage: 2d8+21
      attack: tail slap
      bonus:
      - 34
  special:
  - breath weapon (60-ft. cone, 20d6 sonic damage, DC 31)
  - crush (DC 31, 4d6+21)
  - tail sweep (DC 31, 2d6+21)
  - violent retort
space: 20
reach: 15
reach_other: 20 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: calm emotions
    source: default
    freq: At will
  - name: detect evil
    source: default
    freq: At will
  - name: detect good
    source: default
    freq: At will
  - name: prismatic spray
    source: default
    freq: At will
  - name: sympathetic vibration
    source: default
    freq: At will
  - name: tongues
    source: default
    freq: At will
  sources:
  - name: default
    CL: 26
    concentration: 33
spells:
  entries:
  - name: greater teleport
    source: '?'
    level: 7
  - name: limited wish
    source: '?'
    level: 7
  - name: eyebite
    source: '?'
    level: 6
    DC: 23
  - name: mass suggestion
    source: '?'
    level: 6
    DC: 23
  - name: transformation
    source: '?'
    level: 6
  - name: break enchantment
    source: '?'
    level: 5
  - name: dismissal
    source: '?'
    level: 5
    DC: 22
  - name: dominate person
    source: '?'
    level: 5
    DC: 22
  - name: feeblemind
    source: '?'
    level: 5
    DC: 22
  - name: confusion
    source: '?'
    level: 4
    DC: 21
  - name: lesser geas
    source: '?'
    level: 4
    DC: 21
  - name: locate creature
    source: '?'
    level: 4
  - name: rainbow pattern
    source: '?'
    level: 4
    DC: 21
  - name: gaseous form
    source: '?'
    level: 3
  - name: hold person
    source: '?'
    level: 3
    DC: 20
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 20
  - name: suggestion
    source: '?'
    level: 3
    DC: 20
  - name: detect thoughts
    source: '?'
    level: 2
    DC: 19
  - name: fog cloud
    source: '?'
    level: 2
  - name: hideous laughter
    source: '?'
    level: 2
    DC: 19
  - name: scorching ray
    source: '?'
    level: 2
  - name: touch of idiocy
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 18
  - name: chill touch
    source: '?'
    level: 1
    DC: 18
  - name: color spray
    source: '?'
    level: 1
    DC: 18
  - name: endure elements
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: daze
    source: '?'
    level: 0
    DC: 17
  - name: detect magic
    source: '?'
    level: 0
  - name: flare
    source: '?'
    level: 0
    DC: 17
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
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
  STR: 39
  DEX: 8
  CON: 27
  INT: 24
  WIS: 25
  CHA: 24
BAB: 26
CMB: 44
CMD: 53
CMD_other: 57 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Multiattack
- name: Persuasive
- name: Skill Focus (Perception)
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Appraise: 36
  Bluff: 36
  Diplomacy: 40
  Fly: -15
  Heal: 36
  Intimidate: 40
  Knowledge (arcana): 36
  Knowledge (history): 36
  Knowledge (nobility): 36
  Knowledge (planes): 36
  Perception: 42
  Perform (oratory): 33
  Sense Motive: 36
  Spellcraft: 36
languages:
- Abyssal
- Auran
- Celestial
- Common
- Draconic
- Ignan
- Infernal
- Terran
special_qualities:
- change shape
- dogmatic discordance
- golden armor
ecology:
  environment: any mountains
  organization: solitary
  treasure_type: triple
desc_long: Guardians of balance, sovereign dragons, or lungwangs as they are also
  known, were placed in the skies by the gods themselves to safeguard harmony in the
  world.

---

# Dragon (Imperial, Sovereign), Ancient Sovereign Dragon

**Source** Bestiary 3 pg. 101
**XP** 307,200

N Gargantuan dragon
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +42
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 30)

##### Defense

**AC** 39, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 39 (–1 Dex, +34 natural, –4 size)
**hp** 377 (26d12+208)
**Fort** +23, **Ref** +16, **Will** +24
**DR** 15/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 31

##### Offense
**Speed** 50 ft., fly 250 ft. (clumsy)
**Melee** bite +37 (4d6+21/19–20), 2 claws +37 (2d8+14/19–20), gore +36 (2d8+21), tail slap +34 (2d8+21)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d6 sonic damage, DC 31), crush (DC 31, 4d6+21), tail sweep (DC 31, 2d6+21), violent _[[items/Mundane/Retort|retort]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 26th; concentration +33)
At will—_[[spells/Calm Emotions|calm emotions]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Prismatic Spray|prismatic spray]]_, _[[spells/Sympathetic Vibration|sympathetic vibration]]_, _[[spells/Tongues|tongues]]_
**Spells Known **(CL 15th; concentration +22)
7th (5/day)—greater teleport, _[[spells/Limited Wish|limited wish]]_
6th (7/day)—_[[spells/Eyebite|eyebite]]_ (DC 23), mass _[[spells/Suggestion|suggestion]]_ (DC 23), _[[spells/Transformation|transformation]]_
5th (7/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dismissal|dismissal]]_ (DC 22), _[[spells/Dominate Person|dominate person]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 22)
4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 21), lesser geas (DC 21), _[[spells/Locate Creature|locate creature]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 21)
3rd (8/day)—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20), _suggestion_ (DC 20)
2nd (8/day)—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 19), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Chill Touch|chill touch]]_ (DC 18), _[[spells/Color Spray|color spray]]_ (DC 18), _[[spells/Endure Elements|endure elements]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 17), _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 39, **Dex** 8, **Con** 27, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +26; **CMB** +44; **CMD** 53 (57 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw)
**Skills** Appraise +36, Bluff +36, Diplomacy +40, Fly –15, _[[spells/Heal|Heal]]_ +36, Intimidate +40, Knowledge (arcana, history, nobility, planes) +36, Perception +42, Perform (oratory) +33, Sense Motive +36, Spellcraft +36
**Languages** Abyssal, Auran, Celestial, Common, Draconic, Ignan, Infernal, Terran
**SQ** _[[universal monster rules/Change Shape|change shape]]_, dogmatic discordance, golden armor

##### Ecology

**Environment** any mountains
**Organization** solitary
**Treasure** triple

Guardians of balance, sovereign dragons, or lungwangs as they are also known, were placed in the skies by the gods themselves to safeguard harmony in the world.