---
cssclass: [monsters]
title1: Entothrope, Werewasp (Hybrid Form)
desc_short: With a stinger-tipped abdomen, large wings, compound eyes, anda pair of
  mandibles, this woman is more wasp than elf.
title2: Werewasp (Hybrid Form)
CR: 5
sources:
- name: Bestiary 6
  page: 119
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 1600
alignment: CN
size: Large
type: humanoid
subtypes:
- elf
- shapechanger
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 22
  touch: 12
  flat_footed: 19
  components:
    armor: 6
    dex,+1 dodge: 2
    natural: 4
    size: -1
HP:
  HP: 51
  long: 5d8+25
saves:
  fort: 8
  ref: 4
  will: 8
  other: +4 vs. mind-affecting, +2 vs. enchantment
defensive_abilities:
- insect mind
DR:
- amount: 10
  weakness: silver
immunities:
- sleep
speeds:
  base: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: whip +4 (1d3+4 nonlethal)
      entries:
      - - damage: 1d3+4
          type: nonlethal
      attack: whip
      bonus:
      - 4
    - text: sting +1 (1d8+2 plus curse ofentothropy and poison)
      entries:
      - - damage: 1d8+2
        - effect: curse ofentothropy
        - effect: poison
      attack: sting
      bonus:
      - 1
  special:
  - channel positive energy 4/day (DC 13, 3d6),poison (DC 18, 1/round for 6 rounds,
    1d2 Dex, cure 1 save)
spell_like_abilities:
  entries:
  - name: copycat
    source: cleric
    freq: 7/day
    other: 5 rounds
  - name: dazing touch
    source: cleric
    freq: 7/day
  sources:
  - name: cleric
    CL: 5
    concentration: 9
spells:
  entries:
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 17
  - name: dispel magic
    source: Cleric
    level: 3
  - name: suggestionD
    source: Cleric
    level: 3
    DC: 17
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 16
  - name: invisibilityD
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
    count: 2
  - name: charm personD
    source: Cleric
    level: 1
    DC: 15
  - name: command
    source: Cleric
    level: 1
    count: 2
    DC: 15
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 9
    slots:
      0: at-will
    domains:
    - charm
    - trickery
ability_scores:
  STR: 18
  DEX: 16
  CON: 18
  INT: 8
  WIS: 18
  CHA: 13
BAB: 3
CMB: 8
CMD: 22
feats:
- name: Combat Casting
- name: Dodge
- name: Selective Channeling
skills:
  Fly: 0
  Knowledge (religion): 3
  Perception: 8
  Stealth: -1
languages:
- Common
- Elven
special_qualities:
- change shape (elf, giant wasp, and hybrid; vermin shape II),entothropic empathy
- elven magic.
ecology:
  environment: any land
  organization: solitary, pair, or cult (3-12)
  treasure_type: NPC Gear
  treasure:
  - chainmail
  - whip
  - other treasure
desc_long: Werewasps in humanoid form often have two-toned hair color and a faint,
  humming timbre in their voices.

---

# Entothrope, Werewasp (Hybrid Form)
With a stinger-tipped abdomen, large wings, compound eyes, and

a pair of mandibles, this woman is more wasp than elf.
**Source** Bestiary 6 pg. 119
**XP** 1,600

CN Large humanoid (elf, shapechanger)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+6 armor, +2 Dex,

+1 dodge, +4 natural, –1 size)
**hp** 51 (5d8+25)
**Fort** +8, **Ref** +4, **Will** +8; +4 vs. mind-affecting, +2 vs. enchantment
**Defensive Abilities** insect mind; **DR** 10/silver; **Immune** sleep

##### Offense
**Speed** 20 ft., fly 60 ft. (good)
**Melee** _[[items/Weapon/Whip|whip]]_ +4 (1d3+4 nonlethal), sting +1 (1d8+2 plus curse of

entothropy and poison)
**Special Attacks** channel positive energy 4/day (DC 13, 3d6),

poison (DC 18, 1/round for 6 rounds, 1d2 Dex, cure 1 save)
**_[[classes/Cleric|Cleric]]_ _[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +9)
7/day—copycat (5 rounds), dazing touch
**_Cleric_ Spells Prepared** (CL 5th; concentration +9)
 3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Dispel Magic|dispel magic]]_, suggestionD (DC 17)
 2nd—_[[spells/Hold Person|hold person]]_ (2, DC 16), invisibilityD, _[[spells/Spiritual Weapon|spiritual weapon]]_
 1st—_[[spells/Bless|bless]]_ (2), charm personD (DC 15), _[[spells/Command|command]]_ (2, DC 15)
 0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_
 **D** domain spell; **Domains** Charm, Trickery

##### Statistics
**Str** 18, **Dex** 16, **Con** 18, **Int** 8, **Wis** 18, **Cha** 13
**Base Atk** +3; **CMB** +8; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Selective Channeling|Selective Channeling]]_
**Skills** Fly +0, Knowledge (religion) +3, Perception +8, Stealth –1
**Languages** Common, Elven
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (elf, giant wasp, and hybrid; _[[spells/Vermin Shape II|vermin shape II]]_),

entothropic _[[feats/Empathy|empathy]]_, elven magic.

##### Ecology

**Environment** any land
**Organization** solitary, pair, or cult (3–12)
**Treasure** NPC gear (_[[items/Armor/Chainmail|chainmail]]_, _whip_, other treasure)

##### Description

Werewasps in humanoid form often have two-toned hair color and a faint, humming timbre in their voices.