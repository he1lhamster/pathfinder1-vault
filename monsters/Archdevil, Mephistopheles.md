---
cssclass: [monsters]
title1: Archdevil, Mephistopheles
desc_short: This red-skinned devil has three sets of curving horns atop hisbrow and
  three mismatched pairs of wings.
title2: Mephistopheles
CR: 30
sources:
- name: Bestiary 6
  page: 28
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9830400
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 14
senses:
  darkvision: 60
  detect chaos: true
  detect good: true
  discern lies: true
  see in darkness: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 41
- name: shield of law
  DC: 32
AC:
  AC: 48
  touch: 40
  flat_footed: 37
  components:
    deflection: 4
    dex,+1 dodge: 10
    natural: 8
    profane: 16
    size: -1
HP:
  HP: 752
  long: 35d10+560
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 31
  ref: 33
  will: 37
  other: +8 vs. mind-affecting effects
defensive_abilities:
- ashen essence
- freedom of movement,infernal resurrection
- mind blank
DR:
- amount: 20
  weakness: epic, good, andsilver
immunities:
- ability damage
- ability drain
- bleed
- blindness,blood drain
- charm
- compulsion
- critical hits
- dazzled,deafness
- death effects
- energy drain
- fire
- petrification,poison
- precision damage
resistances:
  acid: 30
  cold: 30
SR: 41
speeds:
  base: 50
  fly: 100
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +5 axiomatic flaming unholy trident +55/+50/+45/+40(2d6+29/19-20 plus
        1d6 fire)
      entries:
      - - damage: 2d6+29
          crit_range: 19-20
        - damage: 1d6
          type: fire
      attack: +5 axiomatic flaming unholy trident
      bonus:
      - 55
      - 50
      - 45
      - 40
    - text: gore +50 (2d8+8)
      entries:
      - - damage: 2d8+8
      attack: gore
      bonus:
      - 50
    - text: 6 wings +48(1d8+8/19-20)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
      count: 6
      attack: wings
      bonus:
      - 48
  special:
  - infernal wings
  - profane gift
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: discern lies
    source: default
    freq: Constant
    DC: 28
  - name: freedom of movement
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: shield of law
    source: default
    freq: Constant
    DC: 32
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - is_mythic_spell: true
    name: desecrate
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dictum
    source: default
    freq: At will
    DC: 31
  - is_mythic_spell: true
    name: dominate person
    source: default
    freq: At will
    DC: 29
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater scrying
    source: default
    freq: At will
    DC: 31
  - name: greater teleport
    source: default
    freq: At will
  - is_mythic_spell: true
    name: order's wrath
    source: default
    freq: At will
    DC: 28
  - name: secret page
    source: default
    freq: At will
  - name: unhallow
    source: default
    freq: At will
  - is_mythic_spell: true
    name: quickened dominate person
    source: default
    freq: 3/day
    DC: 29
  - is_mythic_spell: true
    name: fire storm
    source: default
    freq: 3/day
    DC: 32
  - is_mythic_spell: true
    name: globe of invulnerability
    source: default
    freq: 3/day
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 32
  - is_mythic_spell: true
    name: mislead
    source: default
    freq: 3/day
    DC: 30
  - name: summon devils
    source: default
    freq: 3/day
  - name: soul bind
    source: default
    freq: 1/day
    DC: 33
  - is_mythic_spell: true
    name: time stop
    source: default
    freq: 1/day
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 44
    mythic_restriction: Mephistopheles can use this ability's mythic version in his
      realm.
ability_scores:
  STR: 42
  DEX: 30
  CON: 43
  INT: 35
  WIS: 34
  CHA: 39
BAB: 35
CMB: 52
CMD: 93
feats:
- name: Combat Expertise
- name: Craft Construct
- name: Craft Magic Arms andArmor
- name: Craft Rod
- name: Craft Wondrous Item
- name: Critical Focus
- name: Deceitful
- name: Dodge
- name: Flyby Attack
- name: Forge Ring
- name: Improved Critical (trident)
- name: Improved Critical (wing)
- name: Improved Initiative
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (dominate person)
- name: Staggering Critical
skills:
  Bluff: 56
  Diplomacy: 52
  Disguise: 56
  Fly: 54
  Intimidate: 52
  Knowledge (arcana): 47
  Knowledge (history): 47
  Knowledge (local): 47
  Knowledge (nobility,religion): 47
  Knowledge (planes): 50
  Linguistics: 50
  Perception: 50
  Sense Motive: 50
  Sleight of Hand: 45
  Spellcraft: 47
  Stealth: 44
  Use Magic Device: 49
languages:
- all (language mastery)
- telepathy 300 ft.
special_qualities:
- flattering inquisitor
ecology:
  environment: any (Hell)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - +5 axiomatic flaming unholy trident
  - Visineir,other treasure
special_abilities:
  Ashen Essence (Ex): Despite his appearance, Mephistopheles has a body formed of
    the ashes and brimstone of Hell rather than flesh and blood. He cannot be blinded,
    dazzled, or deafened, and he is immune to bleed damage, blood drain, critical
    hits, and precision-based damage. In addition, once per minute when he is hit
    by a melee or ranged attack, as an immediate action Mephistopheles can cause his
    body and all of his gear to collapse into ashes while he teleports to any point
    within 30 feet of his prior position and re-forms, taking no damage from the attack.
    Within his realm of Caina, he can trigger this power by expending one use of his
    mythic power and can teleport up to 300 feet, or up to 30 feet even when subject
    to effects that normally prevent teleportation.
  Flattering Inquisitor (Su): Mephistopheles is unsurpassed at inveigling himself
    into a creature's good graces and ferreting out secrets. His discern lies spell-like
    ability automatically affects all creatures within 30 feet of him, and he does
    not need to concentrate to know whether a target is lying (although each time
    a creature tries to lie in this area it can attempt a Will save to negate the
    effect as normal). Anyone who attempts to lie when responding to a direct question
    posed by Mephistopheles must succeed at a DC 41 Will save or take 1d3 points of
    Wisdom drain and be unable to speak for 24 hours (Mephistopheles can end this
    enforced vow of silence at will as a free action). This is a mind-affecting effect.
    The save DC is Charisma-based.
  Infernal Wings (Su): Mephistopheles has three pairs of wings, and while the damage
    caused by all six wings is identical, the additional effect caused by a strike
    from a wing depends on its nature. A hit from one of his burning wings deals 1d6
    additional points of fire damage and the creature struck must succeed at a DC
    43 Reflex save or catch fire. A hit from one of his draconic wings deals 2d6 points
    of bleed damage. A hit from one of his raven wings causes permanent blindness
    unless the creature struck succeeds at a DC 43 Fortitude save. The save DCs are
    Constitution-based.
  Profane Gift (Su): As a full-round action, Mephistopheles can grant a willing non-devil
    a +4 profane bonus to one ability score; this also allows him to communicate telepathically
    with and use his mind-affecting spell-like abilities on the creature at any distance
    (even across planar boundaries). A creature can have only one such gift at a time.
    The profane gift can be removed with dispel evil or dispel law, or Mephistopheles
    can remove it as a free action, dealing 3d6 points of Charisma drain to the target
    (no save). In addition, a creature that accepts a wish from Mephistopheles immediately
    becomes lawful evil (Will DC 41 negates) and gains the benefits of good hope for
    1 week, followed by the effects of crushing despair for 1d6 months (CL 30th).
    The save DC is Charisma-based.
desc_long: |-
  Mephistopheles was formed by Asmodeus from the ashes and hellfire of the plane of Hell itself. He is an artist of f lattery and guile, a master of the infernal contract, and a warden of the chained prison plane of Caina. He is tireless in his hunt for new souls, and constantly seeks to lure mortals into signing theirs away in all manner of complex bargains and contracts. 

  Mephistopheles appears as a muscular, 12-foot-tall, red-skinned humanoid.

---

# Archdevil, Mephistopheles
This red-skinned devil has three sets of curving horns atop his

brow and three mismatched pairs of wings.
**Source** Bestiary 6 pg. 28
**XP** 9,830,400

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Good|detect good]]_,

_[[spells/Discern Lies|discern lies]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +50
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 41), _[[spells/Shield of Law|shield of law]]_ (DC 32)

##### Defense

**AC** 48, touch 40, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+4 deflection, +10 Dex,

+1 _[[feats/Dodge|dodge]]_, +8 natural, +16 profane, –1 size)
**hp** 752 (35d10+560); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +31, **Ref** +33, **Will** +37; +8 vs. mind-affecting effects
**Defensive Abilities** ashen essence, _[[spells/Freedom of Movement|freedom of movement]]_,

infernal _[[spells/Resurrection|resurrection]]_, _[[spells/Mind Blank|mind blank]]_; **DR** 20/epic, good, and

silver; **Immune** ability damage, ability drain, _[[universal monster rules/Bleed|bleed]]_, blindness,

_[[universal monster rules/Blood Drain|blood drain]]_, charm, compulsion, critical hits, _[[conditions/Dazzled|dazzled]]_,

deafness, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, fire, petrification,

poison, precision damage; **Resist** acid 30, cold 30; **SR** 41

##### Offense
**Speed** 50 ft., fly 100 ft. (perfect)
**Melee** +5 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Trident|trident]]_ +55/+50/+45/+40

(2d6+29/19–20 plus 1d6 fire), gore +50 (2d8+8), 6 wings +48

(1d8+8/19–20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** infernal wings, profane gift
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +44)
Constant—_detect chaos_, _detect good_, _discern lies_ (DC 28), _freedom of movement_, _mind blank_, _shield of law_ (DC 32), _true seeing_ 
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Dictum|dictum]]_ (DC 31), _[[spells/Dominate Person|dominate person]]_ (DC 29), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Scrying|scrying]]_ (DC 31), greater teleport, order’s wrath (DC 28), _[[spells/Secret Page|secret page]]_, _[[spells/Unhallow|unhallow]]_ 
3/day—quickened _dominate person_ (DC 29), _[[spells/Fire Storm|fire storm]]_ (DC 32), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, mass _[[spells/Charm Monster|charm monster]]_ (DC 32), _[[spells/Mislead|mislead]]_ (DC 30), _[[universal monster rules/Summon|summon]]_ devils 
1/day—_[[spells/Soul Bind|soul bind]]_ (DC 33), _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_ 
 Mephistopheles can use this ability’s mythic version in his realm.

##### Statistics
**Str** 42, **Dex** 30, **Con** 43, **Int** 35, **Wis** 34, **Cha** 39
**Base Atk** +35; **CMB** +52; **CMD** 93
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Construct|Craft Construct]]_, Craft Magic Arms and

Armor, _[[feats/Craft Rod|Craft Rod]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Improved Critical|Improved Critical]]_ (_trident_, wing), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_), _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Bluff +56, Diplomacy +52, Disguise +56, Fly +54,

Intimidate +52, Knowledge (arcana, history, local, nobility,

religion) +47, Knowledge (planes) +50, Linguistics +50,

Perception +50, Sense Motive +50, Sleight of Hand +45,

Spellcraft +47, Stealth +44, Use Magic Device +49
**Languages** all (language mastery); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** flattering _[[classes/Inquisitor|inquisitor]]_

##### Ecology

**Environment** any (Hell)
**Organization** solitary (unique)
**Treasure** triple (+5 _axiomatic_ _flaming_ _unholy_ _trident_, _[[items/Wondrous Item/Visineir|Visineir]]_,

other treasure)

### Special Abilities

**Ashen Essence (Ex)** Despite his appearance, Mephistopheles has a body formed of the ashes and brimstone of Hell rather than flesh and blood. He cannot be _[[conditions/Blinded|blinded]]_, _dazzled_, or _[[conditions/Deafened|deafened]]_, and he is immune to _bleed_ damage, _blood drain_, critical hits, and precision-based damage. In addition, once per minute when he is hit by a melee or ranged attack, as an immediate action Mephistopheles can cause his body and all of his gear to collapse into ashes while he teleports to any point within 30 feet of his prior position and re-forms, taking no damage from the attack. Within his realm of Caina, he can trigger this power by expending one use of his mythic power and can teleport up to 300 feet, or up to 30 feet even when subject to effects that normally prevent teleportation.

**Flattering _Inquisitor_ (Su)** Mephistopheles is unsurpassed at inveigling himself into a creature’s good graces and ferreting out secrets. His _discern lies_ spell-like ability automatically affects all creatures within 30 feet of him, and he does not need to concentrate to know whether a target is lying (although each time a creature tries to lie in this area it can attempt a Will save to negate the effect as normal). Anyone who attempts to lie when responding to a direct question posed by Mephistopheles must succeed at a DC 41 Will save or take 1d3 points of Wisdom drain and be unable to speak for 24 hours (Mephistopheles can end this enforced vow of _[[spells/Silence|silence]]_ at will as a free action). This is a mind-affecting effect. The save DC is Charisma-based.

**Infernal Wings (Su)** Mephistopheles has three pairs of wings, and while the damage caused by all six wings is identical, the additional effect caused by a strike from a wing depends on its nature. A hit from one of his _[[items/Weapon Magic Abilities/Burning|burning]]_ wings deals 1d6 additional points of fire damage and the creature struck must succeed at a DC 43 Reflex save or catch fire. A hit from one of his draconic wings deals 2d6 points of _bleed_ damage. A hit from one of his raven wings causes permanent blindness unless the creature struck succeeds at a DC 43 Fortitude save. The save DCs are Constitution-based.

**Profane Gift (Su)** As a full-round action, Mephistopheles can grant a willing non-devil a +4 profane bonus to one ability score; this also allows him to communicate telepathically with and use his mind-affecting _spell-like abilities_ on the creature at any distance (even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries). A creature can have only one such gift at a time. The profane gift can be removed with _[[spells/Dispel Evil|dispel evil]]_ or _[[spells/Dispel Law|dispel law]]_, or Mephistopheles can remove it as a free action, dealing 3d6 points of Charisma drain to the target (no save). In addition, a creature that accepts a _wish_ from Mephistopheles immediately becomes lawful evil (Will DC 41 negates) and gains the benefits of _[[spells/Good Hope|good hope]]_ for 1 week, followed by the effects of _[[spells/Crushing Despair|crushing despair]]_ for 1d6 months (CL 30th). The save DC is Charisma-based.

##### Description

Mephistopheles was formed by Asmodeus from the ashes and hellfire of the plane of Hell itself. He is an artist of f lattery and guile, a master of the infernal contract, and a warden of the chained prison plane of Caina. He is tireless in his hunt for new souls, and constantly seeks to lure mortals into signing theirs away in all manner of complex bargains and contracts.

Mephistopheles appears as a muscular, 12-foot-tall, red-skinned humanoid.