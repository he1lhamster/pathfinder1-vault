---
cssclass: [monsters]
title1: Carousing Champion
title2: Carousing Champion
CR: 5
sources:
- name: NPC Codex
  page: 47
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Halfling
classes:
- cleric of Cayden Cailean 6
alignment: CN
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 1
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 7
    dex: 1
    size: 1
HP:
  HP: 54
  long: 6d8+24
saves:
  fort: 8
  ref: 4
  will: 9
  other: +2 vs. fear
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 heavy mace +6 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: +1 heavy mace
      bonus:
      - 6
  ranged:
  - - text: light crossbow +7 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 7
  special:
  - channel positive energy 7/day (DC 15, 3d6)
spell_like_abilities:
  entries:
  - name: dazing touch
    source: default
    freq: 6/day
  - name: touch of chaos
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 6
    concentration: 9
spells:
  entries:
  - name: locate object
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: suggestion
    source: Cleric
    level: 3
  - name: summon monster III
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: calm emotions
    source: Cleric
    level: 2
    DC: 15
  - name: eagle's splendor
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 15
  - name: zone of truth
    source: Cleric
    level: 2
    DC: 15
  - name: bless water
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: charm person
    source: Cleric
    level: 1
    DC: 14
  - name: comprehend languages
    source: Cleric
    level: 1
  - name: detect undead
    source: Cleric
    level: 1
  - name: hide from undead
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
    domains:
    - chaos
    - charm
tactics:
  During Combat: The cleric tries to persuade living, intelligent opponents to stop
    fighting and discuss a peaceful solution over a drink, using calm emotions, charm
    person, or suggestion if necessary. When fighting undead, he casts eagle's splendor
    to improve his channel energy ability, and uses his potion and scroll if the battle
    goes poorly.
ability_scores:
  STR: 11
  DEX: 12
  CON: 14
  INT: 8
  WIS: 16
  CHA: 14
BAB: 4
CMB: 3
CMD: 14
feats:
- name: Extra Channel
- name: Toughness
- name: Turn Undead
skills:
  Acrobatics: 0
  Climb: -1
  Diplomacy: 8
  Heal: 9
  Perception: 5
languages:
- Common
- Halfling
special_qualities:
- aura
gear:
  combat:
  - potion of haste
  - scroll of bull's strength
  other:
  - +1 breastplate
  - +1 heavy mace
  - light crossbow with masterwork bolts (20)
  - silver holy symbol
  - 393 gp
desc_long: The carousing champion serves the god of freedom, bravery, and ale, and
  uses his significant abilities to bring happiness to common folk and stand up against
  oppression of all sorts.

---

# Carousing Champion

**Source** NPC Codex pg. 47
**XP** 1,600
Halfling _[[classes/Cleric|cleric]]_ of Cayden Cailean 6

CN Small humanoid (halfling)
**Init** +1; **Senses** Perception +5

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 armor, +1 Dex, +1 size)
**hp** 54 (6d8+24)
**Fort** +8, **Ref** +4, **Will** +9; +2 vs. _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +6 (1d6+1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +7 (1d6/19–20)
**Special Attacks** channel positive energy 7/day (DC 15, 3d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
6/day—dazing touch, touch of chaos
**_Cleric_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Locate Object|locate object]]_, _[[spells/Searing Light|searing light]]_, _[[spells/Suggestion|suggestion]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd—aid, calm emotionsD (DC 15), _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Sound Burst|sound burst]]_ (DC 15), _[[spells/Zone of Truth|zone of truth]]_ (DC 15)
1st—_[[spells/Bless Water|bless water]]_, charm personD (DC 14), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Undead|detect undead]]_, _[[spells/Hide from Undead|hide from undead]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **Chaos, Charm

### Tactics

**During Combat **The _cleric_ tries to persuade living, intelligent opponents to stop fighting and discuss a _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_ solution over a drink, using _[[spells/Calm Emotions|calm emotions]]_, _[[spells/Charm Person|charm person]]_, or _suggestion_ if necessary. When fighting undead, he casts _eagle_’s splendor to improve his channel energy ability, and uses his potion and scroll if the battle goes poorly.

##### Statistics
**Str** 11, **Dex** 12, **Con** 14, **Int** 8, **Wis** 16, **Cha** 14
**Base Atk** +4; **CMB** +3; **CMD** 14
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Turn Undead|Turn Undead]]_
**Skills** Acrobatics +0, _[[universal monster rules/Climb|Climb]]_ –1, Diplomacy +8, _[[spells/Heal|Heal]]_ +9, Perception +5
**Languages** Common, Halfling
**SQ** aura
**Combat Gear** potion of _[[spells/Haste|haste]]_, scroll of bull’s strength; **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _heavy mace_, _light crossbow_ with masterwork bolts (20), silver holy symbol, 393 gp

The _[[npcs/Carousing Champion|carousing champion]]_ serves the god of _[[spells/Freedom|freedom]]_, bravery, and ale, and uses his significant abilities to bring happiness to common folk and stand up against oppression of all sorts.