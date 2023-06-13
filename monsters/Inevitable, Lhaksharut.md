---
cssclass: [monsters]
title1: Inevitable, Lhaksharut
desc_short: This six-armed creature appears to be made of stone. Its lower torso is
  a collection of whirring rings of metal.
title2: Lhaksharut
CR: 20
sources:
- name: Bestiary 2
  page: 164
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 307200
alignment: LN
size: Huge
type: outsider
subtypes:
- extraplanar
- inevitable
- lawful
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect chaos: true
  detect magic: true
  low-light vision: true
  true seeing: true
auras:
- name: shield of law
  DC: 23
AC:
  AC: 36
  touch: 18
  flat_footed: 35
  components:
    deflection: 4
    dex: 1
    insight: 5
    natural: 18
    size: -2
HP:
  HP: 337
  long: 22d10+216
  regeneration: 10
  regeneration_weakness: chaotic
saves:
  fort: 25
  ref: 12
  will: 22
defensive_abilities:
- constructed
DR:
- amount: 15
  weakness: chaotic
immunities:
- energy spells
SR: 31
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +2 wounding spear +32/+27/+22/+17 (3d6+17/x3 plus 1 bleed)
      entries:
      - - damage: 3d6+17
          crit_multiplier: 3
        - damage: '1'
          type: bleed
      attack: +2 wounding spear
      bonus:
      - 32
      - 27
      - 22
      - 17
    - text: +2 wounding longsword +32 (3d6+12/19-20 plus 1 bleed)
      entries:
      - - damage: 3d6+12
          crit_range: 19-20
        - damage: '1'
          type: bleed
      attack: +2 wounding longsword
      bonus:
      - 32
    - text: +2 wounding morningstar +32 (3d6+12 plus 1 bleed)
      entries:
      - - damage: 3d6+12
        - damage: '1'
          type: bleed
      attack: +2 wounding morningstar
      bonus:
      - 32
  - - text: 4 slams +30 (2d8+10)
      entries:
      - - damage: 2d8+10
      count: 4
      attack: slams
      bonus:
      - 30
  ranged:
  - - text: 2 energy bolts +21 (10d6 energy)
      entries:
      - - damage: 10d6
          type: energy
      count: 2
      attack: energy bolts
      bonus:
      - 21
  special:
  - cunning reflexes
  - multiweapon mastery
  - perfect prediction
  - wounding weapons
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: shield of law
    source: default
    freq: Constant
    DC: 23
  - name: true seeing
    source: default
    freq: Constant
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: sending
    source: default
    freq: At will
  - name: dictum
    source: default
    freq: 3/day
    DC: 22
  - name: dimensional anchor
    source: default
    freq: 3/day
    DC: 19
  - name: dimensional lock
    source: default
    freq: 3/day
    DC: 23
  - name: disintegrate
    source: default
    freq: 3/day
    DC: 21
  - name: dismissal
    source: default
    freq: 3/day
    DC: 20
  - name: greater scrying
    source: default
    freq: 3/day
    DC: 22
  - name: plane shift
    source: default
    freq: 3/day
    DC: 20
  - name: wall of force
    source: default
    freq: 3/day
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 22
    concentration: 27
ability_scores:
  STR: 31
  DEX: 13
  CON: 26
  INT: 14
  WIS: 21
  CHA: 20
BAB: 22
CMB: 34
CMD: 50
CMD_other: can't be tripped
feats:
- name: Blind-Fight
- name: Combat Expertise
- name: Combat Reflexes
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Vital Strike
skills:
  Fly: 30
  Intimidate: 30
  Knowledge (arcana): 24
  Knowledge (geography): 24
  Knowledge (planes): 27
  Perception: 34
  Sense Motive: 30
  Spellcraft: 24
  _racial_mods:
    Perception:
      _: 4
languages:
- truespeech
special_qualities:
- perfect prediction
ecology:
  environment: any
  organization: solitary
  treasure_type: double
  treasure:
  - +2 longsword
  - +2 spear
  - +2 morningstar
  - other treasure
special_abilities:
  Cunning Reflexes (Ex): A lhaksharut uses its Wisdom modifier, rather than its Dexterity
    modifier, to determine how many additional attacks of opportunity it gains with
    the Combat Reflexes feat. For most lhaksharut inevitables, this benefit equates
    to 5 additional attacks of opportunity per round.
  Energy Bolt (Su): A lhaksharut can fire bolts of elemental energy from two of its
    six arms-it never wields weapons in these hands. These attacks have a range increment
    of 100 feet and deal 10d6 energy damage of the inevitable's choice (acid, cold,
    electricity, or fire, chosen for each bolt as it is thrown). It can throw two
    bolts of energy as a standard action, and cannot attack with these hands when
    it makes weapon or slam attacks with its other limbs.
  Immunity to Energy Spells (Ex): A lhaksharut is immune to any spell or spell-like
    ability with the acid, cold, electricity, fire, or sonic descriptor that allows
    spell resistance.
  Multiweapon Mastery (Ex): A lhaksharut never takes penalties on its attack rolls
    when fighting with multiple weapons.
  Perfect Prediction (Su): A lhaksharut gains an insight bonus to AC equal to its
    Wisdom bonus.
  Wounding Weapons (Su): Any weapon wielded by a lhaksharut gains the wounding weapon
    quality as long as it remains in the creature's grasp.
desc_long: |-
  A typical lhaksharut is a six-armed construct that appears to be made of a mix of metals and stone. Where a human would have legs, it instead possesses a complex orb of spinning rings similar in shape to an orrery-it is this whirling machine that grants the lhaksharut the ability to fly. Though a lhaksharut has huge, metal wings, they serve as little more than stabilizers when it's in flight. Four of the construct's arms end in functional hands that it normally uses to carry a mix of weapons. The lhaksharut's lower two arms hold large, flaming metal spheres in their hands-it uses these spheres to generate elemental bolts of energy that it can hurl great distances to damage foes.

  Lhaksharuts are tasked with maintaining the separation between different planes of reality, especially the elemental planes. They do not concern themselves with petty trespasses by visitors from one plane to another, nor even the occasional creation of a pocket plane or hijacking of a chunk of one reality to serve as a base within another. What does trouble a lhaksharut is anything that represents a permanent link between planes, or an effort by the denizens of one plane to invade and conquer another. They often find themselves in conflict with the machinations of powerful outsiders who seek to create beachheads on other planes to serve as launching pads for massive incursions.

  When possible, a lhaksharut enforces the separation of planes through the simple expedient of smashing any device that creates a dangerous breach, or killing any creature that seems determined to mix or blend realities. The inevitable does not care why such infractions occur, and is often deaf to any excuse suggesting even a temporary linking of planes is a good idea. However, while singled-mined, a lhaksharut is not mindless or incapable of reason. They are emotionless, but can be negotiated with if a problem cannot be solved by smashing and killing violators.

  Rarely, a lhaksharut can even be convinced that maintaining a planar link is important enough to let the gate stand, if only temporarily. In such cases, the lhaksharut always volunteers to guard the portal until the time comes to shut it down. These arrangements must include a detailed explanation on how a desired course of action will directly lead to meeting the lhaksharut's goal. Only when facing the most overwhelmingly powerful foe does a lhaksharut agree to assist in a task not related to its primary function, and then only to win allies to help it achieve success in an area where the lhaksharut has already met with failure. Even if convinced to undertake such an alliance, a lhaksharut is likely to insist its mission be accomplished first. A creature of pure order, a lhaksharut is incapable of defaulting on a promise made in good faith, but it is aware that not all creatures are so bound. If for some reason the needs of its allies must be put first, a lhaksharut insists on guarantees that its allies will meet their commitments to it once they have what they want.

  In combat, a lhaksharut uses its speed and mobility to get close to targets. A lhaksharut sees groups as imperfect machines, and knows that the best way to overcome them is to disrupt their smooth functioning. While creatures able to directly harm the inevitable are dealt with if necessary, it much prefers to first eliminate healers, scouts, and shield-bearers before tackling powerful fighters or spellcasters. A lhaksharut cannot be taunted or baited into changing its course of action-it is completely emotionless and only cares about the efficiency of its battle plan. It also fights without care for its own survival, trusting that either its regeneration will restore it to life, or a new inevitable will be created to replace it.

  When unaware of a threat to the sanctity of the division of the planes, and not threatened, a lhaksharut can be a surprisingly good conversationalist. They are as likely to be found floating through a void as maintaining any kind of stronghold. Lhaksharuts are aware that the domains they wish to patrol are too vast to be directly viewed with any efficiency. Some lhaksharuts thus forge networks of informants who can patrol the many planes, and send word to the inevitable to alert it of any apparent breaches. The constructs have no other need for the treasure that they gather from transgressors, and sometimes even pay for tips that might lead to a planar infraction. Anyone who might prove to be a valuable informant is treated with respect, and may even be able to gain insights into the planes from the lhaksharut's vast knowledge on the subject, as long as questions never wander into the dangerous territory of combining two planes.

---

# Inevitable, Lhaksharut
This six-armed creature appears to be made of stone. Its lower torso is a collection of whirring rings of metal.
**Source** Bestiary 2 pg. 164
**XP** 307,200

LN Huge outsider (extraplanar, inevitable, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +34
**Aura** _[[spells/Shield of Law|shield of law]]_ (DC 23)

##### Defense

**AC** 36, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+4 deflection, +1 Dex, +5 insight, +18 natural, –2 size)
**hp** 337 (22d10+216); _[[universal monster rules/Regeneration|regeneration]]_ 10 (chaotic)
**Fort** +25, **Ref** +12, **Will** +22
**Defensive Abilities** constructed; **DR** 15/chaotic; **Immune** energy spells; **SR** 31

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** +2 _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _[[items/Weapon/Spear|spear]]_ +32/+27/+22/+17 (3d6+17/x3 plus 1 _[[universal monster rules/Bleed|bleed]]_), +2 _wounding_ _[[items/Weapon/Longsword|longsword]]_ +32 (3d6+12/19–20 plus 1 _bleed_), +2 _wounding_ _[[items/Weapon/Morningstar|morningstar]]_ +32 (3d6+12 plus 1 _bleed_) or 4 slams +30 (2d8+10)
**Ranged** 2 energy bolts +21 (10d6 energy)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[items/Weapon Magic Abilities/Cunning|cunning]]_ reflexes, _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_, perfect prediction, _wounding_ weapons
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 22th; concentration +27)
Constant—_detect chaos_, _detect magic_, _shield of law_ (DC 23), _true seeing_
At will—_[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Sending|sending]]_
3/day—_[[spells/Dictum|dictum]]_ (DC 22), _[[spells/Dimensional Anchor|dimensional anchor]]_ (DC 19), _[[spells/Dimensional Lock|dimensional lock]]_ (DC 23), _[[spells/Disintegrate|disintegrate]]_ (DC 21), _[[spells/Dismissal|dismissal]]_ (DC 20), greater _[[spells/Scrying|scrying]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 20), _[[spells/Wall Of Force|wall of force]]_
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 24)

##### Statistics
**Str** 31, **Dex** 13, **Con** 26, **Int** 14, **Wis** 21, **Cha** 20
**Base Atk** +22; **CMB** +34; **CMD** 50 (can’t be tripped)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +30, Intimidate +30, Knowledge (arcana) +24, Knowledge (geography) +24, Knowledge (planes) +27, Perception +34, Sense Motive +30, Spellcraft +24; **Racial Modifiers** +4 Perception
**Languages** truespeech
**SQ** perfect prediction

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double (+2 _longsword_, +2 _spear_, +2 _morningstar_, other treasure)

### Special Abilities

**_Cunning_ Reflexes (Ex)** A lhaksharut uses its Wisdom modifier, rather than its Dexterity modifier, to determine how many additional attacks of opportunity it gains with the _Combat Reflexes_ feat. For most lhaksharut inevitables, this benefit equates to 5 additional attacks of opportunity per round.

**Energy Bolt (Su)** A lhaksharut can fire bolts of elemental energy from two of its six arms—it never wields weapons in these hands. These attacks have a range increment of 100 feet and deal 10d6 energy damage of the inevitable’s choice (acid, cold, electricity, or fire, chosen for each bolt as it is thrown). It can throw two bolts of energy as a standard action, and cannot attack with these hands when it makes weapon or slam attacks with its other limbs.

**_[[universal monster rules/Immunity|Immunity]]_ to Energy Spells (Ex)** A lhaksharut is immune to any spell or spell-like ability with the acid, cold, electricity, fire, or sonic descriptor that allows _[[universal monster rules/Spell Resistance|spell resistance]]_.

**_Multiweapon Mastery_ (Ex)** A lhaksharut never takes penalties on its attack rolls when fighting with multiple weapons.

**Perfect Prediction (Su)** A lhaksharut gains an insight bonus to AC equal to its Wisdom bonus.

**_Wounding_ Weapons (Su)** Any weapon wielded by a lhaksharut gains the _wounding_ weapon quality as long as it remains in the creature’s _[[spells/Grasp|grasp]]_.

##### Description

A typical lhaksharut is a six-armed construct that appears to be made of a mix of metals and stone. Where a human would have legs, it instead possesses a complex orb of spinning rings similar in shape to an orrery—it is this whirling machine that grants the lhaksharut the ability to fly. Though a lhaksharut has huge, metal wings, they serve as little more than stabilizers when it’s in _[[universal monster rules/Flight|flight]]_. Four of the construct’s arms end in functional hands that it normally uses to carry a mix of weapons. The lhaksharut’s lower two arms hold large, _[[items/Weapon Magic Abilities/Flaming|flaming]]_ metal spheres in their hands—it uses these spheres to generate elemental bolts of energy that it can hurl great distances to damage foes.

Lhaksharuts are tasked with maintaining the separation between different planes of reality, especially the elemental planes. They do not concern themselves with petty trespasses by visitors from one plane to another, nor even the occasional creation of a pocket plane or hijacking of a chunk of one reality to serve as a base within another. What does trouble a lhaksharut is anything that represents a permanent link between planes, or an effort by the denizens of one plane to invade and conquer another. They often find themselves in conflict with the machinations of powerful outsiders who seek to create beachheads on other planes to serve as launching pads for massive incursions.

When possible, a lhaksharut enforces the separation of planes through the simple expedient of _[[items/Weapon Magic Abilities/Smashing|smashing]]_ any device that creates a dangerous breach, or killing any creature that seems determined to mix or _[[spells/Blend|blend]]_ realities. The inevitable does not care why such infractions occur, and is often deaf to any excuse suggesting even a temporary linking of planes is a good idea. However, while singled-mined, a lhaksharut is not mindless or incapable of reason. They are emotionless, but can be negotiated with if a problem cannot be solved by _smashing_ and killing violators.

Rarely, a lhaksharut can even be convinced that maintaining a _[[items/Weapon Magic Abilities/Planar|planar]]_ link is important enough to let the _[[spells/Gate|gate]]_ stand, if only temporarily. In such cases, the lhaksharut always volunteers to _[[npcs/Guard|guard]]_ the portal until the time comes to shut it down. These arrangements must include a detailed explanation on how a desired course of action will directly lead to meeting the lhaksharut’s goal. Only when facing the most overwhelmingly powerful foe does a lhaksharut agree to assist in a task not related to its primary function, and then only to win allies to help it achieve success in an area where the lhaksharut has already met with failure. Even if convinced to undertake such an alliance, a lhaksharut is likely to insist its mission be accomplished first. A creature of pure order, a lhaksharut is incapable of defaulting on a promise made in good faith, but it is aware that not all creatures are so bound. If for some reason the needs of its allies must be put first, a lhaksharut insists on guarantees that its allies will meet their commitments to it once they have what they want.

In combat, a lhaksharut uses its speed and _[[feats/Mobility|mobility]]_ to get close to targets. A lhaksharut sees groups as imperfect machines, and knows that the best way to overcome them is to disrupt their smooth functioning. While creatures able to directly _[[spells/Harm|harm]]_ the inevitable are dealt with if necessary, it much prefers to first eliminate healers, scouts, and shield-bearers before tackling powerful fighters or spellcasters. A lhaksharut cannot be taunted or baited into changing its course of action—it is completely emotionless and only cares about the efficiency of its battle plan. It also fights without care for its own survival, trusting that either its _regeneration_ will restore it to life, or a new inevitable will be created to replace it.

When unaware of a threat to the sanctity of the division of the planes, and not threatened, a lhaksharut can be a surprisingly good conversationalist. They are as likely to be found floating through a void as maintaining any kind of _[[feats/Stronghold|stronghold]]_. Lhaksharuts are aware that the domains they _[[spells/Wish|wish]]_ to patrol are too vast to be directly viewed with any efficiency. Some lhaksharuts thus forge networks of informants who can patrol the many planes, and send word to the inevitable to alert it of any apparent breaches. The constructs have no other need for the treasure that they gather from transgressors, and sometimes even pay for tips that might lead to a _planar_ infraction. Anyone who might prove to be a valuable informant is treated with respect, and may even be able to gain insights into the planes from the lhaksharut’s vast knowledge on the subject, as long as questions never wander into the dangerous territory of combining two planes.