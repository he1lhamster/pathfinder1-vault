---
cssclass: [monsters]
title1: Demon Lord, Deskari
desc_short: Larger than an elephant, this towering insectile nightmare wields a scythe
  made of bone. Its wings are swarms of biting flies, and its inhuman eyes glitter
  with cruel intelligence.
title2: Deskari
CR: 29
sources:
- name: 'Pathfinder #78: City of Locusts'
  page: 88
  link: http://paizo.com/products/btpy93qo?Pathfinder-Adventure-Path-78-City-of-Locusts
XP: 6553600
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- demon
- earth
- evil
- extraplanar
initiative:
  bonus: 14
senses:
  darkvision: 60
  detect good: true
  detect law: true
  swarmsight: true
  true seeing: true
auras:
- name: frightful presence
  radius: 180
  DC: 36
- name: unholy aura
  DC: 28
AC:
  AC: 47
  touch: 32
  flat_footed: 37
  components:
    deflection: 4
    dex: 10
    natural: 15
    profane: 12
    size: -4
HP:
  HP: 742
  long: 33d10+561
  regeneration: 30
  regeneration_weakness: epic and good or deific
saves:
  fort: 31
  ref: 32
  will: 32
defensive_abilities:
- Abyssal resurrection
- all-around vision
- freedom of movement
- rasping armor
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage and drain
- charm and compulsion effects
- death effects
- electricity
- energy drain
- petrification
- poison
resistances:
  acid: 30
  cold: 30
  fire: 30
SR: 40
speeds:
  base: 60
  climb: 60
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: Riftcarver +51/+46/+41/+36 (4d6+30/19-20/×4 plus poison)
      entries:
      - - damage: 4d6+30
          crit_range: 19-20
          crit_multiplier: 4
        - effect: poison
      attack: Riftcarver
      bonus:
      - 51
      - 46
      - 41
      - 36
    - text: bite +41 (2d8+8 plus poison)
      entries:
      - - damage: 2d8+8
        - effect: poison
      attack: bite
      bonus:
      - 41
    - text: sting +41 (2d6+8 plus poison)
      entries:
      - - damage: 2d6+8
        - effect: poison
      attack: sting
      bonus:
      - 41
  special:
  - breath weapon
  - enhanced venom
  - infestation
  - poison
  - swarm master
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 28
  - name: astral projection
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: At will
    DC: 27
  - name: control winds
    source: default
    freq: At will
  - name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - superscripts:
    - APG
    name: hungry pit
    source: default
    freq: At will
    DC: 25
  - name: insect plague
    source: default
    freq: At will
  - name: shapechange
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 25
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 24
  - name: control weather
    source: default
    freq: 3/day
  - name: creeping doom
    source: default
    freq: 3/day
  - name: reverse gravity
    source: default
    freq: 3/day
  - name: summon demons
    source: default
    freq: 3/day
  - name: symbol of weakness
    source: default
    freq: 3/day
    DC: 27
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 29
  - name: earthquake
    source: default
    freq: 1/day
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 29
    concentration: 39
ability_scores:
  STR: 44
  DEX: 30
  CON: 42
  INT: 29
  WIS: 31
  CHA: 31
BAB: 33
CMB: 54
CMB_other: +56 bull rush, +58 sunder
CMD: 92
CMD_other: 94 vs. bull rush, 94 vs. sunder, 100 vs. trip
feats:
- name: Awesome Blow
- name: Combat Expertise
- name: Combat Reflexes
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Flyby Attack
- name: Greater Sunder
- name: Hover
- name: Improved Bull Rush
- name: Improved Critical (scythe)
- name: Improved Initiative
- name: Improved Sunder
- name: Power Attack
- name: Staggering Critical
- name: Toughness
skills:
  Acrobatics: 46
    when jumping: 58
  Bluff: 46
  Climb: 74
  Disable Device: 46
  Fly: 44
  Intimidate: 43
  Knowledge (arcana): 42
  Knowledge (dungeoneering): 42
  Knowledge (engineering): 42
  Knowledge (planes): 42
  Perception: 54
  Sense Motive: 46
  Spellcraft: 45
  Stealth: 34
  Use Magic Device: 46
  _racial_mods:
    Climb:
      _: 16
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Terran
- Undercommon
- telepathy 300 ft.
special_qualities:
- wall crawler
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - Riftcarver
  - other treasure
special_abilities:
  Breath Weapon (Su): Once every 1d4 rounds as a swift action, Deskari can spit out
    a line of noxious black slime in a 120- foot line that creates a 20-foot-radius-spread
    puddle of the stuff on the ground where the line terminates. Any creature caught
    in this area of effect takes 20d10 points of acid damage and is subject to the
    effects of Deskari's poison. A successful DC 42 Reflex save halves the damage,
    but does not mitigate the poison's effects. The line and puddle created by this
    attack remain as active acid on the ground for 1d4 rounds, affecting any creatures
    that move through an affected area. Damage caused by this breath weapon does not
    persist into additional rounds, but on the round a creature takes this damage,
    it is considered to be taking continuous damage for the purposes of spellcasting
    and concentration checks. The save DC is Constitution-based.
  Enhanced Venom (Su): Any poisons created by Deskari (or even those used by him)
    become enhanced, and can affect creatures normally immune to poison. If an affected
    creature is mythic and is normally immune to poison, it instead receives a +4
    bonus on its saving throw against Deskari's poison effects.
  Infestation (Su): Whenever a creature becomes poisoned by Deskari, it also becomes
    infested with thousands of microscopic demonic eggs that quickly multiply and
    spread throughout the victim's bloodstream and flesh alike. Once infested, a creature
    remains infested even after the poison's effects end or are cured. A creature
    that has been infested by Deskari is recognized by all mindless swarms as a host,
    and such swarms never deal damage to the creature unless influenced and compelled
    to do so by an outside influence. An infested creature takes a -4 penalty on all
    saving throws made against Deskari's attacks or spells cast by his clerics. As
    a swift action, Deskari may command a creature's infestation to accelerate; this
    deals 20d6 points of damage and stuns the target for 1 round (a successful DC
    42 Fortitude save halves the damage and negates the stun effect) as the eggs hatch
    and a fiendish locust swarm (Pathfinder RPG Bestiary 4 183) bursts out of the
    creature's body (ending the infestation). Infestation is a disease effect, and
    the save DC is Constitution-based.
  Poison (Ex): Bite, breath weapon, sting, or Riftcarver-injury; save Fort DC 42;
    frequency 1/round for 6 rounds; effect 1d4 Constitution drain plus infestation;
    cure 3 consecutive saves. The save DC is Constitution-based.
  Rasping Armor (Su): The armor plates that protect Deskari's body rasp together whenever
    he is damaged by a physical attack, creating a discordant shrieking and grinding
    sound. Every time a creature strikes Deskari with an attack that deals bludgeoning,
    force, piercing, or slashing damage, all creatures within 10 feet of Deskari must
    succeed at a DC 42 Fortitude save or be sickened for 1d6 rounds. A sickened creature
    that fails this save becomes staggered for 1 round. A staggered creature that
    fails this save becomes nauseated for 1 round. Finally, a nauseated creature that
    fails this save becomes stunned for 1d6 rounds. This is a mind-affecting sonic
    effect that does not affect demons. The save DC is Constitution-based.
  Swarm Master (Su): Deskari is immune to swarm damage and other swarm effects (such
    as distraction). As a swift action, he can direct the movement of any swarm within
    30 feet. An intelligent swarm can resist this compulsion by succeeding at a DC
    36 Will save. Any swarm created by or conjured by Deskari deals +3d6 points of
    swarm damage, and the damage caused by such a swarm is treated as chaotic, epic,
    and evil for the purpose of overcoming damage reduction. The save DC is Charisma-based.
  Swarmsight (Su): Deskari can see through the eyes of any swarm he commands or controls,
    including the swarm of biting flies that makes up his wings (this swarm, incidentally,
    grants him all-around vision).
  Wall Crawler (Su): Deskari can climb any vertical surface with ease and never has
    to attempt Climb checks to avoid falling as a result of taking damage. This grants
    him a +16 racial bonus on Climb checks.
desc_long: |-
  Known as the Lord of the Locust Host and the Usher of the Apocalypse, Deskari has long plagued the region of Sarkoris, ever since he discovered a strange thinness between that nation and his own Abyssal realm. His first attempt to capitalize upon this strange feature ended with his defeat at Aroden's hands, but after the god's death at the outset of the Age of Lost Omens, Deskari and his cult wasted no time in opening the Worldwound to allow the demon lord's plans for Golarion to continue.

  Deskari carved his realm from the raw matter of the Abyss using a great scythe called Riftcarver (see page 63), a weapon he crafted from the remains of the strange creature his father, Pazuzu, mated with tens of thousands of years ago. Today, Pazuzu and Deskari have what passes as a cordial relationship-the two demon lords do not work together, but neither do they oppose each other's goals on the Material Plane and beyond.

---

# Demon Lord, Deskari
Larger than an _[[monsters/Elephant|elephant]]_, this towering insectile _[[spells/Nightmare|nightmare]]_ wields a _[[items/Weapon/Scythe|scythe]]_ made of bone. Its wings are swarms of biting flies, and its inhuman eyes glitter with _[[items/Weapon Magic Abilities/Cruel|cruel]]_ intelligence.
**Source** Pathfinder #78: City of Locusts pg. 88
**XP** 6,553,600
CE Gargantuan outsider (chaotic, demon, earth, evil, extraplanar)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, swarmsight, _[[spells/True Seeing|true seeing]]_; Perception +54
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 36), _[[spells/Unholy Aura|unholy aura]]_ (DC 28)

##### Defense

**AC** 47, touch 32, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+4 deflection, +10 Dex, +15 natural, +12 profane, –4 size)
**hp** 742 (33d10+561); _[[universal monster rules/Regeneration|regeneration]]_ 30 (epic and good or deific)
**Fort** +31, **Ref** +32, **Will** +32
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Freedom of Movement|freedom of movement]]_, rasping armor; **DR** 20/cold iron, epic, and good; **Immune** _[[universal monster rules/Ability Damage and Drain|ability damage and drain]]_, charm and compulsion effects, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification, poison; **Resist** acid 30, cold 30, fire 30; **SR** 40

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 60 ft., fly 90 ft. (good)
**Melee** _[[items/Weapon/Riftcarver|Riftcarver]]_ +51/+46/+41/+36 (4d6+30/19–20/×4 plus poison), bite +41 (2d8+8 plus poison), sting +41 (2d6+8 plus poison)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, enhanced venom, infestation, poison, swarm master
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +39)
Constant—_detect good_, _detect law_, _freedom of movement_, _true seeing_, _unholy aura_ (DC 28)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_ (DC 27), _[[spells/Control Winds|control winds]]_, _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Hungry Pit|hungry pit]]_ (DC 25), _[[spells/Insect Plague|insect plague]]_, _[[spells/Shapechange|shapechange]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 25), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 24)
3/day—_[[spells/Control Weather|control weather]]_, _[[spells/Creeping Doom|creeping doom]]_, _[[spells/Reverse Gravity|reverse gravity]]_, _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol Of Weakness|symbol of weakness]]_ (DC 27)
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 29), _[[spells/Earthquake|earthquake]]_, _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 44, **Dex** 30, **Con** 42, **Int** 29, **Wis** 31, **Cha** 31
**Base Atk** +33; **CMB** +54 (+56 bull rush, +58 sunder); **CMD** 92 (94 vs. bull rush, 94 vs. sunder, 100 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +46 (+58 when jumping), Bluff +46, _Climb_ +74, Disable Device +46, Fly +44, Intimidate +43, Knowledge (arcana, dungeoneering, engineering, planes) +42, Perception +54, Sense Motive +46, Spellcraft +45, Stealth +34, Use Magic Device +46; **Racial Modifiers** +16 _Climb_, +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic, Terran, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** wall crawler

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple (_Riftcarver_, other treasure)

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds as a swift action, Deskari can spit out a line of noxious black slime in a 120- foot line that creates a 20-foot-radius-spread puddle of the stuff on the ground where the line terminates. Any creature caught in this area of effect takes 20d10 points of acid damage and is subject to the effects of Deskari’s poison. A successful DC 42 Reflex save halves the damage, but does not mitigate the poison’s effects. The line and puddle created by this attack remain as active acid on the ground for 1d4 rounds, affecting any creatures that move through an affected area. Damage caused by this _breath weapon_ does not persist into additional rounds, but on the round a creature takes this damage, it is considered to be taking continuous damage for the purposes of spellcasting and concentration checks. The save DC is Constitution-based.

**Enhanced Venom (Su)** Any poisons created by Deskari (or even those used by him) become enhanced, and can affect creatures normally immune to poison. If an affected creature is mythic and is normally immune to poison, it instead receives a +4 bonus on its saving throw against Deskari’s poison effects.

**Infestation (Su)** Whenever a creature becomes poisoned by Deskari, it also becomes infested with thousands of microscopic demonic eggs that quickly multiply and spread throughout the victim’s bloodstream and flesh alike. Once infested, a creature remains infested even after the poison’s effects end or are cured. A creature that has been infested by Deskari is recognized by all mindless swarms as a host, and such swarms never deal damage to the creature unless influenced and compelled to do so by an outside influence. An infested creature takes a –4 penalty on all saving throws made against Deskari’s attacks or spells cast by his clerics. As a swift action, Deskari may _[[spells/Command|command]]_ a creature’s infestation to accelerate; this deals 20d6 points of damage and stuns the target for 1 round (a successful DC 42 Fortitude save halves the damage and negates the stun effect) as the eggs hatch and a fiendish locust swarm (Pathfinder RPG Bestiary 4 183) bursts out of the creature’s body (ending the infestation). Infestation is a disease effect, and the save DC is Constitution-based.

**Poison (Ex)** Bite, _breath weapon_, sting, or _Riftcarver_—injury; save Fort DC 42; frequency 1/round for 6 rounds; effect 1d4 Constitution drain plus infestation; cure 3 consecutive saves. The save DC is Constitution-based.

**Rasping Armor (Su)** The armor plates that protect Deskari’s body rasp together whenever he is damaged by a physical attack, creating a discordant shrieking and _[[items/Armor Magic Abilities/Grinding|grinding]]_ sound. Every time a creature strikes Deskari with an attack that deals bludgeoning, force, piercing, or slashing damage, all creatures within 10 feet of Deskari must succeed at a DC 42 Fortitude save or be _[[conditions/Sickened|sickened]]_ for 1d6 rounds. A _sickened_ creature that fails this save becomes _[[conditions/Staggered|staggered]]_ for 1 round. A _staggered_ creature that fails this save becomes _[[conditions/Nauseated|nauseated]]_ for 1 round. Finally, a _nauseated_ creature that fails this save becomes _[[conditions/Stunned|stunned]]_ for 1d6 rounds. This is a mind-affecting sonic effect that does not affect demons. The save DC is Constitution-based.
**Swarm Master (Su)** Deskari is immune to swarm damage and other swarm effects (such as _[[universal monster rules/Distraction|distraction]]_). As a swift action, he can direct the movement of any swarm within 30 feet. An intelligent swarm can resist this compulsion by succeeding at a DC 36 Will save. Any swarm created by or conjured by Deskari deals +3d6 points of swarm damage, and the damage caused by such a swarm is treated as chaotic, epic, and evil for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. The save DC is Charisma-based.
**Swarmsight (Su)** Deskari can see through the eyes of any swarm he commands or controls, including the swarm of biting flies that makes up his wings (this swarm, incidentally, grants him _all-around vision_).

**Wall Crawler (Su)** Deskari can _climb_ any vertical surface with ease and never has to attempt _Climb_ checks to avoid falling as a result of taking damage. This grants him a +16 racial bonus on _Climb_ checks.

##### Description

Known as the Lord of the Locust Host and the Usher of the Apocalypse, Deskari has long plagued the region of Sarkoris, ever since he discovered a strange thinness between that nation and his own Abyssal realm. His first attempt to capitalize upon this strange feature ended with his defeat at Aroden’s hands, but after the god’s death at the outset of the Age of Lost Omens, Deskari and his cult wasted no time in opening the Worldwound to allow the demon lord’s plans for Golarion to continue.

Deskari carved his realm from the raw matter of the Abyss using a great _scythe_ _[[items/Weapon Magic Abilities/Called|called]]_ _Riftcarver_ (see page 63), a weapon he crafted from the remains of the strange creature his father, Pazuzu, mated with tens of thousands of years ago. Today, Pazuzu and Deskari have what passes as a cordial relationship—the two demon lords do not work together, but neither do they oppose each other’s goals on the Material Plane and beyond.