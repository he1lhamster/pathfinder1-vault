---
cssclass: [monsters]
title1: Paguroida
desc_short: This crab-like creature has the torso and head of a human, one arm ending
  in a massive claw, and another arm wielding a scimitar. It scuttles on six legs
  that emerge from beneath a massive shell with glinting metal and gems embedded into
  its surface.
title2: Paguroida
CR: 9
sources:
- name: 'Pathfinder #122: Into the Shattered Continent'
  page: 86
  link: http://paizo.com/products/btpy9uk0?Pathfinder-Adventure-Path-122-Into-the-Shattered-Continent
XP: 6400
alignment: LN
size: Large
type: monstrous humanoid
subtypes:
- aquatic
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect magic: true
auras:
- name: nondetection
  radius: 30
AC:
  AC: 23
  touch: 15
  flat_footed: 21
  components:
    deflection: 4
    dex: 1
    dodge: 1
    natural: 8
    size: -1
HP:
  HP: 115
  long: 11d10+55
saves:
  fort: 8
  ref: 8
  will: 11
  other: +2 vs. illusion
DR:
- amount: 10
  weakness: magic
resistances:
  cold: 10
  sonic: 10
speeds:
  base: 30
  swim: 20
attacks:
  melee:
  - - text: +2 scimitar +16/+11/+6 (1d6+6/18-20)
      entries:
      - - damage: 1d6+6
          crit_range: 18-20
      attack: +2 scimitar
      bonus:
      - 16
      - 11
      - 6
    - text: claw +16 (1d6+6 plus grab)
      entries:
      - - damage: 1d6+6
        - effect: grab
      attack: claw
      bonus:
      - 16
  ranged:
  - - text: +2 javelin +13/+8/+3 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: +2 javelin
      bonus:
      - 13
      - 8
      - 3
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 9
    concentration: 9
psychic_magic:
  entries:
  - name: detect psychic significance
    PE: 1
  - name: hallucinatory terrain
    DC: 17
    PE: 4
  - name: identify
    PE: 1
  - name: locate object
    PE: 2
  - name: make whole
    PE: 2
  - name: mirage arcana
    DC: 18
    PE: 5
  - name: object reading
    PE: 1
  - name: shatter
    DC: 15
    PE: 2
  - name: sound burst
    DC: 15
    PE: 2
  sources:
  - name: default
    CL: 9
    concentration: 12
  PE: 22
ability_scores:
  STR: 19
  DEX: 13
  CON: 20
  INT: 17
  WIS: 14
  CHA: 10
BAB: 11
CMB: 16
CMB_other: +20 grapple
CMD: 32
CMD_other: 44 vs. trip
feats:
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Quick Draw
- name: Skill Focus (Spellcraft)
- name: Spell Focus (illusion)
skills:
  Diplomacy: 11
  Knowledge (arcana): 14
  Perception: 16
  Spellcraft: 20
  Stealth: 11
  Survival: 16
  Swim: 12
  Use Magic Device: 11
languages:
- Aquan
- Common
special_qualities:
- amphibious
- embedded magic
- undersized weapons
ecology:
  environment: temperate coastlines
  organization: solitary, pair, or enclave (3-8)
  treasure_type: double
  treasure:
  - mwk scimitar
  - 3 mwk javelins
  - 11 caster levels of embedded magic items
special_abilities:
  Embedded Magic (Su): A paguroida can embed a magic item in its shell as a full-round
    action. Once the item is embedded, its magic is channeled into the paguroida's
    body and the item no longer functions normally. It is not considered to be wielded
    or worn, and the item functions as though in an antimagic field while embedded
    in the paguroida's shell. A paguroida that has embedded magic items with a total
    caster level that is at least equal to its Hit Dice (11 for a typical paguroida)
    gains a +4 deflection bonus to its AC and a +2 enhancement bonus on attack and
    damage rolls. A paguroida with embedded magic items whose total caster level is
    at least twice the creature's Hit Dice doubles these bonuses and gains the advanced
    creature simple template (Pathfinder RPG Bestiary 294). A paguroida can remove
    an embedded magic item as a full-round action, adjusting the total caster level
    of its embedded items accordingly. The magic item can then be wielded or worn,
    but it still functions as if in an antimagic field for 1d4 minutes, after which
    time it returns to normal function.
  Nondetection Aura (Su): A paguroida emits an aura out to a radius of 30 feet that
    makes divination difficult. All creatures and objects within the aura are affected
    by a nondetection spell that requires a successful DC 20 caster level check to
    overcome. Creatures or objects revealed to a spellcaster who succeeds at this
    caster level check remain detectable for 24 hours to that spellcaster, even if
    the creature or item exits and reenters the aura. A paguroida automatically succeeds
    at the caster level check to overcome this effect when using its constant detect
    magic spell-like ability.
  Psychic Magic (Su): A paguroida begins each day with a number of PE equal to twice
    the total caster level of all magic items embedded in its shell. (The statistics
    above assume that the paguroida has items with a total caster level equal to 11
    embedded in its shell.) Removing or adding a magic item after the start of the
    day does not increase or reduce this number until the next time the paguroida
    regains PE.
  Undersized Weapons (Ex): Although a paguroida is Large, its upper torso is the same
    size as that of a Medium humanoid. As a result, it wields weapons as if it were
    one size category smaller than its actual size (Medium for most paguroidas). Additionally,
    because it has only one hand-its other appendage is tipped with a massive pincer-a
    paguroida can wield only a shield or a light or one-handed weapon at a given time.
desc_long: Believed to have been created by the aboleths in ages long past as part
  of the alghollthus' experiments on the murajau, paguroidas are reclusive, hermit
  crab-like monstrous humanoids who live in hidden grottoes and seaside estuaries,
  typically on isolated or remote coastlines. One of their upper limbs terminates
  in a humanoid hand, while the other ends in a large pincer capable of gripping and
  crushing prey. A paguroida's face is similar to that of a crab, with protruding
  eyestalks and a wide mandible-filled mouth, though its torso is distinctly humanoid
  in shape and size. A typical paguroida stands 7 feet tall and weighs 1,200 pounds.

---

# Paguroida
This crab-like creature has the torso and head of a human, one arm ending in a massive claw, and another arm wielding a _[[items/Weapon/Scimitar|scimitar]]_. It scuttles on six legs that emerge from beneath a massive shell with glinting metal and gems embedded into its surface.
**Source** Pathfinder #122: Into the Shattered Continent pg. 86
**XP** 6,400

LN Large monstrous humanoid (aquatic)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +16
**Aura** _[[spells/Nondetection|nondetection]]_ (30 ft.)

##### Defense

**AC** 23, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 deflection, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural, –1 size)
**hp** 115 (11d10+55)
**Fort** +8, **Ref** +8, **Will** +11; +2 vs. illusion
**DR** 10/magic; **Resist** cold 10, sonic 10

##### Offense
**Speed** 30 ft., swim 20 ft.
**Melee** +2 _scimitar_ +16/+11/+6 (1d6+6/18–20), claw +16 (1d6+6 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** +2 _[[items/Weapon/Javelin|javelin]]_ +13/+8/+3 (1d6+6)
**Space** 10 ft., **Reach** 5 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +9)
Constant—_detect magic_
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 9th; concentration +12)
22 PE—_[[spells/Detect _[[classes/Psychic|Psychic]]_ Significance|detect _psychic_ significance]]_ (1 PE), _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 17, 4 PE), _[[spells/Identify|identify]]_ (1 PE), _[[spells/Locate Object|locate object]]_ (2 PE), _[[spells/Make Whole|make whole]]_ (2 PE), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 18, 5 PE), _[[spells/Object Reading|object reading]]_ (1 PE), _[[spells/Shatter|shatter]]_ (DC 15, 2 PE), _[[spells/Sound Burst|sound burst]]_ (DC 15, 2 PE)

##### Statistics
**Str** 19, **Dex** 13, **Con** 20, **Int** 17, **Wis** 14, **Cha** 10
**Base Atk** +11; **CMB** +16 (+20 grapple); **CMD** 32 (44 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Skill Focus|Skill Focus]]_ (Spellcraft), _[[feats/Spell Focus|Spell Focus]]_ (illusion)
**Skills** Diplomacy +11, Knowledge (arcana) +14, Perception +16, Spellcraft +20, Stealth +11, Survival +16, Swim +12, Use Magic Device +11
**Languages** Aquan, Common
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, embedded magic, _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** temperate coastlines
**Organization** solitary, pair, or enclave (3-8)
**Treasure** double (mwk _scimitar_, 3 mwk javelins, 11 caster levels of embedded magic items)

### Special Abilities

**Embedded Magic (Su)** A _[[monsters/Paguroida|paguroida]]_ can embed a magic item in its shell as a full-round action. Once the item is embedded, its magic is channeled into the _paguroida_’s body and the item no longer functions normally. It is not considered to be wielded or worn, and the item functions as though in an _[[spells/Antimagic Field|antimagic field]]_ while embedded in the _paguroida_’s shell. A _paguroida_ that has embedded magic items with a total caster level that is at least equal to its Hit Dice (11 for a typical _paguroida_) gains a +4 _deflection_ bonus to its AC and a +2 enhancement bonus on attack and damage rolls. A _paguroida_ with embedded magic items whose total caster level is at least twice the creature’s Hit Dice doubles these bonuses and gains the advanced creature simple template (Pathfinder RPG Bestiary 294). A _paguroida_ can remove an embedded magic item as a full-round action, adjusting the total caster level of its embedded items accordingly. The magic item can then be wielded or worn, but it still functions as if in an _antimagic field_ for 1d4 minutes, after which time it returns to normal function.

**_Nondetection_ Aura (Su)** A _paguroida_ emits an aura out to a radius of 30 feet that makes _[[spells/Divination|divination]]_ difficult. All creatures and objects within the aura are affected by a _nondetection_ spell that requires a successful DC 20 caster level check to overcome. Creatures or objects revealed to a spellcaster who succeeds at this caster level check remain detectable for 24 hours to that spellcaster, even if the creature or item exits and reenters the aura. A _paguroida_ automatically succeeds at the caster level check to overcome this effect when using its constant _detect magic_ spell-like ability.

**_Psychic Magic_ (Su)** A _paguroida_ begins each day with a number of PE equal to twice the total caster level of all magic items embedded in its shell. (The statistics above assume that the _paguroida_ has items with a total caster level equal to 11 embedded in its shell.) Removing or adding a magic item after the start of the day does not increase or reduce this number until the next time the _paguroida_ regains PE.

**_Undersized Weapons_ (Ex)** Although a _paguroida_ is Large, its upper torso is the same size as that of a _[[classes/Medium|Medium]]_ humanoid. As a result, it wields weapons as if it were one size category smaller than its actual size (_Medium_ for most paguroidas). Additionally, because it has only one hand—its other appendage is tipped with a massive pincer—a _paguroida_ can wield only a _[[spells/Shield|shield]]_ or a light or one-handed weapon at a given time.

##### Description

Believed to have been created by the aboleths in ages long past as part of the alghollthus’ experiments on the _[[monsters/Murajau|murajau]]_, paguroidas are reclusive, _[[npcs/Hermit|hermit]]_ crab–like monstrous humanoids who live in hidden grottoes and seaside estuaries, typically on isolated or remote coastlines. One of their upper limbs terminates in a humanoid hand, while the other ends in a large pincer capable of gripping and crushing prey. A _paguroida_’s face is similar to that of a crab, with protruding eyestalks and a wide mandible-filled mouth, though its torso is distinctly humanoid in shape and size. A typical _paguroida_ stands 7 feet tall and weighs 1,200 pounds.