---
cssclass: [monsters]
title1: Kaltestrua, Governess of Casnoriva
desc_short: This serpent-bodied, six-armed woman is painfully thin, haggard, and gaunt.
  Bloody sores dot her flesh, and the skulladorned flails she wields drip black liquid.
title2: Kaltestrua, Governess of Casnoriva
CR: 21
sources:
- name: Demons Revisited
  page: 38
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 409600
race: Female
classes:
- marilith sorcerer 7 (Pathfinder RPG Bestiary 63)
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
  DC: 28
AC:
  AC: 38
  touch: 19
  flat_footed: 32
  components:
    armor: 4
    deflection: 4
    dex: 6
    natural: 15
    size: -1
HP:
  HP: 430
  long: 16d10+7d6+318
  HD: 23
saves:
  fort: 28
  ref: 22
  will: 19
defensive_abilities:
- evasion
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 28
speeds:
  base: 30
attacks:
  melee:
  - - text: +4 ghost touch unholy heavy flail +31/+26/+21/+16 (2d8+14/17-20)
      entries:
      - - damage: 2d8+14
          crit_range: 17-20
      attack: +4 ghost touch unholy heavy flail
      bonus:
      - 31
      - 26
      - 21
      - 16
    - text: 4 +3 ghost touch flails +29 (2d6+6/19-20)
      entries:
      - - damage: 2d6+6
          crit_range: 19-20
      count: 4
      attack: +3 ghost touch flails
      bonus:
      - 29
    - text: tail slap +20 (2d6+3)
      entries:
      - - damage: 2d6+3
      attack: tail slap
      bonus:
      - 20
  special:
  - constrict (tail slap, 2d6+10 plus crushing coils)
  - crushing coils
  - infuse weapon
  - multiweapon mastery
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 28
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: project image
    source: default
    freq: At will
    DC: 27
  - name: telekinesis
    source: default
    freq: At will
    DC: 25
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 26
  - name: fly
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: marilith
      amount: 1
      chance: 20%
    - name: nalfeshnee
      amount: 1
      chance: 35%
    - name: hezrous
      amount: 1d4
      chance: 60%
  - name: grave touch
    source: bloodline
    freq: 13/day
    other: 3 rounds
  sources:
  - name: default
    CL: 16
    concentration: 26
  - name: bloodline
    CL: 7
    concentration: 17
spells:
  entries:
  - name: haste
    source: Sorcerer
    level: 3
  - name: major image
    source: Sorcerer
    level: 3
    DC: 23
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: alter self
    source: Sorcerer
    level: 2
  - name: command undead
    source: Sorcerer
    level: 2
    DC: 22
  - name: false life
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: chill touch
    source: Sorcerer
    level: 1
    DC: 21
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 21
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 20
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 20
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 20
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 17
    slots:
      3: 6
      2: 9
      1: 9
      0: at-will
    bloodline: undead
ability_scores:
  STR: 25
  DEX: 23
  CON: 34
  INT: 20
  WIS: 20
  CHA: 30
BAB: 19
CMB: 27
CMB_other: +31 disarm, +31 trip
CMD: 49
CMD_other: 51 vs. disarm, can't be tripped
feats:
- name: Combat Expertise
- name: Critical Focus
- name: Eschew Materials
- name: Greater Disarm
- name: Greater Trip
- name: Improved Critical (heavy flail)
- name: Improved Disarm
- name: Improved Trip
- name: Multiweapon Defense
- name: Power Attack
- name: Staggering Critical
- name: Toughness
- name: Weapon Focus (heavy flail)
- name: Weapon Focus (flail)
skills:
  Acrobatics: 32
  Bluff: 36
  Diplomacy: 36
  Fly: 30
  Intimidate: 36
  Knowledge (engineering): 26
  Knowledge (religion): 31
  Perception: 39
  Sense Motive: 31
  Stealth: 28
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- bloodline arcana (corporeal undead affected by humanoid-affecting spells)
gear:
  gear:
  - +4 ghost touch unholy heavy flail
  - +3 ghost touch flails (4)
  - ring of evasion
desc_long: |-
  Kaltestrua has been the thrall of the Whispering Tyrant for well over a thousand years, a servitude that has had a singular effect upon her appearance. While she is not herself undead (yet), she appears as if she were a bloodstarved vampire, with sallow flesh clinging tightly to her frame and a skeletal pattern of stripes along her otherwise night-black serpentine lower torso. Kaltestrua was key in the Whispering Tyrant's conquest of the college of Casnoriva, and while the lich has now been imprisoned deep under Gallowspire for nearly 9 centuries, rule of Casnoriva has remained in the marilith's control. In an ironic twist, her greatest enemies in maintaining this control are themselves undead-the spectral and ghostly spirits of the academy's previous professors and arcanists continue to fight against the demon and her servants for control of the site. Led by the ghostly wizard Mistress Qais, these undead have never managed to control a majority of Casnoriva, but neither has Kaltestrua ever been able to wholly defeat them. Today, the site remains a battleground, with the marilith eagerly awaiting the return of her master so that, with his support, she might finally seize full control of the academy.

  It requires a gate spell to conjure Kaltestrua, and even then the marilith is particularly ill-tempered at having been pulled away from her post in the academy. Every second she's gone is another second the ghosts have a chance to regain ground or, in a worst-case scenario, to take control of the building. As a result, if a conjurer has a relatively short-term task (taking less than a day) for the marilith, she is more likely to agree to perform the service than most of her kind, if only so she can get started (and thus finish) the task quickly and return home. A spellcaster who thinks to keep her from returning home had best be prepared for her increasing fury, for even bound, Kaltestrua has other minions who will come to aid her if she is gone for too long. Kaltestrua prefers offerings of magical flails-ghost touch weapons are her favorite, but as long as the flails possess enhancement bonuses of at least +2, they'll do. It's a DC 31 check to research Kaltestrua.

---

# Kaltestrua, Governess of Casnoriva
This serpent-bodied, six-armed woman is painfully thin, haggard, and gaunt. Bloody sores dot her flesh, and the skulladorned flails she wields drip black liquid.
**Source** Demons Revisited pg. 38
**XP** 409,600
Female marilith _[[classes/Sorcerer|sorcerer]]_ 7 (Pathfinder RPG Bestiary 63)
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +39
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 28)

##### Defense

**AC** 38, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+4 armor, +4 deflection, +6 Dex, +15 natural, –1 size)
**hp** 430 (23 HD; 16d10+7d6+318)
**Fort** +28, **Ref** +22, **Will** +19
**Defensive Abilities** evasion; **DR** 10/cold iron and good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 28

##### Offense
**Speed** 30 ft.
**Melee** +4 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Heavy flail|heavy flail]]_ +31/+26/+21/+16 (2d8+14/17–20), 4 +3 _ghost touch_ flails +29 (2d6+6/19–20), tail slap +20 (2d6+3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (tail slap, 2d6+10 plus crushing coils), crushing coils, infuse weapon, _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +26)
Constant—_true seeing_, _unholy aura_ (DC 28)
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Project Image|project image]]_ (DC 27), _[[spells/Telekinesis|telekinesis]]_ (DC 25)
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 26), fly
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 marilith 20%, 1 nalfeshnee 35%, or 1d4 hezrous 60%)
**Bloodline _Spell-Like Abilities_ **(CL 7th; concentration +17)
13/day—grave touch (3 rounds)
**_Sorcerer_ Spells Known **(CL 7th; concentration +17)
3rd (6/day)—_[[spells/Haste|haste]]_, _[[spells/Major Image|major image]]_ (DC 23), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (9/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Command Undead|command undead]]_ (DC 22), _[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_
1st (9/day)—_[[spells/Chill Touch|chill touch]]_ (DC 21), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_ (DC 21), _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 20), _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 20), _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 20)
**Bloodline **undead

##### Statistics
**Str** 25, **Dex** 23, **Con** 34, **Int** 20, **Wis** 20, **Cha** 30
**Base Atk** +19; **CMB** +27 (+31 disarm, +31 _[[universal monster rules/Trip|trip]]_); **CMD** 49 (51 vs. disarm, can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_ (_heavy flail_), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Multiweapon Defense|Multiweapon Defense]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_heavy flail_), _Weapon Focus_ (flail)
**Skills** Acrobatics +32, Bluff +36, Diplomacy +36, Fly +30, Intimidate +36, Knowledge (engineering) +26, Knowledge (religion) +31, Perception +39, Sense Motive +31, Stealth +28
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** bloodline arcana (corporeal undead affected by humanoid-affecting spells)
**Gear** +4 _ghost touch_ _unholy_ _heavy flail_, +3 _ghost touch_ flails (4), _[[items/Ring/Ring of Evasion|ring of evasion]]_

##### Description

Kaltestrua has been the thrall of the Whispering Tyrant for well over a thousand years, a servitude that has had a singular effect upon her appearance. While she is not herself undead (yet), she appears as if she were a bloodstarved _[[monsters/Vampire|vampire]]_, with sallow flesh clinging tightly to her frame and a skeletal pattern of stripes along her otherwise night-black serpentine lower torso. Kaltestrua was key in the Whispering Tyrant’s conquest of the college of Casnoriva, and while the _[[monsters/Lich|lich]]_ has now been imprisoned deep under Gallowspire for nearly 9 centuries, rule of Casnoriva has remained in the marilith’s control. In an ironic twist, her greatest enemies in maintaining this control are themselves undead—the spectral and ghostly spirits of the academy’s previous professors and arcanists continue to fight against the demon and her servants for control of the site. Led by the ghostly _[[classes/Wizard|wizard]]_ Mistress Qais, these undead have never managed to control a majority of Casnoriva, but neither has Kaltestrua ever been able to wholly defeat them. Today, the site remains a battleground, with the marilith eagerly awaiting the return of her master so that, with his support, she might finally seize full control of the academy.

It requires a _[[spells/Gate|gate]]_ spell to conjure Kaltestrua, and even then the marilith is particularly ill-tempered at having been pulled away from her post in the academy. Every second she’s gone is another second the ghosts have a chance to regain ground or, in a worst-case scenario, to take control of the building. As a result, if a conjurer has a relatively short-term task (taking less than a day) for the marilith, she is more likely to agree to perform the service than most of her kind, if only so she can get started (and thus finish) the task quickly and return home. A spellcaster who thinks to keep her from returning home had best be prepared for her increasing fury, for even bound, Kaltestrua has other minions who will come to aid her if she is gone for too long. Kaltestrua prefers offerings of magical flails—_ghost touch_ weapons are her favorite, but as long as the flails possess enhancement bonuses of at least +2, they’ll do. It’s a DC 31 check to research Kaltestrua.