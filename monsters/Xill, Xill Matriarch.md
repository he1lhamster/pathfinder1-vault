---
cssclass: [monsters]
title1: Xill, Xill Matriarch
desc_short: This flame-red, four-armed creature has large mandibles and numerous hornlike
  projections spike from its head.
title2: Xill Matriarch
CR: 9
sources:
- name: Occult Bestiary
  page: 60
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 6400
alignment: LE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 23
  touch: 14
  flat_footed: 19
  components:
    dex: 4
    natural: 7
    shield: 2
HP:
  HP: 123
  long: 13d10+52
saves:
  fort: 12
  ref: 10
  will: 12
speeds:
  base: 40
attacks:
  melee:
  - - text: mwk short sword +19/+14/+9 (1d6+5/19-20)
      entries:
      - - damage: 1d6+5
          crit_range: 19-20
      attack: mwk short sword
      bonus:
      - 19
      - 14
      - 9
    - text: mwk short sword +19/+14 (1d6+5/19-20)
      entries:
      - - damage: 1d6+5
          crit_range: 19-20
      attack: mwk short sword
      bonus:
      - 19
      - 14
    - text: claw +18 (1d4+5 plus grab)
      entries:
      - - damage: 1d4+5
        - effect: grab
      attack: claw
      bonus:
      - 18
    - text: bite +13 (1d3+2 plus paralysis)
      entries:
      - - damage: 1d3+2
        - effect: paralysis
      attack: bite
      bonus:
      - 13
  - - text: 4 claws +18 (1d4+5 plus grab)
      entries:
      - - damage: 1d4+5
        - effect: grab
      count: 4
      attack: claws
      bonus:
      - 18
    - text: bite +18 (1d3+5 plus paralysis)
      entries:
      - - damage: 1d3+5
        - effect: paralysis
      attack: bite
      bonus:
      - 18
  ranged:
  - - text: mwk composite longbow +18/+13/+8 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 18
      - 13
      - 8
    - text: mwk composite longbow +18/+13 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 18
      - 13
  special:
  - implant
  - paralysis (1d4 hours, DC 20)
ability_scores:
  STR: 21
  DEX: 18
  CON: 18
  INT: 15
  WIS: 18
  CHA: 19
BAB: 13
CMB: 18
CMB_other: +22 grapple
CMD: 32
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Improved Two-Weapon Fighting
- name: Lightning Reflexes
- name: Power Attack
- superscripts:
  - OA
  name: Psychic Sensitivity
- name: Two-Weapon Rend
skills:
  Acrobatics: 19
    when jumping: 23
  Bluff: 20
  Intimidate: 20
  Knowledge (arcana): 18
  Knowledge (planes): 18
  Perception: 20
  Sense Motive: 20
  Stealth: 19
languages:
- Common
- Infernal
special_qualities:
- matriarch weapon mastery
- swift planewalk
ecology:
  environment: any (Ethereal Plane)
  organization: solitary or gang (1 plus 2-6 xills)
  treasure_type: standard
  treasure:
  - mwk heavy steel shield
  - 2 mwk short swords
  - 2 mwk composite longbows with 40 arrows
  - other treasure
special_abilities:
  Implant (Ex): As a standard action, a xill matriarch can lay 4d6 eggs in a helpless
    creature. These eggs hatch in 24 hours, at which point the young consume the host
    from within, dealing 1 point of Constitution damage per hour per young until the
    host dies. The young then emerge and planewalk to the Ethereal Plane, if possible.
    A remove disease spell (or similar effect) rids a victim of all implanted eggs
    or active young, or they can be cut out one at a time with successful DC 25 Heal
    checks (each attempt takes 10 minutes). If the healer fails the check, he can
    try again, but each attempt (successful or not) deals 1d4 points of damage to
    the patient. Xill matriarchs can take mental control of creatures in which they
    have implanted eggs as a full-round action. This functions as dominate monster
    (CL 13th) and works at any distance, even between the Ethereal Plane and Material
    Plane. The host takes a -4 penalty on the saving throw to resist the matriarch's
    control. While dominated, the victim is immune to xills' paralysis ability. The
    matriarch can use greater scrying on the dominated victim at will (no saving throw).
    A matriarch can maintain one such link at a time; if she wants to use dominate
    monster or greater scrying on a different creature implanted with her eggs, she
    must end the effects on her current victim (though she can switch back later).
  Matriarch Weapon Mastery (Ex): A xill matriarch never takes penalties on attack
    rolls when fighting with multiple weapons, adds her full Strength modifier on
    damage rolls with off-hand attacks, and treats her claws as primary attacks even
    when also wielding weapons. She is considered to have the Two-Weapon Fighting
    and Double Slice feats for the purpose of fulfilling prerequisites.
  Swift Planewalk (Su): A xill matriarch can shift between the Ethereal Plane and
    the Material Plane, and vice versa, as a move action, and can take a single willing
    or helpless creature with her if she chooses.
desc_long: Xill matriarchs are paragons of their kind, having undergone a ritualistic
  metamorphosis involving the consumption of brain matter from xill egg hosts. The
  matriarchs possess powerful mental abilities, which they use to protect the young
  of their race.

---

# Xill, Xill Matriarch
This flame-red, four-armed creature has large mandibles and numerous hornlike projections spike from its head.
**Source** Occult Bestiary pg. 60
**XP** 6,400

LE Medium outsider (evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 23, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 Dex, +7 natural, +2 _[[spells/Shield|shield]]_)
**hp** 123 (13d10+52)
**Fort** +12, **Ref** +10, **Will** +12

##### Offense
**Speed** 40 ft.
**Melee** mwk _[[items/Weapon/Short sword|short sword]]_ +19/+14/+9 (1d6+5/19–20), mwk _short sword_ +19/+14 (1d6+5/19–20), claw +18 (1d4+5 plus _[[universal monster rules/Grab|grab]]_), bite +13 (1d3+2 plus _[[universal monster rules/Paralysis|paralysis]]_) or 4 claws +18 (1d4+5 plus _grab_), bite +18 (1d3+5 plus _paralysis_)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +18/+13/+8 (1d8+5/×3), mwk _composite longbow_ +18/+13 (1d8+5/×3)
**Special Attacks** implant, _paralysis_ (1d4 hours, DC 20)

##### Statistics
**Str** 21, **Dex** 18, **Con** 18, **Int** 15, **Wis** 18, **Cha** 19
**Base Atk** +13; **CMB** +18 (+22 grapple); **CMD** 32
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Psychic Sensitivity|Psychic Sensitivity]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_
**Skills** Acrobatics +19 (+23 when jumping), Bluff +20, Intimidate +20, Knowledge (arcana) +18, Knowledge (planes) +18, Perception +20, Sense Motive +20, Stealth +19
**Languages** Common, Infernal
**SQ** matriarch weapon mastery, swift planewalk

##### Ecology

**Environment** any (Ethereal Plane)
**Organization** solitary or gang (1 plus 2–6 xills)
**Treasure** standard (mwk _[[items/Shield/Heavy steel shield|heavy steel shield]]_, 2 mwk short swords, 2 mwk composite longbows with 40 arrows, other treasure)

### Special Abilities

**Implant (Ex)** As a standard action, a _[[monsters/Xill|xill]]_ matriarch can lay 4d6 eggs in a _[[conditions/Helpless|helpless]]_ creature. These eggs hatch in 24 hours, at which point the young consume the host from within, dealing 1 point of Constitution damage per hour per young until the host dies. The young then emerge and planewalk to the Ethereal Plane, if possible. A _[[spells/Remove Disease|remove disease]]_ spell (or similar effect) rids a victim of all implanted eggs or active young, or they can be cut out one at a time with successful DC 25 _[[spells/Heal|Heal]]_ checks (each attempt takes 10 minutes). If the _[[npcs/Healer|healer]]_ fails the check, he can try again, but each attempt (successful or not) deals 1d4 points of damage to the patient. _Xill_ matriarchs can take mental control of creatures in which they have implanted eggs as a full-round action. This functions as _[[spells/Dominate Monster|dominate monster]]_ (CL 13th) and works at any distance, even between the Ethereal Plane and Material Plane. The host takes a –4 penalty on the saving throw to resist the matriarch’s control. While dominated, the victim is immune to xills’ _paralysis_ ability. The matriarch can use greater _[[spells/Scrying|scrying]]_ on the dominated victim at will (no saving throw). A matriarch can maintain one such link at a time; if she wants to use _dominate monster_ or greater _scrying_ on a different creature implanted with her eggs, she must end the effects on her current victim (though she can switch back later).

**Matriarch Weapon Mastery (Ex)** A _xill_ matriarch never takes penalties on attack rolls when fighting with multiple weapons, adds her full Strength modifier on damage rolls with off-hand attacks, and treats her claws as primary attacks even when also wielding weapons. She is considered to have the _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_ and _[[feats/Double Slice|Double Slice]]_ feats for the purpose of fulfilling prerequisites.
**Swift Planewalk (Su)** A _xill_ matriarch can shift between the Ethereal Plane and the Material Plane, and vice versa, as a move action, and can take a single willing or _helpless_ creature with her if she chooses.

##### Description

_Xill_ matriarchs are paragons of their kind, having undergone a ritualistic metamorphosis involving the _[[feats/Consumption|consumption]]_ of brain matter from _xill_ egg hosts. The matriarchs possess powerful mental abilities, which they use to protect the young of their race.