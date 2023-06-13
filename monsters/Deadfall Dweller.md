---
cssclass: [monsters]
title1: Deadfall Dweller
desc_short: This creature resembles a fallen tree trunk that walks upon dozens of
  tiny, barbed branches and shambles like a spider.
title2: Deadfall Dweller
CR: 5
sources:
- name: Tears at Bitter Manor
  page: 58
  link: http://paizo.com/products/btpy93qw?Pathfinder-Module-Tears-at-Bitter-Manor
XP: 1600
alignment: N
size: Large
type: magical beast
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 18
  touch: 10
  flat_footed: 17
  components:
    dex: 1
    natural: 8
    size: -1
HP:
  HP: 57
  long: 6d10+24
saves:
  fort: 8
  ref: 6
  will: 3
immunities:
- acid
weaknesses:
- vulnerable to electricity
speeds:
  base: 30
  climb: 10
attacks:
  melee:
  - - text: bite +10 (1d6+5 plus poison)
      entries:
      - - damage: 1d6+5
        - effect: poison
      attack: bite
      bonus:
      - 10
    - text: 2 limbs +5 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: limbs
      bonus:
      - 5
  ranged:
  - - text: spittle +6 (1d6 acid plus entrap)
      entries:
      - - damage: 1d6
          type: acid
        - effect: entrap
      attack: spittle
      bonus:
      - 6
  special:
  - entrap (DC 16, 1d4 rounds, hardness 3, hp 6)
  - implant
  - spittle
space: 10
reach: 5
ability_scores:
  STR: 21
  DEX: 13
  CON: 16
  INT: 5
  WIS: 12
  CHA: 10
BAB: 6
CMB: 12
CMD: 23
CMD_other: can't be tripped
feats:
- name: Improved Initiative
- name: Power Attack
- name: Toughness
skills:
  Climb: 17
  Perception: 7
  Stealth: 2
    in forests or swamps: 10
  _racial_mods:
    Stealth:
      in forests or swamps: 8
languages:
- Sylvan (can't speak)
special_qualities:
- freeze
ecology:
  environment: temperate forests and swamps
  organization: solitary, brood (2-5), or ruin (6-12)
  treasure_type: standard
special_abilities:
  Implant (Ex): A deadfall dweller can inject 1d3 larvae into a helpless creature
    as a full-round action. Excretions from these larvae have a paralyzing effect,
    leaving the host helpless until the larvae mature into young deadfall dwellers
    that erupt from the host's body, killing it. Each day, an impregnated host must
    attempt a DC 16 Fortitude save. If the host succeeds at the saving throw, it is
    no longer helpless, but is still impregnated. If it fails, it takes 1 point of
    Constitution drain and remains helpless for another day. All of the larvae in
    an impregnated creature can be destroyed with a remove disease spell. Alternatively,
    a creature can take 10 minutes to attempt a DC 20 Heal check to remove a single
    larva. This check can be attempted multiple times, but each attempt deals 1d6
    points of damage to the host. The save DC is Constitution-based.
  Poison (Ex): Bite-injury; save Fort DC 16; frequency 1/round for 6 rounds; effect
    1d3 Dexterity damage; cure 1 save.
  Spittle (Ex): As a swift action, a deadfall dweller can emit a stream of corrosive
    spittle at one target within 30 feet. On a successful attack, the target takes
    1d6 points of acid damage, and must save to avoid being entrapped by the solidifying
    mucus.
desc_long: |-
  Deadfall dwellers are dangerous ambush predators most commonly encountered in the old forests and forgotten marshes of eastern Avistan. They make their homes among fallen stands of trees, where they take advantage of a unique form of camouflage. Hungry deadfall dwellers fold their many sticklike legs under themselves, collapsing against large tree trunks or simply lying on the ground. When a warm-blooded creature happens by, a deadfall dweller straightens its legs to pursue, and bellows out a spray of acidic mucus that paralyzes the victim in its tracks. The beast then advances to attack with its poisonous bite and sharp, scraping appendages.

  Deadfall dwellers reproduce by immobilizing prey with repeated applications of acidic spray, then implanting a clutch of eggs within the paralyzed host. The larval dwellers keep their host immobilized while they absorb moisture from its body. After the dwellers grow in size, they emerge from the husk of their host, whose flesh by that point resembles the shriveled bark of a dead tree.

  Most deadfall dwellers have a mottled green-brown carapace, the better to fit into their typical surroundings. A few have been reported in colder climates, with whitegray exoskeletons and freezing spittle. An average deadfall dweller stretches 11 feet long, stands 6 feet tall, and weighs 600 pounds.

---

# Deadfall Dweller
This creature resembles a _[[monsters/Fallen|fallen]]_ tree trunk that walks upon dozens of tiny, barbed branches and shambles like a spider.
**Source** Tears at _[[items/Armor Magic Abilities/Bitter|Bitter]]_ Manor pg. 58
**XP** 1,600

N Large magical beast
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 18, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+1 Dex, +8 natural, –1 size)
**hp** 57 (6d10+24)
**Fort** +8, **Ref** +6, **Will** +3
**Immune** acid
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 10 ft.
**Melee** bite +10 (1d6+5 plus poison), 2 limbs +5 (1d4+2)
**Ranged** spittle +6 (1d6 acid plus _[[universal monster rules/Entrap|entrap]]_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _entrap_ (DC 16, 1d4 rounds, hardness 3, hp 6), implant, spittle

##### Statistics
**Str** 21, **Dex** 13, **Con** 16, **Int** 5, **Wis** 12, **Cha** 10
**Base Atk** +6; **CMB** +12; **CMD** 23 (can’t be tripped)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** _Climb_ +17, Perception +7, Stealth +2 (+10 in forests or swamps); **Racial Modifiers** +8 Stealth in forests or swamps
**Languages** Sylvan (can’t speak)
**SQ** _[[universal monster rules/Freeze|freeze]]_

##### Ecology

**Environment** temperate forests and swamps
**Organization** solitary, brood (2–5), or ruin (6–12)
**Treasure** standard

### Special Abilities

**Implant (Ex)** A _[[monsters/Deadfall Dweller|deadfall dweller]]_ can inject 1d3 larvae into a _[[conditions/Helpless|helpless]]_ creature as a full-round action. Excretions from these larvae have a paralyzing effect, leaving the host _helpless_ until the larvae mature into young deadfall dwellers that erupt from the host’s body, killing it. Each day, an impregnated host must attempt a DC 16 Fortitude save. If the host succeeds at the saving throw, it is no longer _helpless_, but is still impregnated. If it fails, it takes 1 point of Constitution drain and remains _helpless_ for another day. All of the larvae in an impregnated creature can be destroyed with a _[[spells/Remove Disease|remove disease]]_ spell. Alternatively, a creature can take 10 minutes to attempt a DC 20 _[[spells/Heal|Heal]]_ check to remove a single larva. This check can be attempted multiple times, but each attempt deals 1d6 points of damage to the host. The save DC is Constitution-based.

**Poison (Ex)** Bite—injury; save Fort DC 16; frequency 1/round for 6 rounds; effect 1d3 Dexterity damage; cure 1 save.
**Spittle (Ex)** As a swift action, a _deadfall dweller_ can emit a stream of _[[items/Weapon Magic Abilities/Corrosive|corrosive]]_ spittle at one target within 30 feet. On a successful attack, the target takes 1d6 points of acid damage, and must save to avoid being entrapped by the solidifying mucus.

##### Description

Deadfall dwellers are dangerous ambush predators most commonly encountered in the old forests and forgotten marshes of eastern Avistan. They make their homes among _fallen_ stands of trees, where they take advantage of a unique form of camouflage. Hungry deadfall dwellers fold their many sticklike legs under themselves, collapsing against large tree trunks or simply lying on the ground. When a warm-blooded creature happens by, a _deadfall dweller_ straightens its legs to pursue, and _[[items/Mundane/Bellows|bellows]]_ out a spray of acidic mucus that paralyzes the victim in its tracks. The beast then advances to attack with its poisonous bite and sharp, scraping appendages.

Deadfall dwellers reproduce by immobilizing prey with repeated applications of _[[spells/Acidic Spray|acidic spray]]_, then implanting a clutch of eggs within the _[[conditions/Paralyzed|paralyzed]]_ host. The larval dwellers keep their host immobilized while they absorb moisture from its body. After the dwellers grow in size, they emerge from the husk of their host, whose flesh by that point resembles the shriveled bark of a dead tree.

Most deadfall dwellers have a mottled green-brown carapace, the better to fit into their typical surroundings. A few have been reported in colder climates, with whitegray exoskeletons and freezing spittle. An average _deadfall dweller_ stretches 11 feet long, stands 6 feet tall, and weighs 600 pounds.