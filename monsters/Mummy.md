---
cssclass: [monsters]
title1: Mummy
desc_short: This regal mummy reeks of preservative spices and wears the clothing and
  jewelry of a wealthy pharaoh.
title2: Mythic Mummy
CR: 7
MR: 3
sources:
- name: Mythic Adventures
  page: 211
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 3200
alignment: LE
size: Medium
type: undead
subtypes:
- mythic
initiative:
  bonus: 0
senses:
  darkvision: 60
auras:
- name: despair
  radius: 30
  other:
  - paralyzed for 1d4 rounds
  DC: 16
  DC_type: Will
AC:
  AC: 23
  touch: 10
  flat_footed: 23
  components:
    natural: 13
HP:
  HP: 92
  long: 8d8+56
  fast_healing: 5
saves:
  fort: 4
  ref: 2
  will: 8
DR:
- amount: 5
  weakness: '-'
immunities:
- undead traits
weaknesses:
- vulnerable to fire
speeds:
  base: 20
attacks:
  melee:
  - - text: slam +15 (1d8+12 plus mummy rot)
      entries:
      - - damage: 1d8+12
        - effect: mummy rot
      attack: slam
      bonus:
      - 15
  special:
  - create spawn
  - mythic power (3/day, surge +1d6)
ability_scores:
  STR: 26
  DEX: 10
  CON:
  INT: 6
  WIS: 15
  CHA: 15
BAB: 6
CMB: 14
CMD: 24
feats:
- is_mythic: true
  name: Power Attack
- name: Skill Focus (Perception)
- is_mythic: true
  name: Toughness
- name: Weapon Focus (slam)
skills:
  Perception: 16
  Stealth: 11
languages:
- Common
special_qualities:
- change shape (any humanoid; alter self)
- desert mastery
ecology:
  environment: any
  organization: solitary, warden squad (2-6), or guardian detail (7-12)
  treasure_type: standard
special_abilities:
  Create Spawn (Su): As a swift action, a mythic mummy can expend one use of mythic
    power to transform a slain opponent into a non-mythic mummy with the advanced
    simple template. The new mummy is under the command of the mummy that created
    it, and remains enslaved until the mythic mummy's death, at which time it becomes
    a free-willed creature. The spawn retains none of the abilities it had in life.
  Desert Mastery (Su): A mythic mummy can command earth and sand within 100 feet to
    create a variety of spell-like effects. As a s tandard action, a mummy can reduce
    rock to sand (as transmute rock to mud) or create lifelike shapes made from sand
    (as major image, though these shapes collapse if disbelieved or attacked). The
    mummy can expend one use of mythic power to summon a giant advanced sandman (Bestiary
    2 236). The mummy's caster level equals its Hit Dice for these effects.
  Despair (Su): All creatures within a 30-foot radius that see a mummy must succeed
    at a DC 18 Will save or be paralyzed by fear for 1d4 rounds. A creature only has
    to attempt this save against a particular mummy's despair ability once every 24
    hours. This is a paralysis and mind-affecting fear effect. The save DC is Charisma-based
    and includes a +2 racial bonus.
  Mummy Rot (Su): Curse and disease-slam; save Fort DC 18; onset 1 minute; frequency
    1/day; effect 1d6 Con and 1d6 Cha; cure -. This otherwise functions like standard
    mummy rot. The DC is Charisma-based and includes a +2 racial bonus.
desc_long: A mythic mummy is the preserved and animated remains or royalty-the honored
  dead a common mummy is compelled to protect. Wielding powers over sand and able
  to create new minions to replace the fallen, a mythic mummy is a formidable opponent.
  Its used to absolute obedience from living and undead subjects. If awakened from
  its eternal rest, a mythic mummy uses its magic to appear as it did in life, though
  if angered or surprised it may reveal its undead form.

---

# Mummy
Wrapped from head to toe in ancient strips of moldering linen, this humanoid moves with a shuffling gait.
**Source** Pathfinder RPG Bestiary pg. 110
**XP** 1,600

LE Medium undead
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16
**Aura** despair (30 ft., _[[conditions/Paralyzed|paralyzed]]_ for 1d4 rounds, Will DC 16 negates)

##### Defense

**AC** 20, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+10 natural)
**hp** 60 (8d8+24)
**Fort** +4, **Ref** +2, **Will** +8
**DR** 5/—; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 20 ft.
**Melee** slam +14 (1d8+10 plus _[[curses/Mummy rot|mummy rot]]_)

##### Statistics
**Str** 24, **Dex** 10, **Con** —, **Int** 6, **Wis** 15, **Cha** 15
**Base Atk** +6; **CMB** +13; **CMD** 23
**Feats** _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Perception +16, Stealth +11
**Languages** Common

##### Ecology

**Environment** any
**Organization** solitary, warden squad (2–6), or _[[items/Weapon Magic Abilities/Guardian|guardian]]_ detail (7–12)
**Treasure** standard

### Special Abilities

**Despair (Su)** All creatures within a 30-foot radius that see a _[[monsters/Mummy|mummy]]_ must make a DC 16 Will save or be _paralyzed_ by _[[universal monster rules/Fear|fear]]_ for 1d4 rounds. Whether or not the save is successful, that creature cannot be affected again by the same _mummy_’s despair ability for 24 hours. This is a _[[universal monster rules/Paralysis|paralysis]]_ and a mind-affecting _fear_ affect. The save DC is Charisma-based.

**_Mummy Rot_ (Su)** Curse and disease—slam; save Fort DC 16; onset 1 minute; frequency 1/day; effect 1d6 Con and 1d6 Cha; cure —. _Mummy rot_ is both a curse and disease and can only be cured if the curse is first removed, at which point the disease can be magically removed. Even after the curse element of _mummy rot_ is lifted, a creature suffering from it cannot recover naturally over time. Anyone casting a conjuration (healing) spell on the afflicted creature must succeed on a DC 20 caster level check, or the spell is wasted and the healing has no effect. Anyone who dies from _mummy rot_ turns to dust and cannot be raised without a _[[spells/Resurrection|resurrection]]_ or greater magic. The save DC is Charisma-based.

##### Description

Created to _[[npcs/Guard|guard]]_ the tombs of the honored dead, mummies are ever _[[items/Armor Magic Abilities/Vigilant|vigilant]]_ for those who would _[[spells/Desecrate|desecrate]]_ their _[[items/Weapon Magic Abilities/Sacred|sacred]]_ ground.

Mummies are created through a rather lengthy and gruesome embalming process, during which all of the body’s major organs are removed and replaced with dried herbs and flowers. After this process, the flesh is anointed with _sacred_ oils and wrapped in purified linens. The creator then finishes the ritual with a _[[spells/Create Undead|create undead]]_ spell.

Although most mummies are created merely as guardians and remain loyal to their charge until their _[[spells/Destruction|destruction]]_, certain powerful mummies have much more free will. The majority are at least 10th-level clerics, and are often kings or pharaohs who have _[[items/Weapon Magic Abilities/Called|called]]_ upon dark gods or sinister necromancers to bind their souls to their bodies after death—usually as a means to extend their rule beyond the grave, but at times simply to escape what they _fear_ will be an eternity of torment in their own afterlife.