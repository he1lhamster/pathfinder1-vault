---
cssclass: [monsters]
title1: Giant (Fire), Fire Giant Queen
title2: Fire Giant Queen
CR: 19
sources:
- name: Monster Codex
  page: 62
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 204800
race: Fire
classes:
- giant fighter 5
- sorcerer 8
alignment: LE
size: Large
type: humanoid
subtypes:
- fire
- giant
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 31
  touch: 14
  flat_footed: 28
  components:
    armor: 7
    deflection: 2
    dex: 2
    dodge: 1
    natural: 10
    size: -1
HP:
  HP: 326
  long: 15d8+5d10+8d6+204
  HD: 28
saves:
  fort: 22
  ref: 10
  will: 16
  will_other: +1 vs. fear
defensive_abilities:
- bravery +1
- rock catching
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 dispelling furyborn heavy mace +32/+27/+22/+17 (2d6+12/19-20)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
      attack: +1 dispelling furyborn heavy mace
      bonus:
      - 32
      - 27
      - 22
      - 17
  ranged:
  - - text: rock +22 (1d8+15 plus 1d6 fire)
      entries:
      - - damage: 1d8+15
        - damage: 1d6
          type: fire
      attack: rock
      bonus:
      - 22
  special:
  - heated rock
  - rock throwing (120 ft.)
  - weapon training (hammers +1)
space: 10
reach: 10
spells:
  entries:
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 18
  - name: fly
    source: Sorcerer
    level: 3
  - name: bull's strength
    source: Sorcerer
    level: 2
  - superscripts:
    - APG
    name: dust of twilight
    source: Sorcerer
    level: 2
    DC: 17
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 16
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 16
  - name: endure elements
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 16
  - name: summon monster I
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 15
  - name: daze
    source: Sorcerer
    level: 0
    DC: 15
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 15
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 15
  sources:
  - name: Sorcerer
    type: known
    CL: 8
    concentration: 13
    slots:
      4: 4
      3: 6
      2: 7
      1: 8
      0: at-will
    bloodline: arcane
tactics:
  During Combat: The fire giant queen uses a mix of spells and martial power to show
    her dominance in battle.
ability_scores:
  STR: 31
  DEX: 15
  CON: 25
  INT: 17
  WIS: 14
  CHA: 20
BAB: 20
CMB: 31
CMB_other: +33 overrun, +33 sunder
CMD: 46
CMD_other: 48 vs. overrun, 48 vs. sunder
feats:
- name: Cleave
- name: Combat Casting
- name: Critical Focus
- name: Dodge
- name: Enlarge Spell
- name: Eschew Materials
- name: Extend Spell
- name: Great Cleave
- name: Improved Critical (heavy mace)
- name: Improved Overrun
- name: Improved Sunder
- name: Iron Will
- name: Maximize Spell
- name: Power Attack
- name: Quicken Spell
- name: Scribe Scroll
- name: Stunning Critical
- name: Tiring Critical
- name: Weapon Focus (heavy mace)
skills:
  Climb: 22
  Craft (weapons): 11
  Diplomacy: 21
  Intimidate: 16
  Knowledge (arcana): 24
  Perception: 33
  Spellcraft: 34
  Use Magic Device: 36
languages:
- Common
- Giant
- Infernal
special_qualities:
- arcane bond (mace)
- armor training 1
- bloodline arcana (+1 DC for metamagic spells that increase spell level)
- metamagic adept (2/day)
gear:
  combat:
  - potions of cure serious wounds (3)
  - potions of invisibility (2)
  - scrolls of darkness (2)
  - scroll of flame arrow
  - scrolls of lightning bolt (2)
  - scroll of summon monster IV
  - wand of scorching ray (22 charges)
  other:
  - +3 mithral spell storing chain shirt
  - +1 dispelling furyborn heavy mace
  - amulet of natural armor +2
  - belt of physical perfection +2
  - headband of mental prowess +4 (Int, Cha)
  - ring of protection +2
ecology:
  environment: warm mountains
desc_long: Many fire giant queens rule their tribes alongside their husbands, whom
  they wed for life in marriages based on political power rather than romance. Other
  fire giant queens reign alone, bowing to no king and needing no partner to supplement
  their own considerable strength and power.

---

# Giant (Fire), Fire Giant Queen

**Source** Monster Codex pg. 62
**XP** 204,800
Fire giant _[[classes/Fighter|fighter]]_ 5/sorcerer 8

LE Large humanoid (fire, giant)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +33

##### Defense

**AC** 31, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+7 armor, +2 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural, –1 size)
**hp** 326 (28 HD; 15d8+5d10+8d6+204)
**Fort** +22, **Ref** +10, **Will** +16 (+1 vs. _[[universal monster rules/Fear|fear]]_)
**Defensive Abilities** bravery +1, _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** fire
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ _[[items/Weapon Magic Abilities/Furyborn|furyborn]]_ _[[items/Weapon/Heavy mace|heavy mace]]_ +32/+27/+22/+17 (2d6+12/19–20)
**Ranged** rock +22 (1d8+15 plus 1d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** heated rock, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), weapon _[[items/Weapon Magic Abilities/Training|training]]_ (hammers +1)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 8th; concentration +13)
4th (4/day)—_[[spells/Dimension Door|dimension door]]_
3rd (6/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 18), fly
2nd (7/day)—bull’s strength, _[[spells/Dust Of Twilight|dust of twilight]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Color Spray|color spray]]_ (DC 16), _[[spells/Endure Elements|endure elements]]_, _[[spells/Identify|identify]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Summon Monster I|summon monster I]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Flare|flare]]_ (DC 15), _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 15)
**Bloodline** arcane

### Tactics

**During Combat** The fire giant queen uses a mix of spells and martial power to show her dominance in battle.

##### Statistics
**Str** 31, **Dex** 15, **Con** 25, **Int** 17, **Wis** 14, **Cha** 20
**Base Atk** +20; **CMB** +31 (+33 overrun, +33 sunder); **CMD** 46 (48 vs. overrun, 48 vs. sunder)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Enlarge Spell|Enlarge Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_heavy mace_), _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Tiring Critical|Tiring Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_heavy mace_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +22, Craft (weapons) +11, Diplomacy +21, Intimidate +16, Knowledge (arcana) +24, Perception +33, Spellcraft +34, Use Magic Device +36
**Languages** Common, Giant, Infernal
**SQ** arcane bond (mace), armor _training_ 1, bloodline arcana (+1 DC for metamagic spells that increase spell level), metamagic adept (2/day)
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), potions of _invisibility_ (2), scrolls of _[[spells/Darkness|darkness]]_ (2), scroll of _[[spells/Flame Arrow|flame arrow]]_, scrolls of _[[spells/Lightning Bolt|lightning bolt]]_ (2), scroll of _[[spells/Summon Monster IV|summon monster IV]]_, wand of _scorching ray_ (22 charges); **Other Gear** +3 mithral _[[items/Weapon Magic Abilities/Spell Storing|spell storing]]_ _[[items/Armor/Chain shirt|chain shirt]]_, +1 _dispelling_ _furyborn_ _heavy mace_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Perfection +2|belt of physical perfection +2]]_, _[[items/Wondrous Item/Headband of Mental Prowess +4|headband of mental prowess +4]]_ (Int, Cha), _[[items/Ring/Ring of Protection +2|ring of protection +2]]_

##### Ecology

**Environment** warm mountains

##### Description

Many fire giant queens rule their tribes alongside their husbands, whom they wed for life in marriages based on political power rather than romance. Other fire giant queens reign alone, bowing to no _[[npcs/King|king]]_ and needing no partner to supplement their own considerable strength and power.