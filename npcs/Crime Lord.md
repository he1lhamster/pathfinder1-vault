---
cssclass: [monsters]
title1: Crime Lord
title2: Crime Lord
CR: 18
sources:
- name: NPC Codex
  page: 94
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Gnome
classes:
- fighter 19
alignment: N
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 34
  touch: 18
  flat_footed: 29
  components:
    armor: 11
    deflection: 2
    dex: 3
    dodge: 2
    natural: 5
    size: 1
HP:
  HP: 204
  long: 19d10+95
saves:
  fort: 20
  ref: 14
  will: 11
  other: +2 vs. illusions, +5 vs. fear
defensive_abilities:
- blink
- bravery +5
- defensive training (+4 dodge bonus to AC vs. giants)
DR:
- amount: 5
  weakness: '-'
speeds:
  base: 40
attacks:
  melee:
  - - text: +2 dwarven urgrosh +30/+30/+25/+20/+15 (1d4+12/19-20/×3)
      entries:
      - - damage: 1d4+12
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 dwarven urgrosh
      bonus:
      - 30
      - 30
      - 25
      - 20
      - 15
    - text: +2 dwarven urgrosh +30 (1d6+12/19-20/×3)
      entries:
      - - damage: 1d6+12
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 dwarven urgrosh
      bonus:
      - 30
  - - text: +2 dwarven urgrosh (two-handed) +32/+32/+27/+22/+17 (1d4+14/19-20/×3)
      entries:
      - - damage: 1d4+14
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 dwarven urgrosh (two-handed)
      bonus:
      - 32
      - 32
      - 27
      - 22
      - 17
  - - text: +1 spiked armor +28/+28/+23/+18/+13 (1d4+8)
      entries:
      - - damage: 1d4+8
      attack: +1 spiked armor
      bonus:
      - 28
      - 28
      - 23
      - 18
      - 13
  ranged:
  - - text: dart +27/+27/+22/+17/+12 (1d4+7)
      entries:
      - - damage: 1d4+7
      attack: dart
      bonus:
      - 27
      - 27
      - 22
      - 17
      - 12
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - weapon training (double +4, thrown +3, close +2, hammers +1)
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 11
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 19
    concentration: 20
tactics:
  Before Combat: The fighter drinks his potions of barkskin and bear's endurance,
    then activates his ring of blinking and boots of speed.
  During Combat: The fighter starts off with a Dazzling Display, then engages in melee,
    fighting less armored enemies first. He deals most of his attacks with the spear
    end of his weapon.
  Base Statistics: Without barkskin, bear's endurance, blink from his ring of blinking,
    and haste from his boots of speed, the fighter's statistics are AC 28, touch 17,
    flat-footed 24; hp 166; Fort +18, Ref +13; Defensive Abilities no blink; Speed
    20 ft.; Melee +2 dwarven urgrosh +29/+24/+19/+14 (1d4+12/19-20/×3), +2 dwarven
    urgrosh +29 (1d6+12/19-20/×3) or +2 dwarven urgrosh (two-handed) +31/+26/+21/+16
    (1d4+14/19-20/×3) or +1 spiked armor +27/+22/+17/+12 (1d4+8); Ranged dart +26/+21/+16/+11
    (1d4+7); Con 16; CMB +22; CMD 38.
ability_scores:
  STR: 18
  DEX: 16
  CON: 20
  INT: 12
  WIS: 8
  CHA: 12
BAB: 19
CMB: 23
CMD: 39
feats:
- name: Blind-Fight
- name: Dazzling Display
- name: Diehard
- name: Disruptive
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Exotic Weapon Proficiency (dwarven urgrosh)
- name: Improved Critical (dwarven urgrosh)
- name: Improved Initiative
- name: Iron Will
- name: Nimble Moves
- name: Persuasive
- name: Power Attack
- name: Quick Draw
- name: Spellbreaker
- name: Step Up
- name: Two-Weapon Fighting
- name: Weapon Focus (dwarven urgrosh)
- name: Weapon Specialization (dwarven urgrosh)
skills:
  Bluff: 19
  Diplomacy: 18
  Intimidate: 30
  Knowledge (local): 13
  Perception: 1
  Profession (gambler): 5
  Sense Motive: 18
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- armor mastery
- armor training 4
gear:
  combat:
  - potion of barkskin (CL 12th)
  - potion of bear's endurance
  - potions of cure serious wounds (2)
  other:
  - +2 full plate with +1 armor spikes
  - +2/+2 dwarven urgrosh
  - darts (10)
  - belt of giant strength +4
  - boots of speed
  - circlet of persuasion
  - cloak of resistance +4
  - hat of disguise
  - ring of blinking
  - ring of protection +2
  - ruby signet ring (worth 1,000 gp)
  - 5,075 gp
desc_long: Though most criminal masterminds work behind the scenes, crime lords don't
  mind getting their hands dirty.

---

# Crime Lord

**Source** NPC Codex pg. 94
**XP** 153,600
Gnome _[[classes/Fighter|fighter]]_ 19

N Small humanoid (gnome)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +1

##### Defense

**AC** 34, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+11 armor, +2 deflection, +3 Dex, +2 _[[feats/Dodge|dodge]]_, +5 natural, +1 size)
**hp** 204 (19d10+95)
**Fort** +20, **Ref** +14, **Will** +11; +2 vs. illusions, +5 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** _[[spells/Blink|blink]]_, bravery +5, defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants); **DR** 5/—

##### Offense
**Speed** 40 ft.
**Melee** +2 _[[items/Weapon/Dwarven urgrosh|dwarven urgrosh]]_ +30/+30/+25/+20/+15 (1d4+12/19–20/×3), +2 _dwarven urgrosh_ +30 (1d6+12/19–20/×3) or +2 _dwarven urgrosh_ (two-handed) +32/+32/+27/+22/+17 (1d4+14/19–20/×3) or +1 _[[items/Weapon/Spiked armor|spiked armor]]_ +28/+28/+23/+18/+13 (1d4+8)
**Ranged** _[[items/Weapon/Dart|dart]]_ +27/+27/+22/+17/+12 (1d4+7)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, weapon _training_ (double +4, thrown +3, close +2, hammers +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +20)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_

### Tactics

**Before Combat **The _fighter_ drinks his potions of _[[spells/Barkskin|barkskin]]_ and bear’s _[[feats/Endurance|endurance]]_, then activates his _[[items/Ring/Ring of Blinking|ring of blinking]]_ and _[[items/Wondrous Item/Boots of Speed|boots of speed]]_.
**During Combat **The _fighter_ starts off with a _[[feats/Dazzling Display|Dazzling Display]]_, then engages in melee, fighting less armored enemies first. He deals most of his attacks with the _[[items/Weapon/Spear|spear]]_ end of his weapon.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _blink_ from his _ring of blinking_, and _[[spells/Haste|haste]]_ from his _boots of speed_, the _fighter_’s statistics are **AC **28, touch 17, _flat-footed_ 24; **hp **166; **Fort **+18, **Ref **+13; **Defensive Abilities **no _blink_; **Speed **20 ft.; **Melee** +2 _dwarven urgrosh_ +29/+24/+19/+14 (1d4+12/19–20/×3), +2 _dwarven urgrosh_ +29 (1d6+12/19–20/×3) or +2 _dwarven urgrosh_ (two-handed) +31/+26/+21/+16 (1d4+14/19–20/×3) or +1 _spiked armor_ +27/+22/+17/+12 (1d4+8); **Ranged **_dart_ +26/+21/+16/+11 (1d4+7); **Con **16; **CMB** +22; **CMD **38.

##### Statistics
**Str** 18, **Dex** 16, **Con** 20, **Int** 12, **Wis** 8, **Cha** 12
**Base Atk** +19; **CMB** +23; **CMD** 39
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _Dazzling Display_, _[[feats/Diehard|Diehard]]_, _[[feats/Disruptive|Disruptive]]_, _Dodge_, _[[feats/Double Slice|Double Slice]]_, _Endurance_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (_dwarven urgrosh_), _[[feats/Improved Critical|Improved Critical]]_ (_dwarven urgrosh_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[items/Weapon/Spellbreaker|Spellbreaker]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dwarven urgrosh_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_dwarven urgrosh_)
**Skills** Bluff +19, Diplomacy +18, Intimidate +30, Knowledge (local) +13, Perception +1, Profession (_[[npcs/Gambler|gambler]]_) +5, Sense Motive +18
**Languages** Common, Gnome, Sylvan
**SQ** armor mastery, armor _training_ 4
**Combat Gear** potion of _barkskin_ (CL 12th), potion of bear’s _endurance_, potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2); **Other Gear** +2 _[[items/Armor/Full plate|full plate]]_ with +1 armor spikes, +2/+2 _dwarven urgrosh_, darts (10), _[[items/Wondrous Item/Belt of Giant Strength +4|belt of giant strength +4]]_, _boots of speed_, _[[items/Wondrous Item/Circlet of Persuasion|circlet of persuasion]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Hat of Disguise|hat of disguise]]_, _ring of blinking_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, ruby _[[items/Mundane/Signet ring|signet ring]]_ (worth 1,000 gp), 5,075 gp

Though most criminal masterminds work behind the scenes, crime lords don’t mind getting their hands dirty.