---
cssclass: [monsters]
title1: Great Old One, Ghatanothoa
desc_short: An insane tangle of eyes and mouths, arms and legs, tentacles and worse
  rises up upon itself, a mountain of madness come to life.
title2: Ghatanothoa
CR: 29
sources:
- name: 'Pathfinder #114: Black Stars Beckon'
  page: 84
  link: http://paizo.com/products/btpy9qcm?Pathfinder-Adventure-Path-114-Black-Stars-Beckon
XP: 6553600
alignment: NE
size: Colossal
type: aberration
subtypes:
- chaotic
- evil
- Great Old One
initiative:
  bonus: 25
senses:
  blindsight: 60
  darkvision: 60
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 39
AC:
  AC: 47
  touch: 24
  flat_footed: 35
  components:
    dex: 11
    dodge: 1
    insight: 10
    natural: 23
    size: -8
HP:
  HP: 717
  long: 35d8+560
  fast_healing: 25
saves:
  fort: 29
  ref: 24
  will: 30
defensive_abilities:
- all-around vision
- amorphous
- freedom of movement
- immortality
- insanity (DC 37)
DR:
- amount: 15
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- electricity
- energy drain
- mind-affecting effects
- negative energy
- paralysis
- petrification
resistances:
  fire: 30
SR: 40
speeds:
  base: 90
  other_semicolon: air walk
  swim: 90
attacks:
  melee:
  - - text: 3 bites +40 (4d6+21/19-20 plus grab)
      entries:
      - - damage: 4d6+21
          crit_range: 19-20
        - effect: grab
      count: 3
      attack: bites
      bonus:
      - 40
    - text: 6 tentacles +38 (2d8+10/19-20 plus grab)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
        - effect: grab
      count: 6
      attack: tentacles
      bonus:
      - 38
  special:
  - apocalyptic dreams
  - constrict (2d8+31)
  - create mummified creature
  - fast swallow
  - mythic power (10/day, surge +1d12)
  - overwhelming devastation
  - pounce
  - swallow whole (10d6+31 bludgeoning plus 10d6 negative energy damage, AC 21, 71
    hp)
space: 30
reach: 30
reach_other: 60 ft. with tentacles
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - is_mythic_spell: true
    name: black tentacles
    source: default
    freq: At will
  - is_mythic_spell: true
    name: control weather
    source: default
    freq: At will
  - name: create undead
    source: default
    freq: At will
    other: mummies only
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 27
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 25
  - name: project image
    source: default
    freq: At will
    DC: 27
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
    DC: 28
  - name: earthquake
    source: default
    freq: 3/day
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 25
  - name: vortex
    source: default
    freq: 3/day
    DC: 27
  - name: weird
    source: default
    freq: 3/day
    DC: 29
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 29
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 29
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 28
  - is_mythic_spell: true
    name: tsunami
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 29
    concentration: 39
ability_scores:
  STR: 52
  DEX: 33
  CON: 43
  INT: 29
  WIS: 32
  CHA: 30
BAB: 26
CMB: 55
CMB_other: +57 bull rush, +57 sunder
CMD: 87
CMD_other: 89 vs. bull rush, 89 vs. sunder, can't be tripped
feats:
- name: Ability Focus (unspeakable presence)
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Great Fortitude
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (tentacle)
- name: Improved Initiative
- name: Improved Sunder
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Staggering Critical
- name: Weapon Focus (bite)
- name: Weapon Focus (tentacle)
skills:
  Climb: 59
  Intimidate: 48
  Knowledge (arcana): 47
  Knowledge (dungeoneering): 44
  Knowledge (geography): 44
  Knowledge (nature): 44
  Knowledge (planes): 44
  Knowledge (religion): 44
  Perception: 49
  Sense Motive: 46
  Spellcraft: 47
  Swim: 67
  Use Magic Device: 45
languages:
- Aklo
- Aquan
- Undercommon
- telepathy 300 ft.
special_qualities:
- compression
- Great Old One traits
- otherworldly insight
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Apocalyptic Dreams (Su): Ghatanothoa can affect a creature with apocalyptic dreams
    if it has been subjected to his unspeakable presence (even if the creature successfully
    saved against that effect), has been harmed by a natural disaster created by a
    magical effect (such as an earthquake, storm of vengeance, or tsunami spell),
    or has ever offered a prayer to Ghatanothoa. When Ghatanothoa uses his nightmare
    spell-like ability on such a target, the victim has a vivid dream of experiencing
    the end of the world in a fiery, destructive apocalypse-be it from asteroid impact,
    devastating floods, volcanic eruption, or anything else at the GM's whim. Upon
    waking, the conviction that such an apocalypse is only days, if not hours, away
    haunts the victim. In addition to suffering the normal effects of the nightmare,
    the victim must succeed at a DC 37 Will saving throw or be staggered with hopelessness
    for 24 hours. This is a mind-affecting effect. The save DC is Charisma-based.
  Create Mummified Creature (Su): Any creature slain by Ghatanothoa's swallow whole
    attack is immediately transformed into a mummified creature (Pathfinder RPG Bestiary
    4 196) under Ghatanothoa's control. As a free action, Ghatanothoa can disgorge
    any number of swallowed mummified creatures into adjacent squares. As a swift
    action, Ghatanothoa may make a touch attack against a creature that has mummified
    fully as a result of his unspeakable presence to transform that creature into
    a mummified creature under his control (no save).
  Great Old One Traits: Full rules for Ghatanothoa's immortality, insanity, his mythic
    abilities, and otherworldly insight, as well as the base rules for his unspeakable
    presence, can be found on page 306 of Pathfinder RPG Bestiary 4.
  Immortality (Ex): If Ghatanothoa is killed, his form and all perfect images of his
    likeness lose their unspeakable presence ability (see page 85). Ghatanothoa's
    body shrivels and compresses in on itself, growing hard and leathery as it mummifies
    and contracts in size to a Huge object with AC 24, hardness 30, and 200 hit points.
    These remains are immune to cold damage, take half damage from fire and electricity,
    and take 150% damage from acid. An earthquake manifests (as per the spell at CL
    29th) each round thereafter, centered on the location where Ghatanothoa was slain
    (his remains never take damage from the effects of these earthquakes). If Ghatanothoa's
    remains are not destroyed within 1 minute of his death, the remains explode in
    a blast of negative energy with a 600-foot radius that deals 20d6 points of negative
    energy damage to all creatures within that area (Reflex DC 43 half). A creature
    killed by this damage is immediately transformed into a mummified creature (Pathfinder
    RPG Bestiary 4 196). If the remains are destroyed before this occurs, they crumble
    to dust without exploding. In either case, as soon as the remains are destroyed
    or explode, the earthquake effect in the region ends. Once this occurs, Ghatanothoa
    is reborn from one of the hidden cysts deep within his island lair. If his remains
    were destroyed before they could explode, he stays dormant in his lair until outside
    influences awake him once again (this could be a complex ritual performed by cultists,
    an astronomical event, or any natural disaster that strikes the region). If his
    remains were allowed to explode, Ghatanothoa wakes immediately and his unspeakable
    presence ability once again functions as detailed below. The save DC is Constitution-based.
  Overwhelming Devastation (Ex): As a standard action, Ghatanothoa can assault a structure,
    dealing 10d6+31 points of damage to the structure in that round. This damage bypasses
    all hardness the structure has.
  Unspeakable Presence (Su): |-
    Any creature failing a DC 39 Will save against Ghatanothoa's unspeakable presence becomes afflicted with a horrific curse. Ghatanothoa's unspeakable presence is so potent that even perfect images of the Great Old One can have this effect-a “perfect image” can either be a projected image created by Ghatanothoa, a perfectly rendered statue or painting (this requires an expenditure of 100,000 gp in resources, a successful DC 50 Craft [painting or sculpture] check, and a wish by someone who has suffered from Ghatanothoa's unspeakable presence), or any other representation at the GM's whim. Fortunately, the saving throw to resist this effect from a “perfect image” is only DC 20 (DC = 10 + Ghatanothoa's Charisma modifier).

     If a creature fails to resist this curse, it immediately takes 1d10 points of Dexterity drain per round as its body begins to swiftly mummify. If the creature averts its gaze from Ghatanothoa, this drain is reduced to 1 point per round. As soon as a creature's Dexterity score is drained to 0, it transforms into a perfectly preserved and completely immobile mummy, yet the victim does not die. A creature mummified in this way no longer needs to eat, drink, or breathe, and no longer ages. It is essentially immortal, and can observe the world around it (and may even take purely mental actions, including the use of psychic magic), but can take no other actions. No magical effect can end this condition (even if the victim's Dexterity drain is healed) save for an effect that removes the curse. This is a curse effect. The save DC is Charisma-based.
desc_long: Ghatanothoa is a horrific monstrosity who, fortunately, is imprisoned on
  an island on a distant world. Yet even an image of this Great Old One has the potential
  to wreak havoc and destroy lives. Ghatanothoa's form is singularly repulsive-a tangle
  of arms, legs, eyes, mouths, and other body parts capable of shifting its composition
  at a whim, yet always retaining a definite and abhorrent shape.

---

# Great Old One, Ghatanothoa
An insane tangle of eyes and mouths, arms and legs, tentacles and worse rises up upon itself, a mountain of madness come to life.
**Source** Pathfinder #114: Black Stars Beckon pg. 84
**XP** 6,553,600

NE Colossal aberration (chaotic, evil, Great Old One)
**Init** +25; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +49
**Aura** unspeakable presence (300 ft., DC 39)

##### Defense

**AC** 47, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+11 Dex, +1 dodge, +10 insight, +23 natural, –8 size)
**hp** 717 (35d8+560); _[[universal monster rules/Fast Healing|fast healing]]_ 25
**Fort** +29, **Ref** +24, **Will** +30
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Amorphous|amorphous]]_, _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 37); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, negative energy, _[[universal monster rules/Paralysis|paralysis]]_, and petrification; **Resist** fire 30; **SR** 40

##### Offense
**Speed** 90 ft., swim 90 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 3 bites +40 (4d6+21/19–20 plus _[[universal monster rules/Grab|grab]]_), 6 tentacles +38 (2d8+10/19–20 plus _grab_)
**Space** 30 ft., **Reach** 30 ft. (60 ft. with tentacles)
**Special Attacks** apocalyptic dreams, _[[universal monster rules/Constrict|constrict]]_ (2d8+31), create mummified creature, _[[universal monster rules/Fast Swallow|fast swallow]]_, mythic power (10/day, surge +1d12), overwhelming devastation, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Swallow Whole|swallow whole]]_ (10d6+31 bludgeoning plus 10d6 negative energy damage, AC 21, 71 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +39)
Constant—_air walk_, _freedom of movement_, _true seeing_
At will—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Create Undead|create undead]]_ (mummies only), _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _insanity_ (DC 27), _[[spells/Nightmare|nightmare]]_ (DC 25), _[[spells/Project Image|project image]]_ (DC 27), _[[spells/Sending|sending]]_
3/day—_[[spells/Demand|demand]]_ (DC 28), _[[spells/Earthquake|earthquake]]_, quickened _[[spells/Feeblemind|feeblemind]]_ (DC 25), _[[spells/Vortex|vortex]]_ (DC 27), _[[spells/Weird|weird]]_ (DC 29)
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 29), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 29), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 28), _[[spells/Tsunami|tsunami]]_ (DC 29)

##### Statistics
**Str** 52, **Dex** 33, **Con** 43, **Int** 29, **Wis** 32, **Cha** 30
**Base Atk** +26; **CMB** +55 (+57 bull rush, +57 sunder); **CMD** 87 (89 vs. bull rush, 89 vs. sunder, can’t be tripped)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (unspeakable presence), _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (tentacle), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (tentacle)
**Skills** _[[universal monster rules/Climb|Climb]]_ +59, Intimidate +48, Knowledge (arcana) +47, Knowledge (dungeoneering, geography, nature, planes, religion) +44, Perception +49, Sense Motive +46, Spellcraft +47, Swim +67, Use Magic Device +45
**Languages** Aklo, Aquan, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, Great Old One traits, otherworldly insight

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Apocalyptic Dreams (Su)** Ghatanothoa can affect a creature with apocalyptic dreams if it has been subjected to his unspeakable presence (even if the creature successfully saved against that effect), has been harmed by a natural disaster created by a magical effect (such as an _earthquake_, _storm of vengeance_, or _tsunami_ spell), or has ever offered a _[[spells/Prayer|prayer]]_ to Ghatanothoa. When Ghatanothoa uses his _nightmare_ spell-like ability on such a target, the victim has a vivid _dream_ of experiencing the end of the world in a fiery, destructive apocalypse—be it from asteroid _[[items/Weapon Magic Abilities/Impact|impact]]_, devastating floods, _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ eruption, or anything else at the GM’s whim. Upon waking, the _[[feats/Conviction|conviction]]_ that such an apocalypse is only days, if not hours, away haunts the victim. In addition to suffering the normal effects of the _nightmare_, the victim must succeed at a DC 37 Will saving throw or be _[[conditions/Staggered|staggered]]_ with hopelessness for 24 hours. This is a mind-affecting effect. The save DC is Charisma-based.

**Create Mummified Creature (Su)** Any creature slain by Ghatanothoa’s _swallow whole_ attack is immediately transformed into a mummified creature (Pathfinder RPG Bestiary 4 196) under Ghatanothoa’s control. As a free action, Ghatanothoa can disgorge any number of swallowed mummified creatures into adjacent squares. As a swift action, Ghatanothoa may make a touch attack against a creature that has mummified fully as a result of his unspeakable presence to transform that creature into a mummified creature under his control (no save).

**Great Old One Traits** Full rules for Ghatanothoa’s immortality, _insanity_, his mythic abilities, and otherworldly insight, as well as the base rules for his unspeakable presence, can be found on page 306 of Pathfinder RPG Bestiary 4.

**Immortality (Ex)** If Ghatanothoa is killed, his form and all perfect images of his likeness lose their unspeakable presence ability (see page 85). Ghatanothoa’s body shrivels and compresses in on itself, _[[items/Weapon Magic Abilities/Growing|growing]]_ hard and leathery as it mummifies and contracts in size to a Huge object with AC 24, hardness 30, and 200 hit points. These remains are immune to cold damage, take half damage from fire and electricity, and take 150% damage from acid. An _earthquake_ manifests (as per the spell at CL 29th) each round thereafter, centered on the location where Ghatanothoa was slain (his remains never take damage from the effects of these earthquakes). If Ghatanothoa’s remains are not destroyed within 1 minute of his death, the remains explode in a blast of negative energy with a 600-foot radius that deals 20d6 points of negative energy damage to all creatures within that area (Reflex DC 43 half). A creature killed by this damage is immediately transformed into a mummified creature (Pathfinder RPG Bestiary 4 196). If the remains are destroyed before this occurs, they crumble to dust without exploding. In either case, as soon as the remains are destroyed or explode, the _earthquake_ effect in the region ends. Once this occurs, Ghatanothoa is reborn from one of the hidden cysts deep within his island lair. If his remains were destroyed before they could explode, he stays dormant in his lair until outside influences awake him once again (this could be a complex ritual performed by cultists, an astronomical event, or any natural disaster that strikes the region). If his remains were allowed to explode, Ghatanothoa wakes immediately and his unspeakable presence ability once again functions as detailed below. The save DC is Constitution-based.

**Overwhelming Devastation (Ex)** As a standard action, Ghatanothoa can assault a structure, dealing 10d6+31 points of damage to the structure in that round. This damage bypasses all hardness the structure has.

**Unspeakable Presence (Su)** Any creature failing a DC 39 Will save against Ghatanothoa’s unspeakable presence becomes afflicted with a horrific curse. Ghatanothoa’s unspeakable presence is so _[[items/Weapon Magic Abilities/Potent|potent]]_ that even perfect images of the Great Old One can have this effect—a “perfect image” can either be a projected image created by Ghatanothoa, a perfectly rendered _[[spells/Statue|statue]]_ or painting (this requires an expenditure of 100,000 gp in resources, a successful DC 50 Craft [painting or sculpture] check, and a _[[spells/Wish|wish]]_ by someone who has suffered from Ghatanothoa’s unspeakable presence), or any other representation at the GM’s whim. Fortunately, the saving throw to resist this effect from a “perfect image” is only DC 20 (DC = 10 + Ghatanothoa’s Charisma modifier).

If a creature fails to resist this curse, it immediately takes 1d10 points of Dexterity drain per round as its body begins to swiftly mummify. If the creature averts its _[[universal monster rules/Gaze|gaze]]_ from Ghatanothoa, this drain is reduced to 1 point per round. As soon as a creature’s Dexterity score is drained to 0, it transforms into a perfectly preserved and completely immobile _[[monsters/Mummy|mummy]]_, yet the victim does not die. A creature mummified in this way no longer needs to eat, drink, or breathe, and no longer ages. It is essentially immortal, and can observe the world around it (and may even take purely mental actions, including the use of _[[universal monster rules/Psychic Magic|psychic magic]]_), but can take no other actions. No magical effect can end this condition (even if the victim’s Dexterity drain is healed) save for an effect that removes the curse. This is a curse effect. The save DC is Charisma-based.

##### Description

Ghatanothoa is a horrific monstrosity who, fortunately, is imprisoned on an island on a distant world. Yet even an image of this Great Old One has the potential to wreak havoc and destroy lives. Ghatanothoa’s form is singularly repulsive—a tangle of arms, legs, eyes, mouths, and other body parts capable of shifting its composition at a whim, yet always retaining a definite and abhorrent shape.