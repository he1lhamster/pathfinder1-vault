---
cssclass: [monsters]
title1: Mercenary Healer
title2: Mercenary Healer
CR: 1/2
sources:
- name: NPC Codex
  page: 44
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 200
race: Human
classes:
- cleric of Abadar 1
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    armor: 6
    dex: 1
HP:
  HP: 9
  long: 1d8+1
saves:
  fort: 3
  ref: 1
  will: 4
speeds:
  base: 30
attacks:
  melee:
  - - text: morningstar -1 (1d8-1)
      entries:
      - - damage: 1d8-1
      attack: morningstar
      bonus:
      - -1
  ranged:
  - - text: light crossbow +2 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 2
  special:
  - channel negative energy 6/day (DC 13, 1d6)
spell_like_abilities:
  entries:
  - name: inspiring word
    source: default
    freq: 5/day
    other: 1 round
  sources:
  - name: default
    CL: 1
    concentration: 3
spells:
  entries:
  - name: cure light wounds
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: longstrider
    source: Cleric
    level: 1
  - name: protection from good
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    concentration: 3
    slots:
      0: at-will
    domains:
    - nobility
    - travel
tactics:
  During Combat: The cleric uses channeled energy, tanglefoot bags, and longstrider
    to escape.
ability_scores:
  STR: 8
  DEX: 12
  CON: 13
  INT: 10
  WIS: 14
  CHA: 17
BAB: 0
CMB: -1
CMD: 10
feats:
- name: Selective Channeling
- name: Weapon Focus (light crossbow)
skills:
  Appraise: 4
  Diplomacy: 7
  Knowledge (religion): 4
  Spellcraft: 4
  Perception: 2
languages:
- Common
special_qualities:
- aura
- +10 base speed from Travel domain
- agile feet (5/day)
gear:
  combat:
  - potion of cure light wounds
  - tanglefoot bags (2)
  other:
  - chainmail
  - light crossbow with 20 bolts
  - morningstar
  - silver unholy symbol
  - 22 gp
desc_long: Mercenary healers exploit loopholes in laws for their own profit.

---

# Mercenary Healer

**Source** NPC Codex pg. 44
**XP** 200
Human _[[classes/Cleric|cleric]]_ of Abadar 1

LE Medium humanoid (human)
**Init** +1; **Senses** Perception +2

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 armor, +1 Dex)
**hp** 9 (1d8+1)
**Fort** +3, **Ref** +1, **Will** +4

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Morningstar|morningstar]]_ –1 (1d8–1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +2 (1d8/19–20)
**Special Attacks** channel negative energy 6/day (DC 13, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +3)
5/day—inspiring word (1 round)
**_Cleric_ Spells Prepared **(CL 1st; concentration +3)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domains **Nobility, Travel

### Tactics

**During Combat **The _cleric_ uses channeled energy, tanglefoot bags, and _longstrider_ to escape.

##### Statistics
**Str** 8, **Dex** 12, **Con** 13, **Int** 10, **Wis** 14, **Cha** 17
**Base Atk** +0; **CMB** –1; **CMD** 10
**Feats** _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light crossbow_)
**Skills** Appraise +4, Diplomacy +7, Knowledge (religion) +4, Spellcraft +4
**Languages** Common
**SQ** aura, +10 base speed from Travel domain, _[[items/Weapon Magic Abilities/Agile|agile]]_ feet (5/day)
**Combat Gear** potion of _cure light wounds_, tanglefoot bags (2); **Other Gear** _[[items/Armor/Chainmail|chainmail]]_, _light crossbow_ with 20 bolts, _morningstar_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 22 gp

Mercenary healers exploit loopholes in laws for their own profit.