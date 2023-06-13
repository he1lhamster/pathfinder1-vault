---
cssclass: [monsters]
title1: Bugbear, Bugbear Tyrant
title2: Bugbear Tyrant
CR: 13
sources:
- name: Monster Codex
  page: 27
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 25600
race: Male
classes:
- bugbear antipaladin (fearmonger) 12 (Pathfinder RPG Advanced Player's Guide 118,
  see page 20)
alignment: CE
size: Medium
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 1
senses:
  darkvision: 60
  scent: true
auras:
- name: cowardice
  radius: 10
- name: despair
  radius: 10
- name: vengeance
  radius: 10
AC:
  AC: 27
  touch: 12
  flat_footed: 26
  components:
    armor: 11
    deflection: 1
    dex: 1
    natural: 4
HP:
  HP: 136
  long: 3d8+12d10+57
  HD: 15
saves:
  fort: 15
  ref: 11
  will: 11
immunities:
- disease
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 falchion +22/+17/+12 (2d4+9/18-20)
      entries:
      - - damage: 2d4+9
          crit_range: 18-20
      attack: +2 falchion
      bonus:
      - 22
      - 17
      - 12
  ranged:
  - - text: mwk javelin +16 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: mwk javelin
      bonus:
      - 16
  special:
  - channel negative energy (DC 18, 6d6)
  - smite good 4/day (+2 attack and AC, +12 damage)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: At will
  sources:
  - name: default
    CL: 12
    concentration: 14
spells:
  entries:
  - name: isolate
    source: Antipaladin
    level: 3
    DC: 15
  - superscripts:
    - APG
    name: corruption resistance
    source: Antipaladin
    level: 2
  - superscripts:
    - UC
    name: litany of warding
    source: Antipaladin
    level: 2
  - name: scare
    source: Antipaladin
    level: 2
    DC: 14
  - name: disguise self
    source: Antipaladin
    level: 1
  - superscripts:
    - UC
    name: litany of sloth
    source: Antipaladin
    level: 1
  - superscripts:
    - UC
    name: litany of weakness
    source: Antipaladin
    level: 1
  sources:
  - name: Antipaladin
    type: prepared
    CL: 9
    concentration: 11
tactics:
  Before Combat: The bugbear tyrant uses disguise self to get close to unsuspecting
    enemies.
  During Combat: Using the fear effects at his disposal, the bugbear tyrant increases
    his damage with Cruel Opportunist and Hurtful, while regaining hit points using
    his feed on fear ability. The tyrant cares little about the lives of those he
    fights alongside; if he must retreat, he allows his allies to die.
ability_scores:
  STR: 20
  DEX: 12
  CON: 16
  INT: 12
  WIS: 8
  CHA: 15
BAB: 14
CMB: 19
CMD: 30
feats:
- name: Cruel Opportunist
- name: Dazzling Display
- name: Hurtful
- name: Intimidating Prowess
- name: Pile On
- name: Power Attack
- name: Visceral Threat
- name: Weapon Focus (falchion)
skills:
  Intimidate: 26
  Perception: 11
  Stealth: 15
languages:
- Abyssal
- Common
- Goblin
special_qualities:
- cruelties (dazed, frightened, panicked)
- feed on fear (6 hp)
- fiendish boon (weapon +3, 2/day)
- stalker
gear:
  combat:
  - elixir of oppression
  - potion of cure moderate wounds
  other:
  - +2 full plate
  - +2 falchion
  - mwk javelins (2)
  - amulet of natural armor +1
  - boots of striding and springing
  - cloak of resistance +1
  - ring of protection +1
  - 973 gp
ecology:
  environment: temperate mountains
desc_long: |-
  Though he draws other bugbears to follow him by his charismatic presence, a bugbear tyrant truly makes his legend by defeating and torturing other creatures. Bugbears care far less about gaining territory or forcing surrender than they do about inflicting pain and collecting heads. They're quick to recognize and appreciate the cruelty in an antipaladin's heart, and the supernatural ability to inflict pain on others that he brings to bear.

  The tyrant doesn't reserve his violence for enemies of the bugbear race. It doesn't take much for him to turn on his underlings and slice them up for fun, especially if he's growing bored.

---

# Bugbear, Bugbear Tyrant

**Source** Monster Codex pg. 27
**XP** 25,600
Male _[[monsters/Bugbear|bugbear]]_ _[[classes/Antipaladin|antipaladin]]_ (fearmonger) 12 (Pathfinder RPG Advanced Player’s Guide 118, see page 20)
CE Medium humanoid (goblinoid)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +11
**Aura** cowardice (10 ft.), despair (10 ft.), _[[feats/Vengeance|vengeance]]_ (10 ft.)

##### Defense

**AC** 27, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+11 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +4 natural)
**hp** 136 (15 HD; 3d8+12d10+57)
**Fort** +15, **Ref** +11, **Will** +11
**Immune** disease

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Falchion|falchion]]_ +22/+17/+12 (2d4+9/18–20)
**Ranged** mwk _[[items/Weapon/Javelin|javelin]]_ +16 (1d6+5)
**Special Attacks** channel negative energy (DC 18, 6d6), smite good 4/day (+2 attack and AC, +12 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
At will—_[[spells/Detect Good|detect good]]_
**_Antipaladin_ Spells Prepared **(CL 9th; concentration +11)
3rd—_[[spells/Isolate|isolate]]_ (DC 15)
2nd—_[[spells/Corruption Resistance|corruption resistance]]_, _[[spells/Litany of Warding|litany of warding]]_, _[[spells/Scare|scare]]_ (DC 14)
1st—_[[spells/Disguise Self|disguise self]]_, _[[spells/Litany of Sloth|litany of sloth]]_, _[[spells/Litany of Weakness|litany of weakness]]_

### Tactics

**Before Combat** The _bugbear_ tyrant uses _disguise self_ to get close to unsuspecting enemies.
 **During Combat** Using the _[[universal monster rules/Fear|fear]]_ effects at his disposal, the _bugbear_ tyrant increases his damage with _[[items/Weapon Magic Abilities/Cruel|Cruel]]_ Opportunist and _[[feats/Hurtful|Hurtful]]_, while regaining hit points using his feed on _fear_ ability. The tyrant cares little about the lives of those he fights alongside; if he must retreat, he allows his allies to die.

##### Statistics
**Str** 20, **Dex** 12, **Con** 16, **Int** 12, **Wis** 8, **Cha** 15
**Base Atk** +14; **CMB** +19; **CMD** 30
**Feats** _Cruel_ Opportunist, _[[feats/Dazzling Display|Dazzling Display]]_, _Hurtful_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Pile On|Pile On]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Visceral Threat|Visceral Threat]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** Intimidate +26, Perception +11, Stealth +15
**Languages** Abyssal, Common, _[[monsters/Goblin|Goblin]]_
**SQ** cruelties (_[[conditions/Dazed|dazed]]_, _[[conditions/Frightened|frightened]]_, _[[conditions/Panicked|panicked]]_), feed on _fear_ (6 hp), fiendish boon (weapon +3, 2/day), stalker
**Combat Gear** _[[items/Wondrous Item/Elixir of Oppression|elixir of oppression]]_, potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +2 _[[items/Armor/Full plate|full plate]]_, +2 _falchion_, mwk javelins (2), _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 973 gp

##### Ecology

**Environment** temperate mountains

##### Description

Though he draws other bugbears to follow him by his charismatic presence, a _bugbear_ tyrant truly makes his legend by defeating and torturing other creatures. Bugbears care far less about gaining territory or forcing surrender than they do about inflicting pain and collecting heads. They’re quick to recognize and appreciate the _[[feats/Cruelty|cruelty]]_ in an _antipaladin_’s heart, and the supernatural ability to _[[spells/Inflict Pain|inflict pain]]_ on others that he brings to bear.

The tyrant doesn’t reserve his violence for enemies of the _bugbear_ race. It doesn’t take much for him to turn on his underlings and slice them up for fun, especially if he’s _[[items/Weapon Magic Abilities/Growing|growing]]_ bored.