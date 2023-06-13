---
cssclass: [monsters]
title1: Demon Hunter
title2: Demon Hunter
CR: 19
sources:
- name: NPC Codex
  page: 127
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Human
classes:
- paladin 20
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
senses:
  darkvision: 60
auras:
- name: courage
  radius: 10
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
- name: righteousness
  radius: 10
AC:
  AC: 30
  touch: 14
  flat_footed: 30
  components:
    armor: 14
    deflection: 4
    natural: 2
HP:
  HP: 214
  long: 20d10+100
saves:
  fort: 23
  ref: 14
  will: 19
DR:
- amount: 10
  weakness: evil
immunities:
- charm
- compulsion
- disease
- fear
- poison
resistances:
  electricity: 30
  fire: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: +4 cold iron evil outsider-bane greatsword +32/+27/+22/+17 (2d6+14/17-20)
      entries:
      - - damage: 2d6+14
          crit_range: 17-20
      attack: +4 cold iron evil outsider-bane greatsword
      bonus:
      - 32
      - 27
      - 22
      - 17
  ranged:
  - - text: +1 shortbow +21/+16/+11/+6 (1d6+1/×3)
      entries:
      - - damage: 1d6+1
          crit_multiplier: 3
      attack: +1 shortbow
      bonus:
      - 21
      - 16
      - 11
      - 6
  special:
  - channel positive energy (DC 23, 60 points)
  - smite evil 7/day (+3 attack and AC, +20 damage, banish evil outsiders)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 20
    concentration: 23
spells:
  entries:
  - name: break enchantment
    source: Paladin
    level: 4
  - name: death ward
    source: Paladin
    level: 4
  - name: dispel evil
    source: Paladin
    level: 4
  - name: daylight
    source: Paladin
    level: 3
    count: 2
  - name: greater magic weapon
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
  - name: eagle's splendor
    source: Paladin
    level: 2
    count: 2
  - name: protection from energy
    source: Paladin
    level: 2
    count: 2
  - name: divine favor
    source: Paladin
    level: 1
    count: 3
  - name: lesser restoration
    source: Paladin
    level: 1
    count: 2
  sources:
  - name: Paladin
    type: prepared
    CL: 17
    concentration: 20
tactics:
  Before Combat: The paladin casts delay poison and protection from energy (electricity
    and fire) on herself, and greater magic weapon on her greatsword.
  During Combat: The paladin targets the most powerful creature present or an obviously
    demonic target. She uses her divine bond to add the brilliant energy, holy, keen,
    and speed special abilities to her greatsword as appropriate, and uses mercies
    to counteract any negative conditions or afflictions she gains.
  Base Statistics: Without delay poison, greater magic weapon, and protection from
    energy, the paladin's statistics are Immune charm, compulsion, disease, fear;
    Resist none; Melee +1 cold iron evil outsider-bane greatsword +29/+24/+19/+14
    (2d6+11/17-20).
ability_scores:
  STR: 24
  DEX: 10
  CON: 17
  INT: 12
  WIS: 8
  CHA: 16
BAB: 20
CMB: 27
CMD: 41
feats:
- name: Critical Focus
- name: Extra Lay on Hands
- name: Great Fortitude
- name: Improved Critical (greatsword)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Stunning Critical
- name: Toughness
- name: Weapon Focus (greatsword)
skills:
  Climb: 7
  Diplomacy: 11
  Heal: 7
  Intimidate: 13
  Knowledge (arcana): 6
  Knowledge (planes): 21
  Linguistics: 3
  Perception: 19
  Survival: 2
  Swim: 7
languages:
- Abyssal
- Celestial
- Common
- Infernal
special_qualities:
- aura
- code of conduct
- divine bond (weapon +6, 4/day)
- holy champion
- lay on hands (60 points, 15/day)
- mercies (dazed, nauseated, poisoned, sickened, staggered, stunned)
gear:
  combat:
  - +1 evil outsider-bane arrows (5)
  - +1 evil outsider-bane holy arrows (5)
  - +1 holy arrows (5)
  - potions of fly (2)
  other:
  - +5 full plate
  - +1 cold iron evil outsider-bane greatsword
  - +1 shortbow with 20 arrows
  - amulet of natural armor +2
  - belt of physical might +4 (Str, Con)
  - boots of striding and springing
  - cloak of resistance +3
  - goggles of night
  - phylactery of faithfulness
  - ring of protection +4
  - 4,760 gp
desc_long: The demon hunter has sworn to battle the hordes of the Abyss. Though the
  demons constantly tempt her and try to lead her from her path, she remains resolute-though
  somewhat paranoid and difficult to befriend because of the number of allies she's
  seen slain.

---

# Demon Hunter

**Source** NPC Codex pg. 127
**XP** 204,800
Human _[[classes/Paladin|paladin]]_ 20

LG Medium humanoid (human)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.), righteousness (10 ft.)

##### Defense

**AC** 30, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+14 armor, +4 _[[spells/Deflection|deflection]]_, +2 natural)
**hp** 214 (20d10+100)
**Fort** +23, **Ref** +14, **Will** +19
**DR** 10/evil; **Immune** charm, compulsion, disease, _[[universal monster rules/Fear|fear]]_, poison; **Resist** electricity 30, fire 30

##### Offense
**Speed** 30 ft.
**Melee** +4 cold iron evil outsider-bane _[[items/Weapon/Greatsword|greatsword]]_ +32/+27/+22/+17 (2d6+14/17–20)
**Ranged** +1 _[[items/Weapon/Shortbow|shortbow]]_ +21/+16/+11/+6 (1d6+1/×3)
**Special Attacks** channel positive energy (DC 23, 60 points), smite evil 7/day (+3 attack and AC, +20 damage, banish evil outsiders)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +23)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 17th; concentration +20)
4th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Dispel Evil|dispel evil]]_
3rd—_[[spells/Daylight|daylight]]_ (2), greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Prayer|prayer]]_
2nd—_[[spells/Delay Poison|delay poison]]_, _[[monsters/Eagle|eagle]]_’s splendor (2), _[[spells/Protection from Energy|protection from energy]]_ (2)
1st—_[[spells/Divine Favor|divine favor]]_ (3), lesser _[[spells/Restoration|restoration]]_ (2)

### Tactics

**Before Combat **The _paladin_ casts _delay poison_ and _protection from energy_ (electricity and fire) on herself, and greater _magic weapon_ on her _greatsword_.
**During Combat **The _paladin_ targets the most powerful creature present or an obviously demonic target. She uses her divine bond to add the _[[items/Weapon Magic Abilities/Brilliant Energy|brilliant energy]]_, holy, _[[items/Weapon Magic Abilities/Keen|keen]]_, and speed special abilities to her _greatsword_ as appropriate, and uses mercies to counteract any negative conditions or afflictions she gains.
**Base Statistics **Without _delay poison_, greater _magic weapon_, and _protection from energy_, the _paladin_’s statistics are **Immune **charm, compulsion, disease, _fear_; **Resist **none; **Melee** +1 cold iron evil outsider-bane _greatsword_ +29/+24/+19/+14 (2d6+11/17–20).

##### Statistics
**Str** 24, **Dex** 10, **Con** 17, **Int** 12, **Wis** 8, **Cha** 16
**Base Atk** +20; **CMB** +27; **CMD** 41
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extra Lay On Hands|Extra Lay on Hands]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greatsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greatsword_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +7, Diplomacy +11, _[[spells/Heal|Heal]]_ +7, Intimidate +13, Knowledge (arcana) +6, Knowledge (planes) +21, Linguistics +3, Perception +19, Survival +2, Swim +7
**Languages** Abyssal, Celestial, Common, Infernal
**SQ** aura, code of conduct, divine bond (weapon +6, 4/day), holy _[[items/Armor Magic Abilities/Champion|champion]]_, lay on hands (60 points, 15/day), mercies (_[[conditions/Dazed|dazed]]_, _[[conditions/Nauseated|nauseated]]_, poisoned, _[[conditions/Sickened|sickened]]_, _[[conditions/Staggered|staggered]]_, _[[conditions/Stunned|stunned]]_)
**Combat Gear** +1 evil outsider-bane arrows (5), +1 evil outsider-bane holy arrows (5), +1 holy arrows (5), potions of fly (2); **Other Gear** +5 _[[items/Armor/Full plate|full plate]]_, +1 cold iron evil outsider-bane _greatsword_, +1 _shortbow_ with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Str, Con), _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Goggles of Night|goggles of night]]_, _[[items/Wondrous Item/Phylactery of Faithfulness|phylactery of faithfulness]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, 4,760 gp

The _[[feats/Demon Hunter|demon hunter]]_ has sworn to battle the hordes of the Abyss. Though the demons constantly tempt her and try to lead her from her path, she remains resolute—though somewhat paranoid and difficult to befriend because of the number of allies she’s seen slain.