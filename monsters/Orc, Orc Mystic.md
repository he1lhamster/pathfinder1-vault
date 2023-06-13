---
cssclass: [monsters]
title1: Orc, Orc Mystic
title2: Orc Mystic
CR: 2
sources:
- name: Monster Codex
  page: 167
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 600
race: Orc
classes:
- cleric 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- orc
initiative:
  bonus: -1
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 9
  flat_footed: 15
  components:
    armor: 6
    dex: -1
HP:
  HP: 20
  long: 3d8+3
saves:
  fort: 5
  ref: 1
  will: 5
defensive_abilities:
- ferocity
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: battleaxe +5 (1d8+3/×3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: battleaxe
      bonus:
      - 5
  ranged:
  - - text: javelin +1 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: javelin
      bonus:
      - 1
  special:
  - channel negative energy 4/day (DC 12, 2d6)
spell_like_abilities:
  entries:
  - name: copycat
    source: default
    freq: 4/day
    other: 3 rounds
  - name: touch of evil
    source: default
    freq: 4/day
    other: 1 rounds
  sources:
  - name: default
    CL: 3
    concentration: 4
spells:
  entries:
  - name: bull's strength
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 12
  - name: magic weapon
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    DC: 12
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 11
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 3
    concentration: 4
    slots:
      0: at-will
    domains:
    - evil
    - trickery
tactics:
  Before Combat: The mystic casts bull's strength on one ally and magic weapon on
    one ally's weapon.
  During Combat: After casting invisibility on himself, the mystic gets into an advantageous
    position while his allies battle the enemy. He typically casts bane first, followed
    by murderous command, targeting whichever opponent looks the strongest.
ability_scores:
  STR: 17
  DEX: 8
  CON: 12
  INT: 8
  WIS: 13
  CHA: 12
BAB: 2
CMB: 5
CMD: 14
feats:
- name: Combat Casting
- name: Skill Focus (Stealth)
skills:
  Knowledge (religion): 4
  Perception: 2
  Stealth: 4
languages:
- Common
- Orc
special_qualities:
- weapon familiarity
gear:
  combat:
  - scroll of sound burst
  - scroll of summon monster II
  other:
  - breastplate
  - battleaxe
  - javelins (4)
  - cloak of resistance +1
  - wooden holy symbol
  - 135 gp
ecology:
  environment: temperate hills, mountains, or underground
desc_long: |-
  Orcs worship in a different way from many other races, adhering to a polytheistic tradition that varies by tribe. These gods speak to the orcs' love of fire, destruction, slavery, and the like, but the particular offerings and prayers one tribe uses for the Blood God might be the same ones a different tribe gives to the Destroyer. Orcs take little notice of these distinctions. There's no point in religious squabbling when there are villages to raid and people to slaughter.

   There's seldom more than one full mystic in a tribe, though the mystic may teach the ways of divine magic to multiple apprentices. These apprentices are practically slaves to the mystic, and face beatings and starvation during their tutelage. It's not uncommon for a mystic to murder overly ambitious apprentices who seek to usurp his position in the tribe.

---

# Orc, Orc Mystic

**Source** Monster Codex pg. 167
**XP** 600
_[[monsters/Orc|Orc]]_ _[[classes/Cleric|cleric]]_ 3
CE Medium humanoid (_orc_)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 15, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+6 armor, –1 Dex)
**hp** 20 (3d8+3)
**Fort** +5, **Ref** +1, **Will** +5
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Battleaxe|battleaxe]]_ +5 (1d8+3/×3)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +1 (1d6+3)
**Special Attacks** channel negative energy 4/day (DC 12, 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
4/day—copycat (3 rounds), _[[feats/Touch Of Evil|touch of evil]]_ (1 rounds)
**_Cleric_ Spells Prepared **(CL 3rd; concentration +4)
2nd—bull’s strength, _[[spells/Invisibility|invisibility]]_
1st—_[[spells/Bane|bane]]_ (DC 12), _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Murderous Command|murderous command]]_ (DC 12), _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 11), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Evil, Trickery

### Tactics

**Before Combat** The mystic casts bull’s strength on one ally and _magic weapon_ on one ally’s weapon.
 **During Combat **After casting _invisibility_ on himself, the mystic gets into an advantageous position while his allies battle the enemy. He typically casts _bane_ first, followed by _murderous command_, targeting whichever opponent looks the strongest.

##### Statistics
**Str** 17, **Dex** 8, **Con** 12, **Int** 8, **Wis** 13, **Cha** 12
**Base Atk** +2; **CMB** +5; **CMD** 14
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Knowledge (religion) +4, Perception +2, Stealth +4
**Languages** Common, _Orc_
**SQ** weapon familiarity
**Combat Gear** scroll of _[[spells/Sound Burst|sound burst]]_, scroll of _[[spells/Summon Monster II|summon monster II]]_; **Other Gear** _[[items/Armor/Breastplate|breastplate]]_, _battleaxe_, javelins (4), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, wooden holy symbol, 135 gp

##### Ecology

**Environment** temperate hills, mountains, or underground

##### Description

Orcs worship in a different way from many other races, adhering to a polytheistic tradition that varies by tribe. These gods speak to the orcs’ love of fire, _[[spells/Destruction|destruction]]_, slavery, and the like, but the particular offerings and prayers one tribe uses for the Blood God might be the same ones a different tribe gives to the Destroyer. Orcs take little notice of these distinctions. There’s no point in religious squabbling when there are villages to raid and people to slaughter.

There’s seldom more than one full mystic in a tribe, though the mystic may teach the ways of divine magic to multiple apprentices. These apprentices are practically slaves to the mystic, and face beatings and starvation during their tutelage. It’s not uncommon for a mystic to murder overly ambitious apprentices who seek to usurp his position in the tribe.