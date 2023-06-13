---
cssclass: [monsters]
title1: Great Old One, Hastur
desc_short: This entity appears to be a skeletal human form hidden under tattered
  yellow robes, but it moves with unsettling, inhuman grace.
title2: Hastur
CR: 29
sources:
- name: Bestiary 4
  page: 140
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 6553600
alignment: CE
size: Medium
type: aberration
subtypes:
- chaotic
- evil
- Great Old One
initiative:
  bonus: 26
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 40
AC:
  AC: 48
  touch: 37
  flat_footed: 31
  components:
    dex: 16
    dodge: 1
    insight: 10
    natural: 11
HP:
  HP: 731
  long: 34d8+578
  fast_healing: 25
saves:
  fort: 28
  ref: 27
  will: 29
defensive_abilities:
- freedom of movement
- immortality
- insanity (DC 40)
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
- sonic
resistances:
  acid: 30
  electricity: 30
  fire: 30
SR: 40
speeds:
  base: 80
  other_semicolon: air walk
attacks:
  melee:
  - - text: 4 tattered lash +41 (2d8+7 plus bleed)
      entries:
      - - damage: 2d8+7
        - effect: bleed
      count: 4
      attack: tattered lash
      bonus:
      - 41
  special:
  - bleed (1d6)
  - fulvous dreams
  - mythic power (10/ day, surge +1d12)
  - reveal visage
  - sneak attack +10d6
  - Yellow Sign
space: 5
reach: 40
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - is_mythic_spell: true
    name: enervation
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 30
  - name: mirage arcana
    source: default
    freq: At will
    DC: 28
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 28
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: veil
    source: default
    freq: At will
  - is_mythic_spell: true
    name: wish
    source: default
    freq: At will
    other: see below
  - name: demand
    source: default
    freq: 3/day
    DC: 31
  - name: quickened feeblemind
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: interplanetary teleport
    source: default
    freq: 3/day
  - name: mass suggestion
    source: default
    freq: 3/day
    DC: 29
  - name: project image
    source: default
    freq: 3/day
    DC: 30
  - name: symbol of death
    source: default
    freq: 1/day
    DC: 31
  - name: symbol of fear
    source: default
    freq: 1/day
    DC: 29
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 31
  - name: symbol of pain
    source: default
    freq: 1/day
    DC: 28
  - name: symbol of persuasion
    source: default
    freq: 1/day
    DC: 29
  - superscripts:
    - UM
    name: symbol of strife
    source: default
    freq: 1/day
    DC: 32
  - name: symbol of stunning
    source: default
    freq: 1/day
    DC: 30
  - name: symbol of weakness
    source: default
    freq: 1/day
    DC: 30
  sources:
  - name: default
    CL: 29
    concentration: 42
ability_scores:
  STR: 24
  DEX: 43
  CON: 44
  INT: 35
  WIS: 31
  CHA: 36
BAB: 25
CMB: 41
CMD: 69
CMD_other: can't be tripped
feats:
- name: Agile Maneuvers
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Feint
- name: Greater Vital Strike
- name: Improved Critical (tattered lash)
- name: Improved Feint
- name: Improved Vital Strike
- name: Mobility
- name: Quicken Spell-Like Ability (feeblemind)
- name: Spring Attack
- name: Staggering Critical
- name: Vital Strike
- name: Weapon Finesse
- name: Whirlwind Attack
skills:
  Acrobatics: 53
    when jumping: 73
  Bluff: 47
  Disguise: 47
  Intimidate: 50
  Knowledge (arcana): 46
  Knowledge (geography): 46
  Knowledge (history): 46
  Knowledge (local): 46
  Knowledge (nobility): 49
  Perception: 47
  Perform (act): 47
  Sense Motive: 44
  Sleight of Hand: 50
  Spellcraft: 49
  Stealth: 53
  Use Magic Device: 47
  _racial_mods:
    Acrobatics:
      when jumping: 20
languages:
- Aklo
- telepathy 100 ft.
- tongues
special_qualities:
- otherworldly insight
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Fulvous Dreams (Su): When Hastur uses his nightmare spell-like ability on a creature
    that has seen the Yellow Sign, he also afflicts that creature with horrifying
    dreams tinted with a nauseating yellow color and thick with overwhelming sensations
    of decadence, shame, and entropic disorder. In addition to the effect of nightmare,
    the target must also succeed at a DC 40 Will save or be compelled to seek out
    a Yellow Sign, throwing all of his resources and actions into the obsession. While
    obsessed, the target takes a -4 penalty on Will saving throws, saving throws against
    symbol spells, concentration checks, and Wisdom-based skill checks. This obsession
    effect ends immediately if the victim looks upon the Yellow Sign. This is a mind-affecting
    curse effect. The save DC is Charisma-based.
  Immortality (Ex): If Hastur is slain, the robes that drape his frame suddenly drop
    to the ground as if whatever shape supported them had suddenly ceased to exist.
    The robes themselves remain inanimate on the ground, but any humanoid creature
    that touches them must succeed at a DC 40 Will save to resist a sudden urge to
    put the robes on. Doing so is a full-round action that provokes attacks of opportunity.
    Once it has donned Hastur's robes, the creature immediately perishes and its body
    is destroyed. In its place, Hastur lives again, as if brought back via true resurrection.
    If the discarded robes are not donned within 24 hours, they fade away, leaving
    behind a faint yellow stain. In this case, Hastur can't manifest a physical body
    again until the conditions are right, or until an unwitting cultist or fool calls
    him forth once again. The save DC is Charisma-based.
  Reveal Visage (Su): As a swift action, Hastur may reveal to one adjacent creature
    the true shape beneath his robes. The creature must succeed at DC 40 Will save
    or be paralyzed for 1d4 rounds and take 1d4 points of Wisdom drain at the end
    of its turn each round the paralysis lasts, though the revelation is too awful
    for memory to retain. This is a mind-affecting fear effect. The save DC is Charisma-based.
  Tattered Lash (Ex): Hastur attacks with long strips of his tattered yellow robes.
    These strips have a reach of 40 feet and are primary natural slashing attacks.
    Bleed damage from the strips stacks with itself (up to 10d6 points of bleed damage).
    Hastur treats insane targets as if they were flatfooted when he attacks with these
    weapons.
  Unspeakable Presence (Su): Failing a DC 40 Will save against Hastur's unspeakable
    presence afflicts a creature with a random insanity. A creature that is already
    insane instead becomes confused for as long as it remains in the area. The save
    DC is Charisma-based.
  Wish (Sp): Although Hastur may use wish as a spell-like ability at will, he can
    do so only to grant the wishes of other creatures, and only once per creature.
    Invariably, the results of these wishes serve somehow to advance Hastur's agenda.
  Yellow Sign (Su): Once per day as a free action, Hastur can touch any solid surface
    and inscribe the Yellow Sign upon it. Once inscribed, the Yellow Sign remains
    for a year, but is active only on certain nights when the light from Hastur's
    distant world shines in the night sky as a star. Any creature that looks upon
    an active Yellow Sign must succeed at a DC 40 Will save to avoid becoming dominated
    by Hastur (as dominate monster); whether or not the save is successful, the creature
    doesn't have to save against that Yellow Sign again for 24 hours. While the creature
    is under this domination effect, if the creature's Charisma drain plus Charisma
    damage ever equal its Charisma score, it immediately dies and allows Hastur to
    manifest physically at the location of its corpse, as if the victim had donned
    Hastur's tattered robes (see immortality). A Yellow Sign can be removed with dispel
    chaos, dispel evil, or erase, any of which requires the caster to succeed at a
    DC 35 caster level check. Mage's disjunction automatically removes a Yellow Sign.
    This is a mind-affecting effect. The save DC is Charisma-based.
desc_long: Hastur is the most mysterious of the Great Old Ones. In fact, the entity
  known as Hastur might actually be an Outer God. The physical manifestation of this
  entity is known as the King in Yellow, and though most consider this creature-a
  vaguely human-shaped figure draped in a yellow cloak-to be synonymous with Hastur
  himself, many scholars believe that the King in Yellow is nothing more than an avatar
  used by the true Hastur to move among the denizens of the physical world. Hastur
  himself is said to dwell upon a distant world called Carcosa on the shores of the
  monstrous Lake of Hali, and his power on a planet is strongest when the baleful
  light of Carcosa's star is visible in that planet's night sky.

---

# Great Old One, Hastur
This entity appears to be a skeletal human form hidden under tattered yellow robes, but it moves with unsettling, inhuman _[[spells/Grace|grace]]_.
**Source** Bestiary 4 pg. 140
**XP** 6,553,600
CE Medium aberration (chaotic, evil, Great Old One)
**Init** +26; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +47
**Aura** unspeakable presence (300 ft., DC 40)

##### Defense

**AC** 48, touch 37, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+16 Dex, +1 _[[feats/Dodge|dodge]]_, +10 insight, +11 natural)
**hp** 731 (34d8+578); _[[universal monster rules/Fast Healing|fast healing]]_ 25
**Fort** +28, **Ref** +27, **Will** +29
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 40); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, sonic; **Resist** acid 30, electricity 30, fire 30; **SR** 40

##### Offense
**Speed** 80 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 4 tattered lash +41 (2d8+7 plus _[[universal monster rules/Bleed|bleed]]_)
**Space** 5 ft., **Reach** 40 ft.
**Special Attacks** _bleed_ (1d6), fulvous dreams, mythic power (10/ day, surge +1d12), reveal visage, sneak attack +10d6, _[[spells/Yellow Sign|Yellow Sign]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +42)
Constant—_air walk_, _freedom of movement_, _[[spells/Tongues|tongues]]_, _true seeing_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, _[[spells/Enervation|enervation]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _insanity_ (DC 30), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 28), _[[spells/Nightmare|nightmare]]_ (DC 28), _[[spells/Sending|sending]]_, _[[spells/Veil|veil]]_, _[[spells/Wish|wish]]_ (see below)
3/day—_[[spells/Demand|demand]]_ (DC 31), quickened _[[spells/Feeblemind|feeblemind]]_, _[[spells/Interplanetary Teleport|interplanetary teleport]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 29), _[[spells/Project Image|project image]]_ (DC 30)
1/day—_[[spells/Symbol of Death|symbol of death]]_ (DC 31), _[[spells/Symbol of Fear|symbol of fear]]_ (DC 29), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 31), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 28), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 29), _[[spells/Symbol of Strife|symbol of strife]]_ (DC 32), _[[spells/Symbol of Stunning|symbol of stunning]]_ (DC 30), _[[spells/Symbol Of Weakness|symbol of weakness]]_ (DC 30)

##### Statistics
**Str** 24, **Dex** 43, **Con** 44, **Int** 35, **Wis** 31, **Cha** 36
**Base Atk** +25; **CMB** +41; **CMD** 69 (can’t be tripped)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Feint|Greater Feint]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (tattered lash), _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +53 (+73 when jumping), Bluff +47, Disguise +47, Intimidate +50, Knowledge (arcana, geography, history, local) +46, Knowledge (nobility) +49, Perception +47, Perform (act) +47, Sense Motive +44, Sleight of Hand +50, Spellcraft +49, Stealth +53, Use Magic Device +47; **Racial Modifiers** +20 Acrobatics when jumping
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., _tongues_
**SQ** otherworldly insight

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Fulvous Dreams (Su)** When Hastur uses his _nightmare_ spell-like ability on a creature that has seen the _Yellow Sign_, he also afflicts that creature with horrifying dreams tinted with a nauseating yellow color and thick with overwhelming sensations of decadence, shame, and entropic disorder. In addition to the effect of _nightmare_, the target must also succeed at a DC 40 Will save or be compelled to seek out a _Yellow Sign_, _[[items/Weapon Magic Abilities/Throwing|throwing]]_ all of his resources and actions into the obsession. While obsessed, the target takes a –4 penalty on Will saving throws, saving throws against symbol spells, concentration checks, and Wisdom-based skill checks. This obsession effect ends immediately if the victim looks upon the _Yellow Sign_. This is a mind-affecting curse effect. The save DC is Charisma-based.

**Immortality (Ex)** If Hastur is slain, the robes that drape his frame suddenly drop to the ground as if whatever shape supported them had suddenly ceased to exist. The robes themselves remain inanimate on the ground, but any humanoid creature that touches them must succeed at a DC 40 Will save to resist a sudden urge to put the robes on. Doing so is a full-round action that provokes attacks of opportunity. Once it has donned Hastur’s robes, the creature immediately perishes and its body is destroyed. In its place, Hastur lives again, as if brought back via _[[spells/True Resurrection|true resurrection]]_. If the discarded robes are not donned within 24 hours, they fade away, leaving behind a faint yellow stain. In this case, Hastur can’t manifest a physical body again until the conditions are right, or until an unwitting _[[npcs/Cultist|cultist]]_ or fool calls him forth once again. The save DC is Charisma-based.

**Reveal Visage (Su)** As a swift action, Hastur may reveal to one adjacent creature the true shape beneath his robes. The creature must succeed at DC 40 Will save or be _[[conditions/Paralyzed|paralyzed]]_ for 1d4 rounds and take 1d4 points of Wisdom drain at the end of its turn each round the _paralysis_ lasts, though the _[[spells/Revelation|revelation]]_ is too awful for memory to retain. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DC is Charisma-based.

**Tattered Lash (Ex)** Hastur attacks with long strips of his tattered yellow robes. These strips have a reach of 40 feet and are primary natural slashing attacks. _Bleed_ damage from the strips stacks with itself (up to 10d6 points of _bleed_ damage). Hastur treats insane targets as if they were flatfooted when he attacks with these weapons.

**Unspeakable Presence (Su)** Failing a DC 40 Will save against Hastur’s unspeakable presence afflicts a creature with a random _insanity_. A creature that is already insane instead becomes _[[conditions/Confused|confused]]_ for as long as it remains in the area. The save DC is Charisma-based.

**_Wish_ (Sp)** Although Hastur may use _wish_ as a spell-like ability at will, he can do so only to grant the wishes of other creatures, and only once per creature. Invariably, the results of these wishes serve somehow to advance Hastur’s agenda.

**_Yellow Sign_ (Su)** Once per day as a free action, Hastur can touch any solid surface and inscribe the _Yellow Sign_ upon it. Once inscribed, the _Yellow Sign_ remains for a year, but is active only on certain nights when the light from Hastur’s distant world shines in the night sky as a star. Any creature that looks upon an active _Yellow Sign_ must succeed at a DC 40 Will save to avoid becoming dominated by Hastur (as _[[spells/Dominate Monster|dominate monster]]_); whether or not the save is successful, the creature doesn’t have to save against that _Yellow Sign_ again for 24 hours. While the creature is under this domination effect, if the creature’s Charisma drain plus Charisma damage ever equal its Charisma score, it immediately dies and allows Hastur to manifest physically at the location of its corpse, as if the victim had donned Hastur’s tattered robes (see immortality). A _Yellow Sign_ can be removed with _[[spells/Dispel Chaos|dispel chaos]]_, _[[spells/Dispel Evil|dispel evil]]_, or _[[spells/Erase|erase]]_, any of which requires the caster to succeed at a DC 35 caster level check. Mage’s disjunction automatically removes a _Yellow Sign_. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

Hastur is the most mysterious of the Great Old Ones. In fact, the entity known as Hastur might actually be an Outer God. The physical manifestation of this entity is known as the _[[npcs/King|King]]_ in Yellow, and though most consider this creature—a vaguely human-shaped figure draped in a yellow cloak—to be synonymous with Hastur himself, many scholars believe that the _King_ in Yellow is nothing more than an avatar used by the true Hastur to move among the denizens of the physical world. Hastur himself is said to dwell upon a distant world _[[items/Weapon Magic Abilities/Called|called]]_ Carcosa on the shores of the monstrous Lake of Hali, and his power on a planet is strongest when the baleful light of Carcosa’s star is visible in that planet’s night sky.