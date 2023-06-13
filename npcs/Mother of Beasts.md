---
cssclass: [monsters]
title1: Mother of Beasts
title2: Mother of Beasts
CR: 9
sources:
- name: NPC Codex
  page: 51
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 6400
race: Human
classes:
- cleric of Lamashtu 10
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 3
AC:
  AC: 21
  touch: 10
  flat_footed: 21
  other: +1 vs. good opponents
  components:
    armor: 11
    deflection: 1
    dex: -1
HP:
  HP: 78
  long: 10d8+30
saves:
  fort: 10
  ref: 3
  will: 12
  other: +2 vs. good opponents
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 falchion +11/+6 (2d4+5/18-20)
      entries:
      - - damage: 2d4+5
          crit_range: 18-20
      attack: +1 falchion
      bonus:
      - 11
      - 6
  special:
  - aura of madness (DC 19, 10 rounds/day)
  - channel negative energy 4/day (DC 16, 5d6)
  - might of the gods (+10, 10 rounds/day)
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 7/day
    other: '+5'
  - name: vision of madness
    source: default
    freq: 7/day
    other: +/-5
  sources:
  - name: default
    CL: 10
    concentration: 14
spells:
  entries:
  - name: flame strike
    source: Cleric
    level: 5
    DC: 19
  - is_domain_spell: true
    name: righteous might
    source: Cleric
    level: 5
  - name: summon monster V
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: confusion
    source: Cleric
    level: 4
    DC: 18
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: summon monster IV
    source: Cleric
    level: 4
    count: 2
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 18
  - name: blindness/deafness
    source: Cleric
    level: 3
  - name: magic circle against good
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - name: summon monster III
    source: Cleric
    level: 3
  - name: water breathing
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: bull's strength
    source: Cleric
    level: 2
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: darkness
    source: Cleric
    level: 2
  - name: shield other
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 16
  - name: summon monster II
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 15
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 15
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: enlarge person
    source: Cleric
    level: 1
    DC: 15
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 10
    concentration: 14
    slots:
      0: at-will
    domains:
    - madness
    - strength
tactics:
  Before Combat: The cleric casts magic circle against good and magic vestment.
  During Combat: The cleric drinks a potion of invisibility, then uses summon monster
    V and summon monster IV to overwhelm opponents, and attacks with flame strike,
    casting righteous might before entering melee.
  Base Statistics: Without magic circle against good and magic vestment, the cleric's
    statistics are AC 20, touch 10, flat-footed 20.
ability_scores:
  STR: 16
  DEX: 8
  CON: 14
  INT: 10
  WIS: 18
  CHA: 12
BAB: 7
CMB: 10
CMD: 20
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Heavy Armor Proficiency
- name: Improved Initiative
- name: Power Attack
- name: Spell Focus (conjuration)
skills:
  Handle Animal: 11
  Heal: 8
  Knowledge (nature): 1
  Knowledge (religion): 6
  Perception: 14
  Spellcraft: 8
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potions of invisibility (2)
  other:
  - +1 full plate
  - +1 falchion
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +1
  - silver unholy symbol
  - 110 gp
desc_long: The mother of beasts serves the goddess of madness and monsters. She looks
  after horrible creatures and summons extraplanar beings to defend herself and her
  pets.

---

# Mother of Beasts

**Source** NPC Codex pg. 51
**XP** 6,400
Human _[[classes/Cleric|cleric]]_ of Lamashtu 10
CE Medium humanoid (human)
**Init** +3; **Senses** Perception +14

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+11 armor, +1 _[[spells/Deflection|deflection]]_, –1 Dex); +1 vs. good opponents
**hp** 78 (10d8+30)
**Fort** +10, **Ref** +3, **Will** +12; +2 vs. good opponents

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Falchion|falchion]]_ +11/+6 (2d4+5/18–20)
**Special Attacks** aura of madness (DC 19, 10 rounds/day), channel negative energy 4/day (DC 16, 5d6), might of the gods (+10, 10 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
7/day—strength surge (+5), _[[spells/Vision|vision]]_ of madness (+/–5)
**_Cleric_ Spells Prepared **(CL 10th; concentration +14)
5th—_[[spells/Flame Strike|flame strike]]_ (DC 19), _[[spells/Righteous Might|righteous might]]_, _[[spells/Summon Monster V|summon monster V]]_
4th—confusionD (DC 18), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Summon Monster IV|summon monster IV]]_ (2), _[[spells/Unholy Blight|unholy blight]]_ (DC 18)
3rd—blindness/deafness, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Summon Monster III|summon monster III]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—bull’s strength, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Darkness|darkness]]_, _[[spells/Shield Other|shield other]]_, _[[spells/Silence|silence]]_ (DC 16), _[[spells/Summon Monster II|summon monster II]]_
1st—_[[spells/Bane|bane]]_ (DC 15), _[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 15), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, enlarge personD (DC 15)
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mending|mending]]_
**D **Domain spell; **Domains **Madness, Strength

### Tactics

**Before Combat **The _cleric_ casts _magic circle against good_ and _magic vestment_.
**During Combat **The _cleric_ drinks a potion of _[[spells/Invisibility|invisibility]]_, then uses _summon monster V_ and _summon monster IV_ to _[[feats/Overwhelm|overwhelm]]_ opponents, and attacks with _flame strike_, casting _righteous might_ before entering melee.
**Base Statistics **Without _magic circle against good_ and _magic vestment_, the _cleric_’s statistics are **AC **20, touch 10, _flat-footed_ 20.

##### Statistics
**Str** 16, **Dex** 8, **Con** 14, **Int** 10, **Wis** 18, **Cha** 12
**Base Atk** +7; **CMB** +10; **CMD** 20
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration)
**Skills** Handle Animal +11, _[[spells/Heal|Heal]]_ +8, Knowledge (nature) +1, Knowledge (religion) +6, Perception +14, Spellcraft +8
**Languages** Common
**SQ** aura
**Combat Gear** potions of _invisibility_ (2); **Other Gear** +1 _[[items/Armor/Full plate|full plate]]_, +1 _falchion_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 110 gp

The _[[npcs/Mother of Beasts|mother of beasts]]_ serves the goddess of madness and monsters. She looks after horrible creatures and summons extraplanar beings to defend herself and her pets.