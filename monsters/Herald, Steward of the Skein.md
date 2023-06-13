---
cssclass: [monsters]
title1: Herald, Steward of the Skein
desc_short: Skulls adorn the armor of this winged woman. Her helm reveals nothing
  of her features but a pair of glowing eyes.
title2: Steward of the Skein
CR: 15
sources:
- name: Inner Sea Gods
  page: 302
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
- name: 'Pathfinder #44: Trial of the Beast'
  page: 90
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8j5s
XP: 51200
alignment: N
size: Medium
type: outsider
subtypes:
- extraplanar
- herald
- psychopomp
- shapechanger
initiative:
  bonus: 7
senses:
  blindsense: 30
  darkvision: 60
  detect chaos/evil/good/law: true
  spiritsense: true
auras:
- name: fate
  radius: 20
AC:
  AC: 31
  touch: 23
  flat_footed: 27
  components:
    deflection: 4
    dex: 3
    dodge: 1
    insight: 5
    natural: 8
HP:
  HP: 199
  long: 19d10+95
  fast_healing: 5
saves:
  fort: 15
  ref: 20
  will: 22
DR:
- amount: 10
  weakness: adamantine
immunities:
- death effects
- disease
- electricity
- mental control
- poison
- possession
resistances:
  cold: 10
  fire: 10
SR: 26
speeds:
  base: 50
  fly: 150
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 slams +26 (2d10+7 plus gaze)
      entries:
      - - damage: 2d10+7
        - effect: gaze
      count: 2
      attack: slams
      bonus:
      - 26
  special:
  - gaze
  - tugging strands (Fate subdomain, 3/day)
spell_like_abilities:
  entries:
  - name: detect chaos/evil/good/law
    source: default
    freq: Constant
  - name: augury
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: At will
  - name: dancing lights
    source: default
    freq: At will
  - name: death ward
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: disguise self
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 19
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: breath of life
    source: default
    freq: 3/day
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 22
  - name: globe of invulnerability
    source: default
    freq: 3/day
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: greater invisibility
    source: default
    freq: 3/day
    other: self only
  - name: heal
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 3/day
    DC: 21
  - name: limited wish
    source: default
    freq: 3/day
    DC: 23
  - name: plane shift
    source: default
    freq: 3/day
  - name: undeath to death
    source: default
    freq: 3/day
    DC: 22
  - name: wall of force
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 19
    concentration: 25
ability_scores:
  STR: 25
  DEX: 16
  CON: 20
  INT: 18
  WIS: 21
  CHA: 23
BAB: 19
CMB: 26
CMB_other: +28 disarm
CMD: 49
CMD_other: 51 vs. disarm
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Dodge
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Spell Penetration
skills:
  Bluff: 19
  Diplomacy: 16
  Fly: 15
  Handle Animal: 16
  Heal: 27
  Intimidate: 28
  Knowledge (history): 26
  Knowledge (planes): 26
  Knowledge (religion): 26
  Knowledge (nature): 13
  Perception: 27
  Sense Motive: 27
  Stealth: 15
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal
special_qualities:
- change shape (incorporeal form)
- spirit touch
ecology:
  environment: any (Boneyard)
  organization: solitary
  treasure_type: standard
special_abilities:
  Fate Aura (Su): The herald's aura acts as consecrate and grants her a +4 deflection
    bonus to AC, a +5 insight bonus to AC, and a +4 resistance bonus on saving throws.
    Any creature striking the herald from within her aura either is blinded or takes
    1d6 points of Strength damage (herald's choice, Will DC 25 negates). The save
    DC is Charisma-based.
  Gaze (Su): Dazed 2d6 rounds (or stunned if 5 HD or fewer, or held for 2d6 rounds
    if undead), 60 feet; Will DC 25 negates. A creature that succeeds at its save
    is immune to the gaze for 24 hours. This is a mind-affecting effect (or a necromancy
    effect against undead). The save DC is Charisma-based.
  Incorporeal Form (Su): When incorporeal, the herald can use her spell-like abilities
    and gaze attack but can't make slam attacks.
desc_long: The Steward of the Skein is Pharasma's foremost agent, a mighty warrior
  sent to restore the balance of fate, announce auspicious births or deaths, or stem
  a rising tide of undeath. She often appears as an incorporeal shade, making a pronouncement
  and then fading away, though countless creatures over the eons have fallen under
  her armored fists. She stands about 7 feet tall but weighs a mere 200 pounds.

---

# Herald, Steward of the Skein
Skulls adorn the armor of this winged woman. Her helm reveals nothing of her features but a pair of glowing eyes.
**Source** Inner Sea Gods pg. 302, Pathfinder #44: Trial of the Beast pg. 90
**XP** 51,200

N Medium outsider (extraplanar, herald, psychopomp, shapechanger)
**Init** +7; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., detect chaos/evil/good/law, spiritsense; Perception +27
**Aura** fate (20 ft.)

##### Defense

**AC** 31, touch 23, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+4 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +5 insight, +8 natural)
**hp** 199 (19d10+95); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +15, **Ref** +20, **Will** +22
**DR** 10/adamantine; **Immune** death effects, disease, electricity, mental control, poison, _[[spells/Possession|possession]]_; **Resist** cold 10, fire 10; **SR** 26

##### Offense
**Speed** 50 ft., fly 150 ft. (average)
**Melee** 2 slams +26 (2d10+7 plus _[[universal monster rules/Gaze|gaze]]_)
**Special Attacks** _gaze_, tugging strands (Fate subdomain, 3/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +25)
Constant—detect chaos/evil/good/law
At will—_[[spells/Augury|augury]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Disguise Self|disguise self]]_, _[[spells/Major Image|major image]]_ (DC 19), greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 22), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Heal|heal]]_, _[[spells/Hold Monster|hold monster]]_ (DC 21), _[[spells/Limited Wish|limited wish]]_ (DC 23), _[[spells/Plane Shift|plane shift]]_, _[[spells/Undeath to Death|undeath to death]]_ (DC 22), _[[spells/Wall Of Force|wall of force]]_

##### Statistics
**Str** 25, **Dex** 16, **Con** 20, **Int** 18, **Wis** 21, **Cha** 23
**Base Atk** +19; **CMB** +26 (+28 disarm); **CMD** 49 (51 vs. disarm)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Bluff +19, Diplomacy +16, Fly +15, Handle Animal +16, _Heal_ +27, Intimidate +28, Knowledge (history, planes, religion) +26, Knowledge (nature) +13, Perception +27, Sense Motive +27, Stealth +15
**Languages** Abyssal, Celestial, Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[universal monster rules/Incorporeal|incorporeal]]_ form), spirit touch

##### Ecology

**Environment** any (Boneyard)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Fate Aura (Su)** The herald’s aura acts as _[[spells/Consecrate|consecrate]]_ and grants her a +4 _deflection_ bonus to AC, a +5 insight bonus to AC, and a +4 _[[universal monster rules/Resistance|resistance]]_ bonus on saving throws. Any creature striking the herald from within her aura either is _[[conditions/Blinded|blinded]]_ or takes 1d6 points of Strength damage (herald’s choice, Will DC 25 negates). The save DC is Charisma-based.

**_Gaze_ (Su)** _[[conditions/Dazed|Dazed]]_ 2d6 rounds (or _[[conditions/Stunned|stunned]]_ if 5 HD or fewer, or held for 2d6 rounds if undead), 60 feet; Will DC 25 negates. A creature that succeeds at its save is immune to the _gaze_ for 24 hours. This is a mind-affecting effect (or a necromancy effect against undead). The save DC is Charisma-based.

**_Incorporeal_ Form (Su)** When _incorporeal_, the herald can use her _spell-like abilities_ and _gaze_ attack but can’t make slam attacks.

##### Description

The Steward of the Skein is Pharasma’s foremost agent, a mighty warrior sent to restore the balance of fate, announce auspicious births or deaths, or stem a rising tide of undeath. She often appears as an _incorporeal_ shade, making a pronouncement and then fading away, though countless creatures over the eons have _[[monsters/Fallen|fallen]]_ under her armored fists. She stands about 7 feet tall but weighs a mere 200 pounds.