---
cssclass: [monsters]
title1: Sleepless Detective
title2: Sleepless Detective
CR: 9
sources:
- name: Inner Sea NPC Codex
  page: 55
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 6400
race: Human
classes:
- alchemist 5
- Sleepless detective 5
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    armor: 5
    dex: 1
HP:
  HP: 53
  long: 10d8+5
saves:
  fort: 6
  ref: 9
  will: 9
  other: +4 vs. poison
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +7/+2 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 7
      - 2
  ranged:
  - - text: bomb +8 (3d6+4 fire)
      entries:
      - - damage: 3d6+4
          type: fire
      attack: bomb
      bonus:
      - 8
  - - text: dagger +7 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 7
  special:
  - bomb 9/day (3d6+4 fire, DC 16)
  - sneak attack +2d6
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - superscripts:
    - APG
    name: blood biography
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: residual tracking
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 5
spells:
  entries:
  - name: detect thoughts
    source: Alchemist
    level: 2
    DC: 16
  - name: invisibility
    source: Alchemist
    level: 2
  - superscripts:
    - APG
    name: perceive cues
    source: Alchemist
    level: 2
  - name: comprehend languages
    source: Alchemist
    level: 1
  - name: cure light wounds
    source: Alchemist
    level: 1
  - name: detect secret doors
    source: Alchemist
    level: 1
  - name: disguise self
    source: Alchemist
    level: 1
  - name: expeditious retreat
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 5
ability_scores:
  STR: 10
  DEX: 13
  CON: 8
  INT: 19
  WIS: 14
  CHA: 12
BAB: 6
CMB: 6
CMD: 17
feats:
- name: Alertness
- name: Brew Potion
- name: Deft Hands
- superscripts:
  - APG
  name: Extra Discovery
- name: Iron Will
- name: Persuasive
- name: Throw Anything
- name: Toughness
skills:
  Bluff: 5
  Climb: 0
  Craft (alchemy): 17
  Diplomacy: 18
    to gather information: 22
  Disable Device: 17
  Disguise: 10
  Heal: 10
  Intimidate: 8
  Knowledge (arcana): 10
  Knowledge (local): 17
  Knowledge (nature): 10
  Perception: 23
  Sense Motive: 23
  Sleight of Hand: 10
  Spellcraft: 11
  Swim: 4
languages:
- Common
- Hallit
- Skald
- Varisian
special_qualities:
- alchemy (alchemy crafting +5, identify potions)
- canny sleuth
- discoveries (extend potion 4/day, precise bombs [4 squares], tanglefoot bomb)
- eye for detail
- follow clues
- forensic thaumaturgy
- mutagen (+4/-2, +2 natural, 50 minutes)
- poison use
- swift alchemy
gear:
  combat:
  - dust of appearance
  - elixir of truth
  - feather token (bird)
  - potion of jump
  - potion of see invisibility
  - potion of spider climb
  - wand of owl's wisdom (8 charges)
  - acid (3)
  - smokesticks (2)
  - sunrods (2)
  - tanglefoot bag
  - tindertwigs (5)
  other:
  - +1 chain shirt
  - daggers (2)
  - mwk dagger
  - cloak of resistance +1
  - ring of swimming
  - alchemy crafting kit
  - 'formula book (contains all prepared extracts as well as the following: 2nd-see
    invisibility'
special_abilities:
  Canny Sleuth (Ex): A Sleepless detective adds his Intelligence bonus on all Perception
    and Sense Motive checks, as well as on Diplomacy checks made to gather information.
  Eye for Detail (Ex): A Sleepless detective is entitled to an immediate Perception
    check to notice hidden traps, doors, and clues when he passes within 10 feet of
    them, whether or not he is actively looking.
  Follow Clues (Ex): A Sleepless detective can use Perception to follow tracks as
    the Survival skill.
desc_long: The Sleepless Agency operates out of Ustalav but provides peerless investigative
  services to clients located throughout the Inner Sea region. Although the organization
  also hires out bodyguards and other security experts, its most famous operatives
  are its detectives, who are able to spot and analyze the faintest clue. Some Sleepless
  detectives even take on proteges, who are expected to finance the investigations
  they conduct in exchange for receiving their training in the organization. The final
  test to enter the agency's ranks is to prove one's own innocence through superior
  investigative techniques after established Sleepless detectives frame the prospective
  agent.

---

# Sleepless Detective

**Source** Inner Sea NPC Codex pg. 55
**XP** 6,400
Human _[[classes/Alchemist|alchemist]]_ 5/Sleepless detective 5

N Medium humanoid (human)
**Init** +1; **Senses** Perception +23

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor, +1 Dex)
**hp** 53 (10d8+5)
**Fort** +6, **Ref** +9, **Will** +9; +4 vs. poison

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +7/+2 (1d4/19–20)
**Ranged** bomb +8 (3d6+4 fire) or _dagger_ +7 (1d4/19–20)
**Special Attacks** bomb 9/day (3d6+4 fire, DC 16), sneak attack +2d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th)
At will—_[[spells/Detect Magic|detect magic]]_
3/day—_[[spells/Blood Biography|blood biography]]_, _[[spells/Residual Tracking|residual tracking]]_
**_Alchemist_ Extracts Prepared** (CL 5th)
2nd—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Invisibility|invisibility]]_, _[[spells/Perceive Cues|perceive cues]]_
1st—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Detect Secret Doors|detect secret doors]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_

##### Statistics
**Str** 10, **Dex** 13, **Con** 8, **Int** 19, **Wis** 14, **Cha** 12
**Base Atk** +6; **CMB** +6; **CMD** 17
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Deft Hands|Deft Hands]]_, _[[feats/Extra Discovery|Extra Discovery]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Throw Anything|Throw Anything]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +5, _[[universal monster rules/Climb|Climb]]_ +0, Craft (alchemy) +17, Diplomacy +18 (+22 to gather information), Disable Device +17, Disguise +10, _[[spells/Heal|Heal]]_ +10, Intimidate +8, Knowledge (arcana) +10, Knowledge (local) +17, Knowledge (nature) +10, Perception +23, Sense Motive +23, Sleight of Hand +10, Spellcraft +11, Swim +4
**Languages** Common, Hallit, _[[classes/Skald|Skald]]_, Varisian
**SQ** alchemy (alchemy crafting +5, _[[spells/Identify|identify]]_ potions), canny sleuth, discoveries (extend potion 4/day, precise bombs [4 squares], tanglefoot bomb), eye for detail, follow clues, forensic thaumaturgy*, mutagen (+4/–2, +2 natural, 50 minutes), poison use, swift alchemy
**Combat Gear** _[[items/Wondrous Item/Dust of Appearance|dust of appearance]]_, _[[items/Wondrous Item/Elixir of Truth|elixir of truth]]_, feather token (bird), potion of _[[spells/Jump|jump]]_, potion of _[[spells/See Invisibility|see invisibility]]_, potion of _[[spells/Spider Climb|spider climb]]_, wand of owl’s wisdom (8 charges), acid (3), smokesticks (2), sunrods (2), _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_, tindertwigs (5); **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, daggers (2), mwk _dagger_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Swimming|ring of swimming]]_, _[[items/Mundane/Alchemy crafting kit|alchemy crafting kit]]_, _[[items/Mundane/Formula book|formula book]]_ (contains all prepared extracts as well as the following: 2nd—_see invisibility_

### Special Abilities

**Canny Sleuth (Ex)** A _[[npcs/Sleepless Detective|Sleepless detective]]_ adds his Intelligence bonus on all Perception and Sense Motive checks, as well as on Diplomacy checks made to gather information.

**Eye for Detail (Ex)** A _Sleepless detective_ is entitled to an immediate Perception check to notice hidden traps, doors, and clues when he passes within 10 feet of them, whether or not he is actively looking.

**Follow Clues (Ex)** A _Sleepless detective_ can use Perception to follow tracks as the Survival skill.

The Sleepless Agency operates out of Ustalav but provides peerless investigative services to clients located throughout the Inner Sea region. Although the organization also hires out bodyguards and other security experts, its most famous operatives are its detectives, who are able to spot and analyze the faintest clue. Some Sleepless detectives even take on proteges, who are expected to finance the investigations they conduct in exchange for receiving their _[[items/Weapon Magic Abilities/Training|training]]_ in the organization. The final test to enter the agency’s ranks is to prove one’s own _[[spells/Innocence|innocence]]_ through superior investigative techniques after established Sleepless detectives frame the prospective agent.