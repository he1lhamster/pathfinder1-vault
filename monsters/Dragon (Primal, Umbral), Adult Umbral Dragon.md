---
cssclass: [monsters]
title1: Dragon (Primal, Umbral), Adult Umbral Dragon
title2: Adult Umbral Dragon
CR: 14
sources:
- name: Bestiary 2
  page: 102
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 38400
alignment: CE
size: Huge
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 23
AC:
  AC: 29
  touch: 8
  flat_footed: 29
  components:
    natural: 21
    size: -2
HP:
  HP: 195
  long: 17d12+85
saves:
  fort: 15
  ref: 10
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- death effects
- energy drain
- paralysis
- sleep
SR: 25
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +23 (2d8+12/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 23
    - text: tail slap +21 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: tail slap
      bonus:
      - 21
    - text: 2 wings +21 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 21
  special:
  - breath weapon (50-ft. cone, DC 23, 12d8 negative energy, DC 23)
  - crush
  - shadow breath (6 Str)
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  - name: shadow walk
    source: default
    freq: At will
  - name: vampiric touch
    source: default
    freq: At will
  sources:
  - name: default
    CL: 17
    concentration: 22
spells:
  entries:
  - name: dispel magic
    source: '?'
    level: 3
  - name: inflict serious wounds
    source: '?'
    level: 3
    DC: 18
  - name: command undead
    source: '?'
    level: 2
    DC: 17
  - name: invisibility
    source: '?'
    level: 2
  - name: web
    source: '?'
    level: 2
    DC: 17
  - name: grease
    source: '?'
    level: 1
    DC: 16
  - name: inflict light wounds
    source: '?'
    level: 1
    DC: 16
  - name: magic missile
    source: '?'
    level: 1
  - name: reduce person
    source: '?'
    level: 1
    DC: 16
  - name: shield
    source: '?'
    level: 1
  - name: bleed
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: disrupt undead
    source: '?'
    level: 0
    DC: 15
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
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 27
  DEX: 10
  CON: 21
  INT: 20
  WIS: 21
  CHA: 20
BAB: 17
CMB: 27
CMD: 37
CMD_other: 41 vs. trip
feats:
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
  Bluff: 25
  Diplomacy: 25
  Fly: 16
  Knowledge (arcana): 25
  Knowledge (local): 25
  Knowledge (planes): 25
  Perception: 25
  Sense Motive: 25
  Stealth: 18
  Survival: 25
languages:
- Abyssal
- Common
- Draconic
- Undercommon
- 2 more
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

# Dragon (Primal, Umbral), Adult Umbral Dragon

**Source** Bestiary 2 pg. 102
**XP** 38,400
CE Huge dragon (extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +25
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 23)

##### Defense

**AC** 29, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+21 natural, –2 size)
**hp** 195 (17d12+85)
**Fort** +15, **Ref** +10, **Will** +15
**DR** 5/magic; **Immune** cold, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 25

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +23 (2d8+12/19–20), 2 claws +23 (2d6+8), tail slap +21 (2d6+12), 2 wings +21 (1d8+4)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 23, 12d8 negative energy, DC 23), crush, _[[items/Armor Magic Abilities/Shadow|shadow]]_ breath (6 Str)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +22)
At will—_[[spells/Darkness|darkness]]_, _[[spells/Shadow Walk|shadow walk]]_, _[[spells/Vampiric Touch|vampiric touch]]_
**Spells Known **(CL 7th; concentration +12)
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 18)
2nd (7/day)—_[[spells/Command Undead|command undead]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, web (DC 17)
1st (8/day)—_[[spells/Grease|grease]]_ (DC 16), _[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 16), _[[spells/Magic Missile|magic missile]]_, _[[spells/Reduce Person|reduce person]]_ (DC 16), _[[spells/Shield|shield]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Disrupt Undead|disrupt undead]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 27, **Dex** 10, **Con** 21, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +17; **CMB** +27; **CMD** 37 (41 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Hover|Hover]]_, Imp. Critical (bite), Imp. Initiative, Imp. _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Snatch|Snatch]]_, _Vital Strike_
**Skills** Bluff +25, Diplomacy +25, Fly +16, Knowledge (arcana, local, planes) +25, Perception +25, Sense Motive +25, Stealth +18, Survival +25
**Languages** Abyssal, Common, Draconic, Undercommon, 2 more
**SQ** _[[monsters/Ghost|ghost]]_ _[[spells/Bane|bane]]_, _[[feats/Umbral Scion|umbral scion]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

_[[items/Weapon Magic Abilities/Cruel|Cruel]]_ and sadistic, _[[items/Weapon Magic Abilities/Umbral|umbral]]_ dragons prefer the taste of undead flesh or ghostly ectoplasm, yet never turn down opportunities to consume living flesh.