---
cssclass: [monsters]
title1: Dark Nature Priest
title2: Dark Nature Priest
CR: 17
sources:
- name: NPC Codex
  page: 77
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Halfling
classes:
- druid 18
alignment: NE
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 3
AC:
  AC: 28
  touch: 19
  flat_footed: 24
  components:
    armor: 4
    deflection: 3
    dex: 3
    dodge: 1
    insight: 1
    shield: 5
    size: 1
HP:
  HP: 156
  long: 18d8+72
saves:
  fort: 18
  ref: 13
  will: 20
  other: +2 vs. fear, +4 vs. fey and plant-targeted effects
immunities:
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 quarterstaff +15/+10/+5 (1d4)
      entries:
      - - damage: 1d4
      attack: +1 quarterstaff
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: +1 sling +18/+13/+8 (1d3)
      entries:
      - - damage: 1d3
      attack: +1 sling
      bonus:
      - 18
      - 13
      - 8
  special:
  - wild shape 8/day
spell_like_abilities:
  entries:
  - name: wooden fist
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 18
    concentration: 23
spells:
  entries:
  - name: mass cure critical wounds
    source: Druid
    level: 9
  - is_domain_spell: true
    name: shambler
    source: Druid
    level: 9
  - is_domain_spell: true
    name: control plants
    source: Druid
    level: 8
    DC: 23
  - name: whirlwind
    source: Druid
    level: 8
    count: 2
    DC: 23
  - name: word of recall
    source: Druid
    level: 8
  - is_domain_spell: true
    name: animate plants
    source: Druid
    level: 7
  - name: fire storm
    source: Druid
    level: 7
    DC: 22
  - name: heal
    source: Druid
    level: 7
  - name: true seeing
    source: Druid
    level: 7
  - name: empowered flame strike
    source: Druid
    level: 6
    count: 2
    DC: 19
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: mass cat's grace
    source: Druid
    level: 6
  - is_domain_spell: true
    name: repel wood
    source: Druid
    level: 6
  - name: animal growth
    source: Druid
    level: 5
    DC: 20
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 20
  - name: control winds
    source: Druid
    level: 5
    DC: 20
  - name: stoneskin
    source: Druid
    level: 5
    count: 2
  - is_domain_spell: true
    name: wall of thorns
    source: Druid
    level: 5
  - is_domain_spell: true
    name: command plants
    source: Druid
    level: 4
    DC: 19
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    count: 2
    DC: 19
  - name: freedom of movement
    source: Druid
    level: 4
  - name: spike stones
    source: Druid
    level: 4
    DC: 19
  - name: dominate animal
    source: Druid
    level: 3
    DC: 18
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - is_domain_spell: true
    name: plant growth
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
    count: 2
  - is_domain_spell: true
    name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: fog cloud
    source: Druid
    level: 2
  - name: hold animal
    source: Druid
    level: 2
    DC: 17
  - name: spider climb
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - is_domain_spell: true
    name: entangle
    source: Druid
    level: 1
    DC: 16
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: know direction
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 18
    concentration: 23
    slots:
      0: at-will
    domains:
    - plant
tactics:
  Before Combat: The druid casts liveoak and shambler on a regular basis, and always
    has a retinue of 1d4+2 advanced shambling mounds and a treant with her.
  During Combat: The druid detests trespassers. She begins combat by sending her shambling
    mounds and treant into melee and summoning a storm giant. She then summons a tyrannosaurus
    and casts animal growth on it, and spends the next few rounds buffing her summoned
    creatures with barkskin, mass cat's grace, and greater magic fang. She then casts
    offensive spells and drinks her potion of haste before wild shaping into a Huge
    elemental and moving into melee.
ability_scores:
  STR: 8
  DEX: 16
  CON: 16
  INT: 12
  WIS: 20
  CHA: 10
BAB: 13
CMB: 11
CMD: 29
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Empower Spell
- name: Natural Spell
- name: Spell Focus (conjuration)
- name: Vital Strike
- name: Weapon Focus (quarterstaff)
skills:
  Acrobatics: 4
    when jumping: 0
  Climb: 8
  Fly: 12
  Handle Animal: 6
  Heal: 13
  Knowledge (geography): 14
  Knowledge (nature): 16
  Linguistics: 5
  Perception: 24
  Ride: 9
  Spellcraft: 19
  Survival: 19
  Swim: 7
languages:
- Aquan
- Auran
- Common
- Druidic
- Halfling
- Ignan
- Sylvan
- Terran
special_qualities:
- a thousand faces
- bramble armor (1d6+9, 18 rounds/day)
- nature bond (Plant domain)
- nature sense
- timeless body
- trackless step
- wild empathy +18
- woodland stride
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of haste
  - wand of ice storm (3 charges)
  other:
  - +2 leather armor
  - +3 heavy wild darkwood wooden shield
  - +1 quarterstaff
  - +1 sling with 20 bullets
  - cloak of resistance +3
  - dusty rose prism ioun stone
  - headband of inspired wisdom +4
  - ring of protection +3
  - backpack
  - everburning torch
  - holly and mistletoe
  - silk rope (50 ft.)
  - spell component pouch
  - 96 gp
desc_long: These dark nature priests do not nurture their home, but rather spread
  disease, filth, and hate throughout humanoid communities on behalf of an enraged
  and exploited landscape.

---

# Dark Nature Priest

**Source** NPC Codex pg. 77
**XP** 102,400
Halfling _[[classes/Druid|druid]]_ 18

NE Small humanoid (halfling)
**Init** +3; **Senses** Perception +24

##### Defense

**AC** 28, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +3 deflection, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 insight, +5 _[[spells/Shield|shield]]_, +1 size)
**hp** 156 (18d8+72)
**Fort** +18, **Ref** +13, **Will** +20; +2 vs. _[[universal monster rules/Fear|fear]]_, +4 vs. fey and plant-targeted effects
**Immune** poison

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +15/+10/+5 (1d4)
**Ranged** +1 _[[items/Weapon/Sling|sling]]_ +18/+13/+8 (1d3)
**Special Attacks** wild shape 8/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +23)
8/day—wooden fist
**_Druid_ Spells Prepared **(CL 18th; concentration +23)
9th—mass _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Shambler|shambler]]_
8th—control plantsD (DC 23), _[[universal monster rules/Whirlwind|whirlwind]]_ (2, DC 23), _[[spells/Word of Recall|word of recall]]_
7th—_[[spells/Animate Plants|animate plants]]_, _[[spells/Fire Storm|fire storm]]_ (DC 22), _[[spells/Heal|heal]]_, _[[spells/True Seeing|true seeing]]_
6th—empowered _[[spells/Flame Strike|flame strike]]_ (2, DC 19), greater _[[spells/Dispel Magic|dispel magic]]_, mass cat’s _[[spells/Grace|grace]]_, _[[spells/Repel Wood|repel wood]]_
5th—_[[spells/Animal Growth|animal growth]]_ (DC 20), _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Control Winds|control winds]]_ (DC 20), _[[spells/Stoneskin|stoneskin]]_ (2), _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Command|command]]_ plantsD (DC 19), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _flame strike_ (2, DC 19), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spike Stones|spike stones]]_ (DC 19)
3rd—_[[spells/Dominate Animal|dominate animal]]_ (DC 18), greater _[[spells/Magic Fang|magic fang]]_ (2), _[[spells/Plant Growth|plant growth]]_, _[[spells/Protection from Energy|protection from energy]]_ (2)
2nd—barkskinD (3), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Hold Animal|hold animal]]_ (DC 17), _[[spells/Spider Climb|spider climb]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[conditions/Entangled|entangleD]]_ (DC 16), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Know Direction|know direction]]_, light, _[[spells/Read Magic|read magic]]_, stabilize
**D **Domain spell; **Domain **Plant

### Tactics

**Before Combat **The _druid_ casts _[[spells/Liveoak|liveoak]]_ and _shambler_ on a regular basis, and always has a retinue of 1d4+2 advanced shambling mounds and a _[[monsters/Treant|treant]]_ with her.
**During Combat **The _druid_ detests trespassers. She begins combat by _[[spells/Sending|sending]]_ her shambling mounds and _treant_ into melee and summoning a storm giant. She then summons a tyrannosaurus and casts _animal growth_ on it, and spends the next few rounds buffing her summoned creatures with _[[spells/Barkskin|barkskin]]_, mass cat’s _grace_, and greater _magic fang_. She then casts offensive spells and drinks her potion of _[[spells/Haste|haste]]_ before wild shaping into a Huge elemental and moving into melee.

##### Statistics
**Str** 8, **Dex** 16, **Con** 16, **Int** 12, **Wis** 20, **Cha** 10
**Base Atk** +13; **CMB** +11; **CMD** 29
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_quarterstaff_)
**Skills** Acrobatics +4 (+0 when jumping), _[[universal monster rules/Climb|Climb]]_ +8, Fly +12, Handle Animal +6, _Heal_ +13, Knowledge (geography) +14, Knowledge (nature) +16, Linguistics +5, Perception +24, Ride +9, Spellcraft +19, Survival +19, Swim +7
**Languages** Aquan, Auran, Common, Druidic, Halfling, Ignan, Sylvan, Terran
**SQ** a thousand faces, bramble armor (1d6+9, 18 rounds/day), nature bond (Plant domain), nature sense, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +18, woodland stride
**Combat Gear** potions of _cure serious wounds_ (2), potion of _haste_, wand of _[[spells/Ice Storm|ice storm]]_ (3 charges); **Other Gear** +2 _[[items/Armor/Leather armor|leather armor]]_, +3 heavy wild darkwood wooden _shield_, +1 _quarterstaff_, +1 _sling_ with 20 bullets, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, backpack, _[[items/Mundane/Everburning torch|everburning torch]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.), _[[items/Mundane/Spell component pouch|spell component pouch]]_, 96 gp

These dark nature priests do not nurture their home, but rather spread disease, filth, and hate throughout humanoid communities on behalf of an enraged and exploited landscape.