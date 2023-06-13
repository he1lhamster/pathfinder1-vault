---
cssclass: [monsters]
title1: Dragon (Primal, Crystal), Ancient Crystal Dragon
title2: Ancient Crystal Dragon
CR: 15
sources:
- name: Bestiary 2
  page: 99
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 51200
alignment: CG
size: Huge
type: dragon
subtypes:
- earth
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
  tremorsense: 120
auras:
- name: frightful presence
  radius: 300
  DC: 28
AC:
  AC: 37
  touch: 8
  flat_footed: 37
  components:
    natural: 29
    size: -2
HP:
  HP: 283
  long: 21d12+147
saves:
  fort: 21
  ref: 14
  will: 17
defensive_abilities:
- ray reflection
DR:
- amount: 15
  weakness: magic
immunities:
- paralysis
- sleep
- sonic
SR: 26
speeds:
  base: 60
  burrow: 30
  climb: 30
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +30 (2d8+15/19-20)
      entries:
      - - damage: 2d8+15
          crit_range: 19-20
      attack: bite
      bonus:
      - 30
    - text: 2 claws +29 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: claws
      bonus:
      - 29
    - text: tail slap +27 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: tail slap
      bonus:
      - 27
    - text: 2 wings +27 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 27
  special:
  - breath weapon (50-ft. cone, DC 27, 20d4 sonic, DC 27)
  - crush
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: color spray
    source: default
    freq: At will
    DC: 19
  - name: glitterdust
    source: default
    freq: At will
    DC: 20
  - name: rainbow pattern
    source: default
    freq: At will
    DC: 22
  - name: prismatic spray
    source: default
    freq: 3/day
    DC: 25
  - name: stone to flesh
    source: default
    freq: 3/day
    DC: 24
  sources:
  - name: default
    CL: 21
    concentration: 29
spells:
  entries:
  - name: dimension door
    source: '?'
    level: 4
  - name: phantasmal killer
    source: '?'
    level: 4
    DC: 22
  - name: displacement
    source: '?'
    level: 3
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 21
  - name: major image
    source: '?'
    level: 3
    DC: 21
  - name: blindness/deafness
    source: '?'
    level: 2
    DC: 20
  - name: invisibility
    source: '?'
    level: 2
  - name: minor image
    source: '?'
    level: 2
    DC: 20
  - name: mirror image
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: feather fall
    source: '?'
    level: 1
  - name: magic aura
    source: '?'
    level: 1
  - name: silent image
    source: '?'
    level: 1
    DC: 19
  - name: unseen servant
    source: '?'
    level: 1
  - name: acid splash
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: touch of fatigue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 9
    concentration: 17
    slots:
      4: 6
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 31
  DEX: 10
  CON: 25
  INT: 20
  WIS: 21
  CHA: 26
BAB: 21
CMB: 33
CMD: 43
CMD_other: 47 vs. trip
feats:
- name: Deceitful
- name: Great Fortitude
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Bluff: 36
  Climb: 42
  Disguise: 33
  Fly: 16
  Intimidate: 32
  Knowledge (dungeoneering): 29
  Knowledge (geography): 29
  Perception: 29
  Sense Motive: 29
  Stealth: 16
  Survival: 29
languages:
- Common
- Draconic
- Dwarven
- Elven
- Terran
- Undercommon
special_qualities:
- razor sharp
ecology:
  environment: any underground (Plane of Earth)
  organization: solitary
  treasure_type: triple
desc_long: |-
  Crystal dragons are generally good-natured, though their incredible vanity sometimes causes them to seem aloof and cocky. Any perceived insult against its appearance is all but assured to send a crystal dragon into a rage-which is a problem, as most crystal dragons are prone to seeing insults even where none are intended. Crystal dragons prefer underground lairs, and often go for decades or even centuries without emerging from their extensive cavern lairs onto the surface world above. 

  Crystal dragons tend to be exacting and even obsessive-compulsive, their personalities mirroring the precise and ordered nature of the facets of their scales. A crystal dragon's lair is a well-ordered place-these dragons find the very idea of the classic sprawl of a dragon's hoard to be shameful.

---

# Dragon (Primal, Crystal), Ancient Crystal Dragon

**Source** Bestiary 2 pg. 99
**XP** 51,200

CG Huge dragon (earth, extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +29
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 28)

##### Defense

**AC** 37, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+29 natural, –2 size)
**hp** 283 (21d12+147)
**Fort** +21, **Ref** +14, **Will** +17
**Defensive Abilities** ray reflection; **DR** 15/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep, sonic; **SR** 26

##### Offense
**Speed** 60 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 200 ft. (poor)
**Melee** bite +30 (2d8+15/19–20), 2 claws +29 (2d6+10), tail slap +27 (2d6+15), 2 wings +27 (1d8+5)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 27, 20d4 sonic, DC 27), crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 21th; concentration +29)
At will—_[[spells/Color Spray|color spray]]_ (DC 19), _[[spells/Glitterdust|glitterdust]]_ (DC 20), _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 22)
3/day—_[[spells/Prismatic Spray|prismatic spray]]_ (DC 25), _[[spells/Stone to Flesh|stone to flesh]]_ (DC 24)
**Spells Known **(CL 9th; concentration +17)
4th (6/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 22)
3rd (8/day)—_[[spells/Displacement|displacement]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 21), _[[spells/Major Image|major image]]_ (DC 21)
2nd (8/day)—blindness/deafness (DC 20), _[[spells/Invisibility|invisibility]]_, _[[spells/Minor Image|minor image]]_ (DC 20), _[[spells/Mirror Image|mirror image]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Magic Aura|magic aura]]_, _[[spells/Silent Image|silent image]]_ (DC 19), _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 31, **Dex** 10, **Con** 25, **Int** 20, **Wis** 21, **Cha** 26
**Base Atk** +21; **CMB** +33; **CMD** 43 (47 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Deceitful|Deceitful]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +36, _Climb_ +42, Disguise +33, Fly +16, Intimidate +32, Knowledge (dungeoneering, geography) +29, Perception +29, Sense Motive +29, Stealth +16, Survival +29
**Languages** Common, Draconic, Dwarven, Elven, Terran, Undercommon
**SQ** razor sharp

##### Ecology

**Environment** any underground (Plane of Earth)
**Organization** solitary
**Treasure** triple

Crystal dragons are generally good-natured, though their incredible vanity sometimes causes them to seem aloof and cocky. Any perceived insult against its appearance is all but assured to send a crystal dragon into a _[[spells/Rage|rage]]_—which is a problem, as most crystal dragons are _[[conditions/Prone|prone]]_ to seeing insults even where none are intended. Crystal dragons prefer underground lairs, and often go for decades or even centuries without emerging from their extensive cavern lairs onto the surface world above.

Crystal dragons tend to be exacting and even obsessive-compulsive, their personalities mirroring the precise and ordered nature of the facets of their scales. A crystal dragon’s lair is a well-ordered place—these dragons find the very idea of the classic sprawl of a dragon’s hoard to be shameful.