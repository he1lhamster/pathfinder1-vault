---
cssclass: [monsters]
title1: Dragon (Primal, Umbral), Ancient Umbral Dragon
title2: Ancient Umbral Dragon
CR: 19
sources:
- name: Bestiary 2
  page: 103
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 204800
alignment: CE
size: Gargantuan
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 29
AC:
  AC: 38
  touch: 5
  flat_footed: 38
  components:
    dex: -1
    natural: 33
    size: -4
HP:
  HP: 337
  long: 25d12+175
saves:
  fort: 21
  ref: 13
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- death effects
- energy drain
- paralysis
- sleep
SR: 30
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +33 (4d6+18/19-20)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
      attack: bite
      bonus:
      - 33
    - text: 2 claws +33 (2d8+12)
      entries:
      - - damage: 2d8+12
      count: 2
      attack: claws
      bonus:
      - 33
    - text: tail slap +31 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 31
    - text: 2 wings +31 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 31
  special:
  - breath weapon (60-ft. cone, 20d8 neg. energy, DC 29)
  - create shadows
  - crush
  - shadow breath (10 Str)
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  - name: project image
    source: default
    freq: At will
  - name: shadow walk
    source: default
    freq: At will
  - name: vampiric touch
    source: default
    freq: At will
  - name: finger of death
    source: default
    freq: 3/day
    DC: 24
  sources:
  - name: default
    CL: 25
    concentration: 32
spells:
  entries:
  - name: destruction
    source: '?'
    level: 7
    DC: 24
  - name: limited wish
    source: '?'
    level: 7
  - name: harm
    source: '?'
    level: 6
    DC: 23
  - name: mislead
    source: '?'
    level: 6
  - name: veil
    source: '?'
    level: 6
    DC: 23
  - name: greater command
    source: '?'
    level: 5
    DC: 22
  - name: slay living
    source: '?'
    level: 5
    DC: 22
  - name: teleport
    source: '?'
    level: 5
  - name: unhallow
    source: '?'
    level: 5
  - name: enervation
    source: '?'
    level: 4
  - name: inflict critical wounds
    source: '?'
    level: 4
    DC: 21
  - name: phantasmal killer
    source: '?'
    level: 4
    DC: 21
  - name: unholy blight
    source: '?'
    level: 4
    DC: 21
  - name: dispel magic
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: inflict serious wounds
    source: '?'
    level: 3
    DC: 20
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 20
  - name: alter self
    source: '?'
    level: 2
  - name: blur
    source: '?'
    level: 2
  - name: command undead
    source: '?'
    level: 2
    DC: 19
  - name: invisibility
    source: '?'
    level: 2
  - name: web
    source: '?'
    level: 2
    DC: 17
  - name: inflict light wounds
    source: '?'
    level: 1
    DC: 18
  - name: grease
    source: '?'
    level: 1
    DC: 18
  - name: magic missile
    source: '?'
    level: 1
  - name: reduce person
    source: '?'
    level: 1
    DC: 18
  - name: shield
    source: '?'
    level: 1
  - name: acid splash
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
    DC: 17
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: disrupt undead
    source: '?'
    level: 0
    DC: 17
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: ray of frost
    source: '?'
    level: 0
  - name: read magic
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
  STR: 35
  DEX: 8
  CON: 25
  INT: 24
  WIS: 25
  CHA: 24
BAB: 25
CMB: 41
CMD: 50
CMD_other: 54 vs. trip
feats:
- name: Bleeding Critical
- name: Critical Focus
- name: Flyby Attack
- name: Greater Vital Strike
- name: Hover
- name: Imp. Critical (bite)
- name: Imp. Initiative
- name: Imp. Vital Strike
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Snatch
- name: Vital Strike
skills:
  Appraise: 35
  Bluff: 35
  Diplomacy: 35
  Fly: 13
  Knowledge (arcana): 35
  Knowledge (local): 35
  Knowledge (planes): 35
  Knowledge (religion): 35
  Perception: 35
  Sense Motive: 35
  Spellcraft: 35
  Stealth: 21
  Survival: 35
languages:
- Abyssal
- Common
- Draconic
- Undercommon
- 4 more
special_qualities:
- ghost bane
- umbral scion
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
desc_long: Cruel and sadistic, umbral dragons prefer the taste of undead flesh or
  ghostly ectoplasm, yet never turn down opportunities to consume living flesh.

---

# Dragon (Primal, Umbral), Ancient Umbral Dragon

**Source** Bestiary 2 pg. 103
**XP** 204,800
CE Gargantuan dragon (extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +35
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 29)

##### Defense

**AC** 38, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 38 (–1 Dex, +33 natural, –4 size)
**hp** 337 (25d12+175)
**Fort** +21, **Ref** +13, **Will** +21
**DR** 15/magic; **Immune** death effects, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 30

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy)
**Melee** bite +33 (4d6+18/19–20), 2 claws +33 (2d8+12), tail slap +31 (2d8+18), 2 wings +31 (2d6+6)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d8 neg. energy, DC 29), create shadows, crush, _[[items/Armor Magic Abilities/Shadow|shadow]]_ breath (10 Str), tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +32)
At will—_[[spells/Darkness|darkness]]_, _[[spells/Project Image|project image]]_, _[[spells/Shadow Walk|shadow walk]]_, _[[spells/Vampiric Touch|vampiric touch]]_
3/day—_[[spells/Finger Of Death|finger of death]]_ (DC 24)
**Spells Known **(CL 15th; concentration +22)
7th (5/day)—_[[spells/Destruction|destruction]]_ (DC 24), _[[spells/Limited Wish|limited wish]]_
6th (7/day)—_[[spells/Harm|harm]]_ (DC 23), _[[spells/Mislead|mislead]]_, _[[spells/Veil|veil]]_ (DC 23)
5th (7/day)—greater _[[spells/Command|command]]_ (DC 22), _[[spells/Slay Living|slay living]]_ (DC 22), teleport, _[[spells/Unhallow|unhallow]]_
4th (7/day)—_[[spells/Enervation|enervation]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 21), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/Unholy Blight|unholy blight]]_ (DC 21)
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 20), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20)
2nd (8/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Blur|blur]]_, _[[spells/Command Undead|command undead]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, web (DC 17)
1st (8/day)—_[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 18), _[[spells/Grease|grease]]_ (DC 18), _[[spells/Magic Missile|magic missile]]_, _[[spells/Reduce Person|reduce person]]_ (DC 18), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Disrupt Undead|disrupt undead]]_ (DC 17), _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +25; **CMB** +41; **CMD** 50 (54 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Hover|Hover]]_, Imp. Critical (bite), Imp. Initiative, Imp. _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Snatch|Snatch]]_, _Vital Strike_
**Skills** Appraise +35, Bluff +35, Diplomacy +35, Fly +13, Knowledge (arcana, local, planes, religion) +35, Perception +35, Sense Motive +35, Spellcraft +35, Stealth +21, Survival +35
**Languages** Abyssal, Common, Draconic, Undercommon, 4 more
**SQ** _[[monsters/Ghost|ghost]]_ _[[spells/Bane|bane]]_, _[[feats/Umbral Scion|umbral scion]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

_[[items/Weapon Magic Abilities/Cruel|Cruel]]_ and sadistic, _[[items/Weapon Magic Abilities/Umbral|umbral]]_ dragons prefer the taste of undead flesh or ghostly ectoplasm, yet never turn down opportunities to consume living flesh.