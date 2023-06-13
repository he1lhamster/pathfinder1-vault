---
cssclass: [monsters]
title1: Sayona
desc_short: This revolting withered corpse of a woman is dressed in revealing clothes,
  its bare skin wet with fresh blood.
title2: Sayona
CR: 12
sources:
- name: Bestiary 4
  page: 231
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 19200
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 5
senses:
  darkvision: 60
  lifesense: true
AC:
  AC: 26
  touch: 16
  flat_footed: 20
  components:
    dex: 5
    dodge: 1
    natural: 10
HP:
  HP: 161
  long: 17d8+85
  fast_healing: 5
  fast_healing_weakness: see living form
saves:
  fort: 10
  ref: 12
  will: 13
immunities:
- undead traits
resistances:
  cold: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +18 (2d6+1 plus bleed and paralysis)
      entries:
      - - damage: 2d6+1
        - effect: bleed
        - effect: paralysis
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (2d6+1 plus bleed and paralysis)
      entries:
      - - damage: 2d6+1
        - effect: bleed
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 18
  special:
  - absorb blood
  - blood drain (1d4 Con)
  - fear cone (60 ft., DC 23)
  - paralysis (1d4 rounds, DC 23)
  - staggering gaze
spell_like_abilities:
  entries:
  - name: command undead
    source: default
    freq: 3/day
    DC: 17
  - name: dominate person
    source: default
    freq: 3/day
    DC: 20
  - name: fog cloud
    source: default
    freq: 3/day
  - name: gaseous form
    source: default
    freq: 3/day
  - name: invisibility
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 12
    concentration: 17
ability_scores:
  STR: 13
  DEX: 20
  CON:
  INT: 11
  WIS: 12
  CHA: 21
BAB: 12
CMB: 13
CMD: 29
feats:
- name: Dodge
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Spring Attack
- name: Vital Strike
- name: Weapon Finesse
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Bluff: 14
  Diplomacy: 14
  Disguise: 17
  Knowledge (nobility): 8
  Perception: 21
  Sense Motive: 12
  Stealth: 16
languages:
- Abyssal
- Common
- Infernal
special_qualities:
- create spawn
- living form
ecology:
  environment: any land or underground
  organization: solitary or retinue (1d3 plus 2d6 spawn)
  treasure_type: standard
special_abilities:
  Absorb Blood (Su): A sayona adjacent to a bleeding creature automatically accelerates
    the bleeding, dealing 1 point of Con damage to that creature once per round on
    its turn and absorbing the blood through its skin.
  Create Spawn (Su): When a sayona kills a humanoid or fey of Medium or Small size
    with its absorb blood or blood drain ability, the victim rises 24 hours later
    as a ghoul with the advanced creature simple template and the blood drain ability.
    The spawn is the sayona's slave until its master is destroyed.
  Living Form (Su): As a standard action, a sayona can transform into a young, beautiful
    person for 24 hours. It can only use this ability if it has absorbed or drained
    blood in the past hour. In this form, the sayona has the aura of a living creature
    instead of an undead (for the purpose of detect undead and similar effects), its
    fast healing increases to 10, positive energy attacks (such as channel energy)
    deal half damage to it, and it cannot use its fear cone or gaze attack. Exposure
    to holy water or positive energy attacks in this form reduces the duration of
    this transformation by 1d4 hours.
  Staggering Gaze (Su): Staggered for 1d4 rounds, 30 feet, Fortitude DC 23 negates.
    This is a mind-affecting effect. The save DC is Charisma-based.
desc_long: |-
  Occasionally called “weeping vampires” for their ability to cry tears of blood, sayonas are powerful and intelligent undead creatures that hunt mortals to steal from them what they envy most: the ability to exist within living flesh. While they aren't true vampires, similarity between these two creatures creates substantial confusion to those unfamiliar with sayonas. While sayonas and vampires sustain themselves off mortal blood, sayonas don't consume the blood, but rather absorb it through their skin (even when using blood drain), using it to transform their twisted forms back into some semblance of the beauty they had-or believe they had- in life.

  Above all else, sayonas covet youth. Stories of their origins claim that the first sayona was a vain woman who grew old and whose lover left her for a younger paramour; the woman avenged herself by bathing in the blood of her lover's children, then killed herself. Doomed to undeath, she wanders the world crying tears of blood and preying on beautiful young women-slaying them, stealing their beauty, and transforming them into ghastly undead fiends to forever share her fate.

---

# Sayona
This revolting withered corpse of a woman is dressed in revealing clothes, its bare skin wet with fresh blood.
**Source** Bestiary 4 pg. 231
**XP** 19,200
CE Medium undead
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +21

##### Defense

**AC** 26, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 161 (17d8+85); _[[universal monster rules/Fast Healing|fast healing]]_ 5 (see living form)
**Fort** +10, **Ref** +12, **Will** +13
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 30

##### Offense
**Speed** 30 ft.
**Melee** bite +18 (2d6+1 plus _[[universal monster rules/Bleed|bleed]]_ and _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +18 (2d6+1 plus _bleed_ and _paralysis_)
**Special Attacks** absorb blood, _[[universal monster rules/Blood Drain|blood drain]]_ (1d4 Con), _[[universal monster rules/Fear|fear]]_ cone (60 ft., DC 23), _paralysis_ (1d4 rounds, DC 23), staggering _[[universal monster rules/Gaze|gaze]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
3/day—_[[spells/Command Undead|command undead]]_ (DC 17), _[[spells/Dominate Person|dominate person]]_ (DC 20), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Invisibility|invisibility]]_

##### Statistics
**Str** 13, **Dex** 20, **Con** —, **Int** 11, **Wis** 12, **Cha** 21
**Base Atk** +12; **CMB** +13; **CMD** 29
**Feats** _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claw)
**Skills** Bluff +14, Diplomacy +14, Disguise +17, Knowledge (nobility) +8, Perception +21, Sense Motive +12, Stealth +16
**Languages** Abyssal, Common, Infernal
**SQ** create spawn, living form

##### Ecology

**Environment** any land or underground
**Organization** solitary or retinue (1d3 plus 2d6 spawn)
**Treasure** standard

### Special Abilities

**Absorb Blood (Su)** A _[[monsters/Sayona|sayona]]_ adjacent to a bleeding creature automatically accelerates the bleeding, dealing 1 point of Con damage to that creature once per round on its turn and absorbing the blood through its skin.

**Create Spawn (Su)** When a _sayona_ kills a humanoid or fey of _Medium_ or Small size with its absorb blood or _blood drain_ ability, the victim rises 24 hours later as a _[[monsters/Ghoul|ghoul]]_ with the advanced creature simple template and the _blood drain_ ability. The spawn is the _sayona_’s _[[items/Mundane/Slave|slave]]_ until its master is destroyed.

**Living Form (Su)** As a standard action, a _sayona_ can transform into a young, beautiful person for 24 hours. It can only use this ability if it has absorbed or drained blood in the past hour. In this form, the _sayona_ has the aura of a living creature instead of an undead (for the purpose of _[[spells/Detect Undead|detect undead]]_ and similar effects), its _fast healing_ increases to 10, positive energy attacks (such as channel energy) deal half damage to it, and it cannot use its _fear_ cone or _gaze_ attack. Exposure to _[[items/Mundane/Holy water|holy water]]_ or positive energy attacks in this form reduces the duration of this _[[spells/Transformation|transformation]]_ by 1d4 hours.
**Staggering _Gaze_ (Su)** _[[conditions/Staggered|Staggered]]_ for 1d4 rounds, 30 feet, Fortitude DC 23 negates. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

Occasionally _[[items/Weapon Magic Abilities/Called|called]]_ “_[[items/Armor Magic Abilities/Weeping|weeping]]_ vampires” for their ability to cry tears of blood, sayonas are powerful and intelligent undead creatures that hunt mortals to steal from them what they envy most: the ability to exist within living flesh. While they aren’t true vampires, similarity between these two creatures creates substantial _[[spells/Confusion|confusion]]_ to those unfamiliar with sayonas. While sayonas and vampires sustain themselves off mortal blood, sayonas don’t consume the blood, but rather absorb it through their skin (even when using _blood drain_), using it to transform their twisted forms back into some semblance of the beauty they had—or believe they had— in life.

Above all else, sayonas covet youth. Stories of their origins claim that the first _sayona_ was a vain woman who grew old and whose lover left her for a younger paramour; the woman avenged herself by bathing in the blood of her lover’s children, then killed herself. Doomed to undeath, she wanders the world crying tears of blood and preying on beautiful young women—slaying them, stealing their beauty, and transforming them into ghastly undead fiends to forever share her fate.