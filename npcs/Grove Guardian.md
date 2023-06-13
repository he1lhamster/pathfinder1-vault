---
cssclass: [monsters]
title1: Grove Guardian
title2: Grove Guardian
CR: 17
sources:
- name: NPC Codex
  page: 109
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Half-elf
classes:
- monk 18
alignment: LN
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 31
  touch: 27
  flat_footed: 24
  components:
    armor: 4
    deflection: 1
    dex: 6
    dodge: 1
    monk: 4
    wis: 5
HP:
  HP: 148
  long: 18d8+64
saves:
  fort: 16
  ref: 19
  will: 18
  other: +4 vs. enchantments
defensive_abilities:
- improved evasion
immunities:
- disease
- poison
SR: 28
speeds:
  base: 90
attacks:
  melee:
  - - text: +2 unarmed strike +21/+16/+11 (2d8+4)
      entries:
      - - damage: 2d8+4
      attack: +2 unarmed strike
      bonus:
      - 21
      - 16
      - 11
  - - text: mwk cold iron dagger +20/+15/+10 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: mwk cold iron dagger
      bonus:
      - 20
      - 15
      - 10
  - - text: +2 unarmed strike flurry of blows +24/+24/+19/+19/+14/+14/+9 (2d8+4)
      entries:
      - - damage: 2d8+4
      attack: +2 unarmed strike flurry of blows
      bonus:
      - 24
      - 24
      - 19
      - 19
      - 14
      - 14
      - 9
  ranged:
  - - text: mwk cold iron dagger +20/+15/+10 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: mwk cold iron dagger
      bonus:
      - 20
      - 15
      - 10
  special:
  - flurry of blows
  - quivering palm (1/day, DC 24)
  - stunning fist (18/day, DC 24)
tactics:
  Before Combat: The monk attempts to get close to an opponent through Bluff or Diplomacy,
    then drinks her potions of bear's endurance and bull's strength.
  During Combat: Against a single foe, the monk opens with Stunning Fist augmented
    with Improved Vital Strike, then tries to grapple the stunned foe. Against multiple
    opponents, she uses flurry of blows to attempt trip and disarm maneuvers, making
    as many foes prone or weaponless as possible, then strikes when those opponents
    provoke attacks of opportunity. Against foes too large to grapple or immune to
    stunning, she uses her ki pool to boost her movement, then Spring Attack with
    Improved Vital Strike to make hit and run attacks.
  Base Statistics: Without bear's endurance and bull's strength, the monk's statistics
    are hp 112; Fort +14; Melee +2 unarmed strike +21/+16/+11 (2d8+2) or mwk cold
    iron dagger +20/+15/+10 (1d4/19-20) or flurry of blows (+2 unarmed strike) +22/+22/+17/+17/+12/+12/+7
    (2d8+2); Ranged mwk cold iron dagger +20/+15/+10 (1d4/19-20); Str 10, Con 12;
    CMD 45 (47 vs. trip); Skills Climb +4, Swim +5.
ability_scores:
  STR: 14
  DEX: 22
  CON: 16
  INT: 13
  WIS: 20
  CHA: 11
BAB: 13
CMB: 24
CMB_other: +26 grapple, +28 trip
CMD: 47
CMD_other: 49 vs. trip
feats:
- name: Agile Maneuvers
- name: Combat Expertise
- name: Combat Reflexes
- name: Defensive Combat Training
- name: Dodge
- name: Greater Trip
- name: Improved Bull Rush
- name: Improved Disarm
- name: Improved Grapple
- name: Improved Trip
- name: Improved Unarmed Strike
- name: Improved Vital Strike
- name: Skill Focus (Acrobatics)
- name: Spring Attack
- name: Strike Back
- name: Stunning Fist
- name: Vital Strike
- name: Weapon Finesse
skills:
  Acrobatics: 33
    when jumping: 75
  Bluff: 8
  Climb: 4
  Diplomacy: 8
  Knowledge (history): 8
  Knowledge (local): 6
  Knowledge (religion): 7
  Perception: 24
  Perform (dance): 6
  Sense Motive: 26
  Stealth: 23
  Swim: 5
languages:
- Common
- Elven
- Gnome
- tongue of the sun and moon
special_qualities:
- abundant step
- diamond body
- diamond soul
- elf blood
- fast movement
- high jump
- ki pool (14 points, adamantine, lawful, magic)
- maneuver training
- purity of body
- slow fall 90 ft.
- timeless body
- wholeness of body
gear:
  combat:
  - potion of bear's endurance
  - potion of bull's strength
  - potions of cure moderate wounds (2)
  - potions of entropic shield (2)
  - universal solvent (2)
  other:
  - masterwork cold iron dagger
  - amulet of mighty fists +2
  - belt of incredible dexterity +6
  - bracers of armor +4
  - cloak of resistance +2
  - headband of inspired wisdom +4
  - ring of protection +1
  - 298 gp
desc_long: Devoted to the protection of druidic groves or other sacred places of power,
  grove guardians do anything necessary to protect what they guard.

---

# Grove Guardian

**Source** NPC Codex pg. 109
**XP** 102,400
Half-elf _[[classes/Monk|monk]]_ 18

LN Medium humanoid (elf, human)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24

##### Defense

**AC** 31, touch 27, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +6 Dex, +1 _[[feats/Dodge|dodge]]_, +4 _monk_, +5 Wis)
**hp** 148 (18d8+64)
**Fort** +16, **Ref** +19, **Will** +18; +4 vs. enchantments
**Defensive Abilities** improved evasion; **Immune** disease, poison; **SR** 28

##### Offense
**Speed** 90 ft.
**Melee** +2 unarmed strike +21/+16/+11 (2d8+4) or mwk cold iron _[[items/Weapon/Dagger|dagger]]_ +20/+15/+10 (1d4+2/19–20) or +2 unarmed strike flurry of blows +24/+24/+19/+19/+14/+14/+9 (2d8+4)
**Ranged** mwk cold iron _dagger_ +20/+15/+10 (1d4+2/19–20)
**Special Attacks** flurry of blows, quivering palm (1/day, DC 24), _[[feats/Stunning Fist|stunning fist]]_ (18/day, DC 24)

### Tactics

**Before Combat **The _monk_ attempts to get close to an opponent through Bluff or Diplomacy, then drinks her potions of bear’s _[[feats/Endurance|endurance]]_ and bull’s strength.
**During Combat **Against a single foe, the _monk_ opens with _Stunning Fist_ augmented with _[[feats/Improved Vital Strike|Improved Vital Strike]]_, then tries to grapple the _[[conditions/Stunned|stunned]]_ foe. Against multiple opponents, she uses flurry of blows to attempt _[[universal monster rules/Trip|trip]]_ and disarm maneuvers, making as many foes _[[conditions/Prone|prone]]_ or weaponless as possible, then strikes when those opponents provoke attacks of opportunity. Against foes too large to grapple or immune to stunning, she uses her ki pool to boost her movement, then _[[feats/Spring Attack|Spring Attack]]_ with _Improved Vital Strike_ to make hit and run attacks.
**Base Statistics **Without bear’s _endurance_ and bull’s strength, the _monk_’s statistics are **hp **112; **Fort **+14; **Melee **+2 unarmed strike +21/+16/+11 (2d8+2) or mwk cold iron _dagger_ +20/+15/+10 (1d4/19–20) or flurry of blows (+2 unarmed strike) +22/+22/+17/+17/+12/+12/+7 (2d8+2); **Ranged **mwk cold iron _dagger_ +20/+15/+10 (1d4/19–20); Str 10, Con 12; CMD 45 (47 vs. _trip_); **Skills **_[[universal monster rules/Climb|Climb]]_ +4, Swim +5.

##### Statistics
**Str** 14, **Dex** 22, **Con** 16, **Int** 13, **Wis** 20, **Cha** 11
**Base Atk** +13; **CMB** +24 (+26 grapple, +28 _trip_); **CMD** 47 (49 vs. _trip_)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _Dodge_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Grapple|Improved Grapple]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _Improved Vital Strike_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics), _Spring Attack_, _[[feats/Strike Back|Strike Back]]_, _Stunning Fist_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +33 (+75 when jumping), Bluff +8, _Climb_ +4, Diplomacy +8, Knowledge (history) +8, Knowledge (local) +6, Knowledge (religion) +7, Perception +24, Perform (dance) +6, Sense Motive +26, Stealth +23, Swim +5
**Languages** Common, Elven, Gnome; tongue of the sun and moon
**SQ** abundant step, diamond body, diamond soul, elf blood, fast movement, high _[[spells/Jump|jump]]_, ki pool (14 points, adamantine, lawful, magic), maneuver _[[items/Weapon Magic Abilities/Training|training]]_, purity of body, _[[spells/Slow|slow]]_ fall 90 ft., timeless body, wholeness of body
**Combat Gear** potion of bear’s _endurance_, potion of bull’s strength, potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potions of _[[spells/Entropic Shield|entropic shield]]_ (2), _[[items/Wondrous Item/Universal Solvent|universal solvent]]_ (2); **Other Gear** masterwork cold iron _dagger_, _[[items/Wondrous Item/Amulet of Mighty Fists +2|amulet of mighty fists +2]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +6|belt of incredible dexterity +6]]_, _[[items/Wondrous Item/Bracers of Armor +4|bracers of armor +4]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 298 gp

Devoted to the protection of druidic groves or other _[[items/Weapon Magic Abilities/Sacred|sacred]]_ places of power, grove guardians do anything necessary to protect what they _[[npcs/Guard|guard]]_.