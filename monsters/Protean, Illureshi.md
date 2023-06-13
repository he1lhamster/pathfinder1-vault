---
cssclass: [monsters]
title1: Protean, Illureshi
desc_short: This anemic protean wears a wizard's robe and garish jewelry.
title2: Illureshi
CR: 9
sources:
- name: Concordance of Rivals
  page: 57
  link: https://paizo.com/products/btq01x4d?Pathfinder-Campaign-Setting-Concordance-of-Rivals
XP: 6400
alignment: CN
size: Medium
type: outsider
subtypes:
- chaotic
- extraplanar
- protean
- shapechanger
initiative:
  bonus: 8
senses:
  blindsense: 30
  darkvision: 60
  arcane sight: true
  detect law: true
auras:
- name: spellwarp aura
  radius: 30
AC:
  AC: 23
  touch: 14
  flat_footed: 19
  components:
    dex: 4
    natural: 9
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 8
  ref: 12
  will: 13
defensive_abilities:
- amorphous anatomy
- freedom of movement
DR:
- amount: 10
  weakness: lawful
immunities:
- acid
- polymorph
resistances:
  electricity: 10
  sonic: 10
SR: 20
speeds:
  base: 30
  fly: 30
  fly_maneuverability: perfect
  swim: 30
attacks:
  melee:
  - - text: bite +15 (2d6+3)
      entries:
      - - damage: 2d6+3
      attack: bite
      bonus:
      - 15
    - text: 2 claws +15 (1d8+3)
      entries:
      - - damage: 1d8+3
      count: 2
      attack: claws
      bonus:
      - 15
    - text: tail +15 (1d8+1 plus grab)
      entries:
      - - damage: 1d8+1
        - effect: grab
      attack: tail
      bonus:
      - 15
  special:
  - constrict (1d8+3)
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: dispel magic
    source: default
    freq: At will
    DC: 17
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: major creation
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 19
  - name: chaos hammer
    source: default
    freq: 3/day
    DC: 18
  - name: break enchantment
    source: default
    freq: 1/day
  - name: plane shift
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 10
    concentration: 14
spells:
  entries:
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 16
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: cultural adaptationUI
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 10
    slots:
      3: 3
      2: 5
      1: 6
      0: at-will
ability_scores:
  STR: 17
  DEX: 18
  CON: 18
  INT: 23
  WIS: 16
  CHA: 19
BAB: 12
CMB: 15
CMD: 29
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Craft Wondrous Item
- name: Improved Initiative
- name: Iron Will
- name: Scribe Scroll
- name: Spell Penetration
skills:
  Acrobatics: 16
  Bluff: 19
  Diplomacy: 16
  Fly: 19
  Knowledge (any two): 18
  Knowledge (arcana): 21
  Knowledge (planes): 21
  Perception: 18
  Spellcraft: 21
  Swim: 23
  Use Magic Device: 19
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Protean
- tongues
special_qualities:
- change shape (greater polymorph)
ecology:
  environment: any (Maelstrom)
  organization: solitary or ouroboros (3-5)
  treasure_type: double
special_abilities:
  Prehensile Tail (Ex): An illureshi can't wield weapons with its tail, but can use
    its tail to grab unattended items within 10 feet or stowed objects carried on
    its person as a swift action. It can hold such objects with its tail. The only
    items it can manipulate with its tail are wands, which it can activate as a move
    action.
  Spellwarp Aura (Su): Once per round, if a creature casts a spell or spell-like ability
    within the illureshi's aura, the protean can attempt an opposed caster level check
    to redirect the effect to another legal target within range.
  Spellcasting: An illureshi casts spells as a 6th-level sorcerer. It does not gain
    access to other sorcerer abilities.
desc_long: Illureshis embody chaos through sorcery, traveling the planes as chatty
  and whimsical masters of arcane magic.

---

# Protean, Illureshi
This anemic protean wears a _[[classes/Wizard|wizard]]_’s robe and garish _[[items/Mundane/Jewelry|jewelry]]_.
**Source** Concordance of Rivals pg. 57
**XP** 6,400

CN Medium outsider (chaotic, extraplanar, protean, shapechanger)
**Init** +8; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Detect Law|detect law]]_; Perception +18
**Aura** spellwarp aura (30 ft.)

##### Defense

**AC** 23, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 Dex, +9 natural)
**hp** 114 (12d10+48)
**Fort** +8, **Ref** +12, **Will** +13
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_ anatomy, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 10/lawful; **Immune** acid, _[[spells/Polymorph|polymorph]]_; **Resist** electricity 10, sonic 10; **SR** 20

##### Offense
**Speed** 30 ft., fly 30 ft. (perfect), swim 30 ft.
**Melee** bite +15 (2d6+3), 2 claws +15 (1d8+3), tail +15 (1d8+1 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_arcane sight_, _detect law_, _[[spells/Tongues|tongues]]_
 At will—_[[spells/Dispel Magic|dispel magic]]_ (DC 17), greater teleport (self plus 50 lbs. of objects only), _[[spells/Major Creation|major creation]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 19)
 3/day—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 18) 
1/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Plane Shift|plane shift]]_ (DC 21)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known** (CL 6th; concentration +10)
3rd (3/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 16)
 2nd (5/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
 1st (6/day)—cultural adaptationUI, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_
 0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Arcane Mark|arcane mark]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 17, **Dex** 18, **Con** 18, **Int** 23, **Wis** 16, **Cha** 19
**Base Atk** +12; **CMB** +15; **CMD** 29 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Acrobatics +16, Bluff +19, Diplomacy +16, Fly +19, Knowledge (any two) +18, Knowledge (arcana) +21, Knowledge (planes) +21, Perception +18, Spellcraft +21, Swim +23, Use Magic Device +19
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Protean; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (greater _polymorph_)

##### Ecology

**Environment** any (Maelstrom)
**Organization** solitary or _[[monsters/Ouroboros|ouroboros]]_ (3–5)
**Treasure** double

### Special Abilities

**_[[items/Weapon Magic Abilities/Prehensile|Prehensile]]_ Tail (Ex)** An illureshi can’t wield weapons with its tail, but can use its tail to _grab_ unattended items within 10 feet or stowed objects carried on its person as a swift action. It can hold such objects with its tail. The only items it can manipulate with its tail are wands, which it can activate as a move action.
 **Spellwarp Aura (Su)** Once per round, if a creature casts a spell or spell-like ability within the illureshi’s aura, the protean can attempt an opposed caster level check to redirect the effect to another legal target within range.
 **Spellcasting** An illureshi casts spells as a 6th-level _sorcerer_. It does not gain access to other _sorcerer_ abilities.

##### Description

Illureshis embody chaos through sorcery, traveling the planes as chatty and whimsical masters of arcane magic.