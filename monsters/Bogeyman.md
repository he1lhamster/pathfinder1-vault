---
cssclass: [monsters]
title1: Bogeyman
desc_short: Dressed in a long dark coat and a tall hat, this lanky, fanged humanoid
  exudes an almost palpable aura of horror.
title2: Bogeyman
CR: 10
sources:
- name: Bestiary 3
  page: 42
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 9600
alignment: NE
size: Medium
type: fey
initiative:
  bonus: 9
senses:
  low-light vision: true
auras:
- name: deepest fear
  radius: 30
  DC: 25
AC:
  AC: 23
  touch: 23
  flat_footed: 17
  components:
    deflection: 7
    dex: 5
    dodge: 1
HP:
  HP: 93
  long: 17d6+34
  other: terrible rejuvenation 5
saves:
  fort: 9
  ref: 15
  will: 13
DR:
- amount: 15
  weakness: cold iron
SR: 21
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +13 (1d8+1/19-20)
      entries:
      - - damage: 1d8+1
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - sneak attack +6d6
  - striking fear
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: gaseous form
    source: default
    freq: At will
  - name: ghost sound
    source: default
    freq: At will
    DC: 17
  - name: invisibility
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 20
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 21
  - name: hold person
    source: default
    freq: 3/day
    DC: 20
  - name: quickened phantasmal killer
    source: default
    freq: 3/day
    DC: 21
  - name: nightmare
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 16
    concentration: 17
ability_scores:
  STR: 12
  DEX: 21
  CON: 14
  INT: 15
  WIS: 16
  CHA: 25
BAB: 8
CMB: 9
CMD: 32
feats:
- name: Dodge
- name: Great Fortitude
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Mobility
- name: Quicken Spell-Like Ability (phantasmal killer)
- name: Skill Focus (Stealth)
- name: Spring Attack
- name: Weapon Finesse
skills:
  Bluff: 27
  Diplomacy: 20
  Disable Device: 15
  Escape Artist: 18
  Intimidate: 28
  Knowledge (local): 16
  Perception: 23
  Sense Motive: 23
  Spellcraft: 12
  Stealth: 35
  _racial_mods:
    Intimidate:
      _: 4
    Stealth:
      _: 4
languages:
- Aklo
- Common
- tongues
ecology:
  environment: any
  organization: solitary
  treasure_type: double
special_abilities:
  Deepest Fear (Su): A bogeyman is cloaked in a 30-foot aura of fear. This aura manifests
    as a shifting haze of images that reflect the viewer's deepest fears. The first
    time it ends its turn within the aura, a creature must make a DC 25 Will save
    or become shaken for as long as it stays within the aura. If the creature succeeds
    at the saving throw, it cannot be affected again by the aura for another 24 hours.
    This is a fear effect. The DC is Charisma-based.
  Striking Fear (Su): If a bogeyman confirms a critical hit or a sneak attack with
    one of its claws on a target currently suffering a fear effect, that effect automatically
    becomes one step more severe (shaken creatures become frightened, frightened creatures
    become panicked, and panicked creatures cower in fear). A DC 25 Will save negates
    this increase. In addition, a critical hit from the bogeyman's claw forces any
    target that has successfully saved against the creature's fear aura to make another
    Will save against its effects, even if 24 hours have not yet passed. This is a
    fear effect. The DC is Charisma-based.
  Terrible Rejuvenation (Su): A bogeyman gains fast healing 5 while any creature within
    its deepest fear aura is suffering from a fear effect, including any fear effect
    created by the aura itself.
desc_long: |-
  Many believe that the most cruel and mischievous fey become bogeymen as a punishment or a reward for their actions. Others see bogeymen as supernatural manifestations of society's willingness to do itself harm.

  Bogeymen use their powers to haunt houses or secluded natural places where they can hunt prey unobserved. They relish using their ghost sound ability to hint at their presence long before they fully reveal themselves. It is not uncommon for a bogeyman to hide under a bed, or in a closet left slightly ajar, for days or even weeks, all the while feeding on its victims' growing realization that they are not alone.

  The most evil bogeymen are those who abandon the tactic of feeding on one person's fears at a time and take up roles of mass murderers or serial killers, or other pursuits designed to drive fear into the hearts of an entire city of victims. True to their name, all bogeymen are male. Sometimes, children whom they steal away to secret lairs emerge years later, transformed into new bogeymen, and return home to continue their supernatural father's work.

---

# Bogeyman
Dressed in a long dark coat and a tall _[[items/Mundane/Hat|hat]]_, this lanky, fanged humanoid exudes an almost palpable aura of horror.
**Source** Bestiary 3 pg. 42
**XP** 9,600

NE Medium fey
**Init** +9; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +23
**Aura** deepest _[[universal monster rules/Fear|fear]]_ (30 ft., DC 25)

##### Defense

**AC** 23, touch 23, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 93 (17d6+34); terrible rejuvenation 5
**Fort** +9, **Ref** +15, **Will** +13
**DR** 15/cold iron; **SR** 21

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +13 (1d8+1/19–20)
**Special Attacks** sneak attack +6d6, striking _fear_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +17)
Constant—_[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Darkness|darkness]]_, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Suggestion|suggestion]]_ (DC 20)
3/day—_[[spells/Crushing Despair|crushing despair]]_ (DC 21), _[[spells/Hold Person|hold person]]_ (DC 20), quickened _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21)
1/day—_[[spells/Nightmare|nightmare]]_ (DC 22)

##### Statistics
**Str** 12, **Dex** 21, **Con** 14, **Int** 15, **Wis** 16, **Cha** 25
**Base Atk** +8; **CMB** +9; **CMD** 32
**Feats** _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_phantasmal killer_), _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +27, Diplomacy +20, Disable Device +15, Escape Artist +18, Intimidate +28, Knowledge (local) +16, Perception +23, Sense Motive +23, Spellcraft +12, Stealth +35; **Racial Modifiers** +4 Intimidate, +4 Stealth
**Languages** Aklo, Common; _tongues_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double

### Special Abilities

**Deepest _Fear_ (Su)** A _[[monsters/Bogeyman|bogeyman]]_ is cloaked in a 30-foot aura of _fear_. This aura manifests as a shifting haze of images that reflect the viewer’s deepest fears. The first time it ends its turn within the aura, a creature must make a DC 25 Will save or become _[[conditions/Shaken|shaken]]_ for as long as it stays within the aura. If the creature succeeds at the saving throw, it cannot be affected again by the aura for another 24 hours. This is a _fear_ effect. The DC is Charisma-based.
**Striking _Fear_ (Su)** If a _bogeyman_ confirms a critical hit or a sneak attack with one of its claws on a target currently suffering a _fear_ effect, that effect automatically becomes one step more severe (_shaken_ creatures become _[[conditions/Frightened|frightened]]_, _frightened_ creatures become _[[conditions/Panicked|panicked]]_, and _panicked_ creatures cower in _fear_). A DC 25 Will save negates this increase. In addition, a critical hit from the _bogeyman_’s claw forces any target that has successfully saved against the creature’s _fear_ aura to make another Will save against its effects, even if 24 hours have not yet passed. This is a _fear_ effect. The DC is Charisma-based.

**Terrible Rejuvenation (Su)** A _bogeyman_ gains _[[universal monster rules/Fast Healing|fast healing]]_ 5 while any creature within its deepest _fear_ aura is suffering from a _fear_ effect, including any _fear_ effect created by the aura itself.

##### Description

Many believe that the most _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and mischievous fey become bogeymen as a punishment or a reward for their actions. Others see bogeymen as supernatural manifestations of society’s willingness to do itself _[[spells/Harm|harm]]_.

Bogeymen use their powers to haunt houses or secluded natural places where they can hunt prey unobserved. They relish using their _ghost sound_ ability to hint at their presence long before they fully reveal themselves. It is not uncommon for a _bogeyman_ to hide under a bed, or in a closet left slightly ajar, for days or even weeks, all the while feeding on its victims’ _[[items/Weapon Magic Abilities/Growing|growing]]_ realization that they are not alone.

The most evil bogeymen are those who abandon the tactic of feeding on one person’s fears at a time and take up roles of mass murderers or serial killers, or other pursuits designed to drive _fear_ into the hearts of an entire city of victims. True to their name, all bogeymen are male. Sometimes, children whom they steal away to secret lairs emerge years later, transformed into new bogeymen, and return home to continue their supernatural father’s work.