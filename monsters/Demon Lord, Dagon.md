---
cssclass: [monsters]
title1: Demon Lord, Dagon
desc_short: This demon's body is a nightmare of writhing tentacles and slippery coils
  below the leering maw of a deep sea predator.
title2: Dagon
CR: 28
sources:
- name: Bestiary 4
  page: 46
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 4915200
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- water
initiative:
  bonus: 11
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 36
- name: unholy aura
  DC: 28
AC:
  AC: 46
  touch: 31
  flat_footed: 39
  components:
    deflection: 4
    dex: 7
    natural: 15
    profane: 12
    size: -2
HP:
  HP: 676
  long: 33d10+495
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 37
  ref: 24
  will: 33
defensive_abilities:
- Abyssal resurrection
- freedom of movement
DR:
- amount: 20
  weakness: cold iron, epic, and good
immunities:
- ability damage
- ability drain
- charm effects
- compulsion effects
- cold
- death effects
- electricity
- energy drain
- petrification
- poison
resistances:
  acid: 30
  fire: 30
SR: 39
speeds:
  base: 40
  swim: 120
attacks:
  melee:
  - - text: bite +48 (6d6+17/19-20 plus grab)
      entries:
      - - damage: 6d6+17
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 48
    - text: 4 tentacles +43 (2d6+8/19-20 plus grab)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 43
  special:
  - breath weapon
  - command aquatic creature
  - constrict (2d6+25)
  - fast swallow
  - poison
  - swallow whole (transformation, AC 17, 67 hp)
space: 15
reach: 15
reach_other: 30 ft. with tentacle
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
  - name: speak with animals
    source: default
    freq: Constant
    other: aquatic animals only
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
  - name: control water
    source: default
    freq: At will
  - name: control weather
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
  - name: quickened greater dispel magic
    source: default
    freq: 3/day
  - name: insanity
    source: default
    freq: 3/day
    DC: 27
  - name: summon demons
    source: default
    freq: 3/day
  - name: symbol of insanity
    source: default
    freq: 3/day
    DC: 28
  - name: vortex
    source: default
    freq: 3/day
    DC: 27
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 29
  - name: time stop
    source: default
    freq: 1/day
  - name: tsunami
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 28
    concentration: 38
ability_scores:
  STR: 44
  DEX: 25
  CON: 40
  INT: 29
  WIS: 32
  CHA: 31
BAB: 33
CMB: 52
CMB_other: +56 bull rush, +54 disarm, +56 grapple, +54 trip
CMD: 87
CMD_other: 89 vs. bull rush, 89 vs. disarm, can't be tripped
feats:
- name: Awesome Blow
- name: Bleeding Critical
- name: Combat Expertise
- name: Combat Reflexes
- name: Craft Wondrous Item
- name: Critical Focus
- name: Greater Bull Rush
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (tentacle)
- name: Improved Initiative
- name: Improved Trip
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (greater dispel magic)
- name: Vital Strike
skills:
  Acrobatics: 40
    when jumping: 44
  Bluff: 46
  Intimidate: 46
  Knowledge (arcana): 45
  Knowledge (geography): 42
  Knowledge (history): 42
  Knowledge (nature): 45
  Knowledge (planes): 45
  Knowledge (religion): 42
  Perception: 55
  Sense Motive: 47
  Spellcraft: 45
  Stealth: 35
  Swim: 61
  Use Magic Device: 43
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Aquan
- Celestial
- Common
- Draconic
- speak with animals (aquatic animals only)
- telepathy 300 ft.
special_qualities:
- compression
- demon lord traits
ecology:
  environment: any oceans (Abyss)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Breath Weapon (Su): Once every 1d4 rounds as a standard action, Dagon can exhale
    a 60-foot cone of inky blackness. Underwater, this cone manifests as black ink,
    while above water it manifests as a thick cloud. Creatures in the area have their
    vision obscured as if they were in complete darkness. Darkvision does not allow
    someone to see through the ink or smoke, but true seeing does. The ink or smoke
    persists for 1d4 rounds, but dissipates in 1 round in areas with aquatic currents
    or winds. Any creature in the breath weapon's area is exposed to the breath weapon's
    poison (see below) and must succeed at a DC 41 Will save or gain 2 negative levels
    as its memories and knowledge leach away (this is a mind-affecting effect). Any
    creature that enters the ink or cloud, or ends its turn inside it, must succeed
    at another Will save (at a +4 bonus) to avoid further level loss and poisoning.
    The save DC is Constitution-based.
  Command Aquatic Creature (Su): Dagon can command aquatic creatures to do his bidding
    as a move action, either via using his ability to speak with animals or via telepathy.
    This affects all aberrations, animals, magical beasts, oozes, and vermin within
    300 feet that have the aquatic subtype (Will DC 36 negates). This functions like
    mass suggestion, but can affect mindless creatures. Dagon can suggest obviously
    harmful or suicidal acts (though non-mindless creatures gain a +10 bonus on their
    saving throws against these suggestions). The commanded course of activity can
    have a duration of up to 1 hour. If Dagon issues a new command to a creature,
    the previous command is discarded. Once a creature succeeds at its save against
    this effect, it is immune to further commands from Dagon for 24 hours. The save
    DC is Charisma-based.
  Poison (Ex): Breath weapon-contact; save Fort DC 41; frequency 1/round for 6 rounds;
    effect 1d6 Con drain and confused for 1 round; cure 3 consecutive saves.
  Transformation (Su): A creature swallowed by Dagon is assaulted by demonic enzymes,
    rasping talons, sucking tendrils, and vile gases. At the start of the swallowed
    creature's turn, it must succeed at a DC 41 Fortitude save or be nauseated, and
    must succeed at a DC 36 Will save or take 1d6 points of Dexterity and Charisma
    drain. Once the creature's Dexterity and Charisma are drained to 0, the creature
    transforms into a horrifically deformed version of itself that Dagon can then
    disgorge into any adjacent square as a swift action. The transformed creature
    gains the half-fiend template, its Dexterity and Charisma return to their normal
    values, and it is under Dagon's control (as dominate monster, caster level 28th).
    The transformation can be reversed by casting break enchantment and atonement
    on the victim during the first 24 hours (after that, it can be reversed only via
    miracle or wish). The Fortitude save DC is Constitution-based, and the Will save
    DC is Charisma-based.
desc_long: |-
  Dagon is the demon lord of deformity, the sea, and sea monsters. He rules an Abyssal realm that consists of an immense ocean dotted above with strange and horrible islands and marked below with countless deep sea trenches and sunken cities. Dagon is 35 feet long, with the lower body of an eel, a horrif ic visage that evokes images of deep sea predators, and four long tentacles in place of arms.

  Dagon almost always uses Power Attack in combat, taking a -9 penalty on all attack rolls but gaining a +18 bonus on damage rolls. He is never encountered without a large number of aquatic demons or monsters at his side that he uses as pawns in battles, often simply commanding them to attack foes while he hangs back in the shadows and observes the fight with his cold eyes. Immense sharks, hezrous, carnivorous whales, krakens, and shoggoths are the demon lord's favored minions.

  Dagon began life not as a demon lord but as a powerful qlippoth-the reasons for his transformation into a demon lord are not understood by mortal scholars, but there is certainly no love lost between Dagon and the qlippoth race.

---

# Demon Lord, Dagon
This demon’s body is a _[[spells/Nightmare|nightmare]]_ of writhing tentacles and slippery coils below the leering maw of a deep sea predator.
**Source** Bestiary 4 pg. 46
**XP** 4,915,200
CE Huge outsider (chaotic, demon, evil, extraplanar, water)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +55
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 36), _[[spells/Unholy Aura|unholy aura]]_ (DC 28)

##### Defense

**AC** 46, touch 31, _[[conditions/Flat-Footed|flat-footed]]_ 39 (+4 deflection, +7 Dex, +15 natural, +12 profane, –2 size)
**hp** 676 (33d10+495); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +37, **Ref** +24, **Will** +33
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron, epic, and good; **Immune** ability damage, ability drain, charm effects, compulsion effects, cold, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification, and poison; **Resist** acid 30, fire 30; **SR** 39

##### Offense
**Speed** 40 ft., swim 120 ft.
**Melee** bite +48 (6d6+17/19–20 plus _[[universal monster rules/Grab|grab]]_), 4 tentacles +43 (2d6+8/19–20 plus _grab_)
**Space** 15 ft., **Reach** 15 ft. (30 ft. with tentacle)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, _[[spells/Command|command]]_ aquatic creature, _[[universal monster rules/Constrict|constrict]]_ (2d6+25), _[[universal monster rules/Fast Swallow|fast swallow]]_, poison, _[[universal monster rules/Swallow Whole|swallow whole]]_ (_[[spells/Transformation|transformation]]_, AC 17, 67 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 28th; concentration +38)
Constant—_detect good_, _detect law_, _freedom of movement_, _[[spells/Speak with Animals|speak with animals]]_ (aquatic animals only), _true seeing_, _unholy aura_ (DC 28)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_* (DC 27), _[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_*, _[[spells/Desecrate|desecrate]]_*, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Shapechange|shapechange]]_, _[[spells/Telekinesis|telekinesis]]_* (DC 25), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_* (DC 24)
3/day—quickened greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Insanity|insanity]]_ (DC 27), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 28), _[[spells/Vortex|vortex]]_ (DC 27)
1/day—_[[spells/Storm Of Vengeance|storm of vengeance]]_* (DC 29), _[[spells/Time Stop|time stop]]_*, _[[spells/Tsunami|tsunami]]_* (DC 29)
* Dagon can use the mythic version of this ability in his realm.

##### Statistics
**Str** 44, **Dex** 25, **Con** 40, **Int** 29, **Wis** 32, **Cha** 31
**Base Atk** +33; **CMB** +52 (+56 bull rush, +54 disarm, +56 grapple, +54 _[[universal monster rules/Trip|trip]]_); **CMD** 87 (89 vs. bull rush, 89 vs. disarm, can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (tentacle), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (greater _dispel magic_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +40 (+44 when jumping), Bluff +46, Intimidate +46, Knowledge (arcana) +45, Knowledge (geography) +42, Knowledge (history) +42, Knowledge (nature) +45, Knowledge (planes) +45, Knowledge (religion) +42, Perception +55, Sense Motive +47, Spellcraft +45, Stealth +35, Swim +61, Use Magic Device +43; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Aquan, Celestial, Common, Draconic; _speak with animals_ (aquatic animals only), _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, demon lord traits

##### Ecology

**Environment** any oceans (Abyss)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds as a standard action, Dagon can exhale a 60-foot cone of inky blackness. _[[items/Weapon Magic Abilities/Underwater|Underwater]]_, this cone manifests as black _[[items/Mundane/Ink|ink]]_, while above water it manifests as a thick cloud. Creatures in the area have their _[[spells/Vision|vision]]_ obscured as if they were in complete _[[spells/Darkness|darkness]]_. _Darkvision_ does not allow someone to see through the _ink_ or smoke, but _true seeing_ does. The _ink_ or smoke persists for 1d4 rounds, but dissipates in 1 round in areas with aquatic currents or winds. Any creature in the _breath weapon_’s area is exposed to the _breath weapon_’s poison (see below) and must succeed at a DC 41 Will save or gain 2 negative levels as its memories and knowledge leach away (this is a mind-affecting effect). Any creature that enters the _ink_ or cloud, or ends its turn inside it, must succeed at another Will save (at a +4 bonus) to avoid further level loss and _[[items/Armor Magic Abilities/Poisoning|poisoning]]_. The save DC is Constitution-based.

**_Command_ Aquatic Creature (Su)** Dagon can _command_ aquatic creatures to do his bidding as a move action, either via using his ability to _speak with animals_ or via _telepathy_. This affects all aberrations, animals, magical beasts, oozes, and vermin within 300 feet that have the aquatic subtype (Will DC 36 negates). This functions like mass _[[spells/Suggestion|suggestion]]_, but can affect mindless creatures. Dagon can suggest obviously harmful or suicidal acts (though non-mindless creatures gain a +10 bonus on their saving throws against these suggestions). The commanded course of activity can have a duration of up to 1 hour. If Dagon issues a new _command_ to a creature, the previous _command_ is discarded. Once a creature succeeds at its save against this effect, it is immune to further commands from Dagon for 24 hours. The save DC is Charisma-based.

**Poison (Ex) **_Breath weapon_—contact; save Fort DC 41; frequency 1/round for 6 rounds; effect 1d6 Con drain and _[[conditions/Confused|confused]]_ for 1 round; cure 3 consecutive saves.

**_Transformation_ (Su)** A creature swallowed by Dagon is assaulted by demonic enzymes, rasping talons, sucking tendrils, and vile gases. At the start of the swallowed creature’s turn, it must succeed at a DC 41 Fortitude save or be _[[conditions/Nauseated|nauseated]]_, and must succeed at a DC 36 Will save or take 1d6 points of Dexterity and Charisma drain. Once the creature’s Dexterity and Charisma are drained to 0, the creature transforms into a horrifically deformed version of itself that Dagon can then disgorge into any adjacent square as a swift action. The transformed creature gains the half-fiend template, its Dexterity and Charisma return to their normal values, and it is under Dagon’s control (as _[[spells/Dominate Monster|dominate monster]]_, caster level 28th). The _transformation_ can be reversed by casting _[[spells/Break Enchantment|break enchantment]]_ and _[[spells/Atonement|atonement]]_ on the victim during the first 24 hours (after that, it can be reversed only via _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_). The Fortitude save DC is Constitution-based, and the Will save DC is Charisma-based.

##### Description

Dagon is the demon lord of deformity, the sea, and sea monsters. He rules an Abyssal realm that consists of an immense ocean dotted above with strange and horrible islands and marked below with countless deep sea trenches and sunken cities. Dagon is 35 feet long, with the lower body of an eel, a horrif ic visage that evokes images of deep sea predators, and four long tentacles in place of arms.

Dagon almost always uses _Power Attack_ in combat, taking a –9 penalty on all attack rolls but gaining a +18 bonus on damage rolls. He is never encountered without a large number of aquatic demons or monsters at his side that he uses as pawns in battles, often simply commanding them to attack foes while he hangs back in the shadows and observes the fight with his cold eyes. Immense sharks, hezrous, carnivorous whales, krakens, and shoggoths are the demon lord’s favored minions.

Dagon began life not as a demon lord but as a powerful qlippoth—the reasons for his _transformation_ into a demon lord are not understood by mortal scholars, but there is certainly no love lost between Dagon and the qlippoth race.