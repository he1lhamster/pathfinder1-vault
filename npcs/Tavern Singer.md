---
cssclass: [monsters]
title1: Tavern Singer
title2: Tavern Singer
CR: 1/2
sources:
- name: NPC Codex
  page: 26
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 200
race: Half-elf
classes:
- bard 1
alignment: CN
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    armor: 3
    dex: 2
HP:
  HP: 9
  long: 1d8+1
saves:
  fort: 1
  ref: 4
  will: 1
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: rapier +2 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: rapier
      bonus:
      - 2
  ranged:
  - - text: shortbow +2 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 2
  special:
  - bardic performance 7 rounds/day (countersong, distraction, fascinate, inspire
    courage +1)
spells:
  entries:
  - name: grease
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 14
  - name: dancing lights
    source: Bard
    level: 0
  - name: ghost sound
    source: Bard
    level: 0
    DC: 13
  - name: message
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 2
      0: at-will
tactics:
  During Combat: The bard uses grease to escape.
ability_scores:
  STR: 10
  DEX: 14
  CON: 12
  INT: 13
  WIS: 8
  CHA: 17
BAB: 0
CMB: 0
CMD: 12
feats:
- name: Skill Focus (Perform [wind])
- name: Weapon Finesse
skills:
  Bluff: 7
  Diplomacy: 7
  Perception: 5
  Perform (wind): 12
  Sense Motive: 3
  Sleight of Hand: 6
  Stealth: 5
  Use Magic Device: 7
languages:
- Common
- Elven
special_qualities:
- bardic knowledge +1
- elf blood
gear:
  combat:
  - potions of cure light wounds (2)
  - alchemist's fire
  - sunrod
  - tanglefoot bag
  - thunderstone
  other:
  - studded leather
  - rapier
  - shortbow with 20 arrows
  - masterwork flute
  - 13 gp
desc_long: These performers entertain to earn drinks and tips.

---

# Tavern Singer

**Source** NPC Codex pg. 26
**XP** 200
Half-elf _[[classes/Bard|bard]]_ 1

CN Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +2 Dex)
**hp** 9 (1d8+1)
**Fort** +1, **Ref** +4, **Will** +1; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Rapier|rapier]]_ +2 (1d6/18–20)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +2 (1d6/×3)
**Special Attacks** bardic performance 7 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire courage +1)
**_Bard_ Spells Known **(CL 1st; concentration +4)
1st (2/day)—_[[spells/Grease|grease]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 14)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

### Tactics

**During Combat **The _bard_ uses _grease_ to escape.

##### Statistics
**Str** 10, **Dex** 14, **Con** 12, **Int** 13, **Wis** 8, **Cha** 17
**Base Atk** +0; **CMB** +0; **CMD** 12
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Perform [wind]), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +7, Diplomacy +7, Perception +5, Perform (wind) +12, Sense Motive +3, Sleight of Hand +6, Stealth +5, Use Magic Device +7
**Languages** Common, Elven
**SQ** bardic knowledge +1, elf blood
**Combat Gear** potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[classes/Alchemist|alchemist]]_’s fire, _[[items/Mundane/Sunrod|sunrod]]_, _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_, _[[items/Mundane/Thunderstone|thunderstone]]_; **Other Gear** studded leather, _rapier_, _shortbow_ with 20 arrows, masterwork flute, 13 gp

These performers entertain to earn drinks and tips.