---
cssclass: [monsters]
title1: Lamp Blighter
desc_short: This creature looks like a tiny, stooped elf with gray skin, cruel claws,
  and glossy purple moth wings. Its mirthless grin exposes sharp teeth, and a bloody
  string of humanoid eyeballs adorns its neck.
title2: Lamp Blighter
CR: 6
sources:
- name: 'Pathfinder #128: Songbird, Scion, Saboteur'
  page: 90
  link: http://paizo.com/products/btpy9vn0?Pathfinder-Adventure-Path-128-Songbird-Scion-Saboteur
XP: 2400
alignment: CE
size: Small
type: fey
initiative:
  bonus: 5
senses:
  blindsight: 60
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 17
  flat_footed: 11
  components:
    dex: 5
    dodge: 1
    size: 1
HP:
  HP: 45
  long: 10d6+10
saves:
  fort: 4
  ref: 12
  will: 9
defensive_abilities:
- invisibility
DR:
- amount: 10
  weakness: cold iron
SR: 17
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +11 (1d8-2)
      entries:
      - - damage: 1d8-2
      attack: bite
      bonus:
      - 11
    - text: 2 claws +11 (1d10-2/19-20 plus eye pluck)
      entries:
      - - damage: 1d10-2
          crit_range: 19-20
        - effect: eye pluck
      count: 2
      attack: claws
      bonus:
      - 11
  ranged:
  - - text: +1 shortbow +13 (1d4-1/×3)
      entries:
      - - damage: 1d4-1
          crit_multiplier: 3
      attack: +1 shortbow
      bonus:
      - 13
  special:
  - eye pluck
  - special arrows
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: dancing lights
    source: default
    freq: 1/day
  - name: deeper darkness
    source: default
    freq: 1/day
  - name: detect thoughts
    source: default
    freq: 1/day
    DC: 14
  - name: disguise self
    source: default
    freq: 1/day
  - name: dispel magic
    source: default
    freq: 1/day
  - name: entangle
    source: default
    freq: 1/day
    DC: 13
  - name: shield
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 12
ability_scores:
  STR: 7
  DEX: 20
  CON: 12
  INT: 16
  WIS: 15
  CHA: 15
BAB: 5
CMB: 2
CMD: 18
feats:
- name: Dodge
- name: Point-Blank Shot
- name: Precise Shot
- name: Weapon Finesse
- name: Weapon Focus (shortbow)
skills:
  Acrobatics: 16
  Bluff: 13
  Disguise: 13
  Escape Artist: 16
  Fly: 20
  Knowledge (local): 10
  Knowledge (nature): 14
  Perception: 15
  Sense Motive: 13
  Stealth: 22
  Use Magic Device: 13
languages:
- Common
- Sylvan
- Undercommon
gear:
  gear:
  - +1 shortbow
ecology:
  environment: temperate forests and urban
  organization: solitary, pair, or band (3-5)
  treasure_type: standard
  treasure:
  - +1 shortbow
  - other treasure
special_abilities:
  Bite (Ex): A lamp blighter's sharp-toothed bite is a primary natural attack that
    deals 1d8 points of damage.
  Blighted Arrows (Su): |-
    When a lamp blighter fires an arrow from any bow, it can augment the arrow's properties by sprinkling it with dust from its wings as a free action. It can choose any one of the following effects when dusting an arrow. The lamp blighter can use this ability a number of times per day equal to its Charisma score (15 for a typical lamp blighter). The save DCs are Charisma-based. 

    Bleeding Wound: The target must succeed at a DC 15 Fortitude save, or it takes 1d4 points of bleed damage. 

    Blinding Terror: The target must succeed at a DC 15 Will save or become blind and panicked for 1d4+2 rounds. If the target succeeds at its Will save, it is instead shaken for 1 round. 

    Sleep: The target must succeed at a DC 15 Will save or fall asleep for 5 minutes.
  Claws (Ex): A lamp blighter's pointed claws are primary natural attacks that deal
    1d10 points of damage and threaten a critical hit on a roll of 19-20.
  Eye Pluck (Ex): Once per round, when a lamp blighter confirms a critical hit with
    a claw attack, or when it hits a helpless creature with a claw attack, it can
    pluck out its target's eye as a free action unless the affected creature succeeds
    at a DC 13 Fortitude save. A creature that loses an eye this way takes a -4 penalty
    on all sight-based Perception checks until the damage is repaired (such as with
    a restoration spell). The save DC is Strength-based.
  Invisibility (Su): A lamp blighter remains invisible when it attacks. This ability
    is constant, but the lamp blighter can suppress or resume it as a free action.
desc_long: |-
  Twisted in mind and form, lamp blighters have been corrupted by their own hatred for civilization and its encroachment upon lands that were once wild. Named for their practice of darkening lamps to draw victims close and also their love of ripping out eyes with their vicious claws, they take out this hatred upon inhabitants of border villages and towns, amplifying fear of the dark in the places they bedevil.

   Lamp blighters stand 2 feet tall fully when upright, though they are usually hunched over and flying at eye level of their victims, and they weigh about 20 pounds. 

---

# Lamp Blighter
This creature looks like a tiny, stooped elf with _[[monsters/Gray|gray]]_ skin, _[[items/Weapon Magic Abilities/Cruel|cruel]]_ claws, and glossy purple moth wings. Its mirthless grin exposes sharp teeth, and a bloody string of humanoid eyeballs adorns its neck.
**Source** Pathfinder #128: _[[spells/Songbird|Songbird]]_, Scion, Saboteur pg. 90
**XP** 2,400
CE Small fey
**Init** +5; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 17, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+5 Dex, +1 dodge, +1 size)
**hp** 45 (10d6+10)
**Fort** +4, **Ref** +12, **Will** +9
**Defensive Abilities** _[[spells/Invisibility|invisibility]]_; **DR** 10/cold iron; **SR** 17

##### Offense
**Speed** 30 ft.
**Melee** bite +11 (1d8–2), 2 claws +11 (1d10–2/19–20 plus eye pluck)
**Ranged** +1 _[[items/Weapon/Shortbow|shortbow]]_ +13 (1d4–1/×3)
**Special Attacks** eye pluck, special arrows
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
Constant—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_ 
At will—_[[spells/Darkness|darkness]]_ 
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 14), _[[spells/Disguise Self|disguise self]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Entangle|entangle]]_ (DC 13), _[[spells/Shield|shield]]_

##### Statistics
**Str** 7, **Dex** 20, **Con** 12, **Int** 16, **Wis** 15, **Cha** 15
**Base Atk** +5; **CMB** +2; **CMD** 18
**Feats** _Dodge_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_shortbow_)
**Skills** Acrobatics +16, Bluff +13, Disguise +13, Escape Artist +16, Fly +20, Knowledge (local) +10, Knowledge (nature) +14, Perception +15, Sense Motive +13, Stealth +22, Use Magic Device +13
**Languages** Common, Sylvan, Undercommon
**Gear** +1 _shortbow_

##### Ecology

**Environment** temperate forests and urban
**Organization** solitary, pair, or band (3-5)
**Treasure** standard (+1 _shortbow_, other treasure)

### Special Abilities

**Bite (Ex)** A _[[monsters/Lamp Blighter|lamp blighter]]_’s sharp-toothed bite is a primary natural attack that deals 1d8 points of damage.

**Blighted Arrows (Su)** When a _lamp blighter_ fires an arrow from any bow, it can augment the arrow’s properties by sprinkling it with dust from its wings as a free action. It can choose any one of the following effects when dusting an arrow. The _lamp blighter_ can use this ability a number of times per day equal to its Charisma score (15 for a typical _lamp blighter_). The save DCs are Charisma-based.

Bleeding Wound: The target must succeed at a DC 15 Fortitude save, or it takes 1d4 points of _[[universal monster rules/Bleed|bleed]]_ damage.

_[[items/Armor Magic Abilities/Blinding|Blinding]]_ Terror: The target must succeed at a DC 15 Will save or become blind and _[[conditions/Panicked|panicked]]_ for 1d4+2 rounds. If the target succeeds at its Will save, it is instead _[[conditions/Shaken|shaken]]_ for 1 round.

Sleep: The target must succeed at a DC 15 Will save or fall asleep for 5 minutes.

**Claws (Ex)** A _lamp blighter_’s pointed claws are primary _[[universal monster rules/Natural Attacks|natural attacks]]_ that deal 1d10 points of damage and threaten a critical hit on a roll of 19–20.

**Eye Pluck (Ex)** Once per round, when a _lamp blighter_ confirms a critical hit with a claw attack, or when it hits a _[[conditions/Helpless|helpless]]_ creature with a claw attack, it can pluck out its target’s eye as a free action unless the affected creature succeeds at a DC 13 Fortitude save. A creature that loses an eye this way takes a –4 penalty on all sight-based Perception checks until the damage is repaired (such as with a _[[spells/Restoration|restoration]]_ spell). The save DC is Strength-based.

**_Invisibility_ (Su)** A _lamp blighter_ remains _[[conditions/Invisible|invisible]]_ when it attacks. This ability is constant, but the _lamp blighter_ can suppress or resume it as a free action.

##### Description

Twisted in mind and form, _[[items/Mundane/Lamp|lamp]]_ blighters have been corrupted by their own hatred for civilization and its encroachment upon lands that were once wild. Named for their practice of darkening lamps to draw victims close and also their love of ripping out eyes with their _[[items/Weapon Magic Abilities/Vicious|vicious]]_ claws, they take out this hatred upon inhabitants of border villages and towns, amplifying _[[universal monster rules/Fear|fear]]_ of the dark in the places they bedevil.

_Lamp_ blighters stand 2 feet tall fully when upright, though they are usually hunched over and flying at eye level of their victims, and they weigh about 20 pounds.