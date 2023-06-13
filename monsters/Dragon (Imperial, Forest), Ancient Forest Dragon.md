---
cssclass: [monsters]
title1: Dragon (Imperial, Forest), Ancient Forest Dragon
title2: Ancient Forest Dragon
CR: 19
sources:
- name: Bestiary 3
  page: 95
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 204800
alignment: CE
size: Gargantuan
type: dragon
subtypes:
- earth
initiative:
  bonus: 3
senses:
  dragon senses: true
  tremorsense: 60
auras:
- name: frightful presence
  radius: 300
  DC: 29
AC:
  AC: 39
  touch: 5
  flat_footed: 39
  components:
    dex: -1
    natural: 34
    size: -4
HP:
  HP: 387
  long: 25d12+225
saves:
  fort: 22
  ref: 13
  will: 21
DR:
- amount: 10
  weakness: adamantine
immunities:
- paralysis
- poison
- sleep
SR: 30
speeds:
  base: 40
  burrow: 20
  climb: 30
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +35 (4d6+19/19-20)
      entries:
      - - damage: 4d6+19
          crit_range: 19-20
      attack: bite
      bonus:
      - 35
    - text: 2 claws +35 (2d8+13)
      entries:
      - - damage: 2d8+13
      count: 2
      attack: claws
      bonus:
      - 35
    - text: gore +34 (2d8+19)
      entries:
      - - damage: 2d8+19
      attack: gore
      bonus:
      - 34
    - text: tail slap +32 (2d8+19)
      entries:
      - - damage: 2d8+19
      attack: tail slap
      bonus:
      - 32
  special:
  - breath weapon (60-ft. cone, 20d6 piercing damage, DC 32) crush (DC 32, 2d8+19)
  - destructive crush
  - tail sweep (2d6+19, DC 35)
space: 20
reach: 15
reach_other: 20 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: animate plants
    source: default
    freq: At will
  - name: entangle
    source: default
    freq: At will
    DC: 16
  - name: blight
    source: default
    freq: At will
    DC: 20
  - name: pass without trace
    source: default
    freq: At will
  - name: tree stride
    source: default
    freq: At will
  sources:
  - name: default
    CL: 25
    concentration: 30
spells:
  entries:
  - name: power word blind
    source: '?'
    level: 7
  - name: waves of exhaustion
    source: '?'
    level: 7
    DC: 22
  - name: acid fog
    source: '?'
    level: 6
  - name: disintegrate
    source: '?'
    level: 6
    DC: 21
  - name: move earth
    source: '?'
    level: 6
  - name: baleful polymorph
    source: '?'
    level: 5
    DC: 20
  - name: cloudkill
    source: '?'
    level: 5
    DC: 20
  - name: feeblemind
    source: '?'
    level: 5
    DC: 20
  - name: passwall
    source: '?'
    level: 5
  - name: bestow curse
    source: '?'
    level: 4
    DC: 19
  - name: charm monster
    source: '?'
    level: 4
    DC: 19
  - name: solid fog
    source: '?'
    level: 4
  - name: stone shape
    source: '?'
    level: 4
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 18
  - name: wind wall
    source: '?'
    level: 3
  - name: slow
    source: '?'
    level: 3
    DC: 18
  - name: stinking cloud
    source: '?'
    level: 3
    DC: 18
  - name: fog cloud
    source: '?'
    level: 2
  - name: glitterdust
    source: '?'
    level: 2
    DC: 17
  - name: hideous laughter
    source: '?'
    level: 2
    DC: 17
  - name: invisibility
    source: '?'
    level: 2
  - name: touch of idiocy
    source: '?'
    level: 2
  - name: hypnotism
    source: '?'
    level: 1
    DC: 16
  - name: obscuring mist
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: ray of enfeeblement
    source: '?'
    level: 1
    DC: 16
  - name: shield
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  - name: touch of fatigue
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
  STR: 37
  DEX: 8
  CON: 26
  INT: 20
  WIS: 21
  CHA: 20
BAB: 25
CMB: 42
CMD: 51
CMD_other: 55 vs. trip
feats:
- name: Combat Casting
- name: Deceitful
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Natural Armor
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Stealthy
- name: Toughness
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
skills:
  Acrobatics: 24
    when jumping: 28
  Bluff: 35
  Climb: 47
  Disguise: 7
  Escape Artist: 28
  Fly: 0
  Intimidate: 33
  Knowledge (arcana): 31
  Knowledge (nature): 31
  Perception: 33
  Spellcraft: 33
  Stealth: 25
  Survival: 29
languages:
- Common
- Draconic
- Elven
- Goblin
- Sylvan
- Terran
special_qualities:
- change shape
- sound imitation
- woodland stride
ecology:
  environment: any forest
  organization: solitary
  treasure_type: triple
desc_long: Forest dragons, or dilung, are fickle and malevolent dragons that dwell
  in deep, rugged woodlands. While a forest dragon can fly, it prefers to stalk the
  earth, flying only to pursue objects of its wrath.

---

# Dragon (Imperial, Forest), Ancient Forest Dragon

**Source** Bestiary 3 pg. 95
**XP** 204,800
CE Gargantuan dragon (earth)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +33
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 29)

##### Defense

**AC** 39, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 39 (–1 Dex, +34 natural, –4 size)
**hp** 387 (25d12+225)
**Fort** +22, **Ref** +13, **Will** +21
**DR** 10/adamantine; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 30

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 250 ft. (clumsy)
**Melee** bite +35 (4d6+19/19–20), 2 claws +35 (2d8+13), gore +34 (2d8+19), tail slap +32 (2d8+19)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d6 piercing damage, DC 32) crush (DC 32, 2d8+19), destructive crush, tail sweep (2d6+19, DC 35)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +30)
At will—_[[spells/Animate Plants|animate plants]]_, _[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Blight|blight]]_ (DC 20), _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Tree Stride|tree stride]]_
**Spells Known **(CL 15th; concentration +20)
7th (4/day)—_[[spells/Power Word Blind|power word blind]]_, _[[spells/Waves of Exhaustion|waves of exhaustion]]_ (DC 22)
6th (6/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 21), _[[spells/Move Earth|move earth]]_
5th (7/day)—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Cloudkill|cloudkill]]_ (DC 20), _[[spells/Feeblemind|feeblemind]]_ (DC 20), _[[spells/Passwall|passwall]]_
4th (7/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Solid Fog|solid fog]]_, _[[spells/Stone Shape|stone shape]]_
3rd (7/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 18), _[[spells/Wind Wall|wind wall]]_, _[[spells/Slow|slow]]_ (DC 18), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 18)
2nd (7/day)—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (8/day)—_[[spells/Hypnotism|hypnotism]]_ (DC 16), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Shield|shield]]_
0 (at-will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 37, **Dex** 8, **Con** 26, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +25; **CMB** +42; **CMD** 51 (55 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Stealthy|Stealthy]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claws)
**Skills** Acrobatics +24 (+28 when jumping), Bluff +35, _Climb_ +47, Disguise +7, Escape Artist +28, Fly +0, Intimidate +33, Knowledge (arcana, nature) +31, Perception +33, Spellcraft +33, Stealth +25, Survival +29
**Languages** Common, Draconic, Elven, _[[monsters/Goblin|Goblin]]_, Sylvan, Terran
**SQ** _[[universal monster rules/Change Shape|change shape]]_, sound imitation, woodland stride

##### Ecology

**Environment** any forest
**Organization** solitary
**Treasure** triple

Forest dragons, or dilung, are fickle and _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ dragons that dwell in deep, rugged woodlands. While a forest dragon can fly, it prefers to stalk the earth, flying only to pursue objects of its wrath.