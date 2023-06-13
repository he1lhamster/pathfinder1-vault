---
cssclass: [monsters]
title1: Orphne
desc_short: Pale skin and dark features frame this starkly beautiful creature, which
  is surrounded by a palpable aura of death.
title2: Orphne
CR: 4
sources:
- name: Down the Blighted Path
  page: 58
  link: http://paizo.com/products/btpy9j6u?Pathfinder-Module-Down-the-Blighted-Path
XP: 1200
alignment: NE
size: Medium
type: fey
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: desecrating aura
  radius: 30
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    dex: 3
    dodge: 1
    natural: 4
HP:
  HP: 39
  long: 6d6+18
saves:
  fort: 5
  ref: 8
  will: 5
defensive_abilities:
- bone dance
DR:
- amount: 5
  weakness: cold iron
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +5 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: claws
      bonus:
      - 5
  ranged:
  - - text: necrotic ray +6 (2d6 negative energy, plus 2 Con)
      entries:
      - - damage: 2d6
          type: negative energy
        - damage: '2'
          type: Con
      attack: necrotic ray
      bonus:
      - 6
  special:
  - necrotic ray (2d6, DC 15)
spell_like_abilities:
  entries:
  - name: detect undead
    source: default
    freq: Constant
  - name: command undead
    source: default
    freq: At will
  - name: hide from undead
    source: default
    freq: At will
    DC: 15
  - name: animate dead
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 6
    concentration: 8
ability_scores:
  STR: 14
  DEX: 16
  CON: 16
  INT: 15
  WIS: 11
  CHA: 15
BAB: 3
CMB: 5
CMD: 19
feats:
- name: Dodge
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Bluff: 11
  Diplomacy: 11
  Disguise: 8
  Escape Artist: 9
  Intimidate: 5
  Knowledge (arcana): 5
  Knowledge (local): 8
  Knowledge (religion): 5
  Perception: 9
  Sense Motive: 9
  Stealth: 12
languages:
- Common
- Sylvan
- Undercommon
ecology:
  environment: Any underground or urban
  organization: solitary, pair, or wake (3-8)
  treasure_type: standard
special_abilities:
  Bone Dance (Su): As a standard action, an orphne can transform its flesh into ectoplasm,
    becoming incorporeal except for its skeleton. This transformation improves the
    orphne's damage reduction to DR 5/bludgeoning and cold iron, although attacks
    capable of striking incorporeal creatures inflict full damage. The orphne using
    bone dance benefits from its own desecrating aura as if it were undead. An orphne
    may remain in this state for up to 1 hour or until sunrise, whichever comes first,
    and is fatigued afterward for as long as it maintained its bone dance ability.
  Desecrating Aura (Su): Orphne emanate negative energy in a 30-foot-radius that acts
    as a desecrate spell. Undead within this radius gain a +1 profane bonus on attack
    rolls, damage rolls, and saving throws, as well as +1 hit point per Hit Die. The
    saving throw DC of channeled negative energy is increased by 3 within this aura.
    An orphne's desecrating aura can be negated by a dispel evil spell, but an orphne
    can reactivate it on its turn as a move action. A desecrating aura suppresses
    and is suppressed by a consecrate or hallow spell; both effects are negated within
    any overlapping area of effect.
  Necrotic Ray (Su): An orphne can project a ray of pure negative energy as a ranged
    touch attack with a range of 30 feet, inflicting 1d6 points of negative energy
    damage and 1 point of Con damage per 3 Hit Dice (2d6 damage and 2 Con for standard
    orphne).
desc_long: |-
  Often exiled from the First World for their experimentation with necromancy and disregard for boundaries, orphnes are elegant and sadistic fey obsessed with death, pain, and undeath. Blessed with the ability to channel negative energy, their presence sustains the dead and withers living things. They surround themselves with undead chattel of their own creation, and they often serve powerful undead masters in turn.

  Orphne adore art, music, and all the finest luxuries in life, but abuse and suffering truly sustain them. They love to be cared for and appreciated like the beatific creatures they see themselves as, and can quickly turn to anger when not treated as such. Orphne are immeasurably cruel, and without oversight, their lives gravitate towards hurting others for their own amusement, pulling the wings off songbirds or scarring mortal captives in artistic ways. They delight in watching creatures that were once full of life decay into shells of corruption or undeath.

---

# Orphne
Pale skin and dark features frame this starkly beautiful creature, which is surrounded by a palpable aura of death.
**Source** Down the Blighted Path pg. 58
**XP** 1,200

NE Medium fey
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9
**Aura** desecrating aura (30 ft.)

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 39 (6d6+18)
**Fort** +5, **Ref** +8, **Will** +5
**Defensive Abilities** bone dance; **DR** 5/cold iron

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +5 (1d4+2)
**Ranged** necrotic ray +6 (2d6 negative energy, plus 2 Con)
**Special Attacks** necrotic ray (2d6, DC 15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
Constant—_[[spells/Detect Undead|detect undead]]_
At will—_[[spells/Command Undead|command undead]]_, _[[spells/Hide from Undead|hide from undead]]_ (DC 15)
1/day—_[[spells/Animate Dead|animate dead]]_

##### Statistics
**Str** 14, **Dex** 16, **Con** 16, **Int** 15, **Wis** 11, **Cha** 15
**Base Atk** +3; **CMB** +5; **CMD** 19
**Feats** _Dodge_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Bluff +11, Diplomacy +11, Disguise +8, Escape Artist +9, Intimidate +5, Knowledge (arcana) +5, Knowledge (local) +8, Knowledge (religion) +5, Perception +9, Sense Motive +9, Stealth +12
**Languages** Common, Sylvan, Undercommon

##### Ecology

**Environment** Any underground or urban
**Organization** solitary, pair, or wake (3–8)
**Treasure** standard

### Special Abilities

**Bone Dance (Su)** As a standard action, an _[[monsters/Orphne|orphne]]_ can transform its flesh into ectoplasm, becoming _[[universal monster rules/Incorporeal|incorporeal]]_ except for its skeleton. This _[[spells/Transformation|transformation]]_ improves the _orphne_'s _[[universal monster rules/Damage Reduction|damage reduction]]_ to DR 5/bludgeoning and cold iron, although attacks capable of striking _incorporeal_ creatures inflict full damage. The _orphne_ using bone dance benefits from its own desecrating aura as if it were undead. An _orphne_ may remain in this state for up to 1 hour or until sunrise, whichever comes first, and is _[[conditions/Fatigued|fatigued]]_ afterward for as long as it maintained its bone dance ability.

**Desecrating Aura (Su)** _Orphne_ emanate negative energy in a 30-foot-radius that acts as a _[[spells/Desecrate|desecrate]]_ spell. Undead within this radius gain a +1 profane bonus on attack rolls, damage rolls, and saving throws, as well as +1 hit point per Hit Die. The saving throw DC of channeled negative energy is increased by 3 within this aura. An _orphne_'s desecrating aura can be negated by a _[[spells/Dispel Evil|dispel evil]]_ spell, but an _orphne_ can reactivate it on its turn as a move action. A desecrating aura suppresses and is suppressed by a _[[spells/Consecrate|consecrate]]_ or _[[spells/Hallow|hallow]]_ spell; both effects are negated within any overlapping area of effect.

**Necrotic Ray (Su)** An _orphne_ can project a ray of pure negative energy as a ranged touch attack with a range of 30 feet, inflicting 1d6 points of negative energy damage and 1 point of Con damage per 3 Hit Dice (2d6 damage and 2 Con for standard _orphne_).

##### Description

Often exiled from the First World for their experimentation with necromancy and disregard for boundaries, orphnes are elegant and sadistic fey obsessed with death, pain, and undeath. _[[feats/Blessed|Blessed]]_ with the ability to channel negative energy, their presence sustains the dead and withers living things. They surround themselves with undead chattel of their own creation, and they often serve powerful undead masters in turn.

_Orphne_ adore art, music, and all the finest luxuries in life, but abuse and suffering truly sustain them. They love to be cared for and appreciated like the beatific creatures they see themselves as, and can quickly turn to anger when not treated as such. _Orphne_ are immeasurably _[[items/Weapon Magic Abilities/Cruel|cruel]]_, and without oversight, their lives gravitate towards hurting others for their own amusement, pulling the wings off songbirds or scarring mortal captives in artistic ways. They delight in watching creatures that were once full of life decay into shells of corruption or undeath.