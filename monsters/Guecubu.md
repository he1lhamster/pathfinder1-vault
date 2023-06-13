---
cssclass: [monsters]
title1: Guecubu
desc_short: A skeletal carcass pulls itself from the ground, its body formed as much
  from earth and soil as from bones and rotting flesh.
title2: Guecubu
CR: 8
sources:
- name: Bestiary 3
  page: 145
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 4800
alignment: CE
size: Medium
type: undead
subtypes:
- earth
initiative:
  bonus: 8
senses:
  darkvision: 60
  tremorsense: 60
auras:
- name: broken ground
  radius: 30
  DC: 20
AC:
  AC: 21
  touch: 15
  flat_footed: 16
  components:
    dex: 4
    dodge: 1
    natural: 6
HP:
  HP: 104
  long: 11d8+55
  fast_healing: 5
saves:
  fort: 8
  ref: 7
  will: 11
defensive_abilities:
- channel resistance +2
DR:
- amount: 5
  weakness: bludgeoning
immunities:
- electricity
- undead traits
resistances:
  cold: 10
speeds:
  base: 30
  other_semicolon: earth glide
  burrow: 15
attacks:
  melee:
  - - text: bite +14 (1d8+6 plus misfortune)
      entries:
      - - damage: 1d8+6
        - effect: misfortune
      attack: bite
      bonus:
      - 14
    - text: 2 slams +14 (1d6+6 plus misfortune)
      entries:
      - - damage: 1d6+6
        - effect: misfortune
      count: 2
      attack: slams
      bonus:
      - 14
spell_like_abilities:
  entries:
  - name: stone shape
    source: default
    freq: At will
  - name: soften earth and stone
    source: default
    freq: 3/day
  - name: spike growth
    source: default
    freq: 3/day
    DC: 18
  - name: spike stones
    source: default
    freq: 1/day
    DC: 19
  - name: transmute mud to rock
    source: default
    freq: 1/day
    DC: 20
  - name: transmute rock to mud
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 8
    concentration: 13
ability_scores:
  STR: 22
  DEX: 18
  CON:
  INT: 13
  WIS: 18
  CHA: 21
BAB: 8
CMB: 14
CMD: 29
feats:
- name: Combat Expertise
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Spring Attack
- name: Whirlwind Attack
skills:
  Acrobatics: 15
  Knowledge (nature): 12
  Perception: 18
  Sense Motive: 18
  Stealth: 18
languages:
- Abyssal
- Common
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Broken Ground (Su): The ground in a 30-foot radius around a guecubu ripples and
    shudders unnaturally. This transforms the area surrounding a guecubu into difficult
    terrain. A guecubu can move through this area with no penalty. Consecrated ground
    cannot be affected by this ability, nor can any area warded by a magic circle
    against chaos or a magic circle against evil.
  Misfortune (Su): A creature struck by a guecubu must make a DC 20 Will save or become
    permanently cursed with misfortune. The victim of this curse takes a -4 penalty
    on all attack rolls, saving throws, and skill checks, and any critical threat
    against the victim automatically confirms. If a guecubu hits a creature already
    suffering from this curse, the victim must make a DC 20 Will save or be staggered
    for 1 round. This is a curse effect. The save DC is Charisma-based.
desc_long: |-
  Often when a particularly evil criminal is executed, suspicious folk fear that the criminal's remains might rise from death to continue to plague the living. To combat this possibility, many mobs or rural justices take to the practice of burning the bodies, grinding the bones, and scattering the remains in the wild. Yet in the case of particularly evil criminals, even these steps are in vain, for their will is enough to reassemble a body from earth, stone, roots, and plants drawn from the region into which the remains were scattered. Such an undead horror rises as a guecubu, a harbinger of misfortune and vengeance from beyond the grave.

  A newly formed guecubu remembers well how its enemies treated it, and while the undead creature retains none of its previous life's talents, its undead state grants it many new tools to seek revenge with. Typically, a guecubu does not limit its revenge to those directly involved with its execution-entire villages and towns fall victim to its rage. The guecubu's tactics tend toward the subtle, and it seeks to spread misfortune and death on a person-by-person basis, slaying its enemies one at a time until they flee, so that all that remains is a ghost town.

  A guecubu is 6 feet tall and weighs 100 pounds.

---

# Guecubu
A skeletal carcass pulls itself from the ground, its body formed as much from earth and soil as from bones and rotting flesh.
**Source** Bestiary 3 pg. 145
**XP** 4,800
CE Medium undead (earth)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +18
**Aura** _[[conditions/Broken|broken]]_ ground (30 ft., DC 20)

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 104 (11d8+55); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +8, **Ref** +7, **Will** +11
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **DR** 5/bludgeoning; **Immune** electricity, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 15 ft.; _[[universal monster rules/Earth Glide|earth glide]]_
**Melee** bite +14 (1d8+6 plus misfortune), 2 slams +14 (1d6+6 plus misfortune)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +13)
At will—_[[spells/Stone Shape|stone shape]]_
3/day—_[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Spike Growth|spike growth]]_ (DC 18)
1/day—_[[spells/Spike Stones|spike stones]]_ (DC 19), _[[spells/Transmute Mud to Rock|transmute mud to rock]]_ (DC 20), _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ (DC 20)

##### Statistics
**Str** 22, **Dex** 18, **Con** —, **Int** 13, **Wis** 18, **Cha** 21
**Base Atk** +8; **CMB** +14; **CMD** 29
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +15, Knowledge (nature) +12, Perception +18, Sense Motive +18, Stealth +18
**Languages** Abyssal, Common

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Broken_ Ground (Su)** The ground in a 30-foot radius around a _[[monsters/Guecubu|guecubu]]_ ripples and shudders unnaturally. This transforms the area surrounding a _guecubu_ into difficult terrain. A _guecubu_ can move through this area with no penalty. Consecrated ground cannot be affected by this ability, nor can any area warded by a _[[spells/Magic Circle against Chaos|magic circle against chaos]]_ or a _[[spells/Magic Circle against Evil|magic circle against evil]]_.

**Misfortune (Su)** A creature struck by a _guecubu_ must make a DC 20 Will save or become permanently cursed with misfortune. The victim of this curse takes a –4 penalty on all attack rolls, saving throws, and skill checks, and any critical threat against the victim automatically confirms. If a _guecubu_ hits a creature already suffering from this curse, the victim must make a DC 20 Will save or be _[[conditions/Staggered|staggered]]_ for 1 round. This is a curse effect. The save DC is Charisma-based.

##### Description

Often when a particularly evil criminal is executed, suspicious folk _[[universal monster rules/Fear|fear]]_ that the criminal’s remains might rise from death to continue to plague the living. To combat this possibility, many mobs or rural justices take to the practice of _[[items/Weapon Magic Abilities/Burning|burning]]_ the bodies, _[[items/Armor Magic Abilities/Grinding|grinding]]_ the bones, and scattering the remains in the wild. Yet in the case of particularly evil criminals, even these steps are in vain, for their will is enough to reassemble a body from earth, stone, roots, and plants drawn from the region into which the remains were scattered. Such an undead horror rises as a _guecubu_, a harbinger of misfortune and _[[feats/Vengeance|vengeance]]_ from beyond the grave.

A newly formed _guecubu_ remembers well how its enemies treated it, and while the undead creature retains none of its previous life’s talents, its undead state grants it many new tools to seek revenge with. Typically, a _guecubu_ does not limit its revenge to those directly involved with its execution—entire villages and towns fall victim to its _[[spells/Rage|rage]]_. The _guecubu_’s tactics tend toward the subtle, and it seeks to spread misfortune and death on a person-by-person basis, slaying its enemies one at a time until they flee, so that all that remains is a _[[monsters/Ghost|ghost]]_ town.

A _guecubu_ is 6 feet tall and weighs 100 pounds.