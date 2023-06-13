---
cssclass: [monsters]
title1: Desert Protector
title2: Desert Protector
CR: 7
sources:
- name: NPC Codex
  page: 115
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Human
classes:
- paladin of Sarenrae 8
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 3
auras:
- name: courage
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 17
  touch: 10
  flat_footed: 17
  components:
    armor: 7
    deflection: 1
    dex: -1
HP:
  HP: 64
  long: 8d10+16
saves:
  fort: 10
  ref: 4
  will: 11
immunities:
- charm
- disease
- fear
speeds:
  base: 20
attacks:
  melee:
  - - text: 1 falchion +14/+9 (2d4+7/18-20)
      entries:
      - - damage: 2d4+7
          crit_range: 18-20
      count: 1
      attack: falchion
      bonus:
      - 14
      - 9
  ranged:
  - - text: mwk starknife +8/+3 (1d4+4/×3)
      entries:
      - - damage: 1d4+4
          crit_multiplier: 3
      attack: mwk starknife
      bonus:
      - 8
      - 3
  special:
  - channel positive energy (DC 16, 4d6)
  - smite evil 3/day (+2 attack and AC, +8 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 8
    concentration: 10
spells:
  entries:
  - name: delay poison
    source: Paladin
    level: 2
  - name: resist energy
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: lesser restoration
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 5
    concentration: 7
tactics:
  During Combat: The paladin draws attention away from weaker allies, and heals allies
    who are competent fighters.
ability_scores:
  STR: 18
  DEX: 8
  CON: 12
  INT: 10
  WIS: 14
  CHA: 14
BAB: 8
CMB: 12
CMD: 22
feats:
- name: Cleave
- name: Improved Initiative
- name: Power Attack
- name: Toughness
- name: Weapon Focus (falchion)
skills:
  Diplomacy: 10
  Heal: 8
  Knowledge (religion): 11
  Perception: 8
  Sense Motive: 13
  Survival: 4
languages:
- Common
special_qualities:
- aura
- code of conduct
- divine bond (weapon +2, 1/day)
- lay on hands (4d6, 6/day)
- mercies (diseased, sickened)
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 breastplate
  - +1 falchion
  - masterwork starknife
  - cloak of resistance +1
  - ring of protection +1
  - silver holy symbol
  - 426 gp
desc_long: A desert protector watches over the bodies and souls of a nomadic desert
  community.

---

# Desert Protector

**Source** NPC Codex pg. 115
**XP** 3,200
Human _[[classes/Paladin|paladin]]_ of Sarenrae 8

LG Medium humanoid (human)
**Init** +3; **Senses** Perception +8
**Aura** courage (10 ft.), resolve (10 ft.)

##### Defense

**AC** 17, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 armor, +1 _[[spells/Deflection|deflection]]_, –1 Dex)
**hp** 64 (8d10+16)
**Fort** +10, **Ref** +4, **Will** +11
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** 1 _[[items/Weapon/Falchion|falchion]]_ +14/+9 (2d4+7/18–20)
**Ranged** mwk _[[items/Weapon/Starknife|starknife]]_ +8/+3 (1d4+4/×3)
**Special Attacks** channel positive energy (DC 16, 4d6), smite evil 3/day (+2 attack and AC, +8 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +10)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 5th; concentration +7)
2nd—_[[spells/Delay Poison|delay poison]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Bless|bless]]_, lesser _[[spells/Restoration|restoration]]_

### Tactics

**During Combat **The _paladin_ draws attention away from weaker allies, and heals allies who are competent fighters.

##### Statistics
**Str** 18, **Dex** 8, **Con** 12, **Int** 10, **Wis** 14, **Cha** 14
**Base Atk** +8; **CMB** +12; **CMD** 22
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** Diplomacy +10, _[[spells/Heal|Heal]]_ +8, Knowledge (religion) +11, Perception +8, Sense Motive +13, Survival +4
**Languages** Common
**SQ** aura, code of conduct, divine bond (weapon +2, 1/day), lay on hands (4d6, 6/day), mercies (diseased, _[[conditions/Sickened|sickened]]_)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _falchion_, masterwork _starknife_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver holy symbol, 426 gp

A _[[npcs/Desert Protector|desert protector]]_ watches over the bodies and souls of a nomadic desert community.