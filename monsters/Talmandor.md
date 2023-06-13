---
cssclass: [monsters]
title1: Talmandor
desc_short: This gloriously plumed anthropomorphic eagle has feathers tipped with
  shimmering gold, and claws with sharp black talons.
title2: Talmandor
CR: 23
sources:
- name: Andoran, Birthplace of Freedom
  page: 62
  link: http://paizo.com/products/btpy9dz4?Pathfinder-Campaign-Setting-Andoran-Birthplace-of-Freedom
XP: 819200
alignment: NG
size: Large
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: 13
senses:
  darkvision: 60
  see invisibility: true
  true seeing: true
auras:
- name: frightful presence
  radius: 60
  DC: 30
- name: protective aura
  radius: 30
  DC: 30
  duration: 10 rounds
- name: quell the profane
AC:
  AC: 40
  touch: 22
  flat_footed: 27
  components:
    dex: 13
    natural: 18
    size: -1
HP:
  HP: 472
  long: 27d10+324
saves:
  fort: 27
  ref: 22
  will: 21
  other: +4 vs. poison
defensive_abilities:
- evasion
DR:
- amount: 15
  weakness: silver and evil
immunities:
- electricity
- petrification
resistances:
  cold: 10
  sonic: 10
SR: 34
speeds:
  base: 40
  fly: 180
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +40 (3d6+12/18-20/×3)
      entries:
      - - damage: 3d6+12
          crit_range: 18-20
          crit_multiplier: 3
      count: 2
      attack: claws
      bonus:
      - 40
    - text: 2 wings +37 (3d6+4)
      entries:
      - - damage: 3d6+4
      count: 2
      attack: wings
      bonus:
      - 37
  special:
  - channel positive energy
  - coruscating charge
  - pounce
  - rend (2 claws, 3d6+12)
  - sacred slasher
  - twin talons
space: 10
reach: 10
spell_like_abilities:
  entries:
  - superscripts:
    - APG
    name: cloak of winds
    source: default
    freq: Constant
  - name: discern lies
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: magic circle against evil
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: daylight
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
  - name: dispel evil
    source: default
    freq: At will
    DC: 22
  - name: displacement
    source: default
    freq: At will
    other: self only
  - name: greater command
    source: default
    freq: At will
    DC: 22
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: hold monster
    source: default
    freq: At will
    DC: 22
  - name: magic missile
    source: default
    freq: At will
  - name: remove fear
    source: default
    freq: At will
  - superscripts:
    - APG
    name: river of wind
    source: default
    freq: At will
    DC: 21
  - name: wind wall
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: 3/day
  - name: control winds
    source: default
    freq: 3/day
  - name: divine power
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: eagle aerie
    source: default
    freq: 3/day
  - name: quickened empowered chain lightning
    source: default
    freq: 3/day
    DC: 23
  - name: holy aura
    source: default
    freq: 3/day
    DC: 25
  - name: holy word
    source: default
    freq: 3/day
    DC: 24
  - name: miracle
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    DC: 24
  - name: spell turning
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
  - name: mass heal
    source: default
    freq: 1/day
  - superscripts:
    - UM
    name: overwhelming presence
    source: default
    freq: 1/day
    DC: 26
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: 1d4+1 advanced avorals
      chance: 100%
  - name: sunburst
    source: default
    freq: 1/day
    DC: 25
  - name: whirlwind
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 26
  DEX: 36
  CON: 35
  INT: 19
  WIS: 23
  CHA: 24
BAB: 27
CMB: 36
CMD: 59
feats:
- name: Bleeding Critical
- superscripts:
  - APG
  name: Dimensional Agility
- superscripts:
  - APG
  name: Dimensional Assault
- superscripts:
  - APG
  name: Dimensional Dervish
- name: Critical Focus
- name: Empower Spell-Like Ability (chain lightning)
- name: Flyby Attack
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (chain lightning)
- name: Staggering Critical
- name: Stunning Critical
- name: Weapon Finesse
- name: Weapon Focus (claws)
skills:
  Acrobatics: 40
  Bluff: 20
  Diplomacy: 30
  Fly: 45
  Handle Animal: 30
  Intimidate: 30
  Knowledge (history): 10
  Knowledge (local): 10
  Knowledge (nobility): 10
  Knowledge (planes): 10
  Perception: 44
  Perform (oratory): 10
  Sense Motive: 36
  Spellcraft: 10
  Stealth: 38
  Use Magic Device: 34
  _racial_mods:
    Perception:
      _: 8
languages:
- Celestial
- Common
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- benevolent mercy
- lay on hands (10d6, 10/day, as a 20th-level paladin)
ecology:
  environment: any air (Nirvana)
  organization: solitary or flight (Talmandor and 3-6 advanced avorals)
  treasure_type: triple
special_abilities:
  Benevolent Mercy (Su): 'When Talmandor uses his lay on hands ability, he also removes
    all of the following conditions from the target: dazed, nauseated, paralyzed,
    poisoned, sickened, and stunned.'
  Channel Positive Energy (Su): Talmandor can expend two uses of his lay on hands
    ability to channel energy as a 20th-level cleric.
  Coruscating Charge (Su): When Talmandor charges, he can transform his body into
    golden light. He becomes incorporeal until he arrives at the end of his charge
    and makes his physical attacks. In this form, he radiates light as a daylight
    spell. Any evil creature whose space he passes through is affected as by sunbeam
    (Reflex DC 35 negates and Reflex half), while good-aligned creatures whose space
    he passes through gain the benefit of good hope for 1d4 rounds. The save DC is
    Constitution-based.
  Protective Aura (Su): Against attacks made or effects created by evil creatures,
    this ability provides a +4 deflection bonus to AC and a +4 resistance bonus on
    saving throws to anyone within 20 feet of Talmandor. Otherwise, it functions as
    a magic circle against evil effect and a lesser globe of invulnerability, both
    with a radius of 20 feet (and a caster level of 20th). The defensive benefits
    from the magic circle are not included in the statistics above.
  Quell the Profane (Su): Talmandor's frightful presence aura affects only evil creatures.
    Evil creatures inside Talmandor's protective aura also become sickened, and profane
    bonuses are suppressed within his aura unless their caster level exceeds 20th.
  Sacred Slasher (Ex): When attacking with his claws, Talmandor adds 1-1/2 times his
    Strength bonus on damage rolls. He also threatens a critical hit on a roll of
    18-20 and multiplies critical hit damage by 3. His claws overcome all damage reduction
    of evil creatures.
  Twin Talons (Ex): When using the attack action, Talmandor can attack a single target
    with both claws.
desc_long: |-
  Talmandor is the celestial patron of Andoran and a great leader of the avoral agathions, surpassed among their kind only by the empyreal lord Ylimancha, the Harborwing. Talmandor abides in the aptly named Soaring Palace of Talmandor the Golden on the plane of Nirvana, yet travels frequently among the planes. In addition to looking in on the nation that has arisen under his wings, he wanders the Outer Sphere, often acting as an ambassador between mortal priesthoods and the immortal servants of Erastil, Iomedae, and Shelyn.

  Like most agathions, Talmandor takes an interest in influencing mortals and bringing them to a place of enlightenment. He is convinced that the greatest enlightenment for mortals can be achieved through social interaction. He has observed that mortals respond best to a full, robust engagement with their fellow citizens, and that it's important to have a voice in the decisionmaking process of one's society. Talmandor sees hereditary aristocracy and primogeniture as shackles slowing society's ascent into a place of justice and peace where all citizens work together for the common good. Talmandor does not want the rights and importance of individuals to be sacrificed for the greater good, and advocates a balance between collective needs and communitarian works on the one hand and the individual's personal responsibilities and liberties on the other.

  According to popular legend, Talmandor developed his democratic theories and shared them with the mortal poet Darl Jubannich, who transcribed them in his nowfamous treatise, On Government. However, while Talmandor favored overturning established structures of power where necessary, he never promoted anarchy and has long felt great sadness over how the core tenets of his political philosophy have been twisted beyond recognition in Galt. He strives to promote moderation and peaceful reconciliation within government, even in times of upheaval.

  In some parts of Andoran, the adulation Talmandor has earned goes beyond respect to outright worship. The agathion steadfastly refuses to seek godhood in his own right, as he believes he can be a better inspiration to the goals of democratic freedom as a powerful outsider who can aid the mortal citizens of Andoran in times of great need, rather than becoming a godlike creature they worship from afar. Talmandor typically assists only those he feels have earned the right to call upon any ally of Andoran, though he is pleased to give advice to anyone if asked in earnest. He often appears to speak when called upon by the People's Council, offering what guidance he can, but never insists that his suggestions be enacted. He has been known to appear at the meetings of smaller city and town councils as well, though as a guest he does not speak until the council asks him to. Only if Andoran faced some threat it found impossible to handle on its own without his aid would Talmandor take direct action to protect the nation, though his regular presence is certainly considered carefully by Andoran's enemies.

  Though Andoran celebrates a feast day in his honor on 4 Erastus, Talmandor insists the celebration is held to honor him in his capacity as one of many heroes of the nation, rather than as its divine protector. Despite his refusal of the mantle of divinity, a few in Andoran (including a small but growing number of oracles and paladins) revere him as a nascent demigod embodying the virtues of hope, liberty, and community, and his worship has begun to grow in small congregations across the country.

  Talmandor is closely associated with birds of prey and as a result is the patron of the Steel Falcons order of the Eagle Knights of Andoran, as well as a frequent advisor to leaders within the order. Talmandor inspires their work as ambassadors of liberty, and he sometimes even sends aid to those in the midst of dangerous political missions aimed at cultivating peace. Those who rise to greatness also receive Talmandor's direct blessing, which he sees as a rightful reward for good works and a tool that allows those blessed to achieve even greater things. If called to serve through powerful magic (such as gate), Talmandor generally answers but refuses to grant direct assistance except to those overwhelmingly outmatched by evil foes. Even then, he generally requires any aid he gives be paid for in massive donations to the poor and oppressed, though he also often offers a free alternative to his direct involvement, such as receiving his blessing (often crafted with miracle) or gaining some insight into the caller's foes.

---

# Talmandor
This gloriously plumed anthropomorphic _[[monsters/Eagle|eagle]]_ has feathers tipped with shimmering gold, and claws with sharp black talons.
**Source** Andoran, Birthplace of _[[spells/Freedom|Freedom]]_ pg. 62
**XP** 819,200

NG Large outsider (agathion, extraplanar, good)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_, _[[spells/True Seeing|true seeing]]_; Perception +44
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 30), protective aura (30 ft., DC 30, 10 rounds), quell the profane

##### Defense

**AC** 40, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+13 Dex, +18 natural, –1 size)
**hp** 472 (27d10+324)
**Fort** +27, **Ref** +22, **Will** +21; +4 vs. poison
**Defensive Abilities** evasion; **DR** 15/silver and evil; **Immune** electricity, petrification; **Resist** cold 10, sonic 10; **SR** 34

##### Offense
**Speed** 40 ft., fly 180 ft. (good)
**Melee** 2 claws +40 (3d6+12/18–20/×3), 2 wings +37 (3d6+4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel positive energy, coruscating charge, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rend|rend]]_ (2 claws, 3d6+12), _[[items/Weapon Magic Abilities/Sacred|sacred]]_ slasher, twin talons
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Cloak of Winds|cloak of winds]]_, _[[spells/Discern Lies|discern lies]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Mind Blank|mind blank]]_, _see invisibility_, _[[spells/Speak with Animals|speak with animals]]_, _true seeing_
At will—aid, _[[spells/Daylight|daylight]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dispel Evil|dispel evil]]_ (DC 22), _[[spells/Displacement|displacement]]_ (self only), greater _[[spells/Command|command]]_ (DC 22), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Hold Monster|hold monster]]_ (DC 22), _[[spells/Magic Missile|magic missile]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/River of Wind|river of wind]]_ (DC 21), _[[spells/Wind Wall|wind wall]]_
3/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Control Winds|control winds]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Eagle Aerie|eagle aerie]]_, quickened empowered _[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Holy Aura|holy aura]]_ (DC 25), _[[spells/Holy Word|holy word]]_ (DC 24), _[[spells/Miracle|miracle]]_, _[[spells/Plane Shift|plane shift]]_ (DC 24), _[[spells/Spell Turning|spell turning]]_
1/day—_[[spells/Control Weather|control weather]]_, mass _[[spells/Heal|heal]]_, _[[spells/Overwhelming Presence|overwhelming presence]]_ (DC 26), _[[universal monster rules/Summon|summon]]_ (level 8, 1d4+1 advanced avorals 100%), _[[spells/Sunburst|sunburst]]_ (DC 25), _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 25)

##### Statistics
**Str** 26, **Dex** 36, **Con** 35, **Int** 19, **Wis** 23, **Cha** 24
**Base Atk** +27; **CMB** +36; **CMD** 59
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Dimensional Agility|Dimensional Agility]]_, _[[feats/Dimensional Assault|Dimensional Assault]]_, _[[feats/Dimensional Dervish|Dimensional Dervish]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_chain lightning_), _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_chain lightning_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** Acrobatics +40, Bluff +20, Diplomacy +30, Fly +45, Handle Animal +30, Intimidate +30, Knowledge (history, local, nobility, planes) +10, Perception +44, Perform (oratory) +10, Sense Motive +36, Spellcraft +10, Stealth +38, Use Magic Device +34; **Racial Modifiers** +8 Perception
**Languages** Celestial, Common, Draconic, Infernal; _speak with animals_; truespeech
**SQ** _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ mercy, lay on hands (10d6, 10/day, as a 20th-level _[[classes/Paladin|paladin]]_)

##### Ecology

**Environment** any air (Nirvana)
**Organization** solitary or _[[universal monster rules/Flight|flight]]_ (_[[monsters/Talmandor|Talmandor]]_ and 3–6 advanced avorals)
**Treasure** triple

### Special Abilities

**_Benevolent_ Mercy (Su)** When _Talmandor_ uses his lay on hands ability, he also removes all of the following conditions from the target: _[[conditions/Dazed|dazed]]_, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Paralyzed|paralyzed]]_, poisoned, _[[conditions/Sickened|sickened]]_, and _[[conditions/Stunned|stunned]]_.

**Channel Positive Energy (Su)** _Talmandor_ can _[[spells/Expend|expend]]_ two uses of his lay on hands ability to channel energy as a 20th-level _[[classes/Cleric|cleric]]_.

**Coruscating Charge (Su)** When _Talmandor_ charges, he can transform his body into golden light. He becomes _[[universal monster rules/Incorporeal|incorporeal]]_ until he arrives at the end of his charge and makes his physical attacks. In this form, he radiates light as a _daylight_ spell. Any evil creature whose space he passes through is affected as by _[[spells/Sunbeam|sunbeam]]_ (Reflex DC 35 negates and Reflex half), while good-aligned creatures whose space he passes through gain the benefit of _[[spells/Good Hope|good hope]]_ for 1d4 rounds. The save DC is Constitution-based.

**Protective Aura (Su)** Against attacks made or effects created by evil creatures, this ability provides a +4 deflection bonus to AC and a +4 _[[universal monster rules/Resistance|resistance]]_ bonus on saving throws to anyone within 20 feet of _Talmandor_. Otherwise, it functions as a _magic circle against evil_ effect and a lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, both with a radius of 20 feet (and a caster level of 20th). The defensive benefits from the magic circle are not included in the statistics above.

**Quell the Profane (Su)** _Talmandor_’s _frightful presence_ aura affects only evil creatures. Evil creatures inside _Talmandor_’s protective aura also become _sickened_, and profane bonuses are suppressed within his aura unless their caster level exceeds 20th.
**_Sacred_ Slasher (Ex)** When attacking with his claws, _Talmandor_ adds 1-1/2 times his Strength bonus on damage rolls. He also threatens a critical hit on a roll of 18–20 and multiplies critical hit damage by 3. His claws overcome all _[[universal monster rules/Damage Reduction|damage reduction]]_ of evil creatures.

**Twin Talons (Ex)** When using the attack action, _Talmandor_ can attack a single target with both claws.

##### Description

_Talmandor_ is the celestial patron of Andoran and a great leader of the avoral agathions, surpassed among their kind only by the empyreal lord Ylimancha, the Harborwing. _Talmandor_ abides in the aptly named Soaring Palace of _Talmandor_ the Golden on the plane of Nirvana, yet travels frequently among the planes. In addition to looking in on the nation that has _[[feats/Arisen|arisen]]_ under his wings, he wanders the Outer Sphere, often acting as an ambassador between mortal priesthoods and the immortal servants of Erastil, Iomedae, and Shelyn.

Like most agathions, _Talmandor_ takes an interest in influencing mortals and bringing them to a place of enlightenment. He is convinced that the greatest enlightenment for mortals can be achieved through social interaction. He has observed that mortals respond best to a full, robust engagement with their fellow citizens, and that it’s important to have a voice in the decisionmaking process of one’s society. _Talmandor_ sees hereditary aristocracy and primogeniture as shackles slowing society’s ascent into a place of justice and peace where all citizens work together for the common good. _Talmandor_ does not want the rights and importance of individuals to be sacrificed for the greater good, and advocates a balance between collective needs and communitarian works on the one hand and the individual’s personal responsibilities and liberties on the other.

According to popular legend, _Talmandor_ developed his democratic theories and shared them with the mortal poet Darl Jubannich, who transcribed them in his nowfamous treatise, On Government. However, while _Talmandor_ favored overturning established structures of power where necessary, he never promoted anarchy and has long felt great sadness over how the core tenets of his political philosophy have been twisted beyond recognition in Galt. He strives to promote moderation and _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_ reconciliation within government, even in times of upheaval.

In some parts of Andoran, the adulation _Talmandor_ has earned goes beyond respect to outright worship. The agathion steadfastly refuses to seek godhood in his own right, as he believes he can be a better inspiration to the goals of democratic _freedom_ as a powerful outsider who can aid the mortal citizens of Andoran in times of great need, rather than becoming a godlike creature they worship from afar. _Talmandor_ typically assists only those he feels have earned the right to call upon any ally of Andoran, though he is pleased to give advice to anyone if asked in earnest. He often appears to speak when _[[items/Weapon Magic Abilities/Called|called]]_ upon by the People’s Council, offering what _[[spells/Guidance|guidance]]_ he can, but never insists that his suggestions be enacted. He has been known to appear at the meetings of smaller city and town councils as well, though as a guest he does not speak until the council asks him to. Only if Andoran faced some threat it found impossible to handle on its own without his aid would _Talmandor_ take direct action to protect the nation, though his regular presence is certainly considered carefully by Andoran’s enemies.

Though Andoran celebrates a feast day in his honor on 4 Erastus, _Talmandor_ insists the celebration is held to honor him in his capacity as one of many heroes of the nation, rather than as its divine protector. Despite his refusal of the mantle of divinity, a few in Andoran (including a small but _[[items/Weapon Magic Abilities/Growing|growing]]_ number of oracles and paladins) revere him as a nascent demigod embodying the virtues of hope, liberty, and community, and his worship has begun to grow in small congregations across the country.

_Talmandor_ is closely associated with birds of prey and as a result is the patron of the Steel Falcons order of the _Eagle_ Knights of Andoran, as well as a frequent advisor to leaders within the order. _Talmandor_ inspires their work as ambassadors of liberty, and he sometimes even sends aid to those in the midst of dangerous political missions aimed at cultivating peace. Those who rise to greatness also receive _Talmandor_’s direct blessing, which he sees as a rightful reward for good works and a tool that allows those _[[feats/Blessed|blessed]]_ to achieve even greater things. If _called_ to serve through powerful magic (such as _[[spells/Gate|gate]]_), _Talmandor_ generally answers but refuses to grant direct assistance except to those overwhelmingly outmatched by evil foes. Even then, he generally requires any aid he gives be paid for in massive donations to the poor and oppressed, though he also often offers a free alternative to his direct involvement, such as receiving his blessing (often crafted with _miracle_) or gaining some insight into the caller’s foes.