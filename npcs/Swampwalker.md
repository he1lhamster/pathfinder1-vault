---
cssclass: [monsters]
title1: Swampwalker
title2: Swampwalker
CR: 8
sources:
- name: NPC Codex
  page: 132
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Half-elf
classes:
- ranger 9
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    deflection: 1
    dex: 1
    natural: 3
HP:
  HP: 81
  long: 9d10+27
saves:
  fort: 8
  ref: 7
  will: 5
  other: +2 vs. enchantments
defensive_abilities:
- evasion
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk spiked chain +14/+9 (2d4+6)
      entries:
      - - damage: 2d4+6
      attack: mwk spiked chain
      bonus:
      - 14
      - 9
  ranged:
  - - text: +1 composite longbow +12/+7 (1d8+5/19-20/×3)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 composite longbow
      bonus:
      - 12
      - 7
  special:
  - favored enemy (aquatic humanoids +4, humans +2)
spells:
  entries:
  - name: barkskin
    source: Ranger
    level: 2
  - name: snare
    source: Ranger
    level: 2
  - name: pass without trace
    source: Ranger
    level: 1
  - name: speak with animals
    source: Ranger
    level: 1
    count: 2
  sources:
  - name: Ranger
    type: prepared
    CL: 6
    concentration: 8
tactics:
  Before Combat: The ranger casts barkskin and pass without trace.
  During Combat: The ranger attacks from stealth using his bow. He might drag a Small
    opponent underwater, relying on Endurance to outlast his drowning foe (though
    he has his potion of water breathing just in case).
  Base Statistics: Without barkskin, the ranger's statistics are AC 16, touch 12,
    flat-footed 15.
ability_scores:
  STR: 18
  DEX: 12
  CON: 14
  INT: 10
  WIS: 14
  CHA: 8
BAB: 9
CMB: 13
CMD: 25
feats:
- name: Deadly Aim
- name: Endurance
- name: Exotic Weapon Proficiency (spiked chain)
- name: Improved Critical (composite longbow)
- name: Point-Blank Shot
- name: Rapid Shot
- name: Skill Focus (Stealth)
- name: Vital Strike
- name: Weapon Focus (composite longbow)
skills:
  Climb: 12
  Handle Animal: 6
  Knowledge (nature): 12
  Perception: 16
  Stealth: 16
  Survival: 14
  Swim: 16
languages:
- Common
- Elven
special_qualities:
- elf blood
- favored terrain (forest +2, swamp +4)
- hunter's bond (companions)
- swift tracker
- track +4
- wild empathy +8
- woodland stride
gear:
  combat:
  - +1 frost arrows (5)
  - +1 human-bane arrows (5)
  other:
  - f cure moderate wounds
  - potion of haste
  - potion of water breathing
desc_long: The swampwalker is a savage predator of the stinking marsh. He is familiar
  with its threats and uses them as tools to defeat his opponents.

---

# Swampwalker

**Source** NPC Codex pg. 132
**XP** 4,800
Half-elf _[[classes/Ranger|ranger]]_ 9
CE Medium humanoid (elf, human)
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +16

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +3 natural)
**hp** 81 (9d10+27)
**Fort** +8, **Ref** +7, **Will** +5; +2 vs. enchantments
**Defensive Abilities** evasion; **Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Spiked chain|spiked chain]]_ +14/+9 (2d4+6)
**Ranged** +1 _[[items/Weapon/Composite longbow|composite longbow]]_ +12/+7 (1d8+5/19–20/×3)
**Special Attacks** favored enemy (aquatic humanoids +4, humans +2)
**_Ranger_ Spells Prepared **(CL 6th; concentration +8)
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Snare|snare]]_
1st—_[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_ (2)

### Tactics

**Before Combat **The _ranger_ casts _barkskin_ and _pass without trace_.
**During Combat **The _ranger_ attacks from stealth using his bow. He might drag a Small opponent _[[items/Weapon Magic Abilities/Underwater|underwater]]_, relying on _[[feats/Endurance|Endurance]]_ to outlast his drowning foe (though he has his potion of _[[universal monster rules/Water Breathing|water breathing]]_ just in case).
**Base Statistics **Without _barkskin_, the _ranger_’s statistics are **AC **16, touch 12, _flat-footed_ 15.

##### Statistics
**Str** 18, **Dex** 12, **Con** 14, **Int** 10, **Wis** 14, **Cha** 8
**Base Atk** +9; **CMB** +13; **CMD** 25
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _Endurance_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (_spiked chain_), _[[feats/Improved Critical|Improved Critical]]_ (_composite longbow_), _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite longbow_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Handle Animal +6, Knowledge (nature) +12, Perception +16, Stealth +16, Survival +14, Swim +16
**Languages** Common, Elven
**SQ** elf blood, favored terrain (forest +2, swamp +4), _[[classes/Hunter|hunter]]_’s bond (companions), swift tracker, track +4, wild _[[feats/Empathy|empathy]]_ +8, woodland stride
**Combat Gear** +1 frost arrows (5), +1 human-bane arrows (5); **Other Gear** f _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Haste|haste]]_, potion of _water breathing_

The _[[npcs/Swampwalker|swampwalker]]_ is a savage predator of the stinking marsh. He is familiar with its threats and uses them as tools to defeat his opponents.