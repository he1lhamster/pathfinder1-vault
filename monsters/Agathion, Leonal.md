---
cssclass: [monsters]
title1: Agathion, Leonal
desc_short: 'This lion-headed humanoid has golden fur, sharp teeth, and long cat-like
  claws on its hands and feet. '
title2: Leonal
CR: 12
sources:
- name: Bestiary 2
  page: 19
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 19200
alignment: NG
size: Medium
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: protective aura
  radius: 20
AC:
  AC: 27
  touch: 14
  flat_footed: 23
  other: +4 deflection vs. evil
  components:
    dex: 3
    dodge: 1
    natural: 13
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 14
  ref: 12
  will: 6
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 10
  weakness: evil and silver
immunities:
- electricity
- petrification
resistances:
  cold: 10
  sonic: 10
SR: 23
speeds:
  base: 60
attacks:
  melee:
  - - text: bite +23 (1d8+8 plus grab)
      entries:
      - - damage: 1d8+8
        - effect: grab
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 2
      attack: claws
      bonus:
      - 23
  special:
  - roar
  - pounce
  - rake (2 claws +23, 1d6+8)
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
  - name: fireball
    source: default
    freq: At will
    DC: 15
  - name: hold monster
    source: default
    freq: At will
    DC: 7
  - name: cure critical wounds
    source: default
    freq: 3/day
  - name: neutralize poison
    source: default
    freq: 3/day
  - name: remove disease
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 16
ability_scores:
  STR: 27
  DEX: 17
  CON: 20
  INT: 14
  WIS: 14
  CHA: 15
BAB: 14
CMB: 22
CMB_other: +26 grapple
CMD: 36
feats:
- name: Ability Focus (roar)
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Spring Attack
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Acrobatics: 24
    jump: 36
  Handle Animal: 19
  Intimidate: 19
  Knowledge (any one): 19
  Perception: 19
  Sense Motive: 19
  Spellcraft: 16
  Stealth: 24
  _racial_mods:
    Acrobatics:
      _: 4
    Stealth:
      _: 4
languages:
- Celestial
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- lay on hands (7d6, 9/day, as a 14th-level paladin)
ecology:
  environment: any land (Nirvana)
  organization: solitary, pair, or pride (3-8)
  treasure_type: standard
special_abilities:
  Protective Aura (Su): Against attacks made or effects created by evil creatures,
    this ability provides a +4 deflection bonus to AC and a +4 resistance bonus on
    saving throws to anyone within 20 feet of the leonal. Otherwise, it functions
    as a magic circle against evil effect and a lesser globe of invulnerability, both
    with a radius of 20 feet (caster level equals leonal's HD). The defensive benefits
    from the circle are not included in a leonal's stat block.
  Roar (Su): Up to three times per day, a leonal can emit a powerful roar as a standard
    action. Each roar affects a 60-foot cone with the effects of a holy word spell
    and also deals 2d6 points of sonic damage to all creatures in the area (DC 21
    Fortitude negates). This is a sonic effect. The save DC is Charisma-based.
desc_long: |-
  A leonal is a lion-like agathion, noble and fierce. Though gentle with their families and patient with strangers on their home plane, in battle leonals are deadly foes of evil and cruelty. They hunt fiends and other evil monsters, silently tailing their prey until they find the right time to leap and slash. Leonals pride themselves on their hunting prowess, and few land creatures can match their speed. Although capable of using weapons, the majority of leonals prefer to battle evil with tooth and claw. 

  Leonals like their battles to be straightforward affairs. They begin with a roar to put their foes off balance, then follow up with claw and bite attacks. They closely coordinate with others in their pride, watching one another's flanks and setting up devastating attacks. They mainly use their magical abilities against large numbers of weaker foes and against those they need to capture or incapacitate without dealing harm to them. 

  Leonals stand 6 feet tall and weigh 270 pounds on average. Males usually have manes of either dark gold or black hair, which may only surround the head or may extend onto the shoulders and chest. Female leonals do not have manes, but may have longer hair on the back of the neck.

---

# Agathion, Leonal
This lion-headed humanoid has golden fur, sharp teeth, and long cat-like claws on its hands and feet.

**Source** Bestiary 2 pg. 19
**XP** 19,200

NG Medium outsider (agathion, extraplanar, good)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +19
**Aura** protective aura (20 ft.)

##### Defense

**AC** 27, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +13 natural) (+4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 147 (14d10+70)
**Fort** +14, **Ref** +12, **Will** +6; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 10/evil and silver; **Immune** electricity, petrification; **Resist** cold 10, sonic 10; **SR** 23

##### Offense
**Speed** 60 ft.
**Melee** bite +23 (1d8+8 plus _[[universal monster rules/Grab|grab]]_), 2 claws +23 (1d6+8)
**Special Attacks** roar, _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +23, 1d6+8)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +16)
Constant—_[[spells/Speak with Animals|speak with animals]]_ 
At will—_[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Fireball|fireball]]_ (DC 15), _[[spells/Hold Monster|hold monster]]_ (DC 7) 
3/day—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Wall Of Force|wall of force]]_ 
1/day—_[[spells/Heal|heal]]_

##### Statistics
**Str** 27, **Dex** 17, **Con** 20, **Int** 14, **Wis** 14, **Cha** 15
**Base Atk** +14; **CMB** +22 (+26 grapple); **CMD** 36
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (roar), _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw)
**Skills** Acrobatics +24 (+36 _[[spells/Jump|jump]]_), Handle Animal +19, Intimidate +19, Knowledge (any one) +19, Perception +19, Sense Motive +19, Spellcraft +16, Stealth +24; **Racial Modifiers** +4 Acrobatics, +4 Stealth
**Languages** Celestial, Draconic, Infernal; _speak with animals_, truespeech
**SQ** lay on hands (7d6, 9/day, as a 14th-level _[[classes/Paladin|paladin]]_)

##### Ecology

**Environment** any land (Nirvana)
**Organization** solitary, pair, or pride (3–8)
**Treasure** standard

### Special Abilities

**Protective Aura (Su)** Against attacks made or effects created by evil creatures, this ability provides a +4 _deflection_ bonus to AC and a +4 _resistance_ bonus on saving throws to anyone within 20 feet of the leonal. Otherwise, it functions as a _[[spells/Magic Circle against Evil|magic circle against evil]]_ effect and a lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, both with a radius of 20 feet (caster level equals leonal’s HD). The defensive benefits from the circle are not included in a leonal’s stat block.

**Roar (Su)** Up to three times per day, a leonal can emit a powerful roar as a standard action. Each roar affects a 60-foot cone with the effects of a _[[spells/Holy Word|holy word]]_ spell and also deals 2d6 points of sonic damage to all creatures in the area (DC 21 Fortitude negates). This is a sonic effect. The save DC is Charisma-based.

##### Description

A leonal is a lion-like agathion, noble and fierce. Though gentle with their families and patient with strangers on their home plane, in battle leonals are _[[items/Weapon Magic Abilities/Deadly|deadly]]_ foes of evil and _[[feats/Cruelty|cruelty]]_. They hunt fiends and other evil monsters, silently tailing their prey until they find the right time to leap and slash. Leonals pride themselves on their hunting prowess, and few land creatures can match their speed. Although capable of using weapons, the majority of leonals prefer to battle evil with tooth and claw.

Leonals like their battles to be straightforward affairs. They begin with a roar to put their foes off balance, then follow up with claw and bite attacks. They closely coordinate with others in their pride, watching one another’s flanks and setting up devastating attacks. They mainly use their magical abilities against large numbers of weaker foes and against those they need to capture or incapacitate without dealing _[[spells/Harm|harm]]_ to them.

Leonals stand 6 feet tall and weigh 270 pounds on average. Males usually have manes of either dark gold or black hair, which may only surround the head or may extend onto the shoulders and chest. Female leonals do not have manes, but may have longer hair on the back of the neck.