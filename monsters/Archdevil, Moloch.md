---
cssclass: [monsters]
title1: Archdevil, Moloch
desc_short: This immense figure appears to be a suit of blackened, diabolicarmor filled
  with shrieking blasts of blistering fire.
title2: Moloch
CR: 29
sources:
- name: Bestiary 6
  page: 30
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 6553600
alignment: LE
size: Huge
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 11
senses:
  darkvision: 60
  detect chaos: true
  detect good: true
  mistsight: true
  see in darkness: true
  true seeing: true
auras:
- name: fiendish furnace
  radius: 10
- name: frightful presence
  radius: 120
  DC: 38
- name: shield of law
  DC: 29
AC:
  AC: 47
  touch: 34
  flat_footed: 40
  components:
    deflection: 4
    dex,+13 natural: 7
    profane: 15
    size: -2
HP:
  HP: 731
  long: 34d10+544
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 39
  ref: 24
  will: 35
  other: +8 vs. mind-affecting effects
defensive_abilities:
- fortification (50%)
- infernal resurrection
- mindblank
DR:
- amount: 20
  weakness: epic, good, and silver
immunities:
- ability damage,ability drain
- charm
- compulsion
- death effects
- energy drain,fire
- petrification
- poison
resistances:
  acid: 30
  cold: 30
SR: 40
speeds:
  base: 40
  other:
  - air walk
attacks:
  melee:
  - - text: Goreletch +46/+41/+36/+31 (3d6+18/19-20/×4)
      entries:
      - - damage: 3d6+18
          crit_range: 19-20
          crit_multiplier: 4
      attack: Goreletch
      bonus:
      - 46
      - 41
      - 36
      - 31
    - text: Ramithaine +46/+41 (3d6+18/17-20/×3)
      entries:
      - - damage: 3d6+18
          crit_range: 17-20
          crit_multiplier: 3
      attack: Ramithaine
      bonus:
      - 46
      - 41
    - text: bite +42 (2d6+7 plus grab and burn)
      entries:
      - - damage: 2d6+7
        - effect: grab
        - effect: burn
      attack: bite
      bonus:
      - 42
    - text: gore +42 (2d6+7 plus burn)
      entries:
      - - damage: 2d6+7
        - effect: burn
      attack: gore
      bonus:
      - 42
  special:
  - barbed blademaster
  - burn (2d6 hellfire, DC 43),fast swallow
  - incinerate
  - spirit of hellfire
  - swallow whole(20d10 hellfire damage plus pain, AC 16, 73 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: shield of law
    source: default
    freq: Constant
    DC: 29
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
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
    DC: 28
  - is_mythic_spell: true
    name: dominate person
    source: default
    freq: At will
    DC: 26
  - is_mythic_spell: true
    name: fireball
    source: default
    freq: At will
    DC: 24
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - is_mythic_spell: true
    name: order's wrath
    source: default
    freq: At will
    DC: 25
  - is_mythic_spell: true
    name: slow
    source: default
    freq: At will
    DC: 24
  - name: unhallow
    source: default
    freq: At will
  - is_mythic_spell: true
    name: wall of fire
    source: default
    freq: At will
  - is_mythic_spell: true
    name: quickened blade barrier
    source: default
    freq: 3/day
    DC: 27
  - name: empowered fire storm
    source: default
    freq: 3/day
    DC: 29
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 29
  - name: mass hold person
    source: default
    freq: 3/day
    DC: 28
  - name: summon devils
    source: default
    freq: 3/day
  - is_mythic_spell: true
    name: meteor swarm
    source: default
    freq: 1/day
    DC: 30
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
    CL: 29
    concentration: 40
    mythic_restriction: Moloch can use this ability's mythic version in his realm
ability_scores:
  STR: 40
  DEX: 25
  CON: 42
  INT: 25
  WIS: 34
  CHA: 33
BAB: 34
CMB: 51
CMB_other: +53 bull rush
CMD: 87
CMD_other: 89 vs. bull rush
feats:
- name: Combat Expertise
- name: Craft Magic Arms and Armor
- name: CriticalFocus
- name: Double Slice
- name: Empower Spell-Like Ability (firestorm)
- name: Improved Bull Rush
- name: Improved Critical (battleaxe)
- name: Improved Critical (longsword)
- name: Improved Initiative
- name: Improved LightningReflexes
- name: Improved Two-Weapon Fighting
- name: LightningReflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (bladebarrier))
- name: Quicken Spell-Like Ability (Staggering Critical)
- name: Quicken Spell-Like Ability (Two-Weapon Fighting)
- name: Quicken Spell-Like Ability (Two-Weapon Rend)
skills:
  Bluff: 48
  Intimidate: 48
  Knowledge (arcana,history): 41
  Knowledge (religion): 41
  Knowledge (nobility): 44
  Knowledge (planes): 44
  Linguistics: 44
  Perception: 49
  Sense Motive: 49
  Spellcraft: 44
  Survival: 46
  Use Magic Device: 45
languages:
- all (language mastery)
- telepathy 300 ft.
special_qualities:
- call weaponry
- infernal fortress
ecology:
  environment: any (Hell)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - Goreletch
  - Ramithaine
  - other treasure
special_abilities:
  Barbed Blademaster (Ex): Moloch is proficient with all weapons. In addition, any
    piercing or slashing weapon he wields sprouts cruel, wicked barbs that increase
    the weapon's critical multiplier by 1 for as long as he wields it. Targets that
    have fortification gain only half their usual chance of ignoring Moloch's critical
    hits.
  Call Weaponry (Su): Moloch can call his weapons Goreletch (a +3 adamantine unholy
    vorpal battleaxe) and Ramithaine (a +3 axiomatic cruel unholy wounding longsword)
    to his hands at will as a free action from any distance (even across planar boundaries).
    If one of these weapons is destroyed, he can remake it and cause the rebuilt weapon
    to appear in his hand as a standard action; if needed, he can instead remake both
    weapons as a full-round action. Remaking a weapon in this way provokes attacks
    of opportunity, but calling a weapon does not.
  Fiendish Furnace (Ex): Any creature that comes within 10 feet of Moloch or begins
    its turn within this area takes 2d8 points of hellfire damage (no save). In addition,
    creatures that strike Moloch in melee are affected by his burn ability unless
    they succeed at a DC 43 Reflex save. Whenever Moloch would take cold damage, he
    can choose to block all cold damage from that attack, but doing so causes his
    fiendish furnace ability to be negated until the start of his next turn. Choosing
    to do so is reflexive and does not require any action on Moloch's part. The save
    DC is Constitution-based.
  Incinerate (Su): When a creature is reduced to 0 hit points by an attack or effect
    used by Moloch that deals hellfire damage, it is instantly killed and its body
    reduced to ash (Fortitude DC 38 negates). Creatures destroyed in this way can
    be restored to life only through miracle, true resurrection, wish, or divine intervention.
    The save DC is Charisma-based.
  Infernal Fortress (Su): Once per day as a full-round action, Moloch can cause a
    towering fortress to erupt from the ground at a point within 30 feet. Treat this
    ability as if Moloch used an instant fortress, save that the fortress is 60 feet
    square and 90 feet tall, and sized for a Huge inhabitant. Once created, this fortress
    is permanent until Moloch uses the ability again, whereupon the previous fortress
    vanishes; any objects and creatures within the fortress fall to the ground at
    this time.
  Spirit of Hellfire (Su): Whenever Moloch creates an effect that would normally deal
    fire damage, it instead deals hellfire damage. Half of the damage dealt by hellfire
    is fire damage, with the other half being unholy damage that is not reduced by
    fire resistance or fire immunity.
  Swallow Whole (Su): Whenever a creature takes hellfire damage as a result of being
    swallowed whole by Moloch, it must succeed at a DC 43 Will save or be so overwhelmed
    with pain that it can do nothing but shriek and wail in agony, and can take no
    other action; this is a pain effect. Each round that such a victim shrieks in
    pain, Moloch's frightful presence is automatically activated and he gains a +4
    profane bonus to the save DC to resist its effects. The save DC is Constitution-based.
desc_long: |-
  Moloch is the dread general of Hell's armies, both his own hordes in the pits of Malebolge and the legions serving his lieutenants throughout the plane. He is fiercely loyal to Asmodeus and to Hell itself, and he marshals not only devils but also lost souls, other denizens of Hell, and interplanar mercenaries in brutal, endless campaigns. He can recount the dispositions and particulars of every military formation in Hell, and he brooks no insubordination or disobedience in martial matters, under threat of burning torments that are terrible even by Hell's standards. Moloch is surprisingly responsive to his mortal worshipers, and he is quite willing to exchange his favor for gifts of provisions, supplies, and soldiers for the infernal armies. Those sacrificed to him in the fires of the mortal world or ritually cremated in his honor after death face an eternity of soldierly slavery in his legions. 

  Moloch is a hulking giant of fire and steel, standing 24 feet tall and weighing 5 tons. What appears to be his armor is in fact his flesh, inside which lies nothing but flames, ash, and bits of scorched bone from previous victims. Despite his fiery appearance, he is a cool and professional tactician who has studied war for eons and has put every known tactical theory into practice in the endless war against the celestial hosts and the fiendish rivals of Hell.

---

# Archdevil, Moloch
This immense figure appears to be a suit of blackened, diabolic

armor filled with shrieking blasts of blistering fire.
**Source** Bestiary 6 pg. 30
**XP** 6,553,600

LE Huge outsider (devil, evil, extraplanar, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Good|detect good]]_,

_[[universal monster rules/Mistsight|mistsight]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +49
**Aura** fiendish furnace (10 ft.), _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft.,

DC 38), _[[spells/Shield of Law|shield of law]]_ (DC 29)

##### Defense

**AC** 47, touch 34, _[[conditions/Flat-Footed|flat-footed]]_ 40 (+4 deflection, +7 Dex,

+13 natural, +15 profane, –2 size)
**hp** 731 (34d10+544); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +39, **Ref** +24, **Will** +35; +8 vs. mind-affecting effects
**Defensive Abilities** _[[universal monster rules/Fortification|fortification]]_ (50%), infernal _[[spells/Resurrection|resurrection]]_, mind

blank; **DR** 20/epic, good, and silver; **Immune** ability damage,

ability drain, charm, compulsion, death effects, _[[universal monster rules/Energy Drain|energy drain]]_,

fire, petrification, poison; **Resist** acid 30, cold 30; **SR** 40

##### Offense
**Speed** 40 ft., _[[spells/Air Walk|air walk]]_
**Melee** Goreletch +46/+41/+36/+31 (3d6+18/19–20/×4), Ramithaine +46/+41 (3d6+18/17–20/×3), bite +42 (2d6+7 plus _[[universal monster rules/Grab|grab]]_ and _[[universal monster rules/Burn|burn]]_), gore +42 (2d6+7 plus _burn_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** barbed blademaster, _burn_ (2d6 hellfire, DC 43),

_[[universal monster rules/Fast Swallow|fast swallow]]_, incinerate, spirit of hellfire, _[[universal monster rules/Swallow Whole|swallow whole]]_

(20d10 hellfire damage plus pain, AC 16, 73 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +40)
Constant—_air walk_, _detect chaos_, _detect good_, _[[spells/Mind Blank|mind blank]]_, _shield of law_ (DC 29), _true seeing_ 
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Dictum|dictum]]_ (DC 28), _[[spells/Dominate Person|dominate person]]_ (DC 26), _[[spells/Fireball|fireball]]_ (DC 24), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, order’s wrath (DC 25), _[[spells/Slow|slow]]_ (DC 24), _[[spells/Unhallow|unhallow]]_, _[[spells/Wall Of Fire|wall of fire]]_ 
3/day—quickened _[[spells/Blade Barrier|blade barrier]]_ (DC 27), empowered _[[spells/Fire Storm|fire storm]]_ (DC 29), mass _[[spells/Charm Monster|charm monster]]_ (DC 29), mass _[[spells/Hold Person|hold person]]_ (DC 28), _[[universal monster rules/Summon|summon]]_ devils 
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 30), _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_ 
 Moloch can use this ability’s mythic version in his realm

##### Statistics
**Str** 40, **Dex** 25, **Con** 42, **Int** 25, **Wis** 34, **Cha** 33
**Base Atk** +34; **CMB** +51 (+53 bull rush); **CMD** 87 (89 vs. bull rush)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, Critical

Focus, _[[feats/Double Slice|Double Slice]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (fire

storm), _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Battleaxe|battleaxe]]_, _[[items/Weapon/Longsword|longsword]]_), _[[feats/Improved Initiative|Improved Initiative]]_, Improved Lightning

Reflexes, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, Lightning

Reflexes, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (blade

barrier), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, Two-

Weapon _[[universal monster rules/Rend|Rend]]_)
**Skills** Bluff +48, Intimidate +48, Knowledge (arcana,

history, religion) +41, Knowledge (nobility, planes) +44,

Linguistics +44, Perception +49, Sense Motive +49,

Spellcraft +44, Survival +46, Use Magic Device +45
**Languages** all (language mastery); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** call weaponry, infernal fortress

##### Ecology

**Environment** any (Hell)
**Organization** solitary (unique)
**Treasure** triple (Goreletch, Ramithaine, other treasure)

### Special Abilities

**Barbed Blademaster (Ex)** Moloch is proficient with all weapons. In addition, any piercing or slashing weapon he wields sprouts _[[items/Weapon Magic Abilities/Cruel|cruel]]_, wicked barbs that increase the weapon’s critical multiplier by 1 for as long as he wields it. Targets that have _fortification_ gain only half their usual chance of ignoring Moloch’s critical hits.

**Call Weaponry (Su)** Moloch can call his weapons Goreletch (a +3 adamantine _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ _battleaxe_) and Ramithaine (a +3 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _cruel_ _unholy_ _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _longsword_) to his hands at will as a free action from any distance (even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries). If one of these weapons is destroyed, he can remake it and cause the rebuilt weapon to appear in his hand as a standard action; if needed, he can instead remake both weapons as a full-round action. Remaking a weapon in this way provokes attacks of opportunity, but calling a weapon does not.

**Fiendish Furnace (Ex)** Any creature that comes within 10 feet of Moloch or begins its turn within this area takes 2d8 points of hellfire damage (no save). In addition, creatures that strike Moloch in melee are affected by his _burn_ ability unless they succeed at a DC 43 Reflex save. Whenever Moloch would take cold damage, he can choose to block all cold damage from that attack, but doing so causes his fiendish furnace ability to be negated until the start of his next turn. Choosing to do so is reflexive and does not require any action on Moloch’s part. The save DC is Constitution-based.

**Incinerate (Su)** When a creature is reduced to 0 hit points by an attack or effect used by Moloch that deals hellfire damage, it is instantly killed and its body reduced to ash (Fortitude DC 38 negates). Creatures destroyed in this way can be restored to life only through _[[spells/Miracle|miracle]]_, _[[spells/True Resurrection|true resurrection]]_, _wish_, or divine intervention. The save DC is Charisma-based.

**Infernal Fortress (Su)** Once per day as a full-round action, Moloch can cause a towering fortress to erupt from the ground at a point within 30 feet. Treat this ability as if Moloch used an _[[items/Wondrous Item/Instant Fortress|instant fortress]]_, save that the fortress is 60 feet square and 90 feet tall, and sized for a Huge inhabitant. Once created, this fortress is permanent until Moloch uses the ability again, whereupon the previous fortress vanishes; any objects and creatures within the fortress fall to the ground at this time.
**Spirit of Hellfire (Su)** Whenever Moloch creates an effect that would normally deal fire damage, it instead deals hellfire damage. Half of the damage dealt by hellfire is fire damage, with the other half being _unholy_ damage that is not reduced by fire _[[universal monster rules/Resistance|resistance]]_ or fire _[[universal monster rules/Immunity|immunity]]_.
**_Swallow Whole_ (Su)** Whenever a creature takes hellfire damage as a result of being swallowed whole by Moloch, it must succeed at a DC 43 Will save or be so overwhelmed with pain that it can do nothing but shriek and wail in agony, and can take no other action; this is a pain effect. Each round that such a victim shrieks in pain, Moloch’s _frightful presence_ is automatically activated and he gains a +4 profane bonus to the save DC to resist its effects. The save DC is Constitution-based.

##### Description

Moloch is the dread general of Hell’s armies, both his own hordes in the pits of Malebolge and the legions serving his lieutenants throughout the plane. He is fiercely loyal to Asmodeus and to Hell itself, and he marshals not only devils but also lost souls, other denizens of Hell, and interplanar mercenaries in brutal, endless campaigns. He can recount the dispositions and particulars of every military formation in Hell, and he brooks no insubordination or disobedience in martial matters, under threat of _[[items/Weapon Magic Abilities/Burning|burning]]_ torments that are terrible even by Hell’s standards. Moloch is surprisingly responsive to his mortal worshipers, and he is quite willing to exchange his favor for gifts of provisions, supplies, and soldiers for the infernal armies. Those sacrificed to him in the fires of the mortal world or ritually cremated in his honor after death face an eternity of soldierly slavery in his legions.

Moloch is a hulking giant of fire and steel, standing 24 feet tall and weighing 5 tons. What appears to be his armor is in fact his flesh, inside which lies nothing but flames, ash, and bits of scorched bone from previous victims. Despite his fiery appearance, he is a cool and professional tactician who has studied war for eons and has put every known tactical theory into practice in the endless war against the celestial hosts and the fiendish rivals of Hell.