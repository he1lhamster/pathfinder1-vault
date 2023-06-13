---
cssclass: [monsters]
title1: Monastic Sniper
title2: Monastic Sniper
CR: 12
sources:
- name: NPC Codex
  page: 104
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Elf
classes:
- monk 13
alignment: LN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 22
  flat_footed: 20
  components:
    armor: 2
    deflection: 1
    dex: 3
    dodge: 1
    monk: 3
    wis: 4
HP:
  HP: 85
  long: 13d8+23
saves:
  fort: 11
  ref: 13
  will: 14
  other: +4 vs. enchantments
defensive_abilities:
- improved evasion
immunities:
- disease
- poison
- sleep
SR: 23
speeds:
  base: 70
attacks:
  melee:
  - - text: +1 rapier +12/+7 (1d6+3/15-20)
      entries:
      - - damage: 1d6+3
          crit_range: 15-20
      attack: +1 rapier
      bonus:
      - 12
      - 7
  - - text: unarmed strike +11/+6 (2d6+2)
      entries:
      - - damage: 2d6+2
      attack: unarmed strike
      bonus:
      - 11
      - 6
  - - text: unarmed strike flurry of blows +13/+13/+8/+8/+3 (2d6+2)
      entries:
      - - damage: 2d6+2
      attack: unarmed strike flurry of blows
      bonus:
      - 13
      - 13
      - 8
      - 8
      - 3
  ranged:
  - - text: mwk composite longbow +13/+8 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 13
      - 8
  - - text: mwk shuriken +13/+8 (1d2+2)
      entries:
      - - damage: 1d2+2
      attack: mwk shuriken
      bonus:
      - 13
      - 8
  - - text: mwk shuriken flurry of blows +14/+14/+9/+9/+4 (1d2+2)
      entries:
      - - damage: 1d2+2
      attack: mwk shuriken flurry of blows
      bonus:
      - 14
      - 14
      - 9
      - 9
      - 4
  special:
  - flurry of blows
  - stunning fist (13/day, DC 20)
tactics:
  Before Combat: The monk tries to find cover from which to snipe at his enemies,
    using abundant step in conjunction with Stealth to make enemies think they face
    multiple attackers.
  During Combat: If the monk must enter melee, he uses Stunning Fist against flat-footed
    or disadvantaged opponents. If successful, he then uses his rapier in conjunction
    with Power Attack and Vital Strike. If he's outnumbered, the monk uses Spring
    Attack and Vital Strike to whittle down his foes.
ability_scores:
  STR: 14
  DEX: 16
  CON: 12
  INT: 11
  WIS: 18
  CHA: 10
BAB: 9
CMB: 15
CMB_other: +17 disarm
CMD: 33
CMD_other: 35 vs. disarm
feats:
- name: Combat Reflexes
- name: Deadly Aim
- name: Dodge
- name: Improved Critical (rapier)
- name: Improved Disarm
- name: Improved Unarmed Strike
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Quick Draw
- name: Spring Attack
- name: Stunning Fist
- name: Vital Strike
skills:
  Acrobatics: 15
    when jumping: 44
  Bluff: 5
  Climb: 8
  Diplomacy: 10
  Knowledge (history): 5
  Knowledge (religion): 5
  Linguistics: 2
  Perception: 19
  Sense Motive: 15
  Stealth: 15
languages:
- Common
- Dwarven
- Elven
- Sylvan
special_qualities:
- abundant step
- diamond body
- diamond soul
- elven magic
- fast movement
- high jump
- ki pool (10 points, lawful, magic)
- maneuver training
- purity of body
- slow fall 60 ft.
- weapon familiarity
- wholeness of body
gear:
  combat:
  - elixir of truth
  - potion of blur
  - potions of comprehend languages (2)
  - potions of cure moderate wounds (2)
  - potion of cure serious wounds
  - potion of glibness
  other:
  - +1 rapier
  - masterwork composite longbow (+2 Str) with 20 arrows
  - masterwork shuriken (50)
  - belt of incredible dexterity +2
  - boots of elvenkind
  - bracers of armor +2
  - cloak of resistance +2
  - headband of inspired wisdom +2
  - ring of protection +1
  - 179 gp
desc_long: Both archers and diplomats, monastic snipers consider a well-placed warning
  shot the ideal method to open the channels of diplomacy from a position of power.

---

# Monastic Sniper

**Source** NPC Codex pg. 104
**XP** 19,200
Elf _[[classes/Monk|monk]]_ 13

LN Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 24, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +3 _monk_, +4 Wis)
**hp** 85 (13d8+23)
**Fort** +11, **Ref** +13, **Will** +14; +4 vs. enchantments
**Defensive Abilities** improved evasion; **Immune** disease, poison, sleep; **SR** 23

##### Offense
**Speed** 70 ft.
**Melee** +1 _[[items/Weapon/Rapier|rapier]]_ +12/+7 (1d6+3/15–20) or unarmed strike +11/+6 (2d6+2) or unarmed strike flurry of blows +13/+13/+8/+8/+3 (2d6+2)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +13/+8 (1d8+2/×3) or mwk shuriken +13/+8 (1d2+2) or mwk shuriken flurry of blows +14/+14/+9/+9/+4 (1d2+2)
**Special Attacks** flurry of blows, _[[feats/Stunning Fist|stunning fist]]_ (13/day, DC 20)

### Tactics

**Before Combat **The _monk_ tries to find cover from which to snipe at his enemies, using abundant step in conjunction with Stealth to make enemies think they face multiple attackers.
**During Combat **If the _monk_ must enter melee, he uses _Stunning Fist_ against _flat-footed_ or disadvantaged opponents. If successful, he then uses his _rapier_ in conjunction with _[[feats/Power Attack|Power Attack]]_ and _[[feats/Vital Strike|Vital Strike]]_. If he’s outnumbered, the _monk_ uses _[[feats/Spring Attack|Spring Attack]]_ and _Vital Strike_ to whittle down his foes.

##### Statistics
**Str** 14, **Dex** 16, **Con** 12, **Int** 11, **Wis** 18, **Cha** 10
**Base Atk** +9; **CMB** +15 (+17 disarm); **CMD** 33 (35 vs. disarm)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_rapier_), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _Power Attack_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _Spring Attack_, _Stunning Fist_, _Vital Strike_
**Skills** Acrobatics +15 (+44 when jumping), Bluff +5, _[[universal monster rules/Climb|Climb]]_ +8, Diplomacy +10, Knowledge (history, religion) +5, Linguistics +2, Perception +19, Sense Motive +15, Stealth +15
**Languages** Common, Dwarven, Elven, Sylvan
**SQ** abundant step, diamond body, diamond soul, elven magic, fast movement, high _[[spells/Jump|jump]]_, ki pool (10 points, lawful, magic), maneuver _[[items/Weapon Magic Abilities/Training|training]]_, purity of body, _[[spells/Slow|slow]]_ fall 60 ft., weapon familiarity, wholeness of body
**Combat Gear** _[[items/Wondrous Item/Elixir of Truth|elixir of truth]]_, potion of _[[spells/Blur|blur]]_, potions of _[[spells/Comprehend Languages|comprehend languages]]_ (2), potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _[[spells/Glibness|glibness]]_; **Other Gear** +1 _rapier_, masterwork _composite longbow_ (+2 Str) with 20 arrows, masterwork shuriken (50), _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Boots of Elvenkind|boots of elvenkind]]_, _[[items/Wondrous Item/Bracers of Armor +2|bracers of armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 179 gp

Both archers and diplomats, monastic snipers consider a well-placed _[[feats/Warning Shot|warning shot]]_ the ideal method to open the channels of diplomacy from a position of power.