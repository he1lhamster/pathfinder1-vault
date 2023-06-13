---
cssclass: [monsters]
title1: Boggard, Boggard Prophet
title2: Boggard Prophet
CR: 5
sources:
- name: Monster Codex
  page: 13
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Boggard
classes:
- sorcerer 4
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 13
  touch: 10
  flat_footed: 13
  components:
    deflection: 1
    dex: -1
    natural: 3
HP:
  HP: 59
  long: 3d8+4d6+32
  HD: 7
saves:
  fort: 8
  ref: 2
  will: 5
  other: +2 vs. poison
resistances:
  electricity: 5
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: 2 claws +10 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 10
    - text: tongue +4 (plus sticky tongue)
      entries:
      - - effect: plus sticky tongue
      attack: tongue
      bonus:
      - 4
  ranged:
  - - text: sling +3 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: sling
      bonus:
      - 3
  special:
  - claws (1d6+5, 5 rounds/day)
  - terrifying croak (DC 15)
spells:
  entries:
  - name: summon monster II
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 13
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 13
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: summon monster I
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 12
  - name: message
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 4
    concentration: 6
    slots:
      2: 4
      1: 7
      0: at-will
    bloodline: abyssal
ability_scores:
  STR: 20
  DEX: 9
  CON: 16
  INT: 10
  WIS: 9
  CHA: 14
BAB: 4
CMB: 9
CMD: 19
feats:
- name: Combat Casting
- name: Eschew Materials
- name: Improved Initiative
- name: Toughness
- name: Weapon Focus (claw)
skills:
  Acrobatics: 2
    when jumping: 18
  Intimidate: 6
  Knowledge (planes): 5
  Perception: 3
  Spellcraft: 7
  Stealth: 0
    in swamps: 8
  Swim: 13
  Use Magic Device: 9
languages:
- Boggard
special_qualities:
- bloodline arcana (summoned creatures gain DR 2/good)
- hold breath
- swamp stride
gear:
  combat:
  - potion of invisibility
  - scrolls of blindness/deafness (2)
  - scroll of enlarge person
  other:
  - sling with 10 bullets
  - cloak of resistance +1
  - elixir of vision
  - ring of protection +1
  - 75 gp
ecology:
  environment: temperate marshes
desc_long: These casters are often the children of the priest-king.

---

# Boggard, Boggard Prophet

**Source** Monster Codex pg. 13
**XP** 1,600
_[[monsters/Boggard|Boggard]]_ _[[classes/Sorcerer|sorcerer]]_ 4
CE Medium humanoid (_boggard_)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +3

##### Defense

**AC** 13, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+1 _[[spells/Deflection|deflection]]_, –1 Dex, +3 natural)
**hp** 59 (7 HD; 3d8+4d6+32)
**Fort** +8, **Ref** +2, **Will** +5; +2 vs. poison
**Resist** electricity 5

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** 2 claws +10 (1d4+5), tongue +4 (plus _[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** _[[items/Weapon/Sling|sling]]_ +3 (1d4+5)
**Special Attacks** claws (1d6+5, 5 rounds/day), terrifying croak (DC 15)
**_Sorcerer_ Spells Known **(CL 4th; concentration +6)
2nd (4/day)—_[[spells/Summon Monster II|summon monster II]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (DC 13), _[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Mage Armor|mage armor]]_, _[[spells/Summon Monster I|summon monster I]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 12), _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline** abyssal

##### Statistics
**Str** 20, **Dex** 9, **Con** 16, **Int** 10, **Wis** 9, **Cha** 14
**Base Atk** +4; **CMB** +9; **CMD** 19
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +2 (+18 when jumping), Intimidate +6, Knowledge (planes) +5, Perception +3, Spellcraft +7, Stealth +0 (+8 in swamps), Swim +13, Use Magic Device +9
**Languages** _Boggard_
**SQ** bloodline arcana (summoned creatures gain DR 2/good), _[[universal monster rules/Hold Breath|hold breath]]_, swamp stride
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, scrolls of blindness/deafness (2), scroll of _[[spells/Enlarge Person|enlarge person]]_; **Other Gear** _sling_ with 10 bullets, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Elixir of Vision|elixir of vision]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 75 gp

##### Ecology

**Environment** temperate marshes

##### Description

These casters are often the children of the priest-king.