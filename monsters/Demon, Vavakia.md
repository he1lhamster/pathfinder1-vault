---
cssclass: [monsters]
title1: Demon, Vavakia
desc_short: This reptilian demon has a quadrupedal dinosaur's lower body,a vaguely
  humanoid upper torso, and a draconic saurian head.
title2: Vavakia
CR: 18
sources:
- name: Bestiary 6
  page: 88
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 2: Lords of Chaos'
  page: 60
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderChronicles/v5748btpy8hij
XP: 153600
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 2
senses:
  darkvision: 60
  true seeing: true
auras:
- name: frightful presence
  radius: 60
  DC: 25
- name: unholy aura
AC:
  AC: 35
  touch: 14
  flat_footed: 33
  components:
    armor: 8
    deflection: 4
    dex,+13 natural: 2
    size: -2
HP:
  HP: 297
  long: 18d10+198
saves:
  fort: 26
  ref: 12
  will: 22
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- electricity
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 29
speeds:
  base: 45
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 unholy ranseur +28/+23/+18/+13 (3d6+17/×3) orbite +27 (3d6+11 plus
        smoking wound)
      entries:
      - - damage: 3d6+11
        - effect: smoking wound
      attack: +1 unholy ranseur +28/+23/+18/+13 (3d6+17/×3) orbite
      bonus:
      - 27
    - text: 2 claws +27(1d8+11)
      entries:
      - - damage: 1d8+11
      count: 2
      attack: claws
      bonus:
      - 27
    - text: tail slap +22 (2d8+5 plus stun)
      entries:
      - - damage: 2d8+5
        - effect: stun
      attack: tail slap
      bonus:
      - 22
  special:
  - breath weapon
  - trample (4d8+16, DC 30)
space: 15
reach: 15
reach_other: 30 ft. with ranseur
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 24
  - name: enervation
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus worn armor plus 50 additional lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 21
  - name: blasphemy
    source: default
    freq: 3/day
    DC: 23
  - name: quickened enervation
    source: default
    freq: 3/day
  - name: power word stun
    source: default
    freq: 3/day
    DC: 24
  - name: earthquake
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: marilith
      amount: 1
      chance: 40%
    - name: nalfeshnees
      amount: 1d3
      chance: 60%
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 32
  DEX: 14
  CON: 33
  INT: 18
  WIS: 21
  CHA: 23
BAB: 18
CMB: 31
CMB_other: +33 bull rush
CMD: 47
CMD_other: 49 vs. bull rush
feats:
- name: Awesome Blow
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: PowerAttack
- name: Quicken Spell-Like Ability (enervation)
- name: Vital Strike
skills:
  Bluff: 27
  Fly: 16
  Intimidate: 27
  Knowledge (arcana,planes): 25
  Perception: 34
  Sense Motive: 26
  Spellcraft: 25
  Stealth: 20
  Swim: 26
  _racial_mods:
    _other: +8 Perception,+8 Stealth
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or warband (1 vavakia plus 2-4 hezrousand 2-8 vrocks)
  treasure_type: standard
  treasure:
  - +2 breastplate
  - +1 unholy ranseur
  - othertreasure
special_abilities:
  Breath Weapon (Su): Once every 1d4 rounds, a vavakia can breathe out a 60-foot cone
    of green fire that seems to writhe and coil with the tortured shapes of a thousand
    screaming ghosts. This green fire comprises countless souls the vavakia has consumed,
    and these vomited souls consume flesh as surely as they consume sanity. A creature
    struck by this breath weapon takes 20d6 points of damage (Reflex DC 30 half) as
    the raw profane power blackens and melts its flesh and skin. Evil creatures take
    half damage from the breath weapon, but good creatures that take any damage from
    a vavakia's breath weapon are automatically staggered for 1 round by the excruciating
    sensation. In addition, any living creature that takes damage from a vavakia's
    breath weapon must also succeed at a DC 30 Fortitude save or take 1d8 points of
    Wisdom drain as its sanity slips away into madness. Immediately after the vavakia
    expels this green soulfire, the wailing flames flow in reverse into the demon's
    gullet through its open maw. This restores 1d8 hit points to the vavakia for each
    creature that was damaged by its breath weapon. The Wisdom drain element of this
    breath weapon is a mindaffecting effect. The save DC is Constitution-based.
  Smoking Wound (Su): The wounds caused by a vavakia's fangs result in terrible, eerie
    wounds that constantly weep wisps of green smoke rather than blood, a grim manifestation
    of the demon's effect on a mortal soul. Each time a vavakia bites a creature,
    it inflicts 2 negative levels. The wounds continue to smoke as long as the victim
    suffers those negative levels, causing the victim to become sickened from the
    hideous sensation and rank smell of the vapors. An effect that removes this sickened
    condition without restoring the negative levels only temporarily causes the wounds
    to stop smoking-they begin smoking again in 1d6 rounds. Nonliving creatures bitten
    by a vavakia are immune to its energy-draining bite and do not exhibit smoking
    wounds. The Fortitude save to remove these negative levels is DC 25. The save
    DC is Charisma-based.
  Stun (Ex): A creature struck by a vavakia's tail slap must succeed at a DC 30 Fortitude
    save or be stunned for 1 round. On a critical hit, the stun effect lasts for 1d4
    rounds on a failed save and 1 round on a successful save. The save DC is Constitution-based.
desc_long: |-
  Vavakias are immense demons of great power. Saurian in shape, appetite, and destructive power, they are most often encountered on the Material Plane, though not as demons conjured by spellcasters to serve, but rather as violent invaders come to the world through tears in reality or portals to the deeper rifts. On the Material Plane, a single vavakia is a formidable presence, for the strange demon is driven to feed on living souls and spread destruction- roles at which it excels. 

  A vavakia demon measures 30 feet in length and stands 15 feet tall, weighing in at 6,000 pounds. Vavakias form on the Abyss from particularly cruel mortal souls who, in life, practiced the vile act of extracting, enslaving, and even consuming other souls. When such a sinful creature arrives on the Abyss, it brings with it partially absorbed fragments of souls from its victims, which it incorporates during its horrific transformation into one of the Abyss's most dangerous forms of demonic life. 

  The creation of the first vavakias in this manner came at the hands of the demon queen Lamashtu, who was unsatisfied with the raw physical might and monstrous shape of her earliest demonic minions. In those early days, before she had become a deity, Lamashtu was already quite interested in the method by which the Abyss transformed the souls of sinful mortals into demons. When she learned that this process had first been triggered by the daemons, she was at once intrigued and enraged-intrigued because she knew that anything the Horsemen of the Apocalypse could do, she could do, and enraged at the idea that she owed her very existence to the curiosity of a daemonic lord. Though Lamashtu herself rose from the Abyss spontaneously, shortly after the daemons first “taught” the Abyss how to process sinful souls, that difference meant little to the Mother of Monsters. Fueled by rage, she waged war against Abaddon for many years and captured two Horsemen of the Apocalypse- predecessors of those who hold those titles now. She murdered one of them and forced from the other the secret method of manipulating the Abyss and its souls before murdering him as well. Both murdered Horsemen were soon replaced on Abaddon, but by that point Lamashtu's wrath had been spent and all that remained was her own curiosity. 

  Most of Lamashtu's earliest attempts to create demonic life were hideous failures, but Lamashtu found joy and delight even in these failures. It wasn't until the demon used her own body as an incubator to shape and then eventually birth the first vavakias that she found real success. Lamashtu's early work in creating and manipulating the Abyss in this manner may have much to do with her resulting rise in power to the position of queen of demons-had not her escalating war with Pazuzu forced her attentions away from this hideous art form, there's no telling what other strange demonic races she might have birthed upon the world. Now that she is a true goddess, Lamashtu's interests expand far beyond the curiosities of the Abyss, and she has little time or desire to wallow in her home plane's fecund properties. Of course, other demon lords throughout the Abyss are eager to learn these secrets, but to date, none have managed to duplicate Lamashtu's feats of creation. 

  In any event, the vavakias themselves have proven a phenomenal success and are among the Abyss's most dangerous demonic races today-and since the creation of the first of their kind, the Abyss itself seems eager to spawn more and more of these deadly demons. 

  Though originally created to serve as living weapons of war, the vavakias have long since established their own presence as Abyssal warlords and conquerors. While some pledge their service to powerful demon lords, most vavakias rule small empires of their own in the Abyss, typically in remote corners infested with jungles, swamps, and other primeval terrains.

---

# Demon, Vavakia
This reptilian demon has a quadrupedal dinosaur’s lower body,

a vaguely humanoid upper torso, and a draconic _[[monsters/Saurian|saurian]]_ head.
**Source** Bestiary 6 pg. 88, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 2: Lords of Chaos pg. 60
**XP** 153,600
CE Huge outsider (chaotic, demon, evil, extraplanar)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +34
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 25), _[[spells/Unholy Aura|unholy aura]]_

##### Defense

**AC** 35, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+8 armor, +4 deflection, +2 Dex,

+13 natural, –2 size)
**hp** 297 (18d10+198)
**Fort** +26, **Ref** +12, **Will** +22
**DR** 15/cold iron and good; **Immune** electricity, fire, poison; **Resist** acid 10, cold 10; **SR** 29

##### Offense
**Speed** 45 ft., fly 60 ft. (average)
**Melee** +1 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Ranseur|ranseur]]_ +28/+23/+18/+13 (3d6+17/×3) or

bite +27 (3d6+11 plus smoking wound), 2 claws +27

(1d8+11), tail slap +22 (2d8+5 plus stun)
**Space** 15 ft., **Reach** 15 ft. (30 ft. with _ranseur_)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, _[[universal monster rules/Trample|trample]]_ (4d8+16, DC 30)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_true seeing_, _unholy aura_ (DC 24) 
At will—_[[spells/Enervation|enervation]]_, greater teleport (self plus worn armor plus 50 additional lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 21) 
3/day—_[[spells/Blasphemy|blasphemy]]_ (DC 23), quickened _enervation_, _[[spells/Power Word Stun|power word stun]]_ (DC 24) 
1/day—_[[spells/Earthquake|earthquake]]_, _[[universal monster rules/Summon|summon]]_ (level 6, 1 marilith 40% or 1d3 nalfeshnees 60%)

##### Statistics
**Str** 32, **Dex** 14, **Con** 33, **Int** 18, **Wis** 21, **Cha** 23
**Base Atk** +18; **CMB** +31 (+33 bull rush); **CMD** 47 (49 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, Power

Attack, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_enervation_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +27, Fly +16, Intimidate +27, Knowledge (arcana,

planes) +25, Perception +34, Sense Motive +26, Spellcraft +25,

Stealth +20, Swim +26; **Racial Modifiers** +8 Perception,

+8 Stealth
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or warband (1 vavakia plus 2–4 hezrous

and 2–8 vrocks)
**Treasure** standard (+2 _[[items/Armor/Breastplate|breastplate]]_, +1 _unholy_ _ranseur_, other

treasure)

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds, a vavakia can breathe out a 60-foot cone of green fire that seems to writhe and coil with the tortured shapes of a thousand screaming ghosts. This green fire comprises countless souls the vavakia has consumed, and these vomited souls consume flesh as surely as they consume sanity. A creature struck by this _breath weapon_ takes 20d6 points of damage (Reflex DC 30 half) as the raw profane power blackens and melts its flesh and skin. Evil creatures take half damage from the _breath weapon_, but good creatures that take any damage from a vavakia’s _breath weapon_ are automatically _[[conditions/Staggered|staggered]]_ for 1 round by the excruciating sensation. In addition, any living creature that takes damage from a vavakia’s _breath weapon_ must also succeed at a DC 30 Fortitude save or take 1d8 points of Wisdom drain as its sanity slips away into madness. Immediately after the vavakia expels this green soulfire, the wailing flames flow in reverse into the demon’s gullet through its open maw. This restores 1d8 hit points to the vavakia for each creature that was damaged by its _breath weapon_. The Wisdom drain element of this _breath weapon_ is a mindaffecting effect. The save DC is Constitution-based.
**Smoking Wound (Su)** The wounds caused by a vavakia’s fangs result in terrible, eerie wounds that constantly weep wisps of green smoke rather than blood, a grim manifestation of the demon’s effect on a mortal soul. Each time a vavakia bites a creature, it inflicts 2 negative levels. The wounds continue to smoke as long as the victim suffers those negative levels, causing the victim to become _[[conditions/Sickened|sickened]]_ from the hideous sensation and rank smell of the vapors. An effect that removes this _sickened_ condition without restoring the negative levels only temporarily causes the wounds to stop smoking—they begin smoking again in 1d6 rounds. Nonliving creatures bitten by a vavakia are immune to its energy-draining bite and do not exhibit smoking wounds. The Fortitude save to remove these negative levels is DC 25. The save DC is Charisma-based.
**Stun (Ex)** A creature struck by a vavakia’s tail slap must succeed at a DC 30 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1 round. On a critical hit, the stun effect lasts for 1d4 rounds on a failed save and 1 round on a successful save. The save DC is Constitution-based.

##### Description

Vavakias are immense demons of great power. _Saurian_ in shape, appetite, and destructive power, they are most often encountered on the Material Plane, though not as demons conjured by spellcasters to serve, but rather as violent invaders come to the world through tears in reality or portals to the deeper rifts. On the Material Plane, a single vavakia is a formidable presence, for the strange demon is driven to feed on living souls and spread _[[spells/Destruction|destruction]]_— roles at which it excels.

A vavakia demon measures 30 feet in length and stands 15 feet tall, weighing in at 6,000 pounds. Vavakias form on the Abyss from particularly _[[items/Weapon Magic Abilities/Cruel|cruel]]_ mortal souls who, in life, practiced the vile act of extracting, enslaving, and even consuming other souls. When such a sinful creature arrives on the Abyss, it brings with it partially absorbed fragments of souls from its victims, which it incorporates during its horrific _[[spells/Transformation|transformation]]_ into one of the Abyss’s most dangerous forms of demonic life.

The creation of the first vavakias in this manner came at the hands of the demon queen Lamashtu, who was unsatisfied with the raw physical might and monstrous shape of her earliest demonic minions. In those early days, before she had become a deity, Lamashtu was already quite interested in the method by which the Abyss transformed the souls of sinful mortals into demons. When she learned that this process had first been triggered by the daemons, she was at once intrigued and enraged—intrigued because she knew that anything the Horsemen of the Apocalypse could do, she could do, and enraged at the idea that she owed her very existence to the curiosity of a daemonic lord. Though Lamashtu herself rose from the Abyss spontaneously, shortly after the daemons first “taught” the Abyss how to process sinful souls, that difference meant little to the Mother of Monsters. Fueled by _[[spells/Rage|rage]]_, she waged war against Abaddon for many years and captured two Horsemen of the Apocalypse— predecessors of those who hold those titles now. She murdered one of them and forced from the other the secret method of manipulating the Abyss and its souls before murdering him as well. Both murdered Horsemen were soon replaced on Abaddon, but by that point Lamashtu’s wrath had been spent and all that remained was her own curiosity.

Most of Lamashtu’s earliest attempts to create demonic life were hideous failures, but Lamashtu found joy and delight even in these failures. It wasn’t until the demon used her own body as an incubator to shape and then eventually birth the first vavakias that she found real success. Lamashtu’s early work in creating and manipulating the Abyss in this manner may have much to do with her resulting rise in power to the position of queen of demons—had not her escalating war with Pazuzu forced her attentions away from this hideous art form, there’s no telling what other strange demonic races she might have birthed upon the world. Now that she is a true goddess, Lamashtu’s interests expand far beyond the curiosities of the Abyss, and she has little time or desire to wallow in her home plane’s fecund properties. Of course, other demon lords throughout the Abyss are eager to learn these secrets, but to date, none have managed to duplicate Lamashtu’s feats of creation.

In any event, the vavakias themselves have proven a phenomenal success and are among the Abyss’s most dangerous demonic races today—and since the creation of the first of their kind, the Abyss itself seems eager to spawn more and more of these _[[items/Weapon Magic Abilities/Deadly|deadly]]_ demons.

Though originally created to serve as living weapons of war, the vavakias have long since established their own presence as Abyssal warlords and conquerors. While some pledge their service to powerful demon lords, most vavakias rule small empires of their own in the Abyss, typically in remote corners infested with jungles, swamps, and other primeval terrains.