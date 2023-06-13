---
cssclass: [monsters]
title1: Great Old One, Atlach-Nacha
desc_short: The size of a bull elephant, this red-and-black arachnid has a bloated
  body and spindly legs, made all the more horrifying by the all-too-human appearance
  of its baleful visage.
title2: Atlach-Nacha
CR: 28
sources:
- name: 'Pathfinder #112: The Whisper Out of Time'
  page: 84
  link: http://paizo.com/products/btpy9q9o?Pathfinder-Adventure-Path-112-The-Whisper-Out-of-Time
XP: 4915200
alignment: NE
size: Huge
type: aberration
subtypes:
- evil
- Great Old One
initiative:
  bonus: 23
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 35
AC:
  AC: 46
  touch: 32
  flat_footed: 32
  components:
    dex: 13
    dodge: 1
    insight: 10
    natural: 14
    size: -2
HP:
  HP: 688
  long: 32d8+544
  fast_healing: 25
saves:
  fort: 27
  ref: 23
  will: 29
defensive_abilities:
- freedom of movement
- immortality
- insanity (DC 35)
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
- energy drain
- mind-affecting effects
- paralysis
- petrification
- poison
resistances:
  fire: 30
  sonic: 30
SR: 39
speeds:
  base: 80
  climb: 80
attacks:
  melee:
  - - text: bite +39 touch (4d10+25/19-20 plus poison)
      entries:
      - - damage: 4d10+25
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 39
      touch: true
    - text: 4 claws +39 (3d6+25/19-20)
      entries:
      - - damage: 3d6+25
          crit_range: 19-20
      count: 4
      attack: claws
      bonus:
      - 39
  ranged:
  - - text: web +35 touch (special/×3)
      entries:
      - - effect: special
      attack: web
      bonus:
      - 35
      touch: true
  special:
  - critical poisoning
  - dreams of futility
  - feed
  - mythic power (10/day, surge +1d12)
  - penetrating bite
  - poison
  - powerful blows
  - webs (DC 43, 32 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: feather fall
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
  - name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 27
  - name: levitate
    source: default
    freq: At will
  - name: nightmare
    source: default
    freq: At will
    DC: 24
  - name: sending
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 24
  - name: creeping doom
    source: default
    freq: 3/day
  - name: demand
    source: default
    freq: 3/day
    DC: 27
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 24
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 28
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 27
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 28
  sources:
  - name: default
    CL: 28
    concentration: 37
ability_scores:
  STR: 44
  DEX: 36
  CON: 44
  INT: 29
  WIS: 33
  CHA: 28
BAB: 24
CMB: 43
CMB_other: +47 bull rush
CMD: 77
CMD_other: 79 vs. bull rush
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Vital Strike
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Spring Attack
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 48
    when jumping: 88
  Climb: 60
  Intimidate: 44
  Knowledge (arcana): 41
  Knowledge (dungeoneering): 41
  Knowledge (history): 41
  Knowledge (religion): 41
  Perception: 46
  Sense Motive: 43
  Spellcraft: 44
  Stealth: 40
  Survival: 46
  Use Magic Device: 41
  _racial_mods:
    Acrobatics:
      when jumping: 40
languages:
- Aklo
- Undercommon
- telepathy 100 ft.
special_qualities:
- otherworldly leap
- swift construction
ecology:
  environment: any underground
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Critical Poisoning (Su): If Atlach-Nacha confirms a critical hit with its bite,
    it injects its foe with 3 doses of poison (this increases the save DC by 4). A
    foe that is normally immune to poison can be affected by Atlach-Nacha's poison
    in this way, but the victim treats the poisoning as if it had been injected with
    only 1 dose.
  Dreams of Futility (Su): Atlach-Nacha can impose its verminous dreams on any creature
    that has been rendered unconscious at any point in its life as a result of spider
    venom, that has come in contact with the Great Old One's webs, or upon whom Atlach-Nacha
    has fed. When Atlach-Nacha uses nightmare on such a target, the victim must also
    succeed at a DC 35 Will saving throw or become overwhelmed with futility. Whenever
    the victim attempts a skill check, or at the start of each round in combat, the
    victim has a 50% chance to act normally; otherwise, it takes no action. This effect
    persists for 24 hours but can be ended earlier via a successful break enchantment
    spell. This is a mind-affecting effect. The save DC is Charisma-based.
  Feed (Ex): As a standard action, Atlach-Nacha can feed upon a helpless or willing
    living creature by biting it. This deals no hit point damage, but it does cause
    2d6 points of Strength drain and 2d6 points of Dexterity drain. If a creature's
    Strength and Dexterity are drained to 0, any drain that would normally affect
    those ability scores instead affects Constitution-thus, if Atlach-Nacha feeds
    on a creature with Strength and Dexterity scores of 0, the Great Old One drains
    4d6 points of Constitution instead. A successful DC 43 Fortitude save reduces
    the drain to the minimum possible. The save DC is Constitution-based.
  Great Old One Traits: Rules for Atlach-Nacha's Great Old One traits, such as immortality,
    insanity, its mythic abilities, otherworldly insight, and the base rules for unspeakable
    presence, can be found on page 306 of Pathfinder RPG Bestiary 4.
  Immortality (Ex): If Atlach-Nacha is killed, its body splits open and unleashes
    a hideous mass of swarming spiders. Treat this swarm of spiders as a locust plague
    swarm (Pathfinder RPG Bestiary 5 192) save that it has a base speed of 60 feet,
    a climb speed of 60 feet, and no fly speed. If this swarm of spiders is allowed
    to reform after being dispersed by damage (or after 24 hours have passed), the
    spiders fall upon one another in a cannibalistic frenzy, with the last spider
    alive growing and growing until it becomes Atlach-Nacha reborn. If the swarm is
    truly destroyed as a result of devouring a good-aligned minor artifact or holy
    relic, Atlach-Nacha is instead reborn 1d100 months later from one of countless
    hidden eggs in deep underground caverns- but typically not on the same world upon
    which it was most recently defeated.
  Otherworldly Leap (Ex): Atlach-Nacha gains a +20 racial bonus on Acrobatics checks
    made to jump, and this stacks with its bonus to jumping from high speed. It treats
    all jumps as if it had a running start.
  Penetrating Bite (Ex): Atlach-Nacha's bite penetrates all forms of armor. It resolves
    its bite attacks as if they were touch attacks.
  Poison (Ex): Bite-injury; save Fort DC 43; frequency 1/round for 6 rounds; effect
    permanent paralysis plus 1d6 Strength drain; cure 3 consecutive saves. The save
    DC is Constitution-based.
  Powerful Blows (Ex): Atlach-Nacha always modifies the damage from its physical attacks
    with 1-1/2 times its Strength modifier.
  Swift Construction (Ex): Atlach-Nacha can create bridges or walls from its webs
    as a swift action. A web bridge is 15 feet wide and has a maximum length of 200
    feet. A web wall functions as a wall of stone (CL 20th). Atlach-Nacha can use
    its climb speed to move on these webs, but other creatures treat it as sticky
    webbing (see the web universal monster rule on page 305 of Pathfinder RPG Bestiary)
    if they come in contact with it. Atlach-Nacha's web constructions collapse and
    melt into vapor after 1 day has passed, forcing the Great Old One to constantly
    toil to maintain its webs in a futile effort at permanence.
  Unspeakable Presence (Su): Failing a DC 35 Will saving throw against Atlach-Nacha's
    unspeakable presence causes victims to become convinced they are covered with
    swarming spiders and tangled, sticky webbing. This causes victims to become nauseated
    for as long as the Great Old One remains in the area plus an additional 1d6 rounds.
    This is a mind-affecting effect. The save DC is Charisma-based.
  Webs (Ex): Atlach-Nacha can make a ranged attack with its webs as a swift action.
    These webs have a range increment of 200 feet, and it can shoot up to 10 range
    increments.
desc_long: |-
  This strange arachnid Great Old One, known to some as the Void Weaver, is a dualistic entity in many respects. Its gender is fluid, being both and neither male and female. It constantly toils to build, yet its creations are fated to fail. It exists both in the waking world and the realm of dreams. It embodies the alien form of the spider and the recognizable visage of humanity. To Atlach-Nacha, duality exists only to contradict itself.

  Atlach-Nacha is an elephant-sized, red-and-black spider with a monstrously humanoid face, but at times it can appear as a woman with multiple long arms and a spider's lower torso.

---

# Great Old One, Atlach-Nacha
The size of a bull _[[monsters/Elephant|elephant]]_, this red-and-black arachnid has a bloated body and spindly legs, made all the more horrifying by the all-too-human appearance of its baleful visage.
**Source** Pathfinder #112: The Whisper Out of Time pg. 84
**XP** 4,915,200

NE Huge aberration (evil, Great Old One)
**Init** +23; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +46
**Aura** unspeakable presence (300 ft., DC 35)

##### Defense

**AC** 46, touch 32, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+13 Dex, +1 dodge, +10 insight, +14 natural, –2 size)
**hp** 688 (32d8+544); _[[universal monster rules/Fast Healing|fast healing]]_ 25
**Fort** +27, **Ref** +23, **Will** +29
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 35); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, poison; **Resist** fire 30, sonic 30; **SR** 39

##### Offense
**Speed** 80 ft., _[[universal monster rules/Climb|climb]]_ 80 ft.
**Melee** bite +39 touch (4d10+25/19–20 plus poison), 4 claws +39 (3d6+25/19–20)
**Ranged** web +35 touch (special/×3)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** critical _[[items/Armor Magic Abilities/Poisoning|poisoning]]_, dreams of futility, feed, mythic power (10/day, surge +1d12), penetrating bite, poison, powerful blows, webs (DC 43, 32 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 28th; concentration +37)
Constant—_[[spells/Feather Fall|feather fall]]_, _freedom of movement_, _true seeing_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _insanity_ (DC 27), _[[spells/Levitate|levitate]]_, _[[spells/Nightmare|nightmare]]_ (DC 24), _[[spells/Sending|sending]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 24)
3/day—_[[spells/Creeping Doom|creeping doom]]_, _[[spells/Demand|demand]]_ (DC 27), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 24)
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 28), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 27), _[[spells/Dominate Monster|dominate monster]]_ (DC 28)

##### Statistics
**Str** 44, **Dex** 36, **Con** 44, **Int** 29, **Wis** 33, **Cha** 28
**Base Atk** +24; **CMB** +43 (+47 bull rush); **CMD** 77 (79 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +48 (+88 when jumping), _Climb_ +60, Intimidate +44, Knowledge (arcana, dungeoneering, history, religion) +41, Perception +46, Sense Motive +43, Spellcraft +44, Stealth +40, Survival +46, Use Magic Device +41; **Racial Modifiers** +40 Acrobatics when jumping
**Languages** Aklo, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** otherworldly leap, swift construction

##### Ecology

**Environment** any underground
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Critical _Poisoning_ (Su)** If Atlach-Nacha confirms a critical hit with its bite, it injects its foe with 3 doses of poison (this increases the save DC by 4). A foe that is normally immune to poison can be affected by Atlach-Nacha’s poison in this way, but the victim treats the _poisoning_ as if it had been injected with only 1 dose.

**Dreams of Futility (Su)** Atlach-Nacha can impose its verminous dreams on any creature that has been rendered _[[conditions/Unconscious|unconscious]]_ at any point in its life as a result of spider venom, that has come in contact with the Great Old One’s webs, or upon whom Atlach-Nacha has fed. When Atlach-Nacha uses _nightmare_ on such a target, the victim must also succeed at a DC 35 Will saving throw or become overwhelmed with futility. Whenever the victim attempts a skill check, or at the start of each round in combat, the victim has a 50% chance to act normally; otherwise, it takes no action. This effect persists for 24 hours but can be ended earlier via a successful _[[spells/Break Enchantment|break enchantment]]_ spell. This is a mind-affecting effect. The save DC is Charisma-based.

**Feed (Ex)** As a standard action, Atlach-Nacha can feed upon a _[[conditions/Helpless|helpless]]_ or willing living creature by biting it. This deals no hit point damage, but it does cause 2d6 points of Strength drain and 2d6 points of Dexterity drain. If a creature’s Strength and Dexterity are drained to 0, any drain that would normally affect those ability scores instead affects Constitution—thus, if Atlach-Nacha feeds on a creature with Strength and Dexterity scores of 0, the Great Old One drains 4d6 points of Constitution instead. A successful DC 43 Fortitude save reduces the drain to the minimum possible. The save DC is Constitution-based.

**Great Old One Traits** Rules for Atlach-Nacha’s Great Old One traits, such as immortality, _insanity_, its mythic abilities, otherworldly insight, and the base rules for unspeakable presence, can be found on page 306 of Pathfinder RPG Bestiary 4.

**Immortality (Ex)** If Atlach-Nacha is killed, its body splits open and unleashes a hideous mass of swarming spiders. Treat this swarm of spiders as a locust plague swarm (Pathfinder RPG Bestiary 5 192) save that it has a base speed of 60 feet, a _climb_ speed of 60 feet, and no fly speed. If this swarm of spiders is allowed to reform after being dispersed by damage (or after 24 hours have passed), the spiders fall upon one another in a cannibalistic frenzy, with the last spider alive _[[items/Weapon Magic Abilities/Growing|growing]]_ and _growing_ until it becomes Atlach-Nacha reborn. If the swarm is truly destroyed as a result of devouring a good-aligned minor artifact or holy relic, Atlach-Nacha is instead reborn 1d100 months later from one of countless hidden eggs in deep underground caverns— but typically not on the same world upon which it was most recently defeated.

**Otherworldly Leap (Ex)** Atlach-Nacha gains a +20 racial bonus on Acrobatics checks made to _[[spells/Jump|jump]]_, and this stacks with its bonus to jumping from high speed. It treats all jumps as if it had a running start.

**Penetrating Bite (Ex)** Atlach-Nacha’s bite penetrates all forms of armor. It resolves its bite attacks as if they were touch attacks.

**Poison (Ex)** Bite—injury; save Fort DC 43; frequency 1/round for 6 rounds; effect permanent _paralysis_ plus 1d6 Strength drain; cure 3 consecutive saves. The save DC is Constitution-based.

**Powerful Blows (Ex)** Atlach-Nacha always modifies the damage from its physical attacks with 1-1/2 times its Strength modifier.
**Swift Construction (Ex)** Atlach-Nacha can create bridges or walls from its webs as a swift action. A web bridge is 15 feet wide and has a maximum length of 200 feet. A web wall functions as a _[[spells/Wall Of Stone|wall of stone]]_ (CL 20th). Atlach-Nacha can use its _climb_ speed to move on these webs, but other creatures treat it as _[[items/Weapon Magic Abilities/Sticky|sticky]]_ webbing (see the web universal monster rule on page 305 of Pathfinder RPG Bestiary) if they come in contact with it. Atlach-Nacha’s web constructions collapse and melt into vapor after 1 day has passed, forcing the Great Old One to constantly toil to maintain its webs in a futile effort at permanence.

**Unspeakable Presence (Su)** Failing a DC 35 Will saving throw against Atlach-Nacha’s unspeakable presence causes victims to become convinced they are covered with swarming spiders and tangled, _sticky_ webbing. This causes victims to become _[[conditions/Nauseated|nauseated]]_ for as long as the Great Old One remains in the area plus an additional 1d6 rounds. This is a mind-affecting effect. The save DC is Charisma-based.

**Webs (Ex)** Atlach-Nacha can make a ranged attack with its webs as a swift action. These webs have a range increment of 200 feet, and it can shoot up to 10 range increments.

##### Description

This strange arachnid Great Old One, known to some as the Void Weaver, is a dualistic entity in many respects. Its gender is fluid, being both and neither male and female. It constantly toils to build, yet its creations are fated to fail. It exists both in the waking world and the realm of dreams. It embodies the alien form of the spider and the recognizable visage of humanity. To Atlach-Nacha, duality exists only to contradict itself.

Atlach-Nacha is an elephant-sized, red-and-black spider with a monstrously humanoid face, but at times it can appear as a woman with multiple long arms and a spider’s lower torso.