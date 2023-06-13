---
cssclass: [monsters]
title1: Mortic, Relictner
desc_short: This withered, decrepit dwarf has crumbling skin and wears ancient leather
  armor but moves with eerie agility.
title2: Relictner
CR: 12
sources:
- name: "Pathfinder #143: Borne by the Sun's Grace"
  page: 86
  link: https://paizo.com/products/btq01vyh
XP: 19200
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
- mortic
initiative:
  bonus: 2
senses:
  darkvision: 60
  ruin sense: true
auras:
- name: weathering aura
  radius: 60
AC:
  AC: 26
  touch: 13
  flat_footed: 23
  other: +10 vs. environmental effects and traps within bonded ruin
  components:
    armor: 3
    dex: 2
    dodge +10 natural: 1
HP:
  HP: 162
  long: 17d8+85
saves:
  fort: 14
  ref: 9
  will: 10
  other: +10 vs. environmental effects and traps within bonded ruin
defensive_abilities:
- death gasp
- negative energy affinity
DR:
- amount: 5
  weakness: '-'
immunities:
- curses
weaknesses:
- vulnerable to consecration
speeds:
  base: 20
attacks:
  melee:
  - - text: adamantine warhammer +16/+11/+6 (1d8+6/×3)
      entries:
      - - damage: 1d8+6
          crit_multiplier: 3
      attack: adamantine warhammer
      bonus:
      - 16
      - 11
      - 6
  special:
  - fatal accident (1/day, 12d6 or 6d6 plus maneuver, DC 21 half)
spell_like_abilities:
  entries:
  - name: meld into stone
    source: default
    freq: At will
  - name: spike stones
    source: default
    freq: 3/day
    DC: 17
  - name: stone shape
    source: default
    freq: 3/day
  - name: wall of stone
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 20
ability_scores:
  STR: 19
  DEX: 14
  CON: 19
  INT: 15
  WIS: 16
  CHA: 17
BAB: 12
CMB: 16
CMB_other: +20 bull rush, +20 sunder
CMD: 29
CMD_other: 31 vs. bull rush, 31 vs. sunder
feats:
- name: Dodge
- name: Greater Bull Rush
- name: Greater Sunder
- name: Improved Bull Rush
- name: Improved Sunder
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Craft (traps): 20
  Knowledge (engineering): 19
  Perception: 23
  Stealth: 21
languages:
- Common
- Dwarven
special_qualities:
- ruin bond
- unliving nature
ecology:
  environment: any ruins
  organization: solitary, family (2-6), or clan (7-12)
  treasure_type: standard
  treasure:
  - studded leather armor
  - adamantine warhammer
  - other treasure
special_abilities:
  Fatal Accident (Su): Once per day as a standard action, a relictner can focus its
    deteriorating curse to wreak havoc around them. When using this ability, a relictner
    chooses a structure or manufactured object within 60 feet no larger than 15 feet
    by 15 feet, such as a statue, treasure chest, or support pillar. The chosen object
    falls, crumbles, or is otherwise compromised in such a way that it damages any
    creature adjacent to it, dealing 12d6 points of damage to each creature, or half
    as much damage to each creature that succeeds at a DC 21 Reflex save. Alternatively,
    the relictner can deal only 6d6 points of damage and also attempt a ranged bull
    rush, trip, or sunder maneuver check as a free action with a +4 racial bonus against
    each target that fails its Reflex save (sundering in this way deals 6d6 points
    of damage). This attack may deal more or less damage depending on the object chosen
    and the GM's discretion, and it typically creates difficult terrain in the area
    around it. The DC is Charisma-based.
  Ruin Bond (Su: ) A relictner forms a bond with the structure it calls home. Single
    relictners form bonds with huts or houses, families of relictners bond with castles
    or temples, and clans can bond with entire ruined cities. All structures in a
    relictner's bonded ruin lose 1 hit point per day and can be reduced to a minimum
    of 10 hit points. Within its bonded ruin, a relictner gains a +10 bonus to AC
    and on saving throws against environmental effects and any traps. A relictner
    can have only one bonded ruin at a time but can create a new one by living in
    a suitable structure for at least 1 week. A relictner who spends more than 24
    hours away from its bonded ruin becomes fatigued and shaken until it returns to
    the ruin.
  Ruin Sense (Su): A relictner is instantly aware of any creature that dies within
    its bonded ruin, as well as the direction and approximate distance of the dead
    creature.
  Weathering Aura (Su): A relictner radiates an entropic aura of decay and disrepair.
    All objects within 30 feet of a relictner, including held and worn nonmagical
    objects, have their hardness reduced by 5, to a minimum of 0, as long as they
    are within the area of the weathering aura and for 1 round after leaving the area.
    This is a curse effect.
desc_long: |-
  A relictner mortic is two entities in one: a vicious, grasping curse and its half-undead dwarven host. The hosts resemble gaunt, prematurely aged dwarves, their hair gray and ragged, their faces nothing but masses of wrinkles. The curse, however, is a strong and subtle thing, rotting and weathering everything the relictner sees or touches until only ruins are left. Outcast and eternally bitter, most relictners remove themselves to abandoned halls and forgotten ruins that they remake into shrines of mortal despair, filling their new homes with traps and pitfalls to snare the unwary.

   A typical relictner stands about 4 feet tall and weighs 125 pounds.

---

# Mortic, Relictner
This withered, decrepit dwarf has crumbling skin and wears ancient _[[items/Armor/Leather armor|leather armor]]_ but moves with eerie agility.
**Source** Pathfinder #143: Borne by the Sun's _[[spells/Grace|Grace]]_ pg. 86
**XP** 19,200

LE Medium humanoid (dwarf, mortic)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., ruin sense; Perception +23
**Aura** weathering aura (60 ft.)

##### Defense

**AC** 26, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+3 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_ +10 natural); +10 vs. environmental effects and traps within bonded ruin
**hp** 162 (17d8+85)
**Fort** +14, **Ref** +9, **Will** +10; +10 vs. environmental effects and traps within bonded ruin
**Defensive Abilities** death gasp, _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_; **DR** 5/-; **Immune** curses
**Weaknesses** vulnerable to consecration

##### Offense
**Speed** 20 ft.
**Melee** adamantine _[[items/Weapon/Warhammer|warhammer]]_ +16/+11/+6 (1d8+6/×3)
**Special Attacks** fatal accident (1/day, 12d6 or 6d6 plus maneuver, DC 21 half)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +20)
At will—_[[spells/Meld into Stone|meld into stone]]_
 3/day—_[[spells/Spike Stones|spike stones]]_ (DC 17), _[[spells/Stone Shape|stone shape]]_
 1/day—_[[spells/Wall Of Stone|wall of stone]]_

##### Statistics
**Str** 19, **Dex** 14, **Con** 19, **Int** 15, **Wis** 16, **Cha** 17
**Base Atk** +12; **CMB** +16 (+20 bull rush, +20 sunder); **CMD** 29 (31 vs. bull rush, 31 vs. sunder)
**Feats** _Dodge_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Craft (traps) +20, Knowledge (engineering) +19, Perception +23, Stealth +21
**Languages** Common, Dwarven
**SQ** ruin bond, unliving nature

##### Ecology

**Environment** any ruins
**Organization** solitary, family (2–6), or clan (7–12)
**Treasure** standard (_[[items/Armor/Studded leather armor|studded leather armor]]_, adamantine _warhammer_, other treasure)

### Special Abilities

**Fatal Accident (Su)** Once per day as a standard action, a relictner can focus its deteriorating curse to wreak havoc around them. When using this ability, a relictner chooses a structure or manufactured object within 60 feet no larger than 15 feet by 15 feet, such as a _[[spells/Statue|statue]]_, treasure chest, or support pillar. The chosen object falls, crumbles, or is otherwise compromised in such a way that it damages any creature adjacent to it, dealing 12d6 points of damage to each creature, or half as much damage to each creature that succeeds at a DC 21 Reflex save. Alternatively, the relictner can deal only 6d6 points of damage and also attempt a ranged bull rush, _[[universal monster rules/Trip|trip]]_, or sunder maneuver check as a free action with a +4 racial bonus against each target that fails its Reflex save (sundering in this way deals 6d6 points of damage). This attack may deal more or less damage depending on the object chosen and the GM’s discretion, and it typically creates difficult terrain in the area around it. The DC is Charisma-based.

**Ruin Bond (Su**) A relictner forms a bond with the structure it calls home. Single relictners form bonds with huts or houses, families of relictners bond with castles or temples, and clans can bond with entire ruined cities. All structures in a relictner’s bonded ruin lose 1 hit point per day and can be reduced to a minimum of 10 hit points. Within its bonded ruin, a relictner gains a +10 bonus to AC and on saving throws against environmental effects and any traps. A relictner can have only one bonded ruin at a time but can create a new one by living in a suitable structure for at least 1 week. A relictner who spends more than 24 hours away from its bonded ruin becomes _[[conditions/Fatigued|fatigued]]_ and _[[conditions/Shaken|shaken]]_ until it returns to the ruin.

**Ruin Sense (Su)** A relictner is instantly aware of any creature that dies within its bonded ruin, as well as the direction and approximate distance of the dead creature.

**Weathering Aura (Su)** A relictner radiates an entropic aura of decay and disrepair. All objects within 30 feet of a relictner, including held and worn nonmagical objects, have their hardness reduced by 5, to a minimum of 0, as long as they are within the area of the weathering aura and for 1 round after leaving the area. This is a curse effect.

##### Description

A relictner mortic is two entities in one: a _[[items/Weapon Magic Abilities/Vicious|vicious]]_, grasping curse and its half-undead dwarven host. The hosts resemble gaunt, prematurely aged dwarves, their hair _[[monsters/Gray|gray]]_ and ragged, their faces nothing but masses of wrinkles. The curse, however, is a strong and subtle thing, rotting and weathering everything the relictner sees or touches until only ruins are left. Outcast and eternally _[[items/Armor Magic Abilities/Bitter|bitter]]_, most relictners remove themselves to abandoned halls and forgotten ruins that they remake into shrines of mortal despair, filling their new homes with traps and pitfalls to _[[spells/Snare|snare]]_ the unwary.

A typical relictner stands about 4 feet tall and weighs 125 pounds.