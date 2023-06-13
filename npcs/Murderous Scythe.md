---
cssclass: [monsters]
title1: Murderous Scythe
title2: Murderous Scythe
CR: 16
sources:
- name: NPC Codex
  page: 210
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-elf
classes:
- druid 4
- fighter 6
- assassin 7
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 26
  touch: 12
  flat_footed: 26
  components:
    armor: 12
    deflection: 2
    natural: 2
HP:
  HP: 144
  long: 4d8+6d10+7d8+57
saves:
  fort: 15
  ref: 8
  will: 11
  other: +2 vs. enchantments, +2 vs. fear, +3 vs. poison, +4 vs. fey and plant-targeted
    effects
defensive_abilities:
- bravery +2
- improved uncanny dodge
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 scythe +25/+20/+15 (2d4+15/19-20/×4 plus poison)
      entries:
      - - damage: 2d4+15
          crit_range: 19-20
          crit_multiplier: 4
        - effect: poison
      attack: +2 scythe
      bonus:
      - 25
      - 20
      - 15
  special:
  - death attack (DC 19)
  - quiet death
  - sneak attack +4d6
  - true death (DC 22)
  - weapon training (heavy blades +1)
  - wild shape 1/day
spell_like_abilities:
  entries:
  - name: wooden fist
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 4
    concentration: 6
spells:
  entries:
  - is_domain_spell: true
    name: barkskin
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
    DC: 14
  - name: spider climb
    source: Druid
    level: 2
  - name: tree shape
    source: Druid
    level: 2
  - is_domain_spell: true
    name: entangle
    source: Druid
    level: 1
    DC: 13
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - name: longstrider
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: detect magic
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 4
    concentration: 6
    slots:
      0: at-will
    domains:
    - plant
tactics:
  Before Combat: The assassin casts barkskin and longstrider. He applies poison to
    his scythe, and wild shapes into an eagle or dire rat.
  During Combat: In animal form, the assassin studies an enemy spellcaster for 3 rounds
    before casting obscuring mist to sow chaos among his foes. He then takes his real
    form to make a death attack against his target. In melee, he trips his foes.
  Base Statistics: Without barkskin and longstrider, the assassin's statistics are
    AC 24, touch 12, flat-footed 24; Speed 20 ft.
ability_scores:
  STR: 24
  DEX: 10
  CON: 16
  INT: 14
  WIS: 14
  CHA: 8
BAB: 14
CMB: 21
CMB_other: +25 trip
CMD: 33
CMD_other: 35 vs. trip
feats:
- name: Combat Expertise
- name: Critical Focus
- name: Disruptive
- name: Greater Trip
- name: Improved Critical (scythe)
- name: Improved Initiative
- name: Improved Trip
- name: Improved Vital Strike
- name: Natural Spell
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Vital Strike
- name: Weapon Focus (scythe)
- name: Weapon Specialization (scythe)
skills:
  Climb: 13
  Disguise: 1
  Fly: 3
  Knowledge (geography): 10
  Knowledge (local): 7
  Knowledge (religion): 7
  Knowledge (nature): 12
  Perception: 24
  Sense Motive: 19
  Stealth: 21
  Survival: 12
  Swim: 13
languages:
- Common
- Elven
- Goblin
- Sylvan
special_qualities:
- armor training 1
- elf blood
- hidden weapons
- nature bond (Plant domain)
- nature sense
- poison use
- trackless step
- wild empathy +3
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - deathblade poison
  - purple worm poison (3)
  other:
  - +3 glamered darkwood full plate
  - +2 scythe
  - belt of physical might +4 (Str, Con)
  - cloak of resistance +1
  - ring of protection +2
  - 402 gp
desc_long: Many of these murderers serve as assassins for dark druid circles or dominate
  savage humanoid tribes.

---

# Murderous Scythe

**Source** NPC Codex pg. 210
**XP** 76,800
Half-elf _[[classes/Druid|druid]]_ 4/fighter 6/assassin 7

NE Medium humanoid (elf, human)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24

##### Defense

**AC** 26, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+12 armor, +2 _[[spells/Deflection|deflection]]_, +2 natural)
**hp** 144 (4d8+6d10+7d8+57)
**Fort** +15, **Ref** +8, **Will** +11; +2 vs. enchantments, +2 vs. _[[universal monster rules/Fear|fear]]_, +3 vs. poison, +4 vs. fey and plant-targeted effects
**Defensive Abilities** bravery +2, improved uncanny _[[feats/Dodge|dodge]]_

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Scythe|scythe]]_ +25/+20/+15 (2d4+15/19–20/×4 plus poison)
**Special Attacks** death attack (DC 19), _[[feats/Quiet Death|quiet death]]_, sneak attack +4d6, true death (DC 22), weapon _[[items/Weapon Magic Abilities/Training|training]]_ (heavy blades +1), wild shape 1/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
5/day—wooden fist
**_Druid_ Spells Prepared **(CL 4th; concentration +6)
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Resist Energy|resist energy]]_ (DC 14), _[[spells/Spider Climb|spider climb]]_, _[[spells/Tree Shape|tree shape]]_
1st—_[[spells/Entangle|entangle]]_ (DC 13), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Longstrider|longstrider]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Know Direction|know direction]]_
**Domain **Plant

### Tactics

**Before Combat **The assassin casts _barkskin_ and _longstrider_. He applies poison to his _scythe_, and wild shapes into an _[[monsters/Eagle|eagle]]_ or dire rat.
**During Combat **In animal form, the assassin studies an enemy spellcaster for 3 rounds before casting _obscuring mist_ to sow chaos among his foes. He then takes his real form to make a death attack against his target. In melee, he trips his foes.
**Base Statistics **Without _barkskin_ and _longstrider_, the assassin’s statistics are **AC **24, touch 12, _flat-footed_ 24; Speed 20 ft.

##### Statistics
**Str** 24, **Dex** 10, **Con** 16, **Int** 14, **Wis** 14, **Cha** 8
**Base Atk** +14; **CMB** +21 (+25 _[[universal monster rules/Trip|trip]]_); **CMD** 33 (35 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Disruptive|Disruptive]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_scythe_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +13, Disguise +1, Fly +3, Knowledge (geography) +10, Knowledge (local, religion) +7, Knowledge (nature) +12, Perception +24, Sense Motive +19, Stealth +21, Survival +12, Swim +13
**Languages** Common, Elven, _[[monsters/Goblin|Goblin]]_, Sylvan
**SQ** armor _training_ 1, elf blood, hidden weapons, nature bond (Plant domain), nature sense, poison use, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +3, woodland stride
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[poisons/Deathblade|deathblade]]_ poison, _[[poisons/Purple Worm Poison|purple worm poison]]_ (3); **Other Gear** +3 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ darkwood _[[items/Armor/Full plate|full plate]]_, +2 _scythe_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 402 gp

Many of these murderers serve as assassins for dark _druid_ circles or dominate savage humanoid tribes.