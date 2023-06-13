---
cssclass: [monsters]
title1: Guardian Spirit, Guardian Spirit Imp
desc_short: A violet rune glows in the center of this red-skinned fiend's forehead.
title2: Guardian Spirit Imp
CR: 4
sources:
- name: Monster Summoner's Handbook
  page: 26
  link: http://paizo.com/products/btpy9ela?Pathfinder-Player-Companion-Monster-Summoners-Handbook
XP: 1200
alignment: LE
size: Tiny
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  see in darkness: true
AC:
  AC: 20
  touch: 18
  flat_footed: 14
  components:
    dex: 5
    dodge: 1
    natural: 2
    size: 2
HP:
  HP: 32
  long: 5d10+5
  fast_healing: 2
saves:
  fort: 2
  ref: 9
  will: 6
DR:
- amount: 5
  weakness: good or silver
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 15
speeds:
  base: 20
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: sting +11 (1d4+1 plus poison)
      entries:
      - - damage: 1d4+1
        - effect: poison
      attack: sting
      bonus:
      - 11
  special:
  - smite threat 1/day
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: guidance
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
    DC: 17
  - name: augury
    source: default
    freq: 1/day
  - name: call lightning
    source: default
    freq: 1/day
    DC: 19
  - name: protection from chaos
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 19
  - name: commune
    source: default
    freq: 1/week
    other: 6 questions
    CL: 12
  sources:
  - name: default
    CL: 6
    concentration: 10
ability_scores:
  STR: 12
  DEX: 20
  CON: 12
  INT: 15
  WIS: 14
  CHA: 20
BAB: 5
CMB: 4
CMD: 18
feats:
- name: Dodge
- name: Mobility
- name: Weapon Finesse
skills:
  Acrobatics: 12
  Bluff: 13
  Fly: 25
  Knowledge (arcana): 10
  Knowledge (planes): 10
  Perception: 10
  Sense Motive: 7
  Spellcraft: 10
languages:
- Common
- Draconic
- Infernal
special_qualities:
- change shape (boar, giant spider, rat, or raven, beast shape I)
- fated guardian
- guardian spirit 4th level
ecology:
  environment: any (Hell)
  organization: solitary or with ward
  treasure_type: none
special_abilities:
  Poison (Ex): Sting-injury; save Fort DC 15; frequency 1/round for 6 rounds; effect
    1d2 Dex; cure 1 save. The save DC is Constitution-based, and includes a +2 racial
    bonus.
desc_long: A guardian spirit is bound to the fate of a mortal being (called its “ward”).
  This bond may be formed by any number of beings or events carrying the weight of
  destiny, such as deities, the Eldest, norns, and mythic creatures and magic. A spirit
  can bind itself willingly if it believes that doing so is likely to further its
  agenda, give it more power, or allow it access to the world of mortals. Mortals
  can generally invoke a guardian spirit only with summoning and calling spells.

---

# Guardian Spirit, Guardian Spirit Imp
A violet rune glows in the center of this red-skinned fiend’s forehead.
**Source** Monster _[[classes/Summoner|Summoner]]_'s Handbook pg. 26
**XP** 1,200

LE Tiny outsider (devil, evil, extraplanar, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +10

##### Defense

**AC** 20, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +1 dodge, +2 natural, +2 size)
**hp** 32 (5d10+5); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +2, **Ref** +9, **Will** +6
**DR** 5/good or silver; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 15

##### Offense
**Speed** 20 ft., fly 50 ft. (perfect)
**Melee** sting +11 (1d4+1 plus poison)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** smite threat 1/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +10)
Constant—_detect good_, _detect magic_
At will—_[[spells/Guidance|guidance]]_, _[[spells/Invisibility|invisibility]]_ (self only, DC 17)
1/day—_[[spells/Augury|augury]]_, _[[spells/Call Lightning|call lightning]]_ (DC 19), _[[spells/Protection From Chaos|protection from chaos]]_, _[[spells/Suggestion|suggestion]]_ (DC 19)
1/week—_[[spells/Commune|commune]]_ (6 questions, CL 12th)

##### Statistics
**Str** 12, **Dex** 20, **Con** 12, **Int** 15, **Wis** 14, **Cha** 20
**Base Atk** +5; **CMB** +4; **CMD** 18
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +12, Bluff +13, Fly +25, Knowledge (arcana) +10, Knowledge (planes) +10, Perception +10, Sense Motive +7, Spellcraft +10
**Languages** Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[monsters/Boar|boar]]_, giant spider, rat, or raven, _[[spells/Beast Shape I|beast shape I]]_), fated _[[items/Weapon Magic Abilities/Guardian|guardian]]_, _guardian_ spirit 4th level

##### Ecology

**Environment** any (Hell)
**Organization** solitary or with ward
**Treasure** none

### Special Abilities

**Poison (Ex)** Sting—injury; save Fort DC 15; frequency 1/round for 6 rounds; effect 1d2 Dex; cure 1 save. The save DC is Constitution-based, and includes a +2 racial bonus.

##### Description

A _guardian_ spirit is bound to the fate of a mortal being (_[[items/Weapon Magic Abilities/Called|called]]_ its “ward”). This bond may be formed by any number of beings or events carrying the weight of destiny, such as deities, the Eldest, norns, and mythic creatures and magic. A spirit can bind itself willingly if it believes that doing so is likely to further its agenda, give it more power, or allow it access to the world of mortals. Mortals can generally invoke a _guardian_ spirit only with summoning and calling spells.