---
cssclass: [monsters]
title1: Great Old One, Mordiggian
desc_short: This massive wormlike creature appears to be made of solid darkness that
  sucks surrounding light into its body to be forever extinguished.
title2: Mordiggian
CR: 30
sources:
- name: 'Pathfinder #110: The Thrushmoor Terror'
  page: 86
  link: http://paizo.com/products/btpy9l3g
XP: 9830400
alignment: CE
size: Gargantuan
type: aberration
subtypes:
- chaotic
- evil
- Great Old One
- incorporeal
initiative:
  bonus: 31
senses:
  all-around vision: true
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 40
AC:
  AC: 47
  touch: 47
  flat_footed: 31
  components:
    deflection: 13
    dex: 15
    dodge: 1
    insight: 12
    size: -4
HP:
  HP: 752
  long: 35d8+595
  fast_healing: 30
saves:
  fort: 28
  ref: 26
  will: 31
defensive_abilities:
- absorb light
- immortality
- incorporeal
- insanity (DC 40)
DR:
- amount: 20
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- acid
- aging
- blindness
- cold
- death effects
- disease
- energy drain
- mind-affecting effects
- paralysis
- petrification
resistances:
  electricity: 30
  fire: 30
SR: 41
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 6 +5 tentacles +43 (5d6+18/19-20 plus grab)
      entries:
      - - damage: 5d6+18
          crit_range: 19-20
        - effect: grab
      count: 6
      attack: +5 tentacles
      bonus:
      - 43
  special:
  - constrict (5d6+13)
  - dreams of darkness
  - engulf (DC 27, 20d6 negative energy and 1d4 negative levels)
  - mythic power (10/day, surge +1d12)
  - tentacles
space: 20
reach: 20
reach_other: 40 ft. with tentacle
spell_like_abilities:
  entries:
  - name: speak with dead
    source: default
    freq: Constant
    DC: 26
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - name: create undead
    source: default
    freq: At will
  - is_mythic_spell: true
    name: death knell
    source: default
    freq: At will
    DC: 25
  - name: deeper darkness
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 28
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
    DC: 31
  - name: quickened deeper darkness
    source: default
    freq: 3/day
  - name: energy drain
    source: default
    freq: 3/day
    DC: 32
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 28
  - name: quickened slay living
    source: default
    freq: 3/day
    DC: 30
  - name: destruction
    source: default
    freq: 1/day
    DC: 30
  - is_mythic_spell: true
    name: power word kill
    source: default
    freq: 1/day
  - name: symbol of death
    source: default
    freq: 1/day
    DC: 31
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 31
  - name: true resurrection
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 43
ability_scores:
  STR:
  DEX: 40
  CON: 44
  INT: 33
  WIS: 34
  CHA: 37
BAB: 26
CMB: 45
CMB_other: +49 disarm
CMD: 81
CMD_other: 83 vs. disarm
feats:
- name: Ability Focus (slay living)
- name: Blinding Critical
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Disarm
- name: Greater Vital Strike
- name: Improved Critical (tentacle)
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Vital Strike
- name: Mobility
- name: Quicken Spell-Like Ability (deeper darkness)
- name: Quicken Spell-Like Ability (feeblemind)
- name: Quicken Spell-Like Ability (slay living)
- name: Vital Strike
- name: Weapon Focus (tentacle)
skills:
  Acrobatics: 53
  Bluff: 48
  Diplomacy: 48
  Fly: 55
  Knowledge (arcana): 46
  Knowledge (geography): 46
  Knowledge (history): 46
  Knowledge (local): 46
  Knowledge (nobility): 46
  Knowledge (religion): 49
  Perception: 50
  Sense Motive: 47
  Spellcraft: 49
  Stealth: 41
  Use Magic Device: 48
languages:
- Aklo
- Necril
- speak with dead
- telepathy 300 ft.
special_qualities:
- no breath
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Absorb Light (Su): Mordiggian's presence causes all light levels within a 100-foot
    spread to be reduced by one category as long as he has at least 1 hit point. Anyone
    who attempts to cast a spell with the light descriptor in this area must succeed
    at a DC 30 caster level check, or the spell is lost as if it had been counterspelled.
  Dreams of Darkness (Ex): Mordiggian can affect a creature that has been restored
    to life by a worshiper of Mordiggian, that has suffered negative energy damage
    while within the walls of a temple devoted to Mordiggian, or that has been in
    the area of effect of Mordiggian's unspeakable presence (whether or not the creature
    was affected by it) with dreams of darkness. When Mordiggian uses his nightmare
    spell-like ability on such a target, the victim endures what seems to be the passage
    of hundreds of years imprisoned in a lightless sarcophagus or coffin. Upon waking,
    the creature takes an additional effect beyond the normal effects of nightmare-it
    must succeed at a DC 40 Fortitude saving throw or contract an accelerated form
    of ghoul fever that inflicts its damage every hour instead of every day. This
    is a death effect. The save DC is Charisma-based.
  Eldritch Insight (Ex): The whispers of all the world's dead echo in Mordiggian's
    mind, and as a result, he adds his Wisdom modifier as an insight bonus to his
    Armor Class and on all Initiative checks. If Mordiggian is on a planet or in a
    dimension where no creature has ever died, this ability does not function.
  Engulf (Su): When Mordiggian engulfs a creature, he inflicts 20d6 points of negative
    energy damage and 1d4 negative levels. A successful DC 44 Reflex saving throw
    halves the negative energy damage, and a DC 44 Fortitude save removes the negative
    levels. The save DCs are both Constitution-based.
  Great Old One Traits: Rules for Mordiggian's Great Old One traits such as immortality,
    insanity, and otherworldly, as well as the rules for his mythic abilities and
    unspeakable presence can be found on page 306 of Pathfinder RPG Bestiary 4.
  Immortality (Ex): If Mordiggian is killed, the shadows that comprise his body lose
    all form and become a 20-foot-diameter roiling blot of churning darkness with
    a 300-foot fly speed and perfect maneuverability. This blot of darkness is incorporeal
    and cannot be harmed, but it cannot enter an area of bright light. The blot can
    sense all undead creatures within a 100-mile radius, and if it finds an undead
    creature, it can attempt to infuse it. An intelligent undead can resist this attack
    with a successful DC 40 Will saving throw; unintelligent undead receive no save.
    Once this blot of darkness infuses an undead creature, it grants the undead creature
    the advanced creature simple template, but 24 hours later, the undead is destroyed,
    releasing a fully-healed Mordiggian back into the world. If Mordiggian cannot
    find a suitable undead host within 24 hours or is trapped by bright light for
    that duration, the blot of darkness fades away, only to manifest immediately on
    another world-perhaps in the distant past, in the distant future, or even in the
    present. The save DC is Charisma-based.
  Tentacles (Su): Mordiggian's tentacles are primary attacks that inflict bludgeoning
    damage. He adds his Charisma modifier to damage done by his tentacles, which also
    gain a +5 enhancement bonus on attack rolls and damage rolls. These tentacles
    are treated as magic epic chaotic weapons for the purpose of overcoming damage
    reduction. If Mordiggian reduces a living creature to fewer than 0 hit points
    with a tentacle or with his constriction damage, he automatically casts death
    knell on the target as a free action.
  Unspeakable Presence (Su): Failing a DC 40 Will saving throw against Mordiggian's
    unspeakable presence causes the victim to become permanently blinded. A creature
    that is killed while blinded by this ability immediately animates as a chaotic
    evil juju zombie (Pathfinder RPG Bestiary 2 291). The save DC is Charisma-based.
desc_long: |-
  Called the Charnel God by his worshipers, Mordiggian is one of the oldest and most powerful of the Great Old Ones. However, his tendency to move back and forth in time whenever he reincarnates makes the tracking of his age largely academic. None can say how long Mordiggian has existed, for as far as one can look back into the past or forward into the future, the presence of his cult can be found if one searches hard enough.

  Mordiggian has no body. He appears as a cloud of mobile, malevolent darkness and shadow that can change its outline and shape at will. He is fond of appearing as an immense graveworm or limbless giant made of darkness, and when he desires a meal, he can form tentacles of solid darkness to pluck up his feast.

  Ghouls, particularly those that dwell in Leng, often venerate Mordiggian with a ferocious zeal. They consider ghoulish worshipers of other deities, particularly of the demon lord Kabriri, to be heretics and work to eradicate such blasphemers whenever they are found. Although worship of Mordiggian has become quite rare on Golarion as other death gods have gained more prominence, his cult is patient and willing to simply wait for the Charnel God's inevitable return to power.

---

# Great Old One, Mordiggian
This massive wormlike creature appears to be made of solid _[[spells/Darkness|darkness]]_ that sucks surrounding light into its body to be forever extinguished.
**Source** Pathfinder #110: The Thrushmoor Terror pg. 86
**XP** 9,830,400
CE Gargantuan aberration (chaotic, evil, Great Old One, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +31; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +50
**Aura** unspeakable presence (300 ft., DC 40)

##### Defense

**AC** 47, touch 47, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+13 deflection, +15 Dex, +1 _[[feats/Dodge|dodge]]_, +12 insight, –4 size)
**hp** 752 (35d8+595); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +28, **Ref** +26, **Will** +31
**Defensive Abilities** absorb light, immortality, _incorporeal_, _[[spells/Insanity|insanity]]_ (DC 40); **DR** 20/epic and lawful; **Immune** ability damage, ability drain, acid, aging, blindness, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, and petrification; **Resist** electricity 30, fire 30; **SR** 41

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** 6 +5 tentacles +43 (5d6+18/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft. (40 ft. with tentacle)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (5d6+13), dreams of _darkness_, _[[universal monster rules/Engulf|engulf]]_ (DC 27, 20d6 negative energy and 1d4 negative levels), mythic power (10/day, surge +1d12), tentacles
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +43)
Constant—_[[spells/Speak with Dead|speak with dead]]_ (DC 26), _true seeing_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Create Undead|create undead]]_, _[[spells/Death Knell|death knell]]_ (DC 25), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Nightmare|nightmare]]_ (DC 28), _[[spells/Sending|sending]]_
3/day—_[[spells/Demand|demand]]_ (DC 31), quickened _deeper darkness_, _energy drain_ (DC 32), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 28), quickened _[[spells/Slay Living|slay living]]_ (DC 30)
1/day—_[[spells/Destruction|destruction]]_ (DC 30), _[[spells/Power Word Kill|power word kill]]_, _[[spells/Symbol of Death|symbol of death]]_ (DC 31), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 31), _[[spells/True Resurrection|true resurrection]]_

##### Statistics
**Str** —, **Dex** 40, **Con** 44, **Int** 33, **Wis** 34, **Cha** 37
**Base Atk** +26; **CMB** +45 (+49 disarm); **CMD** 81 (83 vs. disarm)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_slay living_), _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (tentacle), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_deeper darkness_, _feeblemind_, _slay living_), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (tentacle)
**Skills** Acrobatics +53, Bluff +48, Diplomacy +48, Fly +55, Knowledge (arcana) +46, Knowledge (geography) +46, Knowledge (history) +46, Knowledge (local) +46, Knowledge (nobility) +46, Knowledge (religion) +49, Perception +50, Sense Motive +47, Spellcraft +49, Stealth +41, Use Magic Device +48
**Languages** Aklo, Necril, _speak with dead_; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Absorb Light (Su)** Mordiggian’s presence causes all light levels within a 100-foot spread to be reduced by one category as long as he has at least 1 hit point. Anyone who attempts to cast a spell with the light descriptor in this area must succeed at a DC 30 caster level check, or the spell is lost as if it had been counterspelled.

**Dreams of _Darkness_ (Ex)** Mordiggian can affect a creature that has been restored to life by a worshiper of Mordiggian, that has suffered negative energy damage while within the walls of a temple devoted to Mordiggian, or that has been in the area of effect of Mordiggian’s unspeakable presence (whether or not the creature was affected by it) with dreams of _darkness_. When Mordiggian uses his _nightmare_ spell-like ability on such a target, the victim endures what seems to be the passage of hundreds of years imprisoned in a lightless sarcophagus or coffin. Upon waking, the creature takes an additional effect beyond the normal effects of _nightmare_—it must succeed at a DC 40 Fortitude saving throw or contract an accelerated form of _[[diseases/Ghoul Fever|ghoul fever]]_ that inflicts its damage every hour instead of every day. This is a death effect. The save DC is Charisma-based.

**Eldritch Insight (Ex)** The whispers of all the world’s dead _[[spells/Echo|echo]]_ in Mordiggian’s mind, and as a result, he adds his Wisdom modifier as an insight bonus to his Armor Class and on all Initiative checks. If Mordiggian is on a planet or in a dimension where no creature has ever died, this ability does not function.

**_Engulf_ (Su)** When Mordiggian engulfs a creature, he inflicts 20d6 points of negative energy damage and 1d4 negative levels. A successful DC 44 Reflex saving throw halves the negative energy damage, and a DC 44 Fortitude save removes the negative levels. The save DCs are both Constitution-based.

**Great Old One Traits** Rules for Mordiggian’s Great Old One traits such as immortality, _insanity_, and otherworldly, as well as the rules for his mythic abilities and unspeakable presence can be found on page 306 of Pathfinder RPG Bestiary 4.

**Immortality (Ex)** If Mordiggian is killed, the shadows that comprise his body lose all form and become a 20-foot-diameter roiling _[[spells/Blot|blot]]_ of churning _darkness_ with a 300-foot fly speed and perfect maneuverability. This _blot_ of _darkness_ is _incorporeal_ and cannot be harmed, but it cannot enter an area of bright light. The _blot_ can sense all undead creatures within a 100-mile radius, and if it finds an undead creature, it can attempt to infuse it. An intelligent undead can resist this attack with a successful DC 40 Will saving throw; unintelligent undead receive no save. Once this _blot_ of _darkness_ infuses an undead creature, it grants the undead creature the advanced creature simple template, but 24 hours later, the undead is destroyed, releasing a fully-healed Mordiggian back into the world. If Mordiggian cannot find a suitable undead host within 24 hours or is trapped by bright light for that duration, the _blot_ of _darkness_ fades away, only to manifest immediately on another world—perhaps in the distant past, in the distant future, or even in the present. The save DC is Charisma-based.

**Tentacles (Su)** Mordiggian’s tentacles are primary attacks that inflict bludgeoning damage. He adds his Charisma modifier to damage done by his tentacles, which also gain a +5 enhancement bonus on attack rolls and damage rolls. These tentacles are treated as magic epic chaotic weapons for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. If Mordiggian reduces a living creature to fewer than 0 hit points with a tentacle or with his constriction damage, he automatically casts _death knell_ on the target as a free action.

**Unspeakable Presence (Su)** Failing a DC 40 Will saving throw against Mordiggian’s unspeakable presence causes the victim to become permanently _[[conditions/Blinded|blinded]]_. A creature that is killed while _blinded_ by this ability immediately animates as a chaotic evil juju zombie (Pathfinder RPG Bestiary 2 291). The save DC is Charisma-based.

##### Description

_[[items/Weapon Magic Abilities/Called|Called]]_ the _[[monsters/Charnel God|Charnel God]]_ by his worshipers, Mordiggian is one of the oldest and most powerful of the Great Old Ones. However, his tendency to move back and forth in time whenever he reincarnates makes the tracking of his age largely academic. None can say how long Mordiggian has existed, for as far as one can look back into the past or forward into the future, the presence of his cult can be found if one searches hard enough.

Mordiggian has no body. He appears as a cloud of mobile, _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ _darkness_ and _[[items/Armor Magic Abilities/Shadow|shadow]]_ that can change its outline and shape at will. He is fond of appearing as an immense graveworm or limbless giant made of _darkness_, and when he desires a meal, he can form tentacles of solid _darkness_ to pluck up his feast.

Ghouls, particularly those that dwell in Leng, often venerate Mordiggian with a ferocious zeal. They consider ghoulish worshipers of other deities, particularly of the demon lord Kabriri, to be heretics and work to eradicate such blasphemers whenever they are found. Although worship of Mordiggian has become quite rare on Golarion as other death gods have gained more prominence, his cult is patient and willing to simply wait for the _Charnel God_’s inevitable return to power.