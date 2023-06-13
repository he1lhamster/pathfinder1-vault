---
cssclass: [monsters]
title1: Acolyte
title2: Acolyte
CR: 1/3
sources:
- name: NPC Codex
  page: 244
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 135
race: Human
classes:
- adept 1
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 14
  touch: 11
  flat_footed: 13
  components:
    armor: 3
    dex: 1
HP:
  HP: 5
  long: 1d6+2
saves:
  fort: -1
  ref: 1
  will: 3
speeds:
  base: 30
attacks:
  melee:
  - - text: morningstar +0 (1d8)
      entries:
      - - damage: 1d8
      attack: morningstar
      bonus:
      - 0
  - - text: silver dagger +0 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: silver dagger
      bonus:
      - 0
  ranged:
  - - text: silver dagger +1 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: silver dagger
      bonus:
      - 1
spells:
  entries:
  - name: bless
    source: Adept
    level: 1
  - name: cure light wounds
    source: Adept
    level: 1
  - name: guidance
    source: Adept
    level: 0
  - name: light
    source: Adept
    level: 0
  - name: mending
    source: Adept
    level: 0
  sources:
  - name: Adept
    type: prepared
    CL: 1
    concentration: 2
    slots:
      0: at-will
tactics:
  During Combat: The adept reads her scroll of sleep and commands her dog to attack.
    She then casts bless and attacks with her morningstar.
ability_scores:
  STR: 10
  DEX: 12
  CON: 8
  INT: 9
  WIS: 13
  CHA: 10
BAB: 0
CMB: 0
CMD: 11
feats:
- name: Skill Focus (Handle Animal)
- name: Toughness
skills:
  Handle Animal: 7
  Heal: 7
  Spellcraft: 3
  Perception: 1
languages:
- Common
gear:
  combat:
  - scroll of cure light wounds
  - scroll of sleep
  - alchemist's fire
  other:
  - studded leather
  - morningstar
  - silver dagger
  - guard dog
  - healer's kit
  - silver holy symbol
  - smokestick
  - spell component pouch
  - tindertwig
  - 9 gp
desc_long: |-
  An acolyte has just begun to unravel the mysteries of her faith, and lacks the fervent zeal that more indoctrinated members of her religion have. She is eager to learn, but her incomplete teachings mean she is more easily swayed by contrary rhetoric.

  Settlements that have adepts rather than clerics are often primitive or remote. Their religious practices may be a strange or heretical offshoot of a main religion, weaker than the common form but giving access to spells that are normally unavailable to true clerics (such as minor creation and sleep). A person trained by a cleric who instead manifests adept abilities may be cast out as a blasphemer or witch.

---

# Acolyte

**Source** NPC Codex pg. 244
**XP** 135
Human adept 1

N Medium humanoid (human)
**Init** +1; **Senses** Perception +1

##### Defense

**AC** 14, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +1 Dex)
**hp** 5 (1d6+2)
**Fort** –1, **Ref** +1, **Will** +3

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Morningstar|morningstar]]_ +0 (1d8) or silver _[[items/Weapon/Dagger|dagger]]_ +0 (1d4/19–20)
**Ranged** silver _dagger_ +1 (1d4/19–20)
**Adept Spells Prepared **(CL 1st; concentration +2)
1st—_[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_
0 (at will)—_[[spells/Guidance|guidance]]_, light, _[[spells/Mending|mending]]_

### Tactics

**During Combat **The adept reads her scroll of sleep and commands her _[[monsters/Dog|dog]]_ to attack. She then casts _bless_ and attacks with her _morningstar_.

##### Statistics
**Str** 10, **Dex** 12, **Con** 8, **Int** 9, **Wis** 13, **Cha** 10
**Base Atk** +0; **CMB** +0; **CMD** 11
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Handle Animal), _[[feats/Toughness|Toughness]]_
**Skills** Handle Animal +7, _[[spells/Heal|Heal]]_ +7, Spellcraft +3
**Languages** Common
**Combat Gear** scroll of _cure light wounds_, scroll of sleep, _[[classes/Alchemist|alchemist]]_’s fire; **Other Gear** studded leather, _morningstar_, silver _dagger_, _[[npcs/Guard|guard]]_ _dog_, _[[npcs/Healer|healer]]_’s kit, silver holy symbol, _[[items/Mundane/Smokestick|smokestick]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Tindertwig|tindertwig]]_, 9 gp

An _[[npcs/Acolyte|acolyte]]_ has just begun to unravel the mysteries of her faith, and lacks the _[[items/Weapon Magic Abilities/Fervent|fervent]]_ zeal that more indoctrinated members of her religion have. She is eager to learn, but her incomplete teachings mean she is more easily swayed by contrary rhetoric.

Settlements that have adepts rather than clerics are often primitive or remote. Their religious practices may be a strange or _[[items/Weapon Magic Abilities/Heretical|heretical]]_ offshoot of a main religion, weaker than the common form but giving access to spells that are normally unavailable to true clerics (such as _[[spells/Minor Creation|minor creation]]_ and sleep). A person trained by a _[[classes/Cleric|cleric]]_ who instead manifests adept abilities may be _[[spells/Cast Out|cast out]]_ as a blasphemer or _[[classes/Witch|witch]]_.