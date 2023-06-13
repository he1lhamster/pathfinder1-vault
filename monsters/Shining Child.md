---
cssclass: [monsters]
title1: Shining Child
desc_short: Surrounded by a nimbus of near-blinding light, this strange creature looks
  something like an emaciated child with clawed hands.
title2: Shining Child
CR: 12
sources:
- name: Bestiary 2
  page: 245
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 19200
alignment: CE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 120
auras:
- name: blinding light
  radius: 60
AC:
  AC: 28
  touch: 21
  flat_footed: 24
  components:
    deflection: 7
    dex: 3
    dodge: 1
    natural: 7
HP:
  HP: 152
  long: 16d10+64
saves:
  fort: 14
  ref: 10
  will: 10
immunities:
- blindness
- fire
- poison
resistances:
  cold: 10
  sonic: 10
speeds:
  base: 30
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 touches +19 (4d10 fire plus burning touch)
      entries:
      - - damage: 4d10
          type: fire
        - effect: burning touch
      count: 2
      attack: touches
      bonus:
      - 19
  ranged:
  - - text: searing ray +19 touch (10d6 fire)
      entries:
      - - damage: 10d6
          type: fire
      attack: searing ray
      bonus:
      - 19
      touch: true
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: light
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 20
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 20
  - name: rainbow pattern
    source: default
    freq: 3/day
    DC: 22
  - name: spell turning
    source: default
    freq: 3/day
  - name: sunbeam
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  - name: scintillating pattern
    source: default
    freq: 1/day
    DC: 25
  - name: screen
    source: default
    freq: 1/day
    DC: 25
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 12
    concentration: 19
ability_scores:
  STR: 10
  DEX: 17
  CON: 18
  INT: 15
  WIS: 11
  CHA: 24
BAB: 16
CMB: 16
CMD: 37
feats:
- name: Ability Focus (blinding light)
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
- name: Skill Focus (Perception)
- name: Spring Attack
- name: Weapon Finesse
skills:
  Bluff: 26
  Diplomacy: 23
  Fly: 11
  Intimidate: 26
  Knowledge (arcana): 21
  Knowledge (planes): 21
  Perception: 25
  Spellcraft: 21
  Use Magic Device: 26
languages:
- telepathy 120 ft.
special_qualities:
- radiant armor
ecology:
  environment: any land (extraplanar)
  organization: solitary, visitation (2-9), or incursion (11-20)
  treasure_type: none
special_abilities:
  Blinding Light (Ex): A shining child can radiate a 60-foot-radius aura of blinding
    light as a free action. Creatures within the affected area must succeed on a DC
    25 Fortitude save or be permanently blinded. A creature that successfully saves
    cannot be affected again by the same shining child's aura for 24 hours. The save
    is Constitution-based.
  Burning Touch (Su): A shining child corrupts the positive energy within a living
    creature into an unnatural burning light. For the next 5 rounds after a successful
    touch attack by a shining child, the target takes 2d6 points of fire damage. The
    burning light can be “extinguished” by casting darkness or deeper darkness on
    the target, or by entering an area of natural darkness (not counting the light
    from the burning target).
  Radiant Armor (Su): The light that surrounds a shining child grants a deflection
    bonus to its AC equal to its Charisma bonus. The bonus is negated as long as the
    shining child is in the area of effect of a spell with the darkness descriptor
    that is at least 3rd level.
  Searing Ray (Su): A shining child's primary attack is a ray of searing light. This
    attack has a range of 120 feet. The ray deals double damage to undead creatures.
desc_long: |-
  Creatures of burning light and strange geometry, shining children are a terror to behold. Beyond the flares of energy that constantly burst from their forms (particularly in beam-like gouts from their eyes and mouths), the creatures are vaguely humanoid, with strange hands that each bear four fingers. Occasionally summoned by powerful wizards in search of rare arcane knowledge, the shining children (who disdain individual names) communicate via telepathy, a psychic roar like metal tearing that sometimes resolves into strained and raspy words.

  Though they harbor many secrets, their greatest secret may be their own origin. Numerous theories abound-that the shining children are beings from another dimension, avatars of a dying star grown sentient, or creatures of light battling living darkness at the edge of reality. A shining child stands just over 4-1/2 feet tall and weighs 85 pounds.

---

# Shining Child
Surrounded by a nimbus of near-blinding light, this strange creature looks something like an emaciated child with clawed hands.
**Source** Bestiary 2 pg. 245
**XP** 19,200
CE Medium outsider (evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +25
**Aura** _[[feats/Blinding Light|blinding light]]_ (60 feet)

##### Defense

**AC** 28, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+7 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 152 (16d10+64)
**Fort** +14, **Ref** +10, **Will** +10
**Immune** blindness, fire, poison; **Resist** cold 10, sonic 10

##### Offense
**Speed** 30 ft., fly 50 ft. (perfect)
**Melee** 2 touches +19 (4d10 fire plus _[[items/Weapon Magic Abilities/Burning|burning]]_ touch)
**Ranged** searing ray +19 touch (10d6 fire)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +19)
At will—greater teleport (self plus 50 lbs. of objects only), light, _[[spells/Major Image|major image]]_ (DC 20)
3/day—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Mirage Arcana|mirage arcana]]_ (DC 20), _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 22), _[[spells/Spell Turning|spell turning]]_, _[[spells/Sunbeam|sunbeam]]_, _[[spells/Wall Of Force|wall of force]]_
1/day—_[[spells/Scintillating Pattern|scintillating pattern]]_ (DC 25), screen (DC 25), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 25)

##### Statistics
**Str** 10, **Dex** 17, **Con** 18, **Int** 15, **Wis** 11, **Cha** 24
**Base Atk** +16; **CMB** +16; **CMD** 37
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_blinding light_), _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +26, Diplomacy +23, Fly +11, Intimidate +26, Knowledge (arcana) +21, Knowledge (planes) +21, Perception +25, Spellcraft +21, Use Magic Device +26
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 120 ft.
**SQ** _[[items/Armor Magic Abilities/Radiant|radiant]]_ armor

##### Ecology

**Environment** any land (extraplanar)
**Organization** solitary, visitation (2–9), or incursion (11–20)
**Treasure** none

### Special Abilities

**_Blinding Light_ (Ex) **A _[[monsters/Shining Child|shining child]]_ can radiate a 60-foot-radius aura of _blinding light_ as a free action. Creatures within the affected area must succeed on a DC 25 Fortitude save or be permanently _[[conditions/Blinded|blinded]]_. A creature that successfully saves cannot be affected again by the same _shining child_’s aura for 24 hours. The save is Constitution-based.

**_Burning_ Touch (Su)** A _shining child_ corrupts the positive energy within a living creature into an unnatural _burning_ light. For the next 5 rounds after a successful touch attack by a _shining child_, the target takes 2d6 points of fire damage. The _burning_ light can be “extinguished” by casting _[[spells/Darkness|darkness]]_ or _[[spells/Deeper Darkness|deeper darkness]]_ on the target, or by entering an area of natural _darkness_ (not counting the light from the _burning_ target).

**_Radiant_ Armor (Su)** The light that surrounds a _shining child_ grants a _deflection_ bonus to its AC equal to its Charisma bonus. The bonus is negated as long as the _shining child_ is in the area of effect of a spell with the _darkness_ descriptor that is at least 3rd level.
**Searing Ray (Su)** A _shining child_’s primary attack is a ray of _[[spells/Searing Light|searing light]]_. This attack has a range of 120 feet. The ray deals double damage to undead creatures.

##### Description

Creatures of _burning_ light and strange geometry, shining children are a terror to behold. Beyond the flares of energy that constantly burst from their forms (particularly in beam-like gouts from their eyes and mouths), the creatures are vaguely humanoid, with strange hands that each bear four fingers. Occasionally summoned by powerful wizards in search of rare arcane knowledge, the shining children (who disdain individual names) communicate via _telepathy_, a _[[classes/Psychic|psychic]]_ roar like metal tearing that sometimes resolves into strained and raspy words.

Though they harbor many secrets, their greatest secret may be their own origin. Numerous theories abound—that the shining children are beings from another dimension, avatars of a _[[conditions/Dying|dying]]_ star grown sentient, or creatures of light battling living _darkness_ at the edge of reality. A _shining child_ stands just over 4-1/2 feet tall and weighs 85 pounds.